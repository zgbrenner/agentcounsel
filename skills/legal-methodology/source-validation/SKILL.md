---
name: Source Validation
description: Use when checking that every cited source, authority, quotation, date, and factual claim in a draft legal work product actually exists and says what is claimed, applying the source hierarchy in `core/source-and-citation-discipline.md`.
---

# Source Validation

## Purpose

Apply a systematic method for checking that every cited source, authority, quotation, date, and factual claim in a draft legal work product actually exists and says what is claimed. The skill enumerates every citation and claim in the draft, classifies each by source tier using the hierarchy in `core/source-and-citation-discipline.md`, and marks each as verified, unverified, or unverifiable. It produces a source-by-source validation table and a list of unresolved items that must be checked before the draft is relied upon.

This skill does not and cannot substitute for independent legal research. It does not confirm whether an authority is current, controlling, or correctly interpreted. Model background knowledge is never treated as a source, even when it appears to confirm a citation. Verification means tracing a claim to a user-provided document or a source independently retrieved and confirmed in the current session — nothing else qualifies.

## Use When

- A draft legal work product contains citations, quotations, authority references, or factual claims that need to be checked before the draft is finalized or passed to attorney review.
- A user asks to "verify the sources," "check the citations," "confirm these quotes are real," or "validate the authority in this draft."
- The Red-Team Verifier (or any review process) has flagged specific citations or claims as unverified and a dedicated source check is needed.
- A legal research memo, brief section, or analysis contains cases, statutes, regulations, or secondary sources that were gathered during research and need to be confirmed before attorney reliance.
- A draft quotes from a source document (contract, filing, policy, statute) and the quotations need to be checked against the provided text.
- The user wants a complete audit trail showing which sources in a draft are confirmed and which require additional verification.

## Required Inputs

- The complete draft to be validated (uploaded or pasted). Do not validate from a summary or paraphrase.
- The source documents or authorities that are supposed to support the claims in the draft — for example, the contract the draft reviews, the cases the memo cites, or the regulatory text the analysis references. These are the materials against which quotations and propositions are checked.
- Optional: the skill or workflow that produced the draft — this informs which sourcing standards apply.
- Optional: a list of specific citations or claims flagged for priority review.

If the draft is not provided, stop and request it. If source documents are not provided, the validation will be limited to classifying citations by tier and marking unsupported claims as unverifiable — note this limitation prominently.

## Do Not Use When

- The task is to conduct new legal research and find sources for unsupported propositions — use `legal-research-memo` or a research skill; this skill validates existing sources, it does not find new ones.
- The task is to conduct a broader structural review of draft quality — use the Red-Team Verifier for that purpose; use this skill for focused source and citation checking.
- The draft contains no citations, quotations, or factual claims traceable to external sources — there is nothing to validate.
- The user needs an attorney to assess whether an authority supports a legal argument — that is a substantive judgment beyond the scope of this skill; flag those items as attorney verification items.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Model background knowledge is never a verification source. A citation that appears consistent with what the model knows about a case or statute is still classified as unverified unless it is present in a user-provided document or independently retrieved and confirmed in this session.
- Do not assert that a citation is valid or that a quotation is accurate based on model background knowledge, training data, or general familiarity with legal sources.
- Do not invent, reconstruct, or complete a partial citation. If a citation is incomplete, mark it as incomplete and list it as an unresolved item.
- Do not assert that a case, statute, or regulation does not exist — only that it could not be verified within this session. Absence of verification is not confirmation of fabrication; that determination requires independent research.
- Do not assess whether an authority is controlling, persuasive, current, or correctly applied — those are attorney functions. This skill checks existence and textual accuracy, not legal significance.
- Do not place client-sensitive facts from the draft into any reusable output beyond this validation report.
- Label the validation report as draft legal work product for attorney review.

## Workflow

1. **Confirm inputs.** Verify that you have the complete draft text. Note whether source documents have been provided and, if not, record the resulting limitation: without source documents, only citation-tier classification is possible — quotation checking and claim-source tracing require the underlying documents.

2. **Enumerate every citation and claim.** Read through the draft systematically and build a complete inventory of:
   - Case citations: case name, citation, reporter, year, court.
   - Statutory and regulatory citations: instrument name, section, version or effective date.
   - Secondary source citations: treatise, article, report, guidance document.
   - Quotations: every passage presented as a direct quotation from any source.
   - Factual claims: every claim of fact that depends on a source document, client representation, or external authority — as distinct from analytical inference.
   - Dates: every specific date asserted in the draft, including effective dates, filing dates, events, and deadlines.

   Assign each item a unique number for tracking. If the draft is long, work section by section and flag the section with each entry.

3. **Classify each item by source tier.** Apply the hierarchy from `core/source-and-citation-discipline.md`:
   - **Tier 1 — User-provided document.** The claim or quotation is traceable to a document the user supplied in this session. This is the highest-trust tier; verify by checking the text of the provided document.
   - **Tier 2 — Independently researched and verified.** The claim was located through a research step and confirmed to exist and to say what is claimed, through a source retrieved in this session. Identify the verification step.
   - **Tier 3 — Model background knowledge.** The claim appears consistent with model training knowledge but has not been confirmed against a Tier 1 or Tier 2 source. Tier 3 is never a valid verification source.

