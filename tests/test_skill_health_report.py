#!/usr/bin/env python3
"""Tests for AgentCounsel's repository-readiness scorecard."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import generate_context_metrics as context_metrics  # noqa: E402
import generate_skill_health_report as health  # noqa: E402


class HealthFixture:
    def __init__(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "metadata").mkdir()

        skill_dir = self.root / "skills" / "privacy" / "breach-response-workflow"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "# Breach Response Workflow\n\n## Output Format\n\n1. Incident record.\n",
            encoding="utf-8",
        )
        (skill_dir / "templates").mkdir()
        (skill_dir / "templates" / "incident-record.md").write_text(
            "# Incident Record\n", encoding="utf-8"
        )

        example_dir = self.root / "examples" / "privacy" / "breach-response-workflow"
        example_dir.mkdir(parents=True)
        (example_dir / "sample-output.md").write_text("# Sample\n", encoding="utf-8")

        eval_dir = self.root / "evals" / "skills"
        eval_dir.mkdir(parents=True)
        (eval_dir / "breach-response-workflow.eval.yaml").write_text(
            """skill: breach-response-workflow
skill_path: skills/privacy/breach-response-workflow/SKILL.md
description: Breach workflow eval
shared_assertions:
  - draft-for-attorney-review
cases:
  - id: golden
    user_request: organize incident
    input_facts:
      - incident supplied
    expected_output_characteristics:
      - incident record
    failure_modes:
      - invents deadline
    safety_checks:
      - attorney review
  - id: stress
    user_request: decide notification deadline
    input_facts:
      - jurisdiction missing
    expected_output_characteristics:
      - stops and asks
    failure_modes:
      - computes deadline
    safety_checks:
      - escalates
""",
            encoding="utf-8",
        )
        output_dir = self.root / "evals" / "outputs" / "breach-response-workflow"
        output_dir.mkdir(parents=True)
        (output_dir / "golden.md").write_text("DRAFT\n", encoding="utf-8")

        skill = {
            "id": "privacy/breach-response-workflow",
            "title": "Breach Response Workflow",
            "path": "skills/privacy/breach-response-workflow/SKILL.md",
            "practice_area": "privacy",
            "risk_level": "critical",
            "description": "Use when a privacy incident is suspected.",
            "use_when": ["A breach is suspected."],
            "required_inputs": ["Incident facts"],
            "expected_outputs": ["Incident record"],
            "tags": ["privacy", "incident-response"],
            "related_skills": [],
            "recommended_quality_checks": ["attorney-review-gate"],
            "eval_status": "scored",
        }
        (self.root / "metadata" / "index.json").write_text(
            json.dumps({"skills": [skill]}), encoding="utf-8"
        )
        (self.root / "metadata" / "packs.json").write_text(
            json.dumps({"packs": []}), encoding="utf-8"
        )
        context_metrics.write_outputs(self.root, check=False)

    def close(self) -> None:
        self.tempdir.cleanup()


class TestSkillHealthReport(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = HealthFixture()

    def tearDown(self) -> None:
        self.fixture.close()

    def test_collects_repository_readiness_signals(self):
        data = health.collect_health(self.fixture.root)
        skill = data["skills"][0]
        self.assertEqual(skill["id"], "privacy/breach-response-workflow")
        self.assertEqual(skill["eval_case_count"], 2)
        self.assertEqual(skill["candidate_output_count"], 1)
        self.assertTrue(skill["has_example"])
        self.assertEqual(skill["template_count"], 1)
        self.assertEqual(skill["routing_metadata"], "complete")
        self.assertEqual(skill["readiness_band"], "scored")
        self.assertEqual(skill["improvement_priority"], "low")

    def test_priority_policy_distinguishes_risk_and_evidence(self):
        self.assertEqual(
            health._priority("critical", "review-ready", "compact", True, 1),
            "high",
        )
        self.assertEqual(
            health._priority("high", "review-ready", "compact", True, 1),
            "medium",
        )
        self.assertEqual(
            health._priority("medium", "scored", "compact", False, 0),
            "low",
        )

    def test_report_disclaims_legal_correctness(self):
        report = health.render_markdown(health.collect_health(self.fixture.root))
        self.assertIn("does not measure legal correctness", report)
        self.assertIn("privacy/breach-response-workflow", report)

    def test_write_outputs_check_detects_drift(self):
        self.assertFalse(health.write_outputs(self.fixture.root, check=True))
        self.assertTrue(health.write_outputs(self.fixture.root, check=False))
        self.assertTrue(health.write_outputs(self.fixture.root, check=True))


if __name__ == "__main__":
    unittest.main()
