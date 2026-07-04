# PACER / RECAP

> Reference material supporting the AgentCounsel skill library, used to help produce draft legal work product for attorney review — not legal advice.

This connector points at the federal courts' docket record — **PACER** (Public Access to Court Electronic Records), the official but paywalled system run by the Administrative Office of the U.S. Courts, and the **RECAP Archive** and **RECAP API** on [CourtListener](https://www.courtlistener.com), the [Free Law Project](https://free.law)'s free mirror of PACER documents that users have contributed. It documents the surface a skill can consult to confirm that a federal **docket exists**, that a **docket entry or filing** is on the record, its **docket number**, and the **date a document was filed** — as facts recorded on the docket, for attorney review.

The broader connector contract is in [`README.md`](README.md). See [`courtlistener.md`](courtlistener.md) for the companion connector that verifies **case-law opinions** on CourtListener — this connector verifies **dockets and filings** (the RECAP corpus), not published opinions, and neither verifies a deadline.

## 1. Source

- **Publisher:** PACER is operated by the Administrative Office of the U.S. Courts. The RECAP Archive and the RECAP API are operated by the Free Law Project (a US-based nonprofit), which redistributes PACER documents that its users have downloaded and contributed.
- **Cost:**
  - **PACER** is **paywalled.** Access requires a registered PACER account and, for most documents, per-page fees. PACER credentials and billing are the user's responsibility; this connector does not provision them.
  - **RECAP** is **free for read access** on CourtListener. No API key is required to begin; an account is recommended for higher rate tiers. RECAP holds only what has already been contributed — it is a partial mirror, not a complete copy of PACER.
- **API version:** RECAP is served through the CourtListener REST API — current **v4**, base URL `https://www.courtlistener.com/api/rest/v4/`. `[CONFIRM: API version currency before integrating in a long-lived tool]`. See [`courtlistener.md`](courtlistener.md) Section 1 for shared rate-limit and versioning notes.
- **Rate limits:** The RECAP endpoints share the CourtListener limits (unauthenticated requests are capped; free accounts have daily caps; a per-minute throttle applies). `[CONFIRM: current rate limits before relying on a sustained workflow]`.
- **License of returned content:** Federal docket sheets and filings are public court records. The Free Law Project's own metadata and database are licensed by them under permissive terms. `[CONFIRM: applicable Free Law Project terms before redistribution]`.

This connector documents the **free RECAP read surface** as the working tier for a skill. It does not automate paid PACER retrieval; where a document is not in RECAP, obtaining it from PACER is an attorney/paralegal task performed with the firm's own PACER account.

## 2. In scope — what PACER / RECAP can verify

For federal **district**, **appellate** (circuit courts of appeals), and **bankruptcy** courts, the RECAP corpus and the surface this connector documents support verifying:

- **That a case exists** — a federal docket with a given case name and **docket number** (e.g., `1:21-cv-00123`), in a named court, is on the record.
- **That a docket entry exists** — a numbered entry on the docket sheet (a motion, order, notice, complaint, answer, etc.), with the **entry number** and the **date the entry was filed** as recorded on the docket.
- **That a document is available in RECAP** — the PDF or text of a filed document that a RECAP contributor has already uploaded, with a stable URL to record for attorney review.
- **Docket metadata** — case name, court, assigned judge (where recorded), nature-of-suit and cause codes (where recorded), and the parties and counsel listed on the docket sheet.
- **A party's filing history within a case** — the sequence of docket entries as they appear on the docket sheet.
- **Reverse lookup** — map a docket number or case name to its RECAP docket, and a RECAP document to its docket entry.

What "verify" means here: confirm that the **docket or filing exists** on the record, that the **docket number and filed date match** what the draft asserts, and that a **public RECAP URL** can be recorded. **Whether a filing was legally sufficient, whether it was timely, and when anything is or was due are not what this connector confirms.** See Sections 3 and 7.

## 3. Out of scope — what PACER / RECAP does not cover

A skill must keep its existing placeholder discipline for anything in this list:

- **Any deadline computation or timeliness judgment.** A filed date on a docket is a record of *when a document was filed* — never a determination of when anything *was due*, whether a filing was *timely*, or when a response, objection, bar date, or hearing deadline *runs*. Every due date remains `[deadline verification required]` — deadline calculation is always an attorney task. This connector does not compute, confirm, or imply a deadline under any circumstance.
- **Legal sufficiency, completeness, or effect of any filing.** The docket shows what was filed and what the court entered; it does not establish that a filing satisfied any requirement, that a motion will be granted, or that an order has a particular legal effect. Adequacy and effect are attorney work in every case.
- **Sealed, restricted, or ex parte filings.** Sealed entries, restricted documents, and materials not on the public docket are not in RECAP and are not confirmable here. Absence is not evidence they do not exist.
- **Documents not yet in RECAP.** RECAP holds only what a user has contributed. A docket entry can exist on PACER and have no document in RECAP; a "not found" in RECAP is **not** proof the filing does not exist — it may simply be unmirrored (obtain it from PACER).
- **State-court dockets.** RECAP is a federal-court archive. State trial and appellate dockets are out of scope; see [`state-courts.md`](state-courts.md) for state-court coverage, which is itself partial and does not cover most trial-court records.
- **Case-law opinions and their citations.** Verifying that a published opinion exists with a given reporter citation belongs to [`courtlistener.md`](courtlistener.md), not this connector.
- **The current status or posture of a case.** RECAP reflects the docket as of the last contribution; whether a case is open, stayed, closed, or on appeal today is an attorney-verification item.

