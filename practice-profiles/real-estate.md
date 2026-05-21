> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Real Estate

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Real Estate |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Real property law, recording practice, title standards, transfer taxes, and zoning are intensely local. Agents gate every jurisdiction-specific point on this list and flag anything outside it for attorney or local-counsel escalation.

| Field | Value |
|---|---|
| Primary Jurisdictions | `[CONFIRM: states / counties / municipalities where the group regularly works]` |
| Secondary / Occasional Jurisdictions | `[CONFIRM: list or "none at this time"]` |
| Default Governing Law | `[CONFIRM: preferred governing law, or "situs-of-property-dependent"]` |
| Local-Counsel Requirement | `[CONFIRM: jurisdictions where local counsel is always engaged]` |
| Title Company / Underwriter Relationships | `[CONFIRM: standard title companies, or "deal-dependent"]` |

**Guiding prompts:**
- In which states and counties does the group close real estate transactions?
- Which jurisdictions always require local counsel or a local title agent?
- Are there asset types (for example ground leases, condominiums) the group handles only in certain jurisdictions?

---

## Client / Team Context

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., acquisitions team, asset management, leasing, treasury]` |
| External Client Types | `[CONFIRM: e.g., institutional owners, developers, REITs, lenders, tenants]` |
| Typical Party Roles | `[CONFIRM: e.g., buyer, seller, landlord, tenant, borrower, lender]` |
| Team Composition | `[CONFIRM: partners, associates, paralegals, lease administrators]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight of AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how matters reach the group]` |

**Guiding prompts:**
- Which side of the deal does the group most often represent?
- Who is the designated supervising attorney for AI-assisted lease and transaction work?
- Does the group use a lease-administration or transaction-management system?

---

## Escalation Thresholds

Conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Transaction value | `[CONFIRM: above $[X], escalate to partner]` | `[CONFIRM: role or name]` |
| Environmental finding or condition | `[CONFIRM: any provided report noting contamination or a recognized environmental condition]` | `[CONFIRM: role or name]` |
| Title exception affecting access, use, or buildability | `[CONFIRM: escalation criteria]` | `[CONFIRM: role or name]` |
| Survey shows encroachment or boundary issue | `[CONFIRM: escalation criteria]` | `[CONFIRM: role or name]` |
| Zoning non-conformity or use-restriction conflict | `[CONFIRM: escalation criteria]` | `[CONFIRM: role or name]` |
| Ground lease or leasehold-mortgage structure | `[CONFIRM: always escalate / apply special review]` | `[CONFIRM: role or name]` |
| Uncapped or one-sided indemnity | `[CONFIRM: escalation criteria]` | `[CONFIRM: role or name]` |
| Counterparty is a government entity | `[CONFIRM: always escalate / apply special review]` | `[CONFIRM: role or name]` |
| Approaching contingency, diligence, or closing deadline | `[CONFIRM: escalate; deadlines are never computed by an agent]` | `[CONFIRM: role or name]` |
| Any term outside the known playbook | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts:**
- At what deal value does a transaction require partner sign-off?
- What environmental, title, or survey findings are standing escalation triggers?
- Which structures (ground lease, condominium, portfolio deal) require specialist review?

---

## Preferred Output Style

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., abstract table, risk matrix, objection tracker, checklist]` |
| Tone | `[CONFIRM: e.g., plain business language, formal legal prose]` |
| Length convention | `[CONFIRM: e.g., executive summary + full table]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Risk-rating scheme | `[CONFIRM: e.g., High / Medium / Low]` |
| Source-citation convention | `[CONFIRM: e.g., section / clause / exhibit / page reference required on every extracted field]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts:**
- Do clients expect a one-page summary plus a full table, or a clause-by-clause walkthrough?
- How should agents cite the source of an extracted lease or title term?

---

## Source-of-Truth Documents

List the authoritative playbooks, templates, and reference materials this group uses. Reference by name and location only — do not paste content.

| Document | Location / Path | Notes |
|---|---|---|
| Lease-review / abstraction playbook | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| Standard form lease(s) | `[CONFIRM: file name and location]` | |
| Purchase and sale agreement template(s) | `[CONFIRM: file name and location]` | |
| Title and survey objection guidelines | `[CONFIRM: file name and location]` | |
| Diligence checklist template | `[CONFIRM: file name and location]` | |
| Closing checklist template | `[CONFIRM: file name and location]` | |
| Signature / approval authority matrix | `[CONFIRM: file name and location]` | |

**Guiding prompts:**
- Where does the group store its approved lease and PSA forms?
- Is there a standing title and survey objection playbook?

---

## Standard Positions / Playbooks

Default starting positions for key real estate terms. An agent uses these to flag deviations and always defers final judgment to an attorney.

| Term | Group's Default Position | Notes / Conditions |
|---|---|---|
| Governing law | `[CONFIRM: e.g., situs of the property]` | `[CONFIRM: exceptions]` |
| Diligence / inspection period | `[CONFIRM: preferred length and extension rights]` | Agents never compute the expiry date |
| Deposit / earnest money and escrow | `[CONFIRM: preferred amount, when it goes hard, escrow agent]` | |
| Financing contingency | `[CONFIRM: required, waivable, or none]` | |
| Title and survey objection process | `[CONFIRM: objection and cure mechanics the group prefers]` | |
| Representations and warranties survival | `[CONFIRM: preferred survival period and cap]` | |
| Casualty / condemnation termination threshold | `[CONFIRM: group's standard threshold]` | |
| Assignment | `[CONFIRM: e.g., permitted to affiliates; consent otherwise]` | |
| Lease — permitted use and exclusivity | `[CONFIRM: standard positions]` | |
| Lease — assignment and subletting consent standard | `[CONFIRM: standard position]` | |
| Estoppel and SNDA | `[CONFIRM: required forms and key protected terms]` | |

**Guiding prompts:**
- What diligence-period length does the group propose as a starting position?
- What title and survey objection mechanics does the group treat as standard?
- What estoppel and SNDA protections does the group always require?

---

## Attorney Review Requirements

What must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Lease abstract or amendment reconciliation | `[CONFIRM: role]` | All; no exceptions |
| Lease, PSA, or estoppel/SNDA review | `[CONFIRM: role]` | All; no exceptions |
| Title and survey objection tracker | `[CONFIRM: role]` | Before any objection or response is sent |
| Diligence or closing checklist | `[CONFIRM: role]` | Before it is relied upon to close |
| Any output touching environmental, title-marketability, or zoning questions | Partner-level and/or local counsel | Always |

**Guiding prompts:**
- Is there a tiered review structure for different deal values?
- Which questions always require local counsel or a specialist consultant?

---

## Prohibited Assumptions

What an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| Title is marketable, insurable, or clear | A title-marketability determination is for an attorney and the title company |
| The intended use is permitted by zoning | Zoning and permitted use are for local counsel or a zoning consultant |
| All amendments, side letters, and exhibits were provided | Only the documents actually provided control; missing documents must be flagged |
| The survey is current and reflects present conditions | Currency and accuracy of a survey must be confirmed |
| A date or deadline can be computed | All contingency, diligence, recording, and closing deadlines are attorney-verified, never computed |
| Recording or transfer-tax requirements are standard | Recording rules, forms, and transfer taxes are jurisdiction-specific and must be confirmed |
| A standard-form lease or PSA is unchanged from the template | Counterparties modify forms; read the actual document |
| The party entity names and signature authority are correct | Must be confirmed against authoritative records |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill. The loading order is: `core/` rules first, then this profile, then the skill.

Do not include client names, matter numbers, confidential facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
