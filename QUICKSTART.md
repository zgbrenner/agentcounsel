# Quick Start

This guide takes you from zero to your first AgentCounsel skill run in about five minutes. It assumes you already have access to an AI assistant (ChatGPT, Claude, Gemini, or a coding agent).

> Everything AgentCounsel produces is **draft legal work product for attorney review** — not legal advice. A licensed attorney must review the output before it is relied upon.

## The idea in one minute

A **skill** is a single Markdown file (`SKILL.md`) that describes a legal workflow: what it is for, what inputs it needs, the steps to follow, the structure of the output, and what an attorney must verify. You give the skill file to an AI assistant as context, provide your inputs, and the assistant produces a structured draft. You — or a supervising attorney — then review it.

A **pack** consolidates every skill in a practice area — plus the global safety rules and slash commands — into one file you can upload to your AI tool's project or workspace. Installing a pack is the fastest way to get started; using individual skill files gives you more control.

## Step 1 — Install a practice-area pack (recommended)

Open the [AgentCounsel packs page](https://zgbrenner.github.io/agentcounsel/packs/) and pick the practice area you work in (Contracts, Litigation, Employment, Privacy, M&A, etc.). Each row has direct downloads for ChatGPT (`.md`), Claude (`.zip`), and Gemini (`.zip`). Repo-agent users (Cursor, Codex, Claude Code) use the `AGENTS.md` / `CLAUDE.md` files in the repo-agents section instead.

Upload the file to a new project in your AI tool. In the project's custom instructions, paste:

> *"Follow the AgentCounsel pack in the project files. Apply the global safety rules to every task. Use the practice profile and the skill that matches the request. Produce draft legal work product for attorney review — not legal advice."*

The pack is regenerated on every push to `main`, so you're always installing the current version.

## Step 2 — Pick the right skill (within the pack)

A pack contains every skill in the practice area. You name a task in plain language; the AI routes to the matching skill using the `COMMANDS.md` content that ships inside the pack.

Example: in a Contracts pack, you say *"Review this NDA — the client is the receiving party, this is for a stand-alone commercial NDA."* The AI routes to the `nda-review` skill and follows its workflow. If you prefer the short form, the same pack lets you say `/contracts:nda` directly.

If you want to browse before you choose, [`SKILLS_INDEX.md`](SKILLS_INDEX.md) lists every skill by practice area, [`WORKFLOW_ROUTER.md`](WORKFLOW_ROUTER.md) maps tasks to skills, and [`COMMANDS.md`](COMMANDS.md) lists the slash commands.

## Step 3 — Provide the Required Inputs

Every skill declares its **Required Inputs** — usually the document, your client's role, the business context, the jurisdiction. The AI will ask for them; provide them in the chat. If you're missing an input, say so — the skill will tell you what's missing and stop rather than guess.

## Step 4 — Review the output against the Attorney Verification Checklist

Every skill ends with an **Attorney Verification Checklist**. Work through it. The draft will contain visible placeholders — `[CONFIRM: ...]`, `[verify jurisdiction]`, `[ATTORNEY TO CONFIRM: ...]` — wherever the skill could not be certain. Each one is a task for a person, not a defect to ignore.

**Do not rely on, send, or file the output until a qualified, licensed attorney has reviewed it.**

## Step 5 — See what "good" looks like

The [`examples/`](examples/) directory has complete sample outputs (with fictional facts) for a contract review, a litigation chronology, a DPA review, a product launch review, and a red-team verification. Read one before your first run so you know what to expect.

## Alternative: use individual skill files

If you prefer to work skill-by-skill rather than installing a whole pack:

1. Route the task with [`WORKFLOW_ROUTER.md`](WORKFLOW_ROUTER.md) or browse [`SKILLS_INDEX.md`](SKILLS_INDEX.md).
2. Open the chosen `SKILL.md`. Check its Use When / Required Inputs / Legal Safety Rules sections.
3. Paste the contents of [`core/`](core/) (or at minimum [`core/source-and-citation-discipline.md`](core/source-and-citation-discipline.md)) plus the `SKILL.md` into your AI assistant, then provide your inputs.
4. Each platform's deeper setup guide lives in [`adapters/`](adapters/) — Claude Code plugin, Claude Cowork, Gemini CLI extension, Codex, generic Markdown.

## A worked example: reviewing an NDA

1. **Route.** `WORKFLOW_ROUTER.md` → "Review this NDA" → `skills/contracts/nda-review/SKILL.md`. (In a Contracts pack, just say "review this NDA" in chat.)
2. **Read.** Required Inputs: the NDA text, your client's role (disclosing, receiving, or mutual), and the business context.
3. **Run.** With a pack: state the task and provide the NDA + role. With files: paste `core/` + the skill + the NDA text into your assistant.
4. **Get back.** A triage rating, a key-terms table, a risk table, prioritized redline points, and an Attorney Verification Checklist.
5. **Review.** Resolve every `[CONFIRM: ...]` placeholder; have an attorney confirm the triage rating and redline priorities before negotiating or signing.

## Where to go next

- [`README.md`](README.md) — what AgentCounsel is, who it is for, and how it is organized.
- [`docs/SAFETY_MODEL.md`](docs/SAFETY_MODEL.md) — the safety model and how to use AgentCounsel with confidential material.
- [`docs/FAQ.md`](docs/FAQ.md) — common questions.
- [`core/`](core/) — the operating rules every skill inherits. Read these once; they apply everywhere.
