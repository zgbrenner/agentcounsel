> Draft legal work product for attorney review. Not legal advice.
> Do not paste client-sensitive facts into a reusable copy of this template.

---

**PRIVACY IMPACT ASSESSMENT**
**Status: DRAFT — FOR PRIVACY-COUNSEL REVIEW**

| Field | Value |
|---|---|
| Activity Name | `[CONFIRM: processing activity name]` |
| Prepared By | `[CONFIRM: name and role]` |
| Date Prepared | `[CONFIRM: date]` |
| Version | 0.1 — Draft |
| Privacy Counsel Reviewer | `[CONFIRM: reviewer name]` |
| Sign-Off Date | Pending privacy-counsel review |

---

## Executive Summary

`[Draft one paragraph summarizing: (1) the processing activity and its stated purpose; (2) the key data categories and data subjects involved; (3) the most significant risks identified; (4) the overall risk rating and draft recommendation. Replace this block with the actual summary when completing the assessment.]`

**Overall Risk Rating:** `[Low / Medium / High — CONFIRM: rating is a draft for privacy-counsel review]`

**Draft Recommendation:** `[Approve / Approve with Conditions / Changes Required / Not Approved — DRAFT, requires privacy-counsel sign-off]`

---

## Section 1 — Description of Processing

### 1.1 Activity Description

`[Describe the feature, system, vendor use, or processing change in functional terms. What does it do? What triggers data collection or use? What is the user or subject experience?]`

### 1.2 Purpose of Processing

`[State the specific business or functional purpose for which personal data is collected or reused. If multiple purposes apply, list each separately.]`

- Primary purpose: `[CONFIRM: purpose]`
- Secondary purposes (if any): `[CONFIRM: secondary purposes, or note none]`

### 1.3 Data Subjects

`[Identify the categories of individuals whose data is involved.]`

| Data Subject Category | Estimated Volume | Notes |
|---|---|---|
| `[e.g., registered customers]` | `[CONFIRM]` | |
| `[e.g., employees]` | `[CONFIRM]` | |
| `[CONFIRM: other categories]` | `[CONFIRM]` | |

`[CONFIRM: whether any data subjects are minors or otherwise in a protected category — [verify jurisdiction]]`

### 1.4 Data Categories

`[List the specific fields or data elements involved. Generic labels (e.g., "user data") are insufficient — list the actual fields.]`

| Data Element | Sensitivity | Source | Notes |
|---|---|---|---|
| `[e.g., email address]` | `[Low / Medium / High]` | `[CONFIRM: collected directly / derived / received from third party]` | |
| `[e.g., precise geolocation]` | `[CONFIRM]` | `[CONFIRM]` | |
| `[CONFIRM: additional fields]` | | | |

### 1.5 New Collection or Reuse

- [ ] New collection — personal data is collected for this activity for the first time.
- [ ] Reuse of previously collected data — data collected for a prior purpose is being used for this activity.
- [ ] `[CONFIRM: clarify]`

If reuse: `[Describe the original collection purpose and assess whether this new use is compatible with the original purpose — flag compatibility as [ATTORNEY TO CONFIRM: compatible-use analysis — [verify jurisdiction]]]`

---

## Section 2 — Legal Basis and Disclosure

> All determinations in this section are subject to `[verify jurisdiction]` and require privacy-counsel confirmation. The agent has not asserted which law applies or what it requires.

### 2.1 Stated Legal Basis for Processing

`[Describe the legal basis the organization intends to rely on for this processing activity — e.g., consent, contract performance, legitimate interests, legal obligation. Do not assert whether this basis is valid under any applicable law.]`

| Processing Purpose | Intended Legal Basis | Status |
|---|---|---|
| `[CONFIRM: purpose]` | `[CONFIRM: stated basis]` | `[ATTORNEY TO CONFIRM: valid under applicable law — [verify jurisdiction]]` |

### 2.2 Disclosure to Data Subjects

`[Describe how this processing activity is or will be disclosed to data subjects — in the privacy policy, a supplemental notice, a consent flow, or otherwise.]`

- Current disclosure mechanism: `[CONFIRM]`
- Privacy policy covers this activity: `[Yes / No / CONFIRM — see Section 4]`
- Supplemental notice required: `[CONFIRM: [ATTORNEY TO CONFIRM]]`

### 2.3 Consent (if applicable)

`[If consent is the intended legal basis, describe the consent mechanism, how consent is recorded, and whether withdrawal is supported. If consent is not the intended basis, note "Not applicable."]`

`[CONFIRM: consent mechanism and records — [verify jurisdiction]]`

---

## Section 3 — Data Flow

### 3.1 Collection

`[Describe how personal data enters the system: directly from the data subject, from another internal system, from a third party, or by derivation.]`

