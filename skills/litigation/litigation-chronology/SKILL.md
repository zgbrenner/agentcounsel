---
name: Litigation Chronology
description: Use when building a factual timeline for litigation from provided source documents, producing a structured chronology table with citations, disputed/undisputed flags, and gap analysis for attorney review.
---

# Litigation Chronology

## Purpose

Produce a structured, sourced factual chronology of events relevant to a litigation or dispute matter. Every event in the chronology is tied to a specific source document or Bates reference. The skill separates undisputed facts from disputed ones, flags evidentiary gaps, and never resolves or adjudicates a factual conflict. It produces draft legal work product for attorney review — not legal advice and not a statement of what happened.

## Use When

- A user asks to "build a timeline," "create a chronology," or "put the facts in order" from a set of documents.
- Counsel needs a fact-organized view of events across multiple documents, productions, or depositions.
- Pre-trial preparation requires organizing the documentary record by event date.
- A mediation brief, motion, or opening statement requires a supporting factual narrative grounded in the record.
- A second attorney is joining the matter and needs a document-grounded orientation to the facts.
- Discovery gaps or missing time periods need to be identified and flagged.

## Required Inputs

- One or more source documents (contracts, correspondence, emails, text messages, records, pleadings, deposition excerpts, discovery responses, or other materials). Do not build a chronology without source documents.
- Identification of each source document: document name, Bates range or other identifier, and date of the document if known.
- The matter name or a brief description of the dispute (to give the chronology appropriate context).
- The client's role (plaintiff, defendant, etc.) so that significance assessments can be framed appropriately.

If no source documents are provided, stop and request them. Do not populate the chronology from background knowledge, assumed facts, or the description of events alone.

## Do Not Use When

- No source documents have been provided (the chronology would be fabricated — do not proceed).
- The user needs an initial matter intake, not a document-based timeline (use `matter-intake`).
- The user needs a demand letter rather than a chronology (use `demand-letter`).
- The user is asking for a legal argument about what the facts mean — the chronology is a factual record, not a legal brief.
- The user needs a summary of tracked changes between document drafts (use `redline-summary`).

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Every event entered in the chronology must be supported by a specific source document. Record the document name and Bates number or page reference for each event.
- Do not infer, extrapolate, or assert events that are not explicitly supported by a provided document.
- Do not resolve factual disputes. When documents conflict, record both versions and mark the event as `[DISPUTED]`.
- Do not characterize a document's legal effect or admissibility — those are attorney determinations.
- Do not invent, guess, or fill in dates. If a date is uncertain or approximate, note that explicitly (e.g., "circa," "on or around," "date unclear — see [CONFIRM]").
- Distinguish the document's date from the event date if they differ.
- Do not quote documents inaccurately. Reproduce language verbatim or paraphrase and note that it is a paraphrase. Never misstate what a document says.
- Flag every gap in the timeline — missing periods, undocumented events, and anticipated documents not yet produced.
- Preserve confidentiality: the chronology itself is attorney work product. Limit distribution accordingly.

## Workflow

1. **Confirm inputs.** Verify that source documents have been provided and that each has been identified with a name or Bates reference. If documents are missing, stop and request them.

2. **Catalog source documents.** Create a source document list: Document Name | Bates Range / Identifier | Date of Document | Document Type (email, contract, invoice, deposition excerpt, etc.) | Produced by / Custodian. This list becomes the "Sources Reviewed" header in the chronology.

3. **Extract events from each document.** For each source document, extract every discrete event, communication, action, or statement that is relevant to the matter. Record:
   - The event date (from the document; flag if approximate or unclear).
   - The time, if stated in the document.
   - A concise description of the event.
   - A verbatim quote or accurate paraphrase of the supporting language, with page/Bates citation.
   - The actor(s) involved.

4. **Assign significance.** For each event, note its apparent significance to the claims or defenses at issue. Label significance as "High," "Medium," or "Low" and briefly explain (e.g., "High — date of alleged breach per Complaint ¶ 12"). Do not characterize legal effect.

5. **Flag disputed events.** Where two or more documents conflict on a fact, date, or description of events, record each version separately, cite each source, and mark the event as `[DISPUTED: see attorney note]`. Do not resolve the dispute or assert which version is correct.

6. **Identify gaps.** After extracting events, note time periods that are not covered by any provided document. Flag anticipated documents that have not been produced (e.g., "No emails from [date range] produced — gap in record"). Record each gap in the "Gaps and Missing Periods" section.

7. **Sequence all events.** Sort all extracted events into chronological order. Where a date is uncertain, place the event in the most probable position and flag it.

8. **Draft the chronology table.** Populate the chronology table using the template at `templates/chronology-table.md`. Every row must have a source citation. Rows without a citation must not be included.

9. **Compile open items.** List all events marked `[DISPUTED]`, all gaps, all approximate dates, and all events where the source document needs to be obtained or verified. These become the "Open Items for Attorney Verification" section.

10. **Label the output.** Mark the completed chronology as "Draft — Attorney Work Product — For Attorney Review Only." Note the sources reviewed, the date prepared, and that the chronology reflects only the documents listed.

## Output Format

Deliver a Litigation Chronology consisting of:

1. **Header Block** — Matter name, client and role, preparer, date prepared, sources reviewed (document catalog).
2. **Chronology Table** — Using the template at `templates/chronology-table.md`. Columns: Date | Time (if known) | Event Description | Source Document / Bates | Actor(s) | Significance | Disputed? | Attorney Note.
3. **Gaps and Missing Periods** — Bulleted list of time periods not covered and anticipated documents not produced.
4. **Open Items for Attorney Verification** — All `[DISPUTED]`, `[CONFIRM]`, and unresolved items requiring attorney review.
5. **Assumptions** — Any assumptions made about document dates, party identities, or event sequencing.

Every row in the chronology table must cite a source. The completed document must be labeled as draft attorney work product.

## Attorney Verification Checklist

- [ ] All source documents are identified and accounted for in the Sources Reviewed list.
- [ ] Every chronology entry cites a specific source document and page or Bates reference.
- [ ] No event has been included without documentary support.
- [ ] Disputed events are flagged and not resolved; both versions are recorded.
- [ ] Approximate dates are identified as such and not treated as established facts.
- [ ] Document dates and event dates are distinguished where they differ.
- [ ] All quotations accurately reproduce the source document language.
- [ ] Gaps and missing periods have been identified and flagged for follow-up discovery or production.
- [ ] The significance assessments reflect the current theory of the case — verify with lead counsel.
- [ ] The chronology has been reviewed for completeness against the full document production.
- [ ] The document is labeled as draft attorney work product and distribution is appropriately limited.
