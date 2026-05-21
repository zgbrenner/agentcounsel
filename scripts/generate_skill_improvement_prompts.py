#!/usr/bin/env python3
"""Generate skill-improvement prompts for the AgentCounsel skill library.

This script scans every canonical skill under ``skills/`` and writes two
maintainer aids into ``reports/``:

  * ``reports/skill-improvement-prompts.md`` — one copyable prompt per
    skill, ready to hand to an AI coding agent to improve that specific
    skill without changing what the skill is for.
  * ``reports/skill-quality-checklist.md`` — a reusable checklist for
    reviewing any skill by hand.

The goal is to make it easy to iteratively improve the library: pick a
skill, copy its prompt, run it, review the diff, validate, repeat.

Standard library only — no third-party packages, no build tools. Run from
anywhere:

    python scripts/generate_skill_improvement_prompts.py
    python scripts/generate_skill_improvement_prompts.py --check

In ``--check`` mode the script writes nothing and exits non-zero if either
report is missing or out of date, so a maintainer (or CI) can confirm the
reports still match the current skill set. See the README section
"Improving skills".
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
REPORTS_DIR = REPO_ROOT / "reports"

PROMPTS_REPORT = REPORTS_DIR / "skill-improvement-prompts.md"
CHECKLIST_REPORT = REPORTS_DIR / "skill-quality-checklist.md"

# Directory names under skills/<area>/ that hold shared reference material,
# not a skill. They have no SKILL.md and are not catalogued as skills.
NON_SKILL_DIRS = {"references"}

# Required H2 sections for every canonical skill, in order. Mirrors
# scripts/validate_repo.py so the prompts ask for the same structure the
# validator enforces.
REQUIRED_SECTIONS = [
    "Purpose",
    "Use When",
    "Required Inputs",
    "Do Not Use When",
    "Legal Safety Rules",
    "Workflow",
    "Output Format",
    "Attorney Verification Checklist",
]

# Practice-area directory name -> display name. Anything not listed falls
# back to a derived title and is grouped after the known areas.
PRACTICE_AREAS = {
    "legal-research": "Legal Research",
    "litigation": "Litigation",
    "contracts": "Contracts",
    "corporate": "Corporate",
    "employment": "Employment",
    "privacy": "Privacy",
    "product-legal": "Product Legal",
    "regulatory": "Regulatory",
    "ai-governance": "AI Governance",
    "ip": "Intellectual Property",
    "setup": "Setup",
    "legal-methodology": "Legal Methodology",
}

# Order in which practice areas appear in the report.
AREA_ORDER = list(PRACTICE_AREAS.keys())

# Four-backtick fence so any triple backticks inside a prompt stay literal.
FENCE = "````"


# --- Parsing ---------------------------------------------------------------

def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path)


def parse_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_text, body). Empty frontmatter if absent."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return "", text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return "", text


def frontmatter_value(fm_text: str, field: str) -> str:
    """Read a single-line scalar field from YAML frontmatter."""
    match = re.search(rf"^{re.escape(field)}:\s*(.+?)\s*$", fm_text, re.M)
    if not match:
        return ""
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def extract_section(body: str, heading: str) -> str:
    """Return the text of an H2 section (without its heading), or ''."""
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$", body, re.M)
    if not match:
        return ""
    start = match.end()
    nxt = re.search(r"^##\s", body[start:], re.M)
    end = start + nxt.start() if nxt else len(body)
    return body[start:end].strip()


def first_sentence(text: str) -> str:
    """Collapse whitespace and return the first sentence of ``text``."""
    collapsed = " ".join(text.split())
    if not collapsed:
        return ""
    match = re.match(r"(.+?[.!?])(\s|$)", collapsed)
    sentence = match.group(1) if match else collapsed
    if len(sentence) > 400:
        sentence = sentence[:397].rstrip() + "..."
    return sentence


def area_display_name(area_dir_name: str) -> str:
    if area_dir_name in PRACTICE_AREAS:
        return PRACTICE_AREAS[area_dir_name]
    return area_dir_name.replace("-", " ").replace("_", " ").title()


def derive_name(skill_dir: Path) -> str:
    return skill_dir.name.replace("-", " ").replace("_", " ").title()


# --- Skill discovery -------------------------------------------------------

class SkillRecord:
    """Everything the report needs about one canonical skill."""

    def __init__(self, skill_dir: Path) -> None:
        self.skill_dir = skill_dir
        self.path = rel(skill_dir / "SKILL.md")
        self.area_key = skill_dir.parent.name
        self.area = area_display_name(self.area_key)

        text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        fm_text, body = parse_frontmatter(text)

        self.name = frontmatter_value(fm_text, "name") or derive_name(skill_dir)
        self.description = (
            frontmatter_value(fm_text, "description")
            or "(no description in frontmatter)"
        )
        self.purpose = (
            first_sentence(extract_section(body, "Purpose"))
            or "(no Purpose section found — the prompt asks for one to be added)"
        )
        self.missing_sections = [
            s for s in REQUIRED_SECTIONS
            if not re.search(rf"^##\s+{re.escape(s)}\s*$", body, re.M)
        ]


def canonical_skill_dirs() -> list[Path]:
    """All skill folders under skills/<area>/<skill>/ that have a SKILL.md."""
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


def collect_records() -> list[SkillRecord]:
    records = [SkillRecord(d) for d in canonical_skill_dirs()]

    def sort_key(record: SkillRecord) -> tuple[int, str]:
        try:
            area_rank = AREA_ORDER.index(record.area_key)
        except ValueError:
            area_rank = len(AREA_ORDER)
        return (area_rank, record.name.lower())

    return sorted(records, key=sort_key)


# --- Prompt rendering ------------------------------------------------------

def build_prompt(record: SkillRecord) -> str:
    """The copyable improvement prompt for one skill."""
    return f"""\