If a skill needs to verify any of the above, treat the connector as unavailable for that placeholder and retain the existing `[CONFIRM: ...]` / `[deadline verification required]` flag.

## 4. Surface — where to hit

### 4a. Public web (no API)

- **RECAP Archive UI:** `https://www.courtlistener.com/recap/` — browse and search contributed federal dockets and documents.
- **Docket page URL pattern:** `https://www.courtlistener.com/docket/<docket-id>/<slug>/`
- **PACER Case Locator (official, account required):** `https://pcl.uscourts.gov/` — the official index of federal cases across courts, used to confirm a docket number when RECAP has no copy. Retrieving documents there incurs PACER fees.

Use this surface for: a browser visual confirmation of a docket, sharing a stable RECAP URL with the attorney, or confirming a docket number on PACER when RECAP lacks it.

### 4b. RECAP search API — the primary lookup surface

- **Endpoint:** `https://www.courtlistener.com/api/rest/v4/search/?type=r&q=<URL-encoded-query>` (the `type=r` parameter selects the RECAP / dockets result type). `[CONFIRM: parameter names against the live Search API docs — they change with API minor versions]`.
- **HTTP method:** `GET`. Returns JSON.
- **Common filters:** court, docket number, case name, date-filed range, party, and assigned judge. The Free Law Project recommends sending an `OPTIONS` request to any endpoint to discover the current filter set.

Use this for: locating a docket by case name, docket number, court, or party when the exact RECAP docket id is not in hand.

### 4c. Dockets, docket-entries, and RECAP-documents endpoints

For structured retrieval once a docket is identified:

- **Docket record:** `https://www.courtlistener.com/api/rest/v4/dockets/<docket-id>/` — case name, court, docket number, assigned judge, parties, and metadata.
- **Docket entries:** `https://www.courtlistener.com/api/rest/v4/docket-entries/?docket=<docket-id>` — the numbered entries with their recorded filed dates.
- **RECAP documents:** `https://www.courtlistener.com/api/rest/v4/recap-documents/` — the contributed PDFs/text tied to entries, with URLs to record. `[CONFIRM: exact endpoint paths and query parameters against the live docs]`.

Use this when the question is "does this docket entry exist and what date was it filed," and for recording the docket number, entry number, filed date, and document URL a verified entry needs.

### 4d. RECAP Fetch — paid PACER retrieval (out of the free surface)

CourtListener exposes a `recap-fetch` endpoint that purchases a document or docket **from PACER** using the requester's own PACER credentials, incurring PACER fees. This is **not part of the free read surface** and is not invoked by a skill automatically. Treat any need for it as an attorney/paralegal action performed deliberately with the firm's PACER account.

### 4e. MCP tool surface

When the user's environment includes an MCP server that wraps CourtListener/RECAP, prefer it over raw URL fetches — it handles authentication, retries, and rate-limit backoff. The connector contract is the same: query, record the verified docket/document URL and the docket number and filed date, fall back to placeholder if unavailable. **This connector does not configure or install any MCP server** — see `connectors/README.md`.

## 5. Calling pattern from a skill

The skills that most often consult this connector are the **litigation** skills — `skills/litigation/subpoena-triage/SKILL.md`, `skills/litigation/discovery-response-workflow/SKILL.md`, `skills/litigation/litigation-chronology/SKILL.md`, and `skills/litigation/matter-intake/SKILL.md` — and the **bankruptcy-restructuring** skills — `skills/bankruptcy-restructuring/bankruptcy-deadline-tracker-intake/SKILL.md`, `skills/bankruptcy-restructuring/proof-of-claim-checklist/SKILL.md`, and `skills/bankruptcy-restructuring/automatic-stay-issue-spotter/SKILL.md`. Each consults it to confirm **that a case or docket exists** and that a **filing's date is on the record as a fact** — never to compute, infer, or confirm a deadline.

When a skill's Workflow reaches a case, docket, or filing reference it would otherwise mark `[CONFIRM: ...]` and the reference is in scope under Section 2:

