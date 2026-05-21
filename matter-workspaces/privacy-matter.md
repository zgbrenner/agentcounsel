> **Blank template — contains no client facts.** Once populated with matter-specific information this file becomes **draft legal work product for attorney review**. It may be protected by the attorney-client privilege and/or the attorney work-product doctrine. Label and access-limit the populated copy accordingly. This is not legal advice.
>
> Privilege designation (populated copy): `[CONFIRM: attorney to designate — e.g., Privileged & Confidential — Attorney Work Product]`

---

# Privacy Matter Workspace

## Matter Header

| Field | Value |
|---|---|
| Matter Name | `[CONFIRM: matter name]` |
| Matter / File # | `[CONFIRM: matter number]` |
| Client | `[CONFIRM: client full legal name and entity type]` |
| Responsible Attorney | `[CONFIRM: attorney name and bar admission]` |
| Practice Profile in Use | `[CONFIRM: e.g., privacy]` |
| Date Opened | `[CONFIRM: date]` |
| Matter Type | `[CONFIRM: e.g., Privacy Event / Data Breach / DSAR / Processing Activity Review / Vendor DPA / Privacy Program Assessment]` |
| Status | `[CONFIRM: e.g., Active — Investigation / Active — Notification / Active — DSAR Response / Closed]` |

---

## 1. Parties

| Party Name | Entity Type | Role | Aliases / Related Entities | Counsel (if known) |
|---|---|---|---|---|
| `[CONFIRM: client name]` | `[CONFIRM: e.g., corporation, LLC]` | Client / `[CONFIRM: controller / processor / joint controller]` | `[CONFIRM: affiliates, trade names]` | Responsible attorney above |
| `[CONFIRM: counterparty or processor name]` | `[CONFIRM: entity type]` | `[CONFIRM: processor / sub-processor / controller / third party]` | `[CONFIRM: aliases]` | `[CONFIRM: if known]` |
| `[CONFIRM: regulator — if applicable]` | `[CONFIRM: government body]` | Supervisory Authority / Regulator | — | — |
| `[CONFIRM: data subject(s) — describe generally, do not list individuals in a template]` | Individual(s) | Data Subject(s) | — | `[CONFIRM: if represented]` |

---

## 2. Processing Activity or Privacy Event Description

> Record only facts provided by the client or established by a source document. Label each fact with its source. Do not characterize legal obligations in this section — that is attorney analysis to be produced separately.

| Field | Value |
|---|---|
| Description of Activity or Event | `[CONFIRM: plain-language description of the processing activity reviewed or the privacy event that occurred]` |
| Date of Event (if applicable) | `[CONFIRM: date — if known]` [deadline verification required] |
| Date Client Became Aware | `[CONFIRM: date — if known]` [deadline verification required] |
| Source of Information | `[CONFIRM: client report, IT investigation, third-party notice, regulatory inquiry, etc.]` |
| Systems / Platforms Involved | `[CONFIRM: describe systems, applications, or platforms involved]` |
| Internal Incident Reference | `[CONFIRM: internal ticket or reference number, if applicable]` |

**Assumptions (not confirmed facts):**

| # | Assumption | Effect on Analysis if Wrong |
|---|---|---|
| 1 | `[CONFIRM: describe assumption]` | `[CONFIRM: describe effect]` |
| 2 | | |

---

## 3. Data Categories and Data Subjects

> Complete for each category of personal data involved. Do not record actual personal data here.

| # | Data Category | Description | Approximate Volume | Data Subject Population | Sensitivity Level | Special Category? |
|---|---|---|---|---|---|---|
| 1 | `[CONFIRM: e.g., contact information]` | `[CONFIRM: describe]` | `[CONFIRM: approximate number of records or individuals]` | `[CONFIRM: e.g., customers, employees, EU residents]` | `[CONFIRM: Standard / Elevated / High]` | `[CONFIRM: Y / N — verify jurisdiction for special category definition]` |
| 2 | | | | | | |
| 3 | | | | | | |

**Note:** Characterization of data sensitivity and special categories depends on applicable law in each relevant jurisdiction. These classifications require attorney confirmation. `[verify jurisdiction]`

