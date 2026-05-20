# Start Here — AgentCounsel as a Local-Folder Legal Playbook

You are looking at **AgentCounsel**, an open Markdown legal skills library, set up as a local-folder playbook. This file tells an AI assistant — or a person — how to use it.

## What this folder is

AgentCounsel is a library of **legal skills**. Each skill is a structured workflow that produces **draft legal work product for attorney review**. It is not legal advice. The canonical library lives in the `skills/` directory, with shared operating rules in `core/`.

## How to use it

1. **Read the core rules first.** Open the files in `core/`. They are the operating rules for every skill, and they always apply.
2. **Route the task.** Use `WORKFLOW_ROUTER.md` (in this folder) to map the request to a skill. To browse, use `SKILLS_INDEX.md`.
3. **Open the skill.** Read that skill's `SKILL.md` and any file in its `templates/` folder.
4. **Gather Required Inputs.** If an input is missing, stop and ask — do not guess.
5. **Follow the Workflow.** Produce the skill's Output Format.
6. **Hand off for review.** Complete the Attorney Verification Checklist. Every output is a draft for a qualified, licensed legal professional to review.

## Working rules for the assistant

- Treat `core/` and `skills/` as a **reference library**. Follow the skills; do not rewrite them.
- **Do not modify the source skill files** (`core/`, `skills/`, `SKILLS_INDEX.md`, `WORKFLOW_ROUTER.md`) unless the user explicitly asks to edit the library itself. Day to day, you read the library and produce deliverables as separate documents.
- Produce draft legal work product only. Never present output as legal advice or as final.
- Never invent legal authority, citations, quotations, facts, or deadlines.
- Preserve confidentiality and privilege. Keep client-sensitive facts out of templates. See `SECURITY.md`.
- Use placeholders (`[CONFIRM: ...]`, `[VERIFY: ...]`) for anything uncertain.

## Where things live

- `core/` — operating rules (read first).
- `skills/` — the canonical skill library, by practice area.
- `WORKFLOW_ROUTER.md` (this folder) — task-to-skill routing.
- `SKILLS_INDEX.md` (this folder) — the full catalog.

## Editing the library

If the user wants to **improve a skill** or add one, that is editing the library itself — follow `CONTRIBUTING.md`. Otherwise, leave the source files unchanged and deliver your work product separately.
