# Citation Map

> Draft work product for attorney review. Map each material statement in the
> matter's drafts to the source that supports it, using the quality-layer
> classification vocabulary. This map feeds
> `skills/legal-methodology/citation-integrity-check/SKILL.md`. It records the
> claimed support — it does **not** verify authorities. Verification is an
> attorney task.

## Statement-to-Source Map

| # | Statement (as drafted) | Output File | Cited Source | Classification | Notes |
|---|---|---|---|---|---|
| 1 | `[CONFIRM: statement]` | `outputs/[CONFIRM]` | `[CONFIRM: source from source_log.md]` | `[CONFIRM: see vocabulary below]` | |
| 2 | | | | | |

## Classification Vocabulary

Use these exact labels in the **Classification** column:

- `source-supported`
- `source-mentioned but insufficient`
- `unsupported`
- `contradicted by source`
- `legal authority required`
- `attorney judgment required`
- `user-provided authority`
- `model-suggested authority requiring verification`
- `unsupported or unverifiable authority`

Any statement classified `unsupported`, `contradicted by source`, or
`unsupported or unverifiable authority` must be moved to `unsupported_claims.md`
and resolved before the draft is relied upon. Any authority classified
`model-suggested authority requiring verification` must be verified by the
attorney before use.
