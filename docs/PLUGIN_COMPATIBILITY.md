# Plugin Compatibility

AgentCounsel is a Markdown-native legal skills library. Platform support is
file-based: generated packs and thin adapter files help each AI environment
find the canonical `skills/`, `core/`, `practice-profiles/`, `matter-packs/`,
and `matter-workspaces/` content. AgentCounsel does not ship a runtime plugin
server and does not position any model as a lawyer.

Every platform path preserves the same rule: outputs are draft legal work
product for review by a licensed attorney, not legal advice.

## Supported Surfaces

| Surface | How to use AgentCounsel | Generated pack shape |
|---|---|---|
| ChatGPT Projects | Create one Project per practice area, upload the generated Markdown pack, and paste the generated Project instructions. | `dist/chatgpt/<area>.md` |
| Claude Projects / plugin-style workflows | Upload the files from the generated ZIP to Project knowledge or a plugin-style workspace and follow `CLAUDE.md`. | `dist/claude/<area>.zip` |
| Cursor | Use the repo-agent generated `.cursorrules` file with a checkout that contains `skills/` and `core/`. | `dist/repo-agents/.cursorrules` |
| Codex / repo agents | Put generated `AGENTS.md` at the repository root, or use `adapters/codex/AGENTS.md` in this repo. | `dist/repo-agents/AGENTS.md` |
| Gemini | Add the generated notebook source files from the Gemini ZIP as sources and follow `notebook-instructions.md`. | `dist/gemini/<area>.zip` |
| Generic Markdown | Open a single `SKILL.md` and the relevant `core/` rules directly. | `adapters/generic-md/` |

## How Packs Are Generated

Run:

```powershell
py scripts\build_platform_packs.py
```

The generator reads canonical source files and writes generated artifacts to
`dist/`:

- ChatGPT practice-area Markdown packs.
- Claude practice-area ZIP packs.
- Gemini practice-area ZIP packs.
- Repo-agent files for Codex, Cursor, and Claude Code.
- `dist/packs.json`, `dist/index.json`, and `dist/manifest.json`.

The source-controlled pack registry is `metadata/packs.json`. Check it without
rewriting files:

```powershell
py scripts\build_platform_packs.py --check
```

## Pack Manifests

Each manifest entry in `metadata/packs.json` includes:

- `pack_id`
- `platform`
- `practice_area` or use case
- generated output path
- included skills
- included core rules
- included templates and references
- included quality checks
- included matter packs and workspace templates when applicable
- setup instructions
- safety disclaimer
- attorney-review requirements
- version and date

The manifest is intentionally descriptive. It does not execute code, call
APIs, or create a plugin runtime.

## Metadata And Routing

`metadata/index.json` now contains normalized skill fields for routing, pack
generation, site display, eval coverage, and platform compatibility. The
canonical authoring surface remains the YAML frontmatter in each `SKILL.md`;
the normalized fields are derived by `scripts/build_skill_index.py`.

`metadata/router.json` is generated from the same source. It helps agents
decide between:

- one-off skill
- practice-area pack
- matter pack
- matter workspace
- quality check
- review panel pattern when one is added

## Limitations

- AgentCounsel does not provide legal advice.
- AgentCounsel does not create an attorney-client relationship.
- AgentCounsel does not compute or verify legal deadlines without attorney
  review.
- Connectors are documented integration points, not runtime services.
- Cursor, Browserbase, and several public skill directories have unclear
  licensing in the checked repositories; their public structure may inform
  compatibility thinking, but their code, text, schemas, and examples must not
  be copied unless permission or a compatible license is confirmed.

## Contributor Checklist

When adding or changing a skill:

1. Update the skill frontmatter using `docs/SKILL_METADATA_STANDARD.md`.
2. Run `py scripts\build_skill_index.py`.
3. If pack contents changed, run `py scripts\build_platform_packs.py`.
4. Run `py scripts\validate_repo.py`.
5. Add or update evals under `evals/skills/` when the skill behavior changes.
6. Do not copy third-party code or content unless
   `docs/THIRD_PARTY_ATTRIBUTION_POLICY.md` permits it and attribution is
   recorded.
