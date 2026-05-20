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

## [0.1.0] - 2026-05-20

### Added

- Initial AgentCounsel scaffold: an open, Markdown-native legal skills library.
- 29 skills across nine practice areas — legal research, litigation, contracts, employment, privacy, product legal, regulatory, AI governance, and intellectual property — each a standalone `SKILL.md` with a consistent structure.
- Six core operating rules in `core/` and seven copyable templates.
- Four adapters: generic Markdown, Codex / repo agents, a Claude Code plugin bundle, and Claude / Cowork local-folder use.
- Project documentation: `README.md`, `SKILLS_INDEX.md`, `WORKFLOW_ROUTER.md`, `SECURITY.md`, `CONTRIBUTING.md`, and an Apache-2.0 `LICENSE`.
- Repository validation: `scripts/validate_repo.py` and `VALIDATION.md`.