You are improving a single skill in AgentCounsel, an open, Markdown-native
library of legal workflows for AI agents and the attorneys who supervise
them. Every skill is a SKILL.md file that produces draft legal work product
for attorney review — never a final legal opinion.

TARGET SKILL
- Skill path: {record.path}
- Current skill name: {record.name}
- Practice area: {record.area}
- Current description: {record.description}
- Core purpose (must not change): {record.purpose}

CONTEXT TO READ FIRST
- Read {record.path} in full.
- Read the shared operating rules in core/ — they apply to every skill.
- Read any references/ folder in the same practice area, and any files in
  this skill's templates/ folder, so your edits stay consistent with them.

TASK
Revise the target skill file in place so it is clearer, tighter, and more
reliable to execute. Improve only this one skill. Do not touch other files
except to keep cross-references accurate.

IMPROVEMENT GOALS
- Make it faster and less ambiguous for an agent to decide whether this
  skill applies to a given request.
- Make the skill produce a more consistent, better-organized, attorney-ready
  result every time it runs.
- Make the safety posture unmistakable: the output is draft work product for
  attorney review, built only on sources the user actually supplied.

SPECIFIC REQUIREMENTS
1. Strengthen trigger clarity. Sharpen "Use When" and "Do Not Use When" so
   the skill's scope is unambiguous and each trigger is concrete and
   testable. Resolve any overlap with neighboring skills by naming them and
   their paths.
2. Strengthen required inputs. Make "Required Inputs" complete and specific:
   every input the workflow depends on must be listed, and optional-but-
   recommended inputs marked as such. State explicitly that when a required
   input is missing the skill stops and requests it, and never reconstructs
   or assumes the missing material.
3. Improve the workflow steps. Make every step in "Workflow" concrete,
   ordered, and checkable. Remove vague or redundant steps and merge
   duplicates. Ensure every deliverable promised by "Output Format" is
   produced by a step, and that no step produces something the output never
   reports.
4. Improve the output format. Make "Output Format" match the workflow
   exactly — every deliverable section named, ordered, and described. Require
   visible placeholders for missing information instead of invented content,
   and define any rating or triage label where it is used.
5. Strengthen attorney-review and source-discipline language. Reinforce
   "Legal Safety Rules" and the "Attorney Verification Checklist": attorney
   review is always required; never invent legal authority, citations,
   quotations, facts, market data, or deadlines; keep fact, assumption, law,
   analysis, and verification items separate; flag every point of
   uncertainty rather than resolving it silently.

REQUIRED CONSTRAINTS
- Do NOT change the core purpose of this skill. It must still do exactly the
  job stated under "Core purpose" above. Reorganizing, tightening, and
  clarifying are welcome; repurposing the skill is not.
- Preserve the AgentCounsel skill structure. Keep the YAML frontmatter with
  a non-empty `name` and `description`, and keep these H2 sections in this
  exact order: Purpose, Use When, Required Inputs, Do Not Use When, Legal
  Safety Rules, Workflow, Output Format, Attorney Verification Checklist.
- Keep `description` a single line that still begins by describing when to
  use the skill.
