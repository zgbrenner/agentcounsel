# Diligence Issue Extraction — Cannot Proceed

> **Draft for attorney review. Not legal advice.** This document is draft attorney work product and does not constitute legal advice. The Diligence Issue Extraction skill cannot proceed on the inputs provided; the sections below list what is missing before any substantive work is attempted.

## Stop and Ask — Missing Required Inputs

The skill cannot proceed without required gate information. The jurisdiction and governing law for this transaction are not provided, and one or more of the skill's required inputs — the target documents, the deal context, and the materiality threshold — are also not provided `[CONFIRM: jurisdiction and governing law]`. Building a diligence issues memo without knowing the applicable law, the deal context, and the materiality threshold would mean guessing at every severity call and every successor-liability flag. This skill stops here before any substantive analysis to avoid fabricating findings from missing facts.

## Inputs Required Before Substantive Work

- [ ] The target due-diligence documents, provided in full — the skill does not query a data room or reconstruct document contents from a description.
- [ ] Deal context: deal name, the user's side (buy-side or sell-side), and the diligence categories in scope.
- [ ] The materiality threshold — dollar amount, percentage, or qualitative standard defining a material issue for this deal.
- [ ] Jurisdiction and governing law `[verify jurisdiction]` — required before any successor-liability or enforceability concept can be flagged meaningfully.

## What This Skill Will Not Do

- Will not assume a materiality threshold to produce an issues table.
- Will not assume a jurisdiction or governing law to fill the gap.
- Will not reconstruct document contents, defined terms, or diligence findings from background knowledge.
- Will not issue a due-diligence opinion or legal sign-off; that is outside this skill's scope in any event.

## Attorney Verification Checklist

- [ ] Confirm jurisdiction and governing law before any successor-liability or contract-enforceability concept is analyzed `[verify jurisdiction]`.
- [ ] Confirm the target documents, deal context, and materiality threshold are obtained before this skill is re-run.
- [ ] Confirm no partial issues memo was relied upon in place of the complete review.
- [ ] Resolve all `[CONFIRM]` placeholders before proceeding.
