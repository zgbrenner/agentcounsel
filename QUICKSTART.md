# Quick Start

This guide takes you from zero to your first AgentCounsel skill run in about five minutes. It assumes you already have access to an AI assistant (ChatGPT, Claude, Gemini, or a coding agent).

> Everything AgentCounsel produces is **draft legal work product for attorney review** — not legal advice. A licensed attorney must review the output before it is relied upon.

## The idea in one minute

A **skill** is a single Markdown file (`SKILL.md`) that describes a legal workflow: what it is for, what inputs it needs, the steps to follow, the structure of the output, and what an attorney must verify. You give the skill file to an AI assistant as context, provide your inputs, and the assistant produces a structured draft. You — or a supervising attorney — then review it.

Nothing is installed. A skill is just a file an AI model reads.

## Step 1 — Pick the right skill

Open [`WORKFLOW_ROUTER.md`](WORKFLOW_ROUTER.md) and find the row that matches your task ("review this NDA", "build a timeline from these documents", "run a privacy impact assessment"). It points you to a `SKILL.md`.

If you would rather browse, [`SKILLS_INDEX.md`](SKILLS_INDEX.md) lists every skill by practice area. If you prefer short command names, [`COMMANDS.md`](COMMANDS.md) maps shorthands like `/contracts:nda` to skills.

## Step 2 — Read the skill

Open the `SKILL.md`. Check three things before you start:

- **Use When / Do Not Use When** — confirm this is the right skill for your task.
- **Required Inputs** — gather these now. Most skills need the actual document, your client's role, and the business context.
- **Legal Safety Rules** — what the skill will and will not do.

## Step 3 — Run it with your AI assistant

Give the assistant the operating rules, the skill, and your inputs. Pick the workflow for your platform:

### Generic — any AI assistant

1. Paste the contents of the `core/` files (or at least [`core/source-and-citation-discipline.md`](core/source-and-citation-discipline.md)).
2. Paste the contents of the chosen `SKILL.md`.
3. Add your inputs and say: *"Follow this skill. Here are the inputs: …"*

### ChatGPT

Create a **Project**, add the skill files as project files (or a consolidated practice-area pack from `dist/chatgpt/` — see Step 6), and start a chat in that Project with your inputs.

### Claude

Use the Claude Code plugin-style bundle in [`adapters/claude-code-plugin/`](adapters/claude-code-plugin/), or keep the repository in a folder Claude can read and ask it to route to the right skill. For Claude Projects, build a ZIP pack with `python scripts/build_platform_packs.py` (`dist/claude/`).

### Gemini

Install the repository as a Gemini CLI extension — `gemini-extension.json` and `GEMINI.md` load the operating model automatically. See [`adapters/gemini/`](adapters/gemini/).

### Codex and other repo agents

Point the agent at the repository through [`AGENTS.md`](AGENTS.md); it will select the narrowest relevant skill. See [`adapters/codex/`](adapters/codex/).

### Cursor

Add the library to your project and reference it from a `.cursorrules` file or `AGENTS.md`. `python scripts/build_platform_packs.py` generates a ready-made `.cursorrules` in `dist/repo-agents/`.

## Step 4 — Review the output against the checklist

Every skill ends with an **Attorney Verification Checklist**. Work through it. The draft will contain visible placeholders — `[CONFIRM: ...]`, `[verify jurisdiction]`, `[ATTORNEY TO CONFIRM: ...]` — wherever the skill could not be certain. Each one is a task for a person, not a defect to ignore.

**Do not rely on, send, or file the output until a qualified, licensed attorney has reviewed it.**

## Step 5 — See what "good" looks like

The [`examples/`](examples/) directory has complete sample outputs (with fictional facts) for a contract review, a litigation chronology, a DPA review, a product launch review, and a red-team verification. Read one before your first run so you know what to expect.

## Step 6 — (Optional) Build a platform pack

To use a whole practice area at once, generate ready-to-install packs:

```
python scripts/build_platform_packs.py
```

This writes per-platform packs to `dist/` (ChatGPT, Claude, Gemini, and repo agents). It uses only the Python standard library — nothing to install.

## A worked example: reviewing an NDA

1. **Route.** `WORKFLOW_ROUTER.md` → "Review this NDA" → `skills/contracts/nda-review/SKILL.md`.
2. **Read.** Required Inputs: the NDA text, your client's role (disclosing, receiving, or mutual), and the business context.
3. **Run.** Paste `core/` + the skill + the NDA text into your assistant. State the client's role.
4. **Get back.** A triage rating, a key-terms table, a risk table, prioritized redline points, and an Attorney Verification Checklist.
5. **Review.** Resolve every `[CONFIRM: ...]` placeholder; have an attorney confirm the triage rating and redline priorities before negotiating or signing.

## Where to go next

- [`README.md`](README.md) — what AgentCounsel is, who it is for, and how it is organized.
- [`docs/SAFETY_MODEL.md`](docs/SAFETY_MODEL.md) — the safety model and how to use AgentCounsel with confidential material.
- [`docs/FAQ.md`](docs/FAQ.md) — common questions.
- [`core/`](core/) — the operating rules every skill inherits. Read these once; they apply everywhere.
