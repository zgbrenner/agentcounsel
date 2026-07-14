#!/usr/bin/env python3
"""Generate deterministic context-size metrics for AgentCounsel.

The estimates are planning signals, not provider token counts or billing data.
One estimated token equals four UTF-8 text characters, rounded up.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_OUTPUT = Path("metadata/context_metrics.json")
MARKDOWN_OUTPUT = Path("reports/context-metrics.md")
PATH_RE = re.compile(r"(?:skills|core|matter-workspaces|matter-packs|playbooks|review-panels|overlays)/[A-Za-z0-9_./-]+")
NUMBERED_ITEM_RE = re.compile(r"^\s*\d+\.\s+", re.M)
BULLET_ITEM_RE = re.compile(r"^\s*[-*]\s+", re.M)


def estimate_tokens(characters: int) -> int:
    """Estimate tokens at one token per four characters, rounded up."""
    if characters <= 0:
        return 0
    return math.ceil(characters / 4)


def _read_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Could not read {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise RuntimeError(f"Expected a JSON object in {path}")
    return data


def _extract_h2(body: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$", body, re.M)
    if not match:
        return ""
    start = match.end()
    next_heading = re.search(r"^##\s+", body[start:], re.M)
    end = start + next_heading.start() if next_heading else len(body)
    return body[start:end].strip()


def _count_output_items(text: str) -> int:
    section = _extract_h2(text, "Output Format")
    numbered = NUMBERED_ITEM_RE.findall(section)
    if numbered:
        return len(numbered)
    return len(BULLET_ITEM_RE.findall(section))


def _linked_paths(text: str, marker: str) -> set[str]:
    return {
        match
        for match in PATH_RE.findall(text)
        if f"/{marker}/" in match and match.endswith(".md")
    }


def _pressure(tokens: int) -> str:
    if tokens <= 2500:
        return "compact"
    if tokens <= 6000:
        return "moderate"
    return "large"


def _pack_paths(root: Path, pack: dict[str, Any]) -> list[str]:
    paths: set[str] = set()
    for key, value in pack.items():
        if not key.startswith("included_") or not isinstance(value, list):
            continue
        for item in value:
            if not isinstance(item, str) or "/" not in item:
                continue
            candidate = root / item
            if candidate.is_file():
                paths.add(item)
    return sorted(paths)


def collect_metrics(root: Path | str = REPO_ROOT) -> dict[str, Any]:
    root = Path(root)
    index = _read_json(root / "metadata" / "index.json")
    packs_data = _read_json(root / "metadata" / "packs.json")

    skill_metrics: list[dict[str, Any]] = []
    for skill in index.get("skills", []):
        if not isinstance(skill, dict):
            continue
        path_text = skill.get("path")
        skill_id = skill.get("id")
        if not isinstance(path_text, str) or not isinstance(skill_id, str):
            continue
        path = root / path_text
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        characters = len(text)
        tokens = estimate_tokens(characters)
        skill_metrics.append(
            {
                "id": skill_id,
                "title": skill.get("title") or skill.get("name") or skill_id,
                "path": path_text,
                "practice_area": skill.get("practice_area", "unknown"),
                "risk_level": skill.get("risk_level", "unknown"),
                "characters": characters,
                "estimated_tokens": tokens,
                "context_pressure": _pressure(tokens),
                "output_section_count": _count_output_items(text),
                "reference_link_count": len(_linked_paths(text, "references")),
                "template_link_count": len(_linked_paths(text, "templates")),
                "related_skill_count": len(skill.get("related_skills", []))
                if isinstance(skill.get("related_skills"), list)
                else 0,
            }
        )
    skill_metrics.sort(key=lambda item: item["id"])

    pack_metrics: list[dict[str, Any]] = []
    for pack in packs_data.get("packs", []):
        if not isinstance(pack, dict):
            continue
        paths = _pack_paths(root, pack)
        characters = sum(len((root / path).read_text(encoding="utf-8")) for path in paths)
        tokens = estimate_tokens(characters)
        pack_metrics.append(
            {
                "pack_id": pack.get("pack_id", "unknown"),
                "platform": pack.get("platform", "unknown"),
                "practice_area": pack.get("practice_area", "unknown"),
                "included_file_count": len(paths),
                "characters": characters,
                "estimated_tokens": tokens,
                "context_pressure": _pressure(tokens),
            }
        )
    pack_metrics.sort(key=lambda item: str(item["pack_id"]))

    return {
        "schema_version": "1.0",
        "approximation": "one token per four characters, rounded up",
        "skill_count": len(skill_metrics),
        "pack_count": len(pack_metrics),
        "skills": skill_metrics,
        "packs": pack_metrics,
    }


def render_markdown(data: dict[str, Any]) -> str:
    skills = list(data.get("skills", []))
    packs = list(data.get("packs", []))
    largest_skills = sorted(
        skills, key=lambda item: (-int(item["estimated_tokens"]), str(item["id"]))
    )[:25]
    largest_packs = sorted(
        packs, key=lambda item: (-int(item["estimated_tokens"]), str(item["pack_id"]))
    )[:25]

    lines = [
        "# AgentCounsel Context Metrics",
        "",
        "Generated by `scripts/generate_context_metrics.py`. Do not edit by hand.",
        "",
        "These figures are a context-planning signal, not provider token counts or billing data. "
        "The deterministic approximation is one token per four characters, rounded up.",
        "",
        f"- Skills measured: {data.get('skill_count', 0)}",
        f"- Packs measured: {data.get('pack_count', 0)}",
        "",
        "Context pressure bands for individual files are: compact (up to 2,500 estimated tokens), "
        "moderate (2,501–6,000), and large (more than 6,000).",
        "",
        "## Largest skills",
        "",
        "| Skill | Practice area | Risk | Estimated tokens | Output items | References | Templates | Pressure |",
        "|---|---|---|---:|---:|---:|---:|---|",
    ]
    for item in largest_skills:
        lines.append(
            f"| `{item['id']}` | {item['practice_area']} | {item['risk_level']} | "
            f"{item['estimated_tokens']:,} | {item['output_section_count']} | "
            f"{item['reference_link_count']} | {item['template_link_count']} | "
            f"{item['context_pressure']} |"
        )

    lines.extend(
        [
            "",
            "## Largest generated packs",
            "",
            "| Pack | Platform | Practice area | Files | Estimated tokens | Pressure |",
            "|---|---|---|---:|---:|---|",
        ]
    )
    for item in largest_packs:
        lines.append(
            f"| `{item['pack_id']}` | {item['platform']} | {item['practice_area']} | "
            f"{item['included_file_count']} | {item['estimated_tokens']:,} | "
            f"{item['context_pressure']} |"
        )

    lines.extend(
        [
            "",
            "The complete per-skill and per-pack dataset is in `metadata/context_metrics.json`.",
            "",
        ]
    )
    return "\n".join(lines)


def _expected_outputs(root: Path) -> dict[Path, str]:
    data = collect_metrics(root)
    json_text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    return {
        root / JSON_OUTPUT: json_text,
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
        print("Context metrics are missing or out of date.", file=sys.stderr)
        return 1
    if not args.check:
        print(f"Wrote {JSON_OUTPUT} and {MARKDOWN_OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
