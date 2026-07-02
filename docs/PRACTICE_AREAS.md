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

The areas and groups marked `stable` below shipped in the v0.2.0 public release
and are the **released baseline**. Their coverage columns show, honestly,
where practice profiles, cold-start interviews, and evals are still being
filled in. New practice areas added under the expansion plan start
`experimental` and are promoted to `stable` only when the definition of done is
met.

## Practice areas — Tiers 1 and 2

| Area | Tier | Maturity | Practice profile | Cold-start interview | Eval coverage |
|---|---|---|---|---|---|
| `legal-research` | 1 — Core | stable | No | No | 5 of 5 skills |
| `litigation` | 1 — Core | stable | Yes | Yes | 9 of 9 skills |
| `contracts` | 1 — Core | stable | Yes | Yes | 5 of 5 skills |
| `corporate` | 1 — Core | stable | Yes | Yes | 6 of 6 skills |
| `employment` | 1 — Core | stable | Yes | Yes | 8 of 8 skills |
| `ip` | 1 — Core | stable | Yes | Yes | 7 of 7 skills |
| `privacy` | 1 — Core | stable | Yes | Yes | 7 of 7 skills |
| `product-legal` | 2 — Advanced / specialized | stable | Yes | Yes | 4 of 4 skills |
| `regulatory` | 2 — Advanced / specialized | stable | Yes | Yes | 4 of 4 skills |
| `ai-governance` | 2 — Advanced / specialized | stable | Yes | Yes | 4 of 4 skills |
| `financial-crime` | 2 — Advanced / specialized | stable | Yes | Yes | 5 of 5 skills |
| `real-estate` | 2 — Advanced / specialized | experimental | Yes | Yes | 9 of 9 skills |
| `m-and-a` | 2 — Advanced / specialized | experimental | Yes | Yes | 10 of 10 skills |
| `family-law` | 2 — Advanced / specialized | experimental | Yes | Yes | 12 of 12 skills |
| `antitrust-competition` | 2 — Advanced / specialized | experimental | Yes | Yes | 10 of 10 skills |
| `securities-capital-markets` | 2 — Advanced / specialized | experimental | Yes | Yes | 12 of 12 skills |
| `tax` | 2 — Advanced / specialized | experimental | Yes | Yes | 10 of 10 skills |
| `bankruptcy-restructuring` | 2 — Advanced / specialized | experimental | Yes | Yes | 12 of 12 skills |
| `insurance` | 2 — Advanced / specialized | experimental | Yes | Yes | 12 of 12 skills |
| `trusts-estates` | 2 — Advanced / specialized | experimental | Yes | Yes | 12 of 12 skills |

## Cross-cutting support groups — Tier 4

These live under `skills/` but are not practice areas. Practice profiles and
cold-start interviews do not apply to them.

| Group | Tier | Maturity | Eval coverage |
|---|---|---|---|
| `legal-methodology` | 4 — Cross-cutting support | stable | 11 of 11 skills |
| `legal-ops` | 4 — Cross-cutting support | stable | 4 of 4 skills |
| `setup` | 4 — Cross-cutting support | stable | 20 of 20 skills |

## Industry / regulatory overlays — Tier 3

Overlays live under `overlays/`, not `skills/`. The overlay mechanism and
templates are in place; see `overlays/README.md`.

| Overlay | Maturity | Status |
|---|---|---|
| `healthcare` | `experimental` | First overlay built under the overlays/ scaffold. Tunes privacy, contracts, employment, regulatory, and AI-governance skills for HIPAA, HITECH, state-law overlays (CMIA, HB 300, MHMDA, SHIELD), 42 CFR Part 2, GINA, and reproductive-health frameworks. `[ORGANIZATION TO FILL]` placeholders in `profile.md` until configured for a specific organization. See `overlays/healthcare/OVERLAY.md`. |
| `fintech-payments` | `experimental` | Tunes contracts, privacy, regulatory, financial-crime, and product-legal skills for a payments / fintech context — money-transmission/MSB, card-network rules, BSA/AML, sanctions, consumer-financial-protection, and digital-asset regimes, each described generically and flagged for jurisdiction verification. `[ORGANIZATION TO FILL]` placeholders in `profile.md` until configured. See `overlays/fintech-payments/OVERLAY.md`. |
| `education-law` | `experimental` | Tunes employment, privacy, regulatory, contracts, and product-legal skills for schools, universities, and ed-tech — student-education-records and children's-online-privacy regimes, minors as data subjects, Title IX-style processes, accessibility, state student-data-privacy statutes, and mandatory-reporting triggers routed to counsel immediately, each described generically and flagged for verification. `[ORGANIZATION TO FILL]` placeholders in `profile.md` until configured. See `overlays/education-law/OVERLAY.md`. |
| `environmental-esg` | `experimental` | Tunes regulatory, corporate, securities-capital-markets, product-legal, contracts, m-and-a, and real-estate skills for environmental and ESG work — permitting/compliance regimes, fast-moving climate/ESG disclosure frameworks flagged `[Verify current law]`, greenwashing/marketing-claims risk, supply-chain diligence regimes, and transactional environmental diligence, with release/contamination and agency-contact escalation gates. `[ORGANIZATION TO FILL]` placeholders in `profile.md` until configured. See `overlays/environmental-esg/OVERLAY.md`. |
| *(other candidates)* | — | Listed in `reports/practice-area-expansion-plan.md` (remaining: entertainment-media-sports). |

## Coverage gaps in the released baseline

The columns above record the remaining gaps:

- **Practice profiles** are missing for `legal-research`.
- **Cold-start interviews** are missing for `legal-research`; each of the other
  19 practice areas has one under `skills/setup/`.
- **Evals** now cover every skill — all 198 skills have a skill eval file
  (`reports/eval-coverage.md` reports 0 skills without coverage); the
  pre-release baseline of 8 covered skills has been fully closed.

The remaining profile and cold-start gaps do not block use of the released
areas, but closing them is part of bringing each area to the standard the
expansion plan sets for new areas.

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
