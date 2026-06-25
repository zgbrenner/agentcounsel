# Platform Gap Analysis

This analysis treats the current AgentCounsel repository as the baseline. The
library already has a large canonical skill corpus, machine-readable metadata,
evals, adapters, matter packs, matter workspaces, practice profiles,
connectors, validation scripts, and a generated site. Follow-up work should
extend those systems rather than rebuild them.

## Current System Inventory

| System | Current implementation |
|---|---|
| Metadata | YAML frontmatter on every canonical `skills/<area>/<skill>/SKILL.md`, documented in `docs/SKILL_METADATA_STANDARD.md`, generated into `metadata/index.json` by `scripts/build_skill_index.py`. |
| Evals | YAML eval cases in `evals/skills/`, shared assertions in `evals/shared/assertions.md`, rubric in `evals/SKILL_QUALITY_RUBRIC.md`, schema checker `scripts/check_evals.py`, heuristic runner `scripts/run_evals.py`, candidate outputs under `evals/outputs/`. |
| Matter packs | Practice-area workflow bundles in `matter-packs/`, documented by `matter-packs/README.md`. |
| Matter workspaces | Single-file matter scaffolds in `matter-workspaces/`, plus `skills/setup/create-matter-workspace/SKILL.md`. |
| Practice profiles | Per-practice-area profile files in `practice-profiles/`, populated through setup cold-start skills. |
| Platform adapters | Thin adapters for generic Markdown, Claude Code plugin, Claude cowork, Gemini, Codex, repo agents, ChatGPT project use, and Cursor-style use through generated packs and repo-agent files. |
| Site | Static catalog generator in `site/generate.mjs`, local server in `site/serve.mjs`, pack downloads and platform guides described in `site/README.md`. |
| Validation | `scripts/validate_repo.py`, `scripts/sync_plugin_skills.py --check`, `scripts/check_evals.py`, `scripts/run_evals.py --strict --quiet`, GitHub Actions in `.github/workflows/validate.yml`. |
| Connectors | Markdown connector contracts under `connectors/` for CourtListener, Federal Register, and eCFR; no runtime network layer. |

## Capability Comparison

| Target capability | Current state | Gap | Recommended next move |
|---|---|---|---|
| Machine-readable skill registry | Strong. `metadata/index.json` contains 191 skills, counts by area/type/risk, and per-skill metadata. | Registry is skill-centric; it does not yet expose packs, workspaces, adapters, connectors, or eval coverage as first-class registry objects. | Extend `metadata/index.json` or add `metadata/platform.json` with generated records for packs, workspaces, adapters, connectors, and eval coverage. |
| Skill router | Strong human/agent docs: `WORKFLOW_ROUTER.md`, `COMMANDS.md`, descriptions in metadata. | No generated router artifact for machines to consume directly. | Generate `metadata/router.json` from existing skill metadata and `COMMANDS.md`; do not hand-maintain a second router. |
| Platform pack builder | Strong. `scripts/build_platform_packs.py` builds ChatGPT, Claude, Gemini, and repo-agent packs from canonical sources. | Pack manifest and pack validation outputs are not exposed as a machine-readable build report. Cursor support is mostly through generic/repo-agent files rather than a dedicated adapter manifest. | Add a generated pack manifest and a thin Cursor pack target if current Cursor plugin specs become license-clear enough to use. |
| Claude/Cursor/ChatGPT/Gemini/Codex adapters | Good thin-adapter coverage through `adapters/`, root agent files, `gemini-extension.json`, and generated platform packs. | Adapter capability matrix is spread across README, site, and adapter folders. Cursor and ChatGPT remain mostly generic Markdown/project-pack flows. | Add `docs/ADAPTER_CAPABILITY_MATRIX.md` or include this in generated site data; keep adapters thin. |
| Eval harness | Good zero-dependency static eval system with schema checks and heuristic assertion scoring. | No model-judged path, no per-skill coverage dashboard, and no automated legal prose/style pass. | Add eval coverage metadata and a style/source-validation runner that checks candidate outputs before any optional model-judge integration. |
| Legal prose quality pass | Partial. Core output rules, skill checklists, and eval assertions enforce discipline. | No dedicated automated pass for AI tells, vague prose, overclaiming, or missing attorney-review framing across generated outputs. | Add a stdlib `scripts/check_legal_prose.py` focused on repository-owned sample outputs and eval candidates; borrow patterns conceptually from MIT-licensed anti-slop projects without copying text. |
| Citation/source validation | Strong policy layer in `core/source-and-citation-discipline.md`, legal-methodology source-validation skill, and connector docs. | Connectors are documentation-only; no machine-readable connector registry or source-check report. | Add `metadata/connectors.json` generated from `connectors/README.md` and optional scripts that verify connector docs, not live legal authority. |
| Firm/practice/matter profiles | Good practice profiles and cold-start interview skills. | Profiles are Markdown-only and not indexed in metadata; no schema validator specific to profile sections. | Add a profile registry and section validator while preserving Markdown as source of truth. |
| Matter workspaces | Good templates and a setup skill. | Workspace templates are not indexed, and there is no validation that referenced skills still exist beyond general link checks. | Add workspace metadata extraction and a workspace-specific validation pass. |
| Legal review panels | Partial. Every skill has an Attorney Verification Checklist; workspace sign-off exists. | No reusable review-panel template or structured output schema for surfacing review status across skills, evals, and workspaces. | Add a canonical review-panel block pattern and optionally a `core/legal-review-panel.md` file consumed by high-risk skills. |
| Website pack builder | Strong. Site generator and pack pages are already present. | Site data is generated directly from files; no shared generated data layer for the site, registry, and pack builder. | Factor common metadata loading into scripts or generate a shared JSON file used by site and pack builders. |
| Local/self-hosted future app path | Early. Repository is static Markdown with no runtime, which is a good substrate. | No local app, persistence layer, auth model, or self-hosted deployment plan. | Plan a separate optional app path that consumes generated metadata and Markdown files; do not turn the core library into an app. |

## High-Leverage Gaps

The next work should focus on generated metadata and validation because that
benefits every platform without rewriting the library:

1. Add generated registries for router, packs, adapters, connectors, profiles,
   workspaces, and eval coverage.
2. Add a legal prose and source-discipline static pass for examples and eval
   outputs.
3. Add a review-panel pattern for high-risk legal outputs.
4. Improve platform-specific pack manifests while keeping all content generated
   from canonical `skills/`, `core/`, `practice-profiles/`, and `matter-packs/`.
