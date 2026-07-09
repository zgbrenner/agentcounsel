> Shared reference material supporting the AgentCounsel contracts skills, used to help produce draft legal work product for attorney review — not legal advice.

# Clause Category Completeness Checklist

This is a **completeness checklist**, not a risk framework. It lists clause
categories that recur across commercial contracts so a reviewer can confirm
that each category was actively considered — either found, found and flagged,
or confirmed absent — before calling a review finished. It does not tell a
reviewer how deep to go on any one category, what severity to assign, or what
position to take. The reviewing skill (`contract-risk-review`, `nda-review`,
or another contracts skill) decides depth, applies its own risk rating, and
draws on `skills/contracts/references/red-flags.md` and
`skills/contracts/references/document-type-checklists.md` for the substantive
analysis. Use this checklist as a first-pass sweep to reduce the chance that a
clause category is simply never looked at.

**Attribution.** The category names and grouping below are adapted from the
category taxonomy used by the CUAD (Contract Understanding Atticus Dataset)
project, The Atticus Project, licensed CC-BY-4.0. The one-line descriptions
of what to check and why are written independently for AgentCounsel; they are
not the CUAD paper's or dataset's text.

---

## How to Use This Checklist

1. Work through each category below against the document under review.
2. For each category, record one of: **Present** (cite the section), **Present
   and flagged** (route to the relevant red-flag or risk-matrix entry), or
   **Absent** (note the absence — under many categories, absence is itself a
   finding).
3. This checklist does not replace the clause-by-clause review, the red-flag
   scan, or the document-type checklist — it runs alongside them as a sweep to
   catch a skipped category.
4. Flag every open question for attorney review; do not resolve ambiguity
   silently.

---

## 1. Formation and Term

| Category | What to check and why it matters |
|---|---|
| Document name | Confirm the document's stated title matches its actual legal function — a mislabeled document (e.g., a "letter agreement" that is actually a binding MSA) can create confusion about which review standard applies. |
| Parties | Confirm every party is a correctly named legal entity, not a trade name or an individual signing without disclosed authority — a defective party block can make the agreement unenforceable against the intended entity. |
| Agreement date | Note the date the agreement was signed; it anchors which version of referenced policies, rates, or law applies and is distinct from the effective date. |
| Effective date | Confirm when obligations actually begin — an effective date that differs from the agreement date can shift when notice periods, renewal clocks, or warranties start running. |
| Expiration date | Confirm whether the agreement has a fixed end date, and whether obligations (confidentiality, indemnity, IP) are stated to survive it. |
| Renewal term | Confirm whether the agreement renews automatically, on the same terms, and for what length — an unnoticed renewal can commit the client to another full term. |
| Notice to terminate renewal | Confirm the window and method required to stop an automatic renewal — a short or ambiguous window is a common way a client gets locked in unintentionally. |
| Governing law | Confirm which jurisdiction's law governs the agreement `[verify jurisdiction]` — this affects how every other clause on this checklist is actually enforced. |
| Termination for convenience | Confirm whether either party (or only one) can exit without cause, on what notice, and at what cost — an asymmetric convenience-termination right favors whichever party holds it. |

## 2. Restrictive Covenants

| Category | What to check and why it matters |
|---|---|
| Most favored nation | Confirm whether either party must offer the other terms at least as good as it gives anyone else — this is an ongoing compliance burden that is easy to overlook after signing. |
| Non-compete | Confirm what activity, market, or geography is restricted and for how long — a non-compete that reaches beyond the deal's subject matter can constrain the client's ordinary business `[verify jurisdiction]`. |
| Exclusivity | Confirm whether either party is barred from dealing with others in the same category — exclusivity can foreclose alternative revenue or supply options the client may need later. |
| No-solicit of customers | Confirm which customers or segments are off-limits and for how long — this can quietly block growth into adjacent markets. |
| No-solicit of employees | Confirm whether the restriction has carve-outs for general job postings and unsolicited applicants, and whether it is scoped to people connected to this deal. |
| Non-disparagement | Confirm what statements are restricted and whether the restriction is mutual — a one-sided non-disparagement clause can silence legitimate complaints from only one side. |
| Covenant not to sue | Confirm the scope of claims released or waived and whether it is reciprocal — a broad covenant not to sue can foreclose remedies for future, unrelated conduct if drafted too widely. |

## 3. Commercial Terms

