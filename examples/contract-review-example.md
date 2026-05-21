# Example: Contract Risk Review

> **Illustrative example — not legal advice.** This is a sample of what the Contract Risk Review skill (`skills/contracts/contract-risk-review/SKILL.md`) produces. Every party, date, figure, and clause in it is **fictional** and was invented for illustration. It is the kind of draft work product a supervising attorney would review — not a finished deliverable, and not legal advice. See `examples/README.md`.

## Scenario

Northwind Analytics, Inc. is a fictional 90-person data-analytics company that wants to adopt a new business-intelligence platform. Its vendor, Cirrus Cloud Platforms LLC, sent over Cirrus's standard-form Master Subscription Agreement (the "MSA") for a three-year subscription, and the deal lead, Jordan Avery, asked the legal team for a first-pass risk review before negotiation. Northwind is the **customer**; Cirrus is the SaaS vendor. The platform will ingest Northwind's customer data and some employee data, and Northwind's own analysts will build dashboards on it. The contract is the vendor's unmodified standard form (higher scrutiny). Approximate transaction value is $360,000 over the initial term. This example shows the draft review the skill produces for the supervising attorney.

## Illustrative Output

> **Draft for attorney review. Not legal advice.** Prepared from the contract text provided; all section references and quotations must be verified against the source document before reliance.

### 1. Document Summary

- **Document:** Master Subscription Agreement, Cirrus Cloud Platforms LLC standard form (rev. "MSA-2025-A").
- **Parties:** Northwind Analytics, Inc. ("Customer," the client) and Cirrus Cloud Platforms LLC ("Provider").
- **Client's role:** Customer / subscriber.
- **Effective date:** `[CONFIRM: effective date — signature block undated]`.
- **Governing law / forum:** Stated as the Provider's home state with exclusive venue there `[CONFIRM: governing law and venue]`.
- **Counterparty form vs. negotiated draft:** Provider's unmodified standard form — review at heightened scrutiny.
- **Transaction profile:** 3-year subscription, ~$360,000 total; moderate risk, elevated by ingestion of customer and employee data.

### 2. Structural Map

**Present:** Definitions; Subscription & Access; Term & Renewal; Fees & Payment; Customer Data & Security; IP & License Grant; Confidentiality; Warranties; Indemnification; Limitation of Liability; Termination; Governing Law & Disputes; Assignment; General.

**Absent:** Service-level / uptime commitment; insurance requirements; force majeure; audit rights; data export / transition assistance on termination; affiliate-use rights.

### 3. Red Flags Quick Scan

- Auto-renewal with a short non-renewal notice window.
- Unilateral price-escalation right with no stated cap.
- Liability cap set at a small fraction of contract value.
- One-sided indemnity (Customer indemnifies Provider; no reciprocal Provider IP indemnity).
- Provider may assign freely, including on change of control, without Customer consent.
- No data-export or transition assistance on termination.

### 4. Clause-by-Clause Summary

- **Parties / signatories** — Entities named; signature block undated and signatory authority unstated. `[CONFIRM: correct Northwind entity and authorized signatory.]`
- **Term & renewal** — 3-year initial term; auto-renews for successive 1-year terms unless either party gives notice 90 days before renewal. Risk: easy to miss the window and be locked in another year.
- **Scope / access** — Subscription to the platform "as made generally available"; Provider may modify or discontinue features in its discretion. Risk: feature Northwind relies on could be removed.
- **Fees & payment** — Net-15 payment; Provider may raise fees on renewal "in its sole discretion" with no cap. Risk: uncapped renewal pricing against switching costs.
- **IP & license grant** — Provider retains all platform IP. Customer Data: Provider takes a license to use it to provide and "improve" the services. Risk: "improve" may extend to model training; ownership of Customer-built dashboard configurations is unaddressed. `[CONFIRM: whether dashboard configurations are Customer- or Provider-owned.]`
- **Confidentiality** — Mutual; obligations expire 2 years post-termination; no return-or-destroy obligation.
- **Data privacy & security** — Generic "industry-standard" security language; no DPA, no breach-notification timeline, no deletion-on-termination commitment. `[CONFIRM: applicable data-privacy regimes — not assessed by this skill.]`
- **Warranties** — Limited warranty that services conform to documentation; all implied warranties disclaimed.
- **Indemnification** — Customer indemnifies Provider broadly, including for Customer Data; no reciprocal Provider indemnity for third-party IP claims arising from the platform.
- **Limitation of liability** — See decomposition in rows 11a–11d below.
- **Insurance** — None required of Provider.
- **Termination** — Provider may terminate for cause on 10 days' notice; for-convenience right is Provider-only. No Customer for-cause cure parity. No transition assistance.
- **Disputes / governing law** — Provider's home forum, exclusive venue, jury waiver.
- **Assignment** — Customer needs consent to assign; Provider may assign freely, including on change of control.
- **Unusual clauses** — Provider may suspend access immediately for any payment dispute, including disputed amounts.

