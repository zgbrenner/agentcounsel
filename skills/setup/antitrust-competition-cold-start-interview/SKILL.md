---
name: Antitrust / Competition Cold-Start Interview
description: "Use when an antitrust / competition practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to an antitrust / competition attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled antitrust / competition practice profile draft for attorney review"
related_skills:
  - skills/antitrust-competition/antitrust-risk-intake/SKILL.md
  - skills/antitrust-competition/merger-antitrust-issue-spotter/SKILL.md
  - skills/antitrust-competition/antitrust-compliance-policy-review/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - antitrust-competition
---

# Antitrust / Competition Cold-Start Interview

## Purpose

Conduct a structured, staged interview with an antitrust / competition practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/antitrust-competition.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/antitrust-competition.md` for the first time.
- An antitrust / competition practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the antitrust / competition area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the antitrust / competition practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live antitrust / competition matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/antitrust-competition.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific antitrust / competition matter (use the appropriate matter-level skill for that task).

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
- In which competition regimes does the group regularly practice — US (DOJ, FTC, state AGs), EU, UK CMA, China SAMR, Brazil CADE, India CCI, others?
- Does the group regularly handle multi-jurisdictional merger-clearance filings, and how is that allocation across jurisdictions tracked?
- Are there sectors — financial services, agriculture, communications, healthcare, technology platforms — the group regularly engages with that have specialized competition frameworks?
- Are there jurisdictions the group treats as out of scope, requiring specialist outside counsel?
- Does the group maintain jurisdiction-by-jurisdiction reference materials on merger thresholds, dominance frameworks, and enforcement priorities?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Does the group represent primarily corporate clients (counseling), M&A clients (clearance), investigation targets (defense), private-litigation parties, or a mix?
- What types of competition matters does the group handle most frequently — clearance, compliance counseling, investigation defense, private litigation, leniency / immunity work?
- How is the team structured — competition partners, associates, economists embedded or external, support staff?
- How does the group coordinate with foreign competition counsel, economic experts, and sector specialists?
- Are there client categories — platform companies, holders of dominant positions, market participants under structural orders — that require special handling?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which matters automatically require escalation — investigation initiation, dawn-raid response, cartel suspicion, market-power / dominance analysis, multi-jurisdictional filing, gun-jumping concern?
- Are there transaction-size thresholds (filing requirement triggers) that automatically require partner-level review?
- When does an algorithm-related concern, a trade-association concern, or an information-exchange concern require immediate specialist involvement?
- Which engagement types — leniency application, voluntary disclosure, consent-decree negotiation — require partner-level review regardless of size?
- Who is the designated escalation contact for competition matters, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should competition work product default to memo format, issue-spotting matrix format, clearance-strategy format, or compliance-checklist format?
- What level of detail does the practice group expect — executive summary, full economic-analysis-supported memo, both layered?
- Are there house style rules for risk ratings, jurisdiction-by-jurisdiction breakdowns, or open-items lists in competition work product?
- Does the group produce clearance-strategy decks or compliance-training materials in standard formats?
- Are there particular deliverable types — clean-team agreements, gun-jumping protocols, leniency applications — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative clearance playbook, and where is it stored?
- Is there a clean-team agreement template, and how is it kept current?
- What document governs the group's trade-association attendance protocol?
- Are there compliance-training materials or policy-template libraries the group treats as authoritative?
- Does the group maintain a dawn-raid protocol with counsel contacts, evidence-preservation rules, and employee guidance?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default clearance-strategy posture — pre-filing engagement, formal filing strategy, second-request preparedness?
- What is the group's default leniency / immunity framework — when warranted, how scoped?
- What is the group's default clean-team membership and information-segregation posture for diligence?
- What is the group's default position on algorithm and AI-pricing matters?
- What is the group's default trade-association attendance protocol and information-sharing framework?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review of competition work product become mandatory — clearance-strategy stage, filing stage, response-to-second-request stage, settlement / consent-decree stage?
- Are there work-product types for which attorney review is always required regardless of size — any HSR filing, any clearance opinion, any clean-team setup, any leniency application, any agency response?
- What is the designated reviewer's role — handling attorney, supervising competition partner, multi-jurisdictional lead?
- What is the expected turnaround for clearance-filing review, and how are urgent reviews (second-request responses, dawn-raid response, agency deadlines) handled?
- Is there a formal sign-off step before any agency filing, leniency application, or consent-decree negotiation?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — that conduct is not a cartel, that an agreement is rule-of-reason, that a market definition is settled, that a clearance is granted, that a safe harbor applies?
- Are there competition-specific risks — cartel involvement, dawn-raid posture, second-request response — where an agent must stop and escalate rather than reason through independently?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — investigation defense, leniency applications, dawn-raid response, criminal antitrust referrals?
- Are there prior incidents — adverse decisions, structural remedies, leniency declinations — that should be encoded as explicit prohibitions for agents working on competition matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/antitrust-competition.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/antitrust-competition.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdiction coverage — including DOJ, FTC, EU, UK, China SAMR, and other regimes — is accurately recorded.
- [ ] Filing-threshold framework and clearance-strategy defaults reflect current law `[Verify current law]`.
- [ ] Clean-team agreement template and gun-jumping protocol references are current.
- [ ] Dawn-raid protocol references are current and counsel-contact list is up to date.
- [ ] Filing deadlines and waiting-period clocks are marked `[deadline verification required]` in any related deliverable.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/antitrust-competition.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
