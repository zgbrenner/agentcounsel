# Skill Specification v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a backward-compatible typed execution contract for every AgentCounsel skill, validate optional custom `SPEC.json` sidecars, pilot the format on three skills, and expose compiled contracts through MCP.

**Architecture:** `scripts/skill_spec_v2.py` is the pure standard-library compiler and validator. `scripts/build_skill_specs.py` scans canonical skills and generates `metadata/skill_specs.json`. Existing `SKILL.md` files remain canonical human-readable workflows; optional `SPEC.json` files enrich the generated contract. The MCP service loads the generated contracts separately from routing cards.

**Tech Stack:** Python 3.12 standard library, JSON and JSON Schema documents, `unittest`, FastMCP adapter, GitHub Actions.

## Global Constraints

- Do not rewrite any existing `SKILL.md` body in Phase 2A.
- Keep all tooling standard-library only.
- Preserve the eleven existing frontmatter fields and eight required H2 sections.
- Custom specs may strengthen but never weaken attorney review, stop-and-ask, source discipline, or no-deadline-calculation controls.
- Do not add model calls, embeddings, connector execution, document parsing, or autonomous legal conclusions.
- `metadata/skill_specs.json` is generated and never hand-edited.
- Every legacy skill must compile without a custom sidecar.

---

### Task 1: Define the failing compiler contract

**Files:**
- Create: `tests/test_skill_spec_v2.py`

**Interfaces:**
- Consumes: temporary skill directories containing legacy `SKILL.md` files and optional `SPEC.json` overlays.
- Produces the test contract for:
  - `SpecValidationError`
  - `compile_skill_spec(skill_dir, metadata, body, derived) -> dict`
  - `load_custom_spec(skill_dir) -> dict | None`
  - `validate_compiled_spec(spec, root) -> list[str]`

- [ ] Write a legacy fixture with required and optional inputs.
- [ ] Assert legacy compilation creates schema version `2.0`, baseline inheritance, safety gates, three execution modes, typed inputs, typed outputs, evidence requirements, and no custom-spec flag.
- [ ] Assert `Optional:` inputs become optional and all required inputs have `may_infer: false`.
- [ ] Assert a custom overlay may refine types, add enum values, add modules, disable a mode, and add a stricter custom gate.
- [ ] Assert an overlay cannot disable attorney review, allow deadline calculation, change missing-input behavior, or remove baseline evidence fields.
- [ ] Assert duplicate IDs, invalid controlled types, and unresolved module paths fail validation.
- [ ] Run `python -m unittest tests.test_skill_spec_v2 -v` and confirm failure because `skill_spec_v2` does not exist.
- [ ] Commit the failing tests.

### Task 2: Implement the pure compiler and validator

**Files:**
- Create: `scripts/skill_spec_v2.py`
- Create: `specs/skill-spec-v2.schema.json`

**Interfaces:**
- Produces:
  - `SCHEMA_VERSION = "2.0"`
  - `SPEC_FILENAME = "SPEC.json"`
  - `SpecValidationError(ValueError)`
  - `load_custom_spec(skill_dir: Path) -> dict | None`
  - `compile_skill_spec(skill_dir: Path, metadata: dict, body: str, derived: dict, root: Path) -> dict`
  - `validate_compiled_spec(spec: dict, root: Path) -> list[str]`

- [ ] Implement deterministic slug creation for inferred field and artifact IDs.
- [ ] Compile legacy frontmatter into typed input and output records.
- [ ] Add baseline inheritance and conditional jurisdiction/deadline inheritance.
- [ ] Add normalized gates and risk-sensitive escalation defaults.
- [ ] Add quick-triage, standard, and deep-review modes.
- [ ] Add baseline evidence schema and required fields.
- [ ] Merge custom overlays by stable IDs rather than replacing entire collections blindly.
- [ ] Enforce non-weakening safety invariants after merge.
- [ ] Validate controlled values, unique IDs, and repository paths.
- [ ] Publish the equivalent JSON Schema reference document.
- [ ] Run focused tests and confirm they pass.
- [ ] Run the full test suite.
- [ ] Commit compiler, validator, and schema.

### Task 3: Define and implement generated skill contracts

**Files:**
- Create: `tests/test_build_skill_specs.py`
- Create: `scripts/build_skill_specs.py`
- Generate: `metadata/skill_specs.json`

**Interfaces:**
- Produces:
  - `collect_skill_specs(root: Path) -> dict`
  - `render_output(data: dict) -> str`
  - `write_output(root: Path, check: bool = False) -> bool`

