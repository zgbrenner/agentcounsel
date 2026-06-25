# Practice Profiles

## What a Practice Profile Is

A practice profile is a fill-in configuration template that a legal practice group completes to tell AI agents how that group works. Each profile records the group's jurisdictions, client context, escalation thresholds, preferred output style, source-of-truth documents, standard positions, attorney review requirements, and things an agent must never assume.

Practice profiles are **not** legal work product and are **not** legal advice. They are internal configuration documents. They must not contain privileged material, client-sensitive facts, or confidential matter information. Source-of-truth documents are referenced by name and location — never pasted in.

Each profile must be reviewed and approved by a supervising attorney before it is loaded alongside any skill.

---

## How an Agent Uses a Completed Profile

When an agent receives a task in a practice area, load the completed profile for that group alongside the `core/` rules and the chosen skill. The profile tells the agent:

- Which jurisdictions are in scope and which require escalation to local counsel.
- Who supervises the work and how escalation is routed.
- The dollar thresholds, risk levels, and matter types that require a human to intervene before the agent proceeds.
- The formatting and tone conventions the group expects in its deliverables.
- Where the group's authoritative playbooks and templates live, so the agent references them by name rather than guessing at positions.
- The group's default negotiating or analytical positions, so deviations from playbook can be flagged.
- What must be reviewed by an attorney before any deliverable is used, sent, or relied upon.
- The specific facts, classifications, and conclusions the agent must never assume and must always surface for human confirmation.

The loading order is: `core/` rules first, then the practice profile, then the skill. The `core/` rules are operating constraints that the profile cannot override. The profile configures; the skill executes; the `core/` rules bound both.

---

## Skills That Use This Profile

The following ~20 non-setup skills explicitly consume profile data when a populated profile is loaded alongside them. Each skill's Required Inputs lists the profile as optional, and the skill's Workflow benchmarks against the profile's Standard Positions, Escalation Thresholds, Source-of-Truth Documents, or Preferred Output Style as relevant. Skills not listed here are unaffected by the profile's presence; they do not consume it.

| Practice area | Skills that consume the profile |
|---|---|
| `ai-governance.md` | `skills/ai-governance/ai-vendor-terms-review/SKILL.md`, `skills/ai-governance/employee-ai-policy/SKILL.md` |
| `contracts.md` | `skills/contracts/contract-risk-review/SKILL.md`, `skills/contracts/nda-review/SKILL.md`, `skills/contracts/sow-review/SKILL.md` |
| `corporate.md` | `skills/corporate/board-minutes/SKILL.md`, `skills/corporate/closing-checklist/SKILL.md`, `skills/corporate/entity-compliance/SKILL.md`, `skills/corporate/written-consent/SKILL.md` |
| `employment.md` | `skills/employment/employee-policy-review/SKILL.md`, `skills/employment/hiring-review/SKILL.md` |
| `insurance.md` | `skills/insurance/insurance-requirements-contract-review/SKILL.md` |
| `litigation.md` | `skills/litigation/brief-section-drafter/SKILL.md` |
| `privacy.md` | `skills/privacy/dpa-review/SKILL.md`, `skills/privacy/dsar-workflow/SKILL.md`, `skills/privacy/pia-generation/SKILL.md`, `skills/privacy/privacy-policy-gap-review/SKILL.md` |
| `regulatory.md` | `skills/regulatory/compliance-gap-matrix/SKILL.md`, `skills/regulatory/compliance-program-tracker/SKILL.md` |

Other profiles (`antitrust-competition`, `bankruptcy-restructuring`, `family-law`, `ip`, `m-and-a`, `product-legal`, `real-estate`, `securities-capital-markets`, `tax`, `trusts-estates`) exist as configuration scaffolds and are populated by their cold-start interviews, but no skill currently consumes them. A skill will be wired to one of these profiles in a future PR if and when its workflow grows a benchmark-against-standing-position step.

---

## How to Use a Populated Profile Alongside a Skill

A practice profile is a single Markdown file. To use it alongside a skill:

1. Populate `practice-profiles/<area>.md` once — either by running the cold-start interview at `skills/setup/<area>-cold-start-interview/SKILL.md`, or by editing the file directly. Have a supervising attorney review and approve the populated profile.

2. When running a skill that uses profile data (see the list above), include the populated profile in your AI workspace alongside the skill:
   - **For platform packs:** the profile is uploaded as a separate file in the same project.
   - **For Claude Code:** place the profile in the same directory the skill is loaded from.
   - **For file-by-file workflows:** paste the profile into the conversation before the skill's Required Inputs.

3. The skill detects the profile by its filename pattern (`practice-profiles/<area>.md`) and uses its Standard Positions, Escalation Thresholds, Source-of-Truth Documents, and Preferred Output Style tables as benchmarking inputs. Skills not on the list above do not consume the profile and are unaffected by its presence.

Profile is always optional. Running a skill without a profile is the default behavior and does not degrade output quality — it only removes benchmarking against the group's standing positions. See `CONFIGURING.md` at the repository root for the full configuration guide.

---

## The Privilege Caution

Practice profiles configure behavior. They are not work-product files. Treating them otherwise risks mixing configuration with privileged analysis, which creates both a privilege-management problem and an operational problem (a configuration file full of client facts is not reusable).

Keep profiles generic. Record positions, thresholds, and process rules — not facts about specific matters, clients, or transactions. If a profile field cannot be answered without disclosing privileged or client-sensitive information, record only the abstract rule and keep the specific facts in the matter file, not in the profile.

The privilege analysis for any deliverable a profile helps to produce belongs in the deliverable itself, not in the profile.

