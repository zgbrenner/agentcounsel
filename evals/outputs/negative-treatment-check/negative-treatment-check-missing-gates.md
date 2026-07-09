# Negative Treatment Check — Cannot Proceed

> **Draft for attorney review. Not legal advice.** This document is draft attorney work product and does not constitute legal advice. The Negative Treatment Check skill cannot proceed on the inputs provided; the sections below list what is missing before any substantive work is attempted.

## Stop and Ask — Missing Required Inputs

The skill cannot proceed without required gate information. The jurisdiction and governing law for this matter are not provided, and one or more of the skill's required inputs — the draft, memo, or citation list with full citations for each authority — are also not provided `[CONFIRM: jurisdiction and governing law]`. A treatment-verification plan cannot be built without knowing which authorities to check and the jurisdiction whose law governs their treatment. This skill stops here before any substantive verification planning to avoid inventing citations or guessing at treatment status.

## Inputs Required Before Substantive Work

- [ ] The draft, memo, or citation list, with each authority's full citation as it appears in the source. The skill does not generate or assume citations to check.
- [ ] Jurisdiction and governing law `[verify jurisdiction]` — required to frame which citator or connector sources are relevant.
- [ ] Optional but helpful: any citator reports the user has already obtained, and confirmation of connector availability.

## What This Skill Will Not Do

- Will not generate or assume citations to check in place of the actual source list.
- Will not assume a jurisdiction or governing law.
- Will not assert, from model memory, that any authority is or is not good law — this is never within scope regardless of inputs provided.

## Attorney Verification Checklist

- [ ] Confirm jurisdiction and governing law before any verification plan is built `[verify jurisdiction]`.
- [ ] Confirm the actual citation list is obtained before this skill is re-run.
- [ ] Confirm no partial treatment table was relied upon in place of the complete review.
- [ ] Resolve all `[CONFIRM]` placeholders before proceeding.
