---
name: Insurance Cold-Start Interview
description: "Use when an insurance practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to an insurance attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled insurance practice profile draft for attorney review"
related_skills:
  - skills/insurance/insurance-policy-summary/SKILL.md
  - skills/insurance/coverage-issue-spotter/SKILL.md
  - skills/insurance/reservation-of-rights-review/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - insurance
---

# Insurance Cold-Start Interview

## Purpose

Conduct a structured, staged interview with an insurance practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/insurance.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/insurance.md` for the first time.
- An insurance practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the insurance area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the insurance practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live insurance matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/insurance.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific insurance matter (use the appropriate matter-level skill for that task).

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
- In which states or countries does the group practice insurance law most frequently?
- Does the group regularly engage with NAIC-uniform frameworks vs. state-specific regimes, and how is that allocation tracked?
- Are there foreign insurance markets (Lloyd's, Bermuda, Cayman captives) the group regularly engages with?
- Are there sectors of insurance — commercial, personal, reinsurance, surplus lines, captive — that drive most of the work?
- Are there jurisdictions or sectors the group treats as out of scope, requiring specialist outside counsel?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Does the group represent primarily policyholders, carriers, brokers, reinsurers, or a mix?
- What types of insurance matters does the group handle most frequently — coverage advisory, claims handling, policy review, reinsurance, regulatory, bad-faith litigation?
- How is the team structured — partners, associates, claims specialists, policy-drafting specialists?
- How does the group coordinate with insurance brokers, claims professionals, and reinsurance counterparties?
- Are there client categories — Fortune 500 policyholders, individual policyholders, reinsurance markets — that require special handling?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which matters automatically require escalation — bad-faith concern, coverage denial, reservation of rights, settlement-authority question, reinsurance coverage dispute?
- Are there claim-value thresholds or coverage-amount thresholds that trigger escalation?
- When does a regulatory matter (market conduct, financial examination) require immediate specialist involvement?
- Which engagement types — coverage opinions, ROR letters, declaratory-judgment posture — require partner-level review regardless of size?
- Who is the designated escalation contact for insurance matters, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should insurance work product default to coverage-opinion format, claim-chronology format, policy-summary format, or memo format?
- What level of detail does the practice group expect — executive summary, full citation-supported coverage analysis, both layered?
- Are there house style rules for citation format (case law, regulatory guidance, policy provisions), coverage-determination flagging, or open-items lists in insurance work product?
- Does the group produce ROR letters, certificate-of-insurance reviews, or claim chronologies in standard formats?
- Are there particular deliverable types — coverage opinions, ROR letters, denial letters — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative policy library and policy-form reference, and where is it stored?
- Is there an ROR letter template library, and how is it kept current?
- What document governs the group's coverage-issue precedent library?
- Are there reinsurance-precedent references the group treats as authoritative?
- Does the group maintain a jurisdiction-by-jurisdiction reference on bad-faith law, claims-handling regulations, and direct-action statutes?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default coverage-determination framework — when does a matter warrant a full coverage opinion vs. a coverage issue-spotting summary?
- What is the group's default reservation-of-rights posture — when warranted, what scope?
- What is the group's default bad-faith risk-assessment framework?
- What is the group's default subrogation posture — preservation, pursuit, waiver thresholds?
- What is the group's default position on additional-insured certificates and waivers of subrogation?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review of insurance work product become mandatory — initial intake, draft coverage opinion, draft ROR letter, claims-handling decision, settlement authority?
- Are there work-product types for which attorney review is always required regardless of size — any coverage opinion, any ROR letter, any claims-handling decision above a threshold, any settlement above a threshold?
- What is the designated reviewer's role — handling attorney, supervising attorney, claim partner, coverage partner?
- What is the expected turnaround for standard coverage review, and how are urgent reviews (claim deadlines, ROR-letter timing) handled?
- Is there a formal sign-off step before any coverage opinion, ROR letter, or denial letter is delivered?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — that coverage exists, that a duty to defend is owed, that bad faith does not apply, that subrogation is preserved, that an additional-insured certificate is current?
- Are there insurance-specific risks — bad faith, coverage waiver, late notice, anti-stacking, anti-subrogation rules — where an agent must stop and escalate rather than reason through independently?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — coverage opinions, ROR letters, settlement authority, declaratory-judgment actions?
- Are there prior incidents — bad-faith judgments, market-conduct findings — that should be encoded as explicit prohibitions for agents working on insurance matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/insurance.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/insurance.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdiction coverage — including bad-faith law and direct-action statutes — is accurately recorded `[verify jurisdiction]`.
- [ ] Coverage-opinion framework reflects the group's current considered posture `[ATTORNEY TO CONFIRM]`.
- [ ] ROR letter template references are current and any related notice deadlines are marked `[deadline verification required]`.
- [ ] Bad-faith risk-assessment framework reflects current law in in-scope jurisdictions `[Verify current law]`.
- [ ] Subrogation and additional-insured defaults are current.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/insurance.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
