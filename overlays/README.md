# Overlays

An **overlay** tunes AgentCounsel's existing skills for a particular industry,
sector, or client type — healthcare, fintech, government contracting, and so
on. Overlays are **Tier 3** of the practice-area taxonomy (see
`docs/PRACTICE_AREAS.md` and `reports/practice-area-expansion-plan.md`).

Overlays are not legal advice and not legal work product. Like practice
profiles, they are internal configuration material that a supervising attorney
reviews before use.

## Why overlays exist

A sector is not a body of law. A healthcare company's legal work *is*
contracts work, privacy work, employment work, and regulatory work — coloured
by the sector. If every sector became its own practice area, the library would
fill up with near-duplicate skills: a healthcare "contract review," a fintech
"contract review," and so on.

An overlay avoids that. It carries the **sector-specific context** — the gates,
the escalation triggers, the terminology, the standard positions — and lets the
existing skills do the work unchanged. **An overlay never contains skills.**

## What an overlay contains

Each overlay is a folder under `overlays/`:

```
overlays/<sector>/
  OVERLAY.md      What the sector is, which skills it modifies, its gates,
                  and what it deliberately does not change.
  profile.md      A sector configuration profile, in the practice-profile
                  style — jurisdictions, gates, standard positions,
                  prohibited assumptions.
  references/     Optional. Sector red-flag catalogues and checklists,
                  modelled on skills/contracts/references/.
```

The one exception to "no skills": if a sector genuinely needs a workflow that
no existing skill covers, that single skill is added to the most relevant
existing practice area under `skills/` — never to an overlay folder.

## How to use an overlay

1. Route the task to a skill as normal (`WORKFLOW_ROUTER.md`).
2. Load, in order: the `core/` rules, the relevant practice profile, the
   skill — and then the overlay's `OVERLAY.md` and `profile.md`.
3. The overlay sharpens the skill for the sector. It adds gates and context;
   it never replaces the skill or the `core/` rules.

The `core/` rules bound everything. A profile or overlay configures; it cannot
override a `core/` operating rule.

## How to add an overlay

1. Confirm the candidate is genuinely an overlay, not a practice area, using
   the decision framework in `reports/practice-area-expansion-plan.md`.
2. Copy `overlays/_template/` to `overlays/<sector>/` and fill in `OVERLAY.md`
   and `profile.md`. Replace every `[bracketed placeholder]`.
3. Add the overlay to the table in `docs/PRACTICE_AREAS.md`.
4. Run `python scripts/validate_repo.py` and resolve any errors.

`scripts/validate_repo.py` checks that every overlay folder contains an
`OVERLAY.md`. Folders whose name begins with `_` (such as `_template`) are
scaffolding and are skipped.

## Status

The overlay mechanism is in place; **no sector overlays have been built yet.**
The expansion plan identifies these candidates:
`healthcare-life-sciences`, `fintech-payments`, an `environmental & ESG`
overlay, `entertainment-media-sports`, and `education-law`. Each will be added
as a folder here when its wave begins.
