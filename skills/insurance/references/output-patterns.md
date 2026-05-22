> Shared reference material supporting the AgentCounsel Insurance skills, used to help produce draft legal work product for attorney review — not legal advice.

# Insurance Output Patterns

This file defines the reusable output structures the Insurance skills produce,
so a policy summary, an issue matrix, a chronology, or a tracker looks and
behaves the same across every skill in `skills/insurance/`. It is a consistency
reference, not a skill — each skill's own `SKILL.md` remains authoritative for
what that skill does.

Three rules apply to every pattern below:

- **Every extracted or summarized term cites its source** — the document and
  the page, form number, endorsement number, section, paragraph, or claim
  document, as written. A cell with no source is not complete.
- **Gaps are marked, never filled.** Where a value is absent or unclear, the
  cell reads `not found`, `not provided`, `unknown`, or `ambiguous` — never a
  guess. Dates are recorded as the document states them and flagged
  `[deadline verification required]`; they are never computed.
- **No final conclusions.** These tables organize facts and questions. They do
  not state that coverage exists, that a duty to defend or indemnify is owed,
  that bad faith occurred, that a tender is valid, that additional insured
  status exists, or that a recovery right exists. They do not approve or deny
  claims, calculate reserves, value claims, or recommend carriers.

All output is draft work product for attorney review.

---

## 1. Insurance Policy Summary Table

Used by `insurance-policy-summary`. Pair the key terms table with a coverage
parts table, an exclusions/conditions inventory, an endorsements table, and a
missing/ambiguous items list. The skill never concludes coverage exists.

| Column | Content |
|---|---|
| Term | The policy term — named insured, policy period, limit, deductible/SIR, etc. |
| Value as written | The value exactly as the policy states it |
| Source | Declarations page, form number, endorsement number, or section |

Coverage parts table: coverage part | insuring agreement (plain language) | limits/sublimits | deductible or SIR | granting form | source. Endorsements table: endorsement number | effect (adds/deletes/modifies) | form amended | source.

---

## 2. Coverage Issue Matrix

Used by `coverage-issue-spotter` and, in lighter form, by
`coverage-position-outline`. Every issue is an open question for counsel — never
a decided outcome.

| Column | Content |
|---|---|
| # | Issue number |
| Issue | The coverage question |
| Coverage layer | Insuring agreement, policy period, notice, exclusions, endorsements, definitions, defense/indemnity, additional insured, allocation, other insurance, limits/SIR, or posture |
| Policy provision (source) | The provision in play, with its source |
| Claim fact (source) | The claim fact that raises it, with its source |
| Why it is an open question | What remains unresolved for counsel |
| Attorney follow-up | The question routed to counsel |

Pair with a source-cited policy/claim fact table, a missing-facts list, and a document request list.

---

## 3. Claims Chronology Table

Used by `claims-chronology-builder`. Built only from provided documents;
deadlines are never computed and timeliness is never judged.

| Column | Content |
|---|---|
| Date | The date as written, or `[date unknown]` |
| Event | The event in plain language |
| Source | The document and location |
| Actor | Who did it |
| Significance | A neutral note on the workflow step — never a timeliness or adequacy judgment |
| Follow-up | Document or date needed |

Pair with a missing/ambiguous facts list (undated events, conflicting dates) and a follow-up items list.

---

## 4. Reservation of Rights Review Table

Used by `reservation-of-rights-review`. The skill never concludes the
reservation is legally sufficient, effective, or timely.

| Column | Content |
|---|---|
| # | Issue number |
| Issue | The issue raised by the letter |
| Letter reference | The paragraph or section of the letter |
| Description | What the letter says, in plain language |
| Why it matters | The reason an attorney would examine it |
| Attorney follow-up | The question routed to counsel |

Pair with a provision-reference table (letter reference | provision cited | policy location | match status: matches / not found / ambiguous), an ambiguity/consistency list, and a missing-facts list.

---

## 5. Tender Completeness Checklist

Used by `tender-letter-review`. The skill never concludes the tender is timely,
valid, or sufficient.

| Column | Content |
|---|---|
| Element | The tender element — recipient, asserted basis, claim identification, duties tendered, additional insured basis, supporting documents, etc. |
| Status | Present / not found / ambiguous |
| Source | The letter, policy provision, or contract clause |
| Note | What is missing or unclear |

Pair with a missing-documents list, a risk-flags table, and direction-only proposed attorney-review revisions.

---

## 6. Coverage Position Outline

Used by `coverage-position-outline`. The deliverable is an outline only — never
a coverage opinion, denial, or recommendation. Candidate grants and exclusions
are framed as questions.

