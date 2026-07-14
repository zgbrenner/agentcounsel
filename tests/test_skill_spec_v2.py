#!/usr/bin/env python3
"""Tests for the standard-library Skill Specification v2 compiler."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from skill_spec_v2 import (  # noqa: E402
    BASELINE_EVIDENCE_FIELDS,
    BASELINE_INHERITS,
    SCHEMA_VERSION,
    SpecValidationError,
    compile_skill_spec,
    load_custom_spec,
    validate_compiled_spec,
)


LEGACY_META = {
    "name": "Test Contract Review",
    "description": "Use when reviewing a test commercial agreement.",
    "practice_area": "contracts",
    "task_type": "review",
    "jurisdictions": [],
    "risk_level": "high",
    "requires_attorney_review": True,
    "inputs": [
        "The full agreement text",
        "The client's role",
        "Optional: the client's negotiation playbook",
    ],
    "outputs": ["Risk summary", "Issue table", "Attorney verification checklist"],
    "related_skills": [],
    "tags": ["contracts", "review"],
}

LEGACY_BODY = """# Test Contract Review

## Use When

- Review a commercial agreement.

## Required Inputs

- The full agreement text.

## Workflow

1. Review the agreement.

## Output Format

1. Risk summary.
2. Issue table.
"""

DERIVED = {
    "requires_jurisdiction": True,
    "requires_deadline_check": True,
    "recommended_quality_checks": [
        "attorney-review-gate",
        "source-validation-check",
        "assumption-audit",
        "jurisdiction-deadline-gates",
    ],
}


class SpecFixture:
    def __init__(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.skill_dir = self.root / "skills" / "contracts" / "test-contract-review"
        self.skill_dir.mkdir(parents=True)
        (self.skill_dir / "SKILL.md").write_text(LEGACY_BODY, encoding="utf-8")
        (self.skill_dir / "templates").mkdir()
        (self.skill_dir / "templates" / "risk-table.md").write_text(
            "# Risk Table\n", encoding="utf-8"
        )
        for path in BASELINE_INHERITS:
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(f"# {target.stem}\n", encoding="utf-8")
        deadline = self.root / "core" / "jurisdiction-and-deadline-gates.md"
        deadline.write_text("# Gates\n", encoding="utf-8")

    def write_spec(self, data: dict) -> None:
        (self.skill_dir / "SPEC.json").write_text(
            json.dumps(data, indent=2) + "\n", encoding="utf-8"
        )

    def compile(self) -> dict:
        return compile_skill_spec(
            self.skill_dir,
            LEGACY_META,
            LEGACY_BODY,
            DERIVED,
            self.root,
        )

    def close(self) -> None:
        self.tempdir.cleanup()


class TestLegacyCompilation(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = SpecFixture()

    def tearDown(self) -> None:
        self.fixture.close()

    def test_legacy_skill_compiles_to_complete_v2_contract(self):
        spec = self.fixture.compile()
        self.assertEqual(spec["schema_version"], SCHEMA_VERSION)
        self.assertEqual(spec["skill_id"], "contracts/test-contract-review")
        self.assertFalse(spec["has_custom_spec"])
        self.assertIsNone(spec["spec_path"])
        self.assertTrue(set(BASELINE_INHERITS).issubset(spec["inherits"]))
        self.assertIn("core/jurisdiction-and-deadline-gates.md", spec["inherits"])
        self.assertEqual(spec["gates"]["missing_inputs"]["behavior"], "stop-and-ask")
        self.assertTrue(spec["gates"]["attorney_review"]["required"])
        self.assertTrue(spec["gates"]["jurisdiction"]["required"])
        self.assertTrue(spec["gates"]["deadline"]["required"])
        self.assertFalse(spec["gates"]["deadline"]["calculation_allowed"])
        self.assertEqual(
            [mode["id"] for mode in spec["execution_modes"]],
            ["quick-triage", "standard", "deep-review"],
        )
        self.assertEqual(len(spec["input_schema"]), 3)
        self.assertEqual(len(spec["output_schema"]), 3)
        self.assertTrue(
            set(BASELINE_EVIDENCE_FIELDS).issubset(
                set(spec["evidence_schema"]["required_fields"])
            )
        )
        self.assertEqual(spec["quality_checks"], DERIVED["recommended_quality_checks"])
        self.assertEqual(validate_compiled_spec(spec, self.fixture.root), [])

    def test_optional_input_is_optional_and_required_inputs_may_not_be_inferred(self):
        spec = self.fixture.compile()
        fields = {field["id"]: field for field in spec["input_schema"]}
        self.assertTrue(fields["full-agreement-text"]["required"])
        self.assertFalse(fields["full-agreement-text"]["may_infer"])
        self.assertFalse(fields["clients-negotiation-playbook"]["required"])
        self.assertEqual(
            fields["clients-negotiation-playbook"]["label"],
            "the client's negotiation playbook",
        )

    def test_legacy_type_inference_is_conservative(self):
        spec = self.fixture.compile()
        fields = {field["id"]: field for field in spec["input_schema"]}
        outputs = {artifact["id"]: artifact for artifact in spec["output_schema"]}
        self.assertEqual(fields["full-agreement-text"]["type"], "document")
        self.assertEqual(fields["clients-role"]["type"], "text")
        self.assertEqual(outputs["issue-table"]["type"], "table")
        self.assertEqual(outputs["attorney-verification-checklist"]["type"], "checklist")


class TestCustomOverlay(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = SpecFixture()

    def tearDown(self) -> None:
        self.fixture.close()

    def _valid_overlay(self) -> dict:
        return {
            "schema_version": "2.0",
            "skill_id": "contracts/test-contract-review",
            "inherits": ["core/business-stakeholder-communication.md"],
            "gates": {
                "deadline": {"required": True, "calculation_allowed": False},
                "custom": [
                    {
                        "id": "specialist-context",
                        "condition": "The agreement is part of an M&A or employment transaction.",
                        "action": "stop-and-escalate",
                        "reason": "The document requires transaction-specific specialist review.",
                    }
                ],
            },
            "execution_modes": [
                {
                    "id": "quick-triage",
                    "enabled": False,
                    "purpose": "Do not triage this agreement without the complete document.",
                    "output_detail": "minimal",
                    "quality_checks": ["attorney-review-gate"],
                }
            ],
            "input_schema": [
                {
                    "id": "clients-role",
                    "label": "Client role",
                    "type": "enum",
                    "required": True,
                    "description": "The client's position in the agreement.",
                    "source_requirement": "user-provided",
                    "may_infer": False,
                    "sensitive": False,
                    "enum": ["customer", "vendor", "mutual"],
                }
            ],
            "output_schema": [
                {
                    "id": "issue-table",
                    "label": "Issue table",
                    "type": "table",
                    "required": True,
                    "description": "Each material issue with evidence and recommended action.",
                    "attorney_review_required": True,
                }
            ],
            "evidence_schema": {"required_fields": ["support_text"]},
            "modules": [
                {
                    "id": "risk-table-template",
                    "kind": "template",
                    "path": "skills/contracts/test-contract-review/templates/risk-table.md",
                    "required": True,
                    "load_when": "standard or deep-review mode",
                }
            ],
        }

    def test_custom_overlay_refines_records_and_adds_modules(self):
        stakeholder = self.fixture.root / "core" / "business-stakeholder-communication.md"
        stakeholder.write_text("# Stakeholder Communication\n", encoding="utf-8")
        overlay = self._valid_overlay()
        self.fixture.write_spec(overlay)
        loaded = load_custom_spec(self.fixture.skill_dir)
        self.assertEqual(loaded["skill_id"], "contracts/test-contract-review")

        spec = self.fixture.compile()
        self.assertTrue(spec["has_custom_spec"])
        self.assertEqual(
            spec["spec_path"],
            "skills/contracts/test-contract-review/SPEC.json",
        )
        self.assertIn("core/business-stakeholder-communication.md", spec["inherits"])
        modes = {mode["id"]: mode for mode in spec["execution_modes"]}
        self.assertFalse(modes["quick-triage"]["enabled"])
        fields = {field["id"]: field for field in spec["input_schema"]}
        self.assertEqual(fields["clients-role"]["type"], "enum")
        self.assertEqual(fields["clients-role"]["enum"], ["customer", "vendor", "mutual"])
        self.assertEqual(spec["modules"][0]["id"], "risk-table-template")
        self.assertIn("support_text", spec["evidence_schema"]["required_fields"])
        self.assertEqual(spec["gates"]["custom"][0]["action"], "stop-and-escalate")

    def test_custom_overlay_cannot_weaken_safety_controls(self):
        invalid_overlays = [
            {"gates": {"attorney_review": {"required": False}}},
            {"gates": {"deadline": {"calculation_allowed": True}}},
            {"gates": {"missing_inputs": {"behavior": "continue-with-assumptions"}}},
            {"evidence_schema": {"replace_required_fields": True, "required_fields": []}},
            {
                "input_schema": [
                    {
                        "id": "full-agreement-text",
                        "required": True,
                        "may_infer": True,
                    }
                ]
            },
        ]
        for overlay in invalid_overlays:
            with self.subTest(overlay=overlay):
                self.fixture.write_spec(overlay)
                with self.assertRaises(SpecValidationError):
                    self.fixture.compile()

    def test_invalid_controlled_values_duplicate_ids_and_paths_fail(self):
        invalid_overlays = [
            {"input_schema": [{"id": "x", "type": "magic"}]},
            {
                "modules": [
                    {
                        "id": "missing",
                        "kind": "template",
                        "path": "skills/contracts/test-contract-review/templates/missing.md",
                        "required": True,
                        "load_when": "standard",
                    }
                ]
            },
            {
                "gates": {
                    "custom": [
                        {
                            "id": "same",
                            "condition": "one",
                            "action": "flag",
                            "reason": "one",
                        },
                        {
                            "id": "same",
                            "condition": "two",
                            "action": "stop-and-escalate",
                            "reason": "two",
                        },
                    ]
                }
            },
        ]
        for overlay in invalid_overlays:
            with self.subTest(overlay=overlay):
                self.fixture.write_spec(overlay)
                with self.assertRaises(SpecValidationError):
                    self.fixture.compile()

    def test_wrong_skill_id_fails(self):
        self.fixture.write_spec(
            {"schema_version": "2.0", "skill_id": "contracts/another-skill"}
        )
        with self.assertRaises(SpecValidationError):
            self.fixture.compile()


if __name__ == "__main__":
    unittest.main()
