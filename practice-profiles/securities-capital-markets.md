> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Securities / Capital Markets

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Securities / Capital Markets |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Exemption availability, filing obligations, disclosure requirements, and blue-sky treatment are regime-specific, and the rules change. Agents gate every regime-specific point on this list, flag anything outside it for attorney escalation, and never treat a remembered rule as current — `[verify current SEC rule version at time of review]` `[VERIFY current law / jurisdiction]`.

| Field | Value |
|---|---|
| Primary Securities Regimes / Regulators | `[CONFIRM: describe by jurisdiction and function — e.g., "national securities regulator," "state securities administrators"]` `[VERIFY current law / jurisdiction]` |
| Reporting / Filer Status of Covered Issuers | `[CONFIRM: supplied by counsel per issuer — e.g., non-reporting, reporting, filer category; the agent never determines filer status]` |
| Exchanges / Listing Venues | `[CONFIRM: venues, or "none — private issuers only"]` |
| Blue-Sky / State Jurisdictions of Sale | `[CONFIRM: states or regions where offers and sales typically occur]` |
| Cross-Border / Foreign-Issuer Exposure | `[CONFIRM: yes/no; if yes, list regimes and note local-counsel practice]` |

**Guiding prompts for this section:**
- Which issuers does the group support, and what is each issuer's reporting and filer status as supplied by counsel?
- In which states or regions do offerings typically involve offers or sales, for blue-sky and notice-filing tracking?
- Which matters involve cross-border investors or foreign regimes, and when is local or specialist counsel engaged?

---

## Client / Team Context

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., CFO / finance, corporate secretary, investor relations, equity administration]` |
| External Client Types | `[CONFIRM: e.g., private issuers, public companies, funds, underwriters or placement agents]` |
| Typical Matter Types | `[CONFIRM: e.g., private placements, public offerings, periodic reporting, insider-trading compliance, beneficial-ownership and Section 16 filings, capital-markets closings]` |
| Team Composition | `[CONFIRM: partners, associates, paralegals, filing coordinators]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight of AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how matters reach the group]` |

**Guiding prompts for this section:**
- Who is the designated supervising attorney for AI-assisted disclosure and offering work?
- Who supplies the issuer-specific inputs the agent must never infer — filer status, outstanding share counts, insider lists?
- Does the group use a filing calendar, equity-administration, or transaction-management system?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Exemption-availability question | Whether an exemption is, or remains, available is never determined by the agent — flag and route | `[CONFIRM: role or name]` |
| Any filing deadline | No securities filing deadline is ever computed or asserted by the agent | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` |
| Materiality or disclosure-adequacy question | Whether a fact is material or a disclosure is adequate is attorney judgment | `[CONFIRM: role or name]` |
| Possible insider status, MNPI, or trading-window issue | `[CONFIRM: any question touching insider status, material nonpublic information, or trading approval]` | `[CONFIRM: role or name]` |
| Beneficial-ownership or Section 16 flag | Any descriptive ownership-ratio flag near a reporting threshold — flagged, never concluded | `[CONFIRM: role or name]` |
| Possible general solicitation or offering communication | `[CONFIRM: any communication that may constitute an offer or general solicitation]` | `[CONFIRM: role or name]` |
| Regulator comment letter, inquiry, or examination | `[CONFIRM: escalate immediately on any regulator contact]` | `[CONFIRM: role or name]` |
| Request to approve a filing, signature, solicitation, or trade | Never approved by the agent; human sign-off always required | `[CONFIRM: role or name]` |
| Offering size | `[CONFIRM: above $[X], escalate to partner]` | `[CONFIRM: role or name]` |
| Any term outside the known playbook | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- Who resolves exemption-availability and materiality questions, and how are they routed?
- What is the escalation path when a possible trading-window or MNPI issue surfaces mid-task?
- At what offering size does a matter require partner sign-off?

---