| Section | Content |
|---|---|
| Facts | Source-cited material facts; disputed and missing facts flagged |
| Policy provisions | Source-cited insuring agreements, definitions, exclusions, endorsements, conditions in play |
| Potential coverage grants | Candidate | insuring-agreement provision (source) | fact in play (source) | question for the attorney |
| Potentially applicable exclusions/endorsements | Candidate | provision (source) | fact in play (source) | question for the attorney |
| Conditions | Condition | provision (source) | claim fact (source) | open question |
| Posture | Reservation/denial/defense posture as it stands, with no recommendation |
| Open issues | Open factual and legal issues, and recommended questions for counsel |

---

## 7. Bad Faith Risk Triage Matrix

Used by `bad-faith-risk-triage`. Every theme is framed neutrally as a potential
risk to evaluate — never an accusation and never an exoneration. The skill
never concludes bad faith occurred or did not occur.

| Column | Content |
|---|---|
| Theme | The claim-handling risk theme |
| Factual trigger | The fact or gap that raises it |
| Source | The claim documents and gaps |
| Why an attorney would examine it | The reason it warrants review |
| Jurisdiction-specific question for counsel | The standard the attorney must supply and apply |

Pair with a chronology-gaps list, a communication-issues list, and a missing-documents list.

---

## 8. Certificate of Insurance Comparison Table

Used by `certificate-of-insurance-review`. A certificate is evidence only of
what it states; the skill never treats it as proof of coverage.

| Column | Content |
|---|---|
| Requirement (or expected element) | The contract requirement or expected element |
| Certificate/endorsement shows | What the certificate or endorsement states |
| Source | The certificate field, endorsement number, or contract clause |
| Match status | Matches / mismatch / not found / ambiguous |
| Note | Whether an endorsement form is attached versus merely box-checked |

Pair with a missing-endorsement list, a mismatch list, and the certificate's own disclaimer and its limitations.

---

## 9. Contract Insurance Requirements Table

Used by `insurance-requirements-contract-review`. The skill never concludes the
requirements are adequate, sufficient, or enforceable.

| Column | Content |
|---|---|
| Requirement | The required policy, limit, endorsement, or administrative item |
| Detail as written | The requirement exactly as the contract states it |
| Responsible party | The party required to carry or arrange it |
| Source clause | The contract section or clause |

Pair with an indemnity and risk-allocation section, a role-aware risk matrix (requirement/gap | source | concern for the side | risk | attorney follow-up), a missing-provisions list, and direction-only negotiation points.

---

## 10. Subrogation / Recovery Tracker

Used by `subrogation-recovery-tracker`. The skill never determines whether a
recovery right exists, its priority, or its value.

| Column | Content |
|---|---|
| Recovery theory | Subrogation, reimbursement, salvage, contribution, or indemnity |
| Responsible party | The potentially responsible party |
| Supporting facts (source) | The loss and payment facts, with sources |
| Contract/policy basis (source) | The indemnity or subrogation provision, with source |
| Open question for the attorney | The question routed to counsel |

Pair with a source table, an evidence-preservation section, a notices/litigation-status section, and a missing-facts and document request list. User-supplied limitations and notice dates are flagged `[deadline verification required]`.

---

## 11. Renewal / Placement Diligence Checklist

Used by `policy-renewal-placement-diligence-checklist`. The skill recommends no
carrier, binds no coverage, quotes no pricing, and reaches no adequacy or
compliance conclusion.

| Column | Content |
|---|---|
| # | Item number |
| Workstream | Expiring program, claims history, material changes, new operations/jurisdictions, contractual coverage obligations, regulatory issues, or coverage gaps |
| Diligence item | The item to review or confirm |
| Status | Open / In progress / Complete |
| Source | The provided document, where the item rests on one |

Pair with a document request list, coverage-gap questions, and attorney and broker verification items.

---

## 12. Insurer / Insured Communications Review Table

Used by `insurer-insured-communications-review`. The skill never approves a
communication for sending; suggested edits are draft-only.

| Column | Content |
|---|---|
| Issue | The communication issue |
| Communication reference | The letter, email, or note and its location |
| Description | What the communication says, in plain language |
| Category | Clarity, consistency, tone, posture, privilege, claim-handling, information-request, or escalation |
| Why it matters | The reason an attorney would examine it |
| Attorney follow-up | The question routed to counsel |

Pair with a source table, direction-only suggested attorney-review edits, a missing-facts list, and escalation flags.

---

## Using these patterns

A skill may extend a pattern with extra columns where its workflow needs them,
but should not drop the source column or the gap-marking convention. When a
maintainer adds a new Insurance skill, reuse the closest pattern here rather
than inventing a new table shape, so the practice area stays consistent. None
of these patterns is a place for a coverage determination, a claim approval or
denial, a reserve, a claim value, a bad-faith conclusion, or a carrier
recommendation — those are outside the Insurance practice area entirely.
