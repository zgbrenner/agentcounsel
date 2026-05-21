---
name: Compliance Program Tracker
description: "Use when building an ongoing compliance-program tracker for a framework — mapping requirements to controls, owners, and evidence, building an audit calendar, and surfacing evidence gaps and remediation items for attorney review and audit readiness."
practice_area: regulatory
task_type: analysis
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The framework, regulation, or standard source text"
  - "The organization's control inventory, with owners and evidence locations"
  - "Audit context: known audit dates, audit period, assessor"
  - "Organization context and regulatory status"
  - "Optional: scope boundaries — entities, business lines, or systems in scope"
outputs:
  - "Control inventory and requirement map"
  - "Evidence status, audit calendar, and remediation items"
  - "Priority view for the next audit"
related_skills:
  - skills/regulatory/compliance-gap-matrix/SKILL.md
  - skills/regulatory/rule-change-summary/SKILL.md
  - skills/regulatory/enforcement-risk-memo/SKILL.md
tags:
  - regulatory
  - compliance
  - audit-readiness
  - controls
  - evidence-tracking
---

# Compliance Program Tracker

## Purpose

Produce a structured, attorney-ready draft compliance-program tracker for a regulatory framework or standard. The skill maps the framework's requirements to the organization's controls, owners, and evidence; builds an audit calendar of upcoming dates and obligations; surfaces evidence gaps and remediation items; and assembles a priority view for the next audit.

This skill provides workflow discipline and analytical structure. It produces draft legal work product for attorney review. This is not legal advice, a compliance certification, or an audit opinion. The tracker supports ongoing compliance management; it does not assert that the program is compliant.

## Use When

- A user says "track our compliance with this framework," "help us prepare for our SOC 2 audit," or "build a compliance dashboard and evidence plan."
- An organization needs an ongoing tracker — a control inventory, an audit calendar, and evidence management — rather than a one-time gap analysis.
- A team is preparing for an audit or examination and needs an evidence-collection plan and a priority view.

## Required Inputs

- **Framework or requirement source**: the actual standard, regulation, or framework text — uploaded or pasted. If not provided, stop and request it. Do not construct requirements from model background knowledge; every requirement in the tracker must trace to this source.
- **Control inventory**: a description of the organization's current controls relevant to the framework — the controls, their owners, where evidence is stored, and when evidence was last collected. The more specific the inventory, the more useful the tracker.
- **Audit context**: any known audit dates, the audit period or reporting window, and the assessor if known.
- **Organization context**: business type and any regulatory status that affects which requirements apply.
- **Scope boundaries** (optional but recommended): which entities, business lines, or systems are in scope. If not provided, flag as `[SCOPE: CONFIRM with attorney]`.

If the framework source is not provided, stop and request it.

## Do Not Use When

- The user needs a one-time, point-in-time mapping of requirements to controls and gaps — use `compliance-gap-matrix`.
- The user needs a summary of what a new rule requires — use `rule-change-summary` first, then return here.
- The user needs to assess enforcement exposure for a specific incident or practice — use `enforcement-risk-memo`.
- No framework or requirement source has been provided and cannot be obtained.
- The user is seeking a compliance certification or a formal audit opinion — this skill produces a draft tracker, not a certification.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice, a compliance certification, or an audit opinion.
- Every requirement in the tracker must trace to the provided framework source. Do not add requirements from model background knowledge without clearly marking them `[UNVERIFIED — not from provided source]`.
- A "control in place" or "evidence current" status reflects the information provided — not an assurance that the control operates effectively or would satisfy an assessor.
- Never fabricate controls, control owners, evidence locations, evidence-collection dates, or audit dates.
- Treat all dates — audit dates, evidence-collection windows, remediation deadlines — as user-supplied. Flag each `[CONFIRM: date]`. Do not invent or assume dates.
- Distinguish: (a) requirements as stated in the source, (b) the current-state control mapping, (c) the evidence status, (d) audit-calendar items, (e) remediation items, (f) attorney-verification items.
- Use `[CONFIRM: ...]` placeholders for any control fact, applicability question, or requirement interpretation that cannot be resolved from the provided materials.
- Preserve confidentiality; do not place sensitive operational details into reusable templates.
- Flag every requirement whose applicability is unclear and every control with stale or missing evidence.

## Workflow

