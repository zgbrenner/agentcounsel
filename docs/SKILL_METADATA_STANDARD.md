# AgentCounsel Skill Metadata Standard

Every canonical skill in AgentCounsel carries a standardized block of
**YAML frontmatter** at the top of its `SKILL.md`. The frontmatter is
agent-readable metadata: it lets LLMs, browser agents, static-site
generators, and package builders discover, filter, and route skills
without parsing the Markdown body.

This document defines each field, the allowed values, and the formatting
rules. It is the reference for the validation enforced by
`scripts/validate_repo.py` and for the index produced by
`scripts/build_skill_index.py`.

## Where the metadata lives

The frontmatter is the first thing in every `skills/<area>/<skill>/SKILL.md`
file, delimited by a line containing only `---` at the start and another at
the end:

```yaml
---
name: NDA Review
description: "Use when reviewing a non-disclosure or confidentiality agreement to produce a triage rating (route, flag, or stop), a structured risk summary, and prioritized redline points for attorney review."
practice_area: contracts
task_type: review
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The full NDA or confidentiality agreement text"
  - "The client's role: disclosing, receiving, or mutual"
  - "The business and transaction context"
  - "Optional: the client's standard NDA positions or playbook"
outputs:
  - "Triage rating (route, flag, or stop)"
  - "Structured risk summary"
  - "Prioritized redline points for attorney review"
related_skills:
  - skills/contracts/contract-risk-review/SKILL.md
  - skills/contracts/redline-summary/SKILL.md
tags:
  - contracts
  - nda
  - confidentiality
  - contract-review
  - risk-triage
---
```

All eleven fields below are **required** on every canonical skill, and they
appear in the order shown above.

## The fields

### `name`

The human-readable skill name, in title case (for example, `NDA Review`).
A non-empty string. It matches the H1 title in the body.

### `description`

One line describing **when to use the skill** — action-oriented and
trigger-rich, not a definition. It must begin with `Use when` and name the
situations, documents, or requests that should route to this skill, so an
agent can match a user's intent to it. Quote the value with double quotes.

Good: `"Use when reviewing a statement of work to assess scope, deliverables, and consistency with the governing master agreement."`

Avoid a bare definition such as `"A skill for statements of work."` — it
says what the skill *is*, not when to reach for it.

### `practice_area`

The practice area the skill belongs to. It **must exactly match the
directory area** — the folder name directly under `skills/`. Current
values: `legal-research`, `litigation`, `contracts`, `corporate`,
`employment`, `privacy`, `product-legal`, `regulatory`, `ai-governance`,
`ip`, `financial-crime`, `real-estate`, `m-and-a`, `antitrust-competition`,
`securities-capital-markets`, `tax`, `bankruptcy-restructuring`, `insurance`,
`trusts-estates`, `family-law`, `legal-ops`, `setup`, `legal-methodology`.

### `task_type`

The kind of work the skill performs. One of the controlled values:

| Value | Meaning |
|---|---|
| `intake` | Capture and structure a new matter, use case, or disclosure so it can be routed. |
| `interview` | Run a structured cold-start interview to configure a practice profile. |
| `research` | Produce a legal research memo answering a specific question. |
| `review` | Review a provided document or document set for risk, gaps, or issues. |
| `triage` | Run a first-pass assessment that rates a matter and routes it to the right specialist. |
| `drafting` | Produce a draft legal document or instrument. |
| `analysis` | Work a structured analytical method through a situation, question, or set of facts. |
| `summarization` | Condense a document or a set of changes into a structured summary. |
| `extraction` | Pull structured data, issues, or events out of a document set. |
| `verification` | Quality-control a draft, or its sources, before it is relied on. |

### `jurisdictions`

A list of jurisdictions the skill is **specific to**. AgentCounsel skills
supply process and structure, not the law of any jurisdiction, so this list
is normally empty (`[]`) — the skill is jurisdiction-agnostic and the actual
jurisdiction is supplied per matter. Populate it only if a skill is
genuinely bound to one or more named jurisdictions.

