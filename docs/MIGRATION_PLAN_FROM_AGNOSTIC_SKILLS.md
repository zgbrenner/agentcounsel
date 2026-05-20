# Migration Plan — agnostic-skills-for-legal into AgentCounsel

**Status: plan only.** No canonical skills have been changed. This document proposes what to migrate and in what order. Each migration listed here is a separate, reviewed change to be carried out later.

## Purpose

`foolish-bandit/agnostic-skills-for-legal` is an existing open-source legal-AI library. This plan compares it against AgentCounsel's canonical `skills/` directory and recommends, in priority order, what content to (A) fold into existing skills, (B) add as new skills, or (C) defer or reject.

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

### Practice areas to keep out of scope for now

- **Corporate / M&A / transactional.** The entire `prompts/corporate` set is a distinct practice area AgentCounsel does not cover. Adding it would significantly expand scope. Defer it as a possible future practice area; do not migrate it piecemeal.

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

## Risks and content-quality concerns

1. **Content not yet read in full.** This plan rests on file names and structural summaries. Every source file must be read and assessed before migration; dispositions may shift after a full read.
2. **Architecture mismatch.** Source workflows use their own structure (triage colours, practice profiles, escalation gates, `[VERIFY]` tags). Each migration is a rewrite into AgentCounsel's fixed `SKILL.md` format, not a copy.
3. **Jurisdiction-specific passages.** Some source workflows contain jurisdiction-specific material (for example, `deposition-prep` references England & Wales practice rules). AgentCounsel skills must stay jurisdiction-agnostic or clearly scope and flag such content.
4. **Drafting-heavy workflows.** `brief-section-drafter`, `demand-draft`, and corporate drafting prompts produce draft documents. These carry more risk and need especially strong "draft for attorney review" framing.
5. **License and attribution.** Migration is Apache-2.0-compatible but requires preserving the attribution chain. Add a `NOTICE` file before migrating content.
6. **Scope creep.** The source has roughly fifty prompts plus a corporate area. Migrating everything would nearly double the library and add a practice area. Phase B must stay limited to high-value skills; the corporate area stays deferred.
7. **Format and safety conformance.** Each migrated skill must pass `scripts/validate_repo.py` and follow the `core/` rules — including the no-invented-authority and confidentiality requirements — regardless of how the source framed the same workflow.

## Recommended next steps

1. Decide whether to proceed with Phase A, Phase B, or both, and in what order. A reasonable order is: add attribution (`NOTICE`), then Phase A high-priority items, then Phase B high-priority items.
2. For each chosen item, read the full source file, then open a skill-improvement or skill-request issue and migrate it as its own pull request following `CONTRIBUTING.md`.
3. Keep the corporate / M&A area as a separate, later decision.
