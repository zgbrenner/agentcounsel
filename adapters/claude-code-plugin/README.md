# AgentCounsel — Claude Code Plugin Adapter

This folder packages a curated starter bundle of AgentCounsel skills in a plugin-style layout.

## What is here

- `plugin.json` — plugin manifest metadata.
- `skills/` — a curated **starter bundle** of skills.

## Starter bundle

The bundle contains a small, high-value subset of the library:

| Skill | Purpose |
|---|---|
| `legal-core` | The AgentCounsel core operating rules as a single loadable skill. |
| `legal-research-memo` | Structuring a legal research question into a reviewable memo. |
| `nda-review` | Reviewing an NDA for risk and redline points. |
| `contract-risk-review` | Risk-reviewing a general commercial contract. |
| `demand-letter` | Drafting a demand letter outline and draft. |
| `litigation-chronology` | Building a sourced factual timeline from documents. |
| `termination-risk` | Organizing the facts around a proposed termination. |
| `dpa-review` | Reviewing a data processing agreement. |
| `ai-use-case-intake` | Intaking and triaging a proposed AI use case. |

## Canonical source

> **The canonical source of truth is the repository's `/skills` directory** (and `/core`).
>
> The skill folders here are **generated copies**. Do not edit them directly. Edit the canonical skill under `/skills`, then regenerate this bundle:
>
> ```
> python scripts/sync_plugin_skills.py
> ```
>
> See `PLUGIN_SYNC.md` for details. Validation (`python scripts/validate_repo.py`) reports any drift between this bundle and `/skills`.

The full library — all practice areas and templates — lives under `/skills`. This adapter is intentionally a thin, partial bundle, not a duplicate of the whole library. `legal-core` is the one hand-maintained skill here: it summarizes the `/core` operating rules and is preserved by the sync script.

## Using the bundle

Load `legal-core` first; it carries the operating rules every other skill depends on. Then load the specific skill for your task. Every skill produces draft legal work product for attorney review — see the root `README.md`, `SECURITY.md`, and `core/` for the full safety model.

## Templates

Where a bundled skill has templates, the sync script copies them into the skill's own `templates/` folder, so the bundle is self-contained. (`ai-use-case-intake` has no template; `legal-core` is hand-maintained and has none.)
