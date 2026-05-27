# Contract Risk Review — Vendor MSA

> **Draft for attorney review. Not legal advice.** Prepared from the contract text provided by the deal lead. This document is draft attorney work product and is not a substitute for a licensed attorney's judgment. All section references and quotations must be verified against the source document before reliance.

## 1. Document Summary

- **Document:** Master Services Agreement (22 pages), counterparty's standard form.
- **Client role:** Customer (buyer).
- **Approximate contract value:** $250,000 / year.
- **Effective date:** `[CONFIRM: effective date]`.
- **Governing law / forum:** `[CONFIRM: governing law and venue — not located in the provided text]`.
- **Form profile:** Vendor's unmodified standard form — review at heightened scrutiny.

## 2. Structural Map

Present: Services, Fees, IP, Confidentiality, Liability, Termination.
Absent: Insurance, SLA, data export on termination, force majeure, audit rights.

## 3. Red Flags Quick Scan

- Liability cap tied to 3 months of fees with no carve-outs.
- Mutual consequential-damages waiver with no exceptions.
- Auto-renewal for successive 12-month terms with a 90-day non-renewal window.
- No transition assistance or data return obligation on termination.

## 4. Clause-by-Clause Summary

- **Term & renewal** — Auto-renews 12 months; 90-day non-renewal window.
- **Fees & payment** — Net-30; renewal increases not capped.
- **IP & license grant** — Provider retains platform IP; Customer Data licensed for service delivery and "improvement" `[CONFIRM: whether "improvement" extends to training]`.
- **Limitation of liability** — Decomposed below (rows 11a–11d in the risk matrix).
- **Termination** — Provider may terminate for material breach on short notice; no Customer parity.
- **Indemnification** — One-sided; Customer indemnifies Provider; no reciprocal Provider IP indemnity.

## 5. Risk Matrix

| # | Clause | Direct vs. Consequential | Cap Base | Carve-Outs | Allocation | Legal Risk | Business Friction |
|---|---|---|---|---|---|---|---|
| 11a | LoL — direct/indirect | Mutual consequential waiver | N/A | None | Symmetrical but undifferentiated | High | None |
| 11b | LoL — cap amount | Cap = fees paid in prior 3 months | ~$62K against $250K deal | None | Materially underprotects Customer | High | None |
| 11c | LoL — carve-outs | None | N/A | Indemnity, breach, willful misconduct all capped | Significant downside exposure | High | None |
| 11d | LoL — overall allocation | Small cap + no carve-outs + mutual consequential waiver | N/A | N/A | Insurance-style transfer of risk to Customer | High | None |
| 2 | Term & renewal | — | — | — | 90-day window vs. 12-month renewal | Medium | Slowing |
| 5 | IP — Customer Data license | — | — | — | Possible model-training exposure | Medium | Confusing |
| 14 | Termination | — | — | — | Asymmetric for-cause rights | Medium | Slowing |

## 6. Prioritized Issue List

**High priority**

1. **Liability cap and carve-outs (11b–11d).**
   - *Preferred Position:* Cap at 12 months' fees with mutual carve-outs (IP indemnity, breach of confidentiality, data-security breach, fraud, willful misconduct).
   - *Fallback Position:* Cap with a fixed dollar floor and carve-outs limited to data breach and willful misconduct.
   - *Suggested Redline Direction:* Raise the cap base, add a mutual carve-out list, preserve consequential damages for carved-out claims.
2. **Auto-renewal mechanism and 90-day notice window (2).** Tracked risk.
   - *Suggested Redline Direction:* Add a calendar-triggered exit option and shorten the non-renewal window.

**Medium priority**

3. **Customer Data "improvement" license (5).** Narrow license scope; exclude training expressly.
4. **One-sided indemnity (10).** Add reciprocal Provider IP indemnity.

## 7. Market Practice Notes

- A 3-month fee cap is characterized as **Aggressive** for a customer — **Needs Attorney Confirmation**. AgentCounsel supplies no market data, and no playbook or comparables were provided.

## 8. Missing Provisions

| Missing Provision | Risk of Absence | Severity | Recommendation |
|---|---|---|---|
| Service-level / uptime commitment | No performance floor | Med | Add uptime SLA with service credits |
| Insurance requirement | No recourse if Provider uninsured | Med | Add minimum coverage |
| Data export on termination | Loss of operational data | High | Add export window + transition assistance |
| Force majeure | Unclear extraordinary-event allocation | Low | Add mutual clause |

## 9. Missing Provisions Section / Internal Consistency Check

- "Order Form" and "Order Schedule" both appear — `[CONFIRM: intended single defined term]`.
- Exhibits A and B referenced; no exhibits attached — `[CONFIRM: missing exhibits]`.

## 10. Business-Friendly Summary

The contract leans heavily toward the vendor. The biggest single issue is the liability cap: at three months of fees, the maximum recoverable amount is small relative to the deal value. The data-export gap is the second priority. Neither is a deal-breaker, but each is a reasonable ask before signature.

## 11. Open Items for Attorney Verification

- [ ] Confirm governing law and venue `[verify jurisdiction]`.
- [ ] Verify all clause quotations against the source document.
- [ ] Confirm whether the Customer Data "improvement" license extends to model training.
- [ ] Confirm acceptable liability allocation given Customer's insurance posture `[ATTORNEY TO CONFIRM]`.
- [ ] Independently verify every market-practice characterization in Section 7.
- [ ] Resolve all `[CONFIRM]` placeholders before reliance.

## 12. Assumptions

- Assumed the document provided is the complete current MSA; no exhibits were attached.
- Assumed the client is the customer and the counterparty is the SaaS vendor.
- Assumed an approximate $250,000 annual contract value, as stated by the deal lead.
- No assumptions were made about governing law or market norms; those are flagged for attorney verification.
