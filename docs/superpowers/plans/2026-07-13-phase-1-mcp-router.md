# Phase 1 MCP Router Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace AgentCounsel's duplicate MCP parsing and keyword router with a canonical metadata-backed service, add executable coverage, and generate context and skill-readiness reports.

**Architecture:** A standard-library `CatalogService` owns metadata loading, search, retrieval, and routing. `mcp_server.py` remains a thin FastMCP adapter. Two standard-library generators produce deterministic context metrics and repository-readiness signals from canonical files.

**Tech Stack:** Python 3.12, standard-library `unittest`, FastMCP transport adapter, generated JSON/Markdown reports, GitHub Actions.

## Global Constraints

- Do not modify legal skill substance under `skills/`.
- Keep `skills/` and generated metadata as the canonical source of truth.
- Do not add embeddings, model calls, network dependencies, or legal-deadline computation.
- Keep all maintainer generators standard-library only.
- Preserve existing MCP tool names and add compact retrieval without breaking older identifiers.
- Reports must not claim legal correctness or attorney approval.

---

### Task 1: Define failing MCP service tests

**Files:**
- Create: `tests/test_mcp_service.py`

**Interfaces:**
- Consumes: temporary fixture repository containing `metadata/index.json`, `metadata/router.json`, and sample `SKILL.md` files.
- Produces: executable contract for `CatalogService`, `CatalogLoadError`, `estimate_confidence`, and structured route records.

- [ ] Write tests for canonical metadata loading and list-valued fields.
- [ ] Write tests for stable IDs, aliases, compact cards, and full retrieval.
- [ ] Write tests proving description/use-when metadata outranks repeated body boilerplate.
- [ ] Write tests for exact ID/title ranking and practice-area filtering.
- [ ] Write tests for route fields, workspace triggers, alternatives, gates, quality checks, and escalation.
- [ ] Write tests for explicit no-match behavior and invalid arguments.
- [ ] Run `python -m unittest tests.test_mcp_service -v` and confirm it fails because `agentcounsel_mcp` does not exist.
- [ ] Commit the failing tests.

### Task 2: Implement the pure metadata-backed service

**Files:**
- Create: `agentcounsel_mcp.py`

**Interfaces:**
- Produces:
  - `CatalogLoadError(Exception)`
  - `CatalogService.from_root(root: Path) -> CatalogService`
  - `CatalogService.list_practice_areas() -> list[dict]`
  - `CatalogService.search_skills(query: str, practice_area: str | None = None, limit: int = 10) -> list[dict]`
  - `CatalogService.get_skill_card(skill_id: str) -> dict`
  - `CatalogService.get_skill(skill_id: str) -> dict`
  - `CatalogService.route_task(task: str, limit: int = 5) -> dict`

- [ ] Load and validate `metadata/index.json` and `metadata/router.json` once in `from_root`.
- [ ] Build stable-ID and backward-compatible alias indexes.
- [ ] Implement deterministic tokenization and weighted metadata-only ranking.
- [ ] Implement compact cards with no full Markdown content.
- [ ] Implement structured routing and confidence calculation.
- [ ] Return `status: no_match` when no candidate has a positive score.
- [ ] Run `python -m unittest tests.test_mcp_service -v` and confirm all tests pass.
- [ ] Run `python -m unittest discover -s tests` and confirm the full suite passes.
- [ ] Commit the service implementation.

### Task 3: Convert the FastMCP server into a thin adapter

**Files:**
- Modify: `mcp_server.py`
- Modify: `docs/MCP_SERVER.md`

**Interfaces:**
- Consumes: one process-wide `CatalogService` instance.
- Produces MCP tools: `list_practice_areas`, `search_skills`, `route_legal_task`, `get_skill_card`, `get_skill`, and `get_core_rules`.

- [ ] Remove the duplicate frontmatter parser and full-text counter.
- [ ] Delegate every catalog/routing tool to `CatalogService`.
- [ ] Add `get_skill_card` for compact retrieval.
- [ ] Keep `get_skill` aliases backward compatible while returning stable IDs.
- [ ] Update MCP documentation to describe structured routing and remove hardcoded skill totals.
- [ ] Run the full unit suite.
- [ ] Commit the adapter and documentation changes.

### Task 4: Add deterministic context metrics

**Files:**
- Create: `scripts/generate_context_metrics.py`
- Create: `tests/test_context_metrics.py`
- Generate: `metadata/context_metrics.json`
- Generate: `reports/context-metrics.md`

**Interfaces:**
- Produces `collect_metrics(root: Path) -> dict`, `render_markdown(data: dict) -> str`, and CLI `--check` behavior.

- [ ] Write failing tests for token approximation, section counts, dependency counts, pack aggregation, and deterministic ordering.
- [ ] Confirm the tests fail before implementation.
- [ ] Implement the generator using generated metadata and canonical files.
- [ ] Generate JSON and Markdown artifacts.
- [ ] Run focused and full tests.
- [ ] Commit metrics tooling and generated artifacts.

### Task 5: Add the skill-readiness scorecard

**Files:**
- Create: `scripts/generate_skill_health_report.py`
- Create: `tests/test_skill_health_report.py`
- Generate: `metadata/skill_health.json`
- Generate: `reports/skill-health.md`

**Interfaces:**
- Produces `collect_health(root: Path) -> dict`, `render_markdown(data: dict) -> str`, and CLI `--check` behavior.

- [ ] Write failing tests for eval depth, scored status, examples, templates, routing metadata, context pressure, and the legal-correctness disclaimer.
- [ ] Confirm the tests fail before implementation.
- [ ] Implement deterministic readiness signals and priority bands.
- [ ] Generate JSON and Markdown artifacts.
- [ ] Run focused and full tests.
- [ ] Commit scorecard tooling and generated artifacts.

### Task 6: Integrate validation and remove stale touched-surface text

**Files:**
- Modify: `.github/workflows/validate.yml`
- Modify: `scripts/check_all.py`
- Modify: `scripts/_shared.py`
- Modify: `CHANGELOG.md`

**Interfaces:**
- CI verifies both generated report families are current and runs MCP service tests through standard test discovery.

- [ ] Add `--check` commands for context metrics and skill-health reports to CI and `check_all.py`.
- [ ] Correct the stale `_shared.py` comment that describes the required eval list as eight skills.
- [ ] Add an Unreleased changelog entry covering the MCP router, tests, and reports.
- [ ] Run `python scripts/check_all.py`.
- [ ] Run `python -m unittest discover -s tests`.
- [ ] Review generated diffs for hardcoded counts, legal-quality overclaims, and accidental skill-body changes.
- [ ] Commit integration changes.

### Task 7: Final verification and pull request

**Files:**
- Review all changed files.

- [ ] Confirm no files under `skills/` changed.
- [ ] Confirm every new generator passes `--check`.
- [ ] Confirm the full test suite and `scripts/check_all.py` pass in GitHub Actions.
- [ ] Open a draft pull request against `main` with a compact technical summary, testing evidence, and explicit non-goals.
