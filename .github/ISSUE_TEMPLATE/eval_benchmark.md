---
name: Eval / benchmark issue
about: Report a problem with an eval, the eval runner, benchmarks, or coverage reporting
title: "[Eval]: "
labels: eval
---

<!-- Do not include confidential, privileged, or real client information.
     Use fictional or redacted examples only. -->

## What is affected

- **Eval file or area:** <!-- e.g. evals/skills/nda-review.eval.yaml, evals/router/, evals/static/ -->
- **Script, if relevant:** <!-- check_evals.py, run_evals.py, generate_eval_report.py — or "n/a" -->

## The problem

<!-- What is wrong? A failing assertion, a schema error, a stale coverage report,
     a missing candidate output, an incorrect expectation? Be specific. -->

## Expected behavior

<!-- What should the eval or report do instead? -->

## Steps to reproduce

<!-- The exact command you ran and its output, e.g.
     python scripts/check_evals.py  or  python scripts/run_evals.py --strict --quiet -->

## Scope reminder

The eval system checks structure, routing, metadata, packs, and candidate-output
safety signals. It does **not** verify legal correctness and does not replace
attorney review. Please confirm the issue is within that scope.

- [ ] This is about eval structure / tooling, not legal correctness

## Additional context

<!-- Anything else that helps. See docs/EVALS.md and docs/CLI.md. -->
