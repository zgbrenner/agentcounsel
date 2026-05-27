# DPA Review — Vendor Form, Controller Side, Healthcare Context

> **Draft attorney work product. Not legal advice.** This draft is for attorney review and is not a clearance to sign. Privacy and sector-specific frameworks are flagged for verification; the skill does not assert which law applies.

## 1. Summary

- **Document:** Data Processing Addendum (DPA) on the vendor's form.
- **Client role:** Controller (per the document and the user's framing).
- **Vendor role:** Processor.
- **Main agreement:** SaaS subscription contract — provided alongside the DPA.
- **Processing scope:** Patient health records and appointment data for a healthcare client.
- **Posture:** Issues list; not a sign / do-not-sign clearance.

## 2. Sectoral Overlay Check — TRIGGERED

The processing covers patient health records. This **may implicate sector-specific regimes** that go beyond a general privacy framework (for example, healthcare-specific obligations on covered entities, business associates, or processors). The skill does **not** assert which regime applies. The sectoral overlay is flagged for specialist review by privacy and healthcare counsel.

- `[CONFIRM: applicable sectoral privacy/healthcare regime — for example, any health-information framework, sector-specific requirements, and any state-specific overlay]`.
- `[CONFIRM: any required business-associate or processor agreement under the applicable healthcare framework]`.

## 3. Risk Table

| # | Issue | What the DPA Says | Risk (Controller Side) | Severity | Suggested Direction |
|---|---|---|---|---|---|
| 1 | Breach-notification timeframe | Notice within a fixed number of business days | The fixed timeframe is recorded as drafted; the skill does not characterize whether it satisfies any statutory deadline | High — **floor maintained** | Add `[CONFIRM: applicable statutory or contractual notice window]`; do not assume a regulatory clock |
| 2 | Sub-processor appointment | Broad processor discretion; no objection mechanism | Controller has no ability to object to or block new sub-processors | High — **floor maintained** | Add advance notice + Controller objection right; obligate processor to flow down DPA terms |
| 3 | Controller / processor role labels | Document labels Controller as controller and Vendor as processor | Role labels are not conclusive; the framework's role definitions govern | High — flagged for verification | `[CONFIRM: role designations under the applicable framework]` |
| 4 | International transfer mechanisms | Not specified in the provided text | `[CONFIRM: whether any cross-border transfer is in scope]` | Medium | Add transfer-mechanism representations as applicable |
| 5 | Audit and assistance rights | Limited audit; no specified deadline for assistance | Controller has limited verification rights | Medium | Strengthen audit and assistance language |

The High-severity floor is observed: no item in this table has been downgraded without an explicit attorney rationale.

## 4. Missing or Underspecified Terms

- Specific statutory or contractual breach-notification clock — `[CONFIRM]`.
- Sub-processor objection mechanism.
- Deletion / return obligations and timeline on termination.
- International transfer mechanism, where applicable `[CONFIRM]`.

## 5. Open Items for Attorney Verification

- [ ] Confirm applicable privacy framework(s) `[verify jurisdiction]`.
- [ ] Confirm applicable sectoral healthcare regime and any business-associate agreement requirements.
- [ ] Verify whether the document's role labels (controller / processor) are correct under the applicable framework.
- [ ] Confirm the operative breach-notification deadline `[CONFIRM]`; do not rely on the contract's days-of-business window as a statutory deadline.
- [ ] Confirm whether any High-severity rating should be adjusted — only with an explicit, attributed attorney decision documented in the file.
- [ ] Resolve all `[CONFIRM]` placeholders before reliance.

## 6. Recommendations

The skill recommends framing this as an **issues list for negotiation**, not a sign-off. Privacy counsel review is required before the DPA is countersigned.

## 7. Assumptions

- Assumed the client is the controller and the vendor is the processor, per the user's framing and the document's labels. Verification under the applicable framework is flagged separately.
- Assumed the DPA text provided is the complete current version.
- Assumed the healthcare context provided is accurate; this is the basis for triggering the sectoral overlay check.
- No assumptions made about which privacy framework applies; those are flagged for attorney verification.
