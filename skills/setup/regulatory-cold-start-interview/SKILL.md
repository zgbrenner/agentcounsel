---
name: Regulatory Cold-Start Interview
description: "Use when a regulatory practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to a regulatory attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled regulatory practice profile draft for attorney review"
related_skills:
  - skills/regulatory/compliance-gap-matrix/SKILL.md
  - skills/regulatory/compliance-program-tracker/SKILL.md
  - skills/regulatory/enforcement-risk-memo/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - regulatory
---

# Regulatory Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a regulatory practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/regulatory.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/regulatory.md` for the first time.
- A regulatory practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the regulatory area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the regulatory practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live regulatory matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/regulatory.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific regulatory matter (use the appropriate matter-level skill for that task).

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
- In which jurisdictions and before which agencies does the group regularly practice — US federal agencies (which ones), US state agencies, foreign regulators, multi-jurisdictional matters?
- What sectors does the group regularly engage with — energy, telecom, healthcare, financial services, transportation, environment, consumer protection?
- Are there sectors or agencies the group treats as out of scope, requiring specialist outside counsel?
- Does the group maintain agency-specific or sector-specific reference materials, and where are they stored?
- Does the group track foreign regulatory developments that affect US clients (e.g., EU regulatory parallels)?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Does the group represent primarily regulated entities, complainants, intervenors, or a mix?
- What types of regulatory matters does the group handle most frequently — advisory, rulemaking participation, license / permit, enforcement defense, agency engagement?
- How is the team structured — sector specialists, generalist regulatory counsel, paralegals, consultant relationships?
- How does the group coordinate with sector technical experts, government-affairs counsel, lobbyists, and trade associations?
- Are there client categories — public-utility holding companies, hospitals, banks, broker-dealers — that require special handling?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which matters automatically require escalation — regulatory inquiry, subpoena / CID, sanctions risk, license / permit revocation, rulemaking participation above threshold?
- Are there sector-specific scenarios — bank examiner inquiry, FDA warning letter, FTC investigative demand — that require immediate review?
- When does an agency engagement (informal meeting, settlement discussion, consent decree negotiation) require partner-level involvement?
- Which rulemaking matters (notice-and-comment, hearing participation, ex parte) require attorney review regardless of size?
- Who is the designated escalation contact for regulatory matters, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should regulatory work product default to memo format, agency-letter format, comment-letter format, or compliance-checklist format?
- What level of detail does the practice group expect — executive summary, full reasoning with agency-precedent citations, both layered?
- Are there house style rules for citation format (agency decisions, no-action letters, guidance documents), risk ratings, or open-items lists?
- Does the group produce rulemaking-comment letters or compliance-program review memos in standard formats?
- Are there particular deliverable types — agency responses, comment letters, enforcement-defense memos — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative library of agency-precedent references, and where is it stored?
- Is there a regulatory-tracking system (rulemaking docket, enforcement actions, agency-guidance changes), and how is it kept current?
- What document governs the group's comment-letter framework?
- Are there compliance-program-review templates or audit-checklist templates the group treats as authoritative?
- Does the group maintain agency-specific protocols for informal contacts, voluntary disclosures, and settlement engagement?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default regulatory engagement posture — proactive engagement, reactive engagement, situational?
- What is the group's default rulemaking-participation threshold — what types of rulemakings warrant a comment letter, and what types warrant a presence at hearings?
- What is the group's default approach to voluntary disclosures — when warranted, what scope?
- What is the group's default comment-letter framework — issue spotting, position taking, both?
- What is the group's default compliance-program-review posture for new regulatory regimes?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review of regulatory work product become mandatory — initial intake, draft comment letter, draft agency response, draft compliance-program update?
- Are there work-product types for which attorney review is always required regardless of size — any agency filing, any rulemaking comment, any voluntary disclosure, any consent-decree negotiation?
- What is the designated reviewer's role — handling attorney, supervising sector partner, regulatory specialist?
- What is the expected turnaround for regulatory review, and how are urgent reviews (agency-deadline-driven, enforcement matters) handled?
- Is there a formal sign-off step before any agency submission or rulemaking comment is filed?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — that a regulation is current, that an interpretation is binding, that an exemption applies, that an enforcement action is unlikely, that an agency precedent is on point?
- Are there regulatory risks — investigation, enforcement, license-revocation, criminal referral — where an agent must stop and escalate rather than reason through independently?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — agency investigations, consent-decree matters, enforcement defense?
- Are there prior incidents — adverse enforcement actions, consent decrees, regulatory findings — that should be encoded as explicit prohibitions for agents working on regulatory matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/regulatory.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/regulatory.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Agency / jurisdiction coverage and sector specialization are accurately recorded.
- [ ] Regulatory-tracking system reference is current and maintenance owner is named.
- [ ] Voluntary-disclosure framework and rulemaking-participation thresholds reflect the group's current considered posture.
- [ ] Agency deadlines (comment periods, response windows, hearing dates) are marked `[deadline verification required]` in any related deliverable.
- [ ] Current-law verification is required for any analysis that turns on a regulation, agency interpretation, or guidance document `[Verify current law]`.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/regulatory.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
