#!/usr/bin/env python3
"""Sync the Claude Code plugin skill bundle from canonical /skills.

The canonical source of truth for AgentCounsel skills is the /skills
directory. The Claude Code plugin adapter ships a curated starter bundle
under adapters/claude-code-plugin/skills/. That bundle is GENERATED from
the canonical skills by this script — it is not maintained by hand.

Run it after editing any canonical skill in the curated set, and before
releasing the plugin bundle:

    python scripts/sync_plugin_skills.py           # copy/update bundle files
    python scripts/sync_plugin_skills.py --check   # report drift only (CI)

In --check mode the script modifies nothing and exits non-zero if any
bundled skill is out of sync with canonical /skills.

The script is idempotent and uses the Python standard library only.
See PLUGIN_SYNC.md.
"""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_ROOT = REPO_ROOT / "skills"
PLUGIN_ROOT = REPO_ROOT / "adapters" / "claude-code-plugin" / "skills"

# The curated starter bundle: skill folder names generated from /skills.
# To add or remove a bundled skill, edit this list.
CURATED_BUNDLE = [
    "legal-research-memo",
    "nda-review",
    "contract-risk-review",
    "demand-letter",
    "litigation-chronology",
    "termination-risk",
    "dpa-review",
    "ai-use-case-intake",
]

# Plugin skills that are hand-maintained, not generated from /skills.
# legal-core summarizes the /core operating rules; update it by hand when
# /core changes. The sync script preserves it and never overwrites it.
MAINTAINED_SKILLS = ["legal-core"]


def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path)


def find_canonical(name: str) -> Path | None:
    """Locate a canonical skill folder by name, at skills/<area>/<name>."""
    if not CANONICAL_ROOT.is_dir():
        return None
    matches = [m for m in sorted(CANONICAL_ROOT.glob(f"*/{name}"))
               if (m / "SKILL.md").is_file()]
    if len(matches) > 1:
        print(f"  warning: skill name '{name}' matches {len(matches)} folders "
              f"({', '.join(rel(m) for m in matches)}); using {rel(matches[0])}",
              file=sys.stderr)
    return matches[0] if matches else None


def bundle_files(canonical_dir: Path) -> dict[str, Path]:
    """Files that belong in a plugin copy: SKILL.md plus any templates."""
    files: dict[str, Path] = {}
    skill = canonical_dir / "SKILL.md"
    if skill.is_file():
        files["SKILL.md"] = skill
    templates = canonical_dir / "templates"
    if templates.is_dir():
        for item in sorted(templates.iterdir()):
            if item.is_file():
                files[f"templates/{item.name}"] = item
    return files


def target_files(target_dir: Path) -> list[str]:
    """Relative paths of bundle files currently present in a plugin copy."""
    present: list[str] = []
    if (target_dir / "SKILL.md").is_file():
        present.append("SKILL.md")
    templates = target_dir / "templates"
    if templates.is_dir():
        for item in sorted(templates.iterdir()):
            if item.is_file():
                present.append(f"templates/{item.name}")
    return present


def plan_skill(name: str):
    """Plan the sync for one curated skill.

    Returns (canonical_dir, target_dir, actions) where actions is a list of
    (status, relpath) with status in: create, update, unchanged, remove.
    canonical_dir is None if the canonical skill cannot be found.
    """
    canonical_dir = find_canonical(name)
    target_dir = PLUGIN_ROOT / name
    if canonical_dir is None:
        return None, target_dir, []

    wanted = bundle_files(canonical_dir)
    actions: list[tuple[str, str]] = []

    for relpath, src in wanted.items():
        dst = target_dir / relpath
        if not dst.exists():
            actions.append(("create", relpath))
        elif not filecmp.cmp(src, dst, shallow=False):
            actions.append(("update", relpath))
        else:
            actions.append(("unchanged", relpath))

    for relpath in target_files(target_dir):
        if relpath not in wanted:
            actions.append(("remove", relpath))

    return canonical_dir, target_dir, actions


