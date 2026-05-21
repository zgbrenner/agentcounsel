#!/usr/bin/env python3
"""Build the machine-readable AgentCounsel skill metadata index.

This script parses the standardized YAML frontmatter of every canonical
``SKILL.md`` and writes ``metadata/index.json`` — a single file that lets
LLMs, browser agents, static-site generators, and package builders discover
and route AgentCounsel skills without reading every Markdown file.

It is also the metadata authority for the repository: ``validate_repo.py``
imports the parser and the validation rules below so the standard is
enforced in one place. See ``docs/SKILL_METADATA_STANDARD.md``.

Standard library only — no third-party packages. Run from anywhere:

    python scripts/build_skill_index.py            # write metadata/index.json
    python scripts/build_skill_index.py --check    # report drift only (CI)

In ``--check`` mode the script writes nothing and exits non-zero if
``metadata/index.json`` is missing or out of date.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
INDEX_PATH = REPO_ROOT / "metadata" / "index.json"

# Directory names under skills/<area>/ that hold shared reference material.
NON_SKILL_DIRS = {"references"}

# The standardized frontmatter fields every canonical skill must declare,
# in canonical order. See docs/SKILL_METADATA_STANDARD.md.
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

SCALAR_FIELDS = {
    "name", "description", "practice_area", "task_type",
    "risk_level", "requires_attorney_review",
}
LIST_FIELDS = {"jurisdictions", "inputs", "outputs", "related_skills", "tags"}

# Controlled vocabularies.
TASK_TYPES = {
    "intake", "interview", "research", "review", "triage",
    "drafting", "analysis", "summarization", "extraction", "verification",
}
RISK_LEVELS = ["low", "medium", "high", "critical"]


def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path)


# --- Minimal YAML frontmatter parser --------------------------------------
#
# AgentCounsel frontmatter uses a deliberately small, fixed YAML subset:
# scalar `key: value`, empty list `key: []`, and block lists of the form
#   key:
#     - "item"
# This is valid YAML for external tools, and parseable here without a
# third-party YAML library (the repository is standard-library only).


def split_frontmatter(text: str):
    """Return (frontmatter_lines, body) or (None, None) if absent."""
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
    """Parse the AgentCounsel frontmatter subset into a dict."""
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


# --- Validation ------------------------------------------------------------

def validate_skill_metadata(skill_dir: Path) -> list[str]:
    """Validate one canonical skill's frontmatter. Return a list of errors."""
    md = skill_dir / "SKILL.md"
    rel_md = rel(md)
    if not md.is_file():
        return [f"{rel_md}: missing SKILL.md"]

    fm_lines, _ = split_frontmatter(md.read_text(encoding="utf-8"))
    if fm_lines is None:
        return [f"{rel_md}: missing or unterminated YAML frontmatter"]

    meta = parse_frontmatter(fm_lines)
    errors: list[str] = []

    for field in REQUIRED_FIELDS:
        if field not in meta:
            errors.append(f"{rel_md}: frontmatter missing required field "
                          f"'{field}'")
    if errors:
        return errors  # report missing fields before type-checking values

    for field in SCALAR_FIELDS:
        if isinstance(meta[field], list):
            errors.append(f"{rel_md}: '{field}' must be a single value, "
                          f"not a list")
    for field in LIST_FIELDS:
        if not isinstance(meta[field], list):
            errors.append(f"{rel_md}: '{field}' must be a list")
    if errors:
        return errors

    name = meta["name"]
    if not isinstance(name, str) or not name.strip():
        errors.append(f"{rel_md}: 'name' must be a non-empty string")

    desc = meta["description"]
    if not isinstance(desc, str) or not desc.strip():
        errors.append(f"{rel_md}: 'description' must be a non-empty string")
    elif not desc.strip().startswith("Use when"):
        errors.append(f"{rel_md}: 'description' must be trigger-rich and "
                      f"begin with 'Use when' (it states when to use the "
                      f"skill)")

    expected_area = skill_dir.parent.name
    if meta["practice_area"] != expected_area:
        errors.append(f"{rel_md}: 'practice_area' is "
                      f"'{meta['practice_area']}' but must match the "
                      f"directory area '{expected_area}'")

    if meta["task_type"] not in TASK_TYPES:
        errors.append(f"{rel_md}: 'task_type' is '{meta['task_type']}' — "
                      f"must be one of: {', '.join(sorted(TASK_TYPES))}")

    if meta["risk_level"] not in RISK_LEVELS:
        errors.append(f"{rel_md}: 'risk_level' is '{meta['risk_level']}' — "
                      f"must be one of: {', '.join(RISK_LEVELS)}")

    if not isinstance(meta["requires_attorney_review"], bool):
        errors.append(f"{rel_md}: 'requires_attorney_review' must be true "
                      f"or false")

    for field in ("inputs", "outputs", "tags"):
        items = meta[field]
        if not items:
            errors.append(f"{rel_md}: '{field}' must list at least one item")
        elif any(not isinstance(x, str) or not x.strip() for x in items):
            errors.append(f"{rel_md}: '{field}' contains an empty item")

    for target in meta["related_skills"]:
        if not (isinstance(target, str)
                and re.fullmatch(r"skills/[A-Za-z0-9_./-]+/SKILL\.md",
                                 target)):
            errors.append(f"{rel_md}: 'related_skills' entry '{target}' "
                          f"must be a repo path like "
                          f"'skills/<area>/<skill>/SKILL.md'")
        elif not (REPO_ROOT / target).is_file():
            errors.append(f"{rel_md}: 'related_skills' entry '{target}' "
                          f"does not resolve to an existing skill")
        elif target == rel_md:
            errors.append(f"{rel_md}: 'related_skills' must not list the "
                          f"skill itself")

    return errors


