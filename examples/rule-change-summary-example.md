# Example: Rule Change Summary

> **Illustrative example — not legal advice.** This is a sample of what the Rule Change Summary skill (`skills/regulatory/rule-change-summary/SKILL.md`) produces. The agency, the rule, its sections, its docket number, and every date and quotation in it are **fictional** and were invented for illustration. **No real regulation, citation, or agency guidance is stated.** Wherever a real published citation or effective date would appear, the example carries a visible `[VERIFY]` / `[Verify current law]` / `[CONFIRM]` placeholder. It is the kind of draft work product a compliance attorney would review — not a finished deliverable, and not legal advice. See `examples/README.md`.

## Scenario

The **Bureau of Consumer Data Protection ("BCDP")** is a **fictional** regulatory agency. In this scenario it has issued a **final rule amending its (fictional) Consumer Data Safeguards Rule**, and the compliance team at **Riverbend Financial Services, Inc.** — a fictional mid-size consumer-lending fintech that collects account, identity, and transaction data from individual borrowers — provided the rule document and asked for a structured first-pass summary to brief leadership before commissioning a full gap review. Because this is an illustrative example, no real rule text exists: the summary is built entirely from a made-up document, and the skill's discipline is on display — everything is drawn from "the provided document," every date is flagged for confirmation against the source, and no real citation is asserted. This example shows the summary structure and the impact table, not any actual regulatory requirement.

## Illustrative Output

**DRAFT RULE CHANGE SUMMARY — FOR ATTORNEY REVIEW ONLY**

> Draft legal work product for attorney review. Not legal advice. Prepared solely from the document provided. No effective date, obligation, or citation below has been verified against an authoritative source; each is flagged for attorney confirmation. This summary asserts no conclusion about whether Riverbend is or is not in compliance.

### 1. Document Identification

- **Issuing body:** Bureau of Consumer Data Protection (BCDP) `[CONFIRM: issuing agency as stated on the document]`
- **Document type:** Final rule `[CONFIRM: proposed / final / interim final — confirm from the document's caption]`
- **Title:** "Amendments to the Consumer Data Safeguards Rule" `[CONFIRM: exact title copied from the document]`
- **Docket / citation:** Docket No. `[CONFIRM: docket number copied exactly from the document]`; published-citation `[VERIFY: publication citation against source — do not supply independently]`
- **Issuance / publication date:** `[CONFIRM date against source text]`
- **Document status:** Final rule as provided `[CONFIRM: whether any correction, stay, or subsequent guidance has since issued — operative status is an attorney item; a published final rule can be stayed, enjoined, withdrawn, or superseded]` `[Verify current law]`

### 2. Stated Purpose and Scope

Per the document's stated rationale, the Bureau is amending the Consumer Data Safeguards Rule to "strengthen the administrative, technical, and physical safeguards that covered entities maintain for consumer financial data" and to "standardize incident-reporting expectations." `[CONFIRM: quotation against source text.]` The document states it applies to "covered entities that collect or maintain consumer financial data in the course of offering a consumer financial product or service." `[CONFIRM: scope language against source; whether Riverbend is a "covered entity" is an applicability question for counsel — see Section 5.]`

### 3. What Changed

*No prior-rule baseline text was provided. The following reflects only what the document itself describes as new or modified; a full "what changed" comparison requires the prior rule text.* `[CONFIRM: obtain prior rule for a complete comparison.]`

- The document describes a **new requirement to designate a qualified individual** to coordinate the safeguards program (framed as new). `[CONFIRM: against source.]`
- The document describes an **expanded written-program requirement** with enumerated elements (framed as modified/expanded). `[CONFIRM.]`
- The document describes a **new incident-reporting obligation** with a fixed outer time limit (framed as new). `[CONFIRM.]`
- The document describes **extended recordkeeping** for program documentation (framed as modified). `[CONFIRM.]`

### 4. Key Dates

*Every date below is drawn from the provided document and is unverified. No date has been computed or interpolated.*

| Date | Description | Source location in document | Flag |
|---|---|---|---|
| `[CONFIRM date]` | Effective date of the amended rule | `[CONFIRM: § / preamble ref]` | `[CONFIRM date against source]` |
| `[CONFIRM date]` | General compliance date | `[CONFIRM: § ref]` | `[CONFIRM date against source]` `[deadline verification required]` |
| `[CONFIRM date]` | Phase-in compliance date for the incident-reporting obligation | `[CONFIRM: § ref]` | `[CONFIRM date against source]` `[deadline verification required]` |
| N/A | Comment deadline | N/A — document presented as a final rule | `[CONFIRM: whether a comment period applies]` |

### 5. Applicability to This Organization

Given Riverbend's described business (consumer lending; collection of account, identity, and transaction data from individual borrowers), the following appear likely within scope, subject to attorney confirmation:

- Riverbend's collection and maintenance of consumer financial data appears to fall within the document's "covered entity" description. `[ATTORNEY TO CONFIRM: whether Riverbend meets the definition of "covered entity" under the amended Rule — verify jurisdiction and definitional scope.]`
- Whether any small-entity, threshold, or activity-based exemption applies is not determinable from the scope prose alone. `[ATTORNEY TO CONFIRM: exemptions and thresholds.]`
- Whether Riverbend's third-party service providers are independently covered, or covered through Riverbend's oversight obligations, is unresolved. `[ATTORNEY TO CONFIRM: service-provider scope.]`

