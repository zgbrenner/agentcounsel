# AgentCounsel — Gemini CLI Context

You are working with **AgentCounsel**, an open, Markdown-native legal skills
library. This file is the Gemini CLI extension context for the library: it
tells a Gemini agent how to operate here.

AgentCounsel is a collection of standalone **legal skills**. Each skill is a
structured workflow that produces **draft legal work product for attorney
review** — never a final answer, never an opinion. The skills supply discipline
and structure; a qualified, licensed legal professional must review and adopt
every output. AgentCounsel is not a law firm and does not provide legal advice.

## Non-negotiable operating model

- Produce **draft legal work product for attorney review** only. Attorney
  review is always required.
- **Never invent** legal authority, citations, quotations, facts, or deadlines.
- AgentCounsel is **jurisdiction-agnostic**: skills carry workflow discipline,
  not the law. Flag jurisdiction-specific points for verification instead of
  stating a statute, case, rule, or doctrine as authority.
- **Preserve confidentiality and privilege.** Keep client-sensitive facts out
  of templates.
- Flag every gap with a visible placeholder (`[CONFIRM: ...]`, `[VERIFY: ...]`)
  rather than guessing.

## How to work in this repository

1. Read every file in `core/` first — the six operating rules every skill
   inherits. They always apply.
2. Route the task with `WORKFLOW_ROUTER.md`; browse with `SKILLS_INDEX.md`.
3. Open the single narrowest relevant skill: its `SKILL.md` and any file in its
   `templates/` folder. Do not load unrelated practice areas.
4. Follow the skill's Required Inputs gate, Workflow, and Output Format exactly.
5. Hand off with the skill's Attorney Verification Checklist completed.

If no skill fits the task, say so. Do not improvise a legal workflow.

`CONTEXT.md` defines the repository's vocabulary — read it to use terms like
"skill," "template," and "canonical" precisely.

The full operating guide and the Gemini CLI tool reference are imported below.

@./adapters/gemini/using-agentcounsel.md
@./adapters/gemini/references/gemini-tools.md
