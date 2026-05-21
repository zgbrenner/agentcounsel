# GitHub Copilot CLI — tool reference

How to do AgentCounsel's file and shell operations from the GitHub Copilot CLI
runtime. AgentCounsel is a Markdown library: working in it means **reading**
skill files and, when editing the library, running the validator. Nothing here
changes the operating model in `using-agentcounsel.md`.

Copilot CLI names its tools differently from other runtimes; map the operations
AgentCounsel needs as follows.

## Core operations

| Operation | Copilot CLI |
|---|---|
| Read a skill, core rule, or template | the file-view tool (`view`) |
| Browse the library / list a practice area | the directory-list tool, or shell `ls` |
| Find the skill for a task | the search tool, or shell `grep` over `WORKFLOW_ROUTER.md` and `SKILLS_INDEX.md` |
| Run repository validation | the shell tool — `python scripts/validate_repo.py` |
| Edit a skill (library work only) | the file-create / file-edit tools (`create`, `str-replace`) |

## Routing a task

1. View `WORKFLOW_ROUTER.md` to map the request to a skill.
2. View the six `core/` files.
3. View the chosen `skills/.../SKILL.md` and any file in its `templates/`
   folder.

## Shell sessions

Copilot CLI may run shell commands in asynchronous sessions. AgentCounsel needs
only short, synchronous commands — `python scripts/validate_repo.py` and
`python scripts/sync_plugin_skills.py`. Wait for each command to finish and
read its output before continuing.

## Editing the library

After any change under `skills/`, `core/`, or `adapters/`, run
`python scripts/validate_repo.py`. If you changed a curated skill, regenerate
the Claude Code plugin bundle with `python scripts/sync_plugin_skills.py`.
Follow `CONTRIBUTING.md` and `VALIDATION.md`.