| Data Element | Collection Method | Directly from Subject? |
|---|---|---|
| `[CONFIRM]` | `[CONFIRM]` | `[Yes / No / CONFIRM]` |

### 3.2 Storage

| Parameter | Detail |
|---|---|
| Storage location (jurisdiction / region) | `[CONFIRM: [verify jurisdiction] if cross-border transfer is involved]` |
| Infrastructure controller | `[CONFIRM: internal / cloud provider name / subprocessor]` |
| Encryption at rest | `[CONFIRM: Yes / No / Unknown]` |
| Encryption in transit | `[CONFIRM: Yes / No / Unknown]` |
| Access controls | `[CONFIRM: role-restricted / unrestricted / Unknown]` |

### 3.3 Sharing and Subprocessors

`[List all third parties — vendors, subprocessors, analytics providers, infrastructure providers — that receive or process this data.]`

| Recipient / Subprocessor | Role | Data Shared | DPA in Place | Notes |
|---|---|---|---|---|
| `[CONFIRM: name]` | `[CONFIRM: processor / joint controller / other]` | `[CONFIRM: data elements]` | `[ATTORNEY TO CONFIRM]` | |
| `[CONFIRM]` | | | | |

`[CONFIRM: whether all subprocessors are disclosed in the current privacy policy — see Section 4]`

### 3.4 Retention and Deletion

| Parameter | Detail |
|---|---|
| Retention period | `[CONFIRM: period — [deadline verification required] if a legal minimum or maximum applies]` |
| Deletion trigger | `[CONFIRM: what event triggers deletion or archival]` |
| Deletion method | `[CONFIRM: automated / manual / unknown]` |
| Backup retention | `[CONFIRM]` |
| Legal hold exception | `[CONFIRM: process for hold if applicable — [verify jurisdiction]]` |

---

## Section 4 — Policy-Consistency Check

> This section cross-references the findings above against the organization's current privacy policy or privacy notice. If the policy was not provided, this section cannot be completed and must be flagged for attorney review.

`[VERIFY: cross-check against current, published privacy policy before finalizing — policy text was [provided / not provided]]`

| PIA Finding | Privacy Policy Commitment | Consistent? | Gap / Issue |
|---|---|---|---|
| Data categories collected | `[CONFIRM: what policy states]` | `[Yes / No / CONFIRM]` | `[Describe gap if any]` |
| Stated purpose of processing | `[CONFIRM: what policy states]` | `[Yes / No / CONFIRM]` | |
| Third-party sharing | `[CONFIRM: what policy states]` | `[Yes / No / CONFIRM]` | |
| Retention period | `[CONFIRM: what policy states]` | `[Yes / No / CONFIRM]` | |
| Data-subject rights offered | `[CONFIRM: what policy states]` | `[Yes / No / CONFIRM]` | |
| Cross-border transfers | `[CONFIRM: what policy states]` | `[Yes / No / CONFIRM]` | |
| `[Additional finding]` | `[CONFIRM]` | | |

**Policy-consistency summary:** `[Summarize the overall consistency finding. Note any gaps that require a policy update, a supplemental notice, or a revised consent flow before the activity launches.]`

---

## Section 5 — Risks and Mitigations

> Each risk must be grounded in a specific design feature, access pattern, data category, purpose, sharing arrangement, or rights gap. Generic risks (e.g., "data breach," "non-compliance") are not acceptable entries. Likelihood and impact ratings are draft assessments for privacy-counsel and operational review.

