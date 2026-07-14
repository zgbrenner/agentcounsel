# Skill Template

A fill-in-the-blanks scaffold for a new AgentCounsel skill. Copy the
frontmatter and section scaffold below (everything from the next `---` on)
into `skills/<practice-area>/<skill-slug>/SKILL.md`, replace every
`<angle-bracket>` placeholder, delete every instructional line, and delete
this note. Read `docs/SKILL_METADATA_STANDARD.md` for the full field
reference and `CONTRIBUTING.md` for the hard requirements a new skill must
meet before it is merged. Match the depth and tone of
`skills/contracts/nda-review/SKILL.md`.

Every valid `SKILL.md` compiles automatically to a typed Skill Specification
v2 contract. Add an optional sibling `SPEC.json` only when explicit types,
execution modes, gates, evidence fields, or selective module-loading rules
materially improve the workflow. Start from
`docs/templates/SPEC_TEMPLATE.json` and follow `docs/SKILL_SPEC_V2.md`. Do
not create a sidecar merely to duplicate the frontmatter below.

---
name: <Skill Name in Title Case>
description: "<Must begin with 'Use when' and name the concrete requests, documents, or situations that should route to this skill — trigger-rich, not a bare definition.>"
practice_area: <practice-area-slug>
task_type: <intake | interview | research | review | triage | drafting | analysis | summarization | extraction | verification>
jurisdictions: []
risk_level: <low | medium | high | critical>
requires_attorney_review: true
inputs:
  - "<short noun phrase for a required input>"
  - "Optional: <short noun phrase for an optional-but-recommended input>"
outputs:
  - "<short noun phrase naming a deliverable section or artifact>"
related_skills:
  - skills/<area>/<neighboring-skill-slug>/SKILL.md
tags:
  - <lowercase-hyphenated-tag>
---

<!--
name: title case, matches the H1 below.
description: quoted, single line, must start with "Use when"; see docs/SKILL_METADATA_STANDARD.md.
practice_area: must exactly match the directory name directly under skills/.
task_type: one of the ten controlled values listed above — pick the closest fit.
jurisdictions: leave [] unless this skill is genuinely bound to named jurisdictions; process/structure skills stay jurisdiction-agnostic.
risk_level: low/medium/high/critical — how much is at stake if a wrong draft is not caught at attorney review.
requires_attorney_review: keep true; this is legal work product.
inputs / outputs: concrete noun phrases, not sentences; at least one each.
related_skills: repository paths of the form skills/<area>/<skill>/SKILL.md; each must resolve to a real skill; never list this skill itself.
tags: four to seven lowercase, hyphenated keywords.
-->

# <Skill Name>

## Purpose

State in 2-3 sentences what draft legal work product this skill produces and
for whom. Close with the standard framing: the skill produces draft legal
work product for attorney review — not legal advice, not a final answer, and
not an opinion on the law.

## Use When

List the concrete requests, documents, or situations that should route an
agent to this skill — the trigger patterns a router, `WORKFLOW_ROUTER.md`, or
another skill's "Do Not Use When" section would point to. Be as specific as
the examples in an existing skill, such as
`skills/contracts/nda-review/SKILL.md`.

## Required Inputs

List every input the skill needs before substantive work starts, including
whatever the jurisdiction and deadline gate in
`core/jurisdiction-and-deadline-gates.md` requires for this task —
jurisdiction, governing law, procedural posture, client posture, and the
relevant "as of" date. State plainly that the skill stops and asks when a
required input is missing; it does not proceed on an assumed default.

## Do Not Use When

Name the adjacent skills, document types, or situations this skill should
not be used for, and point to the skill that should be used instead. Include
any situation calling for a different practice area, a final legal opinion,
or specialist counsel outside this skill's scope.

## Legal Safety Rules

State the rules this skill inherits from `core/`, plus anything specific to
this skill's risk profile. Always include the canonical source-and-citation-
discipline bullet:

- **Source and citation discipline.** Follow
  `core/source-and-citation-discipline.md`. Never invent legal authority,
  citations, quotations, statutes, cases, regulations, filing deadlines, or
  procedural rules. Label every statement as a provided source, a
  user-provided fact, an assumption, a legal inference, or an item requiring
  attorney verification, and use a placeholder such as
  `[Attorney to insert authority]` when no verified source is available.

Add rules specific to this skill — for example a severity floor, an
escalation trigger, or a scope boundary the workflow must enforce.

## Workflow

Write the ordered steps the skill follows, numbered, each naming what it
produces or checks at that step. Reference any shared reference material
under this skill's `templates/` folder or the practice area's `references/`
folder. Include an explicit stop-and-ask step wherever a Required Input is
missing, and a step that assigns any triage rating or escalation call this
skill makes.

## Output Format

Define the deliverable's structure, section by section, in the order it must
appear — following the standard skeleton in `core/output-format-rules.md`
(heading block, summary, body, assumptions, verification items, attorney
checklist) unless this skill has a good reason to deviate. Name every
placeholder convention the skill uses (for example `[CONFIRM: ...]`,
`[VERIFY: ...]`, `[deadline verification required]`).

## Attorney Verification Checklist

List the skill-specific items a supervising attorney must confirm, as an
unchecked list, and add a line noting that this checklist supplements —
never replaces — the baseline checklist in
`core/attorney-review-checklist.md`. The agent never checks a box here; only
the reviewing attorney does.
