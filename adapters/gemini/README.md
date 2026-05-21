# AgentCounsel — Gemini CLI Adapter

This adapter packages AgentCounsel as a **Gemini CLI extension**, so a Gemini
agent loads the library's operating model automatically at the start of every
session.

## What is here

- `gemini-extension.json` (repo root) — the Gemini CLI extension manifest.
- `GEMINI.md` (repo root) — the extension context file the manifest names. It
  imports the two files below.
- `using-agentcounsel.md` — the operating guide: how to find and use a skill
  before producing any legal work product.
- `references/` — tool-name maps for the agent runtimes AgentCounsel is used
  from: `gemini-tools.md`, `copilot-tools.md`, and `codex-tools.md`.

The manifest and context file live at the repository root because Gemini CLI
expects an extension's `gemini-extension.json` and its `contextFileName` there.
Everything else for this adapter lives in this folder.

## How it works

Gemini CLI reads `gemini-extension.json` at the repository root and loads the
`contextFileName` it names — `GEMINI.md`. `GEMINI.md` uses Gemini's `@`-import
directive to pull in `using-agentcounsel.md` and `references/gemini-tools.md`,
so every session starts with AgentCounsel's operating model and the matching
tool reference already in context.

## Install

From a local clone of this repository, link it as an extension:

```
gemini extensions link .
```

Or install it from the repository URL:

```
gemini extensions install <repository-url>
```

Then start `gemini` in any directory; the AgentCounsel operating model loads
automatically.

## Keep it canonical

Like every AgentCounsel adapter, this one is intentionally **thin**. It
contains no copies of skills. The canonical library is the repository's
`skills/` and `core/` directories — always route to and read from there.

## Reminder

AgentCounsel produces draft legal work product for attorney review. It is not
legal advice. A qualified, licensed legal professional must review and adopt
every output.
