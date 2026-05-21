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

### 2. Manual review pass (exercises the skills)

The evals are written so a reviewer can run them by hand:

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

### 3. Adapting to promptfoo (optional, later)

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
