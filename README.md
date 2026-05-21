# AgentCounsel

**An open, Markdown-native legal skills library for AI agents — and the legal professionals who supervise them.**

[![License: Apache 2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Practice areas](https://img.shields.io/badge/practice%20areas-12-purple.svg)](SKILLS_INDEX.md)
[![Skills](https://img.shields.io/badge/skills-58-success.svg)](SKILLS_INDEX.md)
[![Surfaces](https://img.shields.io/badge/works%20with-ChatGPT%20%C2%B7%20Claude%20%C2%B7%20Gemini-lightgrey.svg)](#ways-to-use-agentcounsel)
[![Upstream](https://img.shields.io/badge/derived%20from-claude--for--legal-black.svg)](https://github.com/anthropics/claude-for-legal)
[![Unofficial](https://img.shields.io/badge/unofficial-not%20affiliated%20with%20Anthropic-red.svg)](NOTICE)

AgentCounsel is a collection of standalone *legal skills*. Each skill is a structured workflow that helps an AI agent — or a lawyer — produce **draft legal work product for attorney review**. The skills supply discipline and structure: how to scope a task, what inputs to gather, how to organize the output, and what a supervising attorney must verify.

> AgentCounsel does not provide legal advice. It produces draft work product intended for review and adoption by a qualified, licensed legal professional.

## Why AgentCounsel

Legal teams are increasingly using AI agents to draft, review, and triage. Most agent "instructions" for legal work are locked inside one vendor's product, hard to audit, and easy to misuse. AgentCounsel takes the opposite approach:

- **Markdown-native.** Every skill is a plain Markdown file a lawyer can read, edit, and trust.
- **Platform-agnostic.** No build system, no runtime, no lock-in. The skills work wherever an agent or person can read Markdown.
- **Safety-first.** Every skill is built around the same core rules: draft only, attorney review required, never invent authority, preserve confidentiality.
- **Composable.** Use one skill or the whole library. Copy a single file into any assistant, or bundle the set into an agent project.

## What this is — and is not

**It is:**

- A library of legal *workflows* and *output structures*.
- A way to make AI-assisted legal drafting more consistent, reviewable, and safe.
- Useful piecemeal (one Markdown file) or as a whole.

**It is not:**

- Legal advice, or a substitute for a licensed attorney.
- A source of jurisdiction-specific legal rules. Skills give you process, not the law.
- Built around any single AI product. It is not a "ChatGPT Project" — it is a portable library with adapters for many environments.

## How it is organized

```
core/               Operating rules every skill inherits (read these first).
skills/             The canonical skill library, grouped by practice area.
practice-profiles/  Per-practice-area configuration profiles for a legal team.
matter-workspaces/  Single-file scaffolds for organizing one specific matter.
adapters/           Thin integration files for specific environments.
SKILLS_INDEX.md     Full catalog of every skill.
WORKFLOW_ROUTER.md  "I need to do X" -> which skill to use.
COMMANDS.md         Slash-style command shorthands mapped to skills.
CONTEXT.md          Vocabulary and mental model for AI agents working in the repo.
```

The `skills/` directory is the **canonical source of truth.** Everything else points back to it.

### Anatomy of a skill

Each skill lives in its own folder with a `SKILL.md` file and optional `templates/`:

```
skills/contracts/nda-review/
  SKILL.md                     The workflow.
  templates/nda-risk-table.md  A copyable, attorney-review-ready template.
```

Every `SKILL.md` follows the same structure: Purpose, Use When, Required Inputs, Do Not Use When, Legal Safety Rules, Workflow, Output Format, and an Attorney Verification Checklist.

## Practice areas

| Practice area | Covers |
|---|---|
| Legal Research | Turning research questions into structured, verifiable memos. |
| Litigation | Matter intake, chronologies, demand letters, subpoena triage, depositions, legal holds, privilege logs, claim charts, brief drafting. |
| Contracts | NDAs, commercial contracts, redlines, statements of work. |
| Corporate | Board minutes, written consents, closing checklists, due-diligence review, entity compliance. |
| Employment | Terminations, worker classification, hiring, internal investigations, protected leave, severance, workplace policies. |
| Privacy | Data processing agreements, impact assessments, data subject requests, policy gaps. |
| Product Legal | Launch review, marketing claims, terms of service, AI features. |
| Regulatory | Enforcement risk, rule-change summaries, compliance gaps. |
| AI Governance | AI use-case intake, vendor terms, model risk, AI policies. |
| Intellectual Property | Trademark triage, infringement triage, cease-and-desist response, patent and invention triage, DMCA, open-source licensing. |
| Setup | Cold-start interviews that configure AgentCounsel for a practice group by filling in a practice profile. |
| Legal Methodology | Cross-cutting analytical disciplines: red-team verification, statutory interpretation, risk assessment, source validation. |

See `SKILLS_INDEX.md` for the full catalog.

### Configuring AgentCounsel for a team

Two optional layers let a legal team adapt the library without changing any skill:

- **`practice-profiles/`** — one profile per practice area capturing the team's jurisdictions, escalation thresholds, standard positions, review requirements, and prohibited assumptions. An agent loads the relevant profile alongside `core/` and a skill. The **Setup** skills run a cold-start interview to fill a profile in.
- **`matter-workspaces/`** — single-file scaffolds for organizing one specific matter: parties, documents, deadlines (always flagged for attorney verification), open items, and an index of the draft work product produced by skills.

Both are plain Markdown. They add no backend, runtime, or vendor dependency.

## Ways to use AgentCounsel

**1. Piecemeal — one Markdown file.** Open any `SKILL.md`, copy it into your AI assistant or paste it as context, and follow the workflow. See `adapters/generic-md/`.

**2. As a local-folder playbook.** Keep the repo (or just `skills/` and `core/`) in a folder your assistant can read, and let it route to the right skill. See `adapters/claude-cowork/`.

**3. As a repo-agent instruction library.** Point a coding or repo agent at the library so it selects the narrowest relevant skill. See `adapters/codex/`.

**4. As a Claude Code plugin-style bundle.** Use the curated starter bundle in `adapters/claude-code-plugin/`.

**5. As a Gemini CLI extension.** Install the repository as a Gemini CLI extension; `gemini-extension.json` and `GEMINI.md` load the operating model automatically. See `adapters/gemini/`.

**6. Bundled into your own agent project.** Vendor the `skills/` and `core/` directories into your project and reference them from your agent's instructions.

## Quick start

1. Read the `core/` files — they are the operating rules for every skill.
2. Open `WORKFLOW_ROUTER.md` and find the workflow that matches your task.
3. Open that skill's `SKILL.md` and gather the Required Inputs.
4. Follow the Workflow. Produce the Output Format.
5. Complete the Attorney Verification Checklist before relying on anything.

## Core safety model

Every skill inherits the rules in `core/`:

- **Draft legal work product only.** Attorney review is always required.
- **Never invent legal authority, citations, quotations, facts, or deadlines.**
- **Separate** facts, assumptions, law, analysis, strategy, and verification items.
- **Identify** jurisdiction, governing law, posture, and the relevant date — or flag them as unknown.
- **Preserve** confidentiality and privilege.
- **Flag uncertainty** with visible placeholders instead of guessing.

## Adapters

Adapters are intentionally **thin**. They tell a particular environment how to find and use the canonical library; they do not re-document or duplicate it. The one exception is the Claude Code plugin bundle, which carries generated copies of a curated set of skills (and their templates) for packaging; run `python scripts/sync_plugin_skills.py` to regenerate it from `skills/`, and see `PLUGIN_SYNC.md`.

| Adapter | For | Path |
|---|---|---|
| Generic Markdown | Any AI assistant or agent | `adapters/generic-md/` |
| Codex / repo agents | Repo-based coding and legal agents | `adapters/codex/` |
| Claude Code plugin | Plugin-style packaging | `adapters/claude-code-plugin/` |
| Claude / Cowork | Local-folder playbook use | `adapters/claude-cowork/` |
| Gemini CLI | Gemini CLI extension | `adapters/gemini/` |

## Validation

The repository includes a lightweight validation script that checks every skill has the required structure and frontmatter, that relative links and index paths resolve, and that the safety framing is consistent. It uses only the Python standard library.

```
python scripts/validate_repo.py
```

Run it before opening or updating a pull request. See `VALIDATION.md` for the full list of checks.

The Claude Code plugin bundle under `adapters/claude-code-plugin/` is **generated** from `skills/`. Regenerate it with `python scripts/sync_plugin_skills.py`; validation reports any drift. See `PLUGIN_SYNC.md`.

### Continuous integration

GitHub Actions runs the same checks on every pull request and on pushes to `main`:

```
python scripts/sync_plugin_skills.py --check   # plugin bundle is in sync
python scripts/validate_repo.py                # full repository validation
```

The workflow is `.github/workflows/validate.yml`. It uses only Python and the standard library — no extra dependencies.

## Browsable skill catalog

A static, browser-readable catalog of every skill lives under `site/`. It is generated from the canonical `skills/` directory and includes a homepage, one page per practice area, one page per skill (each with **Copy Full Skill** and **Copy One-Off Prompt** buttons and the full raw `SKILL.md`), platform setup guides, and `llms.txt` / `llms-full.txt` for browser-based LLM agents.

The generator is a zero-dependency Node script — nothing to install — so it keeps the repository's no-dependency, Markdown-first philosophy.

```
cd site
npm run build      # generate the static site into site/public/
npm run serve      # preview it at http://localhost:8080
npm run dev        # build, then serve
```

The output in `site/public/` is plain HTML, one CSS file, and a small script. Deploy it by serving that directory with any static host (GitHub Pages, Netlify, Vercel, an object store, or a plain file server) — there is no backend, no login, and no build step beyond `npm run build`. Re-run the build after adding or editing a skill so the catalog stays in sync. See `site/README.md` for details.

## Contributing

New skills are welcome. AgentCounsel is Markdown-first and safety-first — see `CONTRIBUTING.md` for the rules, and `SECURITY.md` for security guidance.

## License

Apache License 2.0. See `LICENSE`. Attribution for content adapted from other open-source projects is recorded in `NOTICE`.

## Disclaimer

AgentCounsel is a workflow library — not a law firm and not a lawyer. Using it does not create an attorney-client relationship, and it does not provide legal advice. All output is draft work product that must be reviewed and adopted by a qualified, licensed legal professional before it is relied upon. You are responsible for the use of these materials and for compliance with the rules of professional conduct that apply to you.
