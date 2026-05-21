# Using AgentCounsel

How an AI agent finds and uses an AgentCounsel skill before producing any legal
work product. Read this once at the start of a session; it governs how you
operate in this repository.

AgentCounsel is **not** a coding library, and its skills are **not** tools you
call. Each skill is a Markdown workflow you read and follow. "Using a skill"
means routing to it, reading it, and producing its Output Format under the
`core/` rules.

## Instruction priority

When instructions conflict, follow this order:

1. **The user's direct instructions**, including those in repository context
   files (`GEMINI.md`, `AGENTS.md`, `CLAUDE.md`).
2. **The `core/` operating rules** and the safety discipline in this guide.
   These are never overridden to produce unsafe output: if an instruction would
   require inventing authority, presenting a draft as final, or breaching
   confidentiality, stop and flag it instead.
3. **The selected skill's** Workflow and Output Format.
4. **Background knowledge.** Treat it as unverified. User-provided documents win.

## The rule

Before you produce any legal work product, route the task to a skill and read
it. If a request even partly matches a skill in `skills/`, use that skill — do
not improvise a legal workflow from memory.

1. **Read `core/` first.** All seven files in `core/` are the operating rules
   every skill inherits. They always apply.
2. **Route the task.** Use `WORKFLOW_ROUTER.md` to map the request ("review
   this NDA," "build a chronology") to a skill. Browse with `SKILLS_INDEX.md`.
3. **Select the narrowest relevant skill.** If several could apply, choose the
   most specific one. Read only that skill's `SKILL.md` and any file in its
   `templates/` folder. Do not load unrelated practice areas.
4. **Follow the skill exactly.** Honor its Required Inputs gate, Workflow, and
   Output Format. If a Required Input is missing, stop and ask — do not guess.
5. **Hand off for review.** Deliver with the skill's Attorney Verification
   Checklist completed.

If no skill fits the task, say so plainly. Do not invent a legal workflow.

## Red flags — stop if you catch yourself doing any of these

| Red flag | What to do instead |
|---|---|
| Answering a legal question from memory, with no skill | Route via `WORKFLOW_ROUTER.md` and use the skill |
| Stating a statute, case, rule, or doctrine as authority | AgentCounsel is jurisdiction-agnostic — flag it `[verify jurisdiction]` |
| Filling a gap with a plausible guess | Insert a placeholder: `[CONFIRM: ...]` / `[VERIFY: ...]` |
| Computing or asserting a deadline | Never compute deadlines — flag `[deadline verification required]` |
| Calling the output an "answer," an "opinion," or final | It is draft legal work product for attorney review |
| Loading several practice areas at once | Use the single narrowest skill |
| Editing a skill while doing a task | Skills are a reference library — deliver work product separately |

## Skill discipline

- **Draft only.** Every skill produces an intermediate deliverable for a
  supervising attorney to review and adopt. AgentCounsel does not produce the
  answer or the opinion, and it is not legal advice.
- **Never invent** legal authority, citations, quotations, facts, or deadlines.
- **Use user-provided documents first.** Background knowledge is unverified.
- **Identify** jurisdiction, governing law, posture, and the relevant date — or
  flag them as unknown.
- **Preserve confidentiality and privilege.** Keep client-sensitive facts out
  of templates.
- **Two checklists, two scopes.** The *Attorney Verification Checklist* is a
  section of each `SKILL.md`; a template's *Open items for attorney
  verification* is part of that template. They are distinct lists — do not
  conflate them.

## Editing the library vs. using it

If your task is to **use** a skill, do not modify it. Only edit files under
`skills/`, `core/`, or `adapters/` when the task is explicitly to improve the
library itself — then follow `CONTRIBUTING.md` and run
`python scripts/validate_repo.py` before opening a pull request.

## Tool names across runtimes

AgentCounsel is read with plain file and shell operations, so it works in any
agent runtime. Where a runtime names those operations differently, see the
`references/` folder next to this file:

- `references/gemini-tools.md` — Gemini CLI
- `references/copilot-tools.md` — GitHub Copilot CLI
- `references/codex-tools.md` — Codex / OpenAI agents
