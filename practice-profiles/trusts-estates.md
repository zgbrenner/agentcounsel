> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in. The Trusts & Estates skills produce draft work product for a qualified, licensed attorney to review — never instruments, court forms, or legal conclusions.

# Practice Profile: Trusts & Estates

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Trusts & Estates |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Wills, trusts, probate procedure, fiduciary standards, and marital-property regimes are jurisdiction-specific — `[verify jurisdiction]`. Agents gate every jurisdiction-specific point on this list and flag anything outside it for attorney or local-counsel escalation.

| Field | Value |
|---|---|
| Primary Jurisdictions / Situs | `[CONFIRM: states or regions where the group's matters typically sit]` |
| Probate Courts / Registries | `[CONFIRM: courts where the group regularly appears]` |
| Marital-Property Regime Exposure | `[CONFIRM: whether matters arise under community-property or common-law regimes — treatment is attorney work]` `[verify jurisdiction]` |
| Multi-State / Foreign Assets | `[CONFIRM: how matters with out-of-state or foreign assets are handled and referred]` |
| Local-Counsel Requirement | `[CONFIRM: jurisdictions where local counsel is always engaged]` |

**Guiding prompts for this section:**
- In which jurisdictions does the group plan, probate, and administer, and where is local counsel always engaged?
- How are multi-state and foreign assets identified at intake and routed?
- Which courts' local procedures does the group track, and where is that tracked?

---

## Client / Team Context

This is individual-client work. The core rule `core/capacity-and-vulnerable-parties.md` applies to every matter in this practice and cannot be overridden by this profile.

| Field | Value |
|---|---|
| Client Types | `[CONFIRM: e.g., individuals as testators/grantors, fiduciaries, beneficiaries; family offices]` |
| Typical Client / Fiduciary Roles | `[CONFIRM: e.g., testator/grantor, executor, trustee, agent, guardian, beneficiary, heir, petitioner, contestant — the user's role is confirmed at intake, never assumed]` |
| Typical Matter Types | `[CONFIRM: e.g., estate planning, probate administration, trust administration, fiduciary disputes, estate litigation, estate-tax intake]` |
| Team Composition | `[CONFIRM: partners, associates, paralegals, trust administrators]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight of AI-assisted work]` |
| Vulnerable-Party Screening | `[CONFIRM: how intake screens for capacity concerns, potential undue influence, safety risks, minors, and unrepresented individuals — per core/capacity-and-vulnerable-parties.md]` |
| Matter-Intake Process | `[CONFIRM: how matters reach the group]` |

**Guiding prompts for this section:**
- Who is the designated supervising attorney for AI-assisted work with individual clients?
- What does intake ask to surface capacity, influence, and safety concerns early?
- How does the group confirm whether a party is represented?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops. Under `core/capacity-and-vulnerable-parties.md`, agents never assess capacity, undue influence, coercion, or abuse, and safety concerns surface immediately at the top of any output — never buried in a checklist.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Capacity concern indicated | Facts bearing on capacity are organized, never assessed; any indication routes to the attorney | `[CONFIRM: role — per core/capacity-and-vulnerable-parties.md]` |
| Undue-influence / coercion / abuse indicator | Isolation, dependency, a new beneficiary, caregiver involvement in document changes — flagged as facts for attorney evaluation, never labeled as conclusions | `[CONFIRM: role — escalate immediately]` |
| Safety risk (elder abuse, self-harm, violence) | Immediate escalation; surfaced at the top of the output | `[CONFIRM: role — immediate]` |
| Minor involved in the matter | Facts organized for the attorney only; no output framed as advice to or assessment of a child | `[CONFIRM: role]` |
| Apparently unrepresented individual | `[CONFIRM: flag and route; output is a draft for attorney review, never final advice]` | `[CONFIRM: role]` |
| Fiduciary self-dealing or conflict indicator | `[CONFIRM: escalation criteria]` | `[CONFIRM: role or name]` |
| Beneficiary dispute or contest indicator | `[CONFIRM: escalation criteria]` | `[CONFIRM: role or name]` |
| Document-validity or which-instrument-controls question | Never determined by the agent | `[CONFIRM: role or name]` |
| Estate, gift, or transfer-tax question | Routed to a qualified tax professional; never computed | `[CONFIRM: role or name]` |
| Any date or deadline | Never computed by the agent | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` |
| Asset distribution or fiduciary-action decision | `[CONFIRM: escalate before any action]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- What is the immediate routing when a safety concern surfaces mid-task?
- Who evaluates capacity and influence facts once the agent has organized them?
- How are tax questions handed off, and to whom?

---

## Preferred Output Style

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., intake summary, document summary, inventory table, task tracker, facts chronology]` |
| Tone | Plain language — individual clients read these deliverables — without sliding into advice, per `core/capacity-and-vulnerable-parties.md` |
| Length convention | `[CONFIRM: e.g., executive summary + full table]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Source-citation convention | `[CONFIRM: e.g., document / section / page reference on every extracted term]` |
| Sensitive-identifier handling | Mask SSNs, account numbers, and dates of birth by default; medical detail minimized and recorded only as a provided document states it |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- How does the group balance plain language for individual clients with the no-advice rule?
- Are there additional identifiers or medical details the group masks by default?

---

## Source-of-Truth Documents

List the authoritative materials this group uses. Reference by name and location only — do not paste content.

