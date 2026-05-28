# Evals

AgentCounsel evals are lightweight, deterministic quality checks for legal
skills, router behavior, metadata coverage, platform packs, and quality-layer
workflows. They do not call model APIs, require secrets, or verify legal
correctness.

## What Evals Can And Cannot Prove

Static evals can prove that files parse, references resolve, metadata and pack
relationships are coherent, candidate outputs carry required safety framing,
and benchmark cases are ready for manual or model-output review.

Static evals cannot prove that a legal conclusion is correct, that an
authority is current, or that a draft is safe to rely on. Every output remains
draft legal work product for attorney review.

## Eval Types

| Type | Location | Purpose |
|---|---|---|
| Skill evals | `evals/skills/*.eval.yaml` | Per-skill golden-path and safety-stress cases. |
| Candidate outputs | `evals/outputs/<slug>/<case-id>.md` | Optional outputs scored by the static runner. |
| Benchmarks | `evals/benchmarks/*.eval.yaml` | Cross-practice fictional benchmark cases with richer legal-safety fields. |
| Router evals | `evals/router/*.eval.yaml` | Vague request routing expectations. |
| Static integrity evals | `evals/static/*.eval.yaml` | Metadata, router, and pack integrity checks. |
| Shared assertions | `evals/shared/assertions.md` | Reusable candidate-output checks. |
| Rubrics | `evals/RUBRICS.md` | Reusable legal-safety and quality rubrics. |

## Commands

```
py scripts\check_evals.py
py scripts\run_evals.py --strict --quiet
py scripts\generate_eval_report.py
py scripts\generate_eval_report.py --check
```

`check_evals.py` validates schemas and references. `run_evals.py` scores only
candidate outputs that exist under `evals/outputs/`; missing manual-ready
benchmark cases are not counted as passed. `generate_eval_report.py` writes
`reports/eval-coverage.md`.

## Skill Eval Schema

Skill eval files preserve the existing schema:

- `skill`
- `skill_path`
- `description`
- `shared_assertions`
- `cases`

Each skill case includes:

- `id`
- `user_request`
- `input_facts`
- `expected_output_characteristics`
- `failure_modes`
- `safety_checks`

## Benchmark Case Schema

Benchmark cases support:

- `eval_id`
- `title`
- `skill_id`
- `practice_area`
- `category`
- `risk_level`
- `task_prompt`
- `fictional_matter_facts`
- `provided_source_materials`
- `required_output`
- `expected_safety_behaviors`
- `prohibited_behaviors`
- `required_quality_checks`
- `expected_attorney_review_items`
- `rubric`
- `pass_fail_criteria`
- `scoring_weights`
- `known_limitations`
- `eval_status`

Allowed benchmark statuses are `unrun`, `manual-ready`, `automated-static`,
and `scored`. Do not mark a case `scored` unless the current runner or a
recorded manual score actually scored it.

## Adding An Eval

1. Use fictional facts only.
2. Pick the narrowest skill or router behavior being tested.
3. Add expected safety behavior and prohibited behavior, not just happy-path
   output shape.
4. Reference only valid skill IDs and quality-check IDs from
   `metadata/index.json`.
5. Run `py scripts\check_evals.py`.
6. Regenerate the coverage report with `py scripts\generate_eval_report.py`.

## Connections

Metadata uses eval files and candidate outputs to label skill eval coverage.
Router evals compare expected workflow choices against `metadata/router.json`
and `WORKFLOW_ROUTER.md`. Pack/static evals check `metadata/packs.json` and
core safety inclusion. Matter workspaces can store manual eval outputs as
review artifacts, but they do not make attorney review optional.
