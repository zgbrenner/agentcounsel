# AgentCounsel Skill Specification v2 Design

## Status

Approved for implementation through the Phase 2 scope previously presented and the user's July 13, 2026 instruction to merge Phase 1 and move to Phase 2.

## Goal

Add a typed, selectively loadable execution contract for every AgentCounsel skill while preserving every existing `SKILL.md` as valid canonical Markdown and avoiding a disruptive migration of all 212 skills at once.

## Phase decomposition

Phase 2 contains several distinct subsystems. This design implements **Phase 2A — specification foundations**:

1. Define Skill Specification v2.
2. Compile a safe v2 contract for every legacy skill.
3. Allow optional hand-authored v2 sidecars for skills that need more precise types, gates, modes, evidence requirements, or modules.
4. Expose compiled contracts through MCP.
5. Pilot the format on three materially different skills.

Later Phase 2 work will extract large skill bodies into separately loadable modules, migrate additional skills, and generate expanded backward-compatible Markdown bundles from modular sources.

## Considered approaches

### 1. Add nested YAML directly to `SKILL.md`

Rejected. AgentCounsel intentionally uses a tiny top-level YAML subset so all tooling remains standard-library only and portable. Deep mappings and lists would either require a substantially more complex YAML parser or a third-party dependency.

### 2. Require a new typed file for all 212 skills immediately

Rejected. This would produce a very large migration with weak review quality. Most fields can be safely inferred from existing frontmatter and required sections, allowing migration to proceed incrementally.

### 3. Optional `SPEC.json` sidecar plus compiled legacy defaults

Selected. JSON provides nested, typed structures using the Python standard library. Existing Markdown remains canonical for human workflow guidance. Every skill receives a generated v2 execution contract, while a sidecar can override or enrich only the parts that need explicit human design.

## Canonical files and generated artifacts

Each skill may contain:

```text
skills/<practice-area>/<skill-slug>/
  SKILL.md          # existing canonical human-readable workflow
  SPEC.json         # optional canonical typed v2 overlay
  templates/        # existing templates
```

Repository-level files:

```text
specs/skill-spec-v2.schema.json     # published JSON Schema reference
metadata/skill_specs.json           # generated compiled contracts for all skills
docs/SKILL_SPEC_V2.md               # authoring and migration guide
docs/templates/SPEC_TEMPLATE.json   # copyable sidecar template
```

`SPEC.json` is canonical when present. `metadata/skill_specs.json` is always generated and must never be hand-edited.

## Compiled contract

Every compiled skill contract contains:

```text
schema_version
skill_id
title
skill_path
spec_path
has_custom_spec
inherits
gates
execution_modes
input_schema
output_schema
evidence_schema
modules
quality_checks
```

### Inheritance

`inherits` lists repository paths to shared rules. Legacy defaults include:

- `core/legal-work-product.md`
- `core/source-and-citation-discipline.md`
- `core/output-format-rules.md`
- `core/attorney-review-checklist.md`

`core/jurisdiction-and-deadline-gates.md` is added when the skill requires jurisdiction or deadline handling. Custom specs may add but may not remove the baseline safety inheritance.

### Gates

The normalized gate object contains:

- `missing_inputs`: always `stop-and-ask`;
- `attorney_review`: required for all current legal-work-product skills;
- `jurisdiction`: required or conditional;
- `deadline`: required or conditional, with `calculation_allowed: false`;
- `escalation`: risk-sensitive minimum behavior;
- optional skill-specific gates, each with a stable ID, condition, action, and reason.

A custom spec may strengthen a gate but may not weaken baseline attorney-review, no-deadline-calculation, or stop-and-ask controls.

### Execution modes

Every skill supports three normalized modes:

- `quick-triage`: applicability, missing inputs, top issues, and escalation only;
- `standard`: the default attorney-ready deliverable;
- `deep-review`: full references, completeness passes, and all recommended quality checks.

