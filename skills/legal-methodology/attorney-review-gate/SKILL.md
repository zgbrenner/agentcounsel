---
name: Attorney Review Gate
description: "Use when running a final quality gate before legal draft work product is sent, filed, relied upon, or delivered for attorney review, producing must-confirm facts, law, citations, client decisions, ethics flags, privilege flags, jurisdiction/deadline flags, and a ready-or-not-ready status."
practice_area: legal-methodology
task_type: verification
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The final draft legal work product to gate"
  - "The source materials, citations, assumptions, and prior quality-check reports"
  - "The intended recipient, use, jurisdiction, and deadline context"
outputs:
  - "Attorney review gate checklist"
  - "Ready for attorney review or not ready for attorney review status"
related_skills:
  - skills/legal-methodology/citation-integrity-check/SKILL.md
  - skills/legal-methodology/assumption-audit/SKILL.md
  - skills/legal-methodology/privilege-confidentiality-check/SKILL.md
tags:
  - legal-methodology
  - attorney-review
  - review-gate
  - quality-control
  - final-check
---

# Attorney Review Gate

## Purpose

Run the final pre-reliance quality gate for draft legal work product. The skill consolidates must-confirm facts, must-confirm law, must-confirm citations, client decision points, ethical/professional-responsibility flags, privilege/confidentiality flags, jurisdiction/deadline flags, and a status of "ready for attorney review" or "not ready for attorney review."

This gate does not approve, certify, or finalize legal work. It organizes the issues a qualified attorney must review before reliance.

## Use When

- A high-risk legal output is about to be sent, filed, delivered, or relied upon.
- A draft demand letter, client memo, research summary, risk assessment, contract review, or filing-bound draft needs final attorney-review triage.
- Other quality checks have produced findings that need to be consolidated.
- The user asks whether a draft is ready for attorney review.

## Required Inputs

- The complete final draft to gate.
- Source materials, citations, assumptions, and prior quality-check reports if available.
- Intended recipient, use, jurisdiction, governing law, posture, and any deadline context.
- Any client decisions, business positions, or attorney instructions already supplied.

If the draft is missing, stop and request it.

## Do Not Use When

- The user wants the agent to approve, sign, send, file, or certify the draft.
- The draft has not been prepared yet.
- The user asks for legal advice or final legal judgment.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- A "ready for attorney review" status means ready to be reviewed by an attorney, not ready for reliance or external use.
- Do not check boxes as if acting for the attorney. List items for attorney confirmation.
- Follow `core/source-and-citation-discipline.md`; do not invent legal authority, citations, quotations, facts, or deadlines.
- Do not resolve legal conclusions, citations, deadlines, or privilege questions by guessing.
- Preserve confidentiality and privilege.

## Workflow

1. **Confirm gate scope.** Identify draft type, recipient, intended use, jurisdiction, deadlines, and prior quality checks.
2. **Collect must-confirm facts.** List material facts, source-dependent facts, and facts whose change would alter the output.
3. **Collect must-confirm law.** List legal rules, standards, thresholds, elements, exceptions, and current-law questions.
4. **Collect must-confirm citations.** List every authority, quotation, pin cite, and source that must be checked.
5. **Collect client decisions.** List settlement authority, risk tolerance, business positions, tone choices, waiver decisions, and sign-off items.
6. **Identify ethics and professional-responsibility flags.** Include legal-advice framing, unauthorized-practice risk, conflicts, candor, fairness, third-party disclosure, and competence/supervision issues.
7. **Identify privilege and confidentiality flags.** Include sensitive facts, privileged communications, work-product labels, anonymization needs, and external-facing redactions.
8. **Identify jurisdiction and deadline flags.** Include unknown jurisdiction, governing law, venue, agency, court, response dates, filing dates, notice periods, limitations periods, and effective dates.
9. **Assign status.** Use:
   - **Ready for attorney review** if the draft is complete enough for an attorney to review with listed confirmation items.
   - **Not ready for attorney review** if missing inputs, unsupported authorities, unresolved assumptions, or confidentiality issues prevent meaningful review.
10. **State reasons.** If not ready, explain exactly what must be provided or corrected.

## Output Format

Deliver:

1. **Draft Label** — "Draft legal work product for attorney review. Not legal advice."
2. **Gate Status** — Ready for attorney review / Not ready for attorney review.
3. **Reasons for Status** — Short bullet list.
4. **Must-Confirm Facts**
5. **Must-Confirm Law**
6. **Must-Confirm Citations and Sources**
7. **Client Decision Points**
8. **Ethics and Professional-Responsibility Flags**
9. **Privilege and Confidentiality Flags**
10. **Jurisdiction and Deadline Flags**
11. **Attorney Review Checklist**

## Attorney Verification Checklist

- [ ] All must-confirm facts have been checked against the record or client instructions.
- [ ] All must-confirm law has been researched and confirmed by counsel.
- [ ] All citations, quotations, and pin cites have been independently verified.
- [ ] All client decision points have been resolved or escalated.
- [ ] All ethics and professional-responsibility flags have been reviewed.
- [ ] Privilege and confidentiality treatment is appropriate for the recipient.
- [ ] Jurisdiction, governing law, venue, posture, and deadlines are confirmed.
- [ ] The draft remains marked as draft legal work product for attorney review, not legal advice.
