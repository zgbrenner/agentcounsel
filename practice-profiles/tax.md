> **Internal practice-group configuration reference. This is not legal work product, legal advice, or tax advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney or qualified tax professional before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in. The Tax skills produce draft work product for qualified tax counsel or a licensed tax professional to review — never tax computation, return preparation, filing, or tax advice.

# Practice Profile: Tax

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Tax |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney / Tax Professional | `[CONFIRM: name and credentials of approving reviewer]` |
| Last Reviewed Date | `[CONFIRM: date of last review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Tax rules, rates, thresholds, forms, and filing obligations are regime-specific and change frequently. Agents gate every regime-specific point on this list, never construct a rule or rate from memory, and flag every specific with `[Verify current law]` `[verify jurisdiction]`.

| Field | Value |
|---|---|
| Federal / National Regimes | `[CONFIRM: the national tax regimes the group works under]` `[Verify current law]` |
| State / Provincial / Local Regimes | `[CONFIRM: list, or "multistate — confirmed per matter"]` `[verify jurisdiction]` |
| Foreign / Cross-Border Regimes | `[CONFIRM: list or "none at this time"; treaty questions routed to specialists]` |
| Tax Types In Scope | `[CONFIRM: e.g., income, sales/use, employment, transfer, digital-asset reporting]` |
| Out-of-Scope Regimes | `[CONFIRM: regimes always routed to outside specialists]` |

**Guiding prompts for this section:**
- In which jurisdictions does the group regularly handle tax matters, and which are always referred out?
- Which tax types does the group triage, and which go straight to specialists?
- How does the group confirm which jurisdiction's rules a matter implicates before any work begins?

---

## Client / Team Context

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., finance, payroll, corporate development, treasury]` |
| Typical Taxpayer / Entity Types | `[CONFIRM: e.g., individual, C corp, S corp, partnership, LLC, trust, estate, nonprofit]` |
| Typical Matter Types | `[CONFIRM: e.g., transaction diligence, entity setup, sales/use tax, employment tax, cross-border, digital assets, contract tax provisions]` |
| Team Composition | `[CONFIRM: tax counsel, licensed tax professionals, accountants, paralegals]` |
| Supervising Attorney / Tax Professional(s) | `[CONFIRM: name(s) with oversight of AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how tax matters reach the group]` |

**Guiding prompts for this section:**
- Who is the designated qualified tax professional for AI-assisted work?
- Which intake facts must be supplied before any tax skill runs — taxpayer type, jurisdiction, tax year or period, activity type?
- How does the group coordinate with outside accountants or return preparers?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops. The first three are the practice's cardinal rules and are never subject to reframing.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Request to compute any tax amount, rate, basis, gain/loss, or exposure | Never done by the agent, under any framing | `[CONFIRM: qualified tax professional]` |
| Request to state or confirm a filing deadline | Never stated; every echoed date flagged | `[CRITICAL — TAX PROFESSIONAL TO VERIFY DEADLINE]` |
| Request to opine that a tax position is correct or valid | Never opined; positions are adopted only by the professional | `[CONFIRM: qualified tax professional]` |
| Nexus or registration determination | `[CONFIRM: facts organized only; the determination is professional work]` | `[CONFIRM: role or name]` |
| Worker-classification determination | `[CONFIRM: facts organized only; classification is professional work]` | `[CONFIRM: role or name]` |
| Entity-classification or election decision | `[CONFIRM: checklist facts only; election decisions are professional work]` | `[CONFIRM: role or name]` |
| Crypto / digital-asset reporting position | `[CONFIRM: intake facts only; reporting positions are professional work]` | `[CONFIRM: role or name]` |
| Any communication with a tax authority | `[CONFIRM: drafted only at counsel's direction; never sent by the agent]` | `[CONFIRM: role or name]` |
| Return preparation or filing request | Out of scope entirely; route to the professional | `[CONFIRM: role or name]` |
| Penalty, interest, or exposure quantification | Never quantified by the agent | `[CONFIRM: role or name]` |
| Any step outside the tax workflow | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- Who receives a matter the moment a computation, deadline, or position question is asked?
- Which matter types are always escalated to outside specialists?
- How are requests that embed a prohibited task inside a permitted one (e.g., "summarize and compute") handled?

---

## Preferred Output Style

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., issue map, triage table, diligence request list, document organizer]` |
| Tone | `[CONFIRM: e.g., plain business language, formal memo prose]` |
| Length convention | `[CONFIRM: e.g., executive summary + full issue map]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Gap-marker convention | Unknown / not found / not provided / ambiguous — gaps are marked, never filled by guess |
| Date handling | Every echoed date flagged `[deadline verification required]`; no deadline ever computed |
| Sensitive-identifier handling | Mask SSN, EIN, TIN, and account numbers by default; full value only where strictly necessary and expressly approved |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- What format do reviewers expect for an issue map versus a diligence request list?
- Are there additional identifiers or figures the group masks by default?

---

## Source-of-Truth Documents

List the authoritative playbooks and reference materials this group uses. Reference by name and location only — do not paste content.

