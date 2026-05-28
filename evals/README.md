# AgentCounsel Skill Evals

A lightweight evaluation framework for AgentCounsel skills. It checks that
skills produce **useful, safe, attorney-review-ready** legal work product.

## What these evals are — and are not

These evals are **quality checks, not legal validation.**

- They check that a skill's output is well-structured, disciplined about
  inputs and uncertainty, safely framed, and free of fabricated authority.
- They do **not** verify that a skill's legal content is correct, complete, or
  appropriate for any matter. That requires a qualified, licensed attorney and
  each skill's own Attorney Verification Checklist.

A skill that passes every eval is well-built. It is not thereby "approved" for
legal use. See `../VALIDATION.md`, which draws the same line for the
repository validator.

## What the evals test

Each skill eval is a set of **cases**. A case describes a realistic request to
a skill and the properties its output should and should not have:

- **`user_request`** — what the user asks the skill to do.
- **`input_facts`** — the sample facts and materials provided with the request.
- **`expected_output_characteristics`** — what a good output contains.
- **`failure_modes`** — specific ways the output could go wrong.
- **`safety_checks`** — the safety properties the output must hold.

Cases come in two flavors: a **golden-path** case (a well-formed request with
complete inputs) and a **safety-stress** case (missing, ambiguous, or
adversarial input that the skill must handle by stopping and asking rather
than fabricating).

Across cases, evals also reference **shared assertions** — recurring quality
and safety properties defined once in `shared/assertions.md`, such as "output
is labeled a draft for attorney review" and "output does not invent cases,
statutes, citations, or deadlines."

Skills are scored with the eight-dimension `SKILL_QUALITY_RUBRIC.md`.

## Layout

```
evals/
  README.md                  - this file
  SKILL_QUALITY_RUBRIC.md    - 1-5 scoring rubric for skill quality
  RUBRICS.md                 - reusable rubrics for skills, router, packs, and quality checks
  benchmarks/                - richer fictional benchmark cases
  router/                    - vague-request router evals
  static/                    - metadata, router, and pack integrity eval definitions
  shared/
    assertions.md            - recurring quality and safety assertions
  skills/
    contract-risk-review.eval.yaml
    nda-review.eval.yaml
    matter-intake.eval.yaml
    litigation-chronology.eval.yaml
    privilege-log-review.eval.yaml
    dpa-review.eval.yaml
    launch-review.eval.yaml
    compliance-gap-matrix.eval.yaml
    lease-abstract.eval.yaml
    lease-amendment-reconciliation.eval.yaml
    commercial-lease-review.eval.yaml
    psa-review.eval.yaml
    title-survey-objection-tracker.eval.yaml
    real-estate-diligence-checklist.eval.yaml
    closing-deliverables-tracker.eval.yaml
    estoppel-snda-review.eval.yaml
    zoning-use-restriction-issue-spotter.eval.yaml
    loi-term-sheet-review.eval.yaml
    acquisition-diligence-request-list.eval.yaml
    data-room-index-review.eval.yaml
    purchase-agreement-issue-list.eval.yaml
    reps-warranties-disclosure-schedule-review.eval.yaml
    indemnity-escrow-risk-review.eval.yaml
    m-and-a-closing-deliverables-tracker.eval.yaml
    third-party-consents-assignment-review.eval.yaml
    post-closing-obligations-tracker.eval.yaml
    integration-legal-issues-checklist.eval.yaml
```

The schema validator lives at `../scripts/check_evals.py`.

## How to run the evals

There are two layers: a static check that runs in CI, and a manual review
pass that exercises the skills.

### 1. Static schema check (no API keys, runs in CI)

```
python scripts/check_evals.py
```

This is a non-LLM check. It confirms that the eval files exist, parse, and
conform to the schema below; that every required skill has an eval file; and
that every shared assertion referenced is defined. It needs no API key and no
network. It runs in CI alongside `scripts/validate_repo.py` — see
`../.github/workflows/validate.yml`. Exit code `0` means all checks passed.

### 2. Static heuristic runner (no API keys, runs in CI)

```
python scripts/run_evals.py                 # run all eval files
python scripts/run_evals.py <skill-slug>    # run one skill's eval
python scripts/run_evals.py --strict        # required candidates must pass
python scripts/run_evals.py --quiet         # rollup only, no per-case detail
python scripts/run_evals.py --markdown-report reports/eval-run.md
python scripts/generate_eval_report.py      # write reports/eval-coverage.md
python scripts/generate_eval_report.py --check
```

The runner reads candidate skill outputs from `evals/outputs/<slug>/<case-id>.md`
and scores them against the shared assertions in `shared/assertions.md`,
modulated by each case's `input_facts` (jurisdiction-missing,
prompt-injection, stop-and-ask). It is a non-LLM, stdlib-only check — no
API keys and no network.

For each case the runner reports per-assertion pass / fail / skip, an
automated assertion pass rate, and the count of per-case manual-review
items (`expected_output_characteristics`, `failure_modes`, `safety_checks`)
that this static layer does not score. Those remain for the manual review
pass below — or for the LLM-judge promptfoo path the schema already maps
onto.

Under `--strict`, every case in every required eval slug must have a
candidate file under `evals/outputs/` and every applicable assertion must
pass; failure exits 1. The CI pipeline runs `--strict --quiet` after
`check_evals.py`. See `outputs/README.md` for the file convention and how
to add a candidate.

