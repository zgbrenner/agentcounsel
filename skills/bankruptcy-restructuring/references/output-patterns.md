> Shared reference material supporting the AgentCounsel Bankruptcy /
> Restructuring skills, used to help produce draft legal work product for
> attorney review — not legal advice.

# Bankruptcy / Restructuring Output Patterns

This file defines the reusable output structures the Bankruptcy / Restructuring
skills produce, so an intake matrix, a facts table, an issue list, a checklist,
or a tracker looks and behaves the same across every skill in
`skills/bankruptcy-restructuring/`. It is a consistency reference, not a skill —
each skill's own `SKILL.md` remains authoritative for what that skill does and
which patterns it uses.

Four rules apply to every pattern below.

- **Every extracted term, figure, or fact cites its source** — the document and
  the docket entry, pleading section, claim document, contract clause, notice,
  or page, as written. A cell with no source is not complete.
- **Gaps are marked, never filled.** Where a value is absent or unclear, the
  cell reads `unknown`, `not found`, `not provided`, or `ambiguous` — never a
  guess.
- **Nothing is computed.** No deadline, bar date, claim amount, cure amount,
  exposure, or priority is calculated. Dates are recorded as the document
  states them and flagged `[deadline verification required]`.
- **No legal conclusion is stated.** No pattern below concludes stay
  applicability, claim validity or priority, preference liability, whether a
  contract is executory, free-and-clear sale treatment, plan confirmability,
  or lien validity or priority.

Every output is draft work product for a qualified, licensed attorney to
review before reliance, filing, or any action.

---

## 1. Bankruptcy Matter Intake Matrix

Used by `bankruptcy-matter-intake`. One row per matter fact or risk theme,
framed as a question for the attorney — never as a conclusion.

| Column | Content |
|---|---|
| # | Item number |
| Topic | Parties, case status, claim type, contract relationship, collateral/lien, litigation, payments, requested action, etc. |
| Fact as provided | The fact, quoted or summarized from the source |
| Source | Document and location, or `user-stated fact` |
| Open question / risk theme | The question for the attorney — not the answer |
| Status | Provided / `not provided` / `ambiguous` |

Pair with a **gates table**, a **matter summary**, a **dates-as-provided**
list (each `[deadline verification required]`), a **missing-information list**,
and a **document request list**.

## 2. Creditor Claim Facts Table

Used by `creditor-claim-intake`. Organizes claim facts; states no claim
validity, priority, allowance, or secured status.

| Column | Content |
|---|---|
| Fact category | Basis of claim, amount as stated, secured/priority assertion, collateral, guaranties, offsets, payments, disputes, proof-of-claim status |
| Fact as provided | The fact, quoted or summarized |
| Source | Document and location, or `user-stated fact` |
| Status | Provided / asserted (not verified) / `not provided` / `ambiguous` |

Pair with a **dispute-flags list** (questions), a **missing-facts list**, and a
**document request list**.

## 3. Proof of Claim Preparation Checklist

Used by `proof-of-claim-checklist`. A preparation aid — not a filing-ready
claim. No bar date is calculated.

| Column | Content |
|---|---|
| # | Item number |
| Preparation item | Claimant identity, debtor/case detail, basis, amount as stated, supporting documents, secured/priority assertion, interest/fees as provided, assignment/transfer, redaction needs, signature authority |
| Status | Ready / outstanding / `not provided` |
| Source | Supporting document and location |
| Note | Redaction flag, signature-authority flag, or routing |

Pair with a **supporting-document tracker** (item | document | provided? |
redaction needed?), a **bar-date-as-provided** entry flagged
`[deadline verification required]`, and a **missing-information list**.

## 4. Automatic Stay Issue-Spotting Matrix

Used by `automatic-stay-issue-spotter`. One row per action; states no
conclusion on whether the stay applies or whether an action is permitted.

| Column | Content |
|---|---|
| # | Action number |
| Action / communication | Collection, litigation, setoff, foreclosure, repossession, contract termination, payment demand, eviction, lien enforcement, regulatory action, post-petition communication, etc. |
| Timing as stated | Timing relative to the petition date, as the user states it |
| Facts that bear on stay concerns | The source-cited facts — not a conclusion |
| Source | Document and location, or `user-stated fact` |
| Open question for the attorney | The question to evaluate |
| Escalation | Flag if the action should be routed for immediate attorney attention |

Pair with an **action inventory**, a **missing-facts list**, and **attorney
verification questions**.

## 5. Preference Demand Response Timeline

Used by `preference-demand-response-triage`. Records alleged transfers as
stated; concludes no preference liability and no defense.

| Column | Content |
|---|---|
| # | Transfer number |
| Date as stated | The transfer date as alleged or recorded — never computed |
| Amount as stated | The transfer amount as alleged or recorded |
| Source | Demand letter, invoice, statement, or ledger location |
| Note | Context as provided |

Pair with a **defense-facts checklist** (defense theme | facts provided | facts
missing | source — facts only, never conclusions), a **response-planning
issues** list, and a **missing-documents list**.

## 6. Executory Contract Assumption/Rejection Tracker