| Document | Location / Path | Notes |
|---|---|---|
| Tax playbook(s) by matter type | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| Rate / threshold / nexus matrices maintained by the group | `[CONFIRM: file name and location]` | Agent never constructs a rate or threshold from memory; `[Verify current law]` |
| Tax calendar | `[CONFIRM: system name]` | Agent never computes deadlines; the professional verifies every date |
| Entity / organizational chart | `[CONFIRM: file name and location]` | Entity types and elections are user-supplied, never inferred |
| Return and workpaper repository | `[CONFIRM: system name]` | Referenced by name; contents never pasted into a profile |
| Diligence request-list precedents | `[CONFIRM: file name and location]` | Used with `skills/tax/transaction-tax-diligence-request-list/SKILL.md` |
| Output patterns | `skills/tax/references/output-patterns.md` | Canonical AgentCounsel reference |

**Guiding prompts for this section:**
- Where do the group's rate matrices and tax calendar live, and who owns their currency?
- Which repository is authoritative for entity classifications and elections?

---

## Standard Positions / Playbooks

Record the group's default working rules. An agent uses these to flag deviations and always defers final judgment to a qualified tax professional. Nothing in this table states what the tax law is — every legal specific carries `[Verify current law]` `[verify jurisdiction]`.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Intake gate before any tax skill | `[CONFIRM: taxpayer/entity type, jurisdiction(s), tax year or period, and activity type required before substantive work]` | Mirrors the Required Inputs of `skills/tax/tax-issue-intake/SKILL.md` |
| User-supplied computations | Recorded as user-supplied, never confirmed or re-computed | |
| Deadline handling | Every echoed date flagged `[deadline verification required]`; deadlines never computed or stated | |
| Position adoption | `[CONFIRM: only the qualified tax professional adopts a position; the agent maps issues and open questions]` | |
| Nexus-triage fact categories | `[CONFIRM: which activity facts are gathered for the professional's nexus analysis]` | Used with `skills/tax/sales-use-tax-nexus-triage/SKILL.md`; determination is professional work |
| Contract tax-provision review conventions | `[CONFIRM: which covenant and indemnity terms are extracted and benchmarked]` | Used with `skills/tax/tax-covenants-indemnities-review/SKILL.md` |
| Entity-classification checklist conventions | `[CONFIRM: which classification facts and election records are collected]` | Used with `skills/tax/entity-tax-classification-checklist/SKILL.md` |
| Worker-classification intake conventions | `[CONFIRM: which engagement facts are organized for the professional]` | Used with `skills/tax/employment-tax-worker-classification-intake/SKILL.md` |
| Identifier masking | Mask SSN, EIN, TIN, and account numbers by default | |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- What intake facts must be on file before any tax skill produces substantive output?
- How are user-supplied figures and computations labeled so they are never mistaken for verified amounts?
- Which extraction conventions does the group use for contract tax provisions?

---

## Attorney Review Requirements

Specify what must be reviewed by qualified tax counsel or a licensed tax professional before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Tax issue intake / issue map | `[CONFIRM: role]` | All; no exceptions |
| Sales/use tax nexus triage | `[CONFIRM: role]` | All; nexus determination is professional work |
| Entity-tax-classification checklist | `[CONFIRM: role]` | Before any election or structuring decision |
| Worker-classification intake | `[CONFIRM: role]` | Classification decision is professional work |
| Tax covenants / indemnities review | `[CONFIRM: role]` | Before negotiation reliance |
| Tax-provision review checklist | `[CONFIRM: role]` | Before reliance |
| International / crypto issue intake | `[CONFIRM: role — specialist where applicable]` | All |
| Any output echoing a date | `[CRITICAL — TAX PROFESSIONAL TO VERIFY DEADLINE]` | Every date, every deliverable |
| Any communication to a tax authority | Partner-level / qualified tax professional | Always; drafted only, never sent by the agent |

**Guiding prompts for this section:**
- Is there a tiered review structure by matter type or exposure?
- Which deliverables always require an outside specialist in addition to the group's reviewer?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| A tax rate, threshold, or form number from memory is current | Rates and thresholds change frequently; `[Verify current law]` |
| A filing deadline | Never stated or computed; `[deadline verification required]` |
| Tax liability or exposure can be computed | Computation is never performed by the agent, under any framing |
| A position is correct or "should" prevail | Position validity is never opined; adoption is professional work |
| Nexus exists, or does not exist | Nexus is a professional determination on confirmed facts; `[verify jurisdiction]` |
| An entity's classification or election status | Must be user-supplied from authoritative records, never inferred |
| A worker's classification | Classification is a professional determination |
| The tax year or period at issue | Must be user-supplied; never defaulted |
| Provided returns or workpapers are complete, filed, or accepted | Status must be confirmed by the professional |
| A treaty or foreign regime applies | Cross-border treatment is specialist work; `[verify jurisdiction]` |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney or qualified tax professional review and approve the completed profile before it is loaded alongside any skill. The loading order is: `core/` rules first, then this profile, then the skill.

For a guided, question-by-question setup process, use the cold-start interview skill at `skills/setup/tax-cold-start-interview/SKILL.md`. That skill walks through each section of this profile and produces a draft-completed version for professional review.

Do not include taxpayer names, identifiers, return data, matter numbers, confidential facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
