# Local Platform Path

This document describes, at the architecture level only, the future path from the
current Markdown-native library toward a local, source-grounded matter platform.
**Nothing here is built yet.** It exists to keep design decisions coherent so the
library stays a clean foundation for that path without ever requiring it.

> Scope guardrail: AgentCounsel today is a Markdown-native library that produces
> draft legal work product for attorney review. It has no auth, no database, no
> payments, no hosted backend, and no chat UI — and this document does not propose
> adding any of those to the library. It describes an *optional* future
> application layer that could sit on top of the unchanged Markdown library.

## Design principles (today, and preserved on the path)

- **Markdown-native source of truth.** Skills, matter workspaces, playbooks, and
  review panels are plain Markdown. Any future app reads and writes these files;
  it never replaces them with an opaque store.
- **Local-first, no lock-in.** A matter's files live on the user's machine or in
  the user's own storage. No vendor account is required to read or edit them.
- **Attorney-supervised draft work product.** Every output remains a draft for
  attorney review. No future feature converts an output into legal advice or a
  final decision.
- **Deterministic, no-network tooling.** The scripts (`init_matter_workspace.py`,
  validators, builders) are Python standard library only and run offline.

## Future path (architecture-level, not committed)

1. **Local app.** A desktop application that opens a `matters/` directory,
   renders matter workspaces, and runs the existing scripts locally. It would be
   a viewer/editor over the Markdown files — not a new data model.

2. **Self-hosted web app.** The same viewer served from the user's own
   infrastructure, reading the same Markdown files. Self-hosted by design; no
   AgentCounsel-operated backend.

3. **Matter-scoped chat.** An optional assistant scoped to a single matter
   workspace, with the workspace's `facts.md`, `source_log.md`, and `documents/`
   as its grounding context. It would route through `WORKFLOW_ROUTER.md` to the
   right skill, playbook, or review panel, and write outputs back into the
   workspace's `outputs/` and `quality_checks/` folders.

4. **Source-grounded workspace.** Retrieval limited to the matter's own provided
   documents and the source log — so the assistant cites only what is in the
   matter, with every authority still flagged for attorney verification. This
   directly extends the existing source/citation classification vocabulary.

5. **Local model compatibility.** The matter-scoped chat would target a
   pluggable, OpenAI-compatible local inference endpoint — for example LocalAI or
   Ollama — so a matter can be worked entirely on-device with no third-party
   model call. Cloud models remain an opt-in alternative, never a requirement.

6. **No vendor lock-in.** Because the source of truth is Markdown and the
   inference endpoint is pluggable, a user can switch apps, models, or hosting at
   any time and lose nothing. Exporting a matter is just copying its directory.

## What this means for library contributions today

- Keep matter workspaces, playbooks, and review panels strictly Markdown-native.
- Keep the source/citation classification vocabulary stable — it is the contract
  a future source-grounded workspace would rely on.
- Keep scripts standard-library and offline.
- Do not add auth, a database, payments, a hosted backend, or a chat UI to the
  library. Those belong to the optional application layer, if and when it is
  built.

See `docs/MATTER_WORKSPACES.md`, `docs/PLAYBOOKS.md`, `docs/REVIEW_PANELS.md`, and
`docs/SAFETY_MODEL.md` for the pieces this path builds on.
