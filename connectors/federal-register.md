# Federal Register

> Reference material supporting the AgentCounsel skill library, used to help produce draft legal work product for attorney review — not legal advice.

This connector points at [Federal Register](https://www.federalregister.gov), the daily journal of the US federal government, run by the Office of the Federal Register at the National Archives and Records Administration. It documents the v1 REST API surface a skill can consult to confirm that a Federal Register document — a final rule, proposed rule, notice, or presidential document — actually exists with the citation and publication date the draft asserts.

The broader connector contract is in [`README.md`](README.md). See [`ecfr.md`](ecfr.md) for the companion connector that verifies the *codified* current text of a regulation (CFR), as distinct from the *published* document this connector verifies.

## 1. Source

- **Publisher:** Office of the Federal Register, National Archives and Records Administration (NARA).
- **Cost:** Free. Fully public — **no API key, no authentication required** for read access.
- **API version:** v1. Base URL: `https://www.federalregister.gov/api/v1/`. `[CONFIRM: API version currency before integrating in a long-lived tool]`.
- **Coverage:** All Federal Register contents since 1994, including executive orders and all Public Inspection documents made available prior to publication. Source: [Federal Register API Documentation](https://www.federalregister.gov/developers/documentation/api/v1).
- **Output formats:** JSON, CSV, and JSONP. JSON is the working format for skills.
- **Rate limits:** Not stated as a hard published limit on the public docs. `[CONFIRM: live rate-limit guidance before relying on a sustained workflow]`.
- **License of returned content:** Federal Register documents are US government works in the public domain.

## 2. In scope — what Federal Register can verify

- **Final rules** (`type=RULE`) — published agency rules with full preamble, regulatory text, effective date, and compliance date.
- **Proposed rules** (`type=PRORULE`) — notices of proposed rulemaking (NPRMs) with comment-period dates.
- **Notices** (`type=NOTICE`) — agency notices that are not themselves rules: meetings, information collections, sunshine-act notices, enforcement actions, etc.
- **Presidential documents** (`type=PRESDOCU`) — executive orders, presidential memoranda, and proclamations as published in the FR.
- **Public Inspection documents** — pre-publication items made available before formal publication.
- **Per-document basics** — document number, document type, agency, title, publication date, effective date, comment deadline (where applicable), Federal Register citation (volume / page), and the HTML and PDF URLs to the published document.
- **Reverse search** — given a citation, title fragment, or document number, locate the matching document.

What "verify" means here: confirm the document **exists**, that the **citation form matches** what the Federal Register publishes, and that the **public URL** can be recorded for attorney review. **Whether the document remains operative — superseded, stayed, vacated, or amended by a later FR action — is not what this connector confirms.** See Section 7.

## 3. Out of scope — what Federal Register does not cover

A skill must keep its existing placeholder discipline for anything in this list:

- **The current codified text of a regulation.** A final rule in the Federal Register is the *publication* of a rulemaking; what is *currently in effect* lives in the Code of Federal Regulations and may differ from the rule as originally published (subsequent amendments, corrections, stays). Use [`connectors/ecfr.md`](ecfr.md) instead.
- **Federal Register contents before 1994.** Earlier volumes exist in print and in some bulk archives, but are not in the v1 API.
- **State-level regulatory publications.** Each state has its own register; this connector does not cover them.
- **Substantive interpretation, agency guidance not published in the FR, or enforcement actions that did not appear in the FR.**
- **The legal effect of a rule** — final published rules can be vacated, stayed, enjoined, or superseded; the API does not record that status.
- **Pinpoint accuracy of regulatory text inside very long rules** — quotations against the rule text remain attorney-verification items.

If a skill needs to verify any of the above, treat the connector as unavailable for that placeholder and retain the existing `[CONFIRM: ...]` flag.

## 4. Surface — where to hit

### 4a. Public web search (no API)

- **Search URL pattern:** `https://www.federalregister.gov/documents/search?conditions[term]=<URL-encoded-query>`
- **Document page URL pattern:** `https://www.federalregister.gov/documents/<YYYY>/<MM>/<DD>/<document-number>/<slug>`

Use this surface for: a quick browser visual confirmation, or environments without HTTP tooling. The document page URL is also what a verified entry should record.

### 4b. Documents search API

The primary search surface for skills:

- **Endpoint:** `https://www.federalregister.gov/api/v1/documents.json`
- **HTTP method:** `GET`.
- **Filtering with `conditions[...]`:** parameters are namespaced under `conditions`. Examples:
  - `conditions[term]=<URL-encoded-query>` — full-text search.
  - `conditions[type][]=RULE` — filter by document type. Values include `RULE` (Final Rule), `PRORULE` (Proposed Rule), `NOTICE` (Notice), `PRESDOCU` (Presidential Document).
  - `conditions[agencies][]=<agency-slug>` — filter by agency (e.g., `environmental-protection-agency`).
  - `conditions[publication_date][gte]=<YYYY-MM-DD>` / `conditions[publication_date][lte]=<YYYY-MM-DD>` — filter by publication date range.
  - `conditions[president]=<president-slug>` — for `PRESDOCU` searches.
- **Example:** `https://www.federalregister.gov/api/v1/documents.json?conditions[term]=cybersecurity+disclosure&conditions[type][]=RULE&conditions[publication_date][gte]=2024-01-01`
- **Customization:** the API allows specifying which fields to return for performance; results are paginated.

Use this for: locating a document by topic, agency, date window, or document type, when the citation is partial or not in hand.

### 4c. Single-document fetch

For pulling the full record of a specific FR document:

- **Endpoint pattern:** `https://www.federalregister.gov/api/v1/documents/<document_number>.json`
- **HTTP method:** `GET`.
- **Returns:** document metadata, agencies, publication date, effective date, citation, full text URLs (HTML, PDF, XML), comment-period information for proposed rules, and (where applicable) topics, CFR references, and presidential metadata.

Use this when the draft already has a document number (e.g., `2024-12345`) and the question is whether it exists and what its operative dates are.

### 4d. Public Inspection documents endpoint

For documents not yet formally published:

- **Endpoint pattern:** `https://www.federalregister.gov/api/v1/public-inspection-documents.json`
- **HTTP method:** `GET`.
- **Use for:** verifying that a draft is on public inspection but not yet published, or that a document the user has does not yet have a final FR citation.

### 4e. Agencies, suggested-searches, and other endpoints

Additional v1 endpoints expose agency lists, public-inspection issues, and suggested searches. They are not commonly needed for citation verification; consult the live docs (Section 1) when needed.

### 4f. MCP tool surface

When the user's environment includes an MCP server that wraps the Federal Register API, prefer it over raw URL fetches. The connector contract is the same: query, record the verified document URL, fall back to placeholder if unavailable. **This connector does not configure or install any MCP server** — see `connectors/README.md`.

## 5. Calling pattern from a skill

When a skill's Workflow reaches a Federal Register citation it would otherwise mark `[CONFIRM: ...]` and the citation is in scope under Section 2:

1. **Look up the document.** If the draft has a document number, use the single-document endpoint (4c). Otherwise, search by citation, title fragment, or agency + date via the search endpoint (4b).
2. **Branch on the result:**
   - **Exact match:** Record the document in the deliverable (e.g., "Summary of Provided Document," "Rule Change Summary," or the equivalent in the skill) with the public document page URL, the FR citation, agency, publication date, and effective date. Replace the `[CONFIRM: ...]` placeholder with `[ATTORNEY TO CONFIRM: rule still operative — Federal Register confirms publication only]`.
   - **Multiple matches:** Do not pick one. Record the candidates with their URLs and retain a `[CONFIRM: multiple Federal Register matches — attorney to select]` flag.
   - **No match:** Retain a `[CONFIRM: not found in Federal Register — attorney to verify the citation independently]` flag.
   - **Out of scope (per Section 3):** Keep the original placeholder. Do not use the API to confirm codified regulation text (use eCFR instead) or to confirm a rule's current operative status.
3. **If the connector is unavailable:** retain the original placeholder unchanged. Add `[CONFIRM: not verified — no Federal Register connector available in this session]` so the attorney sees the gap.

## 6. Fallback behavior

| Outcome | Action |
|---|---|
| Single match | Record verified URL + citation + dates; mark `[ATTORNEY TO CONFIRM: rule still operative]` |
| Multiple matches | List candidates; mark `[CONFIRM: multiple FR matches — attorney to select]` |
| No match | Mark `[CONFIRM: not found in Federal Register — attorney to verify elsewhere]` |
| Out of scope per Section 3 | Retain the original placeholder; do not query |
| Connector unavailable | Retain the original placeholder; add `not verified — no Federal Register connector` note |

## 7. Limits and known failure modes

- **Publication is not status.** A document being in the Federal Register confirms only that it was published. Final rules can be vacated by a court, stayed by an agency, withdrawn before effective date, or superseded by later FR action; the API does not record that. Treat operative status as an attorney-verification item.
- **Effective vs. compliance dates.** Many rules distinguish an effective date from one or more compliance dates. Do not collapse them; preserve every date the API returns and flag each as `[CONFIRM date against source]` until the attorney verifies it.
- **Comment-period dates drift.** For proposed rules, comment periods can be extended or reopened by subsequent FR notices. A confirmed NPRM citation does not confirm the comment period is still open.
- **Pre-1994 coverage.** The API does not cover pre-1994 Federal Register contents. Older citations must be verified through another source.
- **Agency slugs and document-type codes may evolve.** The slugs documented above (e.g., `environmental-protection-agency`, `RULE`/`PRORULE`/`NOTICE`/`PRESDOCU`) are the published values at the time of writing. Consult the live API documentation before automating against them.

## 8. What this connector does not do

- Does not confirm what a regulation currently says. That belongs to [`ecfr.md`](ecfr.md).
- Does not confirm that a rule is still in effect, unstayed, unvacated, or unsuperseded.
- Does not interpret rule text or characterize its scope or applicability.
- Does not characterize agency enforcement posture, settled penalty ranges, or guidance documents not published in the FR.

All of those remain attorney-verification items. The connector closes the "does this Federal Register document exist with this citation, by this agency, on this date" question. Nothing more.
