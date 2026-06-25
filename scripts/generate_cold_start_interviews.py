#!/usr/bin/env python3
"""Generate cold-start interview SKILL.md files for practice areas that
need one.

The four originally-authored cold-start interviews (contracts, corporate,
litigation, privacy) live under skills/setup/ as hand-written files and
are NEVER touched by this generator. Every other practice area listed in
practice-profiles/ gets a generated cold-start interview produced from
the per-area data block below.

Each generated SKILL.md follows the eight-section structure of the
hand-authored interviews, with area-specific questions in each of the
nine workflow stages and area-specific Attorney Verification Checklist
additions.

Usage:

    python scripts/generate_cold_start_interviews.py             # generate/refresh
    python scripts/generate_cold_start_interviews.py --check     # verify no drift
    python scripts/generate_cold_start_interviews.py --list      # list areas it owns

The --check mode is intended for CI: it prints a diff and exits non-zero
if any generated file on disk differs from what the generator would
emit. This guarantees the data block, the generator, and the committed
skills stay in lockstep.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from textwrap import dedent

REPO_ROOT = Path(__file__).resolve().parent.parent
SETUP_DIR = REPO_ROOT / "skills" / "setup"

# Hand-authored interviews this generator NEVER touches.
HAND_AUTHORED = {"contracts", "corporate", "litigation", "privacy"}


# Per-area prose: the indefinite article ("a" vs. "an") and the lower-case
# noun phrase used mid-sentence. The data is split out from AREAS because
# AREAS keys are slugs ("m-and-a"), display names are title-cased ("M&A"),
# and neither reliably yields correct prose — "M&A" needs "an" because it
# is read "em-and-ay", and a naive `.lower()` would turn "M&A" into "m&a".
AREA_PROSE: dict[str, tuple[str, str]] = {
    "employment":               ("an", "employment"),
    "ip":                       ("an", "intellectual property"),
    "ai-governance":            ("an", "AI-governance"),
    "m-and-a":                  ("an", "M&A"),
    "tax":                      ("a",  "tax"),
    "trusts-estates":           ("a",  "trusts-and-estates"),
    "real-estate":              ("a",  "real-estate"),
    "securities-capital-markets": ("a", "securities and capital markets"),
    "regulatory":               ("a",  "regulatory"),
    "antitrust-competition":    ("an", "antitrust / competition"),
    "bankruptcy-restructuring": ("a",  "bankruptcy and restructuring"),
    "insurance":                ("an", "insurance"),
    "family-law":               ("a",  "family-law"),
    "product-legal":            ("a",  "product-legal"),
    "financial-crime":          ("a",  "financial-crime"),
}


# Per-area content blocks.
#
# For each practice area:
#   display_name        — title-case area name shown in the SKILL.md
#   description_topics  — the 8-topic clause embedded in the YAML description
#   related_skills      — 2-3 representative skills from that practice area
#   stage_questions     — 8 lists of questions (one per workflow stage)
#   checklist_extras    — area-specific items appended to the baseline
#                         Attorney Verification Checklist
AREAS: dict[str, dict] = json.loads(
    (Path(__file__).resolve().parent / "cold_start_areas.json")
    .read_text(encoding="utf-8")
)


SKILL_MD_TEMPLATE = """---
name: {display_name} Cold-Start Interview
description: "Use when {article} {area_phrase} practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering {description_topics}."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to {article} {area_phrase} attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled {area_phrase} practice profile draft for attorney review"
related_skills:
{related_skills_yaml}
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - {area_tag}
---

# {display_name} Cold-Start Interview

## Purpose

