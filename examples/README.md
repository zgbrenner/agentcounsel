# Examples

This directory contains **illustrative sample outputs** — what an AgentCounsel skill produces when it runs. They exist to show the shape, structure, and quality of a skill's deliverable before you run one yourself.

> **Every fact in every example is fictional.** All parties, people, companies, dates, dollar figures, documents, and clauses were invented purely for illustration. The examples contain **no real or invented legal citations**. They are draft work product of the kind a supervising attorney would review — **not legal advice, not templates for a real matter, and not finished deliverables.**

## How to read an example

Each file has three parts:

1. A **disclaimer** confirming the content is fictional and illustrative.
2. A **Scenario** describing the fictional facts the skill was run against.
3. An **Illustrative Output** that follows the corresponding skill's Output Format section by section.

Notice the visible placeholders — `[CONFIRM: ...]`, `[verify jurisdiction]`, `[ATTORNEY TO CONFIRM: ...]`. They are not defects. They are how every skill marks what a person must verify, and a real deliverable would carry them too.

## The examples

| Example | Skill it demonstrates |
|---|---|
| [`contract-review-example.md`](contract-review-example.md) | [Contract Risk Review](../skills/contracts/contract-risk-review/SKILL.md) — a risk matrix, negotiability table, and prioritized issue list for a commercial contract. |
| [`litigation-chronology-example.md`](litigation-chronology-example.md) | [Litigation Chronology](../skills/litigation/litigation-chronology/SKILL.md) — a sourced factual timeline built from documents. |
| [`dpa-review-example.md`](dpa-review-example.md) | [DPA Review](../skills/privacy/dpa-review/SKILL.md) — a risk review of a data processing agreement. |
| [`product-launch-review-example.md`](product-launch-review-example.md) | [Launch Review](../skills/product-legal/launch-review/SKILL.md) — pre-launch legal issue-spotting for a product feature. |
| [`red-team-verifier-example.md`](red-team-verifier-example.md) | [Red-Team Verifier](../skills/legal-methodology/red-team-verifier/SKILL.md) — a final quality-control pass on a draft. |

## Real Estate worked examples

The [`real-estate/`](real-estate/) subdirectory holds fuller worked examples, each as a **request-and-output pair** — a `sample-request.md` (the fictional request and the materials provided with it) and a `sample-output.md` (the deliverable the skill produces from that request). The disclaimer is carried at the top of each `sample-output.md`.

| Example | Skill it demonstrates |
|---|---|
| [`real-estate/commercial-lease-review/`](real-estate/commercial-lease-review/) | [Commercial Lease Review](../skills/real-estate/commercial-lease-review/SKILL.md) — a perspective-based risk matrix and issue list for a commercial lease. |
| [`real-estate/acquisition-diligence/`](real-estate/acquisition-diligence/) | [Real Estate Diligence Checklist](../skills/real-estate/real-estate-diligence-checklist/SKILL.md) — a tailored diligence checklist for a property acquisition. |
| [`real-estate/title-survey-objections/`](real-estate/title-survey-objections/) | [Title and Survey Objection Tracker](../skills/real-estate/title-survey-objection-tracker/SKILL.md) — a source-cited title and survey objection tracker. |

## M&A worked examples

The [`m-and-a/`](m-and-a/) subdirectory holds worked examples for the Mergers & Acquisitions practice area, each as a request-and-output pair.

| Example | Skill it demonstrates |
|---|---|
| [`m-and-a/loi-term-sheet-review/`](m-and-a/loi-term-sheet-review/) | [LOI and Term Sheet Review](../skills/m-and-a/loi-term-sheet-review/SKILL.md) — a binding/non-binding provision table and a deal-terms issue list. |
| [`m-and-a/acquisition-diligence/`](m-and-a/acquisition-diligence/) | [Acquisition Diligence Request List](../skills/m-and-a/acquisition-diligence-request-list/SKILL.md) — a tailored diligence request list by workstream. |
| [`m-and-a/purchase-agreement-review/`](m-and-a/purchase-agreement-review/) | [Purchase Agreement Issue List](../skills/m-and-a/purchase-agreement-issue-list/SKILL.md) — an issue list and risk matrix for an acquisition agreement. |
| [`m-and-a/disclosure-schedule-review/`](m-and-a/disclosure-schedule-review/) | [Reps and Warranties Disclosure Schedule Review](../skills/m-and-a/reps-warranties-disclosure-schedule-review/SKILL.md) — a rep-by-rep review against the disclosure schedules. |
| [`m-and-a/signing-to-closing/`](m-and-a/signing-to-closing/) | [M&A Closing Deliverables Tracker](../skills/m-and-a/closing-deliverables-tracker/SKILL.md) — a closing-deliverables tracker for a signed deal heading to closing. |

