# Candidate skill outputs (eval inputs)

This directory holds **candidate outputs** for the eval cases defined under
`evals/skills/`. Each file is one run of one skill against one case — the
artifact a supervising attorney would receive for review. The runner at
`../scripts/run_evals.py` scores these candidates against the shared
assertions in `shared/assertions.md`.

## File convention

```
evals/outputs/<skill-slug>/<case-id>.md
```

The slug must match the eval file name (e.g. `nda-review` for
`evals/skills/nda-review.eval.yaml`). The case id must match the `id` of a
case inside that file. A missing candidate is not a failure under the
default runner — it is reported as `no candidate available — skipping`.
Under `python scripts/run_evals.py --strict`, every case under each slug
in `REQUIRED_EVAL_SLUGS` must have a candidate present and passing.

## What the candidates here demonstrate

The 16 files checked in cover the eight required eval slugs, two cases
each (golden-path + safety-stress). They are **test fixtures**, sized to
exercise the static heuristics — not finished legal showcases. For
worked, human-readable examples see `../../examples/`.

The candidates are deliberately disciplined: each one carries a "draft
for attorney review / not legal advice" label, separates facts from
assumptions, uses `[CONFIRM]` and `[VERIFY]` placeholders rather than
fabricated authority, and ends with an Attorney Verification Checklist.
Safety-stress candidates demonstrate the "stop and ask" pattern — they
flag missing required inputs and refuse to proceed to substantive work.

## Adding a candidate

1. Pick an eval case in `evals/skills/<slug>.eval.yaml`.
2. Run the skill against the case's `user_request` and `input_facts` in
   your agent or assistant of choice.
3. Save the output as `evals/outputs/<slug>/<case-id>.md`.
4. Run `python scripts/run_evals.py <slug>` and address any failures.
5. If the case is one of the eight `REQUIRED_EVAL_SLUGS` enforced in CI,
   confirm `python scripts/run_evals.py --strict` passes before opening
   a PR.

Keep candidate content free of real client facts — fictional placeholders
only, as `../../CONTRIBUTING.md` requires for the rest of the library.
