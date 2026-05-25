---
name: Bankruptcy and Restructuring Cold-Start Interview
description: "Use when a bankruptcy and restructuring practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to a bankruptcy and restructuring attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled bankruptcy and restructuring practice profile draft for attorney review"
related_skills:
  - skills/bankruptcy-restructuring/bankruptcy-matter-intake/SKILL.md
  - skills/bankruptcy-restructuring/bankruptcy-deadline-tracker-intake/SKILL.md
  - skills/bankruptcy-restructuring/creditor-claim-intake/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - bankruptcy-restructuring
---

# Bankruptcy and Restructuring Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a bankruptcy and restructuring practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/bankruptcy-restructuring.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/bankruptcy-restructuring.md` for the first time.
- A bankruptcy and restructuring practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the bankruptcy and restructuring area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the bankruptcy and restructuring practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live bankruptcy and restructuring matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/bankruptcy-restructuring.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific bankruptcy and restructuring matter (use the appropriate matter-level skill for that task).

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
- In which bankruptcy courts (federal districts, divisions) does the group practice most frequently?
- Does the group regularly engage with cross-border restructurings (Chapter 15, CCAA, UK schemes, others), and which regimes drive most of that work?
- Does the group handle state-law restructuring tools — assignments for the benefit of creditors, receiverships — and in which jurisdictions?
- Are there sector-specific bankruptcy regimes (healthcare, financial institution, municipal Chapter 9) the group regularly engages with?
- Are there jurisdictions or sectors the group treats as out of scope, requiring specialist outside counsel?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Does the group represent primarily debtors, creditors (secured / unsecured / trade / equity / bondholder), committees, plan sponsors, or a mix?
- What types of bankruptcy and restructuring matters does the group handle most frequently — pre-petition advisory, Chapter 11 / 7 / 15 cases, out-of-court restructurings, distressed-asset acquisitions, plan negotiation, litigation within bankruptcy?
- How is the team structured — partners, associates, financial-restructuring specialists, claims-handling paralegals?
- How does the group coordinate with financial advisors, investment bankers, claims agents, and trustees?
- Are there client categories — first-lien holders, DIP lenders, equity sponsors, indenture trustees — that require special handling?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which matters automatically require escalation — petition filing, first-day motions, DIP / cash-collateral, plan negotiation, section 363 sale, preference / fraudulent transfer, substantive consolidation, cross-border filing?
- Are there transaction-value or claim-amount thresholds that trigger escalation?
- When does an avoidance-action analysis (preference, fraudulent transfer, equitable subordination, recharacterization) require partner-level involvement?
- Which engagement types — committee representation, professional retention, fee-application work — require attorney review regardless of size?
- Who is the designated escalation contact for bankruptcy matters, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should bankruptcy work product default to memo format, deadline-tracker format, claim-analysis format, or pleading-draft format?
- What level of detail does the practice group expect — executive summary, full citation-supported analysis, both layered?
- Are there house style rules for citation format, deadline flagging, or claim categorization in bankruptcy work product?
- Does the group produce closing-checklist drafts, first-day-motion summaries, or claim-analysis dashboards in standard formats?
- Are there particular deliverable types — first-day declarations, disclosure statements, plans of reorganization — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative bankruptcy-precedent library (first-day motions, plans, disclosure statements), and where is it stored?
- Is there a deadline-tracker spreadsheet or system for bankruptcy cases, and how is it kept current?
- What document governs the group's claim-analysis framework — categories, evidentiary standards, treatment recommendations?
- Are there sample DIP / cash-collateral / 363-sale motion libraries the group treats as authoritative?
- Does the group maintain a court-specific reference (local rules, judge preferences, district customs) for the bankruptcy courts where it appears?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default cash-collateral / DIP posture — common protections demanded, common objections raised?
- What is the group's default DIP-lender-protection framework — adequate protection, replacement liens, super-priority, carve-outs?
- What is the group's default preference-defense framework — analyzing ordinary-course-of-business, new value, and contemporaneous-exchange defenses?
- What is the group's default substantive-consolidation posture?
- What is the group's default approach to plan-feasibility analysis and confirmation?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review of bankruptcy work product become mandatory — pre-petition advisory, filing stage, first-day motion stage, plan / disclosure-statement stage, distribution stage?
- Are there work-product types for which attorney review is always required regardless of size — any petition, any first-day motion, any plan, any preference complaint, any 363 motion?
- What is the designated reviewer's role — handling attorney, supervising bankruptcy partner, specialty partner for cross-border or sector matters?
- What is the expected turnaround for standard bankruptcy review, and how are urgent reviews (first-day filings, emergency motions) handled?
- Is there a formal sign-off step before any court filing or distribution event?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — that a deadline applies, that a claim is valid, that a transfer is non-preferential, that automatic stay protects, that an order has been entered?
- Are there bankruptcy-specific risks — fraudulent-transfer, preference, equitable subordination, judicial-estoppel, stay-violation, fee-objection — where an agent must stop and escalate rather than reason through independently?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — committee work, cross-border filings, sector-specific bankruptcies (healthcare, financial institution)?
- Are there prior incidents — adverse rulings, sanctions, professional-conduct findings — that should be encoded as explicit prohibitions for agents working on bankruptcy matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/bankruptcy-restructuring.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/bankruptcy-restructuring.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Court coverage and judge-specific local-rule references are accurately recorded.
- [ ] Deadline-tracker reference is current and maintenance owner is named — every deadline in a related deliverable must be marked `[deadline verification required]`.
- [ ] Cash-collateral / DIP / preference-defense defaults reflect the group's current considered practice.
- [ ] Cross-border restructuring posture is current `[Verify current law]`.
- [ ] Conflicts and retention frameworks reflect applicable professional-conduct rules `[ATTORNEY TO CONFIRM]`.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/bankruptcy-restructuring.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
