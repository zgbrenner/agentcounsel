---
name: M&A Cold-Start Interview
description: "Use when an M&A practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to an M&A attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled M&A practice profile draft for attorney review"
related_skills:
  - skills/m-and-a/acquisition-diligence-request-list/SKILL.md
  - skills/m-and-a/purchase-agreement-issue-list/SKILL.md
  - skills/m-and-a/closing-deliverables-tracker/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - m-and-a
---

# M&A Cold-Start Interview

## Purpose

Conduct a structured, staged interview with an M&A practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/m-and-a.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/m-and-a.md` for the first time.
- An M&A practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the M&A area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the M&A practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live M&A matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/m-and-a.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific M&A matter (use the appropriate matter-level skill for that task).

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
- In which countries, states, or provinces does the group form deal entities, perform diligence, and close transactions most frequently?
- Does the group regularly engage cross-border deals, and which deal-side jurisdictions (target operations, regulatory reach) drive most of that work?
- Are there merger-control regimes (HSR, EU, UK, China, India, Brazil) the group regularly files in, and which counsel handles each?
- Does the group regularly engage with foreign-investment-screening regimes (CFIUS, EU FDI, UK NSIA, China security review)?
- Are there sectors or jurisdictions the group treats as out of scope, requiring specialist counsel?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Does the group represent primarily buy-side, sell-side, or both?
- Are clients primarily financial sponsors, strategics, founders, family offices, or a mix? Confirm the default representation profile.
- How is the team structured — partners, associates, deal coordinators, specialists embedded (tax, IP, antitrust, employment, environmental)?
- Are there client industries or deal types that require special handling — regulated industries, public-company targets, distressed M&A, private-equity portfolio activity?
- How does the group coordinate with specialist counsel (tax, IP, antitrust, environmental, employment) on deal teams?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which deal characteristics automatically require escalation or specialist involvement — cross-border, public-company target, regulated industry, sanctioned-counterparty risk, antitrust filing, foreign-investment screening?
- Are there transaction-size or deal-value thresholds that trigger escalation, and what are they?
- When does a reps-and-warranties insurance question, a tax-structuring question, or an antitrust-clearance question require mandatory specialist involvement?
- Which due-diligence findings (material liabilities, fraud indicia, customer concentration concerns) require partner-level escalation regardless of stage?
- Who is the designated escalation contact for M&A matters above the group's thresholds, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should M&A work product default to diligence-report format, issues memo, redline + markup format, or closing-checklist format?
- What level of detail does the practice group expect for diligence reports — executive summary, full issue-by-issue analysis, both layered?
- Are there house style rules for risk ratings, deal-breaker flags, or negotiation-leverage notes in M&A work product?
- Does the group produce closing certificates, closing memos, or integration plans in a standard format?
- Are there particular deliverable types — reps & warranties analysis, MAE assessment, indemnification scorecard — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative form purchase agreement (or library of forms), and where is it stored?
- Is there a reps and warranties schedule library, and how is it kept current?
- What document governs the group's closing-checklist template?
- Does the group maintain a diligence-request-list template, and is it tailored by deal type or sector?
- Is there an integration-playbook reference, and where is it stored?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default position on indemnification — caps, baskets, deductibles, exclusivity of remedy, sandbagging?
- What is the group's default MAE / MAC definition framework?
- What is the group's default reps & warranties insurance posture — required, preferred, situational?
- What is the group's default position on specific performance, expense reimbursement, or termination fees?
- What is the group's default preference between equity and asset structures, and what factors drive deviation?
- What is the group's default approach to escrows, working-capital adjustments, and earnouts?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review of M&A work product become mandatory — initial diligence summary, LOI, definitive agreement, closing certificates, post-closing integration?
- Are there work-product types for which attorney review is always required regardless of stage — any definitive agreement, any reps & warranties policy, any HSR filing, any CFIUS filing?
- What is the designated reviewer's role — handling attorney, supervising attorney, deal partner, general counsel, board?
- What is the expected turnaround for definitive-agreement markups, and how are urgent reviews (signing readiness, closing-day issues) handled?
- Is there a formal sign-off step before signing, before closing, or before delivering any closing certificate?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — that an entity is in good standing, that quorum was duly met, that filings have been made, that consents are duly authorized, that reps survive in the form drafted?
- Are there M&A-specific risks — fraud, undisclosed liabilities, customer concentration, regulatory non-compliance — where an agent must stop and escalate rather than reason through independently?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — public-company targets, distressed transactions, sanctioned-counterparty risk, hostile transactions?
- Are there prior incidents — failed deals, post-closing claims, regulator inquiries — that should be encoded as explicit prohibitions for agents working on M&A matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/m-and-a.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/m-and-a.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdiction coverage — including merger-control and foreign-investment-screening regimes — is accurately recorded.
- [ ] Specialist-counsel allocation (tax, antitrust, IP, environmental, employment, regulatory) on deal teams is current.
- [ ] Indemnification, MAE, and reps-and-warranties insurance defaults reflect the group's current market posture.
- [ ] Closing checklists and reps schedules referenced are current.
- [ ] Signing, closing, and filing deadlines are marked `[deadline verification required]` in any deliverable that depends on them.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/m-and-a.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
