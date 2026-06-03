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
ROUTER_PATH = REPO_ROOT / "metadata" / "router.json"
EVALS_ROOT = REPO_ROOT / "evals"

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
PLATFORMS = ["chatgpt", "claude", "cursor", "codex", "gemini", "generic-md"]
QUALITY_CHECKS = {
    "assumption-audit": "skills/legal-methodology/assumption-audit/SKILL.md",
    "attorney-review-gate": "skills/legal-methodology/attorney-review-gate/SKILL.md",
    "citation-integrity-check": "skills/legal-methodology/citation-integrity-check/SKILL.md",
    "hallucination-red-team": "skills/legal-methodology/hallucination-red-team/SKILL.md",
    "legal-prose-polish": "skills/legal-methodology/legal-prose-polish/SKILL.md",
    "output-format-compliance-check": "skills/legal-methodology/output-format-compliance-check/SKILL.md",
    "privilege-confidentiality-check": "skills/legal-methodology/privilege-confidentiality-check/SKILL.md",
    "source-validation-check": "skills/legal-methodology/source-validation/SKILL.md",
    "jurisdiction-deadline-gates": "core/jurisdiction-and-deadline-gates.md",
}
EVAL_STATUSES = {
    "scored",
    "manual-eval-ready",
    "untested",
}

