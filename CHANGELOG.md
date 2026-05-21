# Changelog

All notable changes to AgentCounsel are recorded in this file. The format follows the Keep a Changelog convention. AgentCounsel is pre-1.0; the library's content and structure may still change between releases.

## [Unreleased]

### Added

- `AGENTS.md` and `CLAUDE.md` at the repository root: an operating manual for AI agents working in the repo. `AGENTS.md` is the universal, tool-agnostic guide — how to decide whether a task is *using a skill* or *editing the library*, how to route a task to the narrowest skill, the non-negotiable safety rules, the library-edit workflow with a "done means validation passes" gate, and a table mapping known LLM failure modes (hallucination, jagged intelligence, anterograde amnesia, sycophancy, prompt injection, weak self-knowledge) to the discipline that contains each one. `CLAUDE.md` imports `AGENTS.md` and adds Claude Code specifics (routing with the Explore subagent, Plan mode for multi-skill edits, the validation suite) plus a pre-handoff self-check.
- `matter-workspaces/corporate-transaction-matter.md` and `matter-workspaces/employment-matter.md`: two new single-file matter scaffolds, bringing the matter-workspace set to six practice areas (litigation, contract review, privacy, regulatory, corporate transactions, and employment). The `matter-workspaces/README.md` template table is updated to match.
- A new Setup skill, `create-matter-workspace`, that recommends the right matter-workspace template, interviews the user for core matter information, and produces a populated workspace draft with maintenance instructions. `WORKFLOW_ROUTER.md` now has a "Before you start" section encouraging users to create a matter workspace before complex or multi-step work, and `SKILLS_INDEX.md` and `COMMANDS.md` list the new skill.
- `evals/`: a lightweight skill eval framework — `README.md`, a shared assertion catalogue (`evals/shared/assertions.md`), an eight-dimension `SKILL_QUALITY_RUBRIC.md`, and sample evals for eight skills (`contract-risk-review`, `nda-review`, `matter-intake`, `litigation-chronology`, `privilege-log-review`, `dpa-review`, `launch-review`, `compliance-gap-matrix`). The evals are quality checks, not legal validation, and the YAML format is shaped to adapt to promptfoo later.
- `scripts/check_evals.py`: a non-LLM static check that validates the eval files exist and conform to the schema, with no API keys required. It runs in CI alongside `scripts/validate_repo.py`.
- Plugin bundle sync tooling: `scripts/sync_plugin_skills.py` generates the Claude Code plugin bundle from canonical `/skills`, with a `--check` mode for CI. Documented in `PLUGIN_SYNC.md`.
- Skill templates are now included in the Claude Code plugin bundle, so it is self-contained.
- Plugin bundle drift detection in `scripts/validate_repo.py`.
- GitHub Actions CI (`.github/workflows/validate.yml`) runs the plugin sync check, repository validation, eval-framework validation, and freshness checks for the generated skill-improvement reports and the static site, on pull requests and pushes to `main`.
- Repository hygiene: issue templates (bug report, skill request, skill improvement), a pull request template, this changelog, and `.gitignore`.
- `docs/MIGRATION_PLAN_FROM_AGNOSTIC_SKILLS.md`: a plan for evaluating `agnostic-skills-for-legal` as source material (no canonical skills changed).
- `NOTICE` file recording Apache-2.0 attribution for content adapted from `agnostic-skills-for-legal` and its upstream projects.
- Six new skills adapted from `agnostic-skills-for-legal` (Phase B migration): `worker-classification` (employment); `deposition-prep`, `legal-hold`, and `privilege-log-review` (litigation); `pia-generation` (privacy); and `cease-and-desist-response` (intellectual property).
- Six further skills adapted from `agnostic-skills-for-legal` (Phase B migration, second batch): `hiring-review` and `wage-hour-qa` (employment); `claim-chart` and `brief-section-drafter` (litigation); and `fto-triage` and `invention-intake` (intellectual property).
- A new **Corporate** practice area (Phase C migration): six skills adapted from `agnostic-skills-for-legal` — `board-minutes`, `written-consent`, `closing-checklist`, `diligence-issue-extraction`, `material-contract-schedule`, and `entity-compliance`.
- Phase D1: three further skills adapted from `agnostic-skills-for-legal` — `internal-investigation` and `protected-leave-review` (employment) and `infringement-triage` (intellectual property).
- `CONTEXT.md`: a concise vocabulary and mental-model reference for AI agents and LLMs working in the repository.
- Gemini CLI extension support: a `gemini-extension.json` manifest and a `GEMINI.md` context file at the repository root, plus a new `adapters/gemini/` adapter with a `using-agentcounsel.md` operating guide and a `references/` folder of per-runtime tool maps (`gemini-tools.md`, `copilot-tools.md`, `codex-tools.md`).
- `practice-profiles/`: nine per-practice-area configuration profile templates (contracts, litigation, corporate, employment, privacy, product-legal, regulatory, ai-governance, ip) capturing jurisdictions, client/team context, escalation thresholds, preferred output style, source-of-truth documents, standard positions, attorney review requirements, and prohibited assumptions.
- A new **Setup** practice area: four cold-start interview skills — `contracts-cold-start-interview`, `litigation-cold-start-interview`, `privacy-cold-start-interview`, and `corporate-cold-start-interview` — that interview a practice group and produce a filled practice-profile draft for attorney review.
- A new **Legal Methodology** practice area: four cross-cutting skills — `red-team-verifier`, `statutory-interpretation`, `risk-assessment`, and `source-validation`.
- `COMMANDS.md`: a command router mapping slash-style command shorthands to every skill, with trigger phrases, required inputs, expected output, and related commands.
- `skills/contracts/references/`: five shared contract-review reference files — `red-flags.md`, `negotiability-ratings.md`, `market-benchmark-framework.md`, `document-type-checklists.md`, and `redline-output-guidance.md`.
- `matter-workspaces/`: four single-file matter scaffolds — litigation, contract review, privacy, and regulatory.
- `site/`: a static, browser-readable skill catalog generated from `skills/` by a zero-dependency Node script — a homepage, practice-area pages, per-skill pages (with the rendered sections, the full raw `SKILL.md`, and Copy Full Skill / Copy One-Off Prompt buttons), platform setup guides, and `llms.txt` / `llms-full.txt`. Build with `npm run build` from `site/`; documented in `site/README.md` and the root `README.md`.
- `scripts/build_platform_packs.py`: generates platform-specific install packs into `dist/` from the canonical `skills/` and `core/` — consolidated Markdown packs for ChatGPT Projects, per-practice-area ZIPs for Claude Projects and Gemini Notebooks, instruction files for repo agents (Codex, Claude Code, Cursor), and `index.json` / `manifest.json` / `SKILL_PACKS_INDEX.md`. The build self-validates skill structure, pack contents, index coverage, and safety language. Standard library only; documented in `README.md`.
- `core/business-stakeholder-communication.md`: a seventh core operating rule defining an optional business-stakeholder summary mode — a plain-language layer (Business Summary, Decision Needed, Recommended Ask, Fallback Position, Escalation Needed?) for briefing non-lawyer decision-makers, with attorney review still required.

