# Source Validation

Source validation checks whether factual and legal claims in draft legal work
product are supported by source materials available in the session.

It is not independent legal research and does not verify current law. It does
not decide whether authority is binding, persuasive, current, or correctly
interpreted. Those remain attorney functions.

## Claim Support Status

Use `skills/legal-methodology/source-validation/SKILL.md` to classify each
material claim:

| Status | Meaning |
|---|---|
| Source-supported | An available source directly supports the claim as stated, subject to attorney review. |
| Source-mentioned but insufficient | A source touches the topic but does not fully support the claim. |
| Unsupported | No available source supports the claim. |
| Contradicted by source | An available source conflicts with the claim. |
| Legal authority required | The claim requires legal authority not supplied in the current materials. |
| Attorney judgment required | The claim depends on legal interpretation, strategy, privilege, or professional judgment. |

## Required Output

The check produces:

- claim table
- source reference table
- citation and source validation table
- unsupported claims list
- contradictions list
- recommended revisions
- date and deadline flags
- attorney verification checklist

## Workflow Integration

Run source validation after a primary skill when the output contains material
facts, source-dependent claims, quotations, legal propositions, or dates.

For legal authorities, run `citation-integrity-check` as a companion check. For
model-generated drafts, run `hallucination-red-team` if unsupported claims or
invented authority risk is material.