### `risk_level`

How much is at stake if the skill's draft output is wrong and the error is
not caught. One of `low`, `medium`, `high`, `critical`:

| Value | Meaning |
|---|---|
| `low` | Configuration or administrative scaffolding. An error is easy to catch and low-consequence. |
| `medium` | Standard issue-spotting, review, or analytical drafts. An error is normally caught at attorney review; consequences are moderate. |
| `high` | Adversarial-facing, filing-bound, deadline-sensitive, or exposure-creating work product. An uncaught error can create real legal exposure. |
| `critical` | Work where an error risks irreversible or severe harm — for example spoliation or waiver of privilege. |

`risk_level` describes the inherent stakes of the skill's domain. It is not
a statement that the output may be used without review — every skill still
requires attorney review (see the next field).

### `requires_attorney_review`

A boolean. `true` means the skill's output is draft legal work product that
a qualified, licensed attorney must review before it is relied upon. For
every skill in this library it is `true`. Set it to `false` only for a
hypothetical future skill whose output is not legal work product at all.

### `inputs`

A list of the inputs the skill needs to run — the materials, facts, and
context a user must supply. Each item is a short noun phrase. Mark
optional-but-recommended inputs by beginning the item with `Optional:`.
At least one item is required.

### `outputs`

A list of the deliverables the skill produces. Each item is a short noun
phrase naming a section or artifact of the output. At least one item is
required.

### `related_skills`

A list of other skills a user might reach for instead of, or alongside,
this one — drawn from the skill's "Do Not Use When" cross-references and its
practice area. **Each entry is a repository path** of the form
`skills/<area>/<skill>/SKILL.md`, and each must resolve to a real skill. A
skill never lists itself. The list may be empty, but in practice every
skill names at least one neighbor.

### `tags`

A list of lowercase, hyphenated keyword tags for search and filtering — for
example `contract-review`, `risk-triage`, `data-protection`. Four to seven
tags is typical. At least one is required.

## YAML format conventions

The frontmatter uses a deliberately small, fixed YAML subset so it stays
both valid YAML (for external tools) and parseable without a third-party
YAML library (the repository is standard-library only):

- **Scalars** are written `key: value`. Quote `description` with double
  quotes; `name`, `practice_area`, `task_type`, and `risk_level` are plain.
- **`requires_attorney_review`** is the bare word `true` or `false`.
- **An empty list** is written inline: `jurisdictions: []`.
- **A non-empty list** is a block of `  - item` lines, indented two spaces.
  Quote `inputs` and `outputs` items with double quotes (they contain
  punctuation); `related_skills` paths and `tags` are plain.

Do not introduce other YAML features (anchors, flow mappings, multi-line
scalars). Keep `description` on a single line.

## The generated index

`scripts/build_skill_index.py` parses the frontmatter of every canonical
skill and writes `metadata/index.json` — one machine-readable file with the
full metadata of every skill, plus counts by practice area, task type, and
risk level. It also writes `metadata/router.json`, a generated routing index
derived from the same canonical skills. Regenerate both whenever a skill's
frontmatter changes:

```
python scripts/build_skill_index.py           # write metadata/index.json and metadata/router.json
python scripts/build_skill_index.py --check    # report drift only
```

Consumers — agents, site generators, package builders — should read
`metadata/index.json` and `metadata/router.json` rather than re-parsing every
`SKILL.md`.


## Typed execution contracts

The eleven frontmatter fields remain the compact discovery and routing
standard. Every skill also compiles to a typed Skill Specification v2
contract in `metadata/skill_specs.json`. The compiler derives safe defaults
for legacy skills, so no sidecar is required.

A skill may include `skills/<area>/<skill>/SPEC.json` when explicit input or
output types, execution modes, custom gates, evidence requirements, or
selectively loaded modules materially improve the workflow. `SPEC.json` is
an overlay: it adds to or refines the frontmatter-derived contract and may
not weaken attorney review, missing-input stops, deadline safeguards,
required-input provenance, baseline evidence fields, or inherited core
rules. See `docs/SKILL_SPEC_V2.md` and
`docs/templates/SPEC_TEMPLATE.json`.

