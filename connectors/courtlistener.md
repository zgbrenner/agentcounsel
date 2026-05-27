# CourtListener

> Reference material supporting the AgentCounsel skill library, used to help produce draft legal work product for attorney review — not legal advice.

This connector points at [CourtListener](https://www.courtlistener.com), the [Free Law Project](https://free.law)'s open database of US case law. It is the first concrete connector under `connectors/`; the broader framing is in [`README.md`](README.md).

The Free Law Project explicitly frames the Citation Lookup endpoint documented here as a guardrail "to help prevent hallucinated citations" (source: [Citation Lookup and Verification API](https://www.courtlistener.com/help/api/rest/citation-lookup/)). That is the use case this connector enables for an AgentCounsel skill — closing the gap between "I left a `[VERIFY-CITE: ...]` placeholder" and "I confirmed the case exists with that citation in a reliable corpus."

## 1. Source

- **Publisher:** Free Law Project (a US-based nonprofit). CourtListener is a research-and-disclosure project, not a commercial legal research vendor.
- **Cost:** Free for read access. No API key required to begin; an account is recommended for monitoring and higher tiers.
- **API version:** Current is **v4** (v4.4 at the time this doc was written). The base URL is `https://www.courtlistener.com/api/rest/v4/`. Older versions exist but should not be relied on for new work; consult the [V4 Migration Guide](https://www.courtlistener.com/help/api/rest/v4/migration-guide/) before using anything older. `[CONFIRM: API version currency before integrating in a long-lived tool]`.
- **Rate limits** (per the Free Law Project's published limits at the time this doc was written): up to **5,000 requests per hour** for unauthenticated users; **5,000 requests per day** for free accounts; the API documentation also notes a **60-requests-per-minute** throttle. Limits are noted as in flux pending a new membership model. `[CONFIRM: current rate limits before relying on a sustained workflow]`. Source: [REST API overview](https://www.courtlistener.com/help/api/rest/) and the Free Law Project's [discussion on limits](https://github.com/freelawproject/courtlistener/discussions/6895).
- **License of returned content:** CourtListener opinions are US public-domain court records; the Free Law Project's own metadata and database are licensed by them under permissive terms. `[CONFIRM: applicable Free Law Project terms before redistribution]`.

This connector documents the **free, mostly no-key surface**. CourtListener also exposes PACER-derived data and paid features; both are out of scope here.

## 2. In scope — what CourtListener can verify

CourtListener's corpus and the surface this connector documents support verifying:

- **US Supreme Court opinions** — full historical corpus.
- **US Courts of Appeals** — federal appellate decisions across all circuits.
- **US District Courts** — selective coverage of district-court opinions.
- **State courts of last resort** — varying coverage by state; many state supreme courts are present, with coverage lag and gaps that vary by jurisdiction. Treat state coverage as partial unless a specific state has been confirmed.
- **Bankruptcy, tax, and specialty federal courts** — partial coverage.
- **Per-opinion basics** — case name, citation(s), court, date, judges, and full opinion text where the opinion is published.
- **Citator-style relationships** — what other opinions cite a given opinion (the "OpinionsCited" graph).
- **Reverse citation lookup** — given a citation string, locate the matching opinion(s). The Citation Lookup endpoint parses citations using [Eyecite](https://github.com/freelawproject/eyecite), which the project says was developed against more than 50 million citations going back more than two centuries.

What "verify" means here: confirm that the cited case **exists**, that the **citation form matches** what CourtListener has on record, and that the **public URL** for the opinion can be recorded for attorney review. **Verifying that the opinion stands for the proposition for which it is cited is not the connector's job — that is attorney work.**

## 3. Out of scope — what CourtListener does not cover

A skill must keep its existing placeholder discipline for anything in this list:

- **Many state intermediate appellate and trial court opinions** — coverage is partial and varies by state.
- **Unpublished or sealed proceedings** — not in the public corpus.
- **Very recent decisions** — coverage lag varies; new opinions appear on a delay.
- **Secondary sources** — treatises, restatements, law review articles, practice guides.
- **Statutes, regulations, court rules, and agency guidance** — CourtListener's primary focus is case law. Statutory verification belongs to a different connector.
- **Foreign and international tribunals** — out of scope. Use a jurisdiction-specific connector when one is added.
- **Pinpoint accuracy of internal page numbers in older volumes** — verify pinpoint cites against the official reporter.

If a skill needs to verify any of the above, treat the connector as unavailable for that placeholder and retain the existing `[VERIFY-CITE: ...]` / `[CONFIRM: ...]` flag.

## 4. Surface — where to hit

### 4a. Public web search (no API)

The simplest surface, available in any browser or HTTP-capable tool:

- **Search URL pattern:** `https://www.courtlistener.com/?q=<URL-encoded-query>`
- **Opinion page URL pattern:** `https://www.courtlistener.com/opinion/<opinion-id>/<slug>/`

Use this surface for: quick visual confirmation of a case, sharing a stable URL with the attorney, or environments without HTTP tooling.

### 4b. Citation Lookup API — the primary verification surface

The most reliable way to resolve a citation string to a specific opinion:

- **Endpoint:** `https://www.courtlistener.com/api/rest/v4/citation-lookup/`
- **HTTP method:** `POST` (not GET).
- **Input modes (per the [Citation Lookup docs](https://www.courtlistener.com/help/api/rest/citation-lookup/)):** the API can look up either a single individual citation or parse and look up every citation in a block of text.
- **Hard limits:** at most **250 citations per request** (excess parsed but returned with a `status` value indicating "Too many citations requested"); at most **64,000 characters** of text per request.
- **Response shape (per the official docs):** each match returns a `citation` (the looked-up form), `normalized_citations` (canonical form(s); multiple entries when ambiguous), `start_index` and `end_index` (positions of the citation in the input text), and a `status` field (`200` indicates a found and valid match).
- **Authentication:** uses the same auth and serialization as the rest of the CourtListener API; works unauthenticated subject to the rate limits in Section 1.

This is the endpoint a skill should hit when resolving a `[VERIFY-CITE: ...]` placeholder. The Eyecite-backed parsing handles ambiguous and non-canonical citation forms that a plain string match would miss.

### 4c. Search API

For richer queries (court filter, date range, case-name search):

- **Endpoint:** `https://www.courtlistener.com/api/rest/v4/search/`
- **HTTP method:** `GET` with query parameters, e.g., `?q=<query>`.
- **Supported filters** (consult the live [Search API docs](https://www.courtlistener.com/help/api/rest/search/) for the current list): query text, document type, court filter, date filed range. `[CONFIRM: exact filter parameter names against the live docs — they change with API minor versions]`. The Free Law Project recommends sending an `OPTIONS` request to any endpoint to discover the current filter set.

Use this for: locating a case by partial information when only a name or topic is known, narrowing within a specific court or date window.

### 4d. Opinion fetch

For pulling the full text of a verified opinion:

- **Endpoint pattern:** `https://www.courtlistener.com/api/rest/v4/opinions/<opinion-id>/`
- **HTTP method:** `GET`.
- **Use for:** confirming that a paraphrase or quotation matches the source text. Confirming the quotation exists in the opinion is a structural check; the legal weight of the quoted passage remains an attorney determination.

### 4e. MCP tool surface

When the user's environment includes an MCP server that wraps CourtListener (community wrappers exist; check the user's installed MCP servers), prefer the MCP tool surface over raw URL fetches — it handles authentication, retries, and rate-limit backoff. The connector contract is the same: query, record the verified URL, fall back to placeholder if unavailable. **This connector does not configure or install any MCP server** — see `connectors/README.md`.

## 5. Calling pattern from a skill

When a skill's Workflow reaches a citation it would otherwise mark `[VERIFY-CITE: ...]` or `[CONFIRM: ...]`, and the citation is in scope under Section 2:

1. **Look up the citation.** For a citation string in a draft, `POST` to the Citation Lookup endpoint (4b). For a case-name or topic-based lookup, use the Search endpoint (4c).
2. **Branch on the result:**
   - **Exact match (single result):** Record the case in the Authorities Cited table (or equivalent) with the CourtListener opinion URL appended, e.g., `Erie R.R. Co. v. Tompkins, 304 U.S. 64 (1938) — verified via CourtListener: https://www.courtlistener.com/opinion/<id>/erie-railroad-co-v-tompkins/`. Replace the `[VERIFY-CITE: ...]` placeholder with `[ATTORNEY TO CONFIRM: proposition supported by the cited case]` — the citation now exists; whether it stands for the asserted proposition is still attorney work.
   - **Multiple matches:** Do not pick one. Record all matches, retain the `[VERIFY-CITE: multiple matches in CourtListener — attorney to select]` flag, and escalate.
   - **No match:** Retain a `[VERIFY-CITE: not found in CourtListener — attorney to verify in another source]` flag. Do not delete the asserted citation; the attorney needs to see what was claimed.
   - **Out of scope (per Section 3):** Keep the original placeholder. Do not query CourtListener for state intermediate appellate cases or non-case-law authority and treat absence-of-result as a verification.
3. **If the connector is unavailable** (no MCP tool, no HTTP capability, rate-limit exceeded): retain the original placeholder unchanged. Add `[VERIFY-CITE: not verified — no CourtListener connector available in this session]` so the attorney sees the gap.

The Output Format of any skill that consumes this connector should record the verification source per authority — see the per-skill changes in `skills/legal-research/legal-research-memo/SKILL.md`, `skills/litigation/brief-section-drafter/SKILL.md`, and `skills/litigation/claim-chart/SKILL.md`.

## 6. Fallback behavior

| Outcome | Action |
|---|---|
| Single match | Record verified URL; mark `[ATTORNEY TO CONFIRM: proposition supported]` |
| Multiple matches | List all; mark `[VERIFY-CITE: multiple matches — attorney to select]` |
| No match | Mark `[VERIFY-CITE: not found in CourtListener — attorney to verify elsewhere]` |
| Out of scope per Section 3 | Retain the original placeholder; do not query |
| Connector unavailable | Retain the original placeholder; add `not verified — no CourtListener connector` note |
| Rate-limit reached | Treat as unavailable for the remainder of the session; flag in Open Items |

## 7. Limits and known failure modes

- **Coverage lag.** New opinions appear with a delay. A citation that does not appear today may appear next week. Do not infer that absence in CourtListener means a case was not decided.
- **State coverage is partial.** A negative result for a state court should be read as "not in CourtListener," not as "does not exist."
- **Citation form drift.** Older citations, parallel citations, and unconventional formats can return false negatives. The Citation Lookup endpoint's Eyecite parser handles many such forms; for stubborn cases, try both the volume-page form (`304 U.S. 64`) and the case name (`Erie v. Tompkins`).
- **Pinpoint citations.** Confirming the case exists is not confirming a pinpoint page or paragraph. Pinpoints remain attorney-verification items.
- **Cited-but-not-quoted propositions.** A case being real does not mean the proposition asserted in the draft is supported by the case. That determination remains with the attorney.
- **Versioning.** Opinions can be revised; en banc rehearings and amended opinions can change pin cites. Record the date of the verification and re-verify before reliance on a sensitive citation.
- **API surface drift.** The Free Law Project is actively developing v4; minor versions add and rename filters. Treat the URLs and parameter names above as the shape *at the time this doc was written* and re-check the live docs (`/help/api/rest/`) before automating against them.

## 8. What this connector does not do

- Does not verify statutes, regulations, court rules, or secondary sources.
- Does not validate that a case is still good law (Shepardizing / KeyCiting is a separate operation that this free surface does not perform).
- Does not characterize a holding, the level of generality of a holding, or the precedential weight of a case in a particular court.
- Does not assess whether a case is binding, persuasive, or distinguishable in the operative forum.

All of those remain attorney-verification items. The connector closes the "does this case exist with this citation" question. Nothing more.