| # | Risk Description | Design Basis | Likelihood | Impact | Proposed Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| R1 | `[CONFIRM: specific, design-grounded risk description]` | `[CONFIRM: the specific design element that creates this risk]` | `[Low / Medium / High / CONFIRM]` | `[Low / Medium / High / CONFIRM]` | `[CONFIRM: specific, actionable mitigation]` | `[CONFIRM: role or team]` | `[Open / In Progress / Resolved]` |
| R2 | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` | `[Open]` |
| R3 | `[CONFIRM: add or remove rows — target 2–5 design-specific risks]` | | | | | | |

**Risk summary:** `[Summarize the risk picture. Note whether any risks are blockers to launch, conditions on launch, or items to monitor post-launch.]`

---

## Section 6 — Data-Subject-Rights Readiness

> Which rights apply to this activity depends on the governing legal framework and is subject to `[verify jurisdiction]`. This table assesses technical and operational readiness for each rights category; it does not determine whether each right is legally required.

| Right | Applicable? | Readiness | Gap / Issue | Notes |
|---|---|---|---|---|
| Access / disclosure | `[CONFIRM — [verify jurisdiction]]` | `[Ready / Partial / Not Ready / CONFIRM]` | `[CONFIRM]` | |
| Correction / rectification | `[CONFIRM — [verify jurisdiction]]` | `[CONFIRM]` | `[CONFIRM]` | |
| Deletion / erasure | `[CONFIRM — [verify jurisdiction]]` | `[CONFIRM]` | `[CONFIRM]` | |
| Portability | `[CONFIRM — [verify jurisdiction]]` | `[CONFIRM]` | `[CONFIRM]` | |
| Objection / opt-out | `[CONFIRM — [verify jurisdiction]]` | `[CONFIRM]` | `[CONFIRM]` | |
| Restriction of processing | `[CONFIRM — [verify jurisdiction]]` | `[CONFIRM]` | `[CONFIRM]` | |
| Automated decision-making / profiling | `[CONFIRM — [verify jurisdiction]]` | `[CONFIRM]` | `[CONFIRM]` | |

**Rights-readiness summary:** `[Summarize gaps. Note which gaps must be resolved before launch versus which can be addressed post-launch with monitoring.]`

---

## Section 7 — Recommendation

> This recommendation is a **draft for privacy-counsel review and sign-off**. It is not a binding approval or a determination that the processing is lawful. Privacy counsel must review the full PIA and make the final determination.

**Draft Recommendation:** `[Select one: Approve / Approve with Conditions / Changes Required / Not Approved]`

`[Draft one paragraph explaining the basis for this recommendation, referencing the risk rating, the most significant risks identified, and the policy-consistency findings.]`

### Conditions (if Approve with Conditions or Changes Required)

`[List each condition as a specific, actionable item. Assign a sign-off role to each condition. Leave blank if recommendation is Approve or Not Approved.]`

- [ ] **Condition 1:** `[CONFIRM: specific condition]` — Sign-off: `[CONFIRM: role]`
- [ ] **Condition 2:** `[CONFIRM]` — Sign-off: `[CONFIRM: role]`
- [ ] **Condition 3:** `[CONFIRM]` — Sign-off: `[CONFIRM: role]`

### Sign-Off Roles

| Role | Name | Date |
|---|---|---|
| Privacy Counsel | `[CONFIRM]` | Pending |
| Data Protection Officer (if applicable) | `[CONFIRM]` | Pending |
| Product / Engineering Owner | `[CONFIRM]` | Pending |
| Legal (additional review if required) | `[CONFIRM]` | Pending |

---

## Open Items for Attorney Verification

`[This section consolidates all flagged items from the PIA. Every [CONFIRM: ...], [VERIFY: ...], [ATTORNEY TO CONFIRM: ...], [verify jurisdiction], [deadline verification required], and [citation needed] item should appear here with a reference to its section. Complete this list when finalizing the draft.]`

| # | Item | Section | Type | Assigned To |
|---|---|---|---|---|
| 1 | Whether a formal DPIA or equivalent is legally required for this activity | Section 2 / Workflow Step 2 | `[ATTORNEY TO CONFIRM — [verify jurisdiction]]` | Privacy Counsel |
| 2 | Legal basis for each processing purpose is valid under applicable law | Section 2.1 | `[ATTORNEY TO CONFIRM — [verify jurisdiction]]` | Privacy Counsel |
| 3 | All data categories and data subjects are accurately and completely identified | Section 1.4–1.5 | `[CONFIRM]` | Activity Owner |
| 4 | Policy-consistency check completed against current published policy | Section 4 | `[VERIFY]` | Privacy Counsel |
| 5 | DPAs in place for all subprocessors listed in Section 3.3 | Section 3.3 | `[ATTORNEY TO CONFIRM]` | Legal / Procurement |
| 6 | Retention periods verified against applicable legal requirements | Section 3.4 | `[verify jurisdiction] [deadline verification required]` | Privacy Counsel |
| 7 | Cross-border transfer mechanisms confirmed (if applicable) | Section 3.2 | `[ATTORNEY TO CONFIRM — [verify jurisdiction]]` | Privacy Counsel |
| 8 | Data-subject rights applicable to this activity confirmed | Section 6 | `[verify jurisdiction]` | Privacy Counsel |
| 9 | Risk likelihood and impact ratings confirmed by person with operational knowledge | Section 5 | `[CONFIRM]` | Activity Owner |
| 10 | All proposed mitigations are technically and operationally feasible; owners confirmed | Section 5 | `[CONFIRM]` | Activity Owner + Privacy Counsel |
| 11 | `[CONFIRM: additional open items identified during completion]` | | | |

---

*This document is a draft prepared for internal review and privacy-counsel evaluation. It does not constitute legal advice, a final privacy determination, or a regulatory filing. All open items must be resolved before this PIA is treated as final.*
