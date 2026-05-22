> Shared reference material supporting the AgentCounsel Tax skills, used to help
> produce draft legal work product for qualified tax professional review — not
> tax advice.

# Tax Output Patterns

This file defines the reusable output structures the Tax skills produce, so an
issue map, a fact table, a request list, or a tracker looks and behaves the
same across every skill in `skills/tax/`. It is a consistency reference, not a
skill — each skill's own `SKILL.md` remains authoritative for what that skill
does and which patterns it uses.

Four rules apply to every pattern below.

- **Every extracted form, term, figure, or record cites its source** — the
  document and the form line, schedule, page, section, or ledger row, as
  written. A cell with no source is not complete.
- **Gaps are marked, never filled.** Where a value is absent or unclear, the
  cell reads `unknown`, `not found`, `not provided`, or `ambiguous` — never a
  guess.
- **Nothing is computed.** No tax, gain or loss, basis, exposure, or deadline
  is calculated. Dates are recorded as the document states them and flagged
  `[deadline verification required]`.
- **Sensitive identifiers are minimized.** SSN, EIN, TIN, and account numbers
  are masked by default (for example, `EIN ••-•••1234`); a full value appears
  only where strictly necessary and expressly requested.

Every output is draft work product for qualified tax counsel or a licensed tax
professional to review. No pattern below states tax treatment, a tax position,
a classification, a nexus conclusion, or a tax consequence.

---

## 1. Tax Issue Intake Matrix

Used by `tax-issue-intake`. One row per potential tax issue, framed as a
question for the tax professional — never as a conclusion.

| Column | Content |
|---|---|
| # | Issue number |
| Tax area | Income, sales/use, payroll/employment, property, transfer, excise, international, digital-asset, etc. |
| Factual trigger | The user-stated fact or sourced document point that raises the issue |
| Source | Document and location, or `user-stated fact` |
| Open question for tax professional | The question to evaluate — not the answer |
| Priority | High / Medium / Low (review urgency, not legal severity) |
| Missing facts | What is needed before the issue can be evaluated |

Pair with a **gates table**, a **source-cited fact register**, a **missing
information list**, and a **document request list**.

## 2. Entity Tax Classification Facts Table

Used by `entity-tax-classification-checklist`. Organizes the facts a tax
professional needs to evaluate classification. It does not state a classification.

| Column | Content |
|---|---|
| Fact category | Formation, ownership, elections, governing documents, ownership changes, foreign owners, filing history, etc. |
| Fact as provided | The fact, quoted or summarized from the source |
| Source | Document and location, or `user-stated fact` |
| Status | Provided / `not provided` / `ambiguous` |
| Classification question it bears on | The open question for tax counsel |

Pair with a **documents-to-review list**, a **possible classification
questions** list (questions only), and a **missing facts** list.

## 3. Transaction Tax Diligence Request List

Used by `transaction-tax-diligence-request-list`. Organized by tax workstream.

| Column | Content |
|---|---|
| # | Item number |
| Workstream | Income tax, sales/use tax, payroll/employment tax, property tax, transfer tax, unclaimed property, credits/incentives, NOLs/attributes, international, tax controversy, etc. |
| Request | The document or information requested |
| Priority | High / Medium / Low |
| Rationale | One line on why it matters to the transaction |
| Owner | Who must produce or follow up |
| Source / basis | What raised the request (deal fact, document, or standard scope) |
| Follow-up | Open questions tied to the item |

## 4. Sales / Use Tax Nexus Fact Map

Used by `sales-use-tax-nexus-triage`. One row per jurisdiction in scope. It
records facts; it does not conclude nexus, taxability, or a filing obligation.

| Column | Content |
|---|---|
| Jurisdiction | State, locality, or other taxing jurisdiction |
| Physical-presence facts | Offices, inventory, remote employees, property — as provided |
| Activity / revenue facts | Sales volume, transaction count, customer types — as provided |
| Product / service type | Tangible goods, software, SaaS, digital goods, services |
| Marketplace / certificate facts | Marketplace-facilitator sales, resale/exemption certificates on file |
| Filing history | Registrations and returns the user reports |
| Source | Document and location, or `user-stated fact` |
| Open question for tax professional | What the tax professional must evaluate |

Pair with a **missing facts list**, a **jurisdiction tracker**, and a
**document request list**.

## 5. Employment Tax Worker Classification Intake Table

Used by `employment-tax-worker-classification-intake`. One row per worker or
worker group. It captures facts to verify; it does not classify any worker.

