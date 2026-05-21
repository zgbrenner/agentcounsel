> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Contracts

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Contracts |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Identify every jurisdiction, governing-law regime, and forum in which this group regularly works. Agents will gate jurisdiction-specific analysis on this list and flag anything outside it for attorney escalation.

| Field | Value |
|---|---|
| Primary Jurisdictions | `[CONFIRM: e.g., state/province, country]` |
| Secondary / Occasional Jurisdictions | `[CONFIRM: list or "none at this time"]` |
| Default Governing Law | `[CONFIRM: preferred governing-law clause, or "counterparty-dependent"]` |
| Preferred Dispute-Resolution Forum | `[CONFIRM: e.g., courts of a specified jurisdiction, arbitration body]` |
| International / Cross-Border Work | `[CONFIRM: yes/no; if yes, list regimes and any export-control considerations]` |

**Guiding prompts for this section:**
- What governing-law clause does the group prefer to propose as a starting position?
- In which jurisdictions does the group regularly enforce or defend contractual claims?
- Are there forum-selection clauses the group treats as standard or as automatic deal points?
- Does the group work on agreements subject to cross-border transfer restrictions or international arbitration rules?

---

## Client / Team Context

Describe who this group serves and how it is organized. Agents use this section to understand escalation paths and supervision structure.

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., business units, product teams, procurement]` |
| External Client Types | `[CONFIRM: e.g., enterprise SaaS vendors, Fortune 500 buyers, startups]` |
| Team Composition | `[CONFIRM: partners, senior associates, associates, paralegals, contract managers]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight responsibility for AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how matters reach the group — ticketing system, direct request, etc.]` |

**Guiding prompts for this section:**
- Who is the primary internal or external client this group supports?
- Who is the designated supervising attorney for AI-assisted contract review or drafting?
- Does the group use a contract management system, intake form, or matter-management platform?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Contract value | `[CONFIRM: e.g., above $[X], escalate to partner]` | `[CONFIRM: role or name]` |
| Liability cap below floor | `[CONFIRM: e.g., cap less than [X] months' fees or $[X] total]` | `[CONFIRM: role or name]` |
| Uncapped liability clause | `[CONFIRM: escalate any agreement with no liability cap]` | `[CONFIRM: role or name]` |
| Auto-renewal clause present | `[CONFIRM: flag for attorney review or client instruction]` | `[CONFIRM: role or name]` |
| IP assignment affecting core assets | `[CONFIRM: any assignment of patents, trademarks, or platform IP]` | `[CONFIRM: role or name]` |
| Indemnification — one-sided or uncapped | `[CONFIRM: escalation criteria]` | `[CONFIRM: role or name]` |
| Counterparty is a government entity | `[CONFIRM: always escalate / apply special review]` | `[CONFIRM: role or name]` |
| Non-standard dispute resolution | `[CONFIRM: e.g., mandatory arbitration in unfamiliar forum]` | `[CONFIRM: role or name]` |
| Any clause outside known playbook | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- At what dollar value does a contract require partner or senior-attorney sign-off?
- Does the group have a minimum acceptable liability cap expressed as a dollar figure or a multiple of fees?
- Are auto-renewal clauses a standing concern requiring client notification before they trigger?
- What indemnification structures are outside the group's standard playbook and require escalation?

---

## Preferred Output Style

Specify the format, tone, and length conventions agents must follow when producing deliverables for this group.

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., tabular risk matrix, memo, redline markup, clause-by-clause summary]` |
| Tone | `[CONFIRM: e.g., plain business language, formal legal prose]` |
| Length convention | `[CONFIRM: e.g., executive summary ≤ 1 page + full matrix; no single-section limit]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Risk-rating scheme | `[CONFIRM: e.g., High / Medium / Low aligned with contract-risk-matrix template]` |
| Redline conventions | `[CONFIRM: e.g., track-changes Word, Markdown strikethrough/insertion, inline annotations]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- Do clients expect a one-page executive summary or a full clause-by-clause walkthrough?
- Does the group use a standard risk-rating scheme that agents should align with?
- How should agents present redline suggestions — narrative, table, or markup?

---

## Source-of-Truth Documents

List the authoritative playbooks, templates, clause libraries, and reference materials this group uses. Reference by name and location only. Do not paste content here.

| Document | Location / Path | Notes |
|---|---|---|
| Standard contract-review playbook | `[CONFIRM: file name and location, e.g., internal drive path or system name]` | `[CONFIRM: version or last-updated date]` |
| Approved clause library | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| NDA template (inbound) | `[CONFIRM: file name and location]` | |
| NDA template (outbound) | `[CONFIRM: file name and location]` | |
| MSA template | `[CONFIRM: file name and location]` | |
| SaaS / subscription agreement template | `[CONFIRM: file name and location]` | |
| Signature authority / approval matrix | `[CONFIRM: file name and location]` | |
| Contract risk matrix template | `skills/contracts/contract-risk-review/templates/contract-risk-matrix.md` | Canonical AgentCounsel template |

**Guiding prompts for this section:**
- Where does the group store its approved templates and clause fallbacks?
- Is there a playbook document that defines the group's standard positions for common clauses?
- What contract management system holds executed agreements?

---

## Standard Positions / Playbooks

Record the group's default negotiating positions for key contract terms. These are starting positions — an agent uses them to flag deviations but always defers final judgment to an attorney.

| Clause | Group's Default Position | Notes / Conditions |
|---|---|---|
| Governing law | `[CONFIRM: preferred jurisdiction]` | `[CONFIRM: when to accept counterparty's law]` |
| Limitation of liability — cap amount | `[CONFIRM: e.g., greater of total fees paid or $[X]]` | `[CONFIRM: when a lower cap is acceptable]` |
| Limitation of liability — consequential damages | `[CONFIRM: e.g., mutual exclusion with named carve-outs]` | `[CONFIRM: required carve-outs, e.g., IP indemnity, fraud, data breach]` |
| Indemnification — IP infringement | `[CONFIRM: e.g., mutual; each party indemnifies for its own IP]` | |
| Indemnification — data breach | `[CONFIRM: group's standard position]` | |
| Auto-renewal | `[CONFIRM: e.g., oppose; require affirmative renewal or minimum notice window]` | `[CONFIRM: minimum acceptable notice period]` |
| Term / initial contract duration | `[CONFIRM: preferred initial term length]` | |
| Termination for convenience | `[CONFIRM: e.g., require mutual right; minimum notice period]` | |
| Assignment / change of control | `[CONFIRM: e.g., require consent for assignment; termination right on change of control]` | |
| Confidentiality duration | `[CONFIRM: minimum post-termination confidentiality period]` | |
| Dispute resolution | `[CONFIRM: preferred mechanism — litigation, arbitration, mediation first]` | |

**Guiding prompts for this section:**
- What is the group's floor for a liability cap as a multiple of fees or an absolute dollar amount?
- Which carve-outs from the consequential-damages exclusion does the group always seek?
- Does the group have a standing position on auto-renewal notice windows?
- What governing-law clauses does the group accept from counterparties without escalation?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Contract risk matrix or review memo | `[CONFIRM: e.g., supervising associate or partner]` | All; no exceptions |
| Redline or draft contract | `[CONFIRM: role]` | All; no exceptions |
| Clause library addition or update | `[CONFIRM: role]` | Requires written approval |
| Playbook update | `[CONFIRM: role]` | Requires written approval and version increment |
| Executed-agreement summary | `[CONFIRM: role]` | `[CONFIRM: before distribution to business?]` |
| Any output touching an uncapped liability or IP assignment | Partner-level review | Always |

**Guiding prompts for this section:**
- Is there a tiered review structure (associate drafts, partner approves) for different contract values?
- Which deliverables can be reviewed by a senior associate without partner sign-off?
- Does the group require countersignature by a second attorney for agreements above a certain value?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| Governing law is the group's preferred jurisdiction | Counterparty's form may specify a different law; must be confirmed |
| Liability cap meets the group's floor | Cap amount and basis must be read from the actual agreement |
| Auto-renewal clause is absent | Must be confirmed by reading every agreement; do not assume it is absent |
| Indemnification is mutual | One-sided indemnification is common; must be confirmed |
| Prior version of an agreement reflects current terms | Only the version provided for review controls |
| A standard-form agreement is unchanged from the template | Counterparties modify forms; read the actual document |
| Client entity name and authorized signatory are correct | Must be confirmed against authoritative records |
| Signature authority has been obtained | Approval matrix must be consulted for each agreement |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill.

For a guided, question-by-question setup process, use the cold-start interview skill at `skills/setup/contracts-cold-start-interview/SKILL.md`. That skill walks through each section of this profile and produces a draft-completed version for attorney review.

Do not include client names, matter numbers, confidential facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
