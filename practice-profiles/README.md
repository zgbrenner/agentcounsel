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

## The Privilege Caution

Practice profiles configure behavior. They are not work-product files. Treating them otherwise risks mixing configuration with privileged analysis, which creates both a privilege-management problem and an operational problem (a configuration file full of client facts is not reusable).

Keep profiles generic. Record positions, thresholds, and process rules — not facts about specific matters, clients, or transactions. If a profile field cannot be answered without disclosing privileged or client-sensitive information, record only the abstract rule and keep the specific facts in the matter file, not in the profile.

The privilege analysis for any deliverable a profile helps to produce belongs in the deliverable itself, not in the profile.

---

## Relationship to Cold-Start Interview Skills

Four practice-area profiles have a matching cold-start interview skill under `skills/setup/`. Those skills walk a practice group through setting up the profile by asking guided questions and producing a draft-completed version for attorney review:

| Profile | Cold-Start Interview Skill |
|---|---|
| `practice-profiles/contracts.md` | `skills/setup/contracts-cold-start-interview/SKILL.md` |
| `practice-profiles/litigation.md` | `skills/setup/litigation-cold-start-interview/SKILL.md` |
| `practice-profiles/privacy.md` | `skills/setup/privacy-cold-start-interview/SKILL.md` |
| `practice-profiles/corporate.md` | `skills/setup/corporate-cold-start-interview/SKILL.md` |

The remaining profiles — `employment.md`, `product-legal.md`, `regulatory.md`, `ai-governance.md`, and `ip.md` — are populated directly by the practice group with the supervising attorney.

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