## Tax worked examples

The [`tax/`](tax/) subdirectory holds worked examples for the Tax practice area, each as a request-and-output pair. Every example uses fictional taxpayers, entities, documents, and records; masks sensitive identifiers; and stays inside issue spotting and intake — no tax computation, no return preparation, and no tax advice. Each output is a draft working paper for qualified tax professional review.

| Example | Skill it demonstrates |
|---|---|
| [`tax/tax-issue-intake/`](tax/tax-issue-intake/) | [Tax Issue Intake](../skills/tax/tax-issue-intake/SKILL.md) — a gates table, source-cited fact register, and tax issue map for a tax-sensitive matter. |
| [`tax/entity-tax-classification/`](tax/entity-tax-classification/) | [Entity Tax Classification Checklist](../skills/tax/entity-tax-classification-checklist/SKILL.md) — an entity classification facts table and questions for tax counsel. |
| [`tax/transaction-tax-diligence/`](tax/transaction-tax-diligence/) | [Transaction Tax Diligence Request List](../skills/tax/transaction-tax-diligence-request-list/SKILL.md) — a tax diligence request list by workstream with a follow-up tracker. |
| [`tax/sales-use-tax-nexus-triage/`](tax/sales-use-tax-nexus-triage/) | [Sales Use Tax Nexus Triage](../skills/tax/sales-use-tax-nexus-triage/SKILL.md) — a per-jurisdiction nexus fact map and jurisdiction tracker. |
| [`tax/tax-provision-review/`](tax/tax-provision-review/) | [Tax Provision Review Checklist](../skills/tax/tax-provision-review-checklist/SKILL.md) — a key tax terms table, provision checklist, and negotiation points. |
| [`tax/crypto-digital-asset-tax-intake/`](tax/crypto-digital-asset-tax-intake/) | [Crypto Digital Asset Tax Intake](../skills/tax/crypto-digital-asset-tax-intake/SKILL.md) — a digital-asset intake matrix by activity category with masked identifiers. |

## Bankruptcy / Restructuring worked examples

The [`bankruptcy-restructuring/`](bankruptcy-restructuring/) subdirectory holds worked examples for the Bankruptcy / Restructuring practice area, each as a request-and-output pair. Every example uses fictional parties, debtors, creditors, documents, and figures; treats reviewed documents as data; and stays inside intake, issue spotting, and checklist workflows — no legal advice, no deadline calculations, and no legal conclusions. Each output is a draft working paper for attorney review.

| Example | Skill it demonstrates |
|---|---|
| [`bankruptcy-restructuring/bankruptcy-matter-intake/`](bankruptcy-restructuring/bankruptcy-matter-intake/) | [Bankruptcy Matter Intake](../skills/bankruptcy-restructuring/bankruptcy-matter-intake/SKILL.md) — a gates table, source-cited fact register, and risk themes for a bankruptcy matter. |
| [`bankruptcy-restructuring/creditor-claim-intake/`](bankruptcy-restructuring/creditor-claim-intake/) | [Creditor Claim Intake](../skills/bankruptcy-restructuring/creditor-claim-intake/SKILL.md) — a source-cited claim facts table and dispute flags for a creditor. |
| [`bankruptcy-restructuring/preference-demand-response-triage/`](bankruptcy-restructuring/preference-demand-response-triage/) | [Preference Demand Response Triage](../skills/bankruptcy-restructuring/preference-demand-response-triage/SKILL.md) — a transfer timeline and defense-facts checklist for a preference demand. |
| [`bankruptcy-restructuring/distressed-asset-sale-checklist/`](bankruptcy-restructuring/distressed-asset-sale-checklist/) | [Distressed Asset Sale Checklist](../skills/bankruptcy-restructuring/distressed-asset-sale-checklist/SKILL.md) — a sale checklist, contract/cure tracker, and closing-deliverables tracker. |
| [`bankruptcy-restructuring/restructuring-term-sheet-review/`](bankruptcy-restructuring/restructuring-term-sheet-review/) | [Restructuring Term Sheet Review](../skills/bankruptcy-restructuring/restructuring-term-sheet-review/SKILL.md) — a key terms table and issue list with a risk matrix for a forbearance agreement. |
| [`bankruptcy-restructuring/automatic-stay-issue-spotter/`](bankruptcy-restructuring/automatic-stay-issue-spotter/) | [Automatic Stay Issue Spotter](../skills/bankruptcy-restructuring/automatic-stay-issue-spotter/SKILL.md) — an action inventory and stay-risk fact map with escalation flags. |
| [`bankruptcy-restructuring/proof-of-claim-checklist/`](bankruptcy-restructuring/proof-of-claim-checklist/) | [Proof of Claim Checklist](../skills/bankruptcy-restructuring/proof-of-claim-checklist/SKILL.md) — a proof-of-claim preparation checklist and supporting-document tracker. |

