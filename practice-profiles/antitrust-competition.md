> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Antitrust / Competition

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Antitrust / Competition |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Merger-control thresholds, safe harbors, and enforcement priorities differ by regime and change over time. Agents gate every regime-specific point on this list, route all reportability questions to counsel, and never treat a remembered threshold as current — `[VERIFY current law / jurisdiction]`.

| Field | Value |
|---|---|
| Jurisdictions of Competitive Effect | `[CONFIRM: jurisdictions where the organization's conduct or transactions may have competitive effects]` |
| Merger-Control Regimes Potentially In Scope | `[CONFIRM: describe by jurisdiction; reportability and filing determinations are attorney work]` `[VERIFY current law / jurisdiction]` |
| Competition Authorities Monitored | `[CONFIRM: describe by jurisdiction and function — e.g., "national competition authority," "sector regulator with competition powers"]` |
| Industries / Markets Typically Involved | `[CONFIRM: sectors; market definition is never assumed — [ATTORNEY TO CONFIRM: market definition]]` |
| Cross-Border Exposure | `[CONFIRM: yes/no; if yes, list regimes and note local-counsel practice]` |

**Guiding prompts for this section:**
- In which jurisdictions could the group's transactions trigger merger-control review, and who makes the reportability call?
- Which authorities' guidance and enforcement activity does the group monitor?
- In which markets do the parties the group advises actually compete, as confirmed by counsel per matter?

---

## Client / Team Context

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., sales, procurement, corporate development, product and pricing teams]` |
| External Client Types | `[CONFIRM: e.g., operating companies, investors, platforms, trade-association members]` |
| Typical Counterparty Posture | `[CONFIRM: whether counterparties are typically competitors, suppliers, distributors, or platform participants — competitive posture is confirmed per market, never assumed]` |
| Typical Matter Types | `[CONFIRM: e.g., competitor collaborations, information sharing, distribution and resale terms, exclusivity and MFN terms, pricing-algorithm review, merger issue spotting, trade-association counseling]` |
| Team Composition | `[CONFIRM: partners, associates, economists or economic consultants, paralegals]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight of AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how matters reach the group]` |

**Guiding prompts for this section:**
- Who is the designated supervising attorney for AI-assisted competition work?
- How does the group confirm, per matter, whether the parties compete in a relevant market?
- When are economists or specialist merger counsel engaged?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops. Hardcore-restraint indicators are always an immediate escalation.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Hardcore-restraint indicator | Any indicator of price fixing, output limitation, market or customer allocation, bid rigging, or group boycott — immediate hard stop; no drafting continues | `[CONFIRM: role or name — escalate immediately]` |
| Planned competitor communication | `[CONFIRM: any planned contact with a competitor touching price, output, capacity, customers, territories, wages, or strategy]` | `[CONFIRM: role or name]` |
| Competitor information exchange | `[CONFIRM: any flow of forward-looking, customer-specific, wage, or bid data between competitors — pause until safeguards are confirmed]` | `[CONFIRM: role or name]` |
| Hub-and-spoke pattern | `[CONFIRM: any information flow between competitors through a shared vendor, platform, consultant, or algorithm provider]` | `[CONFIRM: role or name]` |
| Merger filing / reportability question | Whether a transaction is reportable in any regime is never determined by the agent | `[CONFIRM: role or name]` |
| Pre-signing / pre-closing coordination step | `[CONFIRM: any integration planning, information transfer, or conduct-covenant deviation before closing]` | `[CONFIRM: role or name]` |
| Trade-association participation | `[CONFIRM: joining a new association, agenda concerns, or flagged meeting conduct]` | `[CONFIRM: role or name]` |
| Pricing-algorithm deployment or change | `[CONFIRM: any algorithmic pricing tool using competitor data or a shared vendor model]` | `[CONFIRM: role or name]` |
| Market-definition-dependent question | Any analysis that turns on market definition or market power — `[ATTORNEY TO CONFIRM: market definition]` | `[CONFIRM: role or name]` |
| Request for a legality or clearance conclusion | The agent never concludes that conduct is lawful or that a deal is clearable | `[CONFIRM: role or name]` |
| Any term outside the known playbook | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- What is the immediate escalation path when a hardcore-restraint indicator surfaces mid-task?
- Which information flows between competitors require clean-team or safeguard review before proceeding?
- Who assesses reportability, and what facts does that person need assembled?

---

## Preferred Output Style

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., risk-triage table, issue list, checklist, meeting-review memo]` |
| Tone | `[CONFIRM: e.g., plain business language, formal legal prose]` |
| Length convention | `[CONFIRM: e.g., executive summary + full issue list]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Risk-rating scheme | `[CONFIRM: e.g., High / Medium / Low; hardcore indicators always rated for immediate escalation]` |
| Source-citation convention | `[CONFIRM: e.g., document / section / page reference required on every extracted term or communication]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged & Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- Do reviewers expect triage tables keyed to the risk-indicators reference?
- How should agents label and route outputs that quote business documents or communications?

---

## Source-of-Truth Documents

List the authoritative playbooks, policies, and reference materials this group uses. Reference by name and location only — do not paste content.

