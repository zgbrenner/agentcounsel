# AgentCounsel

**An open, Markdown-native library of legal skills for AI agents — and the legal professionals who supervise them.**

[![License: Apache 2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Practice areas](https://img.shields.io/badge/practice%20areas-20-purple.svg)](SKILLS_INDEX.md)
[![Skills](https://img.shields.io/badge/skills-179-success.svg)](SKILLS_INDEX.md)
[![Works with](https://img.shields.io/badge/works%20with-ChatGPT%20%C2%B7%20Claude%20%C2%B7%20Gemini%20%C2%B7%20Codex%20%C2%B7%20Cursor-lightgrey.svg)](#ways-to-use-agentcounsel)
[![CI](https://github.com/zgbrenner/agentcounsel/actions/workflows/validate.yml/badge.svg)](https://github.com/zgbrenner/agentcounsel/actions/workflows/validate.yml)

AgentCounsel is a collection of standalone **legal skills**. Each skill is a structured workflow that helps an AI agent — or a lawyer — produce **draft legal work product for attorney review**. The skills supply discipline and structure: how to scope a task, what inputs to gather, how to organize the output, and what a supervising attorney must verify before anything is relied upon.

> **AgentCounsel does not provide legal advice.** It produces draft work product intended for review and adoption by a qualified, licensed legal professional. Using it does not create an attorney–client relationship.

New here? Start with **[QUICKSTART.md](QUICKSTART.md)** — it walks through your first skill run in about five minutes.

## Who AgentCounsel is for

- **Practicing lawyers and in-house legal teams** who want AI assistance that is consistent, reviewable, and built around attorney oversight instead of around a vendor's product.
- **Legal operations and knowledge-management teams** standardizing how their organization uses AI for routine legal work — intake, triage, first-pass review, and drafting.
- **Law students and new lawyers** who want to see how experienced practitioners structure a contract review, a chronology, a research memo, or a risk assessment.
- **AI builders and engineers** assembling legal agents or assistants who need well-scoped, safety-first workflow definitions they can drop into any model or framework.

Whoever you are, the assumption is the same: a licensed attorney reviews the output before it is used.

## What it is — and is not

**It is:**

- A library of legal **workflows** and **output structures**.
- A way to make AI-assisted legal drafting more consistent, reviewable, and safe.
- Useful piecemeal (one Markdown file) or as a whole.
- Plain Markdown — no build system, no runtime, no account, no lock-in.

**It is not:**

- Legal advice, or a substitute for a licensed attorney.
- A source of jurisdiction-specific legal rules. Skills give you process and structure, not the law of any jurisdiction.
- A finished-document generator. Every output is a **draft** that an attorney must review.
- Built around any single AI product. It is a portable library with thin adapters for many environments.

## Quick start

1. Read the files in [`core/`](core/) — the operating rules every skill inherits.
2. Open [`WORKFLOW_ROUTER.md`](WORKFLOW_ROUTER.md) and find the workflow that matches your task.
3. Open that skill's `SKILL.md` and gather its **Required Inputs**.
4. Follow the **Workflow**, and produce the **Output Format**.
5. Complete the **Attorney Verification Checklist** before relying on anything.

A worked, step-by-step version of this — with copy-paste prompts for each platform — is in **[QUICKSTART.md](QUICKSTART.md)**. Sample outputs are in **[`examples/`](examples/)**.

## Practice areas

AgentCounsel has **179 skills**: 153 across **20 practice areas**, plus 26 cross-cutting skills in three supporting groups (Setup, Legal Operations, Legal Methodology).

| Practice area | Skills | Covers |
|---|--:|---|
| Legal Research | 1 | Turning research questions into structured, verifiable memos. |
| Litigation | 9 | Matter intake, chronologies, demand letters, subpoena triage, depositions, legal holds, privilege logs, claim charts, brief drafting. |
| Contracts | 5 | NDAs, commercial contracts, redlines, statements of work, vendor agreement status. |
| Corporate | 6 | Board minutes, written consents, closing checklists, diligence review, material-contract schedules, entity compliance. |
| Employment | 8 | Terminations, worker classification, hiring, internal investigations, protected leave, severance, workplace policies. |
| Privacy | 4 | Data processing agreements, impact assessments, data subject requests, policy gaps. |
| Product Legal | 4 | Launch review, marketing claims, terms of service, AI features. |
| Regulatory | 4 | Enforcement risk, rule-change summaries, compliance gaps, compliance-program tracking. |
| AI Governance | 4 | AI use-case intake, vendor terms, model risk, AI policies. |
| Intellectual Property | 7 | Trademark triage, infringement triage, cease-and-desist response, patent FTO triage, invention intake, DMCA, open-source licensing. |
| Financial Crime / AML | 2 | KYC onboarding review, and sanctions / PEP / adverse-media screening review. |
| Real Estate | 9 | Commercial lease abstraction and review, amendment reconciliation, purchase and sale agreement review, title and survey objection tracking, diligence and closing checklists, estoppel and SNDA review, zoning issue-spotting. |
| Mergers & Acquisitions | 10 | LOI and term-sheet review, acquisition diligence and data-room review, purchase-agreement and disclosure-schedule review, indemnity and escrow analysis, third-party consents, and closing, post-closing, and integration tracking. |
| Antitrust / Competition | 10 | Antitrust risk intake, competitor-collaboration and information-sharing review, pricing-algorithm and distribution-restraint review, merger issue-spotting, gun-jumping checklists, and compliance-policy review. |
| Securities / Capital Markets | 12 | Private and public offerings, exemption issue-spotting, offering-document and risk-factor review, SEC filing consistency, Form D and blue-sky tracking, investor-rights and insider-trading review, beneficial-ownership triage, and capital-markets closings. |
| Tax | 10 | Tax issue intake, entity tax-classification facts, transaction tax diligence, sales/use tax nexus triage, employment-tax worker-classification intake, contract tax-provision and covenant/indemnity review, tax document organization, international tax issue-spotting, and crypto/digital-asset tax intake. |
| Bankruptcy / Restructuring | 12 | Bankruptcy and creditor-claim intake, proof-of-claim checklists, automatic-stay and preference issue-spotting, executory-contract assumption/rejection review, distressed-M&A diligence and asset-sale checklists, restructuring term-sheet review, plan and disclosure-statement issue-spotting, DIP financing issue-spotting, and deadline-tracker intake. |
| Insurance | 12 | Insurance policy summaries, coverage issue-spotting, claim chronologies, reservation of rights and tender review, coverage-position outlines, bad-faith risk triage, certificate of insurance and contract insurance-requirements review, subrogation/recovery tracking, and renewal/placement diligence checklists. |
| Trusts & Estates | 12 | Estate-planning intake, estate-document summaries, probate document checklists, trust administration and post-death task tracking, fiduciary-duty issue-spotting, beneficiary-designation review, asset and liability inventories, capacity and undue-influence facts organization, estate-litigation chronologies, trust-funding checklists, and estate-tax issue intake. |
| Family Law | 12 | Family-law matter and divorce intake, custody and parenting facts chronologies and schedule organization, custody-order review, child-support and spousal-support facts intake, asset/debt schedules, settlement-agreement issue-spotting, discovery tracking, hearing preparation, and domestic-violence safety referral. |

Three **cross-cutting skill groups** support work in every practice area:

- **Setup** (19 skills) — cold-start interviews that configure AgentCounsel for a practice group, plus a matter-workspace builder.
- **Legal Methodology** (4 skills) — red-team verification, statutory interpretation, risk assessment, and source validation.
- **Legal Operations** (3 skills) — templated legal responses, meeting briefings, and signature-routing checks.

The four-tier taxonomy that classifies these areas and groups — and the model for expanding it — is recorded in [`docs/PRACTICE_AREAS.md`](docs/PRACTICE_AREAS.md).

See [`SKILLS_INDEX.md`](SKILLS_INDEX.md) for the full catalog and [`WORKFLOW_ROUTER.md`](WORKFLOW_ROUTER.md) to route from a task to a skill.

## How it is organized

```
core/               Operating rules every skill inherits (read these first).
skills/             The canonical skill library, grouped by practice area.
examples/           Illustrative sample outputs, with fictional facts.
practice-profiles/  Per-practice-area configuration profiles for a legal team.
matter-workspaces/  Single-file scaffolds for organizing one specific matter.
matter-packs/       Workflow bundles — recommended skill sequences per matter type.
overlays/           Industry and sector overlays that tune skills for a context.
adapters/           Thin integration files for specific environments.
metadata/           Generated machine-readable skill index (index.json).
docs/               The metadata standard, the safety model, the FAQ, and the practice-area registry.
scripts/            Standard-library Python helpers (validation, index, packs).
SKILLS_INDEX.md     Full catalog of every skill.
WORKFLOW_ROUTER.md  "I need to do X" -> which skill to use.
COMMANDS.md         Slash-style command shorthands mapped to skills.
```

The `skills/` directory is the **canonical source of truth.** Everything else points back to it.

### Anatomy of a skill

Each skill lives in its own folder with a `SKILL.md` file and optional `templates/`:

```
skills/contracts/nda-review/
  SKILL.md                     The workflow.
  templates/nda-risk-table.md  A copyable, attorney-review-ready template.
```

Every `SKILL.md` follows the same structure — Purpose, Use When, Required Inputs, Do Not Use When, Legal Safety Rules, Workflow, Output Format, and an Attorney Verification Checklist — and carries standardized, agent-readable YAML frontmatter so tools and agents can discover and route skills. See [`docs/SKILL_METADATA_STANDARD.md`](docs/SKILL_METADATA_STANDARD.md).

## Ways to use AgentCounsel

### Recommended: install a pre-built practice-area pack

A platform pack is one file that bundles the global safety rules, the practice profile, the slash commands, and every skill in a practice area. Upload it to your AI tool's project or workspace and you can start work immediately — no copying files one at a time.

Pre-built packs are hosted on the deployed Pages site and rebuilt on every push to `main`:

- **[Browse the packs page](https://zgbrenner.github.io/agentcounsel/packs/)** — direct downloads per practice area for ChatGPT (.md), Claude (.zip), and Gemini (.zip), plus AGENTS.md / CLAUDE.md for repo agents.
- The packs page lists every practice area with its skill count and a "How to use" block per platform.

### For finer-grained control, you can also...

AgentCounsel is plain Markdown, so it works anywhere an agent or person can read a file. The library-as-files paths below give you more control than a consolidated pack.

| Surface | How to use AgentCounsel | Where to look |
|---|---|---|
| **Generic Markdown** | Open any `SKILL.md`, paste it into your assistant as context, and follow the workflow. Works with any model. | [`adapters/generic-md/`](adapters/generic-md/) |
| **ChatGPT** | Create a ChatGPT Project and add individual skill files. (For the consolidated practice-area pack, use the packs page above.) | [`adapters/generic-md/`](adapters/generic-md/) |
| **Claude** | Use the Claude Code plugin-style bundle, or keep the repo in a folder Claude can read as a local playbook. | [`adapters/claude-code-plugin/`](adapters/claude-code-plugin/), [`adapters/claude-cowork/`](adapters/claude-cowork/) |
| **Gemini** | Install the repository as a Gemini CLI extension — `gemini-extension.json` and `GEMINI.md` load the operating model automatically. | [`adapters/gemini/`](adapters/gemini/) |
| **Codex / repo agents** | Point a repo-based coding or legal agent at the library through `AGENTS.md` so it selects the narrowest relevant skill. | [`adapters/codex/`](adapters/codex/), [`AGENTS.md`](AGENTS.md) |
| **Cursor** | Add the library to a project and reference it from a `.cursorrules` file or `AGENTS.md`. (The packs page above also serves a ready-made `.cursorrules`.) | [`adapters/codex/`](adapters/codex/) |
| **Your own agent** | Vendor the `skills/` and `core/` directories into your project and reference them from your agent's instructions. | [`skills/`](skills/), [`core/`](core/) |

Adapters are intentionally **thin**: they tell an environment how to find and use the canonical library; they do not duplicate it. The one exception is the Claude Code plugin bundle, which carries generated copies of a curated set of skills — regenerate it with `python scripts/sync_plugin_skills.py` (see [`PLUGIN_SYNC.md`](PLUGIN_SYNC.md)).

### Installing or copying skills

- **A practice area (recommended):** download a pre-built pack from the [packs page](https://zgbrenner.github.io/agentcounsel/packs/) — one file per practice area for ChatGPT, Claude, and Gemini. Or run `python scripts/build_platform_packs.py` locally to produce the same packs in `dist/`.
- **One skill:** copy a single `SKILL.md` (and its `templates/`, if any) into your assistant. Nothing else is required.
- **The whole library:** clone the repository, or vendor `skills/` and `core/` into your own project.

There is no installer, no package to publish, and no runtime dependency. A skill is just a file.

## Safety model

Every skill inherits the operating rules in [`core/`](core/):

- **Draft legal work product only.** Attorney review is always required before output is relied upon.
- **Never invent legal authority, citations, quotations, facts, or deadlines.**
- **Separate** facts, assumptions, law, analysis, strategy, and verification items.
- **Identify** jurisdiction, governing law, posture, and the relevant date — or flag them as unknown.
- **Preserve** confidentiality and privilege.
- **Flag uncertainty** with visible placeholders instead of guessing.

The full safety model — the threat model, what AgentCounsel deliberately does *not* do, and how to use it safely with confidential material — is in **[docs/SAFETY_MODEL.md](docs/SAFETY_MODEL.md)**. Security reporting and guidance are in [`SECURITY.md`](SECURITY.md).

## Configuring AgentCounsel for a team

Two optional layers let a legal team adapt the library without changing any skill:

- **[`practice-profiles/`](practice-profiles/)** — one profile per practice area capturing the team's jurisdictions, escalation thresholds, standard positions, review requirements, and prohibited assumptions. The **Setup** cold-start interview skills fill a profile in.
- **[`matter-workspaces/`](matter-workspaces/)** — single-file scaffolds for organizing one specific matter: parties, documents, deadlines (always flagged for attorney verification), open items, and an index of the draft work product produced by skills.

Both are plain Markdown and add no backend, runtime, or vendor dependency.

## Examples

The [`examples/`](examples/) directory contains illustrative sample outputs — a contract review, a litigation chronology, a DPA review, a product launch review, and a red-team verification. **Every fact in them is fictional.** They show the shape and quality of a skill's deliverable; they are not legal advice and not templates for a real matter.

## Validation and continuous integration

The repository ships a lightweight validation script — Python standard library only, no dependencies — that checks every skill's structure, frontmatter, links, and safety framing:

```
python scripts/validate_repo.py
```

GitHub Actions runs the same checks on every pull request and on pushes to `main` (see [`.github/workflows/validate.yml`](.github/workflows/validate.yml)):

```
python scripts/sync_plugin_skills.py --check   # plugin bundle is in sync
python scripts/validate_repo.py                # full repository validation
```

Other standard-library helpers in `scripts/` build the machine-readable skill index (`build_skill_index.py`), the per-platform install packs (`build_platform_packs.py`), and the browsable static catalog under [`site/`](site/). See [`VALIDATION.md`](VALIDATION.md) for the full list of checks.

## Contributing

New skills and improvements are welcome. AgentCounsel is Markdown-first and safety-first — see [`CONTRIBUTING.md`](CONTRIBUTING.md) for the rules, [`docs/SKILL_METADATA_STANDARD.md`](docs/SKILL_METADATA_STANDARD.md) for the frontmatter standard, and [`SECURITY.md`](SECURITY.md) for security guidance. Questions are answered in [`docs/FAQ.md`](docs/FAQ.md).

## License

Apache License 2.0 — see [`LICENSE`](LICENSE). Attribution for content adapted from other open-source projects is recorded in [`NOTICE`](NOTICE). AgentCounsel is an independent open-source project and is not affiliated with, endorsed by, or sponsored by Anthropic, OpenAI, or Google.

## Disclaimer

AgentCounsel is a workflow library — not a law firm and not a lawyer. Using it does not create an attorney–client relationship, and it does not provide legal advice. All output is draft work product that must be reviewed and adopted by a qualified, licensed legal professional before it is relied upon. You are responsible for the use of these materials and for compliance with the rules of professional conduct that apply to you.