| Document | Location / Path | Notes |
|---|---|---|
| Estate-planning intake form / questionnaire | `[CONFIRM: file name and location]` | Used with `skills/trusts-estates/estate-planning-intake/SKILL.md` |
| Precedent instrument library | `[CONFIRM: referenced by name; the agent never generates wills, trusts, or court forms]` | |
| Probate checklists by court | `[CONFIRM: file name and location]` | Used with `skills/trusts-estates/probate-document-checklist/SKILL.md` |
| Fiduciary-duty playbook | `[CONFIRM: file name and location]` | Used with `skills/trusts-estates/fiduciary-duty-issue-spotter/SKILL.md` |
| Trust-administration procedures | `[CONFIRM: file name and location]` | Used with `skills/trusts-estates/trust-administration-tracker/SKILL.md` |
| Capacity and vulnerable parties core rule | `core/capacity-and-vulnerable-parties.md` | Core operating rule; applies to every matter; cannot be overridden by this profile |
| Output patterns | `skills/trusts-estates/references/output-patterns.md` | Canonical AgentCounsel reference |

**Guiding prompts for this section:**
- Where do the group's intake forms, precedent instruments, and court checklists live?
- Which version of each playbook is authoritative, and who owns it?

---

## Standard Positions / Playbooks

Record the group's default working rules. An agent uses these to flag deviations and always defers final judgment to an attorney.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Capacity and vulnerability screening | `[CONFIRM: screening performed at intake on every matter]` | Per `core/capacity-and-vulnerable-parties.md` |
| Medical and cognitive facts | Recorded only as stated in provided documents; never characterized beyond the source | |
| Safety-first escalation | `[CONFIRM: routing; only user-provided emergency or hotline resources are included — never invented]` | |
| No outcome predictions about people | Rulings on capacity, guardianship, or contests are never predicted; factors and facts are organized, the weighing is the attorney's | |
| Beneficiary-designation reconciliation | `[CONFIRM: designations compared against provided instruments; which controls is attorney work]` | Used with `skills/trusts-estates/beneficiary-designation-review/SKILL.md` |
| Fiduciary red flags framed as questions | Dependency, self-dealing, co-fiduciary disputes, beneficiary objections — framed for attorney evaluation, never as conclusions | |
| Asset-inventory conventions | `[CONFIRM: which asset and liability fields are collected and how sources are cited]` | Used with `skills/trusts-estates/asset-liability-inventory-builder/SKILL.md` |
| Plain-language default | `[CONFIRM: reading level and formatting conventions for client-facing drafts]` | Never slides into advice |
| Review tier for vulnerable-party matters | `[CONFIRM: e.g., partner-level review on any matter with a capacity, influence, or safety flag]` | |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- What does the group's intake screening ask on every matter?
- How are influence and self-dealing indicators phrased so they remain facts, not conclusions?
- What elevated review applies when a vulnerability flag is present?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, filed, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Estate-planning intake summary | `[CONFIRM: role]` | All; no exceptions |
| Estate document summary / asset-liability inventory | `[CONFIRM: role]` | All; no exceptions |
| Capacity / undue-influence facts organization | `[CONFIRM: role — supervising attorney or partner]` | All; facts only — conclusions are attorney work |
| Fiduciary-duty issue-spotter output | `[CONFIRM: role]` | All |
| Probate checklist / post-death task tracker | `[CONFIRM: role]` | Before reliance; every deadline attorney-verified |
| Trust administration / funding tracker | `[CONFIRM: role]` | Before reliance |
| Estate-litigation facts chronology | `[CONFIRM: role]` | Before use in any proceeding |
| Estate-tax issue intake | Qualified tax professional | Before any tax reliance |
| Any matter with a capacity, vulnerability, or safety flag | `[CONFIRM: partner-level]` | Always; per `core/capacity-and-vulnerable-parties.md` |

**Guiding prompts for this section:**
- Which deliverables require partner-level review rather than the supervising associate?
- How is the reviewing attorney alerted to a vulnerability flag before reading the body of the draft?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| A person has, or lacks, capacity | A legal and sometimes medical judgment; never assessed — per `core/capacity-and-vulnerable-parties.md` |
| Undue influence, coercion, or abuse occurred, or did not | Facts are flagged as indicators; the conclusion is the attorney's |
| A document is valid, or which instrument controls | Validity and priority of instruments are legal determinations |
| Heirship or beneficiary entitlement | Entitlement is a legal determination on confirmed facts; `[verify jurisdiction]` |
| A fiduciary breached, or did not breach, a duty | Breach and liability are legal conclusions |
| The client is the user, or a party is represented | Roles and representation status are confirmed at intake |
| Beneficiary designations match the will or trust | Must be reconciled from the provided documents; controlling effect is attorney work |
| A deadline or tax amount can be computed | Never computed; `[deadline verification required]` |
| A medical condition beyond what a provided document states | Medical characterization is never extended by the agent |
| All instruments, amendments, and codicils were provided | Only the documents actually provided control; missing items are flagged |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill. The loading order is: `core/` rules first — including `core/capacity-and-vulnerable-parties.md` — then this profile, then the skill.

For a guided, question-by-question setup process, use the cold-start interview skill at `skills/setup/trusts-estates-cold-start-interview/SKILL.md`. That skill walks through each section of this profile and produces a draft-completed version for attorney review.

Do not include client names, family details, asset values, identifiers, medical facts, matter numbers, or privileged analysis in this profile. This is a configuration document, not a work-product file.
