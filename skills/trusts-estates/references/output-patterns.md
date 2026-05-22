> Shared reference material supporting the AgentCounsel Trusts & Estates
> skills, used to help produce draft legal work product for attorney review —
> not legal advice.

# Trusts & Estates Output Patterns

This file defines the reusable output structures the Trusts & Estates skills
produce, so an intake matrix, a document summary, an inventory, an issue
matrix, a tracker, or a chronology looks and behaves the same across every
skill in `skills/trusts-estates/`. It is a consistency reference, not a skill —
each skill's own `SKILL.md` remains authoritative for what that skill does and
which patterns it uses.

Four rules apply to every pattern below.

- **Every extracted term, figure, or fact cites its source** — the document and
  the will or trust article, instrument section, form field, statement line,
  court notice, or page, as written. A cell with no source is not complete.
- **Gaps are marked, never filled.** Where a value is absent or unclear, the
  cell reads `unknown`, `not found`, `not provided`, or `ambiguous` — never a
  guess.
- **Nothing is computed.** No deadline, tax, exemption, threshold, or asset
  value is calculated. Values appear only as the user provides them. Dates are
  recorded as the document states them and flagged
  `[deadline verification required]`.
- **No legal conclusion is stated.** No pattern below concludes the validity,
  capacity, or enforceability of an instrument; undue influence, fraud, or
  duress; beneficiary entitlement; fiduciary breach or liability; or tax
  treatment.

Every output is draft work product for a qualified, licensed attorney to
review before reliance, signing, filing, a fiduciary action, an asset
distribution, a beneficiary communication, a tax position, a probate action,
or an estate-planning decision.

---

## 1. Estate Planning Intake Matrix

Used by `estate-planning-intake`. One row per planning issue, framed as a
question for the attorney — never as a recommendation.

| Column | Content |
|---|---|
| # | Issue number |
| Topic | Family, fiduciary appointments, assets, business interests, incapacity planning, guardianship, charitable intent, tax, family conflict, etc. |
| Fact as provided | The fact, quoted or summarized from the source |
| Source | Document and location, or `user-stated fact` |
| Open question for the attorney | The question to evaluate — not the answer |
| Status | Provided / `not provided` / `ambiguous` |

Pair with a **gates table**, an **intake summary**, a **source-cited fact
register**, a **missing-information list**, and a **document request list**.

## 2. Estate Document Summary Table

Used by `estate-document-summary`. Concludes nothing on validity, capacity,
enforceability, or tax effect.

| Column | Content |
|---|---|
| Provision | Parties, fiduciaries, successor fiduciaries, beneficiaries, dispositive provisions, powers, conditions, amendment/revocation language, no-contest provision, tax provision, governing law |
| What it says | The provision in plain language |
| Article/Section | Source article, section, or page, as written |
| Source | The document the provision is drawn from |

Pair with a **document summary**, an **ambiguity list** (flagged, never
resolved), an **execution-facts** record (recorded as provided, never
assessed), and a **missing-document list**.

## 3. Probate Document Checklist

Used by `probate-document-checklist`. Prepares no filing-ready forms and
calculates no deadlines.

| Column | Content |
|---|---|
| Document | Death certificate, will/codicils, trust documents, asset statements, debts, beneficiary/heir information, notices, court documents, fiduciary appointment documents, tax documents, real estate records, creditor information |
| Status | Collected / partial / outstanding / `not provided` |
| Source | How the document was provided |
| Responsible party | Who must produce or follow up |
| Note | Uncertainty flags and what a reviewer should check |

Pair with a **missing-document list** and a **dates-as-provided** list (each
`[deadline verification required]`).

## 4. Trust Administration Tracker

Used by `trust-administration-tracker`. Approves no distribution and determines
no beneficiary entitlement.

| Column | Content |
|---|---|
| Task | The administration task — assets, distributions, accountings, tax, real estate, investments, business interests, debts, communications |
| Source | Document and location, or `user-stated fact` |
| Responsible party | Who owns the task |
| Status | Open / in progress / complete |
| Dependency | What the task depends on |
| Missing facts | What is needed before the task can proceed |

Pair with an **open-disputes list** (questions, not conclusions) and a
**dates-as-provided** list.

## 5. Fiduciary Duty Issue Matrix

Used by `fiduciary-duty-issue-spotter`. Concludes no breach, liability, or
compliance.

| Column | Content |
|---|---|
| # | Issue number |
| Issue area | Conflicts, self-dealing concerns, investment decisions, communications, accounting, distributions, expenses, recordkeeping, co-fiduciary issues, beneficiary objections, court supervision |
| Factual trigger | The user-stated fact or sourced point that raises the issue |
| Source | Document and location, or `user-stated fact` |
| Open question for the attorney | The question to evaluate — not the answer |

