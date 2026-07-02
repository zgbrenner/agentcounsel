> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in. The Insurance skills produce draft work product for a qualified, licensed attorney to review — never coverage determinations, claim decisions, reserve calculations, or bad-faith conclusions.

# Practice Profile: Insurance

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Insurance (coverage, claims, and policy review) |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Policy interpretation, notice rules, claim-handling standards, and bad-faith standards vary by jurisdiction and are never stated by the agent as settled — `[verify jurisdiction]`. Agents gate every jurisdiction-specific point on this list and flag anything outside it for attorney escalation.

| Field | Value |
|---|---|
| Primary Jurisdictions | `[CONFIRM: states or regions where coverage and claim matters typically arise]` |
| Governing Law of Policies Reviewed | `[CONFIRM: typical governing law, or "policy-dependent — confirmed per matter"]` |
| Admitted / Surplus-Lines Considerations | `[CONFIRM: whether placements involve surplus-lines markets and how that is flagged]` |
| Cross-Border Programs | `[CONFIRM: yes/no; if yes, note local-counsel and broker coordination]` |

**Guiding prompts for this section:**
- In which jurisdictions do the group's coverage disputes and claims typically arise?
- How is the governing law of a policy confirmed before any issue-spotting begins?
- Which placements involve surplus-lines or cross-border markets, and who coordinates them?

---

## Client / Team Context

| Field | Value |
|---|---|
| Typical Party Posture | `[CONFIRM: insurer-side, insured-side, additional insured, claimant-side, coverage counsel, defense counsel — the user's role is confirmed at intake, never assumed]` |
| Internal Clients Served | `[CONFIRM: e.g., risk management, claims, procurement, treasury]` |
| Typical Policy Types / Lines | `[CONFIRM: e.g., commercial general liability, property, professional liability, directors and officers, auto, umbrella/excess, cyber]` |
| Typical Matter Types | `[CONFIRM: e.g., policy review, coverage issue-spotting, tenders, reservation of rights, bad-faith risk triage, certificates of insurance, contract insurance requirements, subrogation, renewal diligence]` |
| Team Composition | `[CONFIRM: partners, associates, paralegals, risk analysts]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight of AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how matters reach the group; intake requires the policy or summary, claim facts, user role, claim stage, and jurisdiction]` |

**Guiding prompts for this section:**
- Which side does the group most often represent, and how is the user's role confirmed per matter?
- Who is the designated supervising attorney for AI-assisted coverage work?
- Does the group use a policy repository or COI tracking system?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops. `skills/insurance/insurance-requirements-contract-review/SKILL.md` benchmarks against this table when this profile is loaded.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Request for a coverage determination | Coverage, duty to defend, and duty to indemnify are never determined by the agent | `[CONFIRM: role or name]` |
| Reservation of rights received or contemplated | `[CONFIRM: escalate on receipt; sufficiency and timeliness never assessed by the agent]` | `[CONFIRM: role or name]` |
| Bad-faith indicator | Themes organized neutrally — never an accusation or an exoneration; jurisdictional standards never stated | `[CONFIRM: role or name]` |
| Late-notice or notice-timing question | Consequences never concluded; `[verify jurisdiction]` | `[CONFIRM: role or name]` |
| Claim decision (approve / deny / settle) | Never made or recommended as final by the agent | `[CONFIRM: role or name]` |
| Tender decision or response | Tender validity never concluded | `[CONFIRM: role or name]` |
| Any outbound insurer / insured / claimant communication | Drafted only; never approved for sending by the agent | `[CONFIRM: role or name]` |
| Counterparty coverage below the Standard Positions floors | `[CONFIRM: escalate any limit, endorsement, or rating below the tables below]` | `[CONFIRM: role or name]` |
| Carrier rating below floor | `[CONFIRM: any carrier below the group's financial-strength floor]` | `[CONFIRM: role or name]` |
| Any deadline, notice period, or limitations date | Never computed by the agent | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` |
| Any term outside the known playbook | `[CONFIRM: agent flags and pauses rather than improvising — flagged "not addressed by playbook"]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- Who owns coverage-position questions the moment one is asked?
- What is the routing when a reservation-of-rights letter arrives?
- Which shortfalls against the Standard Positions tables require escalation rather than a simple flag?

---