ROUTING_EXAMPLES = [
    {
        "request": "Review this NDA",
        "route_type": "one-off skill",
        "route_to": "skills/contracts/nda-review/SKILL.md",
        "missing_facts": [
            "full NDA text",
            "client role: disclosing, receiving, or mutual",
            "transaction context",
            "jurisdiction or governing law if relevant",
        ],
        "quality_checks": [
            "attorney-review-gate",
            "source-validation-check",
            "legal-prose-polish",
        ],
    },
    {
        "request": "Help me respond to opposing counsel",
        "route_type": "matter workspace, then one-off skill",
        "route_to": "skills/litigation/matter-intake/SKILL.md",
        "fallback_routes": [
            "skills/litigation/demand-letter/SKILL.md",
            "skills/legal-research/legal-research-memo/SKILL.md",
        ],
        "missing_facts": [
            "matter posture",
            "opposing counsel communication",
            "jurisdiction and venue",
            "deadlines or response date",
            "client objective and authorized tone",
        ],
        "quality_checks": [
            "attorney-review-gate",
            "source-validation-check",
            "hallucination-red-team",
            "privilege-confidentiality-check",
            "jurisdiction-deadline-gates",
        ],
    },
    {
        "request": "Summarize this new privacy rule",
        "route_type": "one-off skill with mandatory source validation",
        "route_to": "skills/regulatory/rule-change-summary/SKILL.md",
        "missing_facts": [
            "rule text or official source URL",
            "issuing authority",
            "effective date",
            "affected business activity",
            "jurisdiction",
        ],
        "quality_checks": [
            "attorney-review-gate",
            "citation-integrity-check",
            "source-validation-check",
            "jurisdiction-deadline-gates",
        ],
    },
    {
        "request": "Draft a demand letter",
        "route_type": "one-off skill",
        "route_to": "skills/litigation/demand-letter/SKILL.md",
        "missing_facts": [
            "parties",
            "factual chronology",
            "claim theory supplied by counsel",
            "jurisdiction",
            "response deadline or desired date",
            "settlement authority",
        ],
        "quality_checks": [
            "attorney-review-gate",
            "citation-integrity-check",
            "source-validation-check",
            "hallucination-red-team",
            "privilege-confidentiality-check",
            "jurisdiction-deadline-gates",
        ],
    },
    {
        "request": "Check this contract for risk",
        "route_type": "one-off skill or practice-area pack",
        "route_to": "skills/contracts/contract-risk-review/SKILL.md",
        "missing_facts": [
            "contract text",
            "client role",
            "business context",
            "governing law if supplied",
            "client fallback positions or playbook",
        ],
        "quality_checks": [
            "attorney-review-gate",
            "source-validation-check",
            "assumption-audit",
            "legal-prose-polish",
        ],
    },
    {
        "request": "I need help with a California employee termination",
        "route_type": "matter workspace, then one-off skill",
        "route_to": "skills/employment/termination-risk/SKILL.md",
        "missing_facts": [
            "employee role and tenure",
            "termination reason",
            "protected-class, leave, accommodation, retaliation, or complaint facts",
            "California work location and governing policy documents",
            "planned termination date",
        ],
        "quality_checks": [
            "attorney-review-gate",
            "source-validation-check",
            "assumption-audit",
            "hallucination-red-team",
            "jurisdiction-deadline-gates",
            "privilege-confidentiality-check",
        ],
    },
    {
        "request": "Open a new acquisition that will run for months with diligence, drafts, and deadlines",
        "route_type": "matter workspace",
        "route_to": "matter-workspaces/_template/",
        "why": (
            "Multi-step, document-heavy, deadline-sensitive, and ongoing — the "
            "matter needs a single organizing workspace before any one-off skill. "
            "Initialize with scripts/init_matter_workspace.py."
        ),
        "missing_facts": [
            "deal type, side, and structure",
            "parties and jurisdiction",
            "key deadlines",
            "document set",
            "supervising attorney",
        ],
        "quality_checks": [
            "attorney-review-gate",
            "source-validation-check",
            "assumption-audit",
            "citation-integrity-check",
            "privilege-confidentiality-check",
            "jurisdiction-deadline-gates",
        ],
    },
    {
        "request": "Run a full multi-pass review of this negotiated contract before signing",
        "route_type": "review panel",
        "route_to": "review-panels/contract-review-panel.md",
        "why": (
            "High-risk draft needing several review lenses (issue spotter, "
            "source/citation, client-position, business-risk) before the attorney "
            "gatekeeper. Review passes are not autonomous agents or lawyers — the "
            "output stays attorney-supervised draft work product."
        ),
        "missing_facts": [
            "final contract text",
            "client role and priorities",
            "client fallback positions",
            "governing law",
        ],
        "quality_checks": [
            "attorney-review-gate",
            "source-validation-check",
            "assumption-audit",
            "privilege-confidentiality-check",
            "legal-prose-polish",
        ],
    },
    {
        "request": "We review NDAs the same way every week — give me a repeatable recipe",
        "route_type": "playbook",
        "route_to": "playbooks/nda-review.md",
        "why": (
            "A recurring task type benefits from a playbook's default client-position "
            "questions, risk-tolerance settings, required source materials, and "
            "required quality checks, anchored on skills/contracts/nda-review/SKILL.md."
        ),
        "missing_facts": [
            "full NDA text",
            "client role: disclosing, receiving, or mutual",
            "transaction context",
            "client risk tolerance",
        ],
        "quality_checks": [
            "attorney-review-gate",
            "source-validation-check",
            "legal-prose-polish",
        ],
    },
    {
        "request": "We handle the same kind of contract work in this practice area repeatedly",
        "route_type": "practice-area pack",
        "route_to": "practice-profiles/contracts.md",
        "why": (
            "Repeated work in one practice area is best configured with the "
            "practice profile and the platform pack generated for that area, rather "
            "than re-selecting individual skills each time."
        ),
        "missing_facts": [
            "practice area",
            "team configuration and house positions",
            "platform in use",
        ],
        "quality_checks": [
            "attorney-review-gate",
            "source-validation-check",
        ],
    },
    {
        "request": "Just check this finished memo for invented or unsupported citations",
        "route_type": "quality check",
        "route_to": "skills/legal-methodology/citation-integrity-check/SKILL.md",
        "why": (
            "A self-contained review pass over an existing draft — no new matter or "
            "workspace needed. Pair with source-validation-check and "
            "hallucination-red-team for authority-heavy drafts."
        ),
        "missing_facts": [
            "the draft to review",
            "the sources relied upon",
            "jurisdiction if authorities are jurisdiction-specific",
        ],
        "quality_checks": [
            "citation-integrity-check",
            "source-validation-check",
            "hallucination-red-team",
        ],
    },
]


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
    fm_lines, body = split_frontmatter(md.read_text(encoding="utf-8"))
    meta = parse_frontmatter(fm_lines or [])
    area = skill_dir.parent.name
    slug = skill_dir.name
    skill_id = f"{area}/{slug}"
    use_when = extract_use_when(body or "")
    requires_jurisdiction = bool(meta.get("jurisdictions")) or _mentions(
        body or "", ["jurisdiction", "governing law", "venue", "forum"])
    requires_deadline_check = _mentions(
        body or "", ["deadline", "due date", "effective date", "response date"])
    eval_status = eval_coverage_status(area, slug)
    record = {
        "id": skill_id,
        "title": meta.get("name"),
        "path": rel(md),
        "summary": meta.get("description"),
        "use_when": use_when or [meta.get("description")],
        "required_inputs": meta.get("inputs"),
        "expected_outputs": meta.get("outputs"),
        "category": meta.get("task_type"),
        "requires_jurisdiction": requires_jurisdiction,
        "requires_deadline_check": requires_deadline_check,
        "recommended_quality_checks": recommended_quality_checks(
            meta, requires_jurisdiction, requires_deadline_check, body or ""),
        "compatible_platforms": list(PLATFORMS),
        "pack_tags": pack_tags(meta, area),
        "eval_status": eval_status,
    }
    for field in REQUIRED_FIELDS:
        record[field] = meta.get(field)
    return record