Pair with a **source-cited facts** table, an **escalation-items** list, and a
**missing-facts** list.

## 6. Beneficiary Designation Review Table

Used by `beneficiary-designation-review`. Concludes nothing on legal effect,
which document controls, or beneficiary entitlement.

| Column | Content |
|---|---|
| Account / asset | The account or asset the designation governs |
| Named beneficiary | The primary beneficiary as named on the form |
| Contingent beneficiary | The contingent beneficiary as named |
| Percentage | Allocation percentages as stated |
| Ownership | Account ownership / titling as stated |
| Form date | The designation date as written — `[deadline verification required]` |
| Source | Form, account record, or page |

Pair with an **inconsistency list** (inconsistencies with estate intent, framed
as questions, never resolved) and a **missing-document list**.

## 7. Asset / Liability Inventory

Used by `asset-liability-inventory-builder`. Values appear only as the user
provides them; no asset is appraised.

| Column | Content |
|---|---|
| Item | The asset or liability |
| Type | Real estate, bank/investment/retirement account, life insurance, business interest, vehicle, personal property, digital asset, debt, mortgage, tax, claim |
| Owner / title as provided | Ownership or title, as stated |
| Value as provided by user | The user-supplied value, or `not provided` — never computed |
| Beneficiary / titling note | Beneficiary or titling detail, where provided |
| Source | Statement, deed, record, or page |
| Status | Provided / `ambiguous` / unverified |

Pair with an **ambiguous-or-unverified assets** list and a **missing-facts**
list.

## 8. Capacity / Undue Influence Facts Organizer

Used by `capacity-undue-influence-facts-organizer`. Records facts as the
records state them; determines no capacity, undue influence, fraud, duress, or
validity, and makes no medical judgment.

| Column | Content |
|---|---|
| Date | The date as the record states it — `[deadline verification required]` |
| Event | The event as recorded — medical, relationship, or document-execution fact |
| Actor | The person or party involved |
| Source | Record, document, communication, or page |
| Disputed/undisputed | As the user provides it |

Pair with a **source table**, a **red-flag themes** list (questions, never
conclusions), and a **missing-facts** list.

## 9. Estate Litigation Chronology

Used by `estate-litigation-facts-chronology`. Assesses no merits and predicts
no outcome.

| Column | Content |
|---|---|
| Date | The date as the document states it — `[deadline verification required]` |
| Event | The dated event, supported by a source |
| Actor | The person or party involved |
| Source | Document, record, or page |
| Disputed/undisputed | As the user provides it; a disputed fact is never resolved |
| Relevance | A short, neutral relevance note |

Pair with a **missing-facts** list and a **follow-up items** list.

## 10. Trust Funding Checklist

Used by `trust-funding-checklist`. Prepares no transfer documents and
determines no tax consequences.

| Column | Content |
|---|---|
| Asset | The asset intended to fund the trust |
| Intended for trust | Whether the asset is intended for the trust, as provided |
| Funding evidence | The deed, assignment, retitling, designation, or confirmation provided |
| Responsible party | Who owns the funding item |
| Status | Funded / not started / `ambiguous` / `not provided` |
| Source | Instrument, account record, or page |

Pair with a **source table** and a **missing-items** list.

## 11. Post-Death Administration Task Tracker

Used by `post-death-administration-task-tracker`. Calculates no deadlines and
approves no distributions.

| Column | Content |
|---|---|
| Task | Immediate notices, document collection, asset inventory, debts/claims, fiduciary appointment, beneficiary communications, tax coordination, insurance, real estate, business interests, distributions, accounting, closing tasks |
| Source | Document and location, or `user-stated fact` |
| Owner | Who owns the task |
| Status | Open / in progress / complete |
| Dependency | What the task depends on |
| Uncertainty flag | `[deadline verification required]` or other uncertainty marker |

Pair with a **dates-as-provided** list (near-term dates flagged for attorney
attention) and a **missing-information** list.

## 12. Estate Tax Issue Intake Matrix

Used by `estate-tax-issue-intake`. Calculates no tax, exemption, exclusion, or
threshold, and reaches no tax-treatment conclusion.

| Column | Content |
|---|---|
| # | Issue number |
| Tax area | Estate, gift, GST, or inheritance tax; marital or charitable transfer; business interest; retirement account; life insurance; foreign asset/person |
| Factual trigger | The user-stated fact or sourced point that raises the issue |
| Source | Document and location, or `user-stated fact` |
| Open question for the tax professional | The question to evaluate — not the answer |
| Missing facts | What is needed before the issue can be evaluated |

Pair with a **gates table**, a **source-cited fact register**, a
**missing-facts** list, and a **document request list**.
