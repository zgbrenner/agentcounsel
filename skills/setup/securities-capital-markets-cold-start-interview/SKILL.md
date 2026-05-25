---
name: Securities and Capital Markets Cold-Start Interview
description: "Use when a securities and capital markets practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to a securities and capital markets attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled securities and capital markets practice profile draft for attorney review"
related_skills:
  - skills/securities-capital-markets/public-company-reporting-calendar-intake/SKILL.md
  - skills/securities-capital-markets/offering-document-disclosure-review/SKILL.md
  - skills/securities-capital-markets/comfort-backup-request-tracker/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - securities-capital-markets
---

# Securities and Capital Markets Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a securities and capital markets practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/securities-capital-markets.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/securities-capital-markets.md` for the first time.
- A securities and capital markets practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the securities and capital markets area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the securities and capital markets practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live securities and capital markets matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/securities-capital-markets.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific securities and capital markets matter (use the appropriate matter-level skill for that task).

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
- In which jurisdictions does the group advise on securities matters — US (SEC, FINRA, state blue-sky), UK (LSE), Canada (TSX), Hong Kong, Singapore, others?
- Does the group regularly engage with foreign listing exchanges or ADR programs?
- Are there sector-specific securities regimes (banking, insurance, energy) the group regularly engages with?
- Does the group regularly engage with private-placement regimes across multiple jurisdictions?
- Are there jurisdictions or sectors the group treats as out of scope, requiring specialist outside counsel?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Does the group represent primarily issuers, underwriters, placement agents, investors, or a mix?
- What types of securities matters does the group handle most frequently — public-company reporting, capital raises (IPO, follow-on, debt), M&A securities-side, private placements, advisory?
- How is the team structured — partners, associates, capital-markets specialists, public-company-reporting specialists?
- How does the group coordinate with auditors, financial printers, transfer agents, and stock exchanges?
- Are there client categories — emerging-growth companies, smaller reporting companies, foreign private issuers, sponsors with multiple portfolio companies — that require special handling?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which matters automatically require escalation — material non-disclosure, Reg FD risk, insider-trading risk, Reg S-X audit issue, non-GAAP measure compliance, SEC inquiry, SEC investigation?
- Are there transaction-size or registration-status thresholds that trigger escalation?
- When does a materiality question, a disclosure question, or a Reg-FD question require immediate review?
- Which deliverables (registration statement, periodic report, press release, Form 8-K) require partner-level review regardless of stage?
- Who is the designated escalation contact for securities matters, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should securities work product default to memo format, disclosure-issue list format, redline format, or closing-checklist format?
- What level of detail does the practice group expect — executive summary, full citation-supported analysis, both layered?
- Are there house style rules for citation format, materiality flags, or open-items lists in securities work product?
- Does the group produce comfort-letter backup requests, closing-checklist drafts, or D&O questionnaire summaries in standard formats?
- Are there particular deliverable types — registration statements, periodic reports, press releases — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative library of registration-statement and periodic-report templates, and where is it stored?
- Is there a comfort-letter backup or due-diligence template, and how is it kept current?
- What document governs the group's closing-checklist template for offerings?
- Are there D&O questionnaires, officer-and-director questionnaire templates, or other diligence instruments the group treats as authoritative?
- Does the group maintain a sector-specific reference for offering disclosures, MD&A, or non-GAAP measure compliance?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default materiality threshold framework, and how is it documented?
- What is the group's default Reg FD posture — who has authority to speak with analysts, how is selective disclosure prevented, what are the contemporaneous-public-disclosure rules?
- What is the group's default selective-disclosure protocol?
- What is the group's default non-GAAP measure usage and reconciliation framework?
- What is the group's default approach to insider-trading windows, blackout periods, and 10b5-1 plans?
- What is the group's default approach to forward-looking-statement safe-harbor framing?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage does attorney review of securities work product become mandatory — drafting stage, financial-printer proof stage, filing stage, post-filing amendment stage?
- Are there work-product types for which attorney review is always required regardless of size — any prospectus, any periodic report, any earnings release, any Form 8-K, any private-placement memo?
- What is the designated reviewer's role — handling attorney, supervising securities partner, disclosure committee chair, general counsel?
- What is the expected turnaround for periodic-report review, and how are urgent reviews (8-K events, earnings releases, market-moving developments) handled?
- Is there a formal sign-off step — disclosure committee, officer certifications, attorney certification — before any filing or release?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts agents must never assume without explicit confirmation — that a transaction is exempt from registration, that materiality is settled, that selective disclosure does not occur, that audit comfort is reliable, that a press release is consistent with prior public disclosure?
- Are there securities-specific risks — insider trading, Reg FD violation, material non-disclosure, ITC posture, foreign-issuer disclosure — where an agent must stop and escalate rather than reason through independently?
- Are there matter types where agents must never proceed beyond intake without direct attorney involvement — any registration statement, any 8-K event, any private-placement memo, any securities-fraud claim?
- Are there prior incidents — SEC inquiries, comment letters, restatements — that should be encoded as explicit prohibitions for agents working on securities matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/securities-capital-markets.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/securities-capital-markets.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdiction coverage — including foreign exchanges and ADR programs — is accurately recorded.
- [ ] Reporting calendar and filing deadlines are accurately captured and marked `[deadline verification required]` in any related deliverable.
- [ ] Disclosure committee structure and Reg FD protocol reflect the group's current considered practice `[ATTORNEY TO CONFIRM]`.
- [ ] Materiality, non-GAAP, and forward-looking-statement defaults reflect current SEC guidance `[Verify current law]`.
- [ ] Insider-trading windows, blackout periods, and 10b5-1 plan defaults are current.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/securities-capital-markets.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