- Keep the skill Markdown-only: no build steps, no runtime, no new
  dependencies.
- Do not add jurisdiction-specific legal rules or legal conclusions. The
  skill supplies process and structure, not the law itself.
- Keep relative paths to shared references/ material and to templates/
  accurate; do not break links.

WHEN YOU ARE DONE
- Run `python scripts/validate_repo.py` and confirm it passes.
- Summarize what you changed, section by section, and why each change makes
  the skill clearer or safer."""


def area_anchor(area_name: str) -> str:
    return area_name.lower().replace(" ", "-")


def render_prompts_report(records: list[SkillRecord]) -> str:
    """The full skill-improvement-prompts.md report."""
    by_area: dict[str, list[SkillRecord]] = {}
    for record in records:
        by_area.setdefault(record.area, []).append(record)
    ordered_areas = list(by_area.keys())  # records already sorted by area

    lines: list[str] = []
    lines.append("# AgentCounsel — Skill Improvement Prompts")
    lines.append("")
    lines.append(
        "Generated by `scripts/generate_skill_improvement_prompts.py`. Do "
        "not edit this file by hand — re-run the script after adding or "
        "changing a skill.")
    lines.append("")
    lines.append(
        f"This report contains one copyable improvement prompt for each of "
        f"the {len(records)} skills in the canonical library (`skills/`). "
        "Each prompt asks an AI coding agent to improve one specific skill "
        "while preserving its purpose and the AgentCounsel skill structure.")
    lines.append("")
    lines.append(
        "Adapter copies under `adapters/` are generated from the canonical "
        "skills and are not listed here. Improve the canonical skill, then "
        "run `python scripts/sync_plugin_skills.py` to refresh the bundle.")
    lines.append("")
    lines.append("## How to use these prompts")
    lines.append("")
    lines.append(
        "1. Find the skill you want to improve in the section for its "
        "practice area.")
    lines.append("2. Copy the entire fenced prompt block for that skill.")
    lines.append(
        "3. Paste it into an AI coding agent that has access to this "
        "repository.")
    lines.append(
        "4. Review the resulting diff with attorney-style scrutiny — keep "
        "only the changes that genuinely tighten the skill.")
    lines.append(
        "5. Run `python scripts/validate_repo.py` before committing, and "
        "regenerate this report so it stays in sync.")
    lines.append("")
    lines.append(
        "For a manual review pass, work through "
        "`reports/skill-quality-checklist.md` alongside these prompts.")
    lines.append("")
    lines.append("## Skills by practice area")
    lines.append("")
    for area in ordered_areas:
        count = len(by_area[area])
        noun = "skill" if count == 1 else "skills"
        lines.append(
            f"- [{area}](#{area_anchor(area)}) — {count} {noun}")
    lines.append("")
    lines.append("---")

    for area in ordered_areas:
        lines.append("")
        lines.append(f"## {area}")
        for record in by_area[area]:
            lines.append("")
            lines.append(f"### {record.name}")
            lines.append("")
            lines.append(f"- **Skill file:** `{record.path}`")
            lines.append(f"- **Practice area:** {record.area}")
            lines.append(f"- **Current description:** {record.description}")
            if record.missing_sections:
                missing = ", ".join(record.missing_sections)
                lines.append(
                    f"- **Structure check:** missing required section(s): "
                    f"{missing}. The prompt below asks for the full section "
                    "set to be restored.")
            else:
                lines.append(
                    "- **Structure check:** all "
                    f"{len(REQUIRED_SECTIONS)} required sections present.")
            lines.append("")
            lines.append(f"{FENCE}text")
            lines.append(build_prompt(record))
            lines.append(FENCE)

    return "\n".join(lines) + "\n"


def render_checklist() -> str:
    """The reusable skill-quality-checklist.md report."""
    return """\
# AgentCounsel — Skill Quality Checklist

A reusable checklist for reviewing any AgentCounsel skill (`SKILL.md`), by
hand or with an AI agent. Use it alongside
`reports/skill-improvement-prompts.md` when iterating on the library, and as
a release gate before publishing.

Generated by `scripts/generate_skill_improvement_prompts.py`. The checklist
is reusable and skill-agnostic — re-running the script keeps it current with
the required skill structure.

## Structure and frontmatter

- [ ] The file starts with YAML frontmatter holding a non-empty `name` and `description`.
- [ ] `description` is a single line that begins by describing when to use the skill.
- [ ] The body has an H1 title.
- [ ] These H2 sections are present, in order: Purpose, Use When, Required Inputs, Do Not Use When, Legal Safety Rules, Workflow, Output Format, Attorney Verification Checklist.

