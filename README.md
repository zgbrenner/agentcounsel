# AgentCounsel

**An open, Markdown-native legal skills library for AI agents — and the legal professionals who supervise them.**

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
core/        Operating rules every skill inherits (read these first).
skills/      The canonical skill library, grouped by practice area.
adapters/    Thin integration files for specific environments.
SKILLS_INDEX.md     Full catalog of every skill.
WORKFLOW_ROUTER.md  "I need to do X" -> which skill to use.
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
| Litigation | Matter intake, chronologies, demand letters, subpoena triage. |
| Contracts | NDAs, commercial contracts, redlines, statements of work. |
| Employment | Terminations, severance agreements, workplace policies. |
| Privacy | Data processing agreements, data subject requests, policy gaps. |
| Product Legal | Launch review, marketing claims, terms of service, AI features. |
| Regulatory | Enforcement risk, rule-change summaries, compliance gaps. |
| AI Governance | AI use-case intake, vendor terms, model risk, AI policies. |
| Intellectual Property | Trademark triage, DMCA notices, open-source licensing. |

See `SKILLS_INDEX.md` for the full catalog.

## Ways to use AgentCounsel

**1. Piecemeal — one Markdown file.** Open any `SKILL.md`, copy it into your AI assistant or paste it as context, and follow the workflow. See `adapters/generic-md/`.

**2. As a local-folder playbook.** Keep the repo (or just `skills/` and `core/`) in a folder your assistant can read, and let it route to the right skill. See `adapters/claude-cowork/`.

**3. As a repo-agent instruction library.** Point a coding or repo agent at the library so it selects the narrowest relevant skill. See `adapters/codex/`.

**4. As a Claude Code plugin-style bundle.** Use the curated starter bundle in `adapters/claude-code-plugin/`.

**5. Bundled into your own agent project.** Vendor the `skills/` and `core/` directories into your project and reference them from your agent's instructions.

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

Adapters are intentionally **thin**. They tell a particular environment how to find and use the canonical library; they do not re-document or duplicate it. The one exception is the Claude Code plugin bundle, which may carry copied starter skills for packaging — those are regenerated from `skills/` before release.

| Adapter | For | Path |
|---|---|---|
| Generic Markdown | Any AI assistant or agent | `adapters/generic-md/` |
| Codex / repo agents | Repo-based coding and legal agents | `adapters/codex/` |
| Claude Code plugin | Plugin-style packaging | `adapters/claude-code-plugin/` |
| Claude / Cowork | Local-folder playbook use | `adapters/claude-cowork/` |

## Contributing

New skills are welcome. AgentCounsel is Markdown-first and safety-first — see `CONTRIBUTING.md` for the rules, and `SECURITY.md` for security guidance.

## License

Apache License 2.0. See `LICENSE`.

## Disclaimer

AgentCounsel is a workflow library — not a law firm and not a lawyer. Using it does not create an attorney-client relationship, and it does not provide legal advice. All output is draft work product that must be reviewed and adopted by a qualified, licensed legal professional before it is relied upon. You are responsible for the use of these materials and for compliance with the rules of professional conduct that apply to you.
