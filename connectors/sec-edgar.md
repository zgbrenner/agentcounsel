# SEC EDGAR

> Reference material supporting the AgentCounsel skill library, used to help produce draft legal work product for attorney review — not legal advice.

This connector points at [SEC EDGAR](https://www.sec.gov/edgar), the U.S. Securities and Exchange Commission's Electronic Data Gathering, Analysis, and Retrieval system — the public filing system for registration statements, periodic and current reports, ownership reports, and other documents filed with the SEC. It documents the full-text-search and filing-retrieval surface a skill can consult to confirm that a filing **exists**, when it was **filed**, its **accession metadata**, and what a filing or exhibit **said as filed**.

The broader connector contract is in [`README.md`](README.md). See [`federal-register.md`](federal-register.md) and [`ecfr.md`](ecfr.md) for the companion connectors that verify SEC *rulemaking* documents and *codified* SEC regulations — this connector verifies *filings by registrants and reporting persons*, not the rules that required them.

## 1. Source

- **Publisher:** U.S. Securities and Exchange Commission (SEC).
- **Cost:** Free. Fully public — **no API key, no authentication required** for read access.
- **Surfaces:** EDGAR full-text search (`efts.sec.gov`), the submissions and XBRL JSON APIs (`data.sec.gov`), and the EDGAR document archive (`www.sec.gov/Archives/edgar/`). `[CONFIRM: endpoint currency against the live developer docs before integrating in a long-lived tool]`. Source: [SEC EDGAR APIs and developer resources](https://www.sec.gov/search-filings/edgar-application-programming-interfaces).
- **Coverage:** Electronic filings since EDGAR's phase-in in the early-to-mid 1990s (varies by form type and filer); **full-text search covers filings from 2001 onward** `[CONFIRM: current full-text-search coverage window]`. Paper-only historical filings are not in the system.
- **Output formats:** JSON for search and metadata; HTML, plain text, XBRL, and PDF for filed documents.
- **Rate limits:** The SEC publishes fair-access guidance — a declared `User-Agent` header identifying the requester, and a modest request rate (historically on the order of ten requests per second) `[CONFIRM: current fair-access guidance before any sustained workflow]`. Automated access that ignores the guidance is throttled or blocked.
- **License of returned content:** filings are public documents; SEC-hosted material is public-domain U.S. government work, though filed documents themselves are the registrants' text.

## 2. In scope — what SEC EDGAR can verify

- **That a filing exists** — a registration statement, periodic report (10-K/10-Q-style), current report (8-K-style), proxy statement, ownership report (Forms 3/4/5-style), exempt-offering notice (Form D-style), or other EDGAR-filed document by a named filer.
- **Filed date and accession metadata** — the accession number, filing date, acceptance datetime, form type, period of report, and filer identifiers (CIK, company name, ticker mapping) for a located filing.
- **The filed text of a filing or exhibit** — retrieve what the document said *as filed*, including exhibits (material contracts, charters, bylaws, indentures) attached to the filing.
- **Full-text search** — locate filings since roughly 2001 containing a phrase, term, or name, filtered by form type, date range, and filer.
- **A filer's filing history** — the sequence of a company's EDGAR submissions, including amendments (`/A` filings).
- **Reverse lookup** — map a company name or ticker to a CIK, and an accession number to its filing.

What "verify" means here: confirm the filing **exists**, that the **filed date and accession metadata match** what the draft asserts, that the **as-filed text** of a document or exhibit can be quoted and linked for attorney review, and that the **public URL** can be recorded. **Whether the filing was legally sufficient, timely, complete, or accurate is not what this connector confirms.** See Section 7.

## 3. Out of scope — what SEC EDGAR does not cover

A skill must keep its existing placeholder discipline for anything in this list:

- **Legal sufficiency, completeness, or accuracy of any disclosure.** EDGAR shows what was filed, not whether it satisfied any disclosure obligation. Adequacy is attorney work in every case.
- **Deadline computation.** EDGAR records when a filing *was* made; it does not establish when a filing *was due*, whether it was timely, or when the next one is required. Every due date remains `[deadline verification required]` — deadline calculation is always an attorney task.
- **The true state of beneficial ownership.** An ownership report records what a reporting person filed, not the actual or complete ownership position; unfiled or misfiled positions are invisible to EDGAR.
- **SEC rules, releases, and regulations.** Use [`federal-register.md`](federal-register.md) for rulemaking documents and [`ecfr.md`](ecfr.md) for codified SEC regulations.
- **State blue-sky filings and non-SEC regulators.** State notice filings, FINRA material, and exchange filings live elsewhere.
- **Documents not filed on EDGAR** — paper-only historical filings, confidentially submitted drafts, unredacted versions of documents filed with confidential-treatment redactions, and correspondence not released to the public file.
- **Materiality, interpretation, or characterization of any filed statement.** That is attorney work.

If a skill needs to verify any of the above, treat the connector as unavailable for that placeholder and retain the existing `[CONFIRM: ...]` flag.

## 4. Surface — where to hit

### 4a. Public web (no API)

- **Full-text search UI:** `https://efts.sec.gov/LATEST/search-index?q=...` backs the public UI at `https://www.sec.gov/edgar/search/`.
- **Company browse:** `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=<CIK-or-ticker>&type=<form-type>&count=40`
- **Filing index page pattern:** `https://www.sec.gov/Archives/edgar/data/<CIK>/<accession-number-no-dashes>/<accession-number>-index.htm`

Use this surface for: a browser visual confirmation, or environments without HTTP tooling. The filing index URL is what a verified entry should record.

### 4b. Full-text search API

The primary surface for locating filings by content:

- **Endpoint:** `https://efts.sec.gov/LATEST/search-index?q=<URL-encoded-query>` `[CONFIRM: endpoint path against current live docs]`.
- **HTTP method:** `GET`. Returns JSON.
- **Common parameters:** `q` (phrase queries in double quotes), `forms=<form-type>` (e.g., `10-K`), `dateRange` / explicit `startdt` and `enddt` date bounds, and entity filters `[CONFIRM: parameter names against current live docs]`.
- **Coverage:** filings from roughly 2001 onward only.

Use this for: locating a filing when the draft has a phrase, a topic, or a partial reference but no accession number.

### 4c. Submissions API — filer history and accession metadata

- **Endpoint pattern:** `https://data.sec.gov/submissions/CIK##########.json` (10-digit zero-padded CIK).
- **HTTP method:** `GET`. Returns JSON.
- **Returns:** filer metadata and the filing history — form types, filing dates, acceptance datetimes, accession numbers, primary documents, and period-of-report dates.
- **Ticker-to-CIK mapping:** `https://www.sec.gov/files/company_tickers.json`.

Use this when the question is "did this company file this form on this date" and for building the accession metadata a verified entry records.

### 4d. Document retrieval

- **Pattern:** `https://www.sec.gov/Archives/edgar/data/<CIK>/<accession-number-no-dashes>/<document-filename>`
- **Returns:** the as-filed document (HTML, text, or XBRL), including individual exhibits listed on the filing index page.

Use this for: quoting the filed text of a filing or exhibit, with the URL recorded for attorney review.

### 4e. XBRL data APIs

Structured financial-fact endpoints (`https://data.sec.gov/api/xbrl/companyconcept/...`, `.../companyfacts/...`) expose tagged figures from filings. They are rarely needed for citation verification; where a skill consults them, every figure remains a `[CONFIRM against the filing itself]` item — tagging errors occur.

### 4f. MCP tool surface

When the user's environment includes an MCP server that wraps EDGAR, prefer it over raw URL fetches. The connector contract is the same: query, record the verified filing URL and accession metadata, fall back to placeholder if unavailable. **This connector does not configure or install any MCP server** — see `connectors/README.md`.

## 5. Calling pattern from a skill

The skills that most often consult this connector are the securities-capital-markets skills — `skills/securities-capital-markets/sec-filing-consistency-check/SKILL.md`, `skills/securities-capital-markets/offering-document-disclosure-review/SKILL.md`, `skills/securities-capital-markets/risk-factor-review/SKILL.md`, `skills/securities-capital-markets/public-company-reporting-calendar-intake/SKILL.md`, and `skills/securities-capital-markets/section-16-beneficial-ownership-triage/SKILL.md` — plus the M&A and corporate diligence skills when the target or counterparty is a public company (e.g., `skills/m-and-a/acquisition-diligence-request-list/SKILL.md`, `skills/corporate/diligence-issue-extraction/SKILL.md`, `skills/corporate/material-contract-schedule/SKILL.md`, where material contracts filed as exhibits can be pulled as filed).

When a skill's Workflow reaches a filing reference it would otherwise mark `[CONFIRM: ...]` and the reference is in scope under Section 2:

1. **Resolve the filer.** Map the company name or ticker to a CIK (4c). If the filer cannot be resolved unambiguously, stop and retain the placeholder with a `multiple filer matches` note.
2. **Locate the filing.** If the draft has an accession number, fetch the filing index directly (4a/4d). Otherwise, search the submissions history by form type and date (4c) or full-text search by phrase (4b, 2001+ only).
3. **Check for amendments.** Look for later `/A` filings of the same form; a verified original may have been amended. Record any amendment found — never silently treat the original as the operative version.
4. **Branch on the result:**
   - **Exact match:** Record the filing in the deliverable with the filing index URL, accession number, form type, filed date, and period of report. Replace the `[CONFIRM: ...]` placeholder with `[ATTORNEY TO CONFIRM: EDGAR confirms existence and as-filed text only — sufficiency, accuracy, timeliness, and current status remain attorney items]`.
   - **Multiple matches:** Do not pick one. Record the candidates with their accession numbers and URLs and retain a `[CONFIRM: multiple EDGAR matches — attorney to select]` flag.
   - **No match:** Retain a `[CONFIRM: not found in EDGAR — attorney to verify the filing independently]` flag. Absence from EDGAR is not proof a document does not exist (paper filings, confidential submissions).
   - **Out of scope (per Section 3):** Keep the original placeholder. Do not use EDGAR to conclude a filing was due, timely, sufficient, or that an ownership position is complete.
5. **If the connector is unavailable:** retain the original placeholder unchanged. Add `[CONFIRM: not verified — no EDGAR connector available in this session]` so the attorney sees the gap.

## 6. Fallback behavior

| Outcome | Action |
|---|---|
| Single match | Record filing index URL + accession number + form type + filed date; mark `[ATTORNEY TO CONFIRM: existence and as-filed text only]`; note any `/A` amendment found |
| Multiple matches | List candidates with accession numbers; mark `[CONFIRM: multiple EDGAR matches — attorney to select]` |
| No match | Mark `[CONFIRM: not found in EDGAR — attorney to verify elsewhere]`; absence is not proof of non-existence |
| Out of scope per Section 3 | Retain the original placeholder; do not query |
| Connector unavailable | Retain the original placeholder; add `not verified — no EDGAR connector` note |

## 7. Limits and known failure modes

- **Filed is not sufficient, accurate, or timely.** A filing's presence on EDGAR confirms only that it was filed and accepted. It does not confirm the disclosure was adequate, the statements true, or the filing on time. All of those remain attorney-verification items.
- **Amendments and supersession.** Originals remain on EDGAR after amendment; a draft citing an original 10-K-style report may be citing superseded text. Always check for `/A` filings and later periodic reports.
- **Three dates, not one.** Filing date, acceptance datetime, and period of report differ; do not collapse them. Preserve each date the metadata returns and flag each `[CONFIRM date against source]` until the attorney verifies it.
- **Full-text search floor.** Full-text search reaches back only to roughly 2001; older filings must be located through the submissions history or browse surface, and pre-EDGAR paper filings are absent entirely.
- **Filer identity drift.** Companies change names, merge, and file under multiple CIKs (parent, subsidiaries, successor entities). A name search that misses the right CIK produces a false "not found."
- **Confidential-treatment redactions.** The as-filed text of an exhibit may be redacted; the public text is not the complete agreement.
- **Incorporation by reference.** Filings routinely incorporate exhibits from earlier filings; the document a draft needs may live under a different accession number than the filing that references it.
- **XBRL tagging errors.** Structured-data endpoints reflect filer tagging, which contains errors; confirm any figure against the filed document itself.
- **Fair-access throttling.** Requests without a declared `User-Agent`, or above the published rate guidance, are blocked; a blocked session is a "connector unavailable" outcome, not a "not found."

## 8. What this connector does not do

- Does not confirm that a disclosure was legally sufficient, complete, or accurate.
- Does not compute, confirm, or imply any filing deadline, timeliness determination, or reporting-calendar date — every due date stays `[deadline verification required]`.
- Does not establish the true or complete state of any beneficial-ownership position — only what was filed.
- Does not interpret filed documents, characterize their materiality, or apply them to a matter.
- Does not verify SEC rules or releases ([`federal-register.md`](federal-register.md)), codified regulations ([`ecfr.md`](ecfr.md)), case law ([`courtlistener.md`](courtlistener.md)), state filings, or anything never filed on EDGAR.

All of those remain attorney-verification items. The connector closes the "does this filing exist, filed by this entity, on this date, with this accession number and this as-filed text" question. Nothing more.