## Trigger clarity

- [ ] "Use When" lists concrete, testable situations where the skill applies.
- [ ] "Do Not Use When" lists the cases the skill must decline.
- [ ] Overlap with neighboring skills is resolved — related skills are named with their paths.
- [ ] An agent can decide from these two sections alone whether the skill fits the request.

## Required inputs

- [ ] Every input the workflow depends on is listed in "Required Inputs".
- [ ] Optional-but-recommended inputs are marked as optional.
- [ ] The skill states that it stops and requests any missing required input.
- [ ] The skill never reconstructs or assumes missing source material.

## Workflow

- [ ] Every step is concrete, ordered, and checkable.
- [ ] No step is vague, redundant, or unreachable.
- [ ] Every "Output Format" section is produced by a workflow step.
- [ ] The workflow produces nothing that no output section reports.
- [ ] References to shared `references/` material and to `templates/` are accurate and resolve.

## Output format

- [ ] Every deliverable section is named, ordered, and described.
- [ ] The output structure matches the workflow exactly.
- [ ] Missing information is shown with visible placeholders, not invented content.
- [ ] Any rating or triage label is defined where it is used.

## Attorney review and source discipline

- [ ] The skill states that its output is draft work product for attorney review.
- [ ] The skill never instructs the agent to invent authority, citations, quotations, facts, market data, or deadlines.
- [ ] Fact, assumption, law, analysis, and verification items are kept separate.
- [ ] Jurisdiction, governing law, posture, and the relevant date are identified or flagged as unknown.
- [ ] Confidentiality and privilege are preserved.
- [ ] The "Attorney Verification Checklist" covers every judgment call the skill makes.
- [ ] Points of uncertainty are flagged, not resolved silently.

## Core purpose

- [ ] The skill still does exactly one job, matching its "Purpose" section.
- [ ] Recent edits tightened the skill without repurposing it.

## Validation

- [ ] `python scripts/validate_repo.py` passes.
- [ ] If the skill is in the Claude Code plugin bundle, `python scripts/sync_plugin_skills.py --check` passes.
- [ ] `reports/skill-improvement-prompts.md` has been regenerated so it reflects the current skill.
"""


# --- Modes -----------------------------------------------------------------

def run_write(records: list[SkillRecord]) -> int:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    prompts_md = render_prompts_report(records)
    checklist_md = render_checklist()
    PROMPTS_REPORT.write_text(prompts_md, encoding="utf-8")
    CHECKLIST_REPORT.write_text(checklist_md, encoding="utf-8")

    print("AgentCounsel skill-improvement prompt generator")
    print(f"  canonical skills scanned: {len(records)}")
    print(f"  wrote {rel(PROMPTS_REPORT)} ({len(records)} prompts)")
    print(f"  wrote {rel(CHECKLIST_REPORT)}")
    print("Done.")
    return 0


def run_check(records: list[SkillRecord]) -> int:
    print("Checking generated skill-improvement reports against skills/")
    print()
    expected = {
        PROMPTS_REPORT: render_prompts_report(records),
        CHECKLIST_REPORT: render_checklist(),
    }
    stale = 0
    for path, content in expected.items():
        if not path.is_file():
            stale += 1
            print(f"  MISSING  {rel(path)}")
        elif path.read_text(encoding="utf-8") != content:
            stale += 1
            print(f"  STALE    {rel(path)}")
        else:
            print(f"  ok       {rel(path)}")
    print()
    if stale:
        print(f"OUT OF DATE: {stale} report(s) need regenerating. Run "
              "'python scripts/generate_skill_improvement_prompts.py'.")
        return 1
    print("Reports are up to date.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate skill-improvement prompts for every "
                    "AgentCounsel skill.")
    parser.add_argument(
        "--check", action="store_true",
        help="Report whether the generated reports are out of date and exit "
             "non-zero if so; do not write any files.")
    args = parser.parse_args(argv)

    if not SKILLS_ROOT.is_dir():
        print(f"error: skills directory not found at {rel(SKILLS_ROOT)}",
              file=sys.stderr)
        return 1

    records = collect_records()
    if not records:
        print("error: no canonical skills found under skills/",
              file=sys.stderr)
        return 1

    return run_check(records) if args.check else run_write(records)


if __name__ == "__main__":
    sys.exit(main())
