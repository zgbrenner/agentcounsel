> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Mergers & Acquisitions

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Mergers & Acquisitions |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Deal structure, entity law, antitrust and foreign-investment review, securities treatment, and tax treatment are jurisdiction-specific. Agents gate every jurisdiction-specific point on this list and flag anything outside it for attorney escalation.

| Field | Value |
|---|---|
| Entity / Organizational Jurisdictions | `[CONFIRM: jurisdictions of the entities the group typically works with]` |
| Default Governing Law for Deal Documents | `[CONFIRM: preferred governing law, or "deal-dependent"]` |
| Antitrust / Competition Regimes | `[CONFIRM: regimes that may apply; antitrust analysis is attorney-directed]` |
| Foreign-Investment / National-Security Review | `[CONFIRM: whether the group's deals may trigger review; route to specialist counsel]` |
| Cross-Border Work | `[CONFIRM: yes/no; if yes, list regimes and note local-counsel practice]` |

**Guiding prompts:**
- What governing law does the group propose for purchase agreements as a starting position?
- Which regulators or review regimes recur in the group's deals, and who handles that analysis?
- When is local or specialist counsel always engaged?

---

## Client / Team Context

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., corporate development, a fund's deal team, business units]` |
| External Client Types | `[CONFIRM: e.g., strategic acquirers, private equity sponsors, founders, target companies]` |
| Typical Deal Types | `[CONFIRM: e.g., stock and asset purchases, mergers, acqui-hires, roll-ups, minority investments]` |
| Typical Side | `[CONFIRM: buyer-side, seller-side, company-side, investor-side, or mixed]` |
| Team Composition | `[CONFIRM: partners, associates, paralegals, diligence coordinators]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight of AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how deals reach the group]` |

**Guiding prompts:**
- Which side of the deal does the group most often represent?
- Who is the designated supervising attorney for AI-assisted diligence and agreement review?
- Does the group use a deal-management or virtual-data-room platform?

---

## Escalation Thresholds

Conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Deal value | `[CONFIRM: above $[X], escalate to partner]` | `[CONFIRM: role or name]` |
| Possible antitrust or merger-control filing | `[CONFIRM: any deal that may require a competition filing]` | `[CONFIRM: role or name]` |
| Possible foreign-investment / national-security review | `[CONFIRM: escalation criteria]` | `[CONFIRM: role or name]` |
| Regulated-industry target | `[CONFIRM: e.g., financial services, healthcare, defense]` | `[CONFIRM: role or name]` |
| Uncapped or fundamental-rep indemnity exposure | `[CONFIRM: escalation criteria]` | `[CONFIRM: role or name]` |
| Earnout, rollover equity, or contingent consideration | `[CONFIRM: escalate for structuring review]` | `[CONFIRM: role or name]` |
| Securities or tax-sensitive structure | `[CONFIRM: route structuring questions to specialist counsel]` | `[CONFIRM: role or name]` |
| Government or state-owned counterparty | `[CONFIRM: always escalate / apply special review]` | `[CONFIRM: role or name]` |
| Contested, hostile, or auction process | `[CONFIRM: escalation criteria]` | `[CONFIRM: role or name]` |
| Approaching signing or closing deadline | `[CONFIRM: escalate; deadlines are never computed by an agent]` | `[CONFIRM: role or name]` |
| Any term outside the known playbook | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts:**
- At what deal value does a transaction require partner sign-off?
- Which deals always go to antitrust, tax, or foreign-investment specialists?
- What indemnity structures are outside the group's playbook?

---