def _mentions(text: str, needles: list[str]) -> bool:
    low = text.lower()
    return any(n in low for n in needles)


def extract_use_when(body: str) -> list[str]:
    section = extract_section(body, "Use When")
    items: list[str] = []
    for line in section.splitlines():
        m = re.match(r"^\s*[-*]\s+(.+?)\s*$", line)
        if m:
            item = re.sub(r"[*`]", "", m.group(1)).strip()
            if item:
                items.append(item)
    return items


def extract_section(body: str, section: str) -> str:
    pattern = re.compile(rf"^##\s+{re.escape(section)}\s*$", re.M)
    match = pattern.search(body)
    if not match:
        return ""
    next_heading = re.search(r"^##\s+\S", body[match.end():], re.M)
    end = match.end() + next_heading.start() if next_heading else len(body)
    return body[match.end():end].strip()


def recommended_quality_checks(meta: dict, requires_jurisdiction: bool,
                               requires_deadline_check: bool,
                               body: str) -> list[str]:
    checks = ["attorney-review-gate"]
    task_type = meta.get("task_type")
    risk_level = meta.get("risk_level")
    tags = set(meta.get("tags") or [])
    authority_involved = (
        task_type in {"research", "verification", "analysis"}
        or _mentions(body, ["citation", "authority", "statute", "case law",
                            "regulation", "source validation", "quotation"])
    )
    if task_type == "drafting":
        checks.extend(["legal-prose-polish", "output-format-compliance-check"])
    if task_type == "research":
        checks.extend(["citation-integrity-check", "source-validation-check"])
    if task_type == "review":
        checks.extend(["source-validation-check", "assumption-audit"])
    if task_type in {"analysis", "triage", "extraction", "summarization"}:
        checks.append("assumption-audit")
    if authority_involved:
        checks.extend(["citation-integrity-check", "source-validation-check"])
    if risk_level in {"high", "critical"}:
        checks.extend(["attorney-review-gate", "assumption-audit",
                       "hallucination-red-team"])
        if authority_involved:
            checks.append("citation-integrity-check")
    if requires_jurisdiction or requires_deadline_check:
        checks.append("jurisdiction-deadline-gates")
    if (_mentions(body, ["privilege", "confidential", "work product",
                         "opposing counsel", "demand letter", "send",
                         "external", "regulator", "court", "client update"])
            or {"litigation", "demand-letter", "client-communication"} & tags):
        checks.append("privilege-confidentiality-check")
    if _mentions(body, ["memo", "email", "letter", "matrix", "chronology",
                        "checklist", "table", "client update", "summary"]):
        checks.append("output-format-compliance-check")
    return sorted(set(checks), key=checks.index)