---

## 4. Controller, Processor, and Sub-Processor Roles

| Entity | Asserted Role | Role Confirmed? | Legal Basis for Role | Data Processing Agreement in Place? |
|---|---|---|---|---|
| `[CONFIRM: client name]` | `[CONFIRM: controller / processor / joint controller]` | `[CONFIRM: attorney to confirm — verify jurisdiction]` | `[CONFIRM: contractual, statutory, or other basis — attorney to assess]` | See Section 9 |
| `[CONFIRM: vendor / processor]` | `[CONFIRM: processor / sub-processor]` | `[CONFIRM: attorney to confirm]` | `[CONFIRM]` | `[CONFIRM: Y / N — if Y, reference in documents index]` |
| `[CONFIRM: additional parties]` | | | | |

_Role determinations require attorney assessment under applicable privacy law. `[verify jurisdiction]`_

---

## 5. Jurisdiction, Governing Law, and Posture

> Required by `core/jurisdiction-and-deadline-gates.md` — Gate 1. Complete before substantive analysis.

| Field | Value |
|---|---|
| Jurisdiction(s) | `[CONFIRM: country, state/province, and regulatory regime — may be multiple]` |
| Applicable Privacy Frameworks | `[CONFIRM: attorney to identify — do not cite specific statute or rule; flag for attorney to confirm]` [verify jurisdiction] |
| Governing Law (if contractual matter) | `[CONFIRM: as stated in relevant agreement or to be determined]` |
| Client's Primary Regulatory Domicile | `[CONFIRM: where client is established or primarily supervised for privacy purposes — verify jurisdiction]` |
| Cross-Border Data Transfers Involved? | `[CONFIRM: Y / N — if Y, see Section 8]` |
| Procedural Posture | `[CONFIRM: e.g., internal review, regulatory inquiry, enforcement proceeding, litigation, DSAR response, breach notification]` |
| Client Posture | `[CONFIRM: e.g., self-assessment / responding to regulator / responding to data subject / defending claim]` |
| Analysis "As Of" Date | `[CONFIRM: date of this workspace entry]` |
| Open Jurisdiction Issues | `[CONFIRM: describe any unresolved jurisdiction or applicable-law questions]` |

---

## 6. Documents Index

| # | Document Name / Description | Date | Version | Location / File Path | Relevance |
|---|---|---|---|---|---|
| 1 | `[CONFIRM: e.g., data processing agreement with vendor]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM: controller/processor relationship]` |
| 2 | `[CONFIRM: e.g., privacy policy]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 3 | `[CONFIRM: e.g., data breach incident report]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 4 | `[CONFIRM: e.g., DSAR request letter]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 5 | | | | | |

---

## 7. Deadlines and Key Dates

> **Gate 2 — Required by `core/jurisdiction-and-deadline-gates.md`.** Every date in this table must be independently verified by the responsible attorney. No date has been computed by any agent or tool. Do not rely on any date here without attorney confirmation. Privacy-related notification and response deadlines are jurisdiction-specific and consequence-bearing; attorney verification is critical.

| # | Date | Event / Deadline | Source | Verification Status |
|---|---|---|---|---|
| 1 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., regulatory breach notification deadline — if applicable]` | `[CONFIRM: source — e.g., date of awareness]` | `[CONFIRM: attorney to verify]` |
| 2 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., data subject notification deadline — if applicable]` | `[CONFIRM: source]` | `[CONFIRM: attorney to verify]` |
| 3 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., DSAR response deadline — if applicable]` | `[CONFIRM: date DSAR request received]` | `[CONFIRM: attorney to verify]` |
| 4 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., regulator response deadline — if applicable]` | `[CONFIRM: regulatory notice or inquiry]` | `[CONFIRM: attorney to verify]` |
| 5 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: additional deadline]` | `[CONFIRM: source]` | `[CONFIRM: attorney to verify]` |

**[CRITICAL — ATTORNEY TO VERIFY ALL DEADLINES]** Privacy notification and response deadlines vary significantly by jurisdiction, incident type, data category, and date of discovery. No deadline has been computed here. The responsible attorney must independently verify every deadline, including applicable tolling, extensions, and jurisdictional counting rules.

