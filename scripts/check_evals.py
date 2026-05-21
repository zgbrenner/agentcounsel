#!/usr/bin/env python3
"""AgentCounsel eval-framework validation.

Static, non-LLM schema check for the skill eval framework under evals/.
Standard library only — no third-party packages, no API keys, no network.
Run from anywhere:

    python scripts/check_evals.py

Exit code 0 if all checks pass, 1 if any error is found. The eval file
schema is documented in evals/README.md.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EVALS_DIR = REPO_ROOT / "evals"

errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


# The eight skills that must each have a sample eval file under evals/skills/.
REQUIRED_EVAL_SLUGS = [
    "contract-risk-review",
    "nda-review",
    "litigation-matter-intake",
    "chronology-builder",
    "privilege-log-review",
    "dpa-review",
    "product-launch-review",
    "regulatory-gap-analysis",
]

# The recurring shared assertions evals/shared/assertions.md must define.
REQUIRED_ASSERTION_IDS = [
    "draft-for-attorney-review",
    "not-legal-advice",
    "asks-missing-jurisdiction",
    "facts-vs-assumptions",
    "no-invented-authority",
    "follows-requested-format",
    "attorney-verification-checklist",
]

# Eval file schema. Value is the expected kind:
#   "scalar"   -> non-empty string
#   "strlist"  -> non-empty list of non-empty strings
#   "caselist" -> non-empty list of case mappings
REQUIRED_TOP_KEYS = {
    "skill": "scalar",
    "skill_path": "scalar",
    "description": "scalar",
    "shared_assertions": "strlist",
    "cases": "caselist",
}
REQUIRED_CASE_KEYS = {
    "id": "scalar",
    "user_request": "scalar",
    "input_facts": "strlist",
    "expected_output_characteristics": "strlist",
    "failure_modes": "strlist",
    "safety_checks": "strlist",
}

EVAL_SUFFIX = ".eval.yaml"


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


# --- Assertion catalogue ---------------------------------------------------

ASSERTION_ID_PAT = re.compile(r"^###\s+`([a-z0-9-]+)`", re.M)


def load_assertion_ids() -> set[str]:
    path = EVALS_DIR / "shared" / "assertions.md"
    if not path.is_file():
        err("evals/shared/assertions.md: required file not found")
        return set()
    ids = set(ASSERTION_ID_PAT.findall(path.read_text(encoding="utf-8")))
    for required in REQUIRED_ASSERTION_IDS:
        if required not in ids:
            err(f"evals/shared/assertions.md: missing required assertion "
                f"'{required}'")
    return ids


# --- Eval file validation --------------------------------------------------

def check_strlist(relname: str, where: str, value) -> None:
    if not isinstance(value, list) or not value:
        err(f"{relname}: {where} must be a non-empty list")
        return
    for item in value:
        if not isinstance(item, str) or not item.strip():
            err(f"{relname}: {where} must contain only non-empty text items")
            return


def validate_eval_file(path: Path, valid_assertion_ids: set[str]) -> int:
    """Validate one eval file against the schema. Returns the case count."""
    relname = path.relative_to(REPO_ROOT).as_posix()
    try:
        data = parse_eval_yaml(path.read_text(encoding="utf-8"))
    except EvalParseError as exc:
        err(f"{relname}: {exc}")
        return 0
    if not isinstance(data, dict):
        err(f"{relname}: top level must be a mapping")
        return 0

    for key in data:
        if key not in REQUIRED_TOP_KEYS:
            err(f"{relname}: unknown top-level key '{key}'")
    for key, kind in REQUIRED_TOP_KEYS.items():
        if key not in data:
            err(f"{relname}: missing top-level key '{key}'")
            continue
        value = data[key]
        if kind == "scalar":
            if not isinstance(value, str) or not value.strip():
                err(f"{relname}: '{key}' must be a non-empty scalar")
        elif kind == "strlist":
            check_strlist(relname, f"'{key}'", value)
        elif kind == "caselist":
            if not isinstance(value, list) or not value:
                err(f"{relname}: 'cases' must be a non-empty list")

    # skill field must match the file name slug.
    expected_slug = path.name[:-len(EVAL_SUFFIX)]
    skill = data.get("skill")
    if isinstance(skill, str) and skill.strip() != expected_slug:
        err(f"{relname}: 'skill' is '{skill.strip()}' but the file name "
            f"implies '{expected_slug}'")

    # skill_path must resolve to a file in the repository.
    skill_path = data.get("skill_path")
    if isinstance(skill_path, str) and skill_path.strip():
        if not (REPO_ROOT / skill_path.strip()).is_file():
            err(f"{relname}: skill_path '{skill_path.strip()}' does not point "
                f"to an existing file")

    # shared_assertions must reference defined assertion IDs.
    shared = data.get("shared_assertions")
    if isinstance(shared, list):
        for aid in shared:
            if isinstance(aid, str) and aid not in valid_assertion_ids:
                err(f"{relname}: shared_assertions references undefined "
                    f"assertion '{aid}'")

    # Validate each case.
    cases = data.get("cases")
    case_count = 0
    if isinstance(cases, list):
        seen_ids: set[str] = set()
        for n, case in enumerate(cases, 1):
            if not isinstance(case, dict):
                err(f"{relname}: case #{n} is not a mapping")
                continue
            case_count += 1
            label = case.get("id") if isinstance(case.get("id"), str) else f"#{n}"
            for key in case:
                if key not in REQUIRED_CASE_KEYS:
                    err(f"{relname}: case '{label}' has unknown key '{key}'")
            for key, kind in REQUIRED_CASE_KEYS.items():
                if key not in case:
                    err(f"{relname}: case '{label}' missing key '{key}'")
                    continue
                value = case[key]
                if kind == "scalar":
                    if not isinstance(value, str) or not value.strip():
                        err(f"{relname}: case '{label}' '{key}' must be a "
                            f"non-empty scalar")
                else:
                    check_strlist(relname, f"case '{label}' '{key}'", value)
            cid = case.get("id")
            if isinstance(cid, str) and cid.strip():
                if cid.strip() in seen_ids:
                    err(f"{relname}: duplicate case id '{cid.strip()}'")
                seen_ids.add(cid.strip())
    return case_count


# --- Main ------------------------------------------------------------------

def main() -> int:
    print("AgentCounsel eval-framework validation")

    if not EVALS_DIR.is_dir():
        err("evals/: directory not found")
        print("\nErrors (1):\n  x evals/: directory not found\n")
        print("EVAL VALIDATION FAILED")
        return 1

    for relpath in ("README.md", "SKILL_QUALITY_RUBRIC.md", "shared/assertions.md"):
        if not (EVALS_DIR / relpath).is_file():
            err(f"evals/{relpath}: required file not found")

    skills_dir = EVALS_DIR / "skills"
    if not skills_dir.is_dir():
        err("evals/skills/: directory not found")

    valid_assertion_ids = load_assertion_ids()

    eval_files = (sorted(skills_dir.glob("*" + EVAL_SUFFIX))
                  if skills_dir.is_dir() else [])
    found_slugs = {p.name[:-len(EVAL_SUFFIX)] for p in eval_files}
    for slug in REQUIRED_EVAL_SLUGS:
        if slug not in found_slugs:
            err(f"evals/skills/{slug}{EVAL_SUFFIX}: required eval file is missing")

    total_cases = 0
    for path in eval_files:
        total_cases += validate_eval_file(path, valid_assertion_ids)

    print(f"  eval files:      {len(eval_files)}")
    print(f"  cases:           {total_cases}")
    print(f"  assertions:      {len(valid_assertion_ids)}")
    print()

    if errors:
        print(f"Errors ({len(errors)}):")
        for msg in errors:
            print(f"  x {msg}")
        print()
        print("EVAL VALIDATION FAILED")
        return 1

    print("All eval checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