Used by `executory-contract-assumption-rejection-checklist`. Records contract
facts; concludes nothing on executory status, assumability, assignability, or
rejectability.

| Column | Content |
|---|---|
| Contract | Contract or lease identity |
| Parties / roles | Debtor and counterparty roles |
| Key terms | Term, defaults, assignment rights, anti-assignment language, consent issues, as written |
| Cure / default item | Cure amounts and defaults as stated — never computed |
| Source | Contract clause, notice, or page |
| Status | Assumption/rejection status as stated; `not provided` if absent |
| Issue for the attorney | The open question — not a conclusion |

Pair with a **contract status table**, a **cure/default tracker**, and a
**missing-facts list**.

## 7. Bankruptcy Diligence Request List

Used by `bankruptcy-diligence-request-list`. Organized by workstream.

| Column | Content |
|---|---|
| # | Item number |
| Workstream | Debtor organization, debt structure, liens/collateral, contracts, litigation, claims, taxes, employees/benefits, environmental, real estate, IP, financials, cash management, insider transactions, avoidance actions, regulatory, sale/plan documents, etc. |
| Request | The document or information requested |
| Priority | High / Medium / Low |
| Rationale | One line on why it matters |
| Owner | Who must produce or follow up |
| Source / basis | What raised the request (deal fact, document, or standard scope) |
| Follow-up | Open questions tied to the item; mark conditional requests |

## 8. Restructuring Term Sheet Issue List

Used by `restructuring-term-sheet-review`. One row per restructuring term;
concludes nothing on enforceability, plan feasibility, or legal sufficiency.

| Column | Content |
|---|---|
| # | Issue number |
| Term | Parties, debt instruments, milestones, releases, covenants, payment terms, collateral, guaranties, consents, defaults, fees, voting/support obligations, termination rights, exclusivity, confidentiality, conditions |
| Section | Source section or clause, as written |
| What it says | The term in plain language |
| Concern from the [role] perspective | The concern for the reviewing side |
| Risk | High / Medium / Low (review priority, not a legal conclusion) |
| Attorney follow-up | `[CONFIRM: ...]`, `[ATTORNEY TO CONFIRM: ...]`, or routing |

Pair with a **key terms table**, a **missing-terms list** (`not found` after a
full review), and **negotiation points** (direction only).

## 9. Plan / Disclosure Statement Issue Tracker

Used by `plan-disclosure-statement-issue-spotter`. Concludes nothing on
confirmability, disclosure adequacy, priority compliance, feasibility, or the
voting outcome.

| Column | Content |
|---|---|
| # | Issue number |
| Topic | Classification, treatment, voting, releases/exculpation/injunctions, executory contracts, claims reconciliation, governance, equity treatment, objections, confirmation issues |
| Provision as written | The plan or disclosure-statement provision |
| Section | Source section, article, or page |
| Open question for the attorney | The question to evaluate — not the answer |

Pair with a **source-cited treatment table** (class | classification as written
| treatment as written | source), a **consistency-issues list**, and a
**missing-facts list**.

## 10. Distressed Asset Sale Checklist

Used by `distressed-asset-sale-checklist`. Concludes nothing on free-and-clear
treatment or sale-procedure sufficiency.

| Column | Content |
|---|---|
| Process step | Asset identification, stalking-horse terms, bid procedures, liens/encumbrances, cure costs, assigned contracts, employee matters, IP, real estate, taxes, regulatory approvals, closing deliverables, sale-order issues |
| Status | Complete / partial / `not provided` |
| Source | Sale document, motion, or page |
| Note | What a reviewer should check |

Pair with a **diligence request list**, a **contract/cure tracker** (cure
amounts as provided), and a **closing-deliverables tracker**.

## 11. DIP / Cash Collateral Issue Table

Used by `cash-collateral-dip-financing-issue-spotter`. Approves no financing
term and determines no lien validity, perfection, or priority.

| Column | Content |
|---|---|
| # | Issue number |
| Term | Lenders, collateral, liens, budget, reporting covenants, milestones, roll-ups, adequate protection, carveouts, default triggers, use restrictions, releases, investigation periods, professional fees |
| Section | Source section, clause, budget line, or page |
| What it says | The term in plain language |
| Open question for the attorney | The question to evaluate — flag business vs. legal |
| Status | Present / `not found` after full review / `ambiguous` |

Pair with a **key terms table**, separated **business and legal questions**,
and a **missing-facts list**.

## 12. Bankruptcy Deadline Tracker Intake Table

Used by `bankruptcy-deadline-tracker-intake`. Records only user-provided dates;
calculates nothing. Every row is flagged for attorney verification.

| Column | Content |
|---|---|
| Item | Petition date, bar date, meeting date, objection deadline, plan/disclosure-statement date, sale date, hearing date, internal task deadline |
| Date as provided | The date exactly as the user supplied it |
| Source | Docket entry, notice, order, or page |
| Responsible party | Who owns the item |
| Status | Open / in progress / complete |
| Uncertainty flag | `[deadline verification required]` on every row |

Pair with a **user-supplied computed entries** list (only where the user
supplied the rule and calculation; still flagged for verification), a
**near-term escalation flags** list, and a **missing-information list**.
