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

import argparse
import re
import sys
import json
from pathlib import Path
from _shared import EvalParseError, parse_eval_yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
EVALS_DIR = REPO_ROOT / "evals"

errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


# The eight skills that must each have a sample eval file under evals/skills/.
# Each slug matches the canonical skill folder name under skills/.
REQUIRED_EVAL_SLUGS = [
    "contract-risk-review",
    "nda-review",
    "matter-intake",
    "litigation-chronology",
    "privilege-log-review",
    "dpa-review",
    "launch-review",
    "compliance-gap-matrix",
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

BENCHMARK_REQUIRED_TOP_KEYS = {
    "suite": "scalar",
    "description": "scalar",
    "cases": "caselist",
}
BENCHMARK_REQUIRED_CASE_KEYS = {
    "eval_id": "scalar",
    "title": "scalar",
    "skill_id": "scalar",
    "practice_area": "scalar",
    "category": "scalar",
    "risk_level": "scalar",
    "task_prompt": "scalar",
    "fictional_matter_facts": "strlist",
    "required_output": "strlist",
    "expected_safety_behaviors": "strlist",
    "prohibited_behaviors": "strlist",
    "required_quality_checks": "strlist",
    "expected_attorney_review_items": "strlist",
    "rubric": "strlist",
    "pass_fail_criteria": "strlist",
    "known_limitations": "strlist",
    "eval_status": "scalar",
}
OPTIONAL_BENCHMARK_CASE_KEYS = {
    "provided_source_materials": "strlist",
    "scoring_weights": "strlist",
}
ROUTER_REQUIRED_CASE_KEYS = {
    "eval_id": "scalar",
    "title": "scalar",
    "request": "scalar",
    "expected_primary_skill": "scalar",
    "expected_missing_facts": "strlist",
    "expected_quality_checks": "strlist",
    "expected_gates": "strlist",
    "expected_attorney_escalation": "scalar",
    "eval_status": "scalar",
}
STATIC_REQUIRED_CASE_KEYS = {
    "eval_id": "scalar",
    "title": "scalar",
    "check_type": "scalar",
    "target": "scalar",
    "expected_result": "scalar",
    "eval_status": "scalar",
}
EVAL_STATUSES = {"unrun", "manual-ready", "automated-static", "scored"}
RISK_LEVELS = {"low", "medium", "high", "critical"}


# EvalParseError and parse_eval_yaml live in _shared.py (imported above) so
# check_evals.py and run_evals.py share one restricted-YAML implementation.


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


def _load_metadata() -> tuple[dict, dict, dict]:
    def load_json(relpath: str) -> dict:
        path = REPO_ROOT / relpath
        if not path.is_file():
            err(f"{relpath}: required metadata file not found")
            return {}
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            err(f"{relpath}: invalid JSON ({exc})")
            return {}

    return (
        load_json("metadata/index.json"),
        load_json("metadata/router.json"),
        load_json("metadata/packs.json"),
    )


def _check_case_value(relname: str, label: str, key: str, kind: str, value) -> None:
    if kind == "scalar":
        if not isinstance(value, str) or not value.strip():
            err(f"{relname}: case '{label}' '{key}' must be a non-empty scalar")
    elif kind == "strlist":
        check_strlist(relname, f"case '{label}' '{key}'", value)


def _validate_case_schema(
    relname: str,
    suite_name: str,
    case: dict,
    required: dict[str, str],
    optional: dict[str, str] | None = None,
) -> None:
    optional = optional or {}
    label = case.get("eval_id") if isinstance(case.get("eval_id"), str) else suite_name
    allowed = set(required) | set(optional)
    for key in case:
        if key not in allowed:
            err(f"{relname}: case '{label}' has unknown key '{key}'")
    for key, kind in required.items():
        if key not in case:
            err(f"{relname}: case '{label}' missing key '{key}'")
            continue
        _check_case_value(relname, label, key, kind, case[key])
    for key, kind in optional.items():
        if key in case:
            _check_case_value(relname, label, key, kind, case[key])


def validate_benchmark_file(
    path: Path,
    valid_skill_ids: set[str],
    valid_quality_ids: set[str],
    valid_practice_areas: set[str],
) -> int:
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
        if key not in BENCHMARK_REQUIRED_TOP_KEYS:
            err(f"{relname}: unknown top-level key '{key}'")
    for key, kind in BENCHMARK_REQUIRED_TOP_KEYS.items():
        if key not in data:
            err(f"{relname}: missing top-level key '{key}'")
        elif kind == "scalar" and not isinstance(data[key], str):
            err(f"{relname}: '{key}' must be a scalar")
        elif kind == "caselist" and not isinstance(data[key], list):
            err(f"{relname}: '{key}' must be a list")

    seen: set[str] = set()
    cases = data.get("cases") if isinstance(data.get("cases"), list) else []
    for case in cases:
        if not isinstance(case, dict):
            err(f"{relname}: cases must contain mappings")
            continue
        _validate_case_schema(
            relname,
            "benchmark",
            case,
            BENCHMARK_REQUIRED_CASE_KEYS,
            OPTIONAL_BENCHMARK_CASE_KEYS,
        )
        eval_id = case.get("eval_id")
        if isinstance(eval_id, str):
            if eval_id in seen:
                err(f"{relname}: duplicate eval_id '{eval_id}'")
            seen.add(eval_id)
        skill_id = case.get("skill_id")
        if isinstance(skill_id, str) and skill_id not in valid_skill_ids:
            err(f"{relname}: case '{eval_id}' references unknown skill_id '{skill_id}'")
        area = case.get("practice_area")
        if isinstance(area, str) and area not in valid_practice_areas:
            err(f"{relname}: case '{eval_id}' has unknown practice_area '{area}'")
        risk = case.get("risk_level")
        if isinstance(risk, str) and risk not in RISK_LEVELS:
            err(f"{relname}: case '{eval_id}' has invalid risk_level '{risk}'")
        status = case.get("eval_status")
        if isinstance(status, str) and status not in EVAL_STATUSES:
            err(f"{relname}: case '{eval_id}' has invalid eval_status '{status}'")
        qids = case.get("required_quality_checks")
        if isinstance(qids, list):
            for qid in qids:
                if isinstance(qid, str) and qid not in valid_quality_ids:
                    err(f"{relname}: case '{eval_id}' references unknown quality check '{qid}'")
    return len(cases)


def validate_router_eval_file(
    path: Path,
    valid_skill_ids: set[str],
    valid_quality_ids: set[str],
) -> int:
    relname = path.relative_to(REPO_ROOT).as_posix()
    try:
        data = parse_eval_yaml(path.read_text(encoding="utf-8"))
    except EvalParseError as exc:
        err(f"{relname}: {exc}")
        return 0
    cases = data.get("cases") if isinstance(data, dict) else []
    if not isinstance(cases, list) or not cases:
        err(f"{relname}: cases must be a non-empty list")
        return 0
    seen: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            err(f"{relname}: cases must contain mappings")
            continue
        _validate_case_schema(relname, "router", case, ROUTER_REQUIRED_CASE_KEYS)
        eval_id = case.get("eval_id")
        if isinstance(eval_id, str):
            if eval_id in seen:
                err(f"{relname}: duplicate eval_id '{eval_id}'")
            seen.add(eval_id)
        skill_id = case.get("expected_primary_skill")
        if isinstance(skill_id, str) and skill_id not in valid_skill_ids:
            err(f"{relname}: case '{eval_id}' references unknown skill_id '{skill_id}'")
        status = case.get("eval_status")
        if isinstance(status, str) and status not in EVAL_STATUSES:
            err(f"{relname}: case '{eval_id}' has invalid eval_status '{status}'")
        qids = case.get("expected_quality_checks")
        if isinstance(qids, list):
            for qid in qids:
                if isinstance(qid, str) and qid not in valid_quality_ids:
                    err(f"{relname}: case '{eval_id}' references unknown quality check '{qid}'")
    return len(cases)


def validate_static_eval_file(path: Path) -> int:
    relname = path.relative_to(REPO_ROOT).as_posix()
    try:
        data = parse_eval_yaml(path.read_text(encoding="utf-8"))
    except EvalParseError as exc:
        err(f"{relname}: {exc}")
        return 0
    cases = data.get("cases") if isinstance(data, dict) else []
    if not isinstance(cases, list) or not cases:
        err(f"{relname}: cases must be a non-empty list")
        return 0
    seen: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            err(f"{relname}: cases must contain mappings")
            continue
        _validate_case_schema(relname, "static", case, STATIC_REQUIRED_CASE_KEYS)
        eval_id = case.get("eval_id")
        if isinstance(eval_id, str):
            if eval_id in seen:
                err(f"{relname}: duplicate eval_id '{eval_id}'")
            seen.add(eval_id)
        status = case.get("eval_status")
        if isinstance(status, str) and status not in EVAL_STATUSES:
            err(f"{relname}: case '{eval_id}' has invalid eval_status '{status}'")
    return len(cases)


def check_static_metadata_integrity(index_data: dict, router_data: dict, packs_data: dict) -> None:
    skills = index_data.get("skills") if isinstance(index_data, dict) else []
    packs = packs_data.get("packs") if isinstance(packs_data, dict) else []
    valid_quality = {q.get("id") for q in index_data.get("quality_checks", []) if isinstance(q, dict)}
    skill_ids = {s.get("id") for s in skills if isinstance(s, dict)}

    for skill in skills if isinstance(skills, list) else []:
        if not isinstance(skill, dict):
            continue
        checks = set(skill.get("recommended_quality_checks") or [])
        task = skill.get("category")
        path = skill.get("path")
        if skill.get("risk_level") in {"high", "critical"} and "attorney-review-gate" not in checks:
            err(f"static eval: {path}: high-risk skill missing attorney-review-gate")
        if task == "research" and not {"citation-integrity-check", "source-validation-check"} <= checks:
            err(f"static eval: {path}: research skill missing citation/source quality checks")
        if task == "drafting" and not {"legal-prose-polish", "output-format-compliance-check"} <= checks:
            err(f"static eval: {path}: drafting skill missing prose/format quality checks")
        if skill.get("id") in {
            "litigation/demand-letter",
            "legal-ops/templated-legal-response",
            "ip/cease-and-desist-response",
            "ip/dmca-takedown",
            "regulatory/enforcement-risk-memo",
        } and "privilege-confidentiality-check" not in checks:
            err(f"static eval: {path}: external-facing skill missing privilege-confidentiality-check")
        if any(q not in valid_quality for q in checks):
            err(f"static eval: {path}: recommended quality check missing from metadata")

    for pack in packs if isinstance(packs, list) else []:
        if not isinstance(pack, dict):
            continue
        pid = pack.get("pack_id")
        if not pack.get("included_core_rules"):
            err(f"static eval: {pid}: pack missing core safety rules")
        for field in ("included_skills", "included_core_rules", "included_templates",
                      "included_quality_checks", "included_matter_workspace_templates"):
            for item in pack.get(field) or []:
                if field == "included_quality_checks":
                    if item not in valid_quality:
                        err(f"static eval: {pid}: unknown quality check '{item}'")
                    continue
                if isinstance(item, str) and not (REPO_ROOT / item).exists():
                    err(f"static eval: {pid}: missing referenced file '{item}'")

    router_examples = router_data.get("examples") if isinstance(router_data, dict) else []
    for entry in router_examples if isinstance(router_examples, list) else []:
        if not isinstance(entry, dict):
            continue
        for route in [entry.get("route_to")] + list(entry.get("fallback_routes") or []):
            if isinstance(route, str) and route.startswith("skills/") and not (REPO_ROOT / route).is_file():
                err(f"static eval: router references missing skill path '{route}'")


# --- Main ------------------------------------------------------------------

def main() -> int:
    argparse.ArgumentParser(
        description="Validate the AgentCounsel eval framework under evals/ "
                    "(static, stdlib-only, no network). Exit 0 if all checks pass.",
    ).parse_args()
    print("AgentCounsel eval-framework validation")

    if not EVALS_DIR.is_dir():
        err("evals/: directory not found")
        print("\nErrors (1):\n  x evals/: directory not found\n")
        print("EVAL VALIDATION FAILED")
        return 1

    for relpath in ("README.md", "SKILL_QUALITY_RUBRIC.md", "RUBRICS.md", "shared/assertions.md"):
        if not (EVALS_DIR / relpath).is_file():
            err(f"evals/{relpath}: required file not found")

    skills_dir = EVALS_DIR / "skills"
    if not skills_dir.is_dir():
        err("evals/skills/: directory not found")

    valid_assertion_ids = load_assertion_ids()
    index_data, router_data, packs_data = _load_metadata()
    valid_skill_ids = {
        s.get("id") for s in index_data.get("skills", []) if isinstance(s, dict)
    }
    valid_quality_ids = {
        q.get("id") for q in index_data.get("quality_checks", []) if isinstance(q, dict)
    }
    valid_practice_areas = set(index_data.get("practice_areas", {}).keys())

    eval_files = (sorted(skills_dir.glob("*" + EVAL_SUFFIX))
                  if skills_dir.is_dir() else [])
    found_slugs = {p.name[:-len(EVAL_SUFFIX)] for p in eval_files}
    for slug in REQUIRED_EVAL_SLUGS:
        if slug not in found_slugs:
            err(f"evals/skills/{slug}{EVAL_SUFFIX}: required eval file is missing")

    total_cases = 0
    for path in eval_files:
        total_cases += validate_eval_file(path, valid_assertion_ids)

    benchmark_cases = 0
    benchmark_dir = EVALS_DIR / "benchmarks"
    if benchmark_dir.is_dir():
        for path in sorted(benchmark_dir.glob("*" + EVAL_SUFFIX)):
            benchmark_cases += validate_benchmark_file(
                path, valid_skill_ids, valid_quality_ids, valid_practice_areas)

    router_cases = 0
    router_dir = EVALS_DIR / "router"
    if router_dir.is_dir():
        for path in sorted(router_dir.glob("*" + EVAL_SUFFIX)):
            router_cases += validate_router_eval_file(
                path, valid_skill_ids, valid_quality_ids)

    static_cases = 0
    static_dir = EVALS_DIR / "static"
    if static_dir.is_dir():
        for path in sorted(static_dir.glob("*" + EVAL_SUFFIX)):
            static_cases += validate_static_eval_file(path)

    check_static_metadata_integrity(index_data, router_data, packs_data)

    print(f"  eval files:      {len(eval_files)}")
    print(f"  cases:           {total_cases}")
    print(f"  benchmark cases: {benchmark_cases}")
    print(f"  router cases:    {router_cases}")
    print(f"  static cases:    {static_cases}")
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