## Preferred Output Style

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., disclosure-review issue list, tracker table, checklist, triage memo]` |
| Tone | `[CONFIRM: e.g., plain business language, formal legal prose]` |
| Length convention | `[CONFIRM: e.g., executive summary + full issue list]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Risk-rating scheme | `[CONFIRM: e.g., High / Medium / Low]` |
| Source-citation convention | `[CONFIRM: e.g., document / section / page reference required on every extracted disclosure, figure, or dated event]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- How should agents cite the source of an extracted disclosure, figure, or dated event?
- Do reviewers expect issue lists keyed to the issue-spotting frameworks reference?

---

## Source-of-Truth Documents

List the authoritative playbooks, policies, and reference materials this group uses. Reference by name and location only — do not paste content.

| Document | Location / Path | Notes |
|---|---|---|
| Insider trading policy | `[CONFIRM: file name and location]` | Benchmark for `skills/securities-capital-markets/insider-trading-policy-review/SKILL.md` |
| Disclosure controls and procedures policy | `[CONFIRM: file name and location]` | |
| Reporting calendar / filing tracker | `[CONFIRM: system name and location]` | Deadlines attorney-verified; intake via `skills/securities-capital-markets/public-company-reporting-calendar-intake/SKILL.md` |
| Offering-document precedent files | `[CONFIRM: location]` | Used with `skills/securities-capital-markets/offering-document-disclosure-review/SKILL.md` |
| Risk-factor library | `[CONFIRM: file name and location]` | Used with `skills/securities-capital-markets/risk-factor-review/SKILL.md` |
| Form D / blue-sky notice-filing tracker | `[CONFIRM: system name]` | Used with `skills/securities-capital-markets/form-d-blue-sky-tracker/SKILL.md` |
| Cap table / outstanding-share records | `[CONFIRM: system name]` | Share counts are user-supplied and dated, never assumed current |
| Signature / filing approval matrix | `[CONFIRM: file name and location]` | |
| Issue-spotting frameworks | `skills/securities-capital-markets/references/issue-spotting-frameworks.md` | Canonical AgentCounsel reference |

**Guiding prompts for this section:**
- Where do the insider trading policy, reporting calendar, and offering precedents live, and which versions are authoritative?
- What system is the authoritative record for filings made and deadlines pending?

---

## Standard Positions / Playbooks

Record the group's default starting positions. An agent uses these to flag deviations and always defers final judgment to an attorney. Nothing in this table states what the law permits — availability, adequacy, and status determinations are always attorney work.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Default private-placement pathway | `[CONFIRM: the exemption pathway the group typically starts from — availability always attorney-determined]` | `[VERIFY current law / jurisdiction]` |
| Accredited-investor verification | `[CONFIRM: verification approach and documentation standard]` | |
| General solicitation | `[CONFIRM: e.g., none unless counsel approves the pathway in advance]` | |
| Form D / state notice filings | `[CONFIRM: who prepares, who verifies each deadline]` | `[deadline verification required]` |
| Trading windows and preclearance | `[CONFIRM: window and preclearance conventions per the insider trading policy]` | |
| Section 16 / beneficial-ownership filings | `[CONFIRM: who prepares; insider status and filer status supplied by counsel]` | Used with `skills/securities-capital-markets/section-16-beneficial-ownership-triage/SKILL.md` |
| Risk-factor drafting conventions | `[CONFIRM: ordering, specificity, treatment of mitigating language]` | |
| Filing-consistency review scope | `[CONFIRM: which filings are cross-checked and how discrepancies are routed]` | Used with `skills/securities-capital-markets/sec-filing-consistency-check/SKILL.md` |
| Comfort-letter / backup practice | `[CONFIRM: circle-up and backup-request conventions]` | Used with `skills/securities-capital-markets/comfort-backup-request-tracker/SKILL.md` |
| Investor-rights defaults | `[CONFIRM: registration-rights, information-rights, preemptive-rights starting positions]` | Used with `skills/securities-capital-markets/investor-rights-agreement-review/SKILL.md` |

**Guiding prompts for this section:**
- What exemption pathway does the group start from for private placements, with availability left to counsel?
- Who owns Form D and state notice filings, and who verifies every deadline?
- What are the group's standing conventions for risk-factor drafting and filing-consistency checks?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, filed, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Offering-document or risk-factor disclosure review | `[CONFIRM: role]` | All; adequacy and materiality are attorney judgments |
| Securities-exemption issue-spotter output | `[CONFIRM: role]` | All; exemption availability is attorney work |
| Form D / blue-sky tracker | `[CONFIRM: role]` | Before any filing; every deadline attorney-verified |
| Reporting-calendar intake | `[CONFIRM: role]` | Every date attorney-verified before reliance |
| Insider-trading policy review | `[CONFIRM: role]` | Before adoption or amendment |
| Section 16 / beneficial-ownership triage | `[CONFIRM: role]` | All; before any filing decision |
| SEC filing consistency check | `[CONFIRM: role]` | Findings reviewed before any corrective step |
| Closing checklist or comfort/backup tracker | `[CONFIRM: role]` | Before relied upon to close |
| Any output touching a filing, signature, solicitation, or trade | Partner-level review | Always; the agent never approves |

**Guiding prompts for this section:**
- Is there a tiered review structure by offering size or filing type?
- Which deliverables always require partner-level or specialist review?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| An exemption is available or remains available | Availability is a legal determination for the attorney |
| A filing deadline is known or computable | Deadlines are never computed; `[deadline verification required]` |
| An issuer's filer or reporting status | Supplied by counsel; never inferred from documents |
| A fact is, or is not, material | Materiality is a legal judgment |
| A person is an insider, a beneficial owner, or part of a group | Ownership ratios are descriptive flags only; status is attorney work |
| Outstanding share counts are current | Counts must be user-supplied and dated |
| A prior filing was made, or was accurate | Must be confirmed against filing records |
| A remembered rule, form, or threshold is current | Rules change; `[verify current SEC rule version at time of review]` |
| The provided document set is complete or the latest draft | Only the documents actually provided control; missing items are flagged |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill. The loading order is: `core/` rules first, then this profile, then the skill.

For a guided, question-by-question setup process, use the cold-start interview skill at `skills/setup/securities-capital-markets-cold-start-interview/SKILL.md`. That skill walks through each section of this profile and produces a draft-completed version for attorney review.

Do not include issuer names, offering-specific facts, insider lists, matter numbers, or privileged analysis in this profile. This is a configuration document, not a work-product file.
