---
name: Trusts and Estates Cold-Start Interview
description: "Use when a trusts and estates practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to a trusts and estates attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled trusts and estates practice profile draft for attorney review"
related_skills:
  - skills/trusts-estates/estate-planning-intake/SKILL.md
  - skills/trusts-estates/post-death-administration-task-tracker/SKILL.md
  - skills/trusts-estates/trust-administration-tracker/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - trusts-estates
---

# Trusts and Estates Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a trusts and estates practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/trusts-estates.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/trusts-estates.md` for the first time.
- A trusts and estates practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the trusts and estates area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the trusts and estates practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live trusts and estates matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/trusts-estates.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific trusts and estates matter (use the appropriate matter-level skill for that task).

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
- In which states or countries does the group regularly handle estate-planning and trust-administration matters?
- Are there situs questions the group routinely encounters — trust situs, real-property situs, multi-state property, foreign-property holdings?
- Does the group regularly handle non-resident-alien beneficiaries, international beneficiaries, or international estate-tax exposures?
- Are there jurisdictions the group treats as out of scope (e.g., specialized offshore jurisdictions), requiring specialist counsel?
- Does the group maintain jurisdiction-by-jurisdiction reference materials on estate, inheritance, GST, and gift-tax regimes?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- What types of trusts-and-estates matters does the group handle most frequently — estate planning, trust administration, probate, contested matters, charitable structures?
- Are clients primarily ultra-high-net-worth, high-net-worth, general estate-planning, family offices, or institutional fiduciaries?
- How is the team structured — partners, associates, paralegals, trust officers, fiduciary administrators?
- How does the group coordinate with corporate fiduciaries, tax advisors, accountants, and investment advisors?
- Are there client categories — multi-generational families, blended families, special-needs beneficiaries, business-owning families — that require special handling?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which matters automatically require escalation — contested matters, capacity questions, undue-influence concerns, tax-driven structures, charitable-structure design, international situs?
- Are there asset-value thresholds (total estate value, single-trust value, gift-tax-exposure value) that trigger escalation?
- When does a fiduciary-conflict question — including a question about the group's own duties — require immediate review?
- Which trust-administration events (significant distribution, modification, decanting, termination) require attorney review regardless of size?
- Who is the designated escalation contact for trusts-and-estates matters, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should trusts-and-estates work product default to memo format, structured intake format, trust-administration tracker format, or document drafts?
- What level of detail does the practice group expect — executive summary, full reasoning, both layered?
- Are there house style rules for risk ratings, contested-matter flags, or open-items lists in trusts-and-estates work product?
- Does the group produce funding checklists, trust-administration calendars, or estate-administration timelines in a standard format?
- Are there particular deliverable types — estate-tax memos, fiduciary accounting reviews, trustee-decision memos — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative estate-planning intake instrument, and where is it stored?
- Is there a trust-administration playbook or calendar template, and how is it kept current?
- What document governs the group's standard testamentary-document library — wills, trusts, powers, healthcare directives?
- Are there sample-document libraries for non-standard structures (dynasty trusts, GRATs, ILITs, charitable trusts) the group treats as authoritative?
- Does the group maintain jurisdiction-specific reference materials for estate, gift, GST, and inheritance taxes?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default capacity-assessment threshold, and how does it integrate medical or other evidence?
- What is the group's default revocable-trust posture — revocable trust as core estate-planning tool, or will-based planning with trusts as supplements?
- What is the group's default position on powers of appointment, decanting, and trust-modification mechanisms?
- What is the group's default portability election posture?
- What is the group's default approach to charitable structures (private foundations, donor-advised funds, charitable trusts)?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review of estate-planning work product become mandatory — initial intake, draft document, signing, post-signing?
- Are there work-product types for which attorney review is always required regardless of size — any will, any trust agreement, any tax election, any contested-matter filing, any fiduciary-conflict memo?
- What is the designated reviewer's role — handling attorney, supervising partner, designated fiduciary attorney?
- What is the expected turnaround for standard document review, and how are urgent reviews (terminal-illness drafting, deadline-driven elections) handled?
- Is there a formal sign-off step before a document is finalized, an election is filed, or a trustee decision is communicated?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — that capacity is intact, that no undue influence applies, that an estate is non-taxable, that a trust is properly funded, that a beneficiary designation is current?
- Are there trusts-and-estates risks — capacity, undue influence, fiduciary breach, fraudulent transfer, tax-driven recharacterization — where an agent must stop and escalate rather than reason through independently?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — contested matters, will contests, trust contests, fiduciary-conflict matters?
- Are there prior incidents — adverse judgments, fiduciary findings, malpractice claims — that should be encoded as explicit prohibitions for agents working on trusts-and-estates matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/trusts-estates.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/trusts-estates.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdiction coverage — including situs and multi-state property — is accurately recorded `[verify jurisdiction]`.
- [ ] Capacity-assessment threshold reflects the group's current considered posture, not a provisional one.
- [ ] Tax-driven structures and elections are tied to current authority `[Verify current law]` and all related deadlines are marked `[deadline verification required]`.
- [ ] Fiduciary-conflict protocols are accurately recorded and consistent with applicable professional-responsibility rules.
- [ ] Confidentiality posture protects beneficiary information at the appropriate level.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/trusts-estates.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
