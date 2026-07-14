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

# Skills whose candidate outputs are required by the strict static eval gate.
# Each slug matches the canonical skill folder name under skills/. Shared by
# check_evals.py and run_evals.py so the two scripts cannot drift apart.
REQUIRED_EVAL_SLUGS = [
    "antitrust-compliance-policy-review",
    "attorney-review-gate",
    "automatic-stay-issue-spotter",
    "bad-faith-risk-triage",
    "beneficiary-designation-review",
    "capital-markets-closing-checklist",
    "cease-and-desist-response",
    "compliance-gap-matrix",
    "contract-risk-review",
    "crypto-digital-asset-tax-intake",
    "diligence-issue-extraction",
    "dpa-review",
    "launch-review",
    "litigation-chronology",
    "matter-intake",
    "nda-review",
    "negative-treatment-check",
    "privilege-log-review",
    "rw-insurance-review",
    "termination-risk",
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


# --- SKILL.md frontmatter parser -------------------------------------------
#
# The single implementation of the AgentCounsel frontmatter subset (top-level
# scalars and simple block lists), shared by every script that reads a
# SKILL.md. Three shapes are exposed so each caller keeps its existing return
# contract: split_frontmatter (lines), split_frontmatter_text (string), and
# load_frontmatter (dict).


def split_frontmatter(text: str):
    """Return (frontmatter_lines, body) or (None, None) if absent/unterminated."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "\n".join(lines[i + 1:])
    return None, None


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        inner = value[1:-1]
        if value[0] == '"':
            inner = inner.replace('\\"', '"').replace("\\\\", "\\")
        else:
            inner = inner.replace("''", "'")
        return inner
    return value


def _scalar(value: str):
    value = value.strip()
    if value == "[]":
        return []
    if value == "true":
        return True
    if value == "false":
        return False
    return _unquote(value)


def parse_frontmatter(fm_lines: list[str]) -> dict:
    """Parse the AgentCounsel frontmatter subset (a list of lines) into a dict."""
    meta: dict = {}
    i, n = 0, len(fm_lines)
    while i < n:
        line = fm_lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):(.*)$", line)
        if not match:
            i += 1
            continue
        key, rest = match.group(1), match.group(2).strip()
        if rest:
            meta[key] = _scalar(rest)
            i += 1
            continue
        # A bare "key:" introduces a block list.
        items: list[str] = []
        i += 1
        while i < n:
            item = re.match(r"^\s+-\s?(.*)$", fm_lines[i])
            if item:
                items.append(_unquote(item.group(1)))
                i += 1
            elif fm_lines[i].strip() == "":
                i += 1
            else:
                break
        meta[key] = items
    return meta


def split_frontmatter_text(text: str):
    """split_frontmatter as a single frontmatter string, with the ("", text)
    fallback the text-based callers expect when frontmatter is absent."""
    fm_lines, body = split_frontmatter(text)
    if fm_lines is None:
        return "", text
    return "\n".join(fm_lines), body


def load_frontmatter(text: str):
    """Parse frontmatter into (dict, body), with the ({}, text) fallback the
    dict-based callers expect when frontmatter is absent."""
    fm_lines, body = split_frontmatter(text)
    if fm_lines is None:
        return {}, text
    return parse_frontmatter(fm_lines), body