| Column | Content |
|---|---|
| Worker / group | Role or population, by reference (not by full personal identifier) |
| Engagement facts | Control, supervision, tools/equipment, hours, exclusivity, location |
| Payment facts | Payment method, benefits, reimbursements, expense treatment |
| Document facts | Contract, Form W-2 / Form 1099 status as provided, payroll records |
| Source | Document and location, or `user-stated fact` |
| Fact status | Provided / `not provided` / `ambiguous` |
| Question for employment/tax counsel | The open question — not a classification |

Pair with a **risk-themes list**, a **missing-documents list**, and a
**questions for counsel** list.

## 6. Tax Provision Review Checklist

Used by `tax-provision-review-checklist`. One row per tax-related contract
provision.

| Column | Content |
|---|---|
| # | Item number |
| Provision | Gross-up, withholding, tax indemnity, cooperation, allocation, purchase-price allocation, transfer taxes, sales/use, VAT/GST, information reporting, audit cooperation, survival, caps/baskets, post-closing covenant, etc. |
| Section | Source section or clause, as written |
| What it says | The provision in plain language |
| Issue from the [role] perspective | The concern for the reviewing party |
| Status | Present / absent (`not found` after full review) / `ambiguous` |
| Negotiation point | The direction of a possible change — not drafted language |
| Tax-professional note | `[CONFIRM: ...]`, `[ATTORNEY TO CONFIRM: ...]`, or routing |

Pair with a **key tax terms table**, a **missing provisions list**, and a
**tax-professional verification checklist**.

## 7. Tax Document Inventory

Used by `tax-document-organizer`. One row per document or record set.

| Column | Content |
|---|---|
| # | Item number |
| Document | Return, K-1, W-2, 1099, notice, audit correspondence, entity document, payroll record, sales-tax filing, certificate, ledger, schedule, etc. |
| Period / year | The period the document covers, as labeled |
| Reference | Masked, non-sensitive reference (for example, `Return-2023-A`) |
| Sensitive identifiers | Whether SSN/EIN/TIN/account numbers appear — masked, not reproduced |
| Completeness | Complete / partial / illegible / `not provided` |
| Reviewer note | Uncertainty flags and what a reviewer should check |
| Source | How the document was provided |

Pair with a **missing-document list** and an **uncertainty-flag list**.

## 8. Tax Covenant / Indemnity Review Table

Used by `tax-covenants-indemnities-review`. One row per covenant or indemnity
mechanic.

| Column | Content |
|---|---|
| # | Item number |
| Mechanic | Pre-closing tax covenant, post-closing covenant, Straddle Period allocation, transfer taxes, refunds, tax contests, filing control, cooperation, indemnity scope, survival, cap, basket, exclusion, exclusive remedy, procedures, etc. |
| Section | Source section or clause, as written |
| What it says | The provision in plain language |
| Issue from the [role] perspective | The concern for the reviewing party |
| Status | Present / `not found` after full review / `ambiguous` |
| Negotiation point | The direction of a possible change — not drafted language |
| Tax-counsel note | Verification or routing flag |

Pair with a **covenant/indemnity architecture summary**, a **source table**,
and a **tax-counsel verification checklist**.

## 9. International Tax Issue Map

Used by `international-tax-issue-spotter`. One row per cross-border issue,
framed as a question for tax counsel.

| Column | Content |
|---|---|
| # | Issue number |
| Issue area | Withholding, permanent-establishment concept, transfer pricing, intercompany services, royalties/IP, VAT/GST, treaty question, foreign accounts, CFC/PFIC question, cross-border employment, etc. |
| Jurisdictions involved | The countries the issue touches |
| Factual trigger | The user-stated fact or sourced point that raises the issue |
| Source | Document and location, or `user-stated fact` |
| Open question for tax counsel | The question to evaluate — not the answer |
| Missing facts | What is needed before the issue can be evaluated |

Pair with a **jurisdictions-involved summary**, a **missing facts list**, and a
**document request list**.

## 10. Crypto / Digital Asset Tax Intake Matrix

Used by `crypto-digital-asset-tax-intake`. One row per activity category. It
organizes records; it does not calculate gain or loss or state treatment.

| Column | Content |
|---|---|
| Activity category | Purchase, sale, swap/trade, staking, mining, airdrop, NFT, DeFi, token grant, transfer, etc. |
| Business vs personal | As the user characterizes it, or `ambiguous` |
| Records provided | Wallet/exchange exports, Forms 1099, cost-basis records, statements |
| Record completeness | Complete / partial / `not provided` |
| Source | Wallet/exchange/account reference (masked) and document location |
| Missing records | What is needed before a tax professional can evaluate |
| Open question for tax professional | The question to evaluate — not the answer |

Pair with a **missing-records list**, a **document request list**, and an
**uncertainty-flag list**.
