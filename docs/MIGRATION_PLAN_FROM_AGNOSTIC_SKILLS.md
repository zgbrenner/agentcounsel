# Migration Plan — agnostic-skills-for-legal into AgentCounsel

**Status: Phases A, B, and C executed.** This document is the migration plan for bringing content from `agnostic-skills-for-legal` into AgentCounsel. The new-skill phases are complete; remaining work is tracked in **Phase D** below. See **Migration status** for a summary. The original plan text is retained for reference, with status notes added.

> Current totals (practice areas, skill counts) are tracked in [`metadata/index.json`](../metadata/index.json) and summarized in [`README.md`](../README.md). Any specific figures below reflect the state at the time of writing.

## Purpose

`foolish-bandit/agnostic-skills-for-legal` is an existing open-source legal-AI library. This plan compares it against AgentCounsel's canonical `skills/` directory and recommends, in priority order, what content to (A) fold into existing skills, (B) add as new skills, or (C) defer or reject.

## Migration status

_Last updated 2026-05-20._

| Phase | Scope | Status |
|---|---|---|
| A | Improve existing skills | **Partially done** — `nda-review` and `demand-letter` improved (PR #5). The other nine improvement passes were not run; they are carried into Phase D. |
| B | Add missing high-value skills | **Done** — twelve skills added (PRs #6, #7) and quality-checked (PR #8). |
| C | Corporate / M&A practice area | **Done** — six skills added as a new `corporate/` practice area (PR #9), quality-checked (PR #10). |
| D | Newly identified gaps | **Done** — D1 added three new skills; D2 ran the nine Phase A improvement passes. |

At the time this plan was completed, AgentCounsel had 66 canonical skills across 12 practice areas plus two cross-cutting skill groups; it has since grown to 191 skills across 20 practice areas and three cross-cutting groups (see `docs/PRACTICE_AREAS.md`). `THIRD_PARTY_NOTICES.md` records the upstream attribution chain.

A completeness re-check on 2026-05-20 found that `agnostic-skills-for-legal` has **grown** since this plan was first written — it added five `prompts/` files not covered in the analysis below. Those, together with the unrun Phase A passes, are collected in Phase D.

## Source overview

`agnostic-skills-for-legal` packages legal AI workflows into downloadable platform bundles for several AI assistants. It is Apache-2.0 licensed and is itself derived from `anthropics/claude-for-legal`. The content relevant to AgentCounsel:

- `skills/<area>/` — nine broad practice-area scaffolds (each an `instructions.base.md` plus nested `skills/` and `templates/` folders).
- `prompts/<area>/` — roughly fifty granular workflow prompts across six areas: commercial, corporate, employment, ip, litigation, privacy.
- `site/`, `public/`, `platforms/`, `scripts/`, `package.json`, `tsconfig.json` — website and build tooling.

The source's safety model is close to AgentCounsel's: every output is framed as a draft for licensed-attorney review and never as legal advice; unverified authority is tagged for verification; workflows are written jurisdiction-agnostically with explicit out-of-scope gates.

## Method and limitations

This plan was built from the source repository's public file tree, directory listings, and structural summaries of representative files (`nda-review`, `deposition-prep`, `worker-classification`, `AGENTS.md`).

**Verbatim file content was not fully retrieved.** The dispositions below are a routing plan based on file names and structural summaries — not a substitute for reading each file. Before any actual migration, every source file must be read in full and assessed against AgentCounsel's `core/` operating rules.

## License and attribution

Both repositories are Apache-2.0, so migration is license-compatible. Apache-2.0 requires preserving attribution and `NOTICE` content in derivative works. **Any migrated content must carry attribution** to `agnostic-skills-for-legal` and, through it, to `anthropics/claude-for-legal`. Before Phase A or B work begins, add a `NOTICE` file (or per-file provenance notes) recording this chain.

## Architecture note

The source's `skills/<area>` scaffolds are **broad, practice-area-level** instruction sets. AgentCounsel uses **narrow, per-workflow** skills. Migrate from the source's granular `prompts/`, not its broad `skills/`. The broad scaffolds are too wide for AgentCounsel's model and should not be migrated as skills; at most they may be mined for `core/` ideas. Every migration is a **rewrite into AgentCounsel's `SKILL.md` format** — frontmatter plus the eight required sections — never a copy.

## Coverage comparison

Disposition key: **Duplicate** (already covered) · **Improve** (source content should strengthen an existing skill, Phase A) · **New** (missing skill worth adding, Phase B) · **Defer/Reject** (Phase C). Six `cold-start.md` onboarding prompts and all `manifest.json` build files are excluded from every count below — see Phase C.

### Commercial

| Source prompt | AgentCounsel status | Disposition |
|---|---|---|
| `nda-review` | `contracts/nda-review` | Improve (A) — triage rating, practice-profile intake, specialist-routing gate |
| `vendor-agreement-review` | partial — `contracts/contract-risk-review` | New (B) or Improve — vendor-agreement specialization |
| `saas-review` | partial — `contracts/contract-risk-review` | New (B) or Improve — SaaS-agreement specialization |
| `amendment-history` | overlaps `contracts/redline-summary` | Improve (A) — contract-version/amendment tracking |
| `escalation-flagger` | none | Reject (C) — triage utility, not draft legal work product |
| `renewal-tracker` | none | Reject (C) — contract-lifecycle operations, not legal work product |
| `stakeholder-summary` | none | Reject (C) — reporting/communication, not legal work product |

### Corporate

AgentCounsel has **no corporate / M&A practice area.** The whole `prompts/corporate` set (`board-minutes`, `closing-checklist`, `deal-team-summary`, `diligence-issue-extraction`, `entity-compliance`, `integration-management`, `material-contract-schedule`, `tabular-review`, `written-consent`) is **Defer (C)** — see "Practice areas to keep out of scope." `diligence-issue-extraction` and `material-contract-schedule` are contract-adjacent and may inform contracts skills, but corporate as an area is deferred.

### Employment

| Source prompt | AgentCounsel status | Disposition |
|---|---|---|
| `termination-review` | `employment/termination-risk` | Improve (A) — compare and fold in stronger content |
| `handbook-updates` | overlaps `employment/employee-policy-review` | Improve (A) |
| `policy-drafting` | overlaps `employment/employee-policy-review` | Improve (A) |
| `worker-classification` | none | **New (B) — High.** AgentCounsel's `termination-risk` explicitly flags classification as out of scope |
| `hiring-review` | none | New (B) — Medium-High |
| `wage-hour-qa` | none | New (B) — Medium |
| `expansion-kickoff`, `expansion-update` | none | Reject (C) — project-management workflows |

### Intellectual property

| Source prompt | AgentCounsel status | Disposition |
|---|---|---|
| `cease-desist` | none | **New (B) — High.** Fills a known gap (`trademark-clearance-triage` and `dmca-takedown` route away from a cease-and-desist workflow that does not exist) |
| `fto-triage` | none | New (B) — Medium-High — patent freedom-to-operate triage |
| `invention-intake` | none | New (B) — Medium |
| `clearance` | overlaps `ip/trademark-clearance-triage` | Improve (A) or New — broader IP clearance |
| `ip-clause-review` | overlaps `contracts/contract-risk-review` | Improve (A) — IP clauses in contracts |

### Litigation

| Source prompt | AgentCounsel status | Disposition |
|---|---|---|
| `matter-intake` | `litigation/matter-intake` | Improve (A) |
| `chronology` | `litigation/litigation-chronology` | Improve (A) |
| `subpoena` | `litigation/subpoena-triage` | Improve (A) |
| `demand-letter`, `demand-intake`, `demand-draft` | `litigation/demand-letter` | Improve (A) — adopt the source's three-stage intake/draft/letter structure |
| `deposition-prep` | none | **New (B) — High** |
| `legal-hold` | none | **New (B) — High.** `matter-intake` and `subpoena-triage` both reference litigation holds but no skill exists |
| `privilege-log-review` | none | **New (B) — High.** Complements `subpoena-triage` |
| `claim-chart` | none | New (B) — Medium (niche; patent/IP litigation) |
| `brief-section-drafter` | none | New (B) — Medium (drafting-heavy; see risks) |
| `matter-briefing`, `matter-update`, `matter-close`, `oc-status`, `portfolio-status` | none | Reject (C) — matter status and reporting, not draft legal work product |

### Privacy

| Source prompt | AgentCounsel status | Disposition |
|---|---|---|
| `dpa-review` | `privacy/dpa-review` | Improve (A) |
| `dsar-response` | `privacy/dsar-workflow` | Improve (A) |
| `pia-generation` | none | **New (B) — High** — privacy/data-protection impact assessment |
| `reg-gap-analysis` | overlaps `regulatory/compliance-gap-matrix` and `privacy/privacy-policy-gap-review` | Duplicate — Reject (C) unless a content review shows a meaningful gap |
| `use-case-triage` | overlaps `ai-governance/ai-use-case-intake` | Duplicate — Reject (C) unless review shows a meaningful gap |

## Phase A — improve existing skills

Each item below is a comparison-and-improvement pass on an existing AgentCounsel skill, using the named source prompt(s) as input. No new skills are created in Phase A.

**Status: partially complete.** The two High-priority passes — `nda-review` and `demand-letter` — were executed in PR #5. The nine Medium/Low passes below were not run; they are carried into Phase D (section D2). The table is retained for reference.

| Priority | AgentCounsel skill | Source input | What to fold in |
|---|---|---|---|
| High | `contracts/nda-review` | `nda-review` | Triage rating system, a practice-profile intake step, and a gate routing M&A / employment / investment NDAs to specialist counsel |
| High | `litigation/demand-letter` | `demand-intake`, `demand-draft`, `demand-letter` | The source's three-stage structure (intake → draft → letter) for a clearer workflow |
| Medium | `litigation/litigation-chronology` | `chronology` | Record-fidelity and sourcing improvements |
| Medium | `litigation/matter-intake` | `matter-intake` | Intake-completeness and gating improvements |
| Medium | `litigation/subpoena-triage` | `subpoena` | Comparison pass for any stronger triage content |
| Medium | `privacy/dpa-review` | `dpa-review` | Comparison pass |
| Medium | `privacy/dsar-workflow` | `dsar-response` | Comparison pass |
| Medium | `employment/termination-risk` | `termination-review` | Comparison pass |
| Medium | `employment/employee-policy-review` | `handbook-updates`, `policy-drafting` | Handbook-update and policy-drafting review patterns |
| Low | `contracts/redline-summary` | `amendment-history` | Amendment / version-history tracking patterns |
| Low | `contracts/contract-risk-review` | `saas-review`, `vendor-agreement-review`, `ip-clause-review` | Specialization patterns for SaaS, vendor, and IP-clause review |

## Phase B — add missing high-value skills

New skills, rewritten into AgentCounsel's `SKILL.md` format. Priority reflects value and fit with the existing library.

**Status: complete.** All twelve skills below were added (PRs #6 and #7) and quality-checked (PR #8). `vendor-agreement-review` / `saas-review` were not added as separate skills and remain a Phase D item.

| Priority | Proposed skill | Practice area | Source prompt | Notes |
|---|---|---|---|---|
| High | `worker-classification` | employment | `worker-classification` | Fills a gap `termination-risk` explicitly names; source content is strong and jurisdiction-agnostic |
| High | `deposition-prep` | litigation | `deposition-prep` | Strong source content; watch for jurisdiction-specific (England & Wales) passages |
| High | `legal-hold` | litigation | `legal-hold` | Litigation hold / preservation notice; repeatedly referenced by existing skills |
| High | `privilege-log-review` | litigation | `privilege-log-review` | Complements `subpoena-triage` |
| High | `pia-generation` | privacy | `pia-generation` | Privacy / data-protection impact assessment |
| High | `cease-and-desist-response` | ip | `cease-desist` | Fills a gap that two IP skills currently route away from |
| Medium | `hiring-review` | employment | `hiring-review` | Offer / hiring legal review |
| Medium | `fto-triage` | ip | `fto-triage` | Patent freedom-to-operate triage; introduces patent coverage |
| Medium | `invention-intake` | ip | `invention-intake` | Invention disclosure intake |
| Medium | `wage-hour-qa` | employment | `wage-hour-qa` | Wage-and-hour issue triage |
| Medium | `vendor-agreement-review` / `saas-review` | contracts | `vendor-agreement-review`, `saas-review` | Add as skills only if a review shows they need more than `contract-risk-review` already provides; otherwise fold into Phase A |
| Low | `claim-chart` | litigation | `claim-chart` | Niche (patent/IP litigation) |
| Low | `brief-section-drafter` | litigation | `brief-section-drafter` | Drafting-heavy — only with strong attorney-review framing (see risks) |

## Phase C — defer or reject

**Status: resolved.** The corporate / M&A area, originally deferred here, was subsequently built (PR #9). The reject lists below stand.

### Corporate / M&A — built

- **Corporate / M&A / transactional.** Originally deferred; **subsequently built** (PR #9) as a new `corporate/` practice area with six skills: `board-minutes`, `written-consent`, `closing-checklist`, `diligence-issue-extraction`, `material-contract-schedule`, and `entity-compliance`. The four management- or reporting-oriented corporate prompts — `deal-team-summary`, `integration-management`, `tabular-review`, and `cold-start` — remain excluded.

### Reject — not draft legal work product

These are matter-management, status-reporting, or operational workflows. Migrating them would dilute AgentCounsel's focus on draft legal work product for attorney review.

- Litigation: `matter-briefing`, `matter-update`, `matter-close`, `oc-status`, `portfolio-status`.
- Commercial: `escalation-flagger`, `renewal-tracker`, `stakeholder-summary`.
- Employment: `expansion-kickoff`, `expansion-update`.
- Corporate: `tabular-review` and the management-oriented corporate prompts (covered by the deferral above).

### Reject — duplicative

- Privacy `reg-gap-analysis` — covered by `regulatory/compliance-gap-matrix` and `privacy/privacy-policy-gap-review`.
- Privacy `use-case-triage` — covered by `ai-governance/ai-use-case-intake`.

Reconsider only if a full content review shows a genuine, non-duplicative gap.

### Reject — onboarding and build artifacts

- All `cold-start.md` onboarding prompts and `manifest.json` build files — not legal workflows.
- The source's `site/`, `public/`, `platforms/`, `scripts/`, `package.json`, `package-lock.json`, `tsconfig.json`, `.nvmrc` — website and build tooling. AgentCounsel deliberately ships no website, build system, or package manager. Do not migrate any of it.

### Do not migrate as skills — the broad practice-area scaffolds

The source's `skills/<area>/instructions.base.md` scaffolds are too broad for AgentCounsel's narrow per-workflow model. They may be reviewed for `core/` rule ideas only.

## Phase D — newly identified gaps

A completeness re-check on 2026-05-20 surfaced two categories of remaining work: new source prompts added after this plan was written, and Phase A improvement passes that were never run.

### D1 — New source prompts (added to `agnostic-skills-for-legal` after this plan)

**Status: resolved.** `internal-investigation` and `infringement-triage` were built as new skills; `leave-tracker` was built as `protected-leave-review` (reframed from a deadline tracker to a decision-support review, since AgentCounsel does not compute deadlines); `takedown` is covered by the existing `dmca-takedown`; `portfolio` is excluded as a tracking/reporting tool.

| Source prompt | Practice area | Assessment | Recommended disposition |
|---|---|---|---|
| `employment/internal-investigation` | employment | Structuring a workplace internal investigation (misconduct, fraud, whistleblower complaints). No AgentCounsel equivalent. | **New skill — High** |
| `ip/infringement-triage` | ip | First-pass infringement screening across trademark, copyright, patent, and trade secret. Partly overlaps `cease-and-desist-response` and `fto-triage`; needs an overlap analysis before building. | **New skill — Medium-High** |
| `employment/leave-tracker` | employment | Protected-leave deadline decision support. Tracker-style (compare `entity-compliance`); the source is heavily jurisdiction-specific and would need careful jurisdiction-agnostic adaptation. | **New skill — Medium (judgment call)** |
| `ip/takedown` | ip | DMCA send / respond / counter-notice. Already covered by AgentCounsel's existing `dmca-takedown`. | **Duplicate** — optionally mine to refine `dmca-takedown` |
| `ip/portfolio` | ip | IP maintenance-deadline calendar — a tracking and reporting tool, not a drafting or analysis workflow. | **Reject** — consistent with excluding other status/tracking prompts |

### D2 — Phase A improvement passes not yet run

**Status: complete.** All nine passes below were run — each existing skill was compared against the named source prompt and a targeted improvement folded in. The list is retained for reference.

Nine of the eleven Phase A passes were never executed (the executed Phase A was scoped to `nda-review` and `demand-letter`). They remain available as comparison-and-improvement passes on existing skills, each using the named source prompt:

- `litigation/litigation-chronology` <- `chronology`
- `litigation/matter-intake` <- `matter-intake`
- `litigation/subpoena-triage` <- `subpoena`
- `privacy/dpa-review` <- `dpa-review`
- `privacy/dsar-workflow` <- `dsar-response`
- `employment/termination-risk` <- `termination-review`
- `employment/employee-policy-review` <- `handbook-updates`, `policy-drafting`
- `contracts/redline-summary` <- `amendment-history`
- `contracts/contract-risk-review` <- `saas-review`, `vendor-agreement-review`, `ip-clause-review`

### D3 — Other unresolved items

- `vendor-agreement-review`, `saas-review`, and `clearance` — the plan flagged these as conditional ("add only if a review shows existing skills are insufficient"); never resolved. Most likely folded into the `contract-risk-review` and `trademark-clearance-triage` passes in D2 rather than added as separate skills.
- The source's `litigation/demand-letter.md` is an *inbound* demand-triage workflow; AgentCounsel has no general inbound-demand-triage skill (`cease-and-desist-response` covers received IP demands only). A possible future skill.

## Risks and content-quality concerns

1. **Content not yet read in full.** This plan rests on file names and structural summaries. Every source file must be read and assessed before migration; dispositions may shift after a full read.
2. **Architecture mismatch.** Source workflows use their own structure (triage colours, practice profiles, escalation gates, `[VERIFY]` tags). Each migration is a rewrite into AgentCounsel's fixed `SKILL.md` format, not a copy.
3. **Jurisdiction-specific passages.** Some source workflows contain jurisdiction-specific material (for example, `deposition-prep` references England & Wales practice rules). AgentCounsel skills must stay jurisdiction-agnostic or clearly scope and flag such content.
4. **Drafting-heavy workflows.** `brief-section-drafter`, `demand-draft`, and corporate drafting prompts produce draft documents. These carry more risk and need especially strong "draft for attorney review" framing.
5. **License and attribution.** Migration is Apache-2.0-compatible but requires preserving the attribution chain. Add a `NOTICE` file before migrating content.
6. **Scope creep.** The source has roughly fifty prompts plus a corporate area. Migrating everything would nearly double the library and add a practice area. Phase B must stay limited to high-value skills; the corporate area stays deferred.
7. **Format and safety conformance.** Each migrated skill must pass `scripts/validate_repo.py` and follow the `core/` rules — including the no-invented-authority and confidentiality requirements — regardless of how the source framed the same workflow.

## Recommended next steps

1. Phases A (partial), B, and C are complete. Remaining work is collected in **Phase D**.
2. Build the clear D1 gaps — `internal-investigation` and `infringement-triage` — as new skills, each as its own reviewed pull request following `CONTRIBUTING.md`.
3. Decide the D1 judgment calls: `leave-tracker` (build as a review skill, or treat as a tracking tool and exclude) and `ip/takedown` (leave to the existing `dmca-takedown`, or use it to refine that skill).
4. Optionally run the D2 improvement passes on existing skills.
5. Re-run this completeness check periodically — the source repository continues to evolve.
