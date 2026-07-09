# Canonical Matter Workspace Template

This directory is the **canonical multi-file matter workspace template**. It is a
Markdown-native scaffold for organizing one legal matter across multiple skills,
documents, deadlines, and review passes — with no database, backend, login, or
vendor dependency.

> **Blank template — contains no client facts.** Once you copy this directory and
> populate it with matter-specific information, the populated copy becomes **draft
> legal work product for attorney review**. It may be protected by the
> attorney-client privilege and/or the attorney work-product doctrine. Label and
> access-limit the populated copy accordingly. This is not legal advice.

## When to use the multi-file template vs. a single-file workspace

- **Single-file workspace** (`matter-workspaces/*-matter.md`) — quick to open and
  read; best for a focused matter handled in one or two sittings.
- **This multi-file template** — best for a **document-heavy, multi-step,
  source/citation-intensive, or long-running** matter where facts, sources,
  assumptions, tasks, and outputs each deserve their own tracked file.

Both are draft work product for attorney review. Pick the format that fits the
matter; do not maintain both for the same matter.

## Structure

```
<matter-slug>/
├── matter_profile.md      Matter header: parties, jurisdiction, deadlines, posture
├── facts.md               Known facts and disputed facts, each labeled by source
├── open_questions.md      Unresolved questions blocking or shaping the analysis
├── documents/             Source documents and a documents index
│   └── README.md
├── source_log.md          Every source consulted, with quality-layer classification
├── citation_map.md        Each drafted statement mapped to its supporting source
├── unsupported_claims.md  Statements with no adequate source — must be resolved
├── assumptions.md         Working assumptions and the effect if each is wrong
├── tasks.md               Open action items, owners, and verification status
├── skills_used.md         Which AgentCounsel skills were run, when, and on what
├── outputs/               Draft deliverables produced by skills
│   └── README.md
├── quality_checks/        Records of quality-layer passes run on the outputs
│   └── README.md
├── attorney_review.md     The attorney sign-off gate for the whole matter
└── matter_status.md       Current status, next steps, and a change log
```

## How to create a populated workspace

**Option A — script.** From the repository root:

```
python scripts/init_matter_workspace.py "Contoso MSA Review" --practice-area contracts
```

The script copies this template into a new, safely named matter directory and
seeds `matter_profile.md` with next steps. See `--help` for `--dry-run`,
`--list-templates`, `--pack`, and `--force`.

**Option B — manual.** Copy this entire `_template/` directory to a new location
(for example `matters/2026-contoso-msa-review/`), then work through the files in
this order: `matter_profile.md` → `facts.md` / `open_questions.md` →
`source_log.md` → run skills (recording each in `skills_used.md`, storing drafts
in `outputs/`) → `citation_map.md` / `unsupported_claims.md` / `assumptions.md` →
`quality_checks/` → `attorney_review.md`. Keep `matter_status.md` current
throughout.

Do not edit the files inside `_template/` itself — they are the reusable blank
scaffold. Edit only the copy you create.

## Quality-layer classifications

`source_log.md`, `citation_map.md`, `unsupported_claims.md`, and `assumptions.md`
use the exact classification vocabulary that the quality-layer skills
(`skills/legal-methodology/source-validation/`, `.../citation-integrity-check/`)
already use, so a quality pass maps cleanly onto the workspace:

- **source-supported** — directly supported by a provided source.
- **source-mentioned but insufficient** — the source touches the point but does
  not adequately support the statement.
- **unsupported** — no source supports the statement.
- **contradicted by source** — a provided source cuts against the statement.
- **legal authority required** — a legal proposition needing a verified citation.
- **attorney judgment required** — a determination only the attorney can make.
- **user-provided authority** — authority supplied by the user (still verify).
- **model-suggested authority requiring verification** — an authority surfaced by
  the model that has **not** been verified against an authoritative source.
- **unsupported or unverifiable authority** — an authority that could not be
  located or verified; treat as unusable until verified.

> These templates organize and label sources. They do **not** perform automated
> legal verification. Verification of every authority and deadline remains an
> attorney task.

## No backend, runtime, or vendor dependency

Every file here is plain Markdown. The workspace works in any text editor, any AI
assistant, and any document system. See `core/legal-work-product.md` and the
repository `README.md` for the principles that govern the library.
