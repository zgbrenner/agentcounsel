#!/usr/bin/env python3
"""AgentCounsel repository validation.

Lightweight structural and consistency checks for the AgentCounsel legal
skills library. Standard library only — no third-party packages, no build
tools. Run from anywhere:

    python scripts/validate_repo.py

Exit code 0 if all checks pass, 1 if any error is found. Warnings do not
affect the exit code. See VALIDATION.md for details.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Allow importing sibling scripts (e.g. sync_plugin_skills) when run directly.
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


# Required H2 sections for every canonical skill, in order.
REQUIRED_SECTIONS = [
    "## Purpose",
    "## Use When",
    "## Required Inputs",
    "## Do Not Use When",
    "## Legal Safety Rules",
    "## Workflow",
    "## Output Format",
    "## Attorney Verification Checklist",
]

# Content-scan file types.
TEXT_SUFFIXES = {".md", ".json", ".py", ".txt"}


def parse_frontmatter(text: str):
    """Return (frontmatter_lines, body) or (None, None) if absent/unterminated."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "\n".join(lines[i + 1:])
    return None, None


def strip_code_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def canonical_skill_dirs() -> list[Path]:
    base = REPO_ROOT / "skills"
    dirs: list[Path] = []
    if not base.is_dir():
        err("skills/ directory not found")
        return dirs
    for area in sorted(p for p in base.iterdir() if p.is_dir()):
        for skill in sorted(p for p in area.iterdir() if p.is_dir()):
            dirs.append(skill)
    return dirs


def plugin_skill_dirs() -> list[Path]:
    base = REPO_ROOT / "adapters" / "claude-code-plugin" / "skills"
    if not base.is_dir():
        return []
    return sorted(p for p in base.iterdir() if p.is_dir())


def iter_text_files():
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def excluded_from_content_scan(path: Path) -> bool:
    """The validator and its docs legitimately mention the forbidden strings."""
    parts = path.relative_to(REPO_ROOT).parts
    if parts and parts[0] == "scripts":
        return True
    if path.name == "VALIDATION.md":
        return True
    return False


# --- Check: skill structure ------------------------------------------------

def check_skill(skill_dir: Path, require_sections: bool) -> None:
    md = skill_dir / "SKILL.md"
    if not md.is_file():
        err(f"{rel(skill_dir)}: missing SKILL.md")
        return
    text = md.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    if frontmatter is None:
        err(f"{rel(md)}: missing or unterminated YAML frontmatter "
            f"(file must start with '---' and have a closing '---')")
        return
    fm_text = "\n".join(frontmatter)
    if not re.search(r"^name:\s*\S", fm_text, re.M):
        err(f"{rel(md)}: frontmatter is missing a non-empty 'name:' field")
    if not re.search(r"^description:\s*\S", fm_text, re.M):
        err(f"{rel(md)}: frontmatter is missing a non-empty 'description:' field")

    if not re.search(r"^#\s+\S", body, re.M):
        err(f"{rel(md)}: missing an H1 title ('# Skill Name')")

    if not require_sections:
        return

    positions: dict[str, int] = {}
    for section in REQUIRED_SECTIONS:
        match = re.search(rf"^{re.escape(section)}\s*$", body, re.M)
        if match is None:
            err(f"{rel(md)}: missing required section '{section}'")
        else:
            positions[section] = match.start()
    found_order = [positions[s] for s in REQUIRED_SECTIONS if s in positions]
    if found_order != sorted(found_order):
        err(f"{rel(md)}: required sections are present but out of order")


# --- Check: forbidden phrasing --------------------------------------------

def check_content_scans() -> None:
    forbidden = ["chatgpt project instructions", "chatgpt project package"]
    advice_pat = re.compile(
        r"(provides?|gives?|offers?|renders?)\s+(final\s+)?legal\s+advice"
        r"|\bis\s+legal\s+advice",
        re.I,
    )
    negation_pat = re.compile(
        r"(\bnot\b|\bnever\b|\bno\b|\bnone\b|\bneither\b|\bcannot\b|n't)", re.I)
    todo_pat = re.compile(r"\bTODO\b|\bFIXME\b|lorem ipsum", re.I)

    for path in iter_text_files():
        if excluded_from_content_scan(path):
            continue
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        for phrase in forbidden:
            if phrase in lowered:
                err(f"{rel(path)}: contains forbidden phrase '{phrase}'")
        for match in advice_pat.finditer(text):
            window = text[max(0, match.start() - 48):match.start()]
            if not negation_pat.search(window):
                snippet = match.group(0).strip()
                err(f"{rel(path)}: appears to state that AgentCounsel "
                    f"provides legal advice ('{snippet}') — outputs must be "
                    f"described as draft legal work product for attorney review")
        for match in todo_pat.finditer(text):
            err(f"{rel(path)}: leftover placeholder marker '{match.group(0)}'")


# --- Check: relative links resolve ----------------------------------------

LINK_PAT = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def check_links() -> None:
    for path in iter_text_files():
        if path.suffix.lower() != ".md":
            continue
        text = strip_code_fences(path.read_text(encoding="utf-8"))
        for match in LINK_PAT.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0].strip()
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                err(f"{rel(path)}: broken relative link -> '{target}'")


# --- Check: index paths ---------------------------------------------------

SKILL_PATH_PAT = re.compile(r"skills/[A-Za-z0-9_./-]+?/SKILL\.md")


