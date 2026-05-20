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
> The `SKILL.md` files in this folder are **packaged copies**, included so the bundle is self-contained. They are not the source of truth and can drift from the originals. **Regenerate them from the canonical `/skills` and `/core` files before any release** of this plugin bundle.

The full library — all practice areas and templates — lives under `/skills`. This adapter is intentionally a thin, partial bundle, not a duplicate of the whole library.

## Using the bundle

Load `legal-core` first; it carries the operating rules every other skill depends on. Then load the specific skill for your task. Every skill produces draft legal work product for attorney review — see the root `README.md`, `SECURITY.md`, and `core/` for the full safety model.

## Note on templates

Some canonical skills reference templates in a `templates/` folder (for example, `nda-review` references `templates/nda-risk-table.md`). The packaged copies here include the `SKILL.md` workflow only. When a template is needed, copy it from the canonical skill folder under `/skills`, or regenerate this bundle to include it.
