#!/usr/bin/env python3
"""Tests for deterministic AgentCounsel context metrics."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import generate_context_metrics as metrics  # noqa: E402


class ContextMetricsFixture:
    def __init__(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "metadata").mkdir()
        skill_path = self.root / "skills" / "contracts" / "nda-review" / "SKILL.md"
        skill_path.parent.mkdir(parents=True)
        template_path = skill_path.parent / "templates" / "risk-table.md"
        template_path.parent.mkdir()
        reference_path = self.root / "skills" / "contracts" / "references" / "red-flags.md"
        reference_path.parent.mkdir(parents=True)

        skill_path.write_text(
            """# NDA Review

## Workflow

Use `skills/contracts/references/red-flags.md` and `skills/contracts/nda-review/templates/risk-table.md`.

## Output Format

1. Triage rating.
2. Risk table.
3. Verification items.
""",
            encoding="utf-8",
        )
        template_path.write_text("# Risk Table\n", encoding="utf-8")
        reference_path.write_text("# Red Flags\n", encoding="utf-8")
        core_path = self.root / "core" / "legal-work-product.md"
        core_path.parent.mkdir()
        core_path.write_text("# Legal Work Product\n", encoding="utf-8")

        index = {
            "skills": [
                {
                    "id": "contracts/nda-review",
                    "title": "NDA Review",
                    "path": "skills/contracts/nda-review/SKILL.md",
                    "practice_area": "contracts",
                    "risk_level": "medium",
                    "related_skills": ["skills/contracts/contract-risk-review/SKILL.md"],
                }
            ]
        }
        packs = {
            "packs": [
                {
                    "pack_id": "chatgpt/contracts",
                    "platform": "chatgpt",
                    "included_skills": ["skills/contracts/nda-review/SKILL.md"],
                    "included_core_rules": ["core/legal-work-product.md"],
                    "included_templates": [
                        "skills/contracts/nda-review/templates/risk-table.md"
                    ],
                }
            ]
        }
        (self.root / "metadata" / "index.json").write_text(json.dumps(index), encoding="utf-8")
        (self.root / "metadata" / "packs.json").write_text(json.dumps(packs), encoding="utf-8")

    def close(self) -> None:
        self.tempdir.cleanup()


class TestContextMetrics(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = ContextMetricsFixture()

    def tearDown(self) -> None:
        self.fixture.close()

    def test_token_estimate_rounds_up(self):
        self.assertEqual(metrics.estimate_tokens(0), 0)
        self.assertEqual(metrics.estimate_tokens(1), 1)
        self.assertEqual(metrics.estimate_tokens(9), 3)

    def test_collects_skill_and_pack_metrics(self):
        data = metrics.collect_metrics(self.fixture.root)
        skill = data["skills"][0]
        self.assertEqual(skill["id"], "contracts/nda-review")
        self.assertEqual(skill["output_section_count"], 3)
        self.assertEqual(skill["reference_link_count"], 1)
        self.assertEqual(skill["template_link_count"], 1)
        self.assertEqual(skill["related_skill_count"], 1)
        self.assertGreater(skill["characters"], 0)
        self.assertIn(skill["context_pressure"], {"compact", "moderate", "large"})

        pack = data["packs"][0]
        self.assertEqual(pack["pack_id"], "chatgpt/contracts")
        self.assertEqual(pack["included_file_count"], 3)
        self.assertGreater(pack["estimated_tokens"], skill["estimated_tokens"])

    def test_rendered_report_states_approximation(self):
        report = metrics.render_markdown(metrics.collect_metrics(self.fixture.root))
        self.assertIn("one token per four characters", report)
        self.assertIn("planning signal", report)
        self.assertIn("contracts/nda-review", report)

    def test_write_outputs_check_detects_drift(self):
        self.assertFalse(metrics.write_outputs(self.fixture.root, check=True))
        self.assertTrue(metrics.write_outputs(self.fixture.root, check=False))
        self.assertTrue(metrics.write_outputs(self.fixture.root, check=True))


if __name__ == "__main__":
    unittest.main()