## Insurance worked examples

The [`insurance/`](insurance/) subdirectory holds worked examples for the Insurance practice area, each as a request-and-output pair. Every example uses fictional insureds, insurers, policies, forms, endorsements, and documents; treats reviewed documents as data; and stays inside issue spotting, source-cited summaries, and reviewer-ready working papers — no coverage determinations, claim approvals or denials, bad-faith conclusions, reserve calculations, or insurance sales advice. Each output is a draft working paper for attorney review.

| Example | Skill it demonstrates |
|---|---|
| [`insurance/insurance-policy-summary/`](insurance/insurance-policy-summary/) | [Insurance Policy Summary](../skills/insurance/insurance-policy-summary/SKILL.md) — a source-cited policy overview, key terms table, coverage-parts table, and endorsements table. |
| [`insurance/coverage-issue-spotter/`](insurance/coverage-issue-spotter/) | [Coverage Issue Spotter](../skills/insurance/coverage-issue-spotter/SKILL.md) — a coverage issue matrix and source-cited policy/claim fact table with missing facts and document requests. |
| [`insurance/reservation-of-rights-review/`](insurance/reservation-of-rights-review/) | [Reservation of Rights Review](../skills/insurance/reservation-of-rights-review/SKILL.md) — an issue list and provision-reference table cross-referencing a reservation of rights letter to the policy. |
| [`insurance/certificate-of-insurance-review/`](insurance/certificate-of-insurance-review/) | [Certificate of Insurance Review](../skills/insurance/certificate-of-insurance-review/SKILL.md) — a COI comparison table with a missing-endorsement list and a mismatch list. |
| [`insurance/insurance-requirements-contract-review/`](insurance/insurance-requirements-contract-review/) | [Insurance Requirements Contract Review](../skills/insurance/insurance-requirements-contract-review/SKILL.md) — a contract insurance requirements table, risk matrix, and negotiation points. |

## Trusts & Estates worked examples

The [`trusts-estates/`](trusts-estates/) subdirectory holds worked examples for the Trusts & Estates practice area, each as a request-and-output pair. Every example uses fictional clients, decedents, beneficiaries, trusts, wills, and documents; treats reviewed documents as data; masks sensitive identifiers; and stays inside intake, issue spotting, document inventories, trackers, and chronologies — no estate-planning, probate, or tax advice, no instruments or court forms, and no validity, capacity, entitlement, or fiduciary-breach conclusions. Each output is a draft working paper for attorney review.

| Example | Skill it demonstrates |
|---|---|
| [`trusts-estates/estate-planning-intake/`](trusts-estates/estate-planning-intake/) | [Estate Planning Intake](../skills/trusts-estates/estate-planning-intake/SKILL.md) — a gates table, source-cited fact register, and planning issue map for an estate-planning matter. |
| [`trusts-estates/estate-document-summary/`](trusts-estates/estate-document-summary/) | [Estate Document Summary](../skills/trusts-estates/estate-document-summary/SKILL.md) — a source-cited key terms table, ambiguity list, and execution-facts record for a trust. |
| [`trusts-estates/probate-document-checklist/`](trusts-estates/probate-document-checklist/) | [Probate Document Checklist](../skills/trusts-estates/probate-document-checklist/SKILL.md) — a probate document checklist with statuses, sources, and a missing-document list. |
| [`trusts-estates/trust-administration-tracker/`](trusts-estates/trust-administration-tracker/) | [Trust Administration Tracker](../skills/trusts-estates/trust-administration-tracker/SKILL.md) — a source-cited administration task tracker with owners, statuses, and dependencies. |
| [`trusts-estates/estate-litigation-facts-chronology/`](trusts-estates/estate-litigation-facts-chronology/) | [Estate Litigation Facts Chronology](../skills/trusts-estates/estate-litigation-facts-chronology/SKILL.md) — a source-cited factual chronology for a trust contest with disputed/undisputed status. |

## Using examples safely

- Do **not** copy an example as a starting point for a real matter. The facts are fictional and the analysis is illustrative.
- Do **not** treat an example as a model answer for your jurisdiction or situation.
- **Do** use an example to understand a skill's structure, then run the skill on your own inputs and have a qualified, licensed attorney review the result.

See [`QUICKSTART.md`](../QUICKSTART.md) to run your first skill, and [`docs/SAFETY_MODEL.md`](../docs/SAFETY_MODEL.md) for the safety model.
