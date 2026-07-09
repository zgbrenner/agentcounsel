# 0001. The Claude Code plugin bundle is generated, never hand-edited

## Status

Accepted.

## Context

`adapters/claude-code-plugin/skills/` ships a curated starter set of
AgentCounsel skills for the Claude Code plugin. `/skills` is the single
canonical source of truth for every skill in the library (see `AGENTS.md` and
`CONTRIBUTING.md`). If the plugin bundle were maintained by hand, a fix
applied to a canonical skill under `/skills` could silently fail to reach the
plugin copy, or a plugin-only edit could quietly diverge from canonical
without anyone noticing — exactly the kind of drift that is hard to catch by
reading either copy in isolation.

## Decision

The plugin bundle is a **generated artifact**. `scripts/sync_plugin_skills.py`
copies a curated list of skills (and their templates) from canonical
`/skills` into `adapters/claude-code-plugin/skills/`. Contributors edit only
the canonical skill and then re-run the sync script; they never hand-edit a
file under the plugin bundle directory. The one exception is `legal-core`, a
hand-maintained summary of the `/core` rules that has no canonical `/skills`
equivalent to generate from.

## Consequences

- `scripts/validate_repo.py` fails CI if the plugin bundle drifts from
  canonical, so drift cannot merge silently.
- Anyone changing a curated skill must remember to run
  `python scripts/sync_plugin_skills.py` before committing — an extra step,
  documented in `PLUGIN_SYNC.md` and `CONTRIBUTING.md`.
- `legal-core` requires a manual review whenever `/core` changes, since the
  sync script cannot detect that it has fallen behind.
- Anyone auditing the plugin bundle for correctness should treat
  `adapters/claude-code-plugin/skills/` as a build output, not a place to
  make a substantive fix.

Source: `PLUGIN_SYNC.md`.
