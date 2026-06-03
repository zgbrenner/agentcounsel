#!/usr/bin/env python3
"""AgentCounsel legal-prose quality pass.

A lightweight, standard-library-only linter for the *work-product samples* the
repository owns: the illustrative outputs under `examples/` and the eval
candidate outputs under `evals/outputs/`. It does **not** check legal accuracy
— like the rest of the tooling, it checks form and safety framing only. It is
deliberately conservative so it can run in CI without flagging legitimate
content (placeholders such as `[verify jurisdiction]`, required "attorney must
review" framing, and so on are never flagged).

What it looks for:

  Errors (fail the build):
    - Legal-advice / false-certainty framing — prose that asserts a legal
      conclusion or guarantee rather than draft work product for review
      (e.g. "this is enforceable", "there is no risk", "we guarantee").
      Traces to core/legal-work-product.md and core/output-format-rules.md.
    - Missing attorney-review posture — a work-product sample with no visible
      "draft / attorney review" framing anywhere in the file.

  Warnings (advisory; fail only under --strict):
    - Generic AI "slop" tells and filler phrases.
    - Vague intensifiers and weak verbs that dull legal prose.

This implementation is AgentCounsel-native. It was informed by the idea of an
anti-"slop" prose pass (see docs/OSS_BORROWING_MAP.md, hardikpandya/stop-slop,
MIT) but copies no phrase lists, prompts, or structure from any source; the
categories and patterns below are written for legal work product.

Usage:
    python scripts/check_legal_prose.py            # scan the default targets
    python scripts/check_legal_prose.py --strict   # warnings also fail
    python scripts/check_legal_prose.py --quiet     # summary only
    python scripts/check_legal_prose.py --path examples/dpa-review-example.md

Exit code 0 if no errors (and, under --strict, no warnings), 1 otherwise.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Directories whose work-product samples we scan by default.
DEFAULT_TARGET_DIRS = ("examples", "evals/outputs")

# Files that are not work product and must not be held to the posture check or
# scanned for prose tells: user-supplied sample requests and directory READMEs.
SKIP_FILENAMES = {"README.md", "sample-request.md"}


# --- Patterns -------------------------------------------------------------
#
# Each pattern is a (compiled regex, human-readable message) pair. Patterns are
# written to be high-confidence: they target phrasing that is wrong for draft
# legal work product, not merely informal. Word boundaries and small context
# windows keep them from matching legitimate, encouraged phrasing such as
# "attorney review is required" or "you should consult counsel".

def _c(pattern: str) -> re.Pattern:
    return re.compile(pattern, re.IGNORECASE)


# Errors: legal-advice / false-certainty framing. These assert a legal outcome
# or eliminate risk rather than flagging it for attorney verification.
ADVICE_CERTAINTY_PATTERNS: list[tuple[re.Pattern, str]] = [
    (_c(r"\bthis (?:agreement|clause|provision|contract|document|term) is (?:fully )?(?:legal|illegal|enforceable|unenforceable|valid|invalid|binding)\b"),
     "asserts a legal conclusion; flag enforceability/validity for attorney verification instead"),
    (_c(r"\bis (?:fully|clearly|certainly|definitely) enforceable\b"),
     "asserts enforceability as settled; this is an attorney-verification item"),
    (_c(r"\bthere is no (?:legal |material )?risk\b"),
     "eliminates risk rather than flagging it; state residual risk plainly"),
    (_c(r"\byou are (?:fully )?protected\b"),
     "asserts a guaranteed outcome; frame as risk allocation for attorney review"),
    (_c(r"\b(?:we|i|this memo) guarantee[sd]?\b"),
     "guarantees an outcome; legal work product does not guarantee results"),
    (_c(r"\bit is (?:completely |perfectly )?(?:legal|safe|fine) to\b"),
     "gives advice on what is legal/safe; reframe as draft analysis for attorney review"),
    (_c(r"\byou (?:must|are required to|are obligated to|have to) (?:sign|pay|comply|terminate|file|disclose)\b"),
     "directs the client to act; recommend a course for attorney review instead of directing"),
    (_c(r"\bas an ai(?:\s+(?:language\s+)?model)?\b"),
     "breaks the work-product frame with an AI self-reference"),
    (_c(r"\bthis (?:constitutes|is) legal advice\b"),
     "labels the output as legal advice; it is draft work product for attorney review"),
    (_c(r"\bwe conclude that the law (?:requires|prohibits|permits)\b"),
     "states a settled legal conclusion; mark as legal inference for attorney verification"),
]

# Warnings: generic AI "slop" / filler. Stylistic, not unsafe.
SLOP_PATTERNS: list[tuple[re.Pattern, str]] = [
    (_c(r"\bin today'?s (?:fast-paced|ever-changing|digital|modern) (?:world|landscape|environment)\b"),
     "generic AI opener"),
    (_c(r"\bit is (?:important|worth|crucial) to note that\b"),
     "filler phrase; state the point directly"),
    (_c(r"\bit should be noted that\b"),
     "filler phrase; state the point directly"),
    (_c(r"\bdelv(?:e|ing) into\b"),
     "AI cliche; prefer 'examine' or 'review'"),
    (_c(r"\bnavigat(?:e|ing) the (?:complex|complexities|landscape|nuances)\b"),
     "AI cliche; describe the actual task"),
    (_c(r"\b(?:rich|intricate|complex) tapestry\b"),
     "AI cliche"),
    (_c(r"\bplays? a (?:crucial|vital|key|pivotal) role\b"),
     "vague AI phrasing; name the specific function"),
    (_c(r"\bin the realm of\b"),
     "AI cliche; prefer 'in' or 'for'"),
    (_c(r"\bwhen it comes to\b"),
     "filler; prefer 'for' or 'regarding'"),
    (_c(r"\bat the end of the day\b"),
     "conversational filler"),
    (_c(r"\bneedless to say\b"),
     "filler; if needless, omit it"),
]

# Warnings: vague intensifiers / weak verbs that dull legal prose.
VAGUE_PATTERNS: list[tuple[re.Pattern, str]] = [
    (_c(r"\b(?:very|really|quite|rather|fairly) (?:important|significant|serious|risky|clear)\b"),
     "vague intensifier; prefer a specific characterization"),
    (_c(r"\ba number of\b"),
     "vague quantity; give the count or 'several'"),
    (_c(r"\bvarious (?:issues|risks|provisions|terms|factors)\b"),
     "vague; enumerate or characterize the items"),
    (_c(r"\bin order to\b"),
     "wordy; prefer 'to'"),
    (_c(r"\butili[sz]e[sd]?\b"),
     "prefer 'use'"),
]

# Phrases that, if present anywhere in a work-product file, satisfy the
# attorney-review posture check. Matched case-insensitively. The list covers
# the reviewing-professional framings the library uses — "attorney" for most
# practice areas, and "qualified ... professional" / "tax counsel" for areas
# (such as tax) whose work product is reviewed by a non-attorney professional.
POSTURE_MARKERS = (
    "draft work product",
    "draft legal work product",
    "attorney review",
    "attorney verification",
    "draft for attorney",
    "draft attorney work product",
    "review by a licensed attorney",
    "review by a qualified",
    "for review by",
    "requires attorney",
    "attorney must",
    "licensed attorney",
    "professional review",
    "professional must review",
    "must review it before",
    "tax counsel",
    "counsel must review",
)

# Files that intentionally contain weak or AI-sounding prose to demonstrate a
# quality-layer pass (e.g. a "before / after" prose-polish example). The
# safety ERROR checks still apply to them; only the STYLE (warning) checks are
# skipped, so their teaching content does not generate noise.
STYLE_EXEMPT = {
    "examples/quality-layer/contract-review-prose-polish.md",
}


# --- Scanning -------------------------------------------------------------

def iter_target_files(targets: list[Path]) -> list[Path]:
    files: list[Path] = []
    for base in targets:
        if base.is_file():
            if base.suffix == ".md" and base.name not in SKIP_FILENAMES:
                files.append(base)
            continue
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.md")):
            if path.name in SKIP_FILENAMES:
                continue
            files.append(path)
    return files


def line_of(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def display_path(path: Path) -> str:
    """Repo-relative path when the file is inside the repo, else the path as-is.

    Keeps output readable for the default targets while still supporting
    --path pointing at a file outside the repository.
    """
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def scan_patterns(text: str, patterns: list[tuple[re.Pattern, str]]):
    """Yield (line_number, matched_text, message) for each pattern hit."""
    for pat, message in patterns:
        for m in pat.finditer(text):
            yield line_of(text, m.start()), m.group(0).strip(), message


def has_posture_marker(text: str) -> bool:
    low = text.lower()
    return any(marker in low for marker in POSTURE_MARKERS)


# --- Main -----------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path",
        action="append",
        default=None,
        help="A file or directory to scan instead of the defaults. Repeatable.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as failures too (exit 1 if any warning).",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Print only the summary and any findings counts, not every line.",
    )
    args = parser.parse_args()

    if args.path:
        targets = [
            (Path(p) if Path(p).is_absolute() else REPO_ROOT / p) for p in args.path
        ]
    else:
        targets = [REPO_ROOT / d for d in DEFAULT_TARGET_DIRS]

    files = iter_target_files(targets)

    print("AgentCounsel legal-prose pass")
    print(f"  scanning {len(files)} work-product sample file(s)")
    print()

    errors: list[str] = []
    warnings: list[str] = []

    for path in files:
        rel = display_path(path)
        text = path.read_text(encoding="utf-8")

        # Error: legal-advice / false-certainty framing.
        for line, hit, msg in scan_patterns(text, ADVICE_CERTAINTY_PATTERNS):
            errors.append(f"{rel}:{line}: advice/certainty framing — \"{hit}\" — {msg}")

        # Error: missing attorney-review posture in a work-product sample.
        if not has_posture_marker(text):
            errors.append(
                f"{rel}: no attorney-review framing found — a work-product sample "
                f"must visibly read as a draft for attorney review"
            )

        # Warnings: slop and vague prose. Skipped for files that intentionally
        # demonstrate weak prose as teaching content.
        if rel not in STYLE_EXEMPT:
            for line, hit, msg in scan_patterns(text, SLOP_PATTERNS):
                warnings.append(f"{rel}:{line}: AI-slop phrasing — \"{hit}\" — {msg}")
            for line, hit, msg in scan_patterns(text, VAGUE_PATTERNS):
                warnings.append(f"{rel}:{line}: vague prose — \"{hit}\" — {msg}")

    if warnings and not args.quiet:
        print(f"Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  ! {w}")
        print()

    if errors:
        if not args.quiet:
            print(f"Errors ({len(errors)}):")
            for e in errors:
                print(f"  x {e}")
            print()
        print(f"PROSE CHECK FAILED — {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    if warnings and args.strict:
        print(
            f"PROSE CHECK FAILED (--strict) — 0 errors, {len(warnings)} warning(s)"
        )
        return 1

    print(f"Prose check passed — 0 errors, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