### 5. Risk Matrix

| # | Clause / Topic | What It Says (Plain Language) | Risk to Client | Legal Risk | Business Friction | Suggested Change |
|---|---|---|---|---|---|---|
| 2 | Term & Renewal | Auto-renews 1 yr; 90-day non-renewal notice | Miss window, locked in a year | Med | Slowing | Add calendar-triggered exit; shorten window |
| 4 | Fees & Price Adjustment | Uncapped renewal increase at Provider discretion | Unbudgeted cost spikes | High | Slowing | Cap annual escalation (e.g., fixed %) |
| 5 | IP — Customer Data License | License to "improve" services | Possible model-training use of Northwind data | High | Confusing | Limit license to service delivery; exclude training |
| 8 | Data Privacy & Security | Generic security; no DPA / breach timeline | No clear breach response or deletion duty | High | Slowing | Add DPA, breach-notice SLA, deletion on exit |
| 10 | Indemnification | One-sided; no Provider IP indemnity | Northwind exposed to platform IP claims | High | Confusing | Add mutual indemnity; Provider covers platform IP |
| 11a | LoL — Direct vs. Consequential | "Neither party liable for indirect, incidental, special, or consequential damages" — mutual | Northwind's realistic data-loss losses are consequential in nature | High | None | Carve out data-breach and confidentiality losses |
| 11b | LoL — Cap Amount | Cap = "fees paid in the 3 months preceding the claim" | ~$30K cap vs. $360K deal | High | None | Raise cap; tie to 12 months' fees or total value |
| 11c | LoL — Carve-Outs | No carve-outs; cap applies to all claims | Indemnity, breach, willful misconduct all capped | High | None | Add mutual carve-outs (IP, fraud, breach, willful) |
| 11d | LoL — Overall Allocation | Small cap + broad exclusion + no carve-outs | Northwind materially underprotected | High | None | Reposition allocation `[ATTORNEY TO CONFIRM: vs. insurance]` |
| 12 | Insurance | None required of Provider | No recourse if Provider uninsured | Med | None | Add minimum coverage + certificate |
| 14 | Termination for Convenience | Provider-only; no Customer parity | Service can end; Customer cannot exit early | Med | Slowing | Add mutual for-convenience right |
| 15 | Effects of Termination | No data export / transition assistance | Loss of access to Northwind's own data | High | Blocking | Add export window + transition assistance |
| 17 | Assignment / Change of Control | Provider may assign freely; Customer needs consent | Northwind could be bound to unknown acquirer | Med | Slowing | Add change-of-control consent or exit right |
| 18 | Suspension on Payment Dispute | Immediate suspension for any disputed amount | Service cut off over a good-faith billing dispute | High | Blocking | Limit suspension to undisputed, overdue amounts |

_Legal Risk: High / Med / Low. Business Friction: Blocking / Slowing / Confusing / None. Rated independently per the skill's risk matrix._

### 6. Negotiability Table