- [ ] Write failing tests for deterministic ordering, legacy compilation, custom-sidecar inclusion, invalid-sidecar failure, and `--check` drift detection.
- [ ] Confirm focused tests fail before implementation.
- [ ] Reuse `_shared.load_frontmatter` and `build_skill_index` derivation helpers rather than reparsing skills independently.
- [ ] Compile every canonical skill and report custom-spec counts and coverage by practice area.
- [ ] Generate `metadata/skill_specs.json` with one contract per stable skill ID.
- [ ] Run focused and full tests.
- [ ] Commit generator and generated artifact.

### Task 4: Add three reviewed pilot sidecars

**Files:**
- Create: `skills/contracts/nda-review/SPEC.json`
- Create: `skills/legal-research/legal-research-memo/SPEC.json`
- Create: `skills/privacy/breach-response-workflow/SPEC.json`
- Create: `docs/templates/SPEC_TEMPLATE.json`
- Create: `docs/SKILL_SPEC_V2.md`

**Interfaces:**
- Each sidecar is a partial v2 overlay keyed by stable IDs and compiled against safe defaults.

- [ ] Add typed NDA inputs, enum client role and transaction context, structured outputs, modules, and three modes.
- [ ] Add typed legal-research inputs, authority evidence, connector/reference modules, and deep-review source-validation requirements.
- [ ] Add critical breach gates, sensitive inputs, immediate escalation, privileged outputs, and strict deadline/reportability boundaries.
- [ ] Add a copyable generic template containing no real matter facts.
- [ ] Document migration, non-weakening rules, generated artifacts, and validation commands.
- [ ] Regenerate `metadata/skill_specs.json`.
- [ ] Add tests that load and validate all three real pilot sidecars.
- [ ] Commit pilot migration and documentation.

### Task 5: Expose typed contracts through MCP

**Files:**
- Modify: `agentcounsel_mcp.py`
- Modify: `mcp_server.py`
- Modify: `docs/MCP_SERVER.md`
- Modify: `tests/test_mcp_service.py`

**Interfaces:**
- Adds `CatalogService.get_skill_spec(skill_id: str) -> dict`.
- Adds MCP tool `get_skill_spec`.
- Route responses gain `execution_modes`, typed `missing_required_inputs`, `custom_gates`, and `spec_version`.

- [ ] Write failing MCP tests using a fixture `metadata/skill_specs.json`.
- [ ] Confirm tests fail before implementation.
- [ ] Load and validate the generated contract index once at service creation.
- [ ] Resolve contracts through the existing stable-ID alias layer.
- [ ] Use compiled contract gates, quality checks, and typed required inputs in route responses.
- [ ] Keep backward-compatible card and full-Markdown retrieval unchanged.
- [ ] Update MCP documentation and examples.
- [ ] Run focused and full tests.
- [ ] Commit MCP integration.

### Task 6: Integrate validation, reporting, and repository guidance

**Files:**
- Modify: `.github/workflows/validate.yml`
- Modify: `scripts/check_all.py`
- Modify: `docs/SKILL_METADATA_STANDARD.md`
- Modify: `docs/templates/SKILL_TEMPLATE.md`
- Modify: `CONTRIBUTING.md`
- Modify: `CHANGELOG.md`

**Interfaces:**
- CI runs `python scripts/build_skill_specs.py --check` after the legacy index is checked.

- [ ] Add permanent generated-contract drift validation to CI and local `check_all.py`.
- [ ] Document that frontmatter remains v1 discovery metadata and `SPEC.json` is the optional v2 execution overlay.
- [ ] Link the sidecar template from the skill template and contributor guide.
- [ ] Add an Unreleased changelog entry.
- [ ] Run `python scripts/check_all.py`.
- [ ] Confirm plugin synchronization remains unchanged because sidecars are execution metadata, not duplicated skill bodies.
- [ ] Commit integration and documentation.

### Task 7: Final verification and pull request

**Files:**
- Review all changed files.

- [ ] Confirm the three pilot `SKILL.md` files are unchanged.
- [ ] Confirm no other `SKILL.md` file changed.
- [ ] Confirm all 212 skills appear in `metadata/skill_specs.json`.
- [ ] Confirm exactly three custom sidecars are reported.
- [ ] Confirm every generated contract retains attorney review and no-deadline-calculation safeguards.
- [ ] Confirm full GitHub Actions validation passes.
- [ ] Open a review-ready pull request against `main` with implementation details, migration boundaries, generated coverage, and testing evidence.
