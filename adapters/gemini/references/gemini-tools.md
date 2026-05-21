# Gemini CLI — tool reference

How to do AgentCounsel's file and shell operations from the Gemini CLI runtime.
AgentCounsel is a Markdown library: working in it means **reading** skill files
and, when editing the library, running the validator. Nothing here changes the
operating model in `GEMINI.md` and `using-agentcounsel.md`.

## Core operations

| Operation | Gemini CLI tool |
|---|---|
| Read a skill, core rule, or template | `read_file`, or `read_many_files` for a set |
| Browse the library / list a practice area | `list_directory`, `glob` |
| Find the skill for a task | `search_file_content` over `WORKFLOW_ROUTER.md` and `SKILLS_INDEX.md` |
| Run repository validation | `run_shell_command` — `python scripts/validate_repo.py` |
| Edit a skill (library work only) | `write_file`, `replace` |

## Routing a task

1. `read_file` on `WORKFLOW_ROUTER.md` to map the request to a skill.
2. `read_file` (or `read_many_files`) on the six `core/` files.
3. `read_file` on the chosen `skills/.../SKILL.md` and any file in its
   `templates/` folder.

## Subagents

If the runtime offers a general-purpose subagent, use it only to **locate** a
skill — search and read — not to produce legal work product unsupervised. The
operating model in `using-agentcounsel.md` applies to every subagent: draft
legal work product for attorney review only, never invent authority.

## Editing the library

After any change under `skills/`, `core/`, or `adapters/`, run
`python scripts/validate_repo.py`. If you changed a curated skill, regenerate
the Claude Code plugin bundle with `python scripts/sync_plugin_skills.py`. See
`CONTRIBUTING.md` and `VALIDATION.md`.
