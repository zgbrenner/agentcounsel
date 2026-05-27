# Compliance Gap Matrix — Regulation vs. Current Controls

> **Draft for attorney review. Not legal advice.** This is draft attorney work product. Every classification is a workflow assessment subject to attorney verification, not a binding legal conclusion. The skill does not assert legal liability or enforcement outcomes.

## 1. Sources

- **Requirement source:** Text of the regulation provided by the user, with numbered provisions.
- **Controls source:** User-provided narrative description of current controls, policies, and systems.
- **Organization context:** Mid-size licensed entity (regulatory status as stated).

## 2. Methodology Note

Each requirement traces to a specific numbered provision in the provided source. No requirement has been added from background knowledge. Classifications are workflow assessments subject to attorney verification and are not binding conclusions about legal compliance.

## 3. Status Definitions

- **Met (apparent):** The described control appears to address the requirement; not a confirmation of legal compliance.
- **Partial:** The described control addresses part of the requirement.
- **Gap:** No described control addresses the requirement.
- **Not applicable:** The requirement does not appear to apply to this entity in this regulatory status `[CONFIRM]`.

## 4. Gap Matrix

| # | Source Provision | Requirement (paraphrased from the provided text — verify against source) | Current Control (from user description) | Status | Severity | Notes |
|---|---|---|---|---|---|---|
| 1 | § 101(a) | Provision text as quoted in the user-provided source | Described control matches scope | Met (apparent) | — | Verify wording vs. source. |
| 2 | § 101(b) | Provision text as quoted in the user-provided source | Described control addresses part of the requirement; reporting cadence is unspecified | Partial | Medium | `[CONFIRM: reporting cadence required by the rule]`. |
| 3 | § 102 | Provision text as quoted in the user-provided source | No described control | Gap | High | Remediation framing below. |
| 4 | § 103(a) | Provision text as quoted in the user-provided source | Described control addresses scope but no documentation | Partial | Medium | Documentation gap. |
| 5 | § 104 | Provision text as quoted in the user-provided source | No described control | Gap | High | Remediation framing below. |

## 5. Severity Methodology

- Severity is assigned to **Partial** and **Gap** items only. Met items carry no severity.
- Severity reflects the workflow's prioritization, not enforcement likelihood. The skill does not assert penalty exposure.

## 6. Remediation Framing

- **§ 102 (Gap, High):** Build a control aligned to the provision's scope; identify an owner; document the control; schedule a periodic review.
- **§ 104 (Gap, High):** Confirm whether an internal program area owns the underlying activity; if no owner exists, assign one before drafting the control.
- **§ 101(b) (Partial, Medium):** Confirm cadence required by the rule; align internal reporting accordingly.
- **§ 103(a) (Partial, Medium):** Document the existing control; align documentation to the rule's documentation expectations.

The framing is process-level, not legal advice. The skill does not prescribe specific legal steps.

## 7. Open Items for Attorney Verification

- [ ] Verify every paraphrase against the source-provision text.
- [ ] Confirm that the entity's regulatory status correctly maps to the obligations identified.
- [ ] Attorney sign-off on each Met classification before relying on it as compliance.
- [ ] Attorney evaluation of enforcement risk — **not characterized by this skill**.
- [ ] Confirm jurisdiction-specific application `[verify jurisdiction]`.
- [ ] Resolve all `[CONFIRM]` placeholders before reliance.

## 8. Assumptions

- Assumed the regulatory text provided is the operative version.
- Assumed the user's description of current controls is materially complete; further controls may exist that were not described.
- Assumed the entity's stated regulatory status; the skill does not verify it.
- No assumptions made about whether any control satisfies a legal requirement as a binding conclusion; those are flagged for attorney verification.
