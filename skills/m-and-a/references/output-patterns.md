> Shared reference material supporting the AgentCounsel M&A skills, used to help produce draft legal work product for attorney review — not legal advice.

# M&A Output Patterns

This file defines the reusable output structures the M&A skills produce, so
that an issue list, a tracker, or a matrix looks and behaves the same across
every skill in `skills/m-and-a/`. It is a consistency reference, not a skill —
each skill's own `SKILL.md` remains authoritative for what that skill does.

Two rules apply to every pattern below:

- **Every extracted or summarized term cites its source** — the document and
  the section, clause, schedule, or page, as written. A cell with no source
  is not complete.
- **Gaps are marked, never filled.** Where a value is absent or unclear, the
  cell reads `Not found`, `Not provided`, `Unknown`, or `Ambiguous` — never a
  guess. Dates are recorded as the document states them and flagged
  `[deadline verification required]`; they are never computed.

All output is draft work product for attorney review.

---

## 1. M&A Issue List Table

Used by `purchase-agreement-issue-list` and, in lighter form, by
`loi-term-sheet-review`. Issues are framed from the stated side (buyer or
seller).

| Column | Content |
|---|---|
| # | Issue number |
| Topic / Clause | The deal topic or clause |
| Section | Source section or clause, as written |
| What it says | The provision in plain language |
| Issue from the [side] perspective | The risk or concern for the reviewing side |
| Risk | High / Medium / Low |
| Suggested direction | The direction of a change — not drafted clause language |
| Attorney note | `[CONFIRM: ...]`, `[ATTORNEY TO CONFIRM: ...]`, or routing |

Pair the table with a separate **key terms table**, a **missing provisions**
list, and an **internal inconsistency** list.

---

## 2. Diligence Request List Table

Used by `acquisition-diligence-request-list`. Organized by workstream.

| Column | Content |
|---|---|
| # | Item number |
| Workstream | Corporate, capitalization, financial, tax, contracts, IP, privacy/data, employment, litigation, regulatory, real estate, insurance, debt/liens, related-party, environmental, open-source, etc. |
| Request | The document or information requested |
| Priority | High / Medium / Low |
| Rationale | One line on why it matters |
| Responsible party | Who must produce or follow up |
| Follow-up questions | Open questions tied to the item |
| Conditional? | Marked if the workstream applies only on a stated condition |

---

## 3. Data Room Gap Matrix

Used by `data-room-index-review`. Built from the **index only** — document
contents are never inferred from filenames.

| Column | Content |
|---|---|
| Diligence category | The expected category |
| Coverage | Present / Partial / Absent / Unclear (from the index) |
| Observations | Stale, duplicate, ambiguous, or inconsistently named entries; possible privilege or confidentiality concerns — labeled preliminary |
| Source index reference | The folder or index entry |
| Follow-up request | What to request or clarify |

---

## 4. Disclosure Schedule Review Table

Used by `reps-warranties-disclosure-schedule-review`. One row per
representation. The skill never concludes the disclosures are adequate.

| Column | Content |
|---|---|
| # | Representation number |
| Representation | The representation, summarized |
| Agreement source | The section of the representations article |
| Schedule source | The disclosure schedule reference, or `Not provided` |
| Issue | Missing schedule, blank or `[to be provided]` item, overbroad exception, inconsistent definition, stale date, or fact/disclosure mismatch |
| Risk to the [side] | The concern for the reviewing side |
| Follow-up | What to obtain or resolve |
| Attorney verification item | The question routed to counsel |

---

## 5. Indemnity Architecture Summary

Used by `indemnity-escrow-risk-review`. Summarizes the architecture, then a
**recovery waterfall** (the order and limits of recovery, as the agreement
states them) and a **buyer/seller risk matrix**. Any reference to a "typical"
or "market" figure is a placeholder for attorney verification, marked as such.

| Element | Content |
|---|---|
| Survival | Survival periods, by category (general, fundamental, tax, special) |
| Cap | Cap amount and what it applies to |
| Basket / deductible | Threshold type and amount |
| Escrow / holdback | Amount, release mechanics |
| Special indemnities | Identified special indemnity items |
| Carve-outs | Fraud, fundamental reps, and other carve-outs from limits |
| Claim procedure | Notice, third-party vs. direct claims, setoff, exclusive remedy |
| Insurance / RWI | Whether representation and warranty insurance is referenced |
| Source | Section or clause for each element |

---

## 6. Consent Tracker

Used by `third-party-consents-assignment-review`. The skill flags triggers; it
does not conclude whether consent is legally required or whether a clause is
enforceable.

| Column | Content |
|---|---|
| # | Item number |
| Contract / source | The contract and the triggering section or clause |
| Trigger type | Consent, notice, assignment, change-of-control, anti-assignment, termination, MFN, exclusivity, non-compete/non-solicit, data-transfer, or regulatory/customer/vendor approval |
| Required action | The action the clause appears to call for |
| Timing | As the contract states it, flagged `[deadline verification required]` |
| Business impact | Described, not legally concluded |
| Owner | Who is responsible |
| Follow-up | Open item or document needed |

---

## 7. Closing Deliverables Tracker

Used by `closing-deliverables-tracker`. Deadlines are never computed; only
user-supplied dates appear, flagged for verification.

| Column | Content |
|---|---|
| # | Item number |
| Deliverable | The closing document or action |
| Responsible party | Buyer, seller, escrow, lender, or counsel |
| Status | Open / In progress / Complete |
| Dependency | What it depends on |
| Source | The agreement section, where derived from one |
| Signer | Who signs, if stated |
| Form needs | Notary, original, or certified-copy need, if stated |
| Open issue | Any open question |

---

## 8. Post-Closing Obligations Tracker

Used by `post-closing-obligations-tracker`. Obligations are extracted only from
provided documents; obligations and dates are never invented.

| Column | Content |
|---|---|
| # | Item number |
| Obligation | The post-closing covenant or obligation |
| Owner | Who must perform |
| Trigger | The event or condition that starts it |
| Due date | As the document states it, flagged `[deadline verification required]`, or `Not stated` |
| Source | The document and section |
| Dependency | What it depends on |
| Status | Open / In progress / Complete |
| Verification item | The question routed to counsel |

---

## Using these patterns

A skill may extend a pattern with extra columns where its workflow needs them,
but should not drop the source column or the gap-marking convention. When a
maintainer adds a new M&A skill, reuse the closest pattern here rather than
inventing a new table shape, so the practice area stays consistent.