### 2a. Benchmark, router, and static suites

`benchmarks/*.eval.yaml` uses a richer case schema with `eval_id`, `skill_id`,
practice area, category, risk level, source materials, required quality checks,
rubrics, pass/fail criteria, known limitations, and an `eval_status`.

`router/*.eval.yaml` records expected routing behavior for vague requests:
primary skill, missing facts, gates, quality checks, and attorney escalation.

`static/*.eval.yaml` documents deterministic metadata, router, and pack checks.
`scripts/check_evals.py` enforces those checks against `metadata/index.json`,
`metadata/router.json`, and `metadata/packs.json`.

### 3. Manual review pass (exercises the skills)

The evals are written so a reviewer can run them by hand for the items
the static runner cannot score:

1. Pick a skill eval file under `skills/`.
2. For each case, give the skill its `user_request` and `input_facts` in
   whatever agent or assistant runs AgentCounsel skills.
3. Compare the output against the case:
   - every item in `expected_output_characteristics` should be present;
   - no item in `failure_modes` should occur;
   - every item in `safety_checks` should hold;
   - every assertion in the file's `shared_assertions` should pass (see
     `shared/assertions.md` for pass/fail criteria).
4. Score the skill with `SKILL_QUALITY_RUBRIC.md`.

This pass is human-judged and intentionally not part of CI, so CI stays free
of API keys and model calls.

### 4. Adapting to promptfoo (optional, later)

The eval files are deliberately shaped to map onto
[promptfoo](https://promptfoo.dev) with minimal change, so the manual pass can
later be automated:

- each `case` becomes a promptfoo `test`;
- `user_request` and `input_facts` become `vars` interpolated into the prompt;
- each `expected_output_characteristics`, `failure_modes`, and `safety_checks`
  item becomes an `assert` of type `llm-rubric`;
- each `shared_assertions` ID resolves, via `shared/assertions.md`, to a
  reusable `llm-rubric` assertion.

promptfoo is not added to this repository: it requires Node.js, a package
manager, and model API keys, none of which AgentCounsel otherwise depends on.
Keeping the scaffold as plain YAML preserves the repo's zero-dependency,
Markdown-native design while leaving the promptfoo path open.

## Eval file schema

Each file in `skills/` is named `<skill-slug>.eval.yaml` and uses a small,
fixed subset of YAML: two-space indentation, scalar values that run to the end
of the line, block lists of scalars, and one block list of mappings (`cases`).
There are no quoted strings, no flow collections, and no block scalars — which
is why `scripts/check_evals.py` can validate the files with no third-party
YAML dependency.

Top-level keys (all required):

| Key                 | Type             | Meaning                                              |
|---------------------|------------------|------------------------------------------------------|
| `skill`             | scalar           | The skill slug; must match the file name.            |
| `skill_path`        | scalar           | Repo-relative path to the skill's `SKILL.md`.        |
| `description`       | scalar           | One-line summary of what this eval covers.           |
| `shared_assertions` | list of scalars  | Assertion IDs from `shared/assertions.md`.           |
| `cases`             | list of mappings | One or more eval cases.                              |

Each entry in `cases` (all keys required):

| Key                               | Type            | Meaning                                  |
|-----------------------------------|-----------------|------------------------------------------|
| `id`                              | scalar          | Unique case identifier within the file.  |
| `user_request`                    | scalar          | The request made to the skill.           |
| `input_facts`                     | list of scalars | Sample facts and materials provided.     |
| `expected_output_characteristics` | list of scalars | What a good output contains.             |
| `failure_modes`                   | list of scalars | Specific ways the output could go wrong. |
| `safety_checks`                   | list of scalars | Safety properties the output must hold.  |

`scripts/check_evals.py` rejects unknown keys, empty required values, empty
lists, duplicate case IDs, a `skill_path` that does not resolve to a file, a
`skill` that does not match the file name, and any `shared_assertions` ID not
defined in `shared/assertions.md`.

Benchmark cases use the schema documented in `../docs/EVALS.md`. Their
statuses are `unrun`, `manual-ready`, `automated-static`, and `scored`.
Do not mark a benchmark as `scored` unless there is an actual candidate-output
score or recorded manual score.

## Adding a new skill eval

1. Copy an existing file in `skills/` to `skills/<new-skill-slug>.eval.yaml`.
2. Set `skill` to the slug (it must equal the file name without
   `.eval.yaml`) and `skill_path` to the skill's `SKILL.md`.
3. Write at least two cases — one golden-path, one safety-stress — each with
   all six case keys populated and a unique `id`.
4. In `shared_assertions`, list the IDs from `shared/assertions.md` that the
   skill genuinely exercises. Add a new assertion to `shared/assertions.md`
   first if you need one.
5. Run `python scripts/check_evals.py` and resolve any errors.
6. To make the eval part of the required set checked by CI, add the slug to
   `REQUIRED_EVAL_SLUGS` in `scripts/check_evals.py`.
7. Note the change under "Unreleased" in `../CHANGELOG.md`.

Keep eval content free of real client facts — use fictional placeholders
only, as `../CONTRIBUTING.md` requires for the rest of the library.
