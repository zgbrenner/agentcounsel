# Practice-Area Registry

This file is the single source of truth for AgentCounsel's practice-area
**taxonomy** — which tier each area belongs to, and how mature it is. It
complements `SKILLS_INDEX.md` (the skill catalog) and the metadata in
`metadata/index.json`. The model behind it, and the plan for expanding it, are
in `reports/practice-area-expansion-plan.md`.

Update this file whenever a practice area or an overlay is added, promoted, or
reclassified.

## The four-tier taxonomy

Every area and group is classified into exactly one tier.

1. **Core legal practice areas** — foundational areas almost every legal team
   touches; broad and document- or matter-centric.
2. **Advanced / specialized legal practice areas** — narrower, self-contained
   bodies of legal doctrine that require specialist expertise.
3. **Industry or regulatory overlays** — sectors, industries, or client types,
   not bodies of law. Implemented under `overlays/` as a profile plus
   reference material that tunes existing skills — never a parallel skill tree.
   See `overlays/README.md`.
4. **Cross-cutting support groups** — not legal practice; groups that support
   the library or the user's process.

## Maturity

- **`stable`** — fully resourced and reviewed; meets the definition of done in
  `reports/practice-area-expansion-plan.md`.
- **`experimental`** — present and passing validation, but not yet fully
  resourced (profile, evals, cold-start, subject-matter-expert review).

The areas and groups marked `stable` below shipped in the v0.1.0 public release
and are the **released baseline**. Their coverage columns show, honestly,
where practice profiles, cold-start interviews, and evals are still being
filled in. New practice areas added under the expansion plan start
`experimental` and are promoted to `stable` only when the definition of done is
met.

## Practice areas — Tiers 1 and 2

| Area | Tier | Maturity | Practice profile | Cold-start interview | Eval coverage |
|---|---|---|---|---|---|
| `legal-research` | 1 — Core | stable | No | No | 0 of 1 skills |
| `litigation` | 1 — Core | stable | Yes | Yes | 3 of 9 skills |
| `contracts` | 1 — Core | stable | Yes | Yes | 2 of 5 skills |
| `corporate` | 1 — Core | stable | Yes | Yes | 0 of 6 skills |
| `employment` | 1 — Core | stable | Yes | No | 0 of 8 skills |
| `ip` | 1 — Core | stable | Yes | No | 0 of 7 skills |
| `privacy` | 1 — Core | stable | Yes | Yes | 1 of 4 skills |
| `product-legal` | 2 — Advanced / specialized | stable | Yes | No | 1 of 4 skills |
| `regulatory` | 2 — Advanced / specialized | stable | Yes | No | 1 of 4 skills |
| `ai-governance` | 2 — Advanced / specialized | stable | Yes | No | 0 of 4 skills |
| `financial-crime` | 2 — Advanced / specialized | stable | No | No | 0 of 2 skills |
| `real-estate` | 2 — Advanced / specialized | experimental | Yes | No | 9 of 9 skills |
| `m-and-a` | 2 — Advanced / specialized | experimental | Yes | No | 10 of 10 skills |
| `family-law` | 2 — Advanced / specialized | experimental | Yes | No | 12 of 12 skills |

## Cross-cutting support groups — Tier 4

These live under `skills/` but are not practice areas. Practice profiles and
cold-start interviews do not apply to them.

| Group | Tier | Maturity | Eval coverage |
|---|---|---|---|
| `legal-methodology` | 4 — Cross-cutting support | stable | 0 of 4 skills |
| `legal-ops` | 4 — Cross-cutting support | stable | 0 of 3 skills |
| `setup` | 4 — Cross-cutting support | stable | 0 of 5 skills |

## Industry / regulatory overlays — Tier 3

Overlays live under `overlays/`, not `skills/`. None have been built yet. The
overlay mechanism and templates are in place; see `overlays/README.md`.

| Overlay | Maturity | Status |
|---|---|---|
| *(none yet)* | — | Candidate overlays are listed in `reports/practice-area-expansion-plan.md`. |

## Coverage gaps in the released baseline

The columns above record real gaps, carried forward from v0.1.0:

- **Practice profiles** are missing for `legal-research` and `financial-crime`.
- **Cold-start interviews** exist for only four areas (`contracts`,
  `corporate`, `litigation`, `privacy`).
- **Evals** cover all 9 `real-estate` skills and all 10 `m-and-a` skills, but only 8 of the 66 v0.1.0 baseline skills.

These gaps do not block use of the released areas, but closing them is part of
bringing each area to the standard the expansion plan sets for new areas.

## How to update this registry

- **Adding a new practice area:** add a row to the Tier 1 / 2 table with
  maturity `experimental`; promote it to `stable` only when the definition of
  done in `reports/practice-area-expansion-plan.md` is met. The area must also
  be added to `docs/SKILL_METADATA_STANDARD.md`, `README.md`, `SKILLS_INDEX.md`,
  `WORKFLOW_ROUTER.md`, and `COMMANDS.md`.
- **Adding an overlay:** add a row to the Tier 3 table and create the overlay
  folder under `overlays/` (see `overlays/README.md`).
- **Reclassifying or promoting an area:** update the Tier or Maturity column
  here, and note the change in `CHANGELOG.md`.
