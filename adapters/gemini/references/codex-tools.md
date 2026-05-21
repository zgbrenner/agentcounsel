# Codex / OpenAI agents — tool reference

How to do AgentCounsel's file and shell operations from a Codex or OpenAI-agent
runtime. AgentCounsel is a Markdown library: working in it means **reading**
skill files and, when editing the library, running the validator. Nothing here
changes the operating model in `using-agentcounsel.md`.

The repository also ships a dedicated repo-agent adapter at `adapters/codex/`
(`AGENTS.md`). Read it — it is the canonical Codex instruction file, and it
points to the same canonical `skills/` and `core/` library.

## Core operations

| Operation | Codex runtime |
|---|---|
| Read a skill, core rule, or template | the file-read tool, or shell `cat` |
| Browse the library / list a practice area | shell `ls` |
| Find the skill for a task | shell `grep` over `WORKFLOW_ROUTER.md` and `SKILLS_INDEX.md` |
| Run repository validation | the shell tool — `python scripts/validate_repo.py` |
| Edit a skill (library work only) | the apply-patch / file-write tool |
| Track multi-step work | the plan tool (`update_plan`) |

## Routing a task

1. Read `adapters/codex/AGENTS.md` — the repo-agent instructions.
2. Read `WORKFLOW_ROUTER.md` to map the request to a skill.
3. Read the six `core/` files.
4. Read the chosen `skills/.../SKILL.md` and any file in its `templates/`
   folder.

## Subagents

If the runtime supports spawning subagents (for example, configured under
`~/.codex/config.toml`), a subagent may **locate and read** a skill, but the
operating model in `using-agentcounsel.md` applies to every subagent: draft
legal work product for attorney review only, never invent authority, preserve
confidentiality.

## Editing the library

After any change under `skills/`, `core/`, or `adapters/`, run
`python scripts/validate_repo.py`. If you changed a curated skill, regenerate
the Claude Code plugin bundle with `python scripts/sync_plugin_skills.py`.
Follow `CONTRIBUTING.md` and `VALIDATION.md`.
