# AgentCounsel — Generic Markdown Adapter

This adapter explains how to use AgentCounsel with **any** AI assistant or legal agent, with no special integration. If your tool can read Markdown, it can use AgentCounsel.

## The idea

Every AgentCounsel skill is a self-contained Markdown file. To use one, you give your AI assistant two things:

1. The **core operating rules** (`core/`) — the safety rules every skill depends on.
2. The **one skill** you need for the task (its `SKILL.md` and any template it references).

That is the whole integration. No plugins, no configuration.

## How to use it

See `START_HERE.md` in this folder for step-by-step instructions.

In short:

1. Pick the skill with `WORKFLOW_ROUTER.md` or `SKILLS_INDEX.md`.
2. Paste the `core/` rules and the chosen `SKILL.md` into your assistant as context.
3. Provide the skill's Required Inputs.
4. Follow the Workflow; produce the Output Format.
5. Complete the Attorney Verification Checklist before relying on anything.

## What to copy

For a single task you typically need:

- `core/legal-work-product.md`
- `core/confidentiality-and-privilege.md`
- `core/source-and-citation-discipline.md`
- `core/jurisdiction-and-deadline-gates.md`
- `core/output-format-rules.md`
- `core/attorney-review-checklist.md`
- `core/business-stakeholder-communication.md` (when briefing a non-lawyer stakeholder)
- the chosen `skills/.../SKILL.md`
- any template in that skill's `templates/` folder

If your assistant has limited context, paste the core rules once at the start of a session and reuse them across tasks.

## Keep it canonical

This adapter intentionally contains **no copies** of skills. The canonical source is the repository's `skills/` and `core/` directories. Always copy from there, so you get the current version.

## Reminder

AgentCounsel produces draft legal work product for attorney review. It is not legal advice. A qualified, licensed legal professional must review every output.