---

## Relationship to Cold-Start Interview Skills

Every practice-area profile has a matching cold-start interview skill under `skills/setup/`. Those skills walk a practice group through setting up the profile by asking guided questions and producing a draft-completed version for attorney review:

| Profile | Cold-Start Interview Skill |
|---|---|
| `practice-profiles/contracts.md` | `skills/setup/contracts-cold-start-interview/SKILL.md` |
| `practice-profiles/litigation.md` | `skills/setup/litigation-cold-start-interview/SKILL.md` |
| `practice-profiles/privacy.md` | `skills/setup/privacy-cold-start-interview/SKILL.md` |
| `practice-profiles/corporate.md` | `skills/setup/corporate-cold-start-interview/SKILL.md` |
| `practice-profiles/employment.md` | `skills/setup/employment-cold-start-interview/SKILL.md` |
| `practice-profiles/ip.md` | `skills/setup/ip-cold-start-interview/SKILL.md` |
| `practice-profiles/ai-governance.md` | `skills/setup/ai-governance-cold-start-interview/SKILL.md` |
| `practice-profiles/m-and-a.md` | `skills/setup/m-and-a-cold-start-interview/SKILL.md` |
| `practice-profiles/tax.md` | `skills/setup/tax-cold-start-interview/SKILL.md` |
| `practice-profiles/trusts-estates.md` | `skills/setup/trusts-estates-cold-start-interview/SKILL.md` |
| `practice-profiles/real-estate.md` | `skills/setup/real-estate-cold-start-interview/SKILL.md` |
| `practice-profiles/securities-capital-markets.md` | `skills/setup/securities-capital-markets-cold-start-interview/SKILL.md` |
| `practice-profiles/regulatory.md` | `skills/setup/regulatory-cold-start-interview/SKILL.md` |
| `practice-profiles/antitrust-competition.md` | `skills/setup/antitrust-competition-cold-start-interview/SKILL.md` |
| `practice-profiles/bankruptcy-restructuring.md` | `skills/setup/bankruptcy-restructuring-cold-start-interview/SKILL.md` |
| `practice-profiles/insurance.md` | `skills/setup/insurance-cold-start-interview/SKILL.md` |
| `practice-profiles/family-law.md` | `skills/setup/family-law-cold-start-interview/SKILL.md` |
| `practice-profiles/product-legal.md` | `skills/setup/product-legal-cold-start-interview/SKILL.md` |
| `practice-profiles/financial-crime.md` | `skills/setup/financial-crime-cold-start-interview/SKILL.md` |

The four hand-authored interviews — contracts, litigation, privacy, corporate — are maintained as standalone Markdown files. The remaining fourteen are generated from `scripts/generate_cold_start_interviews.py`; edit the per-area question bank in that script (not the SKILL.md output) and rerun the generator to refresh them.

### Practice-Area Skill Dirs That Do Not Have a Profile

Two skill directories under `skills/` do not have a corresponding practice profile in this directory and are not represented in the interview table above:

- `skills/legal-research/` — a single cross-cutting research skill (`legal-research-memo`) that runs independently of any practice group's positions or playbooks. The skill is configured by the supervising attorney at the matter level, not by a group-level profile.
- `skills/financial-crime/` — KYC and sanctions / PEP / adverse-media review skills. These are sector-specific compliance workflows whose configuration depends on the regulated entity's program rather than on a litigation- or contracts-style practice-group profile, and the cluster has not yet been authored for profile-driven use.

Two other top-level skill directories — `skills/legal-methodology/` and `skills/legal-ops/` — are cross-cutting supporting groups that intentionally do not carry practice profiles either; they are configured per-matter rather than per-practice.

---

## No Backend, Runtime, or Vendor Dependency

Practice profiles are plain Markdown files. They require no database, no authentication system, no API, and no vendor-specific tooling. A completed profile is loaded into an agent session the same way any other Markdown file in this library is loaded — by including it in the context alongside `core/` and the chosen skill.

This design is intentional. The library has no backend and no runtime. Configuration travels with the work, in the same format as everything else, readable and editable by any attorney with a text editor.

---

## Files in This Directory

| File | Practice Area |
|---|---|
| `contracts.md` | Contracts — review, drafting, negotiation |
| `litigation.md` | Litigation — civil disputes, arbitration, pre-litigation |
| `corporate.md` | Corporate — transactions, governance, entity work |
| `employment.md` | Employment — workforce, classification, separation |
| `privacy.md` | Privacy and data protection |
| `product-legal.md` | Product legal — launch gates, product features, terms |
| `regulatory.md` | Regulatory — compliance, agency matters, licensing |
| `ai-governance.md` | AI governance — model risk, prohibited use cases, AI compliance |
| `ip.md` | Intellectual property — patents, trademarks, copyright, licensing |
| `tax.md` | Tax — issue intake, diligence, tax-provision and nexus triage workflows |
| `insurance.md` | Insurance — coverage, claims, policy review, tender, and recovery workflows |
| `m-and-a.md` | Mergers & acquisitions — diligence, signing, closing, integration |
| `securities-capital-markets.md` | Securities and capital markets — offerings, periodic reporting, disclosure |
| `real-estate.md` | Real estate — acquisitions, leasing, financing, title and zoning |
| `trusts-estates.md` | Trusts and estates — planning, administration, fiduciary matters |
| `bankruptcy-restructuring.md` | Bankruptcy and restructuring — cases, claims, plans, distressed M&A |
| `antitrust-competition.md` | Antitrust / competition — clearance, counseling, investigation defense |
| `family-law.md` | Family law — matter intake, custody, support, settlements, safety screening |