| Issue | Negotiability Rating | Basis | Recommended Lawyer Action |
|---|---|---|---|
| Liability cap at 3 months' fees (11b) | Must Push | Cap far below deal value; vendor form; standard to negotiate | Negotiate higher cap and floor |
| No cap carve-outs (11c) | Must Push | Leaves indemnity and breach fully capped | Draft mutual carve-out set |
| Data export on termination (15) | Must Push | Customer's own data; operational continuity at stake | Add export + transition language |
| Customer Data "improvement" license (5) | Strong Push | Potential training use; reputational and data-rights exposure | Narrow license scope |
| Uncapped renewal price increase (4) | Strong Push | High switching cost gives vendor leverage; budget exposure | Negotiate escalation cap |
| Immediate suspension on disputed amount (18) | Strong Push | Disproportionate remedy; business-blocking | Limit to undisputed amounts |
| One-sided indemnity (10) | Strong Push | Reciprocity is reasonably expected for a SaaS platform | Add Provider IP indemnity |
| No DPA / breach-notice timeline (8) | Strong Push | Data-handling exposure; likely regulatory relevance | Require DPA addendum |
| 90-day non-renewal notice (2) | Business Call | Manageable with a tracked calendar reminder | Shorten if leverage allows; otherwise diary |
| No insurance requirement (12) | Acceptable if Balanced | Lower priority if liability terms improve | Add if cap stays low |
| Provider feature-modification right (3) | Low Priority | Common in SaaS; full removal of needed feature is the real concern | Seek notice for material changes |
| Provider's home-forum venue (16) | Do Not Spend Leverage | Common in vendor forms; limited practical effect here | Accept unless other terms unresolved |

### 7. Market Practice Notes

- Liability caps tied to a short fee-measurement period and the absence of standard cap carve-outs are characterized as **Aggressive** for a customer — **Needs Attorney Confirmation**; AgentCounsel supplies no market data, and Northwind has provided no playbook or comparables.
- A Customer Data license extending to service "improvement" is characterized as **Depends on Leverage** and **Needs Attorney Confirmation**.
- Mutual consequential-damages waivers are **Common**, but the lack of carve-outs alongside a low cap is **Aggressive** — **Needs Attorney Confirmation**.
- Every characterization above is flagged for attorney verification: none is backed by a playbook, comparable, prior counterparty form, or attorney-supplied norm.

### 8. Prioritized Issue List

**High priority**

1. **Liability cap and carve-outs (11b–11d).** Why it matters: a ~$30K cap with no carve-outs leaves Northwind unable to recover meaningfully for a data breach or indemnity claim.
   - *Preferred Position:* Cap at 12 months' fees with mutual carve-outs (IP indemnity, breach of confidentiality, data-security breach, fraud, willful misconduct).
   - *Fallback Position:* Cap with a fixed dollar floor and carve-outs limited to data breach and willful misconduct.
   - *Suggested Redline Direction:* Raise the cap base, add a mutual carve-out list, and preserve consequential damages for carved-out claims.
2. **Data export / transition on termination (15).** Why it matters: without an export right, Northwind could lose access to its own operational data.
   - *Preferred Position:* 60-day post-termination export window plus reasonable transition assistance.
   - *Fallback Position:* 30-day export window in a standard format; assistance at Provider's hourly rate.
   - *Suggested Redline Direction:* Add a survival clause guaranteeing export access before any deletion.
3. **Customer Data "improvement" license (5).** Why it matters: an "improve the services" license may permit using Northwind data to train Provider models.
   - *Preferred Position:* License limited to delivering and supporting the services to Northwind.
   - *Fallback Position:* Permit aggregated, de-identified analytics only, with training expressly excluded.
   - *Suggested Redline Direction:* Narrow the license grant and add an express no-training statement.
4. **Suspension on disputed amounts (18).** Why it matters: service could be cut off over a good-faith billing dispute.
   - *Preferred Position:* Suspension only for undisputed amounts overdue 30+ days after notice.
   - *Fallback Position:* Suspension only after notice and a cure period, excluding amounts disputed in good faith.
   - *Suggested Redline Direction:* Condition suspension on undisputed, overdue amounts and prior written notice.

**Medium priority**

5. **Uncapped renewal price increase (4).**
   - *Preferred Position:* Annual increases capped at a fixed percentage.
   - *Fallback Position:* Increases capped at a published inflation index.
   - *Suggested Redline Direction:* Insert an escalation ceiling tied to renewal notice.
