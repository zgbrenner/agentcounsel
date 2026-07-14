#!/usr/bin/env python3
"""Tests for Phase 2B selective-module schema extensions."""

from __future__ import annotations

import unittest

from tests.test_skill_spec_v2 import SpecFixture
from scripts.skill_spec_v2 import SpecValidationError


class TestSelectiveModuleSchema(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = SpecFixture()
        modules = self.fixture.skill_dir / "modules"
        modules.mkdir()
        (modules / "trademark.md").write_text("# Trademark\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.fixture.close()

    def _overlay(self) -> dict:
        return {
            "input_schema": [
                {
                    "id": "rights",
                    "label": "Rights",
                    "type": "string-list",
                    "required": True,
                    "description": "Controlled right identifiers.",
                    "source_requirement": "user-provided",
                    "may_infer": False,
                    "sensitive": False,
                    "items": ["trademark", "copyright"],
                }
            ],
            "modules": [
                {
                    "id": "trademark",
                    "kind": "workflow-module",
                    "path": "skills/contracts/test-contract-review/modules/trademark.md",
                    "required": False,
                    "load_when": "The rights input includes trademark.",
                    "activation": {
                        "modes": ["standard", "deep-review"],
                        "input_id": "rights",
                        "operator": "contains-any",
                        "values": ["trademark"],
                    },
                }
            ],
            "context_scenarios": [
                {
                    "id": "standard-trademark",
                    "mode": "standard",
                    "inputs": {"rights": ["trademark"]},
                    "baseline_estimated_tokens": 1000,
                    "max_ratio": 0.7,
                }
            ],
        }

    def test_compiles_string_list_activation_and_context_scenarios(self):
        self.fixture.write_spec(self._overlay())
        spec = self.fixture.compile()
        rights = {field["id"]: field for field in spec["input_schema"]}["rights"]
        self.assertEqual(rights["type"], "string-list")
        self.assertEqual(rights["items"], ["trademark", "copyright"])
        self.assertEqual(spec["modules"][0]["activation"]["operator"], "contains-any")
        self.assertEqual(spec["context_scenarios"][0]["mode"], "standard")

    def test_rejects_invalid_activation_and_scenario_shapes(self):
        invalid: list[dict] = []

        overlay = self._overlay()
        overlay["modules"][0]["activation"]["operator"] = "matches-regex"
        invalid.append(overlay)

        overlay = self._overlay()
        overlay["modules"][0]["activation"]["modes"] = ["turbo"]
        invalid.append(overlay)

        overlay = self._overlay()
        del overlay["modules"][0]["activation"]["values"]
        invalid.append(overlay)

        overlay = self._overlay()
        overlay["context_scenarios"].append(dict(overlay["context_scenarios"][0]))
        invalid.append(overlay)

        overlay = self._overlay()
        overlay["context_scenarios"][0]["baseline_estimated_tokens"] = 0
        invalid.append(overlay)

        overlay = self._overlay()
        overlay["context_scenarios"][0]["max_ratio"] = 0
        invalid.append(overlay)

        overlay = self._overlay()
        overlay["input_schema"][0]["items"] = ["trademark", "trademark"]
        invalid.append(overlay)

        for candidate in invalid:
            with self.subTest(candidate=candidate):
                self.fixture.write_spec(candidate)
                with self.assertRaises(SpecValidationError):
                    self.fixture.compile()


if __name__ == "__main__":
    unittest.main()
