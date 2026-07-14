#!/usr/bin/env python3
"""Tests for metadata/skill_specs.json generation."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import build_skill_specs  # noqa: E402
from skill_spec_v2 import BASELINE_INHERITS, SpecValidationError  # noqa: E402


SKILL_TEXT = """---
name: {name}
description: "Use when {description}."
practice_area: {area}
task_type: {task_type}
jurisdictions: []
risk_level: {risk}
requires_attorney_review: true
inputs:
  - "The source document"
  - "Optional: the client objective"
outputs:
  - "Structured summary"
related_skills: []
tags:
  - test
---

# {name}

## Purpose

Draft work product for attorney review.

## Use When

- Use this test skill.

## Required Inputs

- The source document.

## Do Not Use When

- A different workflow applies.

## Legal Safety Rules

- Do not invent law or facts.

## Workflow

1. Review the source.

## Output Format

1. Structured summary.

## Attorney Verification Checklist

- [ ] Verify the draft.
"""


class RegistryFixture:
    def __init__(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "metadata").mkdir()
        for path in BASELINE_INHERITS:
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(f"# {target.stem}\n", encoding="utf-8")
        deadline = self.root / "core" / "jurisdiction-and-deadline-gates.md"
        deadline.write_text("# Gates\n", encoding="utf-8")

        self.alpha = self._skill(
            "contracts",
            "alpha-review",
            "Alpha Review",
            "reviewing alpha agreements",
            "review",
            "medium",
        )
        self.beta = self._skill(
            "privacy",
            "beta-intake",
            "Beta Intake",
            "organizing beta incidents with a deadline",
            "intake",
            "critical",
        )
        (self.beta / "SPEC.json").write_text(
            json.dumps(
                {
                    "schema_version": "2.0",
                    "skill_id": "privacy/beta-intake",
                    "gates": {
                        "custom": [
                            {
                                "id": "immediate-escalation",
                                "condition": "Any beta incident is reported.",
                                "action": "stop-and-escalate",
                                "reason": "The matter is time-sensitive.",
                            }
                        ]
                    },
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    def _skill(
        self,
        area: str,
        slug: str,
        name: str,
        description: str,
        task_type: str,
        risk: str,
    ) -> Path:
        directory = self.root / "skills" / area / slug
        directory.mkdir(parents=True)
        (directory / "SKILL.md").write_text(
            SKILL_TEXT.format(
                name=name,
                description=description,
                area=area,
                task_type=task_type,
                risk=risk,
            ),
            encoding="utf-8",
        )
        return directory

    def close(self) -> None:
        self.tempdir.cleanup()


class TestBuildSkillSpecs(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = RegistryFixture()

    def tearDown(self) -> None:
        self.fixture.close()

    def test_collects_every_skill_in_stable_order(self):
        data = build_skill_specs.collect_skill_specs(self.fixture.root)
        self.assertEqual(data["schema_version"], "2.0")
        self.assertEqual(data["skill_count"], 2)
        self.assertEqual(data["custom_spec_count"], 1)
        self.assertEqual(data["legacy_compiled_count"], 1)
        self.assertEqual(data["custom_specs_by_practice_area"], {"privacy": 1})
        self.assertEqual(
            [item["skill_id"] for item in data["skills"]],
            ["contracts/alpha-review", "privacy/beta-intake"],
        )
        beta = data["skills"][1]
        self.assertTrue(beta["has_custom_spec"])
        self.assertEqual(
            beta["gates"]["custom"][0]["id"], "immediate-escalation"
        )
        self.assertTrue(beta["gates"]["deadline"]["required"])
        self.assertFalse(beta["gates"]["deadline"]["calculation_allowed"])

    def test_render_output_is_deterministic_json(self):
        data = build_skill_specs.collect_skill_specs(self.fixture.root)
        first = build_skill_specs.render_output(data)
        second = build_skill_specs.render_output(data)
        self.assertEqual(first, second)
        parsed = json.loads(first)
        self.assertEqual(parsed["skill_count"], 2)
        self.assertTrue(first.endswith("\n"))

    def test_write_output_check_detects_drift(self):
        self.assertFalse(build_skill_specs.write_output(self.fixture.root, check=True))
        self.assertTrue(build_skill_specs.write_output(self.fixture.root, check=False))
        self.assertTrue(build_skill_specs.write_output(self.fixture.root, check=True))
        output = self.fixture.root / "metadata" / "skill_specs.json"
        output.write_text("{}\n", encoding="utf-8")
        self.assertFalse(build_skill_specs.write_output(self.fixture.root, check=True))

    def test_invalid_custom_sidecar_fails_generation(self):
        (self.fixture.beta / "SPEC.json").write_text(
            json.dumps(
                {
                    "schema_version": "2.0",
                    "skill_id": "privacy/beta-intake",
                    "gates": {"deadline": {"calculation_allowed": True}},
                }
            ),
            encoding="utf-8",
        )
        with self.assertRaises(SpecValidationError):
            build_skill_specs.collect_skill_specs(self.fixture.root)


if __name__ == "__main__":
    unittest.main()
