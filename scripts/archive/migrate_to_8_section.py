#!/usr/bin/env python3
"""Migrate newer-cohort SKILL.md files from a 10-section to the canonical
8-section structure.

Two extra H2 sections accreted in the newer practice-area clusters that the
documented standard does not include:

  ## Capability Disclosure                    (between Purpose and Use When)
  ## Example Request and Expected Output Shape (between Output Format and
                                                Attorney Verification Checklist)

This script:

  * locates the "**This skill does not:**" paragraph inside Capability
    Disclosure and appends it to the Do Not Use When section as a final
    paragraph, so the negative-scope content is preserved;
  * drops the Capability Disclosure "**This skill does:**" paragraph
    (substantively redundant with Purpose);
  * removes the Example Request and Expected Output Shape section
    entirely (purely illustrative; adds no requirements).

It is idempotent: rerunning on a migrated file is a no-op.

Usage:

    python scripts/migrate_to_8_section.py             # migrate every affected skill
    python scripts/migrate_to_8_section.py --dry-run   # report only
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def migrate(text: str) -> tuple[str, bool, bool]:
    """Return (new_text, capability_changed, example_changed)."""

    capability_changed = False
    example_changed = False

    cap_re = re.compile(
        r"\n## Capability Disclosure\n(?P<body>.*?)(?=\n## )",
        re.DOTALL,
    )
    cap_match = cap_re.search(text)
    if cap_match:
        body = cap_match.group("body")
        does_not = ""
        m = re.search(
            r"\*\*This skill does not:\*\*\s*(?P<content>.+?)\n\s*\n",
            body + "\n\n",
            re.DOTALL,
        )
        if m:
            does_not = re.sub(r"\s+", " ", m.group("content")).strip()

        text = text[: cap_match.start()] + text[cap_match.end() :]
        capability_changed = True

        if does_not:
            dnw_re = re.compile(
                r"\n## Do Not Use When\n(?P<body>.*?)(?=\n## )",
                re.DOTALL,
            )
            dnw_match = dnw_re.search(text)
            if dnw_match:
                stripped = dnw_match.group("body").rstrip()
                addition = (
                    "\n\nAlso out of scope (this skill does not): "
                    + does_not
                )
                new_dnw = "\n## Do Not Use When\n" + stripped + addition + "\n"
                text = (
                    text[: dnw_match.start()]
                    + new_dnw
                    + text[dnw_match.end() :]
                )

    ex_re = re.compile(
        r"\n## Example Request and Expected Output Shape\n.*?(?=\n## )",
        re.DOTALL,
    )
    ex_match = ex_re.search(text)
    if ex_match:
        text = text[: ex_match.start()] + text[ex_match.end() :]
        example_changed = True

    return text, capability_changed, example_changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    skills_dir = REPO_ROOT / "skills"
    changed = 0
    scanned = 0
    for path in sorted(skills_dir.rglob("SKILL.md")):
        scanned += 1
        original = path.read_text(encoding="utf-8")
        new_text, cap, ex = migrate(original)
        if cap or ex:
            changed += 1
            label = []
            if cap:
                label.append("Capability Disclosure folded into Do Not Use When")
            if ex:
                label.append("Example Request removed")
            print(f"  {path.relative_to(REPO_ROOT)}: {'; '.join(label)}")
            if not args.dry_run and new_text != original:
                path.write_text(new_text, encoding="utf-8")

    verb = "would migrate" if args.dry_run else "migrated"
    print(f"\nScanned {scanned} skills; {verb} {changed}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
