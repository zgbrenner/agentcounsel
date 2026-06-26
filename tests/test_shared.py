#!/usr/bin/env python3
"""Unit tests for scripts/_shared.py — the shared frontmatter and eval-YAML
parsers and schema constants that the validation/build tooling depends on.

Standard library only (unittest); no third-party packages, no network.

    python -m unittest discover -s tests        # from the repo root
"""

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import _shared  # noqa: E402


SAMPLE = """---
name: NDA Review
description: "Use when reviewing a non-disclosure agreement."
practice_area: contracts
jurisdictions: []
requires_attorney_review: true
inputs:
  - "The full NDA text"
  - "The client's role"
tags:
  - contracts
  - nda
---

# NDA Review

Body text.
"""


class TestSplitFrontmatter(unittest.TestCase):
    def test_valid(self):
        lines, body = _shared.split_frontmatter(SAMPLE)
        self.assertEqual(lines[0], "name: NDA Review")
        self.assertIn("# NDA Review", body)
        self.assertNotIn("---", body)

    def test_absent_returns_none(self):
        self.assertEqual(_shared.split_frontmatter("# No frontmatter\n"), (None, None))

    def test_unterminated_returns_none(self):
        self.assertEqual(_shared.split_frontmatter("---\nname: X\nbody\n"), (None, None))

    def test_empty_returns_none(self):
        self.assertEqual(_shared.split_frontmatter(""), (None, None))


class TestParseFrontmatter(unittest.TestCase):
    def setUp(self):
        lines, _ = _shared.split_frontmatter(SAMPLE)
        self.meta = _shared.parse_frontmatter(lines)

    def test_scalar_string(self):
        self.assertEqual(self.meta["name"], "NDA Review")

    def test_quoted_string_unquoted(self):
        self.assertEqual(self.meta["description"],
                         "Use when reviewing a non-disclosure agreement.")

    def test_empty_list_literal(self):
        self.assertEqual(self.meta["jurisdictions"], [])

    def test_bool_scalar(self):
        self.assertIs(self.meta["requires_attorney_review"], True)

    def test_block_list(self):
        self.assertEqual(self.meta["inputs"],
                         ["The full NDA text", "The client's role"])
        self.assertEqual(self.meta["tags"], ["contracts", "nda"])


class TestShapeWrappers(unittest.TestCase):
    def test_split_frontmatter_text_valid(self):
        fm_text, body = _shared.split_frontmatter_text(SAMPLE)
        self.assertIn("name: NDA Review", fm_text)
        self.assertIn("# NDA Review", body)

    def test_split_frontmatter_text_absent_fallback(self):
        self.assertEqual(_shared.split_frontmatter_text("plain\n"), ("", "plain\n"))

    def test_load_frontmatter_valid(self):
        meta, body = _shared.load_frontmatter(SAMPLE)
        self.assertEqual(meta["name"], "NDA Review")
        self.assertIn("# NDA Review", body)

    def test_load_frontmatter_absent_fallback(self):
        self.assertEqual(_shared.load_frontmatter("plain\n"), ({}, "plain\n"))


class TestParseEvalYaml(unittest.TestCase):
    def test_mapping_and_scalar_list(self):
        data = _shared.parse_eval_yaml(
            "skill: nda-review\nshared_assertions:\n  - a\n  - b\n")
        self.assertEqual(data["skill"], "nda-review")
        self.assertEqual(data["shared_assertions"], ["a", "b"])

    def test_list_of_mappings(self):
        data = _shared.parse_eval_yaml(
            "cases:\n  - id: c1\n    user_request: hello\n  - id: c2\n    user_request: bye\n")
        self.assertEqual([c["id"] for c in data["cases"]], ["c1", "c2"])
        self.assertEqual(data["cases"][0]["user_request"], "hello")

    def test_tab_indentation_raises(self):
        with self.assertRaises(_shared.EvalParseError):
            _shared.parse_eval_yaml("key:\n\t- x\n")

    def test_empty_raises(self):
        with self.assertRaises(_shared.EvalParseError):
            _shared.parse_eval_yaml("\n\n")


class TestConstants(unittest.TestCase):
    def test_required_sections(self):
        self.assertEqual(len(_shared.REQUIRED_SECTIONS), 8)
        self.assertEqual(_shared.REQUIRED_SECTIONS[0], "Purpose")
        self.assertEqual(_shared.REQUIRED_SECTIONS[-1], "Attorney Verification Checklist")

    def test_required_fields(self):
        self.assertEqual(len(_shared.REQUIRED_FIELDS), 11)
        self.assertIn("name", _shared.REQUIRED_FIELDS)
        self.assertIn("related_skills", _shared.REQUIRED_FIELDS)


class TestRealSkillRoundTrip(unittest.TestCase):
    """Parsing a real SKILL.md yields the required fields — guards against a
    parser change silently dropping data on the actual library format."""

    def test_nda_review(self):
        path = REPO_ROOT / "skills" / "contracts" / "nda-review" / "SKILL.md"
        meta, _ = _shared.load_frontmatter(path.read_text(encoding="utf-8"))
        for field in _shared.REQUIRED_FIELDS:
            self.assertIn(field, meta)
        self.assertIsInstance(meta["tags"], list)
        self.assertTrue(meta["description"].startswith("Use when"))


if __name__ == "__main__":
    unittest.main()
