---
name: Legal Prose Polish
description: "Use when revising draft legal work product to remove AI-sounding filler, vague risk language, unsupported certainty, and style defects while preserving citations, defined terms, quotations, privilege labels, client instructions, and attorney-review warnings."
practice_area: legal-methodology
task_type: verification
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The draft legal output to polish"
  - "The intended audience and use"
  - "Optional: the source documents, citations, defined terms, and client style preferences"
outputs:
  - "Legal prose polish report"
  - "Safer revised draft or marked revision plan"
related_skills:
  - skills/legal-methodology/output-format-compliance-check/SKILL.md
  - skills/legal-methodology/attorney-review-gate/SKILL.md
  - skills/legal-methodology/assumption-audit/SKILL.md
tags:
  - legal-methodology
  - prose-polish
  - quality-control
  - legal-writing
  - anti-slop
---

# Legal Prose Polish

## Purpose

Polish draft legal work product so it reads like careful legal writing rather than generic AI output. The skill removes throat-clearing, filler transitions, fake balance, vague risk language, overlong caveats, unsupported certainty, conclusory statements, and awkward passive voice where responsibility matters.

This is a writing-quality pass, not a legal accuracy check. It must preserve legal meaning, citations, quotations, defined terms, privilege legends, client-specific instructions, formal legal tone where needed, cautious phrasing where substantively appropriate, and attorney-review warnings.

## Use When

- A draft memo, email, demand letter, risk table, contract review, checklist, or client update sounds generic, padded, or AI-written.
- A draft overuses phrases such as "notably," "moreover," "it is important to note," "delve," "landscape," "underscore," "robust," or similar generic phrasing.
- The user asks to make a legal draft clearer, tighter, more lawyerly, or less AI-sounding.
- A draft contains conclusory or vague legal risk language that should be tied to facts, sources, or attorney-review caveats.
- A draft is external-facing and needs clearer agency, responsibility, and tone before attorney review.

## Required Inputs

- The complete draft to revise.
- The intended audience and use: internal attorney, client, court, opposing party, regulator, business stakeholder, or other recipient.
- Any required style constraints, client instructions, defined terms, privilege designation, and non-editable language.
- Optional: source documents or authority list, if the polish pass must avoid altering cited propositions.

If the draft is not provided, stop and request it. Do not polish from a summary alone.

## Do Not Use When

- The draft has not yet been substantively reviewed for source support, citations, assumptions, and attorney-review readiness.
- The user asks for legal advice, legal sign-off, or a conclusion that a position is correct.
- The task is to verify citations or factual claims; use `skills/legal-methodology/citation-integrity-check/SKILL.md` or `skills/legal-methodology/source-validation/SKILL.md`.
- The task is to change legal substance without attorney-provided direction.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Follow `core/source-and-citation-discipline.md`; do not invent authority, citations, quotations, facts, or deadlines.
- Do not change legal meaning, defined terms, quoted text, citations, pin cites, privilege legends, or client instructions unless you mark the change for attorney review.
- Do not remove cautious legal phrasing merely because it sounds less forceful. Caution is appropriate where facts, law, source support, or jurisdiction are unresolved.
- Do not convert uncertainty into certainty. Replace vague certainty with explicit source, assumption, or attorney-review framing.
- Preserve confidentiality and privilege. Do not add client-sensitive facts or expand sensitive detail.

## Workflow

1. **Confirm scope.** Identify the draft type, audience, intended use, non-editable text, privilege labels, defined terms, citations, quotations, and attorney-review warnings.
2. **Protect fixed text.** Mark citations, quotations, defined terms, privilege legends, client-required language, and attorney-review warnings as preserve zones.
3. **Scan for AI-sounding prose.** Flag throat-clearing, filler transitions, fake balance, repetitive hedging, generic intensifiers, and words such as "delve," "landscape," "underscore," and "robust" where they add no legal precision.
4. **Scan for legal overclaiming.** Flag conclusory legal statements, vague "legal risk" language, unsupported certainty, and caveats that obscure rather than clarify the issue.
5. **Scan for agency and responsibility.** Where passive voice hides who must act, who said what, who bears risk, or who must confirm an item, recommend active phrasing. Preserve passive voice where it is legally or tactically appropriate.
6. **Revise conservatively.** Tighten and clarify prose without changing substance. Where a sentence needs legal or factual support, add a placeholder instead of supplying unsupported substance.
7. **List preserved items.** Record citations, quotations, defined terms, privilege legends, and warnings that were intentionally preserved.
8. **Flag attorney decisions.** Identify any sentence whose revision requires legal judgment, tactical tone choice, client authorization, or privilege/confidentiality judgment.

## Output Format

Deliver:

1. **Draft Label** — "Draft legal work product for attorney review. Not legal advice."
2. **Polish Summary** — Brief description of the major style changes made and any limits.
3. **Preserved Items** — Citations, quotations, defined terms, privilege labels, client instructions, and attorney-review warnings preserved unchanged.
4. **Issue Table**

   | Location | Issue type | Problem | Revision approach | Attorney review needed? |
   |---|---|---|---|---|

5. **Revised Draft** — A clean revised version, or a marked revision plan if the draft cannot be safely revised without missing facts or attorney judgment.
6. **Open Attorney Decisions** — Tone, legal substance, source support, privilege, or client-instruction items that require attorney direction.

## Attorney Verification Checklist

- [ ] The revised draft preserves all citations, quotations, defined terms, privilege labels, client instructions, and attorney-review warnings.
- [ ] No legal conclusion was strengthened beyond the available source support.
- [ ] No cautious phrasing was removed where uncertainty remains.
- [ ] Every unsupported or conclusory legal statement has been revised, sourced, or flagged.
- [ ] Every external-facing tone change is appropriate for the recipient and matter posture.
- [ ] Confidential and privileged information has not been expanded or exposed unnecessarily.
- [ ] The final draft remains labeled as draft legal work product for attorney review, not legal advice.
