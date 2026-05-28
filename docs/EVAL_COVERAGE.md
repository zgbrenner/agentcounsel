# Eval Coverage

The generated eval coverage report lives at
[`reports/eval-coverage.md`](../reports/eval-coverage.md).

Regenerate it after changing eval files, metadata, quality checks, router
behavior, or pack manifests:

```
py scripts\generate_eval_report.py
```

Check for drift:

```
py scripts\generate_eval_report.py --check
```

The report shows evals by practice area, risk level, quality check, and
platform pack, plus skills without eval coverage and high-risk coverage gaps.
It distinguishes static/manual-ready coverage from actual candidate-output
scoring and does not claim legal correctness.