### Changed

- Business-stakeholder summary mode: 25 commercial skills across contracts, product legal, privacy, regulatory, employment, and corporate now offer an optional **Business Stakeholder Summary** in their Output Format (Business Summary, Decision Needed, Recommended Ask, Fallback Position, Escalation Needed?). `SKILLS_INDEX.md` and `WORKFLOW_ROUTER.md` document the mode.

- `red-team-verifier`: broadened into AgentCounsel's universal quality-control workflow for any legal output. Added explicit trigger phrases (checking a memo, contract review, demand letter, risk matrix, research summary, or draft filing; "is this good enough?"; weakness, missing-issue, and hallucination checks), a dedicated legal-reasoning audit (rule statement, element coverage, application, counterarguments, exceptions, ambiguity, weak analogies), a dedicated professional-responsibility audit (unauthorized-advice framing, attorney-review framing, confidentiality and privilege, recipient mismatch), and a missing-fact audit. Reconciled the output format to an Executive Risk Summary, Major Problems, Unsupported Claims Table, Missing Facts, Jurisdiction and Deadline Flags, Suggested Revisions, and Attorney Verification Checklist. `WORKFLOW_ROUTER.md` and `SKILLS_INDEX.md` now recommend it as a final pass after any high-stakes legal output.
- `nda-review`: added an overall GREEN / YELLOW / RED triage rating, a scope check for obligations beyond confidentiality, a routing gate for M&A / employment / investment NDAs, and benchmarking against a client playbook — adapted from `agnostic-skills-for-legal` (Phase A migration).
- `demand-letter`: added a structured intake stage and a pre-draft risk gate (privilege filter, admission risk, accord and satisfaction, settlement-communication posture, privilege-waiver scan, tone, factual accuracy), and clarified that the sent letter carries no work-product header — adapted from `agnostic-skills-for-legal` (Phase A migration).
- `docs/MIGRATION_PLAN_FROM_AGNOSTIC_SKILLS.md`: refreshed to record Phases A–C as executed and to add a Phase D for newly identified gaps (five new source prompts and the unrun Phase A improvement passes).
- Phase D2: nine existing skills improved with content adapted from `agnostic-skills-for-legal` — `litigation-chronology`, `matter-intake`, and `subpoena-triage` (litigation); `dpa-review` and `dsar-workflow` (privacy); `termination-risk` and `employee-policy-review` (employment); and `redline-summary` and `contract-risk-review` (contracts).
- `nda-review` and `contract-risk-review`: added a Red Flags Quick Scan, a Negotiability Rating, Market Benchmark Notes, Preferred / Fallback Position and Suggested Redline Direction for each redline point, and an Internal Consistency Check — all drawing on the new `skills/contracts/references/` material.
- `scripts/validate_repo.py`: now recognizes shared `references/` folders under a practice area as non-skill directories, validates skill paths referenced in `COMMANDS.md`, and checks that the library's expected top-level directories exist. It also skips generated build output (`dist/`, `node_modules/`) when scanning. README practice-area and skills badges updated to 12 practice areas and 59 skills.
- `core/source-and-citation-discipline.md` substantially strengthened to prevent legal hallucination: explicit prohibitions on inventing any legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules; a five-way labeling taxonomy (provided source, user-provided fact, assumption, legal inference, item requiring attorney verification); discipline for working only from documents actually provided; rules for legal research tasks (ask for jurisdiction and date, require current-law verification, separate the research roadmap from any conclusion); and new citation placeholders `[Attorney to insert authority]`, `[Verify current law]`, and `[Confirm local rule]` (also listed in `core/output-format-rules.md`).
- 42 skills — every skill in the litigation, regulatory, privacy, employment, corporate, contracts, and legal-methodology practice areas, plus the skills that lacked equivalent language — now reference `core/source-and-citation-discipline.md` in their Legal Safety Rules.
- `scripts/validate_repo.py`: new check that every `SKILL.md` references the source/citation discipline core rule or carries equivalent language against inventing legal authority or citations.