| Category | What to check and why it matters |
|---|---|
| Right of first refusal / offer / negotiation (ROFR/ROFO/ROFN) | Confirm what triggers the right, how long the holder has to respond, and whether it could slow down or chill a future transaction the client wants to pursue. |
| Change of control | Confirm what happens if either party is acquired or merges — an unaddressed change-of-control trigger can bind the client to an unwanted new counterparty, or let the counterparty exit early. |
| Anti-assignment | Confirm whether the client can assign the agreement (including to an affiliate or in an internal reorganization) without the counterparty's consent — this can complicate the client's own future transactions. |
| Revenue / profit sharing | Confirm how shared amounts are calculated, audited, and reconciled — an ambiguous formula is a common source of later payment disputes. |
| Price restrictions | Confirm any limits on how either party may price a product or service (e.g., resale price terms) — these can carry their own regulatory considerations `[verify jurisdiction]`. |
| Minimum commitment | Confirm the minimum spend or volume the client must meet and the consequence of falling short — an unmet minimum can trigger a shortfall payment the client did not budget for. |
| Volume restriction | Confirm any cap on usage, seats, or output — exceeding it may trigger additional fees or a breach, so it needs to be checked against the client's actual or projected use. |
| Audit rights | Confirm who may audit whom, on what notice, how often, and who bears the cost — an unbounded audit right (in either direction) can be disruptive or used to generate surprise back-charges. |
| Third-party beneficiary | Confirm whether anyone outside the two signing parties can enforce the agreement — an unintended third-party beneficiary designation can expose the client to claims from someone it never negotiated with. |

## 4. IP and Licensing

| Category | What to check and why it matters |
|---|---|
| IP ownership assignment | Confirm the assignment is in present-tense language ("hereby assigns") rather than a future promise to assign, which may require a further act to perfect the transfer `[verify jurisdiction]`. |
| Joint IP ownership | Confirm how joint ownership is defined and how each co-owner may use, license, or enforce the jointly owned IP — joint ownership defaults vary significantly by jurisdiction `[verify jurisdiction]`. |
| License grant | Confirm the scope of the license — field of use, territory, exclusivity, and whether it is a license to use or a transfer of ownership, since the two create very different rights. |
| Non-transferable license | Confirm whether the license can move with an assignment, merger, or corporate reorganization — a non-transferable license can strand a licensee mid-transaction. |
| Affiliate license – licensor | Confirm whether the licensor's affiliates are bound by the same license terms and restrictions, or only the named licensor entity — a gap here can let an affiliate ignore the deal's terms. |
| Affiliate license – licensee | Confirm whether the licensee's affiliates may use the licensed rights, and whether that use is subject to the same restrictions as the named licensee — unaddressed affiliate use is a common compliance gap. |
| Unlimited / all-you-can-eat license | Confirm whether the license is genuinely uncapped as to users, volume, or use case, and whether that scope matches what was actually negotiated — an unlimited grant can be broader than either party intended. |
| Irrevocable or perpetual license | Confirm whether the license survives termination of the underlying agreement and cannot be revoked — this changes what the parties actually retain after the relationship ends. |
| Source code escrow | Confirm the release triggers (e.g., vendor insolvency, abandonment) and whether the escrow deposit is verified as current — an escrow right is only useful if the deposited code actually works. |
| Post-termination services | Confirm what transition assistance, wind-down support, or continued access is owed after termination — without this, a party can be cut off from data or systems with no ability to transition. |

## 5. Liability and Risk

| Category | What to check and why it matters |
|---|---|
| Uncapped liability | Confirm which obligations (if any) are expressly carved out from any cap — uncapped exposure on a broad indemnity or confidentiality breach can be disproportionate to the deal's value. |
| Cap on liability | Confirm the cap's formula and base (e.g., fees paid in a defined period) and compare it to the client's realistic worst-case exposure — see `skills/contracts/references/red-flags.md`, Section 1. |
| Liquidated damages | Confirm whether the stated amount is tied to a genuine pre-estimate of loss or reads as a penalty — enforceability of liquidated-damages clauses varies by jurisdiction `[verify jurisdiction]`. |
| Warranty duration | Confirm how long the warranty runs and when it starts (delivery, acceptance, go-live) — a warranty that expires before latent defects can reasonably surface offers little real protection. |
| Insurance | Confirm what coverage types and limits are required of the counterparty, and whether the client is named as an additional insured — an indemnity is only as good as the counterparty's ability to pay it. |

---

## Reviewer Notes

- This checklist is deliberately shallow — one line per category — so it can
  run as a fast completeness sweep. Depth of analysis, risk rating, and
  negotiation posture belong to the reviewing skill and the supervising
  attorney, not to this checklist.
- A category marked "Absent" is a finding to carry into the risk matrix or
  issue list, not a conclusion that the omission is acceptable or
  unacceptable — that judgment is the attorney's.
- This checklist does not assert what any category typically contains in the
  market; see `skills/contracts/references/market-benchmark-framework.md` and
  `skills/contracts/references/market-standard-baselines.md` for the
  benchmarking discipline.
- See `skills/contracts/contract-risk-review/SKILL.md` for the full
  clause-by-clause review workflow, and
  `skills/contracts/nda-review/SKILL.md` for the NDA-specific scope check.
