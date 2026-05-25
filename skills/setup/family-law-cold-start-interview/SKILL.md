---
name: Family Law Cold-Start Interview
description: "Use when a family-law practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to a family-law attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled family-law practice profile draft for attorney review"
related_skills:
  - skills/family-law/matter-intake/SKILL.md
  - skills/family-law/divorce-intake-organizer/SKILL.md
  - skills/family-law/domestic-violence-safety-referral-checklist/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - family-law
---

# Family Law Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a family-law practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/family-law.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/family-law.md` for the first time.
- A family-law practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the family-law area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the family-law practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live family-law matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/family-law.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific family-law matter (use the appropriate matter-level skill for that task).

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
- In which states or countries does the group practice family law most frequently?
- Does the group regularly engage with UCCJEA (custody jurisdiction), UIFSA (support jurisdiction), or other interstate / international frameworks?
- Does the group regularly engage with Hague Convention (international child-abduction) matters?
- Are there sector-specific populations the group regularly engages with — military families, families with international ties — that require jurisdiction-specific knowledge?
- Are there jurisdictions or matter types the group treats as out of scope, requiring specialist outside counsel?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Does the group represent primarily one party in family-law matters (and which side, if any default), guardians ad litem, or both?
- What types of family-law matters does the group handle most frequently — divorce, custody, support, premarital / postnuptial agreements, adoption, domestic-violence protective orders, paternity?
- How is the team structured — partners, associates, paralegals, victim-advocate or social-work resources?
- How does the group coordinate with custody evaluators, financial neutrals, mental-health professionals, and victim advocates?
- Are there client categories — high-conflict, high-net-worth, families with domestic-violence indicators, blended families — that require special handling?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which matters automatically require escalation — domestic-violence indicator, capacity concern, multi-state custody question, international child-removal risk, child-welfare report, abuse allegation?
- Are there asset-value or income-level thresholds that trigger escalation to senior practitioners?
- When does a safety concern (escalating threats, removal risk, weapon access) require immediate intervention?
- Which engagement types — emergency custody petitions, protective-order responses, child-welfare-agency engagements — require attorney review regardless of stage?
- Who is the designated escalation contact for family-law matters, and what is the expected turnaround? Are there safety-specific escalation pathways?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should family-law work product default to memo format, intake-summary format, chronology format, or settlement-issues format?
- What level of detail does the practice group expect — executive summary, full fact-and-issue analysis, both layered?
- Are there house style rules for safety-flagging, contested-matter flagging, or open-items lists in family-law work product?
- Does the group produce custody-schedule organizers, settlement-issue catalogues, or hearing-preparation outlines in standard formats?
- Are there particular deliverable types — DV safety referrals, custody evaluations, asset-and-debt schedules — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative client-intake instrument, and where is it stored?
- Is there a chronology-template library, and how is it kept current?
- What document governs the group's jurisdiction-specific custody-rules reference?
- Are there safety-screening protocols and victim-advocate-referral resources the group treats as authoritative?
- Does the group maintain a financial-disclosure framework (asset / debt schedules, income-and-expense forms) tied to applicable court forms?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default posture on emergency custody — what facts trigger an emergency petition, what defaults govern the response?
- What is the group's default relocation posture — preferred process, custody-evaluation involvement, when contested?
- What is the group's default abuse-screening protocol — at every intake, situational, or other?
- What is the group's default approach to parenting coordinators, special masters, and other neutral roles?
- What is the group's default approach to settlement vs. litigation framing in initial intake?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review of family-law work product become mandatory — initial intake, any safety-screening output, any draft pleading, any settlement document?
- Are there work-product types for which attorney review is always required regardless of stage — any filing, any custody arrangement, any settlement, any domestic-violence-related document?
- What is the designated reviewer's role — handling attorney, supervising attorney, partner?
- What is the expected turnaround for standard family-law review, and how are urgent reviews (emergency custody, protective-order responses) handled? What is the after-hours escalation pathway?
- Is there a formal sign-off step before any filing, settlement, or court-ordered evaluation?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — that custody is uncontested, that no DV is present, that all assets are disclosed, that a parenting plan is enforceable in another state?
- Are there family-law-specific risks — domestic-violence escalation, child-removal risk, capacity concern, undisclosed asset, undue influence — where an agent must stop and escalate rather than reason through independently?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — protective-order matters, DV-indicator matters, child-welfare matters, capacity-concern matters?
- Are there prior incidents — adverse outcomes, court findings, bar inquiries — that should be encoded as explicit prohibitions for agents working on family-law matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/family-law.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/family-law.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Safety-screening protocol is accurately recorded and an immediate-escalation pathway is named.
- [ ] Jurisdiction coverage — including UCCJEA, UIFSA, and Hague — is accurately recorded.
- [ ] Emergency-custody and protective-order escalation thresholds are accurately recorded and any associated deadlines are marked `[deadline verification required]`.
- [ ] Confidentiality framework protects victim and child information at the appropriate level.
- [ ] Mandatory-reporter obligations are accurately recorded `[verify jurisdiction]`.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/family-law.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