### Fixed

- README badges corrected: the practice-area and skills badges linked to a `prompts/` directory that does not exist in this repository and used the source project's terminology and a stale count; they now reflect AgentCounsel's structure (10 practice areas, 50 skills) and link to `SKILLS_INDEX.md`. The "works with" badge anchor was repaired.
- Refreshed the stale Litigation and Privacy rows of the README practice-area table.
- `scripts/validate_repo.py` now also checks the link target of Markdown image and badge links (`[![alt](image)](target)`) — a case the link checker previously skipped.

## [0.1.0] - 2026-05-20

### Added

- Initial AgentCounsel scaffold: an open, Markdown-native legal skills library.
- 29 skills across nine practice areas — legal research, litigation, contracts, employment, privacy, product legal, regulatory, AI governance, and intellectual property — each a standalone `SKILL.md` with a consistent structure.
- Six core operating rules in `core/` and seven copyable templates.
- Four adapters: generic Markdown, Codex / repo agents, a Claude Code plugin bundle, and Claude / Cowork local-folder use.
- Project documentation: `README.md`, `SKILLS_INDEX.md`, `WORKFLOW_ROUTER.md`, `SECURITY.md`, `CONTRIBUTING.md`, and an Apache-2.0 `LICENSE`.
- Repository validation: `scripts/validate_repo.py` and `VALIDATION.md`.