6. **One-sided indemnity (10).**
   - *Preferred Position:* Mutual indemnities; Provider covers third-party IP claims against the platform.
   - *Fallback Position:* Provider IP indemnity with a standard modification/misuse exclusion.
   - *Suggested Redline Direction:* Add a reciprocal Provider indemnity and narrow Customer's indemnity.
7. **No DPA / breach-notice timeline (8).** Add a DPA addendum with a defined breach-notification window and deletion-on-termination duty.
8. **Provider-only termination for convenience (14).** Add a reciprocal Customer right.

**Low priority**

9. 90-day non-renewal notice — diary a reminder if not shortened. 10. No insurance requirement — add if liability terms remain weak. 11. Provider feature-modification right — seek notice of material changes.

### 9. Missing Provisions

| Missing Provision | Risk of Absence | Severity | Recommendation |
|---|---|---|---|
| Service-level / uptime commitment | No performance floor or remedy for downtime | Med | Add uptime SLA with service credits |
| Insurance requirement | No recourse if Provider is uninsured | Med | Add minimum coverage + certificate |
| Data export / transition assistance | Loss of access to Northwind's own data | High | Add export window + transition terms |
| Force majeure | Unclear allocation of extraordinary-event risk | Low | Add a mutual force majeure clause |
| Audit / verification rights | Cannot verify security or data-handling compliance | Med | Add limited audit or third-party-report right |

### 10. Internal Consistency Check

- The cover page refers to "Order Form" while the body uses "Order Schedule" — `[CONFIRM: intended single defined term.]`
- "Affiliate" is defined but never used; affiliate-use rights are unaddressed in the body.
- A cross-reference in the Termination section points to "Section 9 (Fees)," but Fees appears under a different number — `[CONFIRM: corrected cross-reference.]`
- Exhibits A and B are referenced; no exhibits were attached to the provided document — `[CONFIRM: missing exhibits.]`

### 11. Business-Friendly Summary

This is Cirrus's standard customer contract, and it leans in the vendor's favor in ways worth pushing back on before signing. The four things that matter most: (1) if something goes badly wrong — for example a data breach — the contract limits what Northwind could recover to roughly three months of fees, which is small against the deal size; (2) there is no guaranteed way to get Northwind's own data back out when the contract ends; (3) the contract may let Cirrus use Northwind's data to "improve" its product, which could include training; and (4) Cirrus could shut off access over a billing dispute. None of these is necessarily a deal-breaker, but each is a reasonable ask. The main business tradeoff is how hard to push on price-increase caps versus other terms, given the cost of switching platforms later. Nothing here clearly stops the deal — but the liability and data-export points should be resolved before signature.

### 12. Open Items for Attorney Verification

- [ ] Confirm the correct Northwind entity, authorized signatory, and effective date.
- [ ] Confirm governing law and venue are appropriate `[verify jurisdiction]`.
- [ ] Verify the limitation-of-liability quotations (11a–11d) verbatim against the source document.
- [ ] Confirm whether the Customer Data license extends to model training.
- [ ] Assess applicable data-privacy regimes — not performed by this skill.
- [ ] Confirm ownership of Customer-built dashboard configurations.
- [ ] Resolve internal-consistency items (defined-term mismatch, broken cross-reference, missing exhibits).
- [ ] Confirm whether the liability allocation is acceptable given Northwind's insurance `[ATTORNEY TO CONFIRM]`.
- [ ] Independently verify every market-practice characterization in Section 7.
- [ ] Resolve all `[CONFIRM: ...]` placeholders before reliance.

### 13. Assumptions

- Assumed the document provided is the complete current MSA; no exhibits were attached.
- Assumed Northwind is the customer and Cirrus is the SaaS vendor, per the deal lead's instructions.
- Assumed an approximate $360,000 three-year transaction value, as provided by Jordan Avery.
- Assumed the platform will ingest Northwind customer and employee data, per the business context given.
- Assumed this is Cirrus's unmodified standard form; no Northwind playbook or comparable contracts were supplied.
- No assumptions were made about governing law, market norms, or regulatory requirements; those are flagged for attorney verification.
