---
name: Tax Cold-Start Interview
description: "Use when a tax practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to a tax attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled tax practice profile draft for attorney review"
related_skills:
  - skills/tax/tax-issue-intake/SKILL.md
  - skills/tax/international-tax-issue-spotter/SKILL.md
  - skills/tax/sales-use-tax-nexus-triage/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - tax
---

# Tax Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a tax practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/tax.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/tax.md` for the first time.
- A tax practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the tax area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the tax practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live tax matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/tax.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific tax matter (use the appropriate matter-level skill for that task).

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
- In which jurisdictions does the group advise — US federal, US state and local (and which states are most common), international, treaty-based?
- Does the group handle cross-border matters routinely, and which treaty relationships drive most of that work?
- Are there sales-and-use, VAT/GST, transfer-pricing, or other transactional regimes the group regularly advises on?
- Are there jurisdictions where the group works only through specified foreign tax counsel, and how is that allocation tracked?
- Are there jurisdictions the group treats as out of scope, requiring specialist outside tax counsel?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- What types of tax matters does the group handle most frequently — planning, controversy, transactional, compliance support, opinions?
- Are clients primarily corporate, partnership/LLC, high-net-worth individual, tax-exempt, or a mix?
- How is the team structured — tax partners, associates, LL.M.-tax specialists, transfer-pricing economists, CPAs supporting the team?
- How does the group coordinate with accountants, transfer-pricing economists, and external tax preparers?
- Are there client categories — financial sponsors, REITs, tax-exempt entities, multinationals — that require special handling?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which tax matters automatically require escalation — cross-border structuring, transfer pricing, tax-exempt entity questions, IRS audit / agency inquiry, ruling requests, M&A tax structuring?
- Are there transaction-value or tax-amount thresholds that trigger escalation, and what are they?
- When does a tax position rise to a 'reportable transaction' or other disclosure-required posture that requires immediate review?
- Which tax-opinion requests (will / should / would / more-likely-than-not) require partner-level review regardless of size?
- Who is the designated escalation contact for tax matters, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should tax work product default to formal memo format, structuring deck, opinion letter, or controversy-defense memo?
- What level of detail does the practice group expect — executive summary, full citation-supported analysis, both layered?
- Are there house style rules for citation format, levels of assurance (will / should / more-likely-than-not), or 'wandering issues' flagging in tax work product?
- Does the group produce structuring decks or step plans, and if so, in what format?
- Are there particular deliverable types — opinion letters, ruling requests, controversy memos — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative tax-positions library, and where is it stored?
- Is there a transfer-pricing policy or documentation framework, and how is it kept current?
- What document governs the group's M&A tax-structuring playbook?
- Are there controversy precedents (prior audit defense, prior IRS appeals, prior ruling requests) the group treats as authoritative for similar matters?
- Is there a tax-elections checklist or treasury-checklist the group references?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default assurance-level framework — when do matters warrant a will opinion, a should opinion, a more-likely-than-not opinion?
- What is the group's default chain-of-authority approach — strict reliance on primary authority, layered approach, or other?
- What is the group's default substance-over-form posture — strict, deferential, mixed?
- What is the group's default position on reportable-transaction disclosure?
- What is the group's default approach to tax-exempt entity matters, if applicable?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review of tax work product become mandatory — initial issue spotting, opinion drafting, ruling submission, controversy filings?
- Are there work-product types for which attorney review is always required regardless of size — any opinion, any IRS submission, any structuring memo on a multi-step plan, any tax position taken on a return?
- What is the designated reviewer's role — handling attorney, supervising tax partner, LL.M. specialist, peer reviewer?
- What is the expected turnaround for opinion review, and how are urgent reviews (filing deadlines, audit responses) handled?
- Is there a formal sign-off step before an opinion is delivered, a ruling is submitted, or a tax position is communicated to the client?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — that a tax position is sustained on audit, that an entity classification is current, that a treaty applies, that a ruling continues to bind, that an exemption is preserved?
- Are there tax-specific risks — substance over form, economic substance, reportable transaction, anti-abuse — where an agent must stop and escalate rather than reason through independently?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — opinions, rulings, structuring on multi-step plans, controversy filings?
- Are there prior incidents — adverse audit findings, IRS challenges, sanctions — that should be encoded as explicit prohibitions for agents working on tax matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/tax.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/tax.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdiction coverage — federal, state, local, international, treaty — is accurately recorded `[Verify current law]`.
- [ ] Assurance-level framework (will / should / more-likely-than-not / reasonable basis) is current and tied to the group's engagement-letter and malpractice posture `[ATTORNEY TO CONFIRM]`.
- [ ] Reportable-transaction disclosure framework reflects current IRS guidance `[Verify current law]`.
- [ ] Tax-positions library references are current and version-controlled.
- [ ] Statute-of-limitations and filing-deadline triggers in any related matters are marked `[deadline verification required]`.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/tax.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