def apply_skill(name: str) -> tuple[bool, list[tuple[str, str]]]:
    """Sync one curated skill. Returns (found, actions)."""
    canonical_dir, target_dir, actions = plan_skill(name)
    if canonical_dir is None:
        return False, []

    wanted = bundle_files(canonical_dir)
    for status, relpath in actions:
        dst = target_dir / relpath
        if status in ("create", "update"):
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(wanted[relpath], dst)
        elif status == "remove":
            dst.unlink()

    templates_dir = target_dir / "templates"
    if templates_dir.is_dir() and not any(templates_dir.iterdir()):
        templates_dir.rmdir()

    return True, actions


def run_sync() -> int:
    """Copy/update the plugin bundle from canonical /skills."""
    print("Syncing the Claude Code plugin bundle from canonical /skills")
    print()
    PLUGIN_ROOT.mkdir(parents=True, exist_ok=True)

    missing: list[str] = []
    changed_files = 0

    for name in CURATED_BUNDLE:
        found, actions = apply_skill(name)
        if not found:
            missing.append(name)
            print(f"  ERROR     {name}: no canonical skill found under skills/")
            continue
        changes = [a for a in actions if a[0] != "unchanged"]
        changed_files += len(changes)
        if changes:
            for status, relpath in changes:
                print(f"  {status:9s} {name}/{relpath}")
        else:
            print(f"  unchanged {name}")

    print()
    for name in MAINTAINED_SKILLS:
        skill_md = PLUGIN_ROOT / name / "SKILL.md"
        if skill_md.is_file():
            print(f"  preserved {name} (hand-maintained — not synced from /skills)")
        else:
            print(f"  WARNING   {name}/SKILL.md is missing "
                  f"(expected a hand-maintained skill at {rel(skill_md)})")

    print()
    if missing:
        print(f"FAILED: canonical skill(s) not found: {', '.join(missing)}")
        return 1
    print(f"Done. {len(CURATED_BUNDLE)} curated skills synced; "
          f"{changed_files} file change(s) written.")
    print("Run 'python scripts/validate_repo.py' to confirm.")
    return 0


def run_check() -> int:
    """Report plugin bundle drift without modifying files. Exit 1 on drift."""
    print("Checking the Claude Code plugin bundle against canonical /skills")
    print()
    problems = 0

    for name in CURATED_BUNDLE:
        canonical_dir, _, actions = plan_skill(name)
        if canonical_dir is None:
            problems += 1
            print(f"  ERROR     {name}: no canonical skill found under skills/")
            continue
        drift = [a for a in actions if a[0] != "unchanged"]
        if drift:
            problems += 1
            detail = ", ".join(f"{relpath} ({status})"
                               for status, relpath in drift)
            print(f"  DRIFT     {name}: {detail}")
        else:
            print(f"  ok        {name}")

    print()
    for name in MAINTAINED_SKILLS:
        skill_md = PLUGIN_ROOT / name / "SKILL.md"
        if skill_md.is_file():
            print(f"  ok        {name} (hand-maintained — presence checked)")
        else:
            problems += 1
            print(f"  ERROR     {name}/SKILL.md is missing ({rel(skill_md)})")

    print()
    if problems:
        print(f"OUT OF SYNC: {problems} issue(s). Run "
              f"'python scripts/sync_plugin_skills.py' to regenerate the bundle.")
        return 1
    print("Plugin bundle is in sync with canonical /skills.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Sync the Claude Code plugin skill bundle from "
                    "canonical /skills.")
    parser.add_argument(
        "--check", action="store_true",
        help="Report whether the bundle is out of sync and exit non-zero "
             "if so; do not modify any files.")
    args = parser.parse_args(argv)
    return run_check() if args.check else run_sync()


if __name__ == "__main__":
    sys.exit(main())
