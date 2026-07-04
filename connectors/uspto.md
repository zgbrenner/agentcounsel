# USPTO — Patents and Trademarks

> Reference material supporting the AgentCounsel skill library, used to help produce draft legal work product for attorney review — not legal advice.

This connector points at the public data of the [U.S. Patent and Trademark Office](https://www.uspto.gov) (USPTO) — **Patent Public Search** and PatentsView-style patent data for patents and published applications, and **TSDR** (Trademark Status & Document Retrieval) and the USPTO trademark search system for marks. It documents the surface a skill can consult to confirm that a **patent or published application exists** with a given number and what its **status metadata** is, that a **trademark registration or application exists** and what its **prosecution-status metadata** is, and what **assignment records** the office has recorded — all as facts on the public register, for attorney review.

The broader connector contract is in [`README.md`](README.md). This connector verifies **existence and status metadata only.** It does not interpret claim scope, assess validity, or reach any freedom-to-operate or infringement conclusion — those are attorney determinations the connector explicitly does not touch. See Sections 3 and 7.

## 1. Source

- **Publisher:** U.S. Patent and Trademark Office (USPTO), an agency of the U.S. Department of Commerce.
- **Cost:** Free. The public search surfaces are open to the public. Some programmatic APIs (notably TSDR) require a free USPTO-issued API key. `[CONFIRM: current API-key requirements before integrating in a long-lived tool]`.
- **Surfaces:** Patent Public Search (`ppubs.uspto.gov`), PatentsView / USPTO open patent data APIs, the Trademark Search system (`tmsearch.uspto.gov`), TSDR (`tsdr.uspto.gov`), and the Assignment Search systems (`assignment.uspto.gov`). `[CONFIRM: endpoint paths and product names against the live USPTO developer docs before relying on them — the USPTO has migrated these systems more than once]`.
- **Coverage:** Issued US patents and published US applications, and US trademark registrations and applications, with prosecution and assignment history. Coverage and the exact fields available vary by system and by era of the record.
- **Output formats:** HTML for the search UIs; JSON and XML for the APIs (TSDR returns status documents; PatentsView returns structured JSON).
- **Rate limits:** The USPTO publishes fair-access guidance and, for keyed APIs, per-key rate limits. `[CONFIRM: current fair-access guidance and per-key limits before any sustained workflow]`. Automated access that ignores the guidance is throttled or blocked.
- **License of returned content:** USPTO records are public records; the office's data is US government work. Patent and trademark documents themselves contain applicants' text and figures.

## 2. In scope — what USPTO data can verify

The USPTO public surfaces support verifying:

- **That a patent or published application exists** — an issued US patent or a published US application identified by **patent number**, **publication number**, or **application number** is on the register.
- **Patent status metadata** — issue date, publication date, filing/priority date as recorded, current legal status (e.g., active, expired, lapsed for non-payment where the system records it), and, where available, patent-term-adjustment and maintenance-fee-event data **as recorded by the office** — not as a computed expiration.
- **That a trademark registration or application exists** — a mark identified by **serial number** (application) or **registration number** is on the register, with the mark, the owner of record, the goods/services and international classes as filed, and the filing/registration dates.
- **Trademark prosecution-status metadata** — the current TSDR status (e.g., live/dead, registered, pending, abandoned, cancelled, suspended, in opposition) and the prosecution-history events **as recorded** by the office.
- **Assignment records** — recorded assignments of patents and of trademarks: the parties to a recorded assignment, the reel/frame or recordation number, and the recordation date, from the Assignment Search systems.
- **Reverse lookup** — map a patent/publication/application number or a trademark serial/registration number to its record, and an owner or assignee name to associated records (subject to the coverage limits below).

What "verify" means here: confirm that the **patent, application, or mark exists** on the register, that the **numbers, dates, owner of record, and status match** what the draft asserts, and that a **public URL or record identifier** can be recorded for attorney review. **Whether a patent is valid, what its claims cover, whether a product infringes or is free to operate, and whether a mark is registrable or confusingly similar are not what this connector confirms.** See Sections 3 and 7.

## 3. Out of scope — what USPTO data does not cover

A skill must keep its existing placeholder discipline for anything in this list:

- **Freedom-to-operate and infringement conclusions.** The register confirms that a patent exists and its status; it never establishes that a product is or is not blocked, that a mark is or is not infringing, or that anything is "clear to operate." Those are formal attorney determinations. Route them to the IP triage skills; do not draw them from a status lookup.
- **Claim scope and claim construction.** The recorded claim text can be retrieved, but interpreting what a claim covers — its scope, the meaning of its terms, the reach of the doctrine of equivalents — is attorney work the connector does not perform.
- **Validity and enforceability.** Issuance is not validity. Prior art, obviousness, enablement, inequitable conduct, and post-grant challenges are outside the register lookup; a granted patent may be invalid and an active registration may be vulnerable.
- **Trademark likelihood of confusion, distinctiveness, or registrability.** The register shows what is filed and its status; it does not judge whether a proposed mark is available, distinctive, or confusable with an existing mark. That is the clearance/triage attorney's work.
- **Any deadline computation.** Estimated patent expiration, maintenance-fee due dates, trademark renewal and Section-8/15 windows, response deadlines, and priority/bar dates are **never** computed here. The office may record dated events; deriving a due date or expiration from them is an attorney task. Every such date stays `[deadline verification required]`.
- **The complete or current chain of title.** Assignment Search shows recorded assignments; unrecorded transfers, security interests, licenses, and equitable interests are invisible. Ownership of record is not necessarily true beneficial ownership.
- **Foreign patents, applications, and marks.** This connector covers US records only. Foreign counterparts and international registrations are out of scope.

If a skill needs any of the above, treat the connector as unavailable for that placeholder and retain the existing `[VERIFY: ...]` / `[CONFIRM: ...]` / `[deadline verification required]` flag.

## 4. Surface — where to hit

### 4a. Patents — public search and data

- **Patent Public Search (UI):** `https://ppubs.uspto.gov/pubwebapp/` — the office's public search tool for issued patents and published applications.
- **PatentsView / open patent data API:** the USPTO's structured patent-data API (PatentsView) supports querying by patent number, dates, assignee, and other fields and returns JSON. `[CONFIRM: current base URL and query schema against the live PatentsView / USPTO Open Data Portal docs — the endpoint has moved]`.
- **Patent number / status:** confirm existence and recorded legal status of a patent or application by number.

Use this for: confirming that a patent number exists, its issue/publication/filing dates, its recorded status, and retrieving the recorded claim text for the attorney to construe (never for the skill to construe).

### 4b. Trademarks — TSDR and search

- **Trademark Search system (UI):** `https://tmsearch.uspto.gov/` — the office's public search for registered and applied-for marks (successor to the retired TESS).
- **TSDR (UI):** `https://tsdr.uspto.gov/` — status and document retrieval for a specific serial or registration number.
- **TSDR API pattern:** `https://tsdr.uspto.gov/ts/cd/casestatus/sn<serial-number>/info.json` (and the parallel `rn<registration-number>` form / XML variant) returns the case-status document. **Programmatic TSDR access requires a USPTO-issued API key.** `[CONFIRM: exact endpoint path and the current API-key header against the live TSDR API docs]`.

Use this for: confirming a mark's serial/registration number, its live/dead and prosecution status, the owner of record, and the goods/services and classes as filed.

### 4c. Assignments — patents and trademarks

- **Patent Assignment Search:** `https://assignment.uspto.gov/patent/` — recorded patent assignments.
- **Trademark Assignment Search:** `https://assignment.uspto.gov/trademark/` — recorded trademark assignments.
- Both expose recorded assignment parties, reel/frame or recordation numbers, and recordation dates.

Use this for: confirming that an assignment was **recorded** and its recorded parties and date — never for concluding that title is complete or that a recorded owner is the true current owner.

### 4d. MCP tool surface

When the user's environment includes an MCP server that wraps the USPTO patent or trademark APIs, prefer it over raw URL fetches — it handles authentication, keys, retries, and rate-limit backoff. The connector contract is the same: query, record the verified record URL and the numbers/dates/status, fall back to placeholder if unavailable. **This connector does not configure or install any MCP server** — see `connectors/README.md`.

## 5. Calling pattern from a skill

The skills that most often consult this connector are the **IP** skills — `skills/ip/fto-triage/SKILL.md`, `skills/ip/infringement-triage/SKILL.md`, `skills/ip/trademark-clearance-triage/SKILL.md`, and `skills/ip/invention-intake/SKILL.md`, plus the patent claim-chart skill `skills/litigation/claim-chart/SKILL.md`. Each consults it to confirm **that a patent, application, or mark exists** and **what its recorded status is, as a fact** — never to reach a freedom-to-operate, infringement, validity, or registrability conclusion, all of which remain attorney determinations.

When a skill's Workflow reaches a patent, application, or trademark reference it would otherwise mark `[VERIFY: ...]` or `[CONFIRM: ...]` and the reference is in scope under Section 2:

1. **Resolve the record.** For a patent, look up the patent/publication/application number (4a). For a mark, resolve the serial or registration number via TSDR (4b). For chain of title, query Assignment Search (4c).
2. **Branch on the result:**
   - **Exact match:** Record the record in the deliverable with the public URL or record identifier, the number(s), the recorded dates, the owner/assignee of record, and the recorded status. Replace the `[VERIFY: ...]` placeholder with `[ATTORNEY TO CONFIRM: USPTO confirms existence and recorded status only — validity, claim scope, FTO/infringement, registrability, chain of title, and any deadline remain attorney items]`. **Do not compute an expiration, renewal, or maintenance date, and do not draw an FTO/infringement/validity/registrability conclusion.**
   - **Multiple matches:** Do not pick one. Record the candidate records with their numbers and URLs and retain a `[CONFIRM: multiple USPTO records — attorney to select]` flag.
   - **No match:** Retain a `[VERIFY: not found in USPTO records — attorney to verify independently]` flag. Absence is not proof of non-existence (recent filings, indexing lag, foreign records, unrecorded transfers).
   - **Out of scope (per Section 3):** Keep the original placeholder. Never use the register to conclude validity, claim scope, FTO/infringement, registrability, complete title, or any due date.
3. **If the connector is unavailable:** retain the original placeholder unchanged. Add `[VERIFY: not verified — no USPTO connector available in this session]` so the attorney sees the gap.

Every date a skill records from this connector stays `[deadline verification required]` for any expiration, maintenance-fee, renewal, or response purpose. The connector confirms *what the office records*; it never computes a due date, and it never draws a legal conclusion about scope, validity, or infringement.

## 6. Fallback behavior

| Outcome | Action |
|---|---|
| Single match | Record record URL/identifier + number(s) + recorded dates + owner of record + status; mark `[ATTORNEY TO CONFIRM: existence and recorded status only — no FTO/infringement/validity/registrability conclusion, no deadline]` |
| Multiple matches | List candidate records with numbers; mark `[CONFIRM: multiple USPTO records — attorney to select]` |
| No match | Mark `[VERIFY: not found in USPTO records — attorney to verify elsewhere]`; absence is not proof of non-existence |
| Out of scope per Section 3 (validity, scope, FTO, registrability, deadline, title) | Retain the original placeholder / `[deadline verification required]`; do not query for a conclusion |
| Connector unavailable | Retain the original placeholder; add `not verified — no USPTO connector` note |

## 7. Limits and known failure modes

- **Issuance is not validity, and existence is not scope.** A patent's presence on the register confirms only that it issued or published; it says nothing about validity, enforceability, or what the claims cover. A registration's presence says nothing about its strength or vulnerability. These remain attorney-verification items.
- **Status lookups do not decide FTO, infringement, or registrability.** Confirming that a patent or mark exists is never a freedom-to-operate, infringement, or clearance conclusion. The IP triage skills exist precisely to keep those judgments with counsel.
- **No deadline is ever computed.** Recorded events (issue date, maintenance-fee events, registration date, renewal windows) are facts; expiration and due dates derived from them are attorney work. Every such date stays `[deadline verification required]`.
- **Recorded owner is not necessarily true owner.** Assignment Search shows recorded assignments only; unrecorded assignments, security interests, licenses, and equitable interests are invisible. Chain of title requires attorney diligence beyond the register.
- **Status and legal-status lag.** Recorded legal status (expired/lapsed/abandoned) can lag actual events, and maintenance-fee or renewal status may not reflect a very recent payment or grace-period cure. Confirm status as of a date and re-verify before reliance.
- **Number-format and family drift.** Patent, publication, and application numbers follow different formats and eras; continuations, divisionals, reissues, and foreign counterparts fragment a patent family. A mark can exist as multiple applications/registrations across classes and owners. A search that misses the right number or class produces a false "not found."
- **System migration and API drift.** The USPTO has migrated its search and data systems repeatedly (TESS retired; PatentsView/Open Data endpoints moved; TSDR added key requirements). Re-check the live developer docs before automating against any endpoint above.
- **US only.** Foreign patents, applications, and marks are out of scope; a clear US register is not a clear global position.

## 8. What this connector does not do

- Does not reach any freedom-to-operate, infringement, or "clear to operate" conclusion — those are formal attorney determinations (route to the IP triage skills).
- Does not construe claims, characterize claim scope, or assess the doctrine of equivalents.
- Does not assess validity, enforceability, or the strength of a patent or a trademark.
- Does not judge trademark likelihood of confusion, distinctiveness, or registrability.
- Does not compute, confirm, or imply any expiration, maintenance-fee, renewal, response, priority, or bar date — every such date stays `[deadline verification required]`.
- Does not establish complete or current chain of title — only what assignments were recorded.
- Does not verify foreign patents, applications, or marks.

All of those remain attorney-verification items. The connector closes the "does this patent, application, or mark exist, with this number, owner of record, and recorded status" question. Nothing more — never a scope, validity, infringement, or registrability conclusion, and never a deadline.
