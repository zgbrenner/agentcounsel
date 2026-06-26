---
name: Financial Crime / AML Cold-Start Interview
description: "Use when a financial-crime practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions."
practice_area: setup
task_type: interview
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "Access to a financial-crime attorney or authorized designee"
  - "The practice group's jurisdictions and client context"
  - "Standard positions, escalation thresholds, and review requirements"
outputs:
  - "Filled financial-crime practice profile draft for attorney review"
related_skills:
  - skills/financial-crime/kyc-onboarding-review/SKILL.md
  - skills/financial-crime/sanctions-screening-review/SKILL.md
  - skills/regulatory/compliance-gap-matrix/SKILL.md
tags:
  - setup
  - cold-start
  - practice-profile
  - configuration
  - financial-crime
---

# Financial Crime / AML Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a financial-crime practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/financial-crime.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/financial-crime.md` for the first time.
- A financial-crime practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the financial-crime area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the financial-crime practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, templates, source-of-truth documents, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live financial-crime matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/financial-crime.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to handle a specific financial-crime matter (use the appropriate matter-level skill for that task).

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
- In which jurisdictions does the group support KYC, customer due diligence, and sanctions / PEP / adverse-media screening work most frequently?
- Which regulated entities does the group work with, and which supervisory regimes govern their AML programs?
- Are there jurisdictions, list sources, or sanctions regimes the group treats as in scope for screening, and how is that coverage tracked?
- Are there cross-border relationships — foreign UBOs, offshore structures, non-resident applicants — that the group routinely encounters and must account for?
- Are there jurisdictions or sanctions regimes the group treats as out of scope entirely, requiring escalation or specialist outside counsel?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Does the group support primarily a financial institution's compliance function, a corporate client's onboarding team, outside counsel, or a mix? Confirm the default posture.
- What types of financial-crime matters does the group handle most frequently — onboarding KYC, periodic refresh, beneficial-ownership analysis, sanctions / PEP / adverse-media alert adjudication, or others?
- How is the team structured — compliance officers, onboarding analysts, supervising attorneys, paralegals, non-attorney professionals whose work must be supervised?
- Are there applicant categories — high-risk customers, PEPs, complex ownership structures, correspondent relationships — that require enhanced due diligence or additional sign-off?
- How does the group coordinate with the firm's compliance function, MLRO or BSA officer, and any external screening providers?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- Which KYC findings automatically require escalation — opaque or undisclosed beneficial ownership, missing source-of-funds evidence, expired or unverifiable identity documents, high-risk-jurisdiction exposure?
- Which screening outcomes require mandatory escalation — a possible or likely true sanctions match, a confirmed PEP designation, significant adverse media — regardless of the screening context?
- Is there a customer risk-rating outcome (for example, a high rating, or a recommendation to decline or apply enhanced due diligence) that always triggers escalation, and to whom?
- What is the escalation path when a suspicious-activity concern or potential reporting obligation surfaces during a review?
- Who is the designated escalation contact for financial-crime matters — the MLRO, BSA officer, or supervising attorney — and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should financial-crime work product default to a structured KYC onboarding file, a screening / alert-adjudication review, a compliance-facing summary, or several layered?
- What format does the group use for the customer risk rating and disposition recommendation — factor table, narrative, or both?
- Are there house style rules for confidence classifications, risk ratings, escalation flags, or open questions in financial-crime work product?
- Does the group produce document-inventory tables, beneficial-ownership charts, or alert-disposition tables, and if so, in what format?
- Are there particular deliverable types — onboarding files, screening reviews, escalation packets — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What is the group's authoritative KYC/AML rules grid or CDD policy, including the required-document matrix and risk-rating methodology, and where is it stored?
- Is there a separately maintained high-risk-jurisdiction list, and how is it kept current?
- What document governs the group's screening or alert-disposition policy, including match thresholds and false-positive criteria?
- Does the group maintain a beneficial-ownership / control verification standard, and is it tied to specific applicant types?
- Are there enhanced-due-diligence procedures or escalation playbooks the group treats as authoritative, and is any of them under revision or pending update?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default customer due diligence posture by applicant type, and what triggers a step up to enhanced due diligence?
- What is the group's default beneficial-ownership threshold and control standard for identifying UBOs and controllers?
- What is the group's default source-of-funds / source-of-wealth evidence expectation across risk levels?
- What is the group's default approach to disposition recommendations — clear, request documents, escalate to enhanced due diligence, or recommend decline — and what drives each?
- What is the group's default posture on screening: which list sources are screened, how possible matches are handled, and how false positives are documented?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage of a financial-crime matter does attorney or compliance review of work product become mandatory — intake, before any risk rating, before any disposition recommendation, before any escalation, or at other defined stages?
- Are there work-product types for which review is always required regardless of matter size — for example, any sanctions match, any high-risk rating, any recommendation to decline, any enhanced-due-diligence file?
- What is the designated reviewer's role — handling attorney, supervising attorney, MLRO or BSA officer, compliance lead?
- What is the expected turnaround for standard onboarding or screening review, and how are urgent reviews (potential sanctions exposure, time-sensitive onboarding) handled?
- Is there a formal sign-off step — required signature, approval, or logged confirmation — before a customer is onboarded, an alert is dispositioned, or an escalation packet is transmitted?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts, postures, or conclusions agents must never assume without explicit confirmation — that an applicant is cleared, that a risk rating is low, that beneficial ownership is complete, that a screening alert is a false positive, that source of funds is adequately evidenced?
- Are there scenarios — a possible sanctions match, a confirmed PEP, a suspicious-activity concern — where an agent must stop and escalate rather than reason through independently?
- Are there matter types or applicant populations (high-risk customers, complex ownership structures, correspondent relationships) where agents must never proceed beyond intake without direct compliance or attorney involvement?
- Are there prior incidents, regulator findings, or lessons learned that should be encoded as explicit prohibitions for agents working on financial-crime matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/financial-crime.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/financial-crime.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdiction and sanctions-regime coverage for KYC and screening work is accurately recorded `[verify jurisdiction]`.
- [ ] KYC/AML rules grid, CDD policy, and high-risk-jurisdiction list references are current and version-controlled `[Verify current law]`.
- [ ] Beneficial-ownership thresholds and the customer risk-rating methodology reflect the group's current considered posture, not a provisional one.
- [ ] Screening / alert-disposition thresholds and false-positive criteria reflect the firm's current policy, and every possible or likely true sanctions match is routed to compliance and counsel.
- [ ] Any reporting, response, or refresh dates surfaced during a review are marked `[deadline verification required]` and are computed by the attorney or compliance function, not by an agent.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/financial-crime.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
