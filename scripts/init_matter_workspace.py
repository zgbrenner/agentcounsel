#!/usr/bin/env python3
"""Initialize a new matter workspace from the canonical template.

Copies ``matter-workspaces/_template/`` into a new, safely named matter
directory and seeds ``matter_profile.md`` with the matter name, practice area,
jurisdiction, and optional matter pack, plus a short "next steps" block.

Standard library only — no third-party packages, no network calls, no paid
APIs. Run from anywhere:

    py scripts/init_matter_workspace.py "Contoso MSA Review" --practice-area contracts

The populated workspace it creates is DRAFT LEGAL WORK PRODUCT for attorney
review and may be privileged. Populated workspaces are written under ``matters/``
which is git-ignored by default.

Exit code 0 on success, 1 on error (e.g. destination exists without --force).
"""

from __future__ import annotations

import argparse
import datetime
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = REPO_ROOT / "matter-workspaces" / "_template"
DEFAULT_OUTPUT_ROOT = REPO_ROOT / "matters"
PROFILE_FILE = "matter_profile.md"
STATUS_FILE = "matter_status.md"


def slugify(name: str) -> str:
    """Produce a safe, lowercase, hyphenated filesystem name."""
    slug = name.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug or "matter"


def practice_area_dirs() -> list[str]:
    skills_dir = REPO_ROOT / "skills"
    if not skills_dir.is_dir():
        return []
    return sorted(
        p.name for p in skills_dir.iterdir()
        if p.is_dir() and not p.name.startswith(".") and p.name != "setup"
    )


def list_templates() -> int:
    print("Canonical matter workspace template:")
    if TEMPLATE_DIR.is_dir():
        print(f"  {TEMPLATE_DIR.relative_to(REPO_ROOT).as_posix()}/")
        for item in sorted(TEMPLATE_DIR.rglob("*")):
            if item.is_file():
                print(f"    {item.relative_to(TEMPLATE_DIR).as_posix()}")
    else:
        print("  (missing — expected matter-workspaces/_template/)")
        return 1
    print("\nSingle-file workspace templates:")
    ws_dir = REPO_ROOT / "matter-workspaces"
    for item in sorted(ws_dir.glob("*-matter.md")):
        print(f"  {item.relative_to(REPO_ROOT).as_posix()}")
    print("\nKnown practice areas (for --practice-area):")
    print("  " + ", ".join(practice_area_dirs()))
    return 0


def seed_profile(text: str, args: argparse.Namespace, today: str) -> str:
    """Replace the leading [CONFIRM] placeholders we can fill from CLI args."""
    pack_value = args.pack or "none"
    replacements = {
        "`[CONFIRM: descriptive matter name]`": f"{args.matter_name}",
        "`[CONFIRM: e.g., contracts, litigation, privacy, employment, corporate, regulatory]`":
            args.practice_area or "`[CONFIRM: practice area]`",
        "`[CONFIRM: governing law and relevant jurisdictions — verify jurisdiction]`":
            (f"{args.jurisdiction} [verify jurisdiction]" if args.jurisdiction
             else "`[CONFIRM: governing law and relevant jurisdictions — verify jurisdiction]`"),
        "`[CONFIRM: e.g., matter-packs/m-and-a.md — or \"none\"]`": pack_value,
        "`[CONFIRM: date]`": today,
    }
    for old, new in replacements.items():
        text = text.replace(old, new, 1)
    next_steps = (
        "\n## Next Steps (seeded by init_matter_workspace.py)\n\n"
        "1. Confirm parties, client role, and counterparty in the Matter Header.\n"
        "2. Confirm jurisdiction, governing law, and posture — never assume a default.\n"
        "3. Record source documents in `documents/` and `source_log.md`.\n"
        "4. Capture known and disputed facts in `facts.md`; open items in `tasks.md`.\n"
        "5. Run the recommended quality checks and record them in `quality_checks/`.\n"
        "6. Resolve every `[CONFIRM: ...]` / `[VERIFY: ...]` / `[ACTION: ...]` placeholder.\n"
        "7. Obtain supervising-attorney sign-off in `attorney_review.md` before any\n"
        "   output is relied upon, sent, filed, or signed.\n"
    )
    return text.rstrip() + "\n\n" + next_steps


def create_workspace(args: argparse.Namespace) -> int:
    if not TEMPLATE_DIR.is_dir():
        print(f"ERROR: template not found: {TEMPLATE_DIR}", file=sys.stderr)
        return 1

    slug = slugify(args.matter_name)
    output_root = Path(args.output_dir).resolve() if args.output_dir else DEFAULT_OUTPUT_ROOT
    dest = output_root / slug
    today = datetime.date.today().isoformat()

    if dest.exists() and not args.force:
        print(
            f"ERROR: workspace already exists: {dest}\n"
            f"       Use --force to overwrite, or choose a different matter name.",
            file=sys.stderr,
        )
        return 1

    if args.dry_run:
        print("DRY RUN - no files written.")
        print(f"  Would create: {dest}")
        print(f"  From template: {TEMPLATE_DIR.relative_to(REPO_ROOT).as_posix()}")
        print(f"  Matter name:   {args.matter_name}")
        print(f"  Practice area: {args.practice_area or '[CONFIRM]'}")
        print(f"  Jurisdiction:  {args.jurisdiction or '[CONFIRM]'}")
        print(f"  Matter pack:   {args.pack or 'none'}")
        print("  Files that would be created:")
        for item in sorted(TEMPLATE_DIR.rglob("*")):
            if item.is_file():
                print(f"    {dest.name}/{item.relative_to(TEMPLATE_DIR).as_posix()}")
        return 0

    if dest.exists() and args.force:
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(TEMPLATE_DIR, dest)

    profile_path = dest / PROFILE_FILE
    if profile_path.is_file():
        profile_path.write_text(
            seed_profile(profile_path.read_text(encoding="utf-8"), args, today),
            encoding="utf-8",
        )

    status_path = dest / STATUS_FILE
    if status_path.is_file():
        status_path.write_text(
            status_path.read_text(encoding="utf-8").replace(
                "| `[CONFIRM: date]` | Matter workspace created | `[CONFIRM]` |",
                f"| {today} | Matter workspace created by init_matter_workspace.py | `[CONFIRM]` |",
                1,
            ),
            encoding="utf-8",
        )

    rel_dest = dest.relative_to(REPO_ROOT) if dest.is_relative_to(REPO_ROOT) else dest
    print(f"Created matter workspace: {rel_dest}")
    print(f"  Start with: {rel_dest}/{PROFILE_FILE}")
    print("  This is DRAFT legal work product for attorney review - label and")
    print("  access-limit it. Obtain attorney sign-off before relying on any output.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Initialize a matter workspace from the canonical template.",
    )
    parser.add_argument("matter_name", nargs="?", help="Descriptive matter name.")
    parser.add_argument("--practice-area", help="Practice area (see --list-templates).")
    parser.add_argument("--jurisdiction", help="Governing law / jurisdiction (still attorney-verified).")
    parser.add_argument("--pack", help="Matter pack path, e.g. matter-packs/m-and-a.md.")
    parser.add_argument("--output-dir", help="Where to create the workspace (default: matters/).")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing workspace.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be created; write nothing.")
    parser.add_argument("--list-templates", action="store_true", help="List available templates and exit.")
    args = parser.parse_args(argv)

    if args.list_templates:
        return list_templates()
    if not args.matter_name:
        parser.error("matter_name is required (or use --list-templates).")
    return create_workspace(args)


if __name__ == "__main__":
    raise SystemExit(main())
