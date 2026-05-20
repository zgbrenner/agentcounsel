# Changelog

All notable changes to AgentCounsel are recorded in this file. The format follows the Keep a Changelog convention. AgentCounsel is pre-1.0; the library's content and structure may still change between releases.

## [Unreleased]

### Added

- Plugin bundle sync tooling: `scripts/sync_plugin_skills.py` generates the Claude Code plugin bundle from canonical `/skills`, with a `--check` mode for CI. Documented in `PLUGIN_SYNC.md`.
- Skill templates are now included in the Claude Code plugin bundle, so it is self-contained.
- Plugin bundle drift detection in `scripts/validate_repo.py`.
- GitHub Actions CI (`.github/workflows/validate.yml`) runs the plugin sync check and repository validation on pull requests and pushes to `main`.
- Repository hygiene: issue templates (bug report, skill request, skill improvement), a pull request template, this changelog, and `.gitignore`.
- `docs/MIGRATION_PLAN_FROM_AGNOSTIC_SKILLS.md`: a plan for evaluating `agnostic-skills-for-legal` as source material (no canonical skills changed).
- `NOTICE` file recording Apache-2.0 attribution for content adapted from `agnostic-skills-for-legal` and its upstream projects.
- Six new skills adapted from `agnostic-skills-for-legal` (Phase B migration): `worker-classification` (employment); `deposition-prep`, `legal-hold`, and `privilege-log-review` (litigation); `pia-generation` (privacy); and `cease-and-desist-response` (intellectual property).
- Six further skills adapted from `agnostic-skills-for-legal` (Phase B migration, second batch): `hiring-review` and `wage-hour-qa` (employment); `claim-chart` and `brief-section-drafter` (litigation); and `fto-triage` and `invention-intake` (intellectual property).
- A new **Corporate** practice area (Phase C migration): six skills adapted from `agnostic-skills-for-legal` — `board-minutes`, `written-consent`, `closing-checklist`, `diligence-issue-extraction`, `material-contract-schedule`, and `entity-compliance`.

### Changed

- `nda-review`: added an overall GREEN / YELLOW / RED triage rating, a scope check for obligations beyond confidentiality, a routing gate for M&A / employment / investment NDAs, and benchmarking against a client playbook — adapted from `agnostic-skills-for-legal` (Phase A migration).
- `demand-letter`: added a structured intake stage and a pre-draft risk gate (privilege filter, admission risk, accord and satisfaction, settlement-communication posture, privilege-waiver scan, tone, factual accuracy), and clarified that the sent letter carries no work-product header — adapted from `agnostic-skills-for-legal` (Phase A migration).

## [0.1.0] - 2026-05-20

### Added

- Initial AgentCounsel scaffold: an open, Markdown-native legal skills library.
- 29 skills across nine practice areas — legal research, litigation, contracts, employment, privacy, product legal, regulatory, AI governance, and intellectual property — each a standalone `SKILL.md` with a consistent structure.
- Six core operating rules in `core/` and seven copyable templates.
- Four adapters: generic Markdown, Codex / repo agents, a Claude Code plugin bundle, and Claude / Cowork local-folder use.
- Project documentation: `README.md`, `SKILLS_INDEX.md`, `WORKFLOW_ROUTER.md`, `SECURITY.md`, `CONTRIBUTING.md`, and an Apache-2.0 `LICENSE`.
- Repository validation: `scripts/validate_repo.py` and `VALIDATION.md`.