def check_index_paths(index_name: str) -> None:
    index = REPO_ROOT / index_name
    if not index.is_file():
        err(f"{index_name}: file not found")
        return
    text = index.read_text(encoding="utf-8")
    referenced = sorted(set(SKILL_PATH_PAT.findall(text)))
    if not referenced:
        warn(f"{index_name}: no skill paths found to validate")
    for skill_path in referenced:
        if not (REPO_ROOT / skill_path).is_file():
            err(f"{index_name}: references missing skill path '{skill_path}'")


# --- Check: adapters point back to canonical ------------------------------

def check_adapters() -> None:
    back_refs = {
        "adapters/codex/SKILLS_INDEX.md": "../../SKILLS_INDEX.md",
        "adapters/claude-cowork/SKILLS_INDEX.md": "../../SKILLS_INDEX.md",
        "adapters/claude-cowork/WORKFLOW_ROUTER.md": "../../WORKFLOW_ROUTER.md",
    }
    for name, expected in back_refs.items():
        path = REPO_ROOT / name
        if not path.is_file():
            err(f"{name}: adapter file not found")
            continue
        if expected not in path.read_text(encoding="utf-8"):
            err(f"{name}: should point back to the canonical root file "
                f"('{expected}')")

    agents = REPO_ROOT / "adapters" / "codex" / "AGENTS.md"
    if agents.is_file() and "/skills" not in agents.read_text(encoding="utf-8"):
        err("adapters/codex/AGENTS.md: should direct repo agents to the "
            "canonical '/skills' library")


# --- Check: plugin manifest ------------------------------------------------

def check_plugin_manifest() -> None:
    manifest = REPO_ROOT / "adapters" / "claude-code-plugin" / "plugin.json"
    if not manifest.is_file():
        err("adapters/claude-code-plugin/plugin.json: file not found")
        return
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        err(f"adapters/claude-code-plugin/plugin.json: invalid JSON ({exc})")
        return
    for field in ("name", "version", "description"):
        if not data.get(field):
            err(f"adapters/claude-code-plugin/plugin.json: missing '{field}'")


# --- Check: every canonical skill is catalogued ---------------------------

def check_index_coverage(skill_dirs: list[Path]) -> None:
    index = REPO_ROOT / "SKILLS_INDEX.md"
    if not index.is_file():
        return
    text = index.read_text(encoding="utf-8")
    for skill_dir in skill_dirs:
        skill_path = rel(skill_dir / "SKILL.md")
        if skill_path not in text:
            warn(f"{skill_path}: not listed in SKILLS_INDEX.md")


# --- Check: plugin bundle is present and in sync --------------------------

def check_plugin_bundle() -> None:
    """Detect Claude Code plugin bundle drift against canonical /skills."""
    try:
        import sync_plugin_skills as sync
    except Exception as exc:  # pragma: no cover - defensive
        warn(f"could not run plugin bundle checks (import failed: {exc})")
        return

    expected = list(sync.CURATED_BUNDLE) + list(sync.MAINTAINED_SKILLS)

    for name in expected:
        skill_md = sync.PLUGIN_ROOT / name / "SKILL.md"
        if not skill_md.is_file():
            err(f"plugin bundle: expected skill '{name}' is missing "
                f"({rel(skill_md)})")

    if sync.PLUGIN_ROOT.is_dir():
        for sub in sorted(p for p in sync.PLUGIN_ROOT.iterdir() if p.is_dir()):
            if sub.name not in expected:
                warn(f"plugin bundle: unexpected skill folder '{sub.name}' "
                     f"(not in the curated bundle or the maintained set)")

    for name in sync.CURATED_BUNDLE:
        canonical_dir, _, actions = sync.plan_skill(name)
        if canonical_dir is None:
            err(f"plugin bundle: no canonical source found for curated "
                f"skill '{name}' under skills/")
            continue
        drift = [(status, relpath) for status, relpath in actions
                 if status != "unchanged"]
        if drift:
            detail = ", ".join(f"{relpath} ({status})"
                               for status, relpath in drift)
            err(f"plugin bundle: '{name}' is out of sync with canonical "
                f"skills/ [{detail}] — run: python scripts/sync_plugin_skills.py")


# --- Main ------------------------------------------------------------------

def main() -> int:
    canonical = canonical_skill_dirs()
    plugin = plugin_skill_dirs()

    print(f"AgentCounsel repository validation — {rel(REPO_ROOT) or '.'}")
    print(f"  canonical skills: {len(canonical)}")
    print(f"  plugin skills:    {len(plugin)}")
    print()

    for skill_dir in canonical:
        check_skill(skill_dir, require_sections=True)
    for skill_dir in plugin:
        check_skill(skill_dir, require_sections=False)

    check_content_scans()
    check_links()
    check_index_paths("SKILLS_INDEX.md")
    check_index_paths("WORKFLOW_ROUTER.md")
    check_adapters()
    check_plugin_manifest()
    check_plugin_bundle()
    check_index_coverage(canonical)

    if warnings:
        print(f"Warnings ({len(warnings)}):")
        for msg in warnings:
            print(f"  ! {msg}")
        print()

    if errors:
        print(f"Errors ({len(errors)}):")
        for msg in errors:
            print(f"  x {msg}")
        print()
        print("VALIDATION FAILED")
        return 1

    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