| Document | Location / Path | Notes |
|---|---|---|
| Antitrust compliance policy | `[CONFIRM: file name and location]` | Benchmark for `skills/antitrust-competition/antitrust-compliance-policy-review/SKILL.md` |
| Clean-team protocol template | `[CONFIRM: file name and location]` | Used with `skills/antitrust-competition/information-sharing-clean-team-review/SKILL.md` and `skills/antitrust-competition/gun-jumping-clean-team-checklist/SKILL.md` |
| Information-sharing guidelines | `[CONFIRM: file name and location]` | |
| Trade-association participation guidelines | `[CONFIRM: file name and location]` | Used with `skills/antitrust-competition/trade-association-meeting-review/SKILL.md` |
| Merger-review / deal playbook | `[CONFIRM: file name and location]` | Used with `skills/antitrust-competition/merger-antitrust-issue-spotter/SKILL.md` |
| Document-drafting / communications hygiene guidance | `[CONFIRM: file name and location]` | |
| Risk-indicators reference | `skills/antitrust-competition/references/risk-indicators.md` | Canonical AgentCounsel reference |

**Guiding prompts for this section:**
- Where do the compliance policy, clean-team forms, and trade-association guidelines live, and which versions are authoritative?
- Is there standing guidance on drafting language in deal and business documents?

---

## Standard Positions / Playbooks

Record the group's default protocols. An agent uses these to flag deviations and always defers final judgment to an attorney. Nothing in this table states what the law permits — legality, reportability, and safe-harbor questions are always counsel determinations.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Hardcore indicators | `[CONFIRM: e.g., always an immediate escalation; no drafting or analysis continues until counsel directs]` | |
| Competitor information exchange | `[CONFIRM: default safeguards — e.g., aggregation, historical-only data, independent intermediary — as the group's starting protocol; adequacy confirmed by counsel per matter]` | `[VERIFY current law / jurisdiction]` |
| Clean-team defaults | `[CONFIRM: membership rules, firewalls, data handling, and document-labeling conventions]` | |
| Trade-association participation | `[CONFIRM: e.g., agenda in advance, counsel review of sensitive topics, exit-and-report protocol for improper discussions]` | |
| Pricing-algorithm governance | `[CONFIRM: intake and counsel review required before deployment or material change]` | Used with `skills/antitrust-competition/pricing-algorithm-risk-triage/SKILL.md` |
| Distribution / resale terms | `[CONFIRM: which restraint types require counsel review before proposal or acceptance]` | Used with `skills/antitrust-competition/distribution-restraints-review/SKILL.md` |
| Exclusivity / MFN terms | `[CONFIRM: which exclusivity, MFN, or parity terms require counsel review]` | Used with `skills/antitrust-competition/exclusivity-mfn-pricing-review/SKILL.md` |
| Pre-signing / pre-closing conduct | `[CONFIRM: default conduct covenants and integration-planning guardrails until closing]` | |
| Filing-question routing | `[CONFIRM: who assesses reportability; the agent only assembles the facts counsel requests]` | |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- What safeguards does the group treat as its starting protocol for any competitor information flow?
- What conduct is permitted, and what is off-limits, for deal teams between signing and closing under the group's playbook?
- Which contract terms always route to counsel before they are proposed or accepted?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Antitrust risk intake or triage output | `[CONFIRM: role]` | All; no exceptions |
| Competitor-collaboration or information-sharing review | `[CONFIRM: role]` | All; before any exchange or collaboration proceeds |
| Distribution-restraints or exclusivity/MFN review | `[CONFIRM: role]` | All; before terms are proposed or accepted |
| Merger antitrust issue-spotter output | `[CONFIRM: role]` | All; filing decisions are counsel and specialist work |
| Gun-jumping / clean-team checklist | `[CONFIRM: role]` | Before any pre-closing coordination step |
| Trade-association meeting review | `[CONFIRM: role]` | Before attendance or on any flagged conduct |
| Pricing-algorithm risk triage | `[CONFIRM: role]` | Before deployment or material change |
| Any output touching a legality, filing, or clearance question | Partner-level and/or specialist counsel | Always |

**Guiding prompts for this section:**
- Which deliverables always require partner-level or specialist review?
- How are urgent hardcore-indicator escalations reviewed and documented?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| Conduct is lawful, or unlawful | Legality is a counsel determination; the agent organizes facts and flags indicators |
| A transaction is, or is not, reportable | Filing analysis is attorney and specialist work in every regime |
| A safe harbor, exemption, or threshold applies | Applicability is jurisdiction-specific and changes; `[VERIFY current law / jurisdiction]` |
| A market definition or market share | `[ATTORNEY TO CONFIRM: market definition]`; shares depend on the defined market |
| Conduct receives per-se or rule-of-reason treatment | Characterization is a legal conclusion |
| The parties are not competitors | Competitive posture must be confirmed per market, per matter |
| Shared information is public or competitively harmless | Provenance, granularity, and sensitivity must be confirmed |
| Enforcement is unlikely | Enforcement likelihood is never predicted |
| An information flow through a vendor is insulated | Hub-and-spoke exposure must be assessed by counsel |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill. The loading order is: `core/` rules first, then this profile, then the skill.

For a guided, question-by-question setup process, use the cold-start interview skill at `skills/setup/antitrust-competition-cold-start-interview/SKILL.md`. That skill walks through each section of this profile and produces a draft-completed version for attorney review.

Do not include client names, counterparty names, matter-specific facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
