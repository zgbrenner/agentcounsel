# 0003. AgentCounsel ships no code inside a skill — Markdown only, no runtime

## Status

Accepted.

## Context

AgentCounsel produces draft legal work product for attorney review, never a
final answer or legal advice (`AGENTS.md`). Its safety model depends on every
step of a skill's workflow being visible, human-readable, and auditable by a
supervising attorney before the output is relied upon. A script embedded in a
skill would run outside that model: it could fetch data, transform text, or
make a decision the attorney cannot read in plain language before the
deliverable reaches them, reintroducing exactly the "hidden behavior" risk
`AGENTS.md`'s non-negotiable rules warn against. A Markdown-only library is
also trivially portable across agent harnesses and platforms, with nothing
to install, compile, or trust beyond reading the text.

## Decision

A skill is a `SKILL.md` file plus optional Markdown templates and reference
material — nothing else. No scripts, no build steps, no runtime ships inside
`skills/`, `core/`, or `connectors/`. `scripts/` exists, but it is
maintainer-facing repository tooling (validation, index generation, plugin
sync) that runs against the library from the outside; it is never invoked by
a skill's own workflow, and connectors are documented integration points, not
code that calls out on the library's behalf (see `connectors/README.md`).

## Consequences

- Every workflow step a skill performs is something a human can read and
  verify by reading the `SKILL.md` — there is no step whose actual behavior
  is hidden inside a script.
- Adding a capability that seems to need code (e.g., an automated citation
  lookup) means writing it as a documented connector or a maintainer-facing
  script under `scripts/`, never as code shipped inside a skill folder — see
  `CONTRIBUTING.md`'s "no unnecessary scripts" requirement.
- The library has no dependency, package-manager, or execution-environment
  requirement for an end user beyond a Markdown-capable agent or reader.
- Any future proposal to run code as part of a skill's own workflow is a
  safety-model change, not a routine contribution, and should be raised as an
  issue before being attempted.

Source: `AGENTS.md` ("no runtime" and the safety model), `CONTRIBUTING.md`.
