# Quality Checks

> Record the quality-layer passes run on this matter's outputs. Each record is
> draft work product for attorney review. These checks organize and surface
> issues; they do **not** perform automated legal verification. The supervising
> attorney remains responsible for verifying every authority and deadline.

Store one record per check run. Suggested naming:
`<output-slug>-<check-slug>.md` (for example `01-nda-review-source-validation.md`).

## Checks Run

| # | Output Reviewed | Quality Check | Date | Result | Open Items Created |
|---|---|---|---|---|---|
| 1 | `outputs/[CONFIRM]` | `[CONFIRM: e.g., source-validation]` | `[CONFIRM]` | `[CONFIRM: Pass / Issues found]` | `[CONFIRM: tasks.md / unsupported_claims.md refs]` |
| 2 | | | | | |

## Recommended Checks for This Matter

See `matter_profile.md` → Recommended Quality Checks. The standard quality-layer
skills live under `skills/legal-methodology/`:

- `source-validation` — every statement traced to a classified source.
- `citation-integrity-check` — every authority verified or flagged.
- `assumption-audit` — assumptions surfaced, none treated as fact.
- `hallucination-red-team` — adversarial pass for invented content.
- `privilege-confidentiality-check` — privilege and confidentiality preserved.
- `output-format-compliance-check` — output matches the requested format.
- `legal-prose-polish` — clarity without changing substance.
- `attorney-review-gate` — final supervised gate (see `attorney_review.md`).