1. **Confirm inputs.** Verify that the framework source and a control inventory are both provided. If the source is missing, stop and request it. Clarify scope boundaries and audit context.

2. **Parse the framework.** Extract discrete, individually trackable requirements from the source. Number each for reference. Quote the operative language where precision matters. Flag any requirement whose applicability to the organization is unclear as `[APPLICABILITY: CONFIRM]`.

3. **Build the control inventory map.** For each requirement, identify the control, the control owner, the evidence location, and the date evidence was last collected, from the inventory provided. If no control is described, note "No control described."

4. **Classify the tracking status.** For each requirement, apply one status: **Control in place** (a described control addresses the requirement, subject to verification); **Partial** (the described control addresses some elements only); **No control** (no described control addresses the requirement); **Unknown** (insufficient information to classify).

5. **Assess evidence.** For each control, record whether evidence is identified, where it is stored, and whether it is current or stale against the audit period. Flag stale and missing evidence.

6. **Build the audit calendar.** List the upcoming audit dates, the evidence-collection windows, and the remediation deadlines, with the responsible owner for each. Flag every date `[CONFIRM: date]`.

7. **List gaps and remediation items.** For each Partial, No-control, and stale-evidence item, write a remediation item: what type of action appears warranted, a proposed owner, and a placeholder target date. Do not prescribe specific legal steps — that is attorney judgment.

8. **Build the priority view.** Identify the items most urgent for the next audit — the requirements with no control or stale evidence whose evidence-collection window is closest.

9. **Identify attorney-verification items.** Flag any requirement interpretation, control-sufficiency question, or applicability question that requires attorney judgment.

10. **Assemble the tracker** and label it a draft.

## Output Format

Deliver the following sections in order:

**DRAFT COMPLIANCE PROGRAM TRACKER — FOR ATTORNEY REVIEW ONLY**

1. **Scope and Inputs Summary** — the framework source (title, version, date from the document), the control inventory reviewed, organization context, scope boundaries, the audit context, and any limitations on the analysis.

2. **Methodology Note** — a brief explanation of the tracking statuses (Control in place / Partial / No control / Unknown) and the evidence assessment, with the caveat that all classifications are workflow assessments subject to attorney verification and are not a compliance certification.

3. **Program Snapshot** — counts by tracking status; counts of evidence current versus stale or missing; the next audit date.

4. **Control Inventory and Requirement Map** — table:

   | # | Requirement | Source ref | Control | Owner | Evidence location | Last collected | Status |
   |---|---|---|---|---|---|---|---|
   | 1 | [from source] | [§ or provision] | [from inventory] | [function] | [where] | [date — CONFIRM] | Control in place / Partial / No control / Unknown |

5. **Evidence Status** — table or narrative of evidence by control, with stale and missing evidence flagged.

6. **Audit Calendar** — table: item, type (audit / evidence collection / remediation), date `[CONFIRM]`, owner.

7. **Gaps and Remediation Items** — table: item, severity, remediation (draft), proposed owner, target date `[CONFIRM]`.

8. **Priority View — Next Audit** — the items most urgent before the next audit.

9. **Open Questions** — requirements of unclear applicability, controls of uncertain scope, and interpretive questions for attorney or subject-matter resolution.

10. **Attorney Verification Items** — see the Attorney Verification Checklist below.

## Attorney Verification Checklist

- [ ] Every requirement in the tracker has been extracted from the actual framework source; none was supplied from model background knowledge without disclosure.
- [ ] The applicability of each requirement to this organization has been confirmed by an attorney with subject-matter expertise.
- [ ] Each "Control in place" status has been verified: the described control exists, is operative, and has been assessed as sufficient to address the requirement.
- [ ] Each control owner has confirmed ownership of the control and its evidence.
- [ ] Evidence locations have been verified, and stale or missing evidence has been scheduled for collection before the audit period closes.
- [ ] Every audit date, evidence-collection window, and remediation deadline has been confirmed against the actual audit timeline.
- [ ] Remediation items have been reviewed and supplemented by legal and operational judgment before being entered into a remediation plan.
- [ ] The scope of the tracker (which entity, business line, or system) has been confirmed and documented.
- [ ] The priority view reflects the organization's actual audit timeline and risk tolerance.
- [ ] All open questions have been resolved before the tracker is presented to an assessor, an auditor, or the board.
- [ ] The draft is labeled appropriately and is not represented as a compliance certification.
