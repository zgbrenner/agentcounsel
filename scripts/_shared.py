#!/usr/bin/env python3
"""Shared definitions for AgentCounsel's stdlib-only tooling.

A neutral leaf module imported by the validation and build scripts so the
"what is a valid skill" schema and the restricted eval-YAML parser live in
exactly one place instead of being copied across scripts. Standard library
only — no third-party packages, no runtime.

Scripts run as ``python scripts/<name>.py``, which puts ``scripts/`` on
``sys.path``; ``import _shared`` then resolves the same way the existing
cross-script imports (``import build_skill_index``, ``import check_evals``)
already do.
"""

from __future__ import annotations

import re

# The required H2 sections for every canonical skill, in order. Stored as bare
# titles (without the leading "## "); callers that need the heading form build
# it themselves. See docs/SKILL_METADATA_STANDARD.md and CONTRIBUTING.md;
# validate_repo.py is the gating check that enforces both presence and order.
REQUIRED_SECTIONS = [
    "Purpose",
    "Use When",
    "Required Inputs",
    "Do Not Use When",
    "Legal Safety Rules",
    "Workflow",
    "Output Format",
    "Attorney Verification Checklist",
]

# The standardized frontmatter fields every canonical skill must declare, in
# canonical order. See docs/SKILL_METADATA_STANDARD.md.
REQUIRED_FIELDS = [
    "name",
    "description",
    "practice_area",
    "task_type",
    "jurisdictions",
    "risk_level",
    "requires_attorney_review",
    "inputs",
    "outputs",
    "related_skills",
    "tags",
]


# --- Restricted YAML subset parser ----------------------------------------
#
# Supports exactly what the eval files use: a top-level mapping, two-space
# indentation, scalar values (rest of line), block lists of scalars, and
# block lists of mappings. No flow collections, no block scalars, no quoting.


class EvalParseError(Exception):
    pass


def parse_eval_yaml(text: str):
    """Parse the restricted YAML subset used by eval files into dict/list."""
    rows: list[tuple[int, str, int]] = []
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip()
        stripped = line.lstrip(" ")
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(stripped)
        if "\t" in line[:indent]:
            raise EvalParseError(f"line {lineno}: tab in indentation; use spaces")
        if indent % 2 != 0:
            raise EvalParseError(
                f"line {lineno}: indentation must be a multiple of 2 spaces")
        rows.append((indent, stripped, lineno))

    if not rows:
        raise EvalParseError("file has no content")
    if rows[0][0] != 0:
        raise EvalParseError("top level must not be indented")

    pos = 0

    def parse_mapping(indent: int) -> dict:
        nonlocal pos
        result: dict = {}
        while pos < len(rows):
            ind, content, lineno = rows[pos]
            if ind < indent:
                break
            if ind > indent:
                raise EvalParseError(f"line {lineno}: unexpected indentation")
            if content.startswith("- "):
                break
            key, sep, inline = content.partition(":")
            if not sep:
                raise EvalParseError(f"line {lineno}: expected 'key: value'")
            key = key.strip()
            inline = inline.strip()
            pos += 1
            if inline:
                result[key] = inline
            elif pos < len(rows) and rows[pos][0] > indent:
                child = rows[pos][0]
                if rows[pos][1].startswith("- "):
                    result[key] = parse_list(child)
                else:
                    result[key] = parse_mapping(child)
            else:
                result[key] = None
        return result

    def parse_list(indent: int) -> list:
        nonlocal pos
        result: list = []
        while pos < len(rows):
            ind, content, lineno = rows[pos]
            if ind < indent or not content.startswith("- "):
                break
            if ind > indent:
                raise EvalParseError(
                    f"line {lineno}: unexpected indentation in list")
            item = content[2:].strip()
            if not item:
                raise EvalParseError(f"line {lineno}: empty list item")
            key, sep, inline = item.partition(":")
            is_mapping = bool(sep) and re.fullmatch(r"[A-Za-z0-9_]+", key.strip())
            if is_mapping:
                pos += 1
                mapping: dict = {}
                first_key = key.strip()
                inline = inline.strip()
                if inline:
                    mapping[first_key] = inline
                elif pos < len(rows) and rows[pos][0] > indent + 2:
                    child = rows[pos][0]
                    if rows[pos][1].startswith("- "):
                        mapping[first_key] = parse_list(child)
                    else:
                        mapping[first_key] = parse_mapping(child)
                else:
                    mapping[first_key] = None
                mapping.update(parse_mapping(indent + 2))
                result.append(mapping)
            else:
                pos += 1
                result.append(item)
        return result

    data = parse_mapping(0)
    if pos != len(rows):
        ind, content, lineno = rows[pos]
        raise EvalParseError(
            f"line {lineno}: could not parse (check indentation and structure)")
    return data