# --- Index building --------------------------------------------------------

def canonical_skill_dirs() -> list[Path]:
    dirs: list[Path] = []
    if not SKILLS_ROOT.is_dir():
        return dirs
    for area in sorted(p for p in SKILLS_ROOT.iterdir() if p.is_dir()):
        for skill in sorted(p for p in area.iterdir() if p.is_dir()):
            if skill.name in NON_SKILL_DIRS:
                continue
            if (skill / "SKILL.md").is_file():
                dirs.append(skill)
    return dirs


def skill_record(skill_dir: Path) -> dict:
    """Parsed metadata for one skill, in canonical field order."""
    md = skill_dir / "SKILL.md"
    fm_lines, _ = split_frontmatter(md.read_text(encoding="utf-8"))
    meta = parse_frontmatter(fm_lines or [])
    record = {"path": rel(md)}
    for field in REQUIRED_FIELDS:
        record[field] = meta.get(field)
    return record


def build_index() -> dict:
    """Assemble the full skill metadata index as a dict."""
    records = [skill_record(d) for d in canonical_skill_dirs()]
    records.sort(key=lambda r: r["path"])

    def counts(field: str) -> dict:
        tally: dict[str, int] = {}
        for r in records:
            tally[r[field]] = tally.get(r[field], 0) + 1
        return {k: tally[k] for k in sorted(tally)}

    risk_counts = {lvl: 0 for lvl in RISK_LEVELS}
    for r in records:
        if r["risk_level"] in risk_counts:
            risk_counts[r["risk_level"]] += 1

    return {
        "generated_by": "scripts/build_skill_index.py",
        "schema": "docs/SKILL_METADATA_STANDARD.md",
        "skill_count": len(records),
        "practice_areas": counts("practice_area"),
        "task_types": counts("task_type"),
        "risk_levels": risk_counts,
        "skills": records,
    }


def render_index() -> str:
    return json.dumps(build_index(), indent=2, ensure_ascii=False) + "\n"


# --- Modes -----------------------------------------------------------------

def run_write() -> int:
    skill_dirs = canonical_skill_dirs()
    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill_metadata(skill_dir))
    if errors:
        print("Cannot build the index — frontmatter validation failed:")
        for msg in errors:
            print(f"  x {msg}")
        return 1

    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(render_index(), encoding="utf-8")
    print("AgentCounsel skill metadata index")
    print(f"  skills indexed: {len(skill_dirs)}")
    print(f"  wrote {rel(INDEX_PATH)}")
    print("Done.")
    return 0


def run_check() -> int:
    skill_dirs = canonical_skill_dirs()
    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill_metadata(skill_dir))
    if errors:
        print("Frontmatter validation failed:")
        for msg in errors:
            print(f"  x {msg}")
        return 1

    expected = render_index()
    if not INDEX_PATH.is_file():
        print(f"MISSING: {rel(INDEX_PATH)} has not been generated.")
        print("Run 'python scripts/build_skill_index.py'.")
        return 1
    if INDEX_PATH.read_text(encoding="utf-8") != expected:
        print(f"STALE: {rel(INDEX_PATH)} is out of date.")
        print("Run 'python scripts/build_skill_index.py'.")
        return 1
    print(f"{rel(INDEX_PATH)} is up to date ({len(skill_dirs)} skills).")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build the AgentCounsel skill metadata index.")
    parser.add_argument(
        "--check", action="store_true",
        help="Report whether metadata/index.json is out of date and exit "
             "non-zero if so; do not write any files.")
    args = parser.parse_args(argv)

    if not SKILLS_ROOT.is_dir():
        print(f"error: skills directory not found at {rel(SKILLS_ROOT)}",
              file=sys.stderr)
        return 1

    return run_check() if args.check else run_write()


if __name__ == "__main__":
    sys.exit(main())
