# Congress.gov and GovInfo

> Reference material supporting the AgentCounsel skill library, used to help produce draft legal work product for attorney review — not legal advice.

This connector points at [Congress.gov](https://www.congress.gov), the Library of Congress's official portal for U.S. federal legislation, and its companion [GovInfo](https://www.govinfo.gov), the Government Publishing Office's repository of official government publications. Together they document the surface a skill can consult to confirm that a federal bill or resolution **exists**, what its current **status** and **committee history** are, whether its text is **enacted or still pending**, and the **public-law number** assigned once it is signed.

The broader connector contract is in [`README.md`](README.md). See [`federal-register.md`](federal-register.md) for the companion connector that verifies *agency rulemaking* published after a statute takes effect, and [`ecfr.md`](ecfr.md) for the *codified regulation* that implements it — this connector verifies the *legislative record itself*, not what an agency later did with the resulting law.

## 1. Source

- **Publisher:** Congress.gov is maintained by the Library of Congress in partnership with the Clerk of the House, the Secretary of the Senate, and GPO; GovInfo is maintained by the U.S. Government Publishing Office (GPO).
- **Cost:** Free. Fully public — **no API key required for Congress.gov's public site**; GovInfo's API requires a free, self-service API key. `[CONFIRM: current key requirement against the live developer docs before integrating in a long-lived tool]`.
- **Surfaces:** The public Congress.gov bill-tracking pages, the Congress.gov API (`api.congress.gov`), and GovInfo's bulk data and API (`api.govinfo.gov`), which carries the authoritative published text of bills, statutes, and the United States Code.
- **Coverage:** Congress.gov's bill-tracking data runs from the 93rd Congress (1973) forward, with full text search generally strongest from the 103rd Congress (1993) forward `[CONFIRM: current coverage window against the live docs]`. GovInfo's collections vary by publication type.
- **Output formats:** JSON for API responses; HTML, PDF, and XML for bill text and published statutes.
- **Rate limits:** Both APIs publish fair-use guidance and require a registered key for sustained use `[CONFIRM: current rate-limit guidance before relying on a sustained workflow]`.
- **License of returned content:** Legislative text and government publications are U.S. government works in the public domain.

## 2. In scope — what Congress.gov / GovInfo can verify

- **That a bill or resolution exists** — a numbered bill (e.g., `H.R. 1234`, `S. 567`) or resolution in a given Congress, and its short title and sponsor as introduced.
- **Bill status** — introduced, referred, reported, passed one chamber, passed both chambers, presented to the President, signed, vetoed, or became law without signature.
- **Committee actions** — referral, hearings held, markups, and reported-out status, as recorded in the bill's official actions list.
- **Enacted-vs-pending text** — whether the version a draft quotes is the introduced version, an amended version, an engrossed version, or the enrolled (final, enacted) version, and which of those the draft is actually citing.
- **Public-law number and enactment metadata** — once signed, the assigned public-law number (e.g., `Pub. L. No. 118-1`), the enactment date as recorded, and the Statutes at Large citation once published.
- **Companion and related bills** — cross-chamber companion bills and bills the record identifies as related.

What "verify" means here: confirm the bill or resolution **exists** under the asserted number and Congress, that its **recorded status matches** what the draft asserts, and that the **version of text quoted** can be identified and linked. **Whether the bill's substance means what the draft says it means, whether it will pass, or what its legal effect is once enacted, is not what this connector confirms.** See Section 7.

## 3. Out of scope — what Congress.gov / GovInfo does not cover

A skill must keep its existing placeholder discipline for anything in this list:

- **Legal effect or interpretation of any bill or enacted statute.** The connector confirms status and text; what a provision means or how a court would read it is attorney work in every case.
- **Deadline computation of any kind.** Session calendars, markup schedules, and floor votes shift constantly, and legislative "deadlines" (e.g., a stated effective date in a not-yet-enacted bill) are provisional until enactment. Every date remains `[deadline verification required]` — deadline calculation is always an attorney task, and this connector never predicts when a pending bill will move.
- **Whether a bill will pass, in what form, or on what timeline.** Legislative prediction is out of scope entirely.
- **Codified U.S. Code text as currently in force.** Once a bill is enacted, its provisions are eventually codified into the U.S. Code; this connector verifies the legislative record and the Statutes at Large citation, not the current codified section — `[CONFIRM: codification connector not yet documented in this library]`.
- **State and local legislation.** Congress.gov and GovInfo cover federal legislation only.
- **Regulatory action implementing a statute.** Use [`federal-register.md`](federal-register.md) and [`ecfr.md`](ecfr.md) for the agency-side record.
- **The substantive merits, policy wisdom, or constitutionality of any bill.**

If a skill needs to verify any of the above, treat the connector as unavailable for that placeholder and retain the existing `[CONFIRM: ...]` flag.

## 4. Surface — where to hit

### 4a. Public web (no API)

- **Bill page pattern:** `https://www.congress.gov/bill/<congress-ordinal>th-congress/<chamber>-bill/<number>` (e.g., `https://www.congress.gov/bill/118th-congress/house-bill/1234`).
- **All-actions and text tabs:** each bill page has an "All Actions" tab (committee and floor history) and a "Text" tab (every published version, with the enrolled version marked if enacted).

Use this surface for: a browser visual confirmation, or environments without HTTP tooling. The bill page URL is what a verified entry should record.

### 4b. Congress.gov API

- **Endpoint pattern:** `https://api.congress.gov/v3/bill/<congress>/<bill-type>/<number>` `[CONFIRM: endpoint path against current live docs]`.
- **HTTP method:** `GET`. Returns JSON.
- **Returns:** sponsor, introduction date, latest action, full actions list, committee referrals, related bills, and links to available text versions.
- **Search:** `https://api.congress.gov/v3/bill/<congress>?query=...` for locating a bill by keyword when the number is not in hand `[CONFIRM: search parameter names against current live docs]`.

Use this for: confirming current status, committee history, and the set of available text versions for a specific bill.

### 4c. GovInfo — authoritative published text

- **Endpoint pattern:** `https://api.govinfo.gov/collections/BILLS/...` and `https://api.govinfo.gov/collections/PLAW/...` (public laws) `[CONFIRM: exact collection paths against current live docs]`.
- **HTTP method:** `GET`. Requires an API key.
- **Returns:** the authoritative published text (introduced, engrossed, enrolled, or public-law versions) as PDF, XML, or text, plus the Statutes at Large citation once assigned.

Use this for: retrieving and quoting the actual text of a specific bill version, and for confirming the public-law number and Statutes at Large citation of an enacted bill.

### 4d. MCP tool surface

When the user's environment includes an MCP server that wraps Congress.gov or GovInfo, prefer it over raw URL fetches. The connector contract is the same: query, record the verified bill URL and status metadata, fall back to placeholder if unavailable. **This connector does not configure or install any MCP server** — see `connectors/README.md`.

## 5. Calling pattern from a skill

When a skill's Workflow reaches a reference to a federal bill, its status, or its enactment that it would otherwise mark `[CONFIRM: ...]` and the reference is in scope under Section 2:

1. **Resolve the bill.** Identify the Congress, chamber, and bill number from the draft. If any of these is missing or the bill cannot be resolved unambiguously by title alone, stop and retain the placeholder with a `bill not identified` note.
2. **Check current status.** Query the bill's status and actions (4b). Record the latest official action and its date exactly as recorded — do not paraphrase "signed" from "passed the Senate."
3. **Identify which text version the draft relies on.** Confirm whether the draft quotes the introduced, an amended, an engrossed, or the enrolled version, and retrieve the matching version (4c). A draft that quotes bill text without stating which version it is quoting is itself a defect to flag.
4. **If enacted, record the public-law number.** Confirm the assigned public-law number and, once available, the Statutes at Large citation (4c).
5. **Branch on the result:**
   - **Exact match:** Record the bill in the deliverable with the Congress.gov bill page URL, current status, the specific text version quoted, and (if enacted) the public-law number. Replace the `[CONFIRM: ...]` placeholder with `[ATTORNEY TO CONFIRM: Congress.gov/GovInfo confirms bill existence, recorded status, and text version only — legal effect, interpretation, and whether the cited version is still current remain attorney items]`.
   - **Multiple candidates:** Do not pick one. Record the candidates with their bill numbers and URLs and retain a `[CONFIRM: multiple Congress.gov matches — attorney to select]` flag.
   - **No match:** Retain a `[CONFIRM: not found in Congress.gov/GovInfo — attorney to verify the bill independently]` flag.
   - **Out of scope (per Section 3):** Keep the original placeholder. Do not use this connector to predict passage, compute a deadline, or confirm codified U.S. Code text.
6. **If the connector is unavailable:** retain the original placeholder unchanged. Add `[CONFIRM: not verified — no Congress.gov/GovInfo connector available in this session]` so the attorney sees the gap.

## 6. Fallback behavior

| Outcome | Action |
|---|---|
| Single match | Record bill page URL + status + text version + (if enacted) public-law number; mark `[ATTORNEY TO CONFIRM: existence, status, and text version only]` |
| Multiple candidates | List candidates with bill numbers and URLs; mark `[CONFIRM: multiple Congress.gov matches — attorney to select]` |
| No match | Mark `[CONFIRM: not found in Congress.gov/GovInfo — attorney to verify elsewhere]` |
| Out of scope per Section 3 | Retain the original placeholder; do not query |
| Connector unavailable | Retain the original placeholder; add `not verified — no Congress.gov/GovInfo connector` note |

## 7. Limits and known failure modes

- **Status is not passage, and passage is not enactment.** A bill "reported out of committee" is not "passed"; a bill that "passed the House" has not become law. Preserve the exact recorded status language rather than summarizing it into a stronger-sounding state.
- **Version drift.** Bill text changes at every stage — introduced, amended in committee, engrossed, enrolled. A quotation checked against the wrong version silently misstates what the enacted (or currently pending) text says.
- **No prediction of outcome or timing.** The connector records what has happened, never what will happen or when. Do not use status history to imply a bill is likely to pass or to estimate a timeline.
- **Public-law number lags signature.** There can be a short gap between a bill being signed and the public-law number and Statutes at Large citation being assigned and published; a very recent enactment may show as signed without a public-law number yet.
- **Codification lag.** An enacted statute is not immediately reflected in the codified U.S. Code; this connector does not track codification status at all — that is a separate, currently undocumented gap (Section 3).
- **Coverage floor.** Full-text search is markedly weaker before the 103rd Congress (1993); older legislative history may require a different research path.
- **API key friction (GovInfo).** GovInfo API requests without a valid key are blocked; a blocked session is a "connector unavailable" outcome, not a "not found."

## 8. What this connector does not do

- Does not confirm the legal effect, interpretation, or constitutionality of any bill or enacted statute.
- Does not compute, confirm, or imply any legislative deadline, markup date, floor-vote date, or effective date — every date stays `[deadline verification required]`.
- Does not predict whether, when, or in what form a pending bill will be enacted.
- Does not verify current codified U.S. Code text, agency rulemaking implementing a statute (`connectors/federal-register.md`), or codified federal regulations (`connectors/ecfr.md`).
- Does not cover state or local legislation.

All of those remain attorney-verification items. The connector closes the "does this bill exist, what is its recorded status, which text version is this, and what is its public-law number" question. Nothing more.
