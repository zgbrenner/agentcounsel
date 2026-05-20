# AGENTS.md — AgentCounsel (Codex / Repo-Agent Adapter)

This repository is **AgentCounsel**, a Markdown legal skills library. If you are a repo-based coding or legal agent working in this repository, follow these instructions.

## Canonical library

- The canonical skill library is `/skills`. Treat it as the source of truth.
- The operating rules are in `/core`. They apply to every skill.
- Use `WORKFLOW_ROUTER.md` to map a task to a skill, and `SKILLS_INDEX.md` to browse.

## How to work

1. **Select the narrowest relevant skill.** Match the task to one skill in `/skills`. If several could apply, choose the most specific one.
2. **Read only what you need.** Read the selected `SKILL.md`, its `templates/`, and the `/core` rules. Do **not** load unrelated practice areas or the rest of the library.
3. **Follow the skill.** Use its Workflow and Output Format exactly.
4. **Produce draft legal work product for attorney review.** Never present output as legal advice or as final.

## Hard rules

- Never invent legal authority, citations, quotations, facts, or deadlines.
- Use user-provided documents first. Treat background knowledge as unverified.
- Identify jurisdiction, governing law, posture, and the relevant date — or flag them as unknown.
- Preserve confidentiality and privilege. Keep client-sensitive facts out of templates.
- Use placeholders (`[CONFIRM: ...]`, `[VERIFY: ...]`) wherever verification is needed. Never guess.
- Include the skill's Attorney Verification Checklist with every deliverable.

## Editing the library

If your task is to **use** the skills, do not modify them. Only edit files under `/skills`, `/core`, or `/adapters` when the task is explicitly to improve the library itself — and then follow `CONTRIBUTING.md`.

## Not covered

If no skill fits the task, say so. Do not improvise a legal workflow.