4. **Verify Tier 1 items.** For every claim or quotation classified as Tier 1:
   - Locate the specific text in the provided document.
   - Confirm that the quotation matches the source text exactly.
   - Confirm that the section reference, page, or paragraph is accurate.
   - Confirm that the claim accurately represents what the source says (not overstated, not understated).
   - Mark as: **Verified — Tier 1**, with a note identifying the source document and location.
   - If the claim cannot be located in the provided document, reclassify as Unverified and note the discrepancy.

5. **Assess Tier 2 items.** For every claim classified as Tier 2 (independently researched):
   - Identify whether the research step and verification are documented in the draft or the underlying workflow.
   - If documented and confirmable in this session, mark as **Verified — Tier 2**, with a note identifying the verification step.
   - If not documented or not confirmable in this session, mark as **Unverified — requires independent confirmation** and list as an unresolved item.

6. **Flag all Tier 3 items.** For every claim that relies only on model background knowledge:
   - Mark as **Unverified — Tier 3 (model knowledge only); must be independently confirmed before reliance**.
   - Do not treat apparent consistency with model knowledge as verification.
   - List every Tier 3 item as an unresolved item requiring independent research.

7. **Identify unverifiable items.** Flag items that cannot be verified within this session and whose verification requires access to external legal databases, official sources, or documents not provided:
   - Case citations where the case text was not provided.
   - Statutory text where the current version was not provided.
   - Regulatory text where the regulation was not provided.
   - Quotations from sources not provided.
   Mark each as **Unverifiable in this session — must be confirmed by attorney or researcher**.

8. **Check for incomplete and malformed citations.** For every citation in the inventory, check:
   - Is the citation complete? (Case: name, reporter, volume, page, court, year. Statute: instrument, section, version. Regulation: title, part, section, version.)
   - Are there missing elements (for example, a case name without a reporter cite, or a statute without a section number)?
   - Are there obvious formatting errors (for example, mismatched parenthetical dates or transposed numbers)?
   Mark incomplete citations as defects and list them as unresolved items.

9. **Check date claims.** For every date in the inventory:
   - Identify whether it is a user-provided date, a date from a provided document, or an asserted date with no source.
   - Flag any date that appears to have been computed or derived (rather than quoted from a source) as `[deadline verification required]`.
   - Flag any effective date or filing date that has not been confirmed against the applicable source.

10. **Compile unresolved items.** Build a consolidated list of all items marked Unverified, Unverifiable, or defective. For each, state: what the item is, why it is unresolved, and what step is needed to resolve it.

11. **Assemble the validation report** using the output format below. Label it as a draft for attorney review.

## Output Format

Deliver a Source Validation Report with the following sections:

1. **Report Header** — Draft title or description; date of validation; count of items (total | verified | unverified | unverifiable | defective); overall status (Cleared for attorney review / Unresolved items present — see below).
2. **Scope and Limitations** — Whether source documents were provided; any limitations on what could be verified in this session; explicit statement that model background knowledge was not used as a verification source.
3. **Source Validation Table** — One row per enumerated item:

   | # | Item Type | Claim / Citation as Stated | Asserted Source | Source Tier | Status | Notes |
   |---|-----------|---------------------------|-----------------|-------------|--------|-------|

   Status values: Verified — Tier 1 | Verified — Tier 2 | Unverified | Unverifiable in this session | Defective (incomplete / malformed)

4. **Unresolved Items List** — A numbered list of all unverified, unverifiable, and defective items, each stating: what needs to be checked, by what method, and who is responsible (attorney / legal researcher / client).
5. **Date and Deadline Flags** — A separate list of all date claims flagged `[deadline verification required]` or lacking a confirmed source.
6. **Overall Status Statement** — Either: "No unresolved items. Draft cleared for attorney review, subject to attorney verification checklist." Or: "Unresolved items present. Draft must not be relied upon until all unresolved items are confirmed."

Label the report: **Draft legal work product for attorney review. Not legal advice.**

## Attorney Verification Checklist

- [ ] Every Tier 1 (user-provided document) verification has been confirmed: the attorney has checked that the quotation and claim match the source document.
- [ ] Every Tier 2 (independently researched) item has been confirmed: the research step is documented and the authority has been independently verified.
- [ ] Every item marked Unverified or Unverifiable has been independently checked against an authoritative source by the attorney or a qualified researcher.
- [ ] Every case citation has been confirmed to exist, to be correctly cited, and to stand for the proposition the draft attributes to it.
- [ ] Every statute and regulation citation has been confirmed in the current version applicable to the matter `[deadline verification required]`.
- [ ] Every quotation has been checked against its source text and confirmed to be accurate and in context.
- [ ] Every defective (incomplete or malformed) citation has been corrected or removed.
- [ ] No date in the draft was computed by the agent; all dates are confirmed against source documents or attorney knowledge `[deadline verification required]`.
- [ ] No authority has been accepted as verified on the basis of model background knowledge alone.
- [ ] All items on the Unresolved Items List have been resolved and documented.
- [ ] The validation report and any corrections are retained as part of the matter file.
- [ ] The draft is appropriately labeled as draft legal work product for attorney review, not legal advice.
