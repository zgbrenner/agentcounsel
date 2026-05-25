---
name: Real Estate Cold-Start Interview
description: "Use when a real estate practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to a real estate attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled real estate practice profile draft for attorney review"
related_skills:
  - skills/real-estate/psa-review/SKILL.md
  - skills/real-estate/commercial-lease-review/SKILL.md
  - skills/real-estate/title-survey-objection-tracker/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - real-estate
---

# Real Estate Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a real estate practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/real-estate.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/real-estate.md` for the first time.
- A real estate practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the real estate area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the real estate practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live real estate matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/real-estate.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific real estate matter (use the appropriate matter-level skill for that task).

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
- In which states or countries does the group handle real-estate matters most frequently — commercial, residential, industrial, mixed?
- Does the group regularly engage with multi-state portfolios, and which jurisdictions are most common?
- Are there municipal regimes — rent control / RSO, transfer-tax rules, building-code regimes — that drive a meaningful share of the work?
- Does the group regularly engage with foreign-jurisdiction property matters?
- Are there sectors or jurisdictions the group treats as out of scope, requiring specialist counsel?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Does the group represent primarily owners, tenants, lenders, developers, REITs, or a mix?
- What types of real-estate matters does the group handle most frequently — acquisitions and dispositions, leasing, development, financing, title resolution, environmental, zoning?
- How is the team structured — partners, associates, paralegals, title specialists, surveyors?
- Are there asset types (multifamily, office, industrial, retail, hospitality, mixed-use) that require special handling?
- How does the group coordinate with title insurance, lenders, environmental consultants, and zoning counsel?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which findings automatically require escalation — title defect (encumbrance, easement, lien), zoning non-conformity, environmental issue (CERCLA, state superfund, brownfield), historic-preservation issue?
- Are there deal-value thresholds that trigger escalation?
- When does a rent-control / RSO question or a fair-housing question require immediate specialist involvement?
- Which lender-required deliverables (SNDA, estoppel, non-disturbance) require partner-level review regardless of stage?
- Who is the designated escalation contact for real-estate matters, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should real-estate work product default to issue-list format, redline format, closing-checklist format, or narrative memo?
- What level of detail does the practice group expect for diligence reports — executive summary, full issue analysis, both layered?
- Are there house style rules for risk ratings, deal-breaker flags, or open-items lists in real-estate work product?
- Does the group produce lease abstracts, title-objection letters, or closing memos in a standard format?
- Are there particular deliverable types — title objections, estoppel certificates, environmental memos — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative lease-template library, and where is it stored?
- Is there a closing-checklist template, and how is it tailored by asset class or jurisdiction?
- What document governs the group's title-objection or title-objection-letter framework?
- Are there environmental-review checklists or guidance the group treats as authoritative?
- Does the group maintain a jurisdiction-by-jurisdiction reference on transfer taxes, recording requirements, and local-rule peculiarities?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default SNDA posture — required, preferred, negotiable?
- What is the group's default estoppel content — minimum content, expanded content?
- What is the group's default position on lender approval rights, particularly for transfers and leasing decisions?
- What is the group's default position on permitted-use carveouts, exclusive-use clauses, and radius restrictions?
- What is the group's default lien-priority posture and approach to subordination?
- What is the group's default approach to environmental reps and indemnities?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review of real-estate work product become mandatory — initial diligence summary, LOI, definitive agreement, closing certificates, post-closing matters?
- Are there work-product types for which attorney review is always required regardless of size — any deed, any lease above a threshold, any title-objection letter, any environmental memo?
- What is the designated reviewer's role — handling attorney, supervising attorney, partner, general counsel?
- What is the expected turnaround for definitive-agreement and lease review, and how are urgent reviews (closing-day issues, title-clearance pressures) handled?
- Is there a formal sign-off step before closing, before recording, or before delivering any closing certificate?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — that title is clean, that zoning is conforming, that no environmental issues exist, that lender consent is given, that no easements affect use?
- Are there real-estate risks — environmental, title, zoning, rent-control, fair-housing — where an agent must stop and escalate rather than reason through independently?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — environmental contamination, title disputes, zoning variance applications?
- Are there prior incidents — failed closings, title disputes, environmental claims — that should be encoded as explicit prohibitions for agents working on real-estate matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/real-estate.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/real-estate.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdiction coverage — including municipal regimes — is accurately recorded.
- [ ] Title, environmental, and zoning escalation triggers are accurately recorded.
- [ ] Lender-required deliverables (SNDA, estoppel, non-disturbance) defaults reflect current market practice.
- [ ] Transfer-tax, recording, and filing deadlines are marked `[deadline verification required]` in any related deliverable.
- [ ] Environmental-risk posture is current and tied to applicable CERCLA / state superfund / brownfield frameworks `[Verify current law]`.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/real-estate.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