### 6. New and Modified Obligations

*Extracted as discrete obligations from the document as provided. Operative language is quoted where precision matters; each quotation is flagged for verification against the source.*

1. **Designate a qualified individual.** The document requires each covered entity to "designate a qualified individual responsible for overseeing and implementing the safeguards program." `[CONFIRM: quotation and section — § ref.]`
2. **Maintain a written safeguards program.** The document requires a written program "based on a documented risk assessment" addressing enumerated administrative, technical, and physical safeguards. `[CONFIRM: enumerated elements against source.]`
3. **Provide periodic reporting to governance.** The document requires the qualified individual to "report in writing, at least annually," to the entity's governing body. `[CONFIRM: frequency and audience against source.]`
4. **Report qualifying incidents within a fixed window.** The document requires notification to the Bureau of a "qualifying data incident" within a stated outer time limit. `[CONFIRM: definition of "qualifying data incident" and the exact time limit against source — do not compute or assume the deadline.]` `[deadline verification required]`
5. **Retain program records.** The document requires retention of program documentation for a stated period. `[CONFIRM: retention period against source.]`

*Any obligation whose scope reads ambiguously in the provided text is flagged in Section 8.*

### 7. Implementation Considerations

*Preliminary observations only — not a compliance roadmap. Attorney to evaluate and prioritize.*

- **Governance:** identifying and formally designating the "qualified individual"; establishing the annual written report to the governing body.
- **Policy:** updating or creating the written safeguards program and the underlying risk-assessment methodology.
- **Systems / security:** mapping current technical and physical safeguards to the enumerated elements to see where changes may be needed.
- **Incident response:** revising the incident-response plan to align with the reporting trigger and time limit `[CONFIRM]`.
- **Recordkeeping:** aligning document-retention practices with the stated retention period.
- **Third-party contracts:** reviewing service-provider agreements for flow-down of the safeguards and incident-reporting expectations.
- **Training:** briefing relevant staff on the new designation, reporting, and incident-notification steps.

### 8. Open Questions and Interpretive Issues

- What is the precise definition of "qualifying data incident," and does it turn on likelihood of harm, number of records, or data type? `[ATTORNEY TO CONFIRM.]`
- Does "qualified individual" require particular credentials, or may the role be outsourced? `[ATTORNEY TO CONFIRM.]`
- Does the annual-reporting obligation apply to a board, a committee, or senior management? `[CONFIRM against source.]`
- How do the general compliance date and the incident-reporting phase-in date interact for an entity onboarding after the effective date? `[ATTORNEY TO CONFIRM — no dates computed here.]`
- Does the amended Rule preempt, supplement, or run parallel to any other applicable data-safeguards regime? `[ATTORNEY TO CONFIRM — conflict/overlap analysis.]` `[Verify current law]`

### 9. Impact Summary Table

*At-a-glance view of the obligations extracted. "Status" is "attorney to assess" for every row; nothing below is a compliance conclusion.*

| Obligation / Change | Source (doc section) | Affected Function | Effective/Compliance Date | Status |
|---|---|---|---|---|
| Designate qualified individual | `[CONFIRM: § ref]` | Governance / Security leadership | `[CONFIRM date]` | Attorney to assess |
| Written safeguards program (expanded elements) | `[CONFIRM: § ref]` | Compliance / InfoSec | `[CONFIRM date]` | Attorney to assess |
| Annual written report to governing body | `[CONFIRM: § ref]` | Governance / Board | `[CONFIRM date]` | Attorney to assess |
| Incident reporting within fixed window | `[CONFIRM: § ref]` | Incident response / Legal | `[CONFIRM date]` `[deadline verification required]` | Attorney to assess |
| Program recordkeeping / retention | `[CONFIRM: § ref]` | Records / Compliance | `[CONFIRM date]` | Attorney to assess |
| Service-provider oversight / flow-down | `[CONFIRM: § ref]` | Vendor management / Legal | `[CONFIRM date]` | Attorney to assess |

### 10. Attorney Verification Items

See the Attorney Verification Checklist below.

---

## Attorney Verification Checklist

- [ ] The document provided is the authoritative, final version; no subsequent amendments, corrections, or agency guidance have been issued.
- [ ] All dates (effective date, compliance date, comment deadline, phase-in milestones) have been verified against the source document and, where applicable, the Federal Register or official agency publication.
- [ ] The document citation, docket number, and title are accurate and complete.
- [ ] The "what changed" comparison is based on the actual prior rule text, not a summary or recollection.
- [ ] The applicability assessment has been confirmed by an attorney with subject-matter expertise; no applicability conclusion has been accepted as final from this draft alone.
- [ ] Each discrete obligation listed accurately reflects the rule text; no obligation was misstated through paraphrase.
- [ ] All interpretive questions and open items have been resolved or escalated appropriately before the summary is relied upon for compliance planning.
- [ ] No rule text, penalty provision, or agency interpretation was assumed from model background knowledge without verification against the provided document.
- [ ] The organization's actual activities have been mapped against the rule's scope by a qualified attorney, not solely by this summary.
- [ ] The draft is labeled appropriately and has not been transmitted to any third party without attorney review and approval.

---

*This example is illustrative and built on a fictional agency and rule. It demonstrates the structure and discipline of the Rule Change Summary skill; it is not legal advice and states no real regulatory requirement. Run the skill on the actual document in your matter and have a qualified attorney verify every citation, date, and obligation against the source.*