---

## 8. Cross-Border Data Transfer Considerations

> Complete if personal data is transferred across international or jurisdictional boundaries. If not applicable, mark as not applicable.

| Field | Value |
|---|---|
| Transfers Involved? | `[CONFIRM: Y / N — if N, mark section not applicable]` |
| Origin Jurisdiction(s) | `[CONFIRM: jurisdiction(s) from which data originates]` |
| Destination Jurisdiction(s) | `[CONFIRM: jurisdiction(s) to which data is transferred]` |
| Transfer Mechanism | `[CONFIRM: attorney to assess — do not identify specific mechanism; flag for attorney to confirm with applicable law]` [verify jurisdiction] |
| Adequacy or Equivalent Determination? | `[CONFIRM: attorney to assess — verify jurisdiction]` |
| Transfer Mechanism Status | `[CONFIRM: In Place / Not Yet Established / Under Review]` |
| Attorney Assessment Required | `[ATTORNEY TO CONFIRM: cross-border transfer legality and mechanism adequacy — verify jurisdiction]` |

_Reference: `skills/privacy/dpa-review/SKILL.md` for data processing agreement review where a transfer mechanism is part of a DPA._

---

## 9. DSAR Tracking

> Complete for each data subject access or rights request received. If not applicable, mark section as not applicable.

| # | Request Type | Date Received | Data Subject Identity Verified? | Deadline | Response Status | Response Date | Notes |
|---|---|---|---|---|---|---|---|
| 1 | `[CONFIRM: e.g., access, erasure, portability, rectification, objection]` | `[CONFIRM]` [deadline verification required] | `[CONFIRM: Y / N / Pending — attorney to confirm verification method]` | `[CONFIRM]` [deadline verification required] [CONFIRM: attorney to verify] | `[CONFIRM: Open / In Progress / Responded / Closed]` | `[CONFIRM: date if responded]` [deadline verification required] | |
| 2 | | | | | | | |

_Skills for DSAR work: `skills/privacy/dsar-workflow/SKILL.md`_

---

## 10. Breach and Notification Tracking

> Complete if a potential data breach or security incident is involved. If not applicable, mark section as not applicable.

| Field | Value |
|---|---|
| Incident Occurred? | `[CONFIRM: Y / Suspected / Under Investigation / N]` |
| Date of Incident | `[CONFIRM: date — if known]` [deadline verification required] |
| Date of Discovery / Awareness | `[CONFIRM: date]` [deadline verification required] |
| Nature of Incident | `[CONFIRM: e.g., unauthorized access, ransomware, accidental disclosure, lost device — based on information provided]` |
| Personal Data Affected | `[CONFIRM: reference Section 3 — data categories and approximate volume]` |
| Regulatory Notification Required? | `[CONFIRM: attorney to assess — verify jurisdiction]` [ATTORNEY TO CONFIRM: notification obligation determination] |
| Regulatory Notification Deadline | `[CONFIRM: attorney to verify]` [deadline verification required] [CONFIRM: attorney to verify] |
| Regulatory Notification Made? | `[CONFIRM: Y / N / Pending — date if made]` [deadline verification required] |
| Data Subject Notification Required? | `[CONFIRM: attorney to assess — verify jurisdiction]` [ATTORNEY TO CONFIRM: notification obligation determination] |
| Data Subject Notification Deadline | `[CONFIRM: attorney to verify]` [deadline verification required] [CONFIRM: attorney to verify] |
| Data Subject Notification Made? | `[CONFIRM: Y / N / Pending — date if made]` |
| Notification Work Product | `[CONFIRM: reference Work-Product Index, Section 11]` |

---

## 11. Work-Product Index

> Index every draft deliverable produced by an AgentCounsel skill for this matter. Each entry is draft legal work product for attorney review.