1. **Locate the docket.** If the draft has a docket number, search by it and court (4b) or fetch the docket record (4c). Otherwise search by case name and party (4b).
2. **Locate the entry.** Retrieve the docket entries (4c) and identify the specific entry by number or description. Confirm the **filed date as recorded on the docket** — record it as a docket fact, not as a computed or operative date.
3. **Branch on the result:**
   - **Exact match:** Record the docket in the deliverable with the RECAP docket URL, the docket number, the court, the entry number, and the recorded filed date. Replace the `[CONFIRM: ...]` placeholder with `[ATTORNEY TO CONFIRM: RECAP confirms the docket entry and its recorded filed date only — timeliness, sufficiency, and any deadline remain attorney items]`. **Do not derive any due date from the filed date.**
   - **Multiple matches:** Do not pick one. Record the candidate dockets with their numbers and URLs and retain a `[CONFIRM: multiple RECAP dockets — attorney to select]` flag.
   - **No match:** Retain a `[CONFIRM: not found in RECAP — attorney to verify on PACER]` flag. Absence from RECAP is not proof the filing does not exist; it may be unmirrored, sealed, or on PACER only.
   - **Out of scope (per Section 3):** Keep the original placeholder. Never use this connector to conclude a filing was due, timely, or sufficient, and never to compute a bar date, response deadline, objection deadline, or hearing date.
4. **If the connector is unavailable:** retain the original placeholder unchanged. Add `[CONFIRM: not verified — no PACER/RECAP connector available in this session]` so the attorney sees the gap.

Every date a skill records from this connector stays `[deadline verification required]` for any due-date, response, or bar-date purpose. The connector confirms *when a document was filed as the docket records it*; it never establishes when anything is due.

## 6. Fallback behavior

| Outcome | Action |
|---|---|
| Single match | Record RECAP docket URL + docket number + court + entry number + recorded filed date; mark `[ATTORNEY TO CONFIRM: docket entry and filed date only — no deadline implied]` |
| Multiple matches | List candidate dockets with numbers; mark `[CONFIRM: multiple RECAP dockets — attorney to select]` |
| No match | Mark `[CONFIRM: not found in RECAP — attorney to verify on PACER]`; absence is not proof of non-existence |
| Out of scope per Section 3 (incl. any deadline question) | Retain the original placeholder / `[deadline verification required]`; do not query for a due date |
| Connector unavailable | Retain the original placeholder; add `not verified — no PACER/RECAP connector` note |
| Rate-limit reached | Treat as unavailable for the remainder of the session; flag in Open Items |

## 7. Limits and known failure modes

- **Filed is not due, timely, or sufficient.** A docket entry's presence confirms only that a document was filed and entered. It does not confirm the filing was timely, the deadline that governed it, or that it satisfied any requirement. Every deadline stays `[deadline verification required]`; this connector never computes one.
- **RECAP is a partial mirror.** RECAP contains only documents users have contributed. A docket may be incomplete, an entry may have no document, and a recent filing may not appear for some time. A "not found" means "not in RECAP," not "does not exist."
- **Contribution lag and staleness.** A RECAP docket reflects the state as of the last contribution, which may be weeks or months old. Do not infer current case status from a stale docket.
- **Sealed and restricted material is invisible.** Sealed entries and restricted documents do not appear; their absence proves nothing.
- **Docket-number and court ambiguity.** The same numeric docket number exists in many districts; always pair a docket number with its court. Related cases, consolidated cases, and multidistrict litigation can fragment a matter across dockets.
- **Filed date vs. entry date vs. service date.** The date a document was filed, the date the clerk entered it, and any service date can differ. Preserve whichever date the docket records and flag each `[CONFIRM date against source]`; never collapse them into a deadline.
- **PACER fees and credentials.** Retrieving anything not already in RECAP requires the firm's own PACER account and incurs fees; automated PACER purchase is out of the free surface documented here.
- **API surface drift.** The Free Law Project is actively developing v4; endpoint paths and filter names change with minor versions. Re-check the live docs (`/help/api/rest/`) before automating against them.

## 8. What this connector does not do

- Does not compute, confirm, or imply any deadline, bar date, response date, objection deadline, or hearing date — every due date stays `[deadline verification required]`.
- Does not confirm that a filing was timely, legally sufficient, complete, or that any motion or order has a particular effect.
- Does not confirm the current status or posture of a case.
- Does not reach sealed, restricted, or ex parte filings, documents not contributed to RECAP, or any state-court docket (see [`state-courts.md`](state-courts.md)).
- Does not verify case-law opinions or their citations (see [`courtlistener.md`](courtlistener.md)).
- Does not interpret a filing, characterize its significance, or apply it to a matter.

All of those remain attorney-verification items. The connector closes the "does this federal docket or filing exist, with this docket number, in this court, filed on this recorded date" question. Nothing more — and never a deadline.