A sidecar may disable a mode when unsafe. For example, a critical breach workflow may keep quick triage limited to immediate escalation and fact capture rather than substantive analysis.

### Typed inputs

Each input field includes:

```text
id
label
type
required
description
source_requirement
may_infer
sensitive
```

Allowed types are `text`, `document`, `document-set`, `enum`, `date`, `datetime`, `boolean`, `integer`, `number`, `jurisdiction`, and `object`.

Legacy input phrases are converted deterministically. Items beginning with `Optional:` become optional. The compiler never marks a legacy input as inferable.

### Typed outputs

Each output artifact includes:

```text
id
label
type
required
description
attorney_review_required
```

Allowed output types are `section`, `table`, `checklist`, `memo`, `letter`, `tracker`, `timeline`, `matrix`, and `structured-data`.

Legacy outputs compile to required `section` artifacts. Custom specs provide more precise shapes.

### Evidence schema

All contracts inherit a common claim-support record:

```text
claim_id
source_document_id
locator
support_text
support_type
verification_status
confidence
reviewer
reviewed_at
```

The default required fields are `claim_id`, `source_document_id`, `locator`, `support_type`, and `verification_status`. A sidecar may require additional fields but may not remove the baseline required fields.

### Modules

`modules` declare selectively loadable references, templates, profiles, connectors, or optional workflow material:

```text
id
kind
path
required
load_when
```

Allowed kinds are `reference`, `template`, `profile`, `connector`, `quality-check`, and `workflow-module`. All paths must resolve within the repository. Modules do not execute code.

## Validation

A standard-library compiler validates:

- schema version and skill ID;
- controlled types and execution mode IDs;
- baseline inheritance and safety gates;
- unique field, artifact, gate, and module IDs;
- required labels and descriptions;
- repository path resolution;
- `may_infer` remains false for required legal inputs;
- deadline calculation remains disabled;
- custom specs cannot weaken inherited safety controls.

`python scripts/build_skill_specs.py --check` validates every custom sidecar and detects generated-artifact drift.

## MCP behavior

The MCP catalog service loads `metadata/skill_specs.json` once and adds:

- `get_skill_spec(skill_id)` for the complete typed contract;
- compact spec summaries on skill cards;
- execution modes and typed missing-input fields in route responses;
- quality checks and gates from the compiled contract rather than duplicate heuristics where available.

The full `SKILL.md` remains available separately through `get_skill`.

## Pilot skills

### `contracts/nda-review`

Demonstrates enum inputs, three execution modes, optional playbook/profile modules, structured risk outputs, and evidence tied to contract sections.

### `legal-research/legal-research-memo`

Demonstrates jurisdiction inputs, authority/source modules, memo outputs, citation evidence, and a deep-review mode requiring source-validation and negative-treatment checks.

### `privacy/breach-response-workflow`

Demonstrates critical-risk escalation, immediate-attorney-attention gates, privileged and sensitive inputs, strict no-deadline-calculation behavior, and disabling any mode that could imply a legal reportability conclusion.

## Non-goals

- Do not rewrite the three pilot `SKILL.md` bodies.
- Do not migrate all 212 skills to custom sidecars in this change.
- Do not add runtime model calls, document parsing, connectors, or autonomous execution.
- Do not calculate legal deadlines.
- Do not allow typed schemas to imply that model output is legally correct.
- Do not remove existing frontmatter or required Markdown sections.

## Testing

Tests use temporary repositories and standard-library `unittest`.

Required coverage:

- deterministic legacy compilation;
- optional input inference from `Optional:` prefixes;
- baseline inheritance and gates;
- three default execution modes;
- custom sidecar merge behavior;
- safety controls cannot be weakened;
- invalid types, duplicate IDs, and unresolved paths fail;
- dedicated generated artifact is deterministic and `--check` detects drift;
- MCP skill-spec retrieval and routing use compiled contracts;
- all three pilot sidecars validate;
- existing 212-skill metadata and pack generation remain compatible.