| # | Skill Used | Date Run | Output Description | File / Location | Attorney Reviewer | Review Status |
|---|---|---|---|---|---|---|
| 1 | `skills/privacy/dpa-review/SKILL.md` | `[CONFIRM: date]` | DPA review | `[CONFIRM: file path]` | `[CONFIRM]` | `[CONFIRM: Draft / Under Review / Adopted / Superseded]` |
| 2 | `skills/privacy/dsar-workflow/SKILL.md` | `[CONFIRM: date]` | DSAR response workflow | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 3 | `skills/privacy/pia-generation/SKILL.md` | `[CONFIRM: date]` | Privacy impact assessment draft | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 4 | `skills/privacy/privacy-policy-gap-review/SKILL.md` | `[CONFIRM: date]` | Privacy policy gap review | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 5 | `skills/legal-research/legal-research-memo/SKILL.md` | `[CONFIRM: date]` | Research memo | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |

---

## 12. Risk and Issue Summary

> This summary is based solely on information recorded in this workspace. It is draft legal work product for attorney review and is not a legal conclusion. The responsible attorney must review, correct, and adopt any risk characterization before it is relied upon.

| # | Issue / Risk | Category | Preliminary Assessment | Priority | Attorney Confirmation Status |
|---|---|---|---|---|---|
| 1 | `[CONFIRM: e.g., regulatory notification obligation — timing unclear]` | `[CONFIRM: e.g., Breach Notification, DSAR Compliance, Controller/Processor Role, Cross-Border Transfer]` | `[CONFIRM: preliminary notes — not a legal conclusion]` | `[CONFIRM: High / Medium / Low]` | `[ATTORNEY TO CONFIRM]` |
| 2 | | | | | |
| 3 | | | | | |

**Preliminary Risk Band:** `[CONFIRM: Low / Medium / High]` `[ATTORNEY TO CONFIRM: preliminary triage only — not a legal conclusion]`

---

## 13. Open Items and Action Items

| # | Item | Type | Owner | Due Date | Status |
|---|---|---|---|---|---|
| 1 | Verify all notification deadlines independently | `[ACTION]` | `[CONFIRM: responsible attorney]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 2 | Confirm controller/processor role determinations | `[ACTION]` | `[CONFIRM: responsible attorney]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 3 | Confirm applicable jurisdictions and privacy frameworks | `[ACTION]` | `[CONFIRM: responsible attorney]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 4 | Assess cross-border transfer mechanism adequacy (if applicable) | `[ACTION]` | `[CONFIRM: responsible attorney]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 5 | Respond to DSAR(s) within verified deadline (if applicable) | `[ACTION]` | `[CONFIRM]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 6 | `[CONFIRM: additional action item]` | | `[CONFIRM]` | `[CONFIRM]` [deadline verification required] | Open |

---

## 14. Attorney Sign-Off

> The responsible attorney must review this workspace, resolve all `[CONFIRM: ...]` and `[ACTION: ...]` placeholders, and sign off before this workspace is relied upon or shared.

- [ ] Client identity and controller/processor role confirmed under applicable law.
- [ ] Applicable jurisdictions and privacy frameworks identified and confirmed by attorney. `[verify jurisdiction]`
- [ ] All deadlines in Section 7 independently verified — none computed or inferred.
- [ ] Breach/incident notification obligations assessed; notifications made on time if required.
- [ ] DSAR response deadlines verified and responses completed within verified deadline if required.
- [ ] Cross-border transfer mechanisms assessed and confirmed as adequate if applicable.
- [ ] Data processing agreements in place with all processors as required.
- [ ] All `[CONFIRM: ...]` and `[ACTION: ...]` placeholders in this workspace resolved.
- [ ] Work-product index (Section 11) reflects all drafts produced; each draft reviewed and adopted or superseded by attorney.
- [ ] Risk and issue summary (Section 12) reviewed and confirmed or revised by responsible attorney.
- [ ] Privilege and confidentiality of this workspace protected; distribution limited to authorized personnel.
- [ ] No actual personal data and no client-sensitive facts appear in any reusable copy of the blank template.

| Field | Value |
|---|---|
| Responsible Attorney | `[CONFIRM: name and bar admission]` |
| Sign-Off Date | `[CONFIRM: date]` |
| Notes | |
