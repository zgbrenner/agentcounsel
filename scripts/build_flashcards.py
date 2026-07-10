#!/usr/bin/env python3
"""Build an Anki-importable "routing" flashcard deck from skill metadata.

This script reads the generated ``metadata/index.json`` (built by
``scripts/build_skill_index.py`` from the canonical skills' frontmatter) and
writes ``dist/flashcards/agentcounsel-router-deck.txt`` — a tab-separated
file Anki can import directly, with one card per skill:

  * **Front** — a routing question built from the skill's ``summary``
    (its frontmatter ``description``, which by convention starts with
    "Use when ..."), phrased as "Which skill: <situation>?"
  * **Back** — the skill's name, its canonical path, and the matching
    slash-style command from ``COMMANDS.md`` if one exists there.

This is a *training* deck, not a routing engine: a lawyer studies it with
spaced repetition to internalize which situation maps to which skill, the
same way `WORKFLOW_ROUTER.md` and `COMMANDS.md` do for a live lookup. See
``docs/CLI.md`` for how this fits alongside the other scripts.

Standard library only — no third-party packages, no network calls. The
output lives under the git-ignored ``dist/`` directory, so there is no
``--check`` mode; just re-run this after skills change and re-import into
Anki if you keep a personal deck.

    python scripts/build_flashcards.py
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = REPO_ROOT / "metadata" / "index.json"
COMMANDS_PATH = REPO_ROOT / "COMMANDS.md"
OUTPUT_PATH = REPO_ROOT / "dist" / "flashcards" / "agentcounsel-router-deck.txt"

# Matches a COMMANDS.md table row: | `/area:name` | `skills/.../SKILL.md` | ...
COMMAND_ROW_RE = re.compile(r"^\|\s*`(/[a-z0-9\-]+:[a-z0-9\-]+)`\s*\|\s*`([^`]+)`\s*\|")

NO_COMMAND = "(no slash command — open the skill directly)"


def load_commands_by_path(text: str) -> dict[str, str]:
    """Parse COMMANDS.md's tables into {skill path: command}."""
    commands: dict[str, str] = {}
    for line in text.splitlines():
        match = COMMAND_ROW_RE.match(line)
        if not match:
            continue
        command, path = match.group(1), match.group(2)
        commands[path] = command
    return commands


def question_from_summary(summary: str) -> str:
    """Turn a skill's 'Use when ...' description into a routing question."""
    text = summary.strip()
    lowered = text[:1].lower() + text[1:] if text else text
    for prefix in ("use when ", "use this when "):
        if lowered.startswith(prefix):
            lowered = lowered[len(prefix):]
            break
    lowered = lowered.rstrip(". ").strip()
    if lowered:
        lowered = lowered[0].lower() + lowered[1:]
    return f"Which skill: {lowered}?"


def tsv_escape(value: str) -> str:
    """Anki's TSV import cannot tolerate literal tabs or newlines in a field."""
    return value.replace("\t", " ").replace("\n", " ").replace("\r", " ").strip()


def build_deck(index: dict, commands_by_path: dict[str, str]) -> list[str]:
    lines = [
        "#separator:tab",
        "#html:false",
        "#columns:Front\tBack",
    ]
    for skill in index.get("skills", []):
        title = skill.get("title") or skill.get("name") or skill.get("id", "")
        path = skill.get("path", "")
        summary = skill.get("summary") or skill.get("description") or ""
        front = tsv_escape(question_from_summary(summary))
        command = commands_by_path.get(path, NO_COMMAND)
        back = tsv_escape(f"{title} — {path} — {command}")
        lines.append(f"{front}\t{back}")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    if not INDEX_PATH.exists():
        print(
            f"error: {INDEX_PATH.relative_to(REPO_ROOT)} not found — "
            "run scripts/build_skill_index.py first.",
            file=sys.stderr,
        )
        return 1

    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    commands_text = COMMANDS_PATH.read_text(encoding="utf-8") if COMMANDS_PATH.exists() else ""
    commands_by_path = load_commands_by_path(commands_text)

    lines = build_deck(index, commands_by_path)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    card_count = len(lines) - 3  # minus the three header comment lines
    print(
        f"Wrote {card_count} cards to {OUTPUT_PATH.relative_to(REPO_ROOT)} "
        f"({len(commands_by_path)} skills matched to a COMMANDS.md shorthand)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