Regenerate and validate typed contracts whenever frontmatter, a skill body,
or a sidecar changes:

```
python scripts/build_skill_specs.py
python scripts/build_skill_specs.py --check
```

Consumers that need execution modes, typed fields, gates, evidence records,
or module-loading conditions should read `metadata/skill_specs.json` rather
than reconstructing those fields from `SKILL.md`.

## Normalized generated fields

The frontmatter remains intentionally small. The generated index adds derived
fields needed for routing, pack generation, site display, eval tracking, and
plugin compatibility:

| Field | Source |
|---|---|
| `id` | Stable `<practice_area>/<skill-folder>` identifier. |
| `title` | Alias of frontmatter `name`. |
| `category` | Alias of frontmatter `task_type`. |
| `path` | Repository path to the canonical `SKILL.md`. |
| `summary` | Alias of frontmatter `description`. |
| `use_when` | Bullets from the skill's `Use When` section, falling back to `description`. |
| `required_inputs` | Alias of frontmatter `inputs`. |
| `expected_outputs` | Alias of frontmatter `outputs`. |
| `risk_level` | Frontmatter `risk_level`. |
| `requires_jurisdiction` | Derived from jurisdiction metadata and jurisdiction/governing-law gates in the skill body. |
| `requires_deadline_check` | Derived from deadline/date language in the skill body. |
| `requires_attorney_review` | Frontmatter `requires_attorney_review`. |
| `related_skills` | Frontmatter `related_skills`. |
| `recommended_quality_checks` | Derived list of AgentCounsel quality-check IDs such as `attorney-review-gate`, `assumption-audit`, `citation-integrity-check`, `source-validation-check`, `hallucination-red-team`, `privilege-confidentiality-check`, `legal-prose-polish`, `output-format-compliance-check`, and `jurisdiction-deadline-gates`. |
| `compatible_platforms` | File-based platform surfaces currently supported by generated packs and adapters. |
| `pack_tags` | Search and pack-building tags derived from practice area, task type, risk level, and frontmatter `tags`. |
| `eval_status` | Eval coverage status based on `evals/skills/<slug>.eval.yaml` and candidate outputs under `evals/outputs/<slug>/`: `untested`, `manual-eval-ready`, or `scored`. |

Do not hand-edit generated metadata. If a derived field looks wrong, fix the
skill body/frontmatter or the generator and re-run the script.

## Validation

`scripts/validate_repo.py` enforces this standard on every canonical skill.
A skill fails validation if any required field is missing, a list field is
not a list, `description` does not begin with `Use when`, `practice_area`
does not match the directory, `task_type` or `risk_level` is outside its
controlled set, `requires_attorney_review` is not a boolean, `inputs`,
`outputs`, or `tags` is empty, or a `related_skills` entry does not resolve
to a real skill. Validation also fails if `metadata/index.json` or
`metadata/router.json` is missing or out of date, if normalized skill IDs are
duplicated, if a normalized path does not exist, if a compatible platform or
quality-check ID is invalid, or if an eval coverage status is invalid. Eval
coverage labels describe repository test coverage only; they do not claim legal
correctness.

## Adding or changing a skill

1. Write the frontmatter with all eleven fields, in the order above.
2. Make `description` trigger-rich — it must say *when* to use the skill.
3. Set `practice_area` to the directory area.
4. Pick `task_type` and `risk_level` from the controlled values.
5. Keep `requires_attorney_review: true` for any legal work product.
6. List concrete `inputs`, `outputs`, `related_skills` paths, and `tags`.
7. Run `python scripts/build_skill_index.py` to regenerate the index and router.
8. Run `python scripts/build_skill_specs.py` to regenerate and validate typed execution contracts.
9. If the skill should affect platform packs, run `python scripts/build_platform_packs.py`.
10. Run `python scripts/validate_repo.py` and confirm it passes.