## Preferred Output Style

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., issue list, risk matrix, diligence request list, tracker]` |
| Tone | `[CONFIRM: e.g., plain business language, formal legal prose]` |
| Length convention | `[CONFIRM: e.g., executive summary + full matrix]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Risk-rating scheme | `[CONFIRM: e.g., High / Medium / Low]` |
| Source-citation convention | `[CONFIRM: e.g., section / clause / schedule / page reference required on every extracted term]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts:**
- Do clients expect an executive summary plus a full issue list, or a section-by-section walkthrough?
- How should agents cite the source of an extracted agreement or schedule term?

---

## Source-of-Truth Documents

List the authoritative playbooks, forms, and reference materials this group uses. Reference by name and location only — do not paste content.

| Document | Location / Path | Notes |
|---|---|---|
| Purchase-agreement review playbook | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| Standard form purchase agreement(s) | `[CONFIRM: file name and location]` | |
| Diligence request-list template(s) | `[CONFIRM: file name and location]` | |
| Disclosure schedule conventions | `[CONFIRM: file name and location]` | |
| Indemnity / escrow playbook | `[CONFIRM: file name and location]` | |
| Closing checklist template | `[CONFIRM: file name and location]` | |
| Signature / approval authority matrix | `[CONFIRM: file name and location]` | |

**Guiding prompts:**
- Where does the group store its approved purchase-agreement and ancillary forms?
- Is there a standing indemnity and escrow playbook?

---

## Standard Positions / Playbooks

Default starting positions for key deal terms. An agent uses these to flag deviations and always defers final judgment to an attorney. Any numerical figure is a starting placeholder for attorney verification, not a market-standard assertion.

| Term | Group's Default Position | Notes / Conditions |
|---|---|---|
| Deal structure | `[CONFIRM: preferred structure by deal type]` | `[CONFIRM: tax and liability drivers — confirm with specialists]` |
| Governing law / forum | `[CONFIRM: preferred governing law and forum]` | |
| Purchase-price adjustment / working capital | `[CONFIRM: preferred mechanics]` | |
| Earnout / contingent consideration | `[CONFIRM: position; structuring escalated]` | |
| Escrow / holdback | `[CONFIRM: starting position — placeholder for attorney verification]` | |
| Indemnity cap | `[CONFIRM: starting position — placeholder, not a market-standard claim]` | |
| Indemnity basket / deductible | `[CONFIRM: starting position — placeholder]` | |
| Survival of representations | `[CONFIRM: preferred survival periods; fundamental reps separately]` | |
| Sandbagging / materiality scrape | `[CONFIRM: group's standard stance]` | |
| Exclusivity period | `[CONFIRM: preferred length]` | |
| Representation and warranty insurance | `[CONFIRM: when the group uses RWI]` | |

**Guiding prompts:**
- What escrow, cap, and basket positions does the group open with — and are they framed as placeholders, not market claims?
- What is the group's stance on sandbagging and the materiality scrape?

---

## Attorney Review Requirements

What must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| LOI / term sheet review | `[CONFIRM: role]` | All; no exceptions |
| Purchase-agreement issue list or risk matrix | `[CONFIRM: role]` | All; no exceptions |
| Diligence request list or data-room review | `[CONFIRM: role]` | Before it is relied upon |
| Reps / disclosure-schedule review | `[CONFIRM: role]` | Before signing |
| Indemnity / escrow review | `[CONFIRM: role]` | Before signing |
| Closing or post-closing tracker | `[CONFIRM: role]` | Before relied upon to close |
| Any output touching antitrust, tax, securities, or foreign-investment questions | Partner-level and/or specialist counsel | Always |

**Guiding prompts:**
- Is there a tiered review structure by deal value?
- Which questions always require tax, antitrust, or regulatory specialists?

---

## Prohibited Assumptions

What an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| A provision is legally binding or enforceable | Binding effect and enforceability are legal questions for the attorney |
| Consent is, or is not, legally required | A consent determination depends on the contract and the law; confirm with counsel |
| An antitrust or foreign-investment filing is, or is not, required | A filing determination is attorney and specialist work |
| The disclosure schedules are complete or accurate | Only the schedules actually provided are reviewed; completeness is for counsel |
| A date or deadline can be computed | Signing, closing, survival, and filing deadlines are attorney-verified, never computed |
| The tax or securities treatment of the structure is known | Tax and securities treatment are specialist determinations |
| A figure is "market standard" | Any cap, basket, or escrow figure is a placeholder for attorney verification |
| The LOI controls over a later draft agreement, or vice versa | Which document controls is a legal question; surface the conflict, do not resolve it |
| All deal documents, schedules, and ancillary agreements were provided | Only the documents actually provided control; missing documents must be flagged |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill. The loading order is: `core/` rules first, then this profile, then the skill.

Do not include client names, target names, deal-specific facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