Conduct a structured, staged interview with {article} {area_phrase} practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/{area_slug}.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/{area_slug}.md` for the first time.
- {article_cap} {area_phrase} practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the {area_phrase} area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the {area_phrase} practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live {area_phrase} matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/{area_slug}.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific {area_phrase} matter (use the appropriate matter-level skill for that task).

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Never guess or infer an answer to any interview question. If the interviewee cannot answer a question, record `[CONFIRM: answer required from practice group]` and move on.
- The filled profile is a draft. It must be reviewed and explicitly approved by the supervising attorney or practice group before it governs any AgentCounsel work product.
- Do not invent standard positions, clause preferences, escalation thresholds, or review rules. Record only what the interviewee provides.
- Do not include client-specific facts, client names, matter identifiers, or privileged details in the profile. The profile is a reusable group-level configuration, not a matter record.
- Do not state or imply that any threshold, position, or rule in the profile satisfies a legal requirement under any jurisdiction. Jurisdiction-specific legal obligations are for the attorney to verify.
- Flag every item the interviewee defers or leaves open with a visible `[CONFIRM: ...]` placeholder so the reviewer can see exactly what is unresolved.

## Workflow

**Stage 1 — Jurisdictions**

Ask the interviewee:
{q_jurisdictions}

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
{q_client_context}

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
{q_escalation}

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
{q_output_style}

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
{q_source_documents}

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
{q_standard_positions}

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
{q_review_requirements}

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
{q_prohibited_assumptions}

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/{area_slug}.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/{area_slug}.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
{checklist_extras}
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/{area_slug}.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
"""


def render_questions(questions: list[str]) -> str:
    """Render a question list as Markdown bullets."""
    return "\n".join(f"- {q}" for q in questions)


def render_related_skills(skills: list[str]) -> str:
    """Render a related_skills list as YAML."""
    return "\n".join(f"  - {s}" for s in skills)


def render_checklist_extras(extras: list[str]) -> str:
    """Render checklist extras as unchecked Markdown checklist items."""
    return "\n".join(f"- [ ] {item}" for item in extras)


def render_skill_md(area_slug: str, area: dict) -> str:
    """Render a complete SKILL.md for one practice area."""
    article, area_phrase = AREA_PROSE[area_slug]
    return SKILL_MD_TEMPLATE.format(
        display_name=area["display_name"],
        area_slug=area_slug,
        article=article,
        article_cap=article.capitalize(),
        area_phrase=area_phrase,
        area_tag=area_slug,
        description_topics=area["description_topics"],
        related_skills_yaml=render_related_skills(area["related_skills"]),
        q_jurisdictions=render_questions(area["stage_questions"]["jurisdictions"]),
        q_client_context=render_questions(area["stage_questions"]["client_context"]),
        q_escalation=render_questions(area["stage_questions"]["escalation"]),
        q_output_style=render_questions(area["stage_questions"]["output_style"]),
        q_source_documents=render_questions(area["stage_questions"]["source_documents"]),
        q_standard_positions=render_questions(area["stage_questions"]["standard_positions"]),
        q_review_requirements=render_questions(area["stage_questions"]["review_requirements"]),
        q_prohibited_assumptions=render_questions(area["stage_questions"]["prohibited_assumptions"]),
        checklist_extras=render_checklist_extras(area["checklist_extras"]),
    )


def skill_path(area_slug: str) -> Path:
    return SETUP_DIR / f"{area_slug}-cold-start-interview" / "SKILL.md"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify no drift between data and disk")
    parser.add_argument("--list", action="store_true", help="List practice areas this generator owns")
    args = parser.parse_args()

    if args.list:
        print("Generator owns these cold-start interviews:")
        for slug in sorted(AREAS):
            print(f"  - skills/setup/{slug}-cold-start-interview/SKILL.md")
        print(f"\nHand-authored (NEVER touched by this generator): {sorted(HAND_AUTHORED)}")
        return 0

    drift = []
    written = []
    for slug, data in sorted(AREAS.items()):
        if slug in HAND_AUTHORED:
            print(f"  skip      {slug} (hand-authored)", file=sys.stderr)
            continue
        target = skill_path(slug)
        rendered = render_skill_md(slug, data)
        if args.check:
            if not target.exists():
                drift.append(f"missing: {target.relative_to(REPO_ROOT)}")
                continue
            current = target.read_text(encoding="utf-8")
            if current != rendered:
                drift.append(f"drift:   {target.relative_to(REPO_ROOT)}")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(rendered, encoding="utf-8")
            written.append(target.relative_to(REPO_ROOT))

    if args.check:
        if drift:
            print("Generated content is out of sync with disk:")
            for d in drift:
                print(f"  {d}")
            print(
                "\nRun `python scripts/generate_cold_start_interviews.py` to refresh.",
                file=sys.stderr,
            )
            return 1
        print("Cold-start interview bundle is in sync.")
        print(f"  generated interviews: {len(AREAS)}")
        return 0

    print(f"Wrote {len(written)} cold-start interview SKILL.md files:")
    for p in written:
        print(f"  {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