## Preferred Output Style

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., policy summary table, coverage issue-spotter matrix, chronology, tracker, review memo]` |
| Tone | `[CONFIRM: e.g., plain business language, formal legal prose; bad-faith themes always framed neutrally]` |
| Length convention | `[CONFIRM: e.g., executive summary + full matrix]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Risk-rating scheme | `[CONFIRM: e.g., High / Medium / Low]` |
| Source-citation convention | `[CONFIRM: e.g., cite to page, form number, endorsement number, section, or claim document on every extracted term]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- How should agents cite an extracted policy term — form, endorsement, section, page?
- How are neutral bad-faith-theme write-ups distinguished from advocacy documents?

---

## Source-of-Truth Documents

List the authoritative materials this group uses. Reference by name and location only — do not paste content.

| Document | Location / Path | Notes |
|---|---|---|
| Insurance-requirements playbook | `[CONFIRM: file name and location]` | Benchmark for `skills/insurance/insurance-requirements-contract-review/SKILL.md` |
| Standard contract insurance exhibit / template | `[CONFIRM: file name and location]` | |
| COI tracking system | `[CONFIRM: system name]` | Used with `skills/insurance/certificate-of-insurance-review/SKILL.md` |
| Policy repository (policies, endorsements, dec pages) | `[CONFIRM: system name]` | The policy itself is always the source; a certificate is never a substitute |
| Claims-handling guidelines | `[CONFIRM: file name and location]` | |
| Broker / placement contacts and renewal calendar | `[CONFIRM: file name or system name]` | Renewal dates attorney- or broker-verified; never computed |
| Output patterns | `skills/insurance/references/output-patterns.md` | Canonical AgentCounsel reference |

**Guiding prompts for this section:**
- Where is the authoritative copy of each policy and endorsement kept?
- Who owns the renewal calendar, and who verifies its dates?

---

## Standard Positions / Playbooks

The group's starting requirements for contract insurance provisions. `skills/insurance/insurance-requirements-contract-review/SKILL.md` benchmarks counterparty requirements against this table when this profile is loaded; anything the table does not address is flagged "not addressed by playbook." Every figure is the organization's own fill-in — not a market standard and not a legal requirement.

| Requirement | Group's Default Position | Notes / Conditions |
|---|---|---|
| Commercial general liability — minimum limits | `[CONFIRM: $[X] per occurrence / $[X] aggregate]` | `[CONFIRM: when higher limits are required]` |
| Automobile liability — minimum limits | `[CONFIRM: $[X] combined single limit]` | |
| Workers' compensation / employer's liability | `[CONFIRM: as required by applicable law — [verify jurisdiction] — plus $[X] employer's liability]` | |
| Umbrella / excess — minimum limits | `[CONFIRM: $[X]; when required]` | |
| Professional liability / E&O | `[CONFIRM: when required and minimum $[X]]` | |
| Cyber liability | `[CONFIRM: when required and minimum $[X]]` | |
| Additional-insured status | `[CONFIRM: when required and by what endorsement scope — e.g., ongoing and completed operations]` | Status is confirmed from the endorsement, never from a certificate |
| Waiver of subrogation | `[CONFIRM: when required and for which lines]` | |
| Primary and non-contributory wording | `[CONFIRM: when required]` | |
| Carrier financial-strength rating floor | `[CONFIRM: minimum rating and the named rating agency]` | |
| Notice of cancellation | `[CONFIRM: required notice period and mechanism]` | |
| COI collection and tracking | `[CONFIRM: cadence and system; a certificate is never treated as proof of policy terms]` | |

**Guiding prompts for this section:**
- What minimum limits does the group require by line, and when do higher-risk contracts require more?
- Which endorsements must be sighted — not just referenced on a certificate — before a requirement is marked satisfied?
- What carrier-rating floor does the group apply, and from which rating agency?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Policy summary or coverage issue-spotter output | `[CONFIRM: role]` | All; coverage conclusions are attorney work |
| Coverage position outline | `[CONFIRM: role]` | All; before any position is communicated |
| Tender letter or reservation-of-rights review | `[CONFIRM: role]` | All; before any response |
| Bad-faith risk triage | `[CONFIRM: role — senior]` | All; neutral framing verified by the reviewer |
| COI or contract insurance-requirements review | `[CONFIRM: role]` | Before reliance; endorsement gaps confirmed against policies |
| Claims chronology / subrogation-recovery tracker | `[CONFIRM: role]` | Before reliance; every date attorney-verified |
| Renewal / placement diligence checklist | `[CONFIRM: role]` | Before any binding decision — binding is broker / insured work, never the agent's |
| Any insurer / insured / claimant communication | Partner-level review | Always; drafted only, never sent by the agent |

**Guiding prompts for this section:**
- Which deliverables require senior or partner-level review?
- Who confirms that flagged endorsement gaps were checked against the actual policy?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| A claim is covered, or not covered | Coverage determination is attorney work |
| A duty to defend or indemnify exists, or does not | These are legal conclusions on the policy and the facts |
| An exclusion or endorsement applies, or does not | The policy must be read; application is a legal judgment |
| A certificate of insurance reflects actual coverage | Certificate contents must be confirmed against the policy and endorsements |
| Additional-insured status exists | Must be confirmed from the endorsement itself; its effect is attorney work |
| Notice was timely, or late notice forfeits coverage | Notice consequences are jurisdiction-specific legal questions; `[verify jurisdiction]` |
| Bad faith occurred, or did not occur | Never concluded either way; jurisdictional standards never stated |
| The policy is in force and limits are uneroded | Policy status and remaining limits must be user-supplied or confirmed |
| Renewal terms match expiring terms | Must be compared document to document |
| A deadline, notice period, or limitations date can be computed | Never computed; `[deadline verification required]` |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill. The loading order is: `core/` rules first, then this profile, then the skill. When populated, the Standard Positions and Escalation Thresholds tables are consumed by `skills/insurance/insurance-requirements-contract-review/SKILL.md` as benchmarking inputs.

For a guided, question-by-question setup process, use the cold-start interview skill at `skills/setup/insurance-cold-start-interview/SKILL.md`. That skill walks through each section of this profile and produces a draft-completed version for attorney review.

Do not include insured names, claim facts, policy numbers, matter numbers, confidential facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
