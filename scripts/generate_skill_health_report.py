#!/usr/bin/env python3
"""Generate AgentCounsel repository-readiness signals for every skill.

The scorecard measures repository evidence and maintainability signals. It does
not measure legal correctness, attorney approval, or fitness for a real matter.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from _shared import EvalParseError, parse_eval_yaml
from generate_context_metrics import collect_metrics

REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_OUTPUT = Path("metadata/skill_health.json")
MARKDOWN_OUTPUT = Path("reports/skill-health.md")
ROUTING_FIELDS = (
    "description",
    "use_when",
    "required_inputs",
    "expected_outputs",
    "tags",
    "related_skills",
    "recommended_quality_checks",
)


def _read_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Could not read {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise RuntimeError(f"Expected a JSON object in {path}")
    return data


def _eval_case_count(path: Path) -> int:
    if not path.is_file():
        return 0
    try:
        data = parse_eval_yaml(path.read_text(encoding="utf-8"))
    except EvalParseError:
        return 0
    cases = data.get("cases") if isinstance(data, dict) else None
    return len(cases) if isinstance(cases, list) else 0


def _routing_status(skill: dict[str, Any]) -> tuple[str, list[str]]:
    missing: list[str] = []
    for field in ROUTING_FIELDS:
        if field not in skill:
            missing.append(field)
            continue
        value = skill[field]
        if field == "related_skills":
            if not isinstance(value, list):
                missing.append(field)
        elif not value:
            missing.append(field)
    return ("complete" if not missing else "incomplete", missing)


def _readiness_band(
    eval_status: str,
    eval_case_count: int,
    candidate_output_count: int,
    routing_metadata: str,
) -> str:
    if (
        eval_status == "scored"
        and eval_case_count >= 2
        and candidate_output_count > 0
        and routing_metadata == "complete"
    ):
        return "scored"
    if eval_case_count >= 2 and routing_metadata == "complete":
        return "review-ready"
    return "baseline"


def _priority(
    risk_level: str,
    readiness_band: str,
    context_pressure: str,
    has_example: bool,
    template_count: int,
) -> str:
    """Convert repository evidence into an actionable improvement priority.

    The band is about where maintainers should invest next, not how legally safe
    a skill is to use. Scored, compact skills can be low priority even when the
    underlying legal work is inherently high risk.
    """
    if readiness_band == "baseline":
        return "high"
    if risk_level == "critical" and readiness_band != "scored":
        return "high"
    if readiness_band == "scored" and context_pressure != "large":
        return "low"
    if risk_level == "high" and readiness_band != "scored":
        return "medium"
    if context_pressure == "large" or (not has_example and template_count == 0):
        return "medium"
    return "low"


def collect_health(root: Path | str = REPO_ROOT) -> dict[str, Any]:
    root = Path(root)
    index = _read_json(root / "metadata" / "index.json")
    context_path = root / "metadata" / "context_metrics.json"
    context = _read_json(context_path) if context_path.is_file() else collect_metrics(root)
    context_by_id = {
        item.get("id"): item
        for item in context.get("skills", [])
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }

    records: list[dict[str, Any]] = []
    for skill in index.get("skills", []):
        if not isinstance(skill, dict):
            continue
        skill_id = skill.get("id")
        path_text = skill.get("path")
        if not isinstance(skill_id, str) or not isinstance(path_text, str):
            continue
        area, slug = skill_id.split("/", 1) if "/" in skill_id else ("unknown", skill_id)
        skill_dir = (root / path_text).parent
        eval_path = root / "evals" / "skills" / f"{slug}.eval.yaml"
        eval_cases = _eval_case_count(eval_path)
        candidate_dir = root / "evals" / "outputs" / slug
        candidate_count = (
            len(list(candidate_dir.glob("*.md"))) if candidate_dir.is_dir() else 0
        )
        example_dir = root / "examples" / area / slug
        has_example = example_dir.is_dir() and any(example_dir.rglob("*.md"))
        template_dir = skill_dir / "templates"
        template_count = (
            len(list(template_dir.rglob("*.md"))) if template_dir.is_dir() else 0
        )
        routing_metadata, missing_routing_fields = _routing_status(skill)
        eval_status = str(skill.get("eval_status", "untested"))
        context_record = context_by_id.get(skill_id, {})
        context_pressure = str(context_record.get("context_pressure", "unknown"))
        readiness = _readiness_band(
            eval_status, eval_cases, candidate_count, routing_metadata
        )
        risk_level = str(skill.get("risk_level", "unknown"))

        records.append(
            {
                "id": skill_id,
                "title": skill.get("title") or skill.get("name") or skill_id,
                "path": path_text,
                "practice_area": skill.get("practice_area", area),
                "risk_level": risk_level,
                "eval_status": eval_status,
                "eval_case_count": eval_cases,
                "candidate_output_count": candidate_count,
                "has_example": has_example,
                "template_count": template_count,
                "routing_metadata": routing_metadata,
                "missing_routing_fields": missing_routing_fields,
                "estimated_tokens": context_record.get("estimated_tokens", 0),
                "context_pressure": context_pressure,
                "readiness_band": readiness,
                "improvement_priority": _priority(
                    risk_level,
                    readiness,
                    context_pressure,
                    has_example,
                    template_count,
                ),
            }
        )

    priority_order = {"high": 0, "medium": 1, "low": 2}
    records.sort(
        key=lambda item: (
            priority_order.get(str(item["improvement_priority"]), 9),
            str(item["id"]),
        )
    )
    counts: dict[str, int] = {"high": 0, "medium": 0, "low": 0}
    bands: dict[str, int] = {"scored": 0, "review-ready": 0, "baseline": 0}
    for record in records:
        counts[str(record["improvement_priority"])] += 1
        bands[str(record["readiness_band"])] += 1

    return {
        "schema_version": "1.0",
        "scope_note": (
            "Repository-readiness and maintainability signals only; does not measure "
            "legal correctness, attorney approval, or matter-specific fitness."
        ),
        "skill_count": len(records),
        "priority_counts": counts,
        "readiness_counts": bands,
        "skills": records,
    }


def render_markdown(data: dict[str, Any]) -> str:
    records = list(data.get("skills", []))
    priority_counts = data.get("priority_counts", {})
    readiness_counts = data.get("readiness_counts", {})
    lines = [
        "# AgentCounsel Skill Readiness Scorecard",
        "",
        "Generated by `scripts/generate_skill_health_report.py`. Do not edit by hand.",
        "",
        "This scorecard measures repository-readiness and maintainability signals. "
        "It does not measure legal correctness, attorney approval, or fitness for a real matter.",
        "",
        f"- Skills measured: {data.get('skill_count', 0)}",
        f"- Scored: {readiness_counts.get('scored', 0)}",
        f"- Review-ready: {readiness_counts.get('review-ready', 0)}",
        f"- Baseline: {readiness_counts.get('baseline', 0)}",
        f"- High improvement priority: {priority_counts.get('high', 0)}",
        f"- Medium improvement priority: {priority_counts.get('medium', 0)}",
        f"- Low improvement priority: {priority_counts.get('low', 0)}",
        "",
        "Priority is a maintenance queue, not a legal-risk rating. Baseline skills and "
        "unscored critical workflows are high priority; unscored high-risk workflows, "
        "large-context skills, and skills with neither an example nor a template are "
        "medium priority; scored compact skills can be low priority.",
        "",
        "## Per-skill signals",
        "",
        "| Skill | Risk | Readiness | Priority | Eval cases | Candidates | Example | Templates | Routing | Est. tokens | Pressure |",
        "|---|---|---|---|---:|---:|---|---:|---|---:|---|",
    ]
    for item in records:
        lines.append(
            f"| `{item['id']}` | {item['risk_level']} | {item['readiness_band']} | "
            f"{item['improvement_priority']} | {item['eval_case_count']} | "
            f"{item['candidate_output_count']} | {'yes' if item['has_example'] else 'no'} | "
            f"{item['template_count']} | {item['routing_metadata']} | "
            f"{int(item['estimated_tokens']):,} | {item['context_pressure']} |"
        )
    lines.extend(
        [
            "",
            "The complete machine-readable scorecard is in `metadata/skill_health.json`.",
            "",
        ]
    )
    return "\n".join(lines)


def _expected_outputs(root: Path) -> dict[Path, str]:
    data = collect_health(root)
    return {
        root / JSON_OUTPUT: json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        root / MARKDOWN_OUTPUT: render_markdown(data),
    }


def write_outputs(root: Path | str = REPO_ROOT, check: bool = False) -> bool:
    root = Path(root)
    outputs = _expected_outputs(root)
    if check:
        return all(
            path.is_file() and path.read_text(encoding="utf-8") == content
            for path, content in outputs.items()
        )
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report drift without writing")
    args = parser.parse_args()
    ok = write_outputs(REPO_ROOT, check=args.check)
    if args.check and not ok:
        print("Skill readiness reports are missing or out of date.", file=sys.stderr)
        return 1
    if not args.check:
        print(f"Wrote {JSON_OUTPUT} and {MARKDOWN_OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