def pack_tags(meta: dict, area: str) -> list[str]:
    tags = [area, meta.get("task_type"), meta.get("risk_level")]
    tags.extend(meta.get("tags") or [])
    return sorted({t for t in tags if isinstance(t, str) and t.strip()})


def eval_coverage_status(area: str, slug: str) -> str:
    eval_candidates = [
        EVALS_ROOT / "skills" / f"{slug}.eval.yaml",
        EVALS_ROOT / "skills" / f"{area}-{slug}.eval.yaml",
    ]
    if not any(path.is_file() for path in eval_candidates):
        return "untested"
    output_dirs = [
        EVALS_ROOT / "outputs" / slug,
        EVALS_ROOT / "outputs" / f"{area}-{slug}",
    ]
    if any(output_dir.is_dir() and any(output_dir.glob("*.md"))
           for output_dir in output_dirs):
        return "scored"
    return "manual-eval-ready"


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
        "normalized_schema_version": "1.0",
        "skill_count": len(records),
        "platforms": list(PLATFORMS),
        "quality_checks": [
            {"id": qid, "path": path}
            for qid, path in sorted(QUALITY_CHECKS.items())
        ],
        "practice_areas": counts("practice_area"),
        "task_types": counts("task_type"),
        "risk_levels": risk_counts,
        "skills": records,
    }


def render_index() -> str:
    return json.dumps(build_index(), indent=2, ensure_ascii=False) + "\n"


def build_router() -> dict:
    index = build_index()
    routes = []
    for skill in index["skills"]:
        routes.append({
            "id": skill["id"],
            "title": skill["title"],
            "route_type": "one-off skill",
            "path": skill["path"],
            "practice_area": skill["practice_area"],
            "category": skill["category"],
            "summary": skill["summary"],
            "triggers": skill["use_when"],
            "required_inputs": skill["required_inputs"],
            "jurisdiction_gate": skill["requires_jurisdiction"],
            "deadline_gate": skill["requires_deadline_check"],
            "attorney_escalation": (
                "Required before reliance; escalate immediately for missing "
                "jurisdiction, missing deadlines, source uncertainty, "
                "privilege/confidentiality risk, or any high-stakes legal "
                "conclusion."
            ),
            "recommended_quality_checks": skill["recommended_quality_checks"],
            "source_validation_mandatory": (
                "source-validation" in skill["recommended_quality_checks"]
            ),
            "related_skills": skill["related_skills"],
        })
    return {
        "generated_by": "scripts/build_skill_index.py",
        "schema_version": "1.0",
        "routing_order": [
            "matter workspace for multi-step, document-heavy, high-risk, ongoing, "
            "jurisdiction-sensitive, deadline-sensitive, or source/citation-heavy matters",
            "review panel for a structured multi-pass supervised review of a draft or document",
            "playbook for a recurring task type that needs default questions, "
            "risk-tolerance settings, and required quality checks",
            "matter pack for recurring multi-skill matter types",
            "practice-area pack for repeated work in one practice area",
            "one-off skill for a self-contained task",
            "quality check for review, source validation, or red-team passes",
        ],
        "workspace_triggers": [
            "multi-step",
            "document-heavy",
            "high-risk",
            "ongoing",
            "jurisdiction-sensitive",
            "deadline-sensitive",
            "source/citation-heavy",
            "likely to require multiple quality checks",
            "likely to require attorney escalation",
        ],
        "route_types": [
            "one-off skill",
            "practice-area pack",
            "matter pack",
            "matter workspace",
            "quality check",
            "review panel",
        ],
        "quality_checks": list(sorted(QUALITY_CHECKS)),
        "examples": ROUTING_EXAMPLES,
        "routes": routes,
    }


