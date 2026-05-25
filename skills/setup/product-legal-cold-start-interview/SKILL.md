---
name: Product Legal Cold-Start Interview
description: "Use when a product-legal practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to a product-legal attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled product-legal practice profile draft for attorney review"
related_skills:
  - skills/product-legal/launch-review/SKILL.md
  - skills/product-legal/terms-of-service-review/SKILL.md
  - skills/product-legal/marketing-claims-review/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - product-legal
---

# Product Legal Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a product-legal practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/product-legal.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/product-legal.md` for the first time.
- A product-legal practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the product-legal area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the product-legal practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live product-legal matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/product-legal.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific product-legal matter (use the appropriate matter-level skill for that task).

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
- In which jurisdictions are the client's products available — US federal (FTC), US state (state AGs), EU, UK, Canada, others?
- Does the group regularly engage with sector-specific consumer-protection regimes (children's privacy / COPPA, health-related claims / FDA, financial / CFPB, age-restricted products)?
- Are there jurisdictions where the group's clients face heightened consumer-protection enforcement (e.g., California, NY, FTC priority areas)?
- Are there jurisdictions or product categories the group treats as out of scope, requiring specialist outside counsel?
- Does the group track foreign consumer-protection regimes (EU Digital Services Act, UK CMA, Australia ACL) that affect US clients?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Who are the primary clients of the product-legal group — product teams, engineering, design, marketing, executives, external clients?
- What types of product-legal matters does the group handle most frequently — feature reviews, ToS / privacy-policy reviews, advertising-claim reviews, pricing-page reviews, subscription / cancellation flows, dark-pattern reviews?
- How is the team structured, and how does it coordinate with privacy counsel, IP counsel, and external regulatory counsel?
- Are there product categories (consumer financial products, health products, children's products, age-restricted products) that require special handling?
- How does the group engage with the client's product-launch process, design-review process, or marketing-review process?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which feature characteristics automatically require escalation — child-directed features, biometric features, financial features, health-related claims, dark-pattern indicators, UDAAP / FTC Act section 5 risk?
- Which advertising claims automatically require escalation — health, financial, environmental / green claims, sponsorship / influencer disclosures, comparative claims, free-trial-to-paid conversions?
- What pricing-page or subscription scenarios trigger escalation — auto-renewal without prominent disclosure, retention dark patterns, refund-policy disclosure, drip pricing?
- When does a UX flow (cancellation, account deletion, consent, opt-out) require immediate specialist review?
- Who is the designated escalation contact for product-legal matters, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should product-legal work product default to feature-launch-checklist format, redline format, risk-matrix format, or memo format?
- What level of detail does the practice group expect — executive summary, full UX-element-by-element review, both layered?
- Are there house style rules for risk ratings, mitigation recommendations, or open-items lists in product-legal work product?
- Does the group produce go / no-go recommendations or mitigation lists in a standard format?
- Are there particular deliverable types — feature-launch checklists, ToS-update memos, advertising-claim memos — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative feature-launch playbook, and where is it stored?
- Is there an advertising-substantiation requirements reference, and how is it kept current?
- What document governs the group's subscription / UDAAP standards reference?
- Are there dark-pattern criteria or design-review checklists the group treats as authoritative?
- Does the group maintain a current-FTC-priority reference and a state-AG enforcement-priority reference?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default dark-pattern posture — categories the group always flags, categories the group escalates?
- What is the group's default consent posture — opt-in, opt-out, layered, just-in-time?
- What is the group's default subscription / auto-renewal disclosure framework?
- What is the group's default UDAAP / FTC Act section 5 risk threshold?
- What is the group's default approach to advertising claims, substantiation, and disclosure?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review of product-legal work product become mandatory — design-review stage, pre-launch stage, post-launch monitoring, incident response?
- Are there work-product types for which attorney review is always required regardless of stage — any feature launch above a complexity threshold, any ToS update, any advertising claim above a risk threshold, any pricing-page change?
- What is the designated reviewer's role — handling attorney, supervising attorney, product partner, general counsel?
- What is the expected turnaround for product-legal review, and how are urgent reviews (launch-day issues, FTC inquiries, viral product issues) handled?
- Is there a formal sign-off step before any feature launch, any ToS update, or any advertising-campaign launch?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — that a claim is substantiated, that consent is informed, that a disclosure is sufficient, that a feature is FTC-compliant, that a dark pattern is acceptable?
- Are there product-legal risks — UDAAP, dark patterns, deceptive advertising, child-protection, fair lending — where an agent must stop and escalate rather than reason through independently?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — FTC inquiries, state-AG inquiries, viral product incidents, child-protection matters?
- Are there prior incidents — adverse FTC enforcement, state-AG settlements, consumer-complaint pattern findings — that should be encoded as explicit prohibitions for agents working on product-legal matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/product-legal.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/product-legal.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdiction coverage — including FTC, state AGs, and foreign consumer-protection regimes — is accurately recorded `[Verify current law]`.
- [ ] Dark-pattern criteria and UDAAP-risk threshold reflect current FTC and state-AG enforcement guidance.
- [ ] Subscription / auto-renewal disclosure framework reflects current state-by-state requirements `[verify jurisdiction]`.
- [ ] Advertising substantiation requirements references are current.
- [ ] Feature-launch checklist references are current and tied to the client's product process.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/product-legal.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
