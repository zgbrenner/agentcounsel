"""AgentCounsel MCP server.

Exposes the repository's Markdown-native legal workflow library over MCP.
All returned material is draft workflow guidance for licensed-attorney review,
not legal advice.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parent
SKILLS_ROOT = ROOT / "skills"
CORE_ROOT = ROOT / "core"

mcp = FastMCP(
    "AgentCounsel",
    instructions=(
        "AgentCounsel provides structured legal workflows for draft work product. "
        "Use the narrowest relevant skill, preserve uncertainty, and require review "
        "and adoption by a qualified licensed attorney before reliance. It does not "
        "provide legal advice or create an attorney-client relationship."
    ),
    host="0.0.0.0",
    port=int(os.getenv("PORT", "8000")),
)


def _skill_files() -> list[Path]:
    return sorted(SKILLS_ROOT.glob("**/SKILL.md"))


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _parse_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}

    result: dict[str, Any] = {}
    for line in parts[1].splitlines():
        if ":" not in line or line.startswith((" ", "\t", "-")):
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        if value:
            result[key.strip()] = value
    return result


def _record(path: Path, include_content: bool = False) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    meta = _parse_frontmatter(text)
    skill_id = path.parent.name
    practice_area = path.parent.parent.name if path.parent.parent != SKILLS_ROOT else "general"
    title_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    description = meta.get("description", "")

    item: dict[str, Any] = {
        "id": meta.get("name", skill_id),
        "title": title_match.group(1).strip() if title_match else skill_id.replace("-", " ").title(),
        "practice_area": practice_area,
        "description": description,
        "path": _relative(path),
    }
    if include_content:
        item["content"] = text
    return item


@mcp.tool()
def list_practice_areas() -> list[dict[str, Any]]:
    """List available AgentCounsel practice areas and their skill counts."""
    counts: dict[str, int] = {}
    for path in _skill_files():
        area = path.parent.parent.name if path.parent.parent != SKILLS_ROOT else "general"
        counts[area] = counts.get(area, 0) + 1
    return [
        {"practice_area": area, "skill_count": count}
        for area, count in sorted(counts.items())
    ]


@mcp.tool()
def search_skills(query: str, practice_area: str | None = None, limit: int = 10) -> list[dict[str, Any]]:
    """Search AgentCounsel skills by task, keyword, title, description, or content."""
    query = query.strip().lower()
    if not query:
        raise ValueError("query must not be empty")
    limit = max(1, min(limit, 50))
    terms = [term for term in re.split(r"\W+", query) if term]
    matches: list[tuple[int, dict[str, Any]]] = []

    for path in _skill_files():
        record = _record(path)
        if practice_area and record["practice_area"].lower() != practice_area.lower():
            continue
        text = path.read_text(encoding="utf-8").lower()
        haystack = " ".join(
            [record["id"], record["title"], record["description"], record["practice_area"], text]
        ).lower()
        score = sum(haystack.count(term) for term in terms)
        if query in haystack:
            score += 10
        if score:
            record["relevance_score"] = score
            matches.append((score, record))

    matches.sort(key=lambda item: (-item[0], item[1]["id"]))
    return [record for _, record in matches[:limit]]


@mcp.tool()
def get_skill(skill_id: str) -> dict[str, Any]:
    """Return the complete Markdown workflow for one AgentCounsel skill."""
    normalized = skill_id.strip().lower()
    for path in _skill_files():
        record = _record(path, include_content=True)
        candidates = {
            str(record["id"]).lower(),
            path.parent.name.lower(),
            record["path"].lower(),
        }
        if normalized in candidates:
            return record
    raise ValueError(f"Unknown skill: {skill_id}")


@mcp.tool()
def route_legal_task(task: str, limit: int = 5) -> dict[str, Any]:
    """Route a described legal task to the most relevant AgentCounsel skills."""
    results = search_skills(task, limit=limit)
    return {
        "task": task,
        "recommended_skills": results,
        "usage_note": (
            "Select the narrowest applicable workflow, gather its required inputs, "
            "and require licensed-attorney review before relying on any output."
        ),
    }


@mcp.tool()
def get_core_rules() -> dict[str, str]:
    """Return AgentCounsel's global operating and legal-safety rules."""
    rules: dict[str, str] = {}
    if CORE_ROOT.exists():
        for path in sorted(CORE_ROOT.glob("*.md")):
            rules[_relative(path)] = path.read_text(encoding="utf-8")
    return rules


@mcp.resource("agentcounsel://catalog")
def catalog_resource() -> str:
    """A compact Markdown catalog of every available AgentCounsel skill."""
    lines = ["# AgentCounsel Skill Catalog", ""]
    for path in _skill_files():
        record = _record(path)
        lines.append(
            f"- `{record['id']}` — **{record['title']}** "
            f"({record['practice_area']}): {record['description']}"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
