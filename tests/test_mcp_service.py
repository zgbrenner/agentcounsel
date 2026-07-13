#!/usr/bin/env python3
"""Tests for the standard-library AgentCounsel MCP catalog service."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from agentcounsel_mcp import CatalogLoadError, CatalogService


class CatalogFixture:
    def __init__(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "metadata").mkdir()
        (self.root / "core").mkdir()

        skills = [
            {
                "id": "contracts/nda-review",
                "title": "NDA Review",
                "name": "NDA Review",
                "path": "skills/contracts/nda-review/SKILL.md",
                "summary": "Use when reviewing a non-disclosure or confidentiality agreement.",
                "description": "Use when reviewing a non-disclosure or confidentiality agreement.",
                "use_when": [
                    "Review a mutual NDA before signature.",
                    "Identify confidentiality and non-use risks.",
                ],
                "required_inputs": ["Full NDA text", "Client role"],
                "expected_outputs": ["Triage rating", "Risk table"],
                "practice_area": "contracts",
                "task_type": "review",
                "risk_level": "medium",
                "requires_jurisdiction": True,
                "requires_deadline_check": False,
                "requires_attorney_review": True,
                "recommended_quality_checks": [
                    "attorney-review-gate",
                    "source-validation-check",
                ],
                "tags": ["nda", "confidentiality", "contract-review"],
                "related_skills": ["skills/contracts/contract-risk-review/SKILL.md"],
                "eval_status": "scored",
            },
            {
                "id": "contracts/contract-risk-review",
                "title": "Contract Risk Review",
                "name": "Contract Risk Review",
                "path": "skills/contracts/contract-risk-review/SKILL.md",
                "summary": "Use when reviewing a general commercial agreement for legal and business risk.",
                "description": "Use when reviewing a general commercial agreement for legal and business risk.",
                "use_when": ["Review a services agreement, SaaS agreement, or other commercial contract."],
                "required_inputs": ["Full agreement text", "Client role"],
                "expected_outputs": ["Risk summary", "Issue list"],
                "practice_area": "contracts",
                "task_type": "review",
                "risk_level": "high",
                "requires_jurisdiction": True,
                "requires_deadline_check": True,
                "requires_attorney_review": True,
                "recommended_quality_checks": [
                    "attorney-review-gate",
                    "assumption-audit",
                    "source-validation-check",
                ],
                "tags": ["commercial-contract", "risk-review"],
                "related_skills": ["skills/contracts/nda-review/SKILL.md"],
                "eval_status": "manual-eval-ready",
            },
            {
                "id": "privacy/breach-response-workflow",
                "title": "Breach Response Workflow",
                "name": "Breach Response Workflow",
                "path": "skills/privacy/breach-response-workflow/SKILL.md",
                "summary": "Use when a privacy or security incident is suspected or confirmed.",
                "description": "Use when a privacy or security incident is suspected or confirmed.",
                "use_when": ["Organize ransomware, unauthorized access, or exposed personal data."],
                "required_inputs": ["Incident description", "Discovery date", "Privilege posture"],
                "expected_outputs": ["Incident facts record", "Notification question set"],
                "practice_area": "privacy",
                "task_type": "intake",
                "risk_level": "critical",
                "requires_jurisdiction": True,
                "requires_deadline_check": True,
                "requires_attorney_review": True,
                "recommended_quality_checks": [
                    "attorney-review-gate",
                    "jurisdiction-deadline-gates",
                    "privilege-confidentiality-check",
                ],
                "tags": ["breach-response", "incident-response", "privacy"],
                "related_skills": [],
                "eval_status": "manual-eval-ready",
            },
        ]
        index = {
            "skill_count": len(skills),
            "practice_areas": {"contracts": 2, "privacy": 1},
            "skills": skills,
        }
        router = {
            "workspace_triggers": [
                "multi-step",
                "document-heavy",
                "high-risk",
                "ongoing",
                "deadline-sensitive",
            ],
            "route_types": ["one-off skill", "matter workspace", "quality check"],
        }
        (self.root / "metadata" / "index.json").write_text(
            json.dumps(index), encoding="utf-8"
        )
        (self.root / "metadata" / "router.json").write_text(
            json.dumps(router), encoding="utf-8"
        )
        (self.root / "core" / "legal-work-product.md").write_text(
            "# Legal Work Product\n\nDraft for attorney review.\n", encoding="utf-8"
        )

        for skill in skills:
            path = self.root / skill["path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            repeated = "\n".join(["NDA confidentiality boilerplate." for _ in range(40)])
            body = repeated if skill["id"] == "contracts/contract-risk-review" else "Specific body."
            path.write_text(
                f"---\nname: {skill['title']}\n---\n# {skill['title']}\n\n{body}\n",
                encoding="utf-8",
            )

    def close(self) -> None:
        self.tempdir.cleanup()


class TestCatalogService(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = CatalogFixture()
        self.service = CatalogService.from_root(self.fixture.root)

    def tearDown(self) -> None:
        self.fixture.close()

    def test_loads_generated_metadata_and_preserves_lists(self):
        card = self.service.get_skill_card("contracts/nda-review")
        self.assertEqual(card["id"], "contracts/nda-review")
        self.assertEqual(card["required_inputs"], ["Full NDA text", "Client role"])
        self.assertEqual(card["tags"], ["nda", "confidentiality", "contract-review"])

    def test_list_practice_areas_uses_generated_counts(self):
        self.assertEqual(
            self.service.list_practice_areas(),
            [
                {"practice_area": "contracts", "skill_count": 2},
                {"practice_area": "privacy", "skill_count": 1},
            ],
        )

    def test_search_returns_stable_ids_and_exact_id_first(self):
        results = self.service.search_skills("contracts/nda-review")
        self.assertEqual(results[0]["id"], "contracts/nda-review")
        self.assertGreater(results[0]["relevance_score"], 0)

    def test_trigger_metadata_outweighs_repeated_body_boilerplate(self):
        results = self.service.search_skills("review NDA confidentiality")
        self.assertEqual(results[0]["id"], "contracts/nda-review")

    def test_practice_area_filter(self):
        results = self.service.search_skills("incident", practice_area="privacy")
        self.assertEqual([item["id"] for item in results], ["privacy/breach-response-workflow"])

    def test_get_skill_accepts_slug_title_and_path_aliases(self):
        for alias in (
            "nda-review",
            "NDA Review",
            "skills/contracts/nda-review/SKILL.md",
        ):
            record = self.service.get_skill(alias)
            self.assertEqual(record["id"], "contracts/nda-review")
            self.assertIn("# NDA Review", record["content"])

    def test_compact_card_omits_content(self):
        card = self.service.get_skill_card("nda-review")
        self.assertNotIn("content", card)
        self.assertEqual(card["id"], "contracts/nda-review")

    def test_route_returns_structured_gates_and_alternatives(self):
        route = self.service.route_task("Review this NDA before signature", limit=2)
        self.assertEqual(route["status"], "matched")
        self.assertEqual(route["primary_route"]["id"], "contracts/nda-review")
        self.assertEqual(route["route_type"], "one-off skill")
        self.assertIn("Full NDA text", route["missing_required_inputs"])
        self.assertIn("attorney-review-gate", route["mandatory_quality_checks"])
        self.assertTrue(route["gates"]["jurisdiction"])
        self.assertFalse(route["gates"]["deadline"])
        self.assertTrue(route["gates"]["attorney_review"])
        self.assertFalse(route["escalation_required"])
        self.assertEqual(len(route["alternative_routes"]), 1)
        self.assertIn(route["confidence"], {"low", "medium", "high"})
        self.assertTrue(route["why_selected"])

    def test_critical_skill_requires_escalation(self):
        route = self.service.route_task("Organize a ransomware breach incident")
        self.assertEqual(route["primary_route"]["id"], "privacy/breach-response-workflow")
        self.assertTrue(route["escalation_required"])

    def test_workspace_trigger_changes_route_type(self):
        route = self.service.route_task(
            "This is an ongoing multi-step document-heavy contract matter"
        )
        self.assertEqual(route["route_type"], "matter workspace")

    def test_no_match_is_explicit(self):
        route = self.service.route_task("quantum gardening telescope")
        self.assertEqual(route["status"], "no_match")
        self.assertIsNone(route["primary_route"])
        self.assertEqual(route["alternative_routes"], [])

    def test_empty_query_and_invalid_limit_rejected(self):
        with self.assertRaises(ValueError):
            self.service.search_skills("   ")
        with self.assertRaises(ValueError):
            self.service.search_skills("nda", limit=0)

    def test_unknown_skill_raises_key_error(self):
        with self.assertRaises(KeyError):
            self.service.get_skill_card("missing/skill")


class TestCatalogLoadErrors(unittest.TestCase):
    def test_missing_metadata_raises_descriptive_error(self):
        with tempfile.TemporaryDirectory() as tempdir:
            with self.assertRaises(CatalogLoadError) as ctx:
                CatalogService.from_root(Path(tempdir))
        self.assertIn("metadata/index.json", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
