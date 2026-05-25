---
name: Intellectual Property Cold-Start Interview
description: "Use when an intellectual property practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to an intellectual property attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled intellectual property practice profile draft for attorney review"
related_skills:
  - skills/ip/trademark-clearance-triage/SKILL.md
  - skills/ip/fto-triage/SKILL.md
  - skills/ip/open-source-license-review/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - ip
---

# Intellectual Property Cold-Start Interview

## Purpose

Conduct a structured, staged interview with an intellectual property practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/ip.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/ip.md` for the first time.
- An intellectual property practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the intellectual property area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the intellectual property practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live intellectual property matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/ip.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific intellectual property matter (use the appropriate matter-level skill for that task).

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
- In which countries or territories does the group prosecute, defend, or counsel on IP matters most frequently?
- Does the group handle multi-jurisdictional filings (PCT, Madrid Protocol, EUTM, Hague System), and how is jurisdiction coverage allocated across the team?
- Are there sector-specific regimes the group regularly engages with — FDA-regulated technologies, export-controlled subject matter, semiconductor or AI-specific IP regimes?
- Are there jurisdictions where the group works only through specified foreign counsel, and how is that allocation tracked?
- Are there jurisdictions the group treats as out of scope entirely, requiring routing to specialist outside counsel?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Does the group represent primarily IP owners, IP users (licensees, defendants), or both? Confirm the default representation posture.
- What types of IP matters does the group handle most frequently — prosecution, litigation, counseling, clearance, licensing, open-source compliance, trade-secret protection?
- How is the team structured — registered patent attorneys / agents, trademark specialists, copyright counsel, technology specialists, paralegals?
- Are there client industries or technology areas that require special handling or additional sign-off — for example, life sciences, semiconductor, AI, software?
- How does the group coordinate with patent agents, foreign counsel, and specialist counsel (e.g., antitrust counsel for SEP/F-RAND matters)?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which engagement types automatically require attorney review before reliance — clearance opinions, FTO opinions, validity opinions, infringement opinions, non-infringement opinions?
- Are there bar-date or statutory-deadline events (patent on-sale, public-use, priority filing windows) that always require escalation?
- Which industry-specific scenarios — standard-essential patents, F/RAND obligations, biosimilar disputes — require mandatory specialist involvement?
- What scenarios touching open-source license obligations require mandatory escalation — e.g., copyleft license uses, dual-license obligations, redistribution events?
- Who is the designated escalation contact for IP matters above the group's thresholds, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should IP work product default to formal legal-opinion format, triage / first-pass analysis format, or both layered?
- What is the group's tiered framework for opinions — full reasoned opinion, short reasoned opinion, no-opinion triage? Where do clearance triages fit?
- Are there house style rules for marking preliminary findings, risk indicators, or open questions in IP work product?
- Does the group produce portfolio dashboards or status reports, and if so, in what format?
- Are there particular deliverable types — invention disclosures, opinion drafts, cease-and-desist responses — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative source of truth for IP strategy, clearance criteria, and opinion templates?
- Is there a written open-source policy or compliance program, and where is it stored?
- Does the group maintain a trademark watch program or a docketing system, and what document governs its operation?
- Is there a trade-secret protection policy or program documentation the group references?
- Are there sector-specific reference materials (FDA Orange Book, biosimilars patent dance procedures, semiconductor licensing standards) the group treats as authoritative?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What clearance threshold triggers a full opinion vs. a triage assessment? How does the group calibrate that threshold?
- What is the group's default position on open-source license usage — permissive vs. copyleft, redistribution thresholds, attribution / source-disclosure obligations?
- What is the group's default trademark-watch posture — proactive opposition, defensive watch only, hybrid?
- What is the group's default trade-secret marking, access-control, and departure-process posture?
- Are there technology areas where the group will not opine without specific specialist review, regardless of urgency?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review become mandatory — any clearance triage that escalates, any opinion, any FTO assessment, any cease-and-desist response, any DMCA notice or counter-notice?
- Are there matter types for which attorney review is always required regardless of size — for example, any opinion, any matter touching SEP/F-RAND, any matter touching a registered IP right?
- What is the designated reviewer's role — registered patent attorney, supervising counsel, practice group lead, outside counsel?
- What is the expected turnaround for clearance triage vs. full opinion review, and how are urgent reviews handled?
- Is there a formal sign-off step before an opinion is delivered, a clearance is communicated, or a response is sent externally?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — for example, that a mark is clear, that a patent claim is anticipated, that an FTO opinion remains current, that an open-source license obligation has been satisfied?
- Are there scenarios where an agent must stop and escalate rather than reason through independently — SEP licensing, biosimilars, willfulness questions, ITC posture?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — opinion-of-counsel work, validity opinions, willfulness opinions?
- Are there prior incidents — adverse opinions, sanctions, regulator inquiries — that should be encoded as explicit prohibitions for agents working on IP matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/ip.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/ip.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdiction coverage — including PCT, Madrid, EUTM, Hague, and any sector-specific regimes — is accurately recorded.
- [ ] Foreign-counsel allocation by jurisdiction has been confirmed.
- [ ] Opinion-tier framework (full opinion / short opinion / triage / no-opinion) is consistent with the group's current malpractice and engagement-letter posture `[ATTORNEY TO CONFIRM]`.
- [ ] Open-source compliance program references are current `[Verify current law]`.
- [ ] Bar-date and priority-filing escalation triggers are accurately captured and all related deadlines are marked `[deadline verification required]`.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/ip.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
