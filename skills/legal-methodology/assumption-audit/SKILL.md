---
name: Assumption Audit
description: "Use when extracting and auditing explicit assumptions, hidden assumptions, missing facts, missing documents, jurisdiction gaps, deadline gaps, client-role ambiguity, escalation items, business decision points, and professional-responsibility concerns in draft legal work product."
practice_area: legal-methodology
task_type: verification
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The draft legal output to audit"
  - "The user-provided facts, source documents, and instructions available for comparison"
  - "The intended use, audience, jurisdiction, and client role if known"
outputs:
  - "Assumption audit table"
  - "Missing-information and escalation list"
related_skills:
  - skills/legal-methodology/source-validation/SKILL.md
  - skills/legal-methodology/attorney-review-gate/SKILL.md
  - skills/legal-methodology/red-team-verifier/SKILL.md
tags:
  - legal-methodology
  - assumptions
  - missing-facts
  - quality-control
  - verification
---

# Assumption Audit

## Purpose

Audit a draft legal output for assumptions and unresolved gaps. The skill extracts explicit assumptions, hidden assumptions, missing facts, missing documents, jurisdiction gaps, deadline gaps, client-role ambiguity, attorney escalation items, business decision points, and professional-responsibility concerns.

It then recommends revisions or placeholders for any output that relies on unresolved assumptions.

## Use When

- A draft may have filled gaps silently or treated uncertain facts as established.
- A document review, research memo, client update, demand letter, or risk matrix contains assumptions or missing-input notes.
- The user asks what facts are still needed, what assumptions are built into the analysis, or what could change the conclusion.
- A matter is moving from a draft output into attorney review or a matter workspace.

## Required Inputs

- The complete draft to audit.
- The source documents, user facts, and instructions available for comparison.
- The intended use, audience, client role, and jurisdiction if known.

If the draft is missing, stop and request it. If source materials are missing, audit the draft internally and mark the source-comparison limitation.

## Do Not Use When

- The task is to supply missing facts or legal analysis. This skill identifies gaps; it does not fill them.
- The user wants a final legal conclusion despite missing information.
- The task is citation-focused; use `citation-integrity-check` or `source-validation`.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Follow `core/source-and-citation-discipline.md` and `core/jurisdiction-and-deadline-gates.md`.
- Do not resolve missing facts, documents, jurisdiction, deadlines, or client-role ambiguity by guessing.
- Do not convert an assumption into a fact. Label assumptions and route them for confirmation.
- Preserve confidentiality and privilege.

## Workflow

1. **Confirm scope and inputs.** Identify the draft type, source materials, intended use, audience, and known jurisdiction/client role.
2. **Extract explicit assumptions.** List every statement labeled as assumption, premise, caveat, limitation, or subject-to-confirmation item.
3. **Find hidden assumptions.** Identify conclusions that depend on unstated facts, documents, legal rules, party status, timing, client objectives, or business decisions.
4. **Find missing facts.** List absent facts that could change the analysis, risk rating, recommendation, or tone.
5. **Find missing documents.** List agreements, amendments, exhibits, policies, communications, filings, source law, or evidence the draft appears to need.
6. **Audit jurisdiction and deadlines.** Flag missing or assumed jurisdiction, governing law, venue, agency, court, effective dates, filing dates, response dates, notice periods, and other legal dates.
7. **Audit client-role ambiguity.** Identify uncertainty about who the client is, who the output protects, what side the client is on, and whether conflicts or privilege concerns may exist.
8. **Identify escalation items.** Flag attorney judgment items, business decision points, professional-responsibility concerns, and confidentiality/privilege concerns.
9. **Recommend safer markings.** For each unresolved assumption or gap, recommend a revision, placeholder, or stop-and-ask item.

## Output Format

Deliver:

1. **Draft Label** — "Draft legal work product for attorney review. Not legal advice."
2. **Audit Summary** — Overall readiness and the highest-risk unresolved assumptions.
3. **Assumption Table**

   | # | Assumption or gap | Type | Location | Why it matters | Recommended marking or revision |
   |---|---|---|---|---|---|

   Types: explicit assumption | hidden assumption | missing fact | missing document | jurisdiction gap | deadline gap | client-role ambiguity | attorney escalation | business decision point | professional-responsibility concern.

4. **Output Revisions Needed** — Sentences or sections that should be rewritten, bracketed, or withheld until assumptions are resolved.
5. **Stop-and-Ask Questions** — The minimum questions needed before the draft can proceed.
6. **Attorney Escalation Items** — Items requiring attorney judgment before reliance or external use.

## Attorney Verification Checklist

- [ ] Every explicit assumption has been confirmed, corrected, or preserved as an assumption.
- [ ] Every hidden assumption has been surfaced.
- [ ] Missing facts and documents have been requested or the limitation has been accepted by counsel.
- [ ] Jurisdiction and governing law are confirmed or visibly flagged.
- [ ] Every deadline or legally significant date is attorney-verified.
- [ ] Client role, recipient, and privilege posture are confirmed.
- [ ] No draft section relies on an unresolved assumption as if it were fact.
