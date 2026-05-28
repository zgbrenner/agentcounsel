# Agent commands

Guidance for repo agents (Codex, Claude Code, Cursor, Gemini CLI, and similar)
working in the AgentCounsel checkout. It tells you which commands to run after
which kind of edit, which files are generated, and what not to touch. Full
per-script detail is in `docs/CLI.md`.

> AgentCounsel is Markdown-native, offline, and attorney-supervised. Every legal
> output is draft work product for attorney review. There is no backend, no
> database, and no network dependency — keep it that way.

## Golden rule

`skills/` and `core/` are the **canonical source of truth.** Several files are
**generated** from them and must be refreshed (not hand-edited) after a change:

| Generated file / dir | Refresh with |
|---|---|
| `metadata/index.json`, `metadata/router.json` | `py scripts/build_skill_index.py` |
| `metadata/packs.json`, `dist/` | `py scripts/build_platform_packs.py` |
| `reports/eval-coverage.md` | `py scripts/generate_eval_report.py` |
| `reports/skill-improvement-prompts.md`, `reports/skill-quality-checklist.md` | `py scripts/generate_skill_improvement_prompts.py` |
| `adapters/claude-code-plugin/skills/` | `py scripts/sync_plugin_skills.py` |
| generated cold-start interviews under `skills/setup/` | `py scripts/generate_cold_start_interviews.py` |
| `site/public/` | `node site/generate.mjs` |

## Validation sequence before commit

Run this full sequence and read the output before claiming done. All must pass:

```
py scripts/validate_repo.py
py scripts/build_skill_index.py --check
py scripts/build_platform_packs.py --check
py scripts/check_evals.py
py scripts/run_evals.py --strict --quiet
py scripts/generate_eval_report.py --check
py scripts/sync_plugin_skills.py --check
py scripts/generate_skill_improvement_prompts.py --check
py scripts/generate_cold_start_interviews.py --check
node site/generate.mjs
```

If a `--check` reports "out of date" / "out of sync", run the same script
without `--check` to regenerate, commit the result, and re-run the sequence.

## After editing... (do this)

**...a skill (`skills/<area>/<slug>/SKILL.md`):**
1. `py scripts/build_skill_index.py` (regenerate index + router).
2. If the skill is in the Claude Code plugin bundle: `py scripts/sync_plugin_skills.py`.
3. `py scripts/build_platform_packs.py` (its pack changed).
4. Update `SKILLS_INDEX.md` and, where relevant, `WORKFLOW_ROUTER.md` / `COMMANDS.md`.
5. `py scripts/generate_skill_improvement_prompts.py`; `node site/generate.mjs`.
6. `py scripts/validate_repo.py` and the full sequence above.

**...packs (`scripts/build_platform_packs.py` logic):**
1. `py scripts/build_platform_packs.py` to regenerate `metadata/packs.json` + `dist/`.
2. `node site/generate.mjs` (the packs page reads the manifest).
3. `py scripts/validate_repo.py` (pack-registry integrity).

**...evals (`evals/**/*.eval.yaml` or `evals/outputs/`):**
1. `py scripts/check_evals.py` (schema + metadata integrity).
2. `py scripts/run_evals.py --strict --quiet` (candidate outputs).
3. `py scripts/generate_eval_report.py` (refresh `reports/eval-coverage.md`).

**...site data (`site/generate.mjs`, assets, or any displayed metadata):**
1. `node site/generate.mjs`.
2. `py scripts/validate_repo.py` (doc/site link checks).

**...matter workspace templates (`matter-workspaces/_template/`), playbooks (`playbooks/`), or review panels (`review-panels/`):**
1. `py scripts/build_platform_packs.py` (packs include these where justified).
2. `py scripts/validate_repo.py` (template completeness, required sections, classification vocabulary).
3. `py scripts/check_evals.py` if you touched the related static evals.

**...top-level docs (`README.md`, `docs/*.md`, `QUICKSTART.md`, `CONTRIBUTING.md`):**
1. `py scripts/validate_repo.py` (required-docs presence + link resolution).

## Do not touch without a specific reason

- **Generated files** in the table above — edit the canonical source and
  regenerate. Hand-edits will be overwritten and will fail `--check`.
- **`adapters/claude-code-plugin/skills/`** — generated bundle; regenerate via
  `sync_plugin_skills.py`.
- **`matters/`** — git-ignored; holds confidential, potentially privileged local
  workspaces. Never commit its contents.
- **`dist/` and `site/public/`** — git-ignored build output.
- **The four hand-authored cold-start interviews** (contracts, corporate,
  litigation, privacy) — the interview generator must not overwrite them.
- **Anything under `skills/` or `core/`** when your task is only *using* a skill
  rather than editing the library (see `AGENTS.md`).

## Safety guardrails for any edit

- Never introduce legal-advice phrasing, an "AI lawyer" claim, invented authority,
  or a computed deadline. Use visible placeholders for gaps.
- Keep everything Markdown-native and offline; add no dependencies, network calls,
  or API keys.
- Note user-facing changes under "Unreleased" in `CHANGELOG.md`.

See `AGENTS.md` for the operating model, `docs/CLI.md` for per-script detail, and
`VALIDATION.md` for the validation checks.