def render_router() -> str:
    return json.dumps(build_router(), indent=2, ensure_ascii=False) + "\n"


def validate_normalized_index(data: dict | None = None) -> list[str]:
    data = data or build_index()
    errors: list[str] = []
    valid_platforms = set(PLATFORMS)
    valid_checks = set(QUALITY_CHECKS)
    seen: set[str] = set()
    for skill in data.get("skills", []):
        sid = skill.get("id")
        path = skill.get("path")
        if not sid:
            errors.append(f"{path or '<unknown>'}: missing normalized id")
        elif sid in seen:
            errors.append(f"{path}: duplicate normalized id '{sid}'")
        else:
            seen.add(sid)
        if not path or not (REPO_ROOT / path).is_file():
            errors.append(f"{sid or '<unknown>'}: metadata path does not exist")
        if skill.get("risk_level") not in RISK_LEVELS:
            errors.append(f"{path}: invalid risk_level '{skill.get('risk_level')}'")
        for platform in skill.get("compatible_platforms") or []:
            if platform not in valid_platforms:
                errors.append(f"{path}: invalid compatible platform '{platform}'")
        for check in skill.get("recommended_quality_checks") or []:
            if check not in valid_checks:
                errors.append(f"{path}: unknown quality check '{check}'")
            elif not (REPO_ROOT / QUALITY_CHECKS[check]).exists():
                errors.append(f"{path}: quality check target missing for '{check}'")
        checks = set(skill.get("recommended_quality_checks") or [])
        if skill.get("risk_level") in {"high", "critical"}:
            for required in ("attorney-review-gate", "assumption-audit"):
                if required not in checks:
                    errors.append(f"{path}: high-risk skill missing '{required}'")
            if ("citation" in " ".join(skill.get("pack_tags") or [])
                    or "source-validation-check" in checks):
                if "citation-integrity-check" not in checks:
                    errors.append(f"{path}: authority-related high-risk skill "
                                  "missing 'citation-integrity-check'")
        if skill.get("eval_status") not in EVAL_STATUSES:
            errors.append(f"{path}: invalid eval_status '{skill.get('eval_status')}'")
    canonical_paths = {rel(d / "SKILL.md") for d in canonical_skill_dirs()}
    indexed_paths = {s.get("path") for s in data.get("skills", [])}
    for missing in sorted(canonical_paths - indexed_paths):
        errors.append(f"{missing}: skill missing from metadata/index.json")
    return errors


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
    ROUTER_PATH.write_text(render_router(), encoding="utf-8")
    print("AgentCounsel skill metadata index")
    print(f"  skills indexed: {len(skill_dirs)}")
    print(f"  wrote {rel(INDEX_PATH)}")
    print(f"  wrote {rel(ROUTER_PATH)}")
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
    expected_router = render_router()
    if not ROUTER_PATH.is_file():
        print(f"MISSING: {rel(ROUTER_PATH)} has not been generated.")
        print("Run 'python scripts/build_skill_index.py'.")
        return 1
    if ROUTER_PATH.read_text(encoding="utf-8") != expected_router:
        print(f"STALE: {rel(ROUTER_PATH)} is out of date.")
        print("Run 'python scripts/build_skill_index.py'.")
        return 1
    normalized_errors = validate_normalized_index()
    if normalized_errors:
        print("Normalized metadata validation failed:")
        for msg in normalized_errors:
            print(f"  x {msg}")
        return 1
    print(f"{rel(INDEX_PATH)} and {rel(ROUTER_PATH)} are up to date "
          f"({len(skill_dirs)} skills).")
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
