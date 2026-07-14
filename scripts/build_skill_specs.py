#!/usr/bin/env python3
"""Build the generated AgentCounsel Skill Specification v2 registry.

Every canonical ``SKILL.md`` compiles to a safe typed execution contract.
An optional sibling ``SPEC.json`` may enrich that contract, but may not weaken
baseline legal-safety controls. The generated output is written to
``metadata/skill_specs.json``.

Standard library only. Run from anywhere:

    python scripts/build_skill_specs.py
    python scripts/build_skill_specs.py --check
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import build_skill_index
from _shared import load_frontmatter
from skill_spec_v2 import SCHEMA_VERSION, compile_skill_spec

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
OUTPUT_PATH = REPO_ROOT / "metadata" / "skill_specs.json"
NON_SKILL_DIRS = {"references"}


def canonical_skill_dirs(root: Path) -> list[Path]:
    """Return every canonical skill directory in stable path order."""
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return []
    result: list[Path] = []
    for area in sorted(path for path in skills_root.iterdir() if path.is_dir()):
        for skill_dir in sorted(path for path in area.iterdir() if path.is_dir()):
            if skill_dir.name in NON_SKILL_DIRS:
                continue
            if (skill_dir / "SKILL.md").is_file():
                result.append(skill_dir)
    return result


def _mentions(text: str, needles: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(needle in lowered for needle in needles)


def _metadata_text(metadata: dict[str, Any]) -> str:
    """Collapse routing-relevant metadata into text for conservative gate detection."""
    values: list[str] = []
    for field in ("description", "inputs", "outputs", "tags"):
        value = metadata.get(field)
        if isinstance(value, str):
            values.append(value)
        elif isinstance(value, list):
            values.extend(item for item in value if isinstance(item, str))
    return "\n".join(values)


def _derived_fields(metadata: dict[str, Any], body: str) -> dict[str, Any]:
    searchable_text = body + "\n" + _metadata_text(metadata)
    requires_jurisdiction = bool(metadata.get("jurisdictions")) or _mentions(
        searchable_text, ("jurisdiction", "governing law", "venue", "forum")
    )
    requires_deadline_check = _mentions(
        searchable_text,
        (
            "deadline",
            "due date",
            "effective date",
            "response date",
            "trigger date",
            "notification window",
        ),
    )
    quality_checks = build_skill_index.recommended_quality_checks(
        metadata,
        requires_jurisdiction,
        requires_deadline_check,
        body,
    )
    return {
        "requires_jurisdiction": requires_jurisdiction,
        "requires_deadline_check": requires_deadline_check,
        "recommended_quality_checks": quality_checks,
    }


def collect_skill_specs(root: Path | str = REPO_ROOT) -> dict[str, Any]:
    """Compile and validate every canonical skill under ``root``."""
    root = Path(root).resolve()
    records: list[dict[str, Any]] = []
    custom_by_area: dict[str, int] = {}

    for skill_dir in canonical_skill_dirs(root):
        text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        metadata, body = load_frontmatter(text)
        if not metadata:
            raise ValueError(f"{skill_dir / 'SKILL.md'}: missing YAML frontmatter")
        derived = _derived_fields(metadata, body)
        compiled = compile_skill_spec(skill_dir, metadata, body, derived, root)
        records.append(compiled)
        if compiled["has_custom_spec"]:
            area = str(metadata.get("practice_area", skill_dir.parent.name))
            custom_by_area[area] = custom_by_area.get(area, 0) + 1

    records.sort(key=lambda item: str(item["skill_id"]))
    custom_count = sum(1 for item in records if item["has_custom_spec"])
    return {
        "schema_version": SCHEMA_VERSION,
        "skill_count": len(records),
        "custom_spec_count": custom_count,
        "legacy_compiled_count": len(records) - custom_count,
        "custom_specs_by_practice_area": dict(sorted(custom_by_area.items())),
        "skills": records,
    }


def render_output(data: dict[str, Any]) -> str:
    """Render the registry as deterministic pretty-printed JSON."""
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def write_output(root: Path | str = REPO_ROOT, check: bool = False) -> bool:
    """Write the generated registry, or return whether it is current."""
    root = Path(root).resolve()
    output_path = root / "metadata" / "skill_specs.json"
    expected = render_output(collect_skill_specs(root))
    if check:
        return output_path.is_file() and output_path.read_text(encoding="utf-8") == expected
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(expected, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero when metadata/skill_specs.json is missing or stale",
    )
    args = parser.parse_args()
    current = write_output(REPO_ROOT, check=args.check)
    if args.check and not current:
        print("metadata/skill_specs.json is missing or out of date.", file=sys.stderr)
        return 1
    if not args.check:
        data = collect_skill_specs(REPO_ROOT)
        print(
            f"Wrote metadata/skill_specs.json: {data['skill_count']} skills, "
            f"{data['custom_spec_count']} custom specs."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
