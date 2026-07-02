# Education Overlay Profile

A sector configuration profile, in the same style as the files under `practice-profiles/`. It records how a team's work in **education** differs from the general case.

This profile is **not** legal work product and **not** legal advice. It is internal configuration. It must be reviewed and approved by a supervising attorney — ideally an education / student-privacy-specialist attorney — before it is loaded alongside any skill. Organization-specific values are left as `[ORGANIZATION TO FILL]` placeholders because this profile ships with the overlay scaffold, not with a specific organization's configuration.

The overlay's framework references (`OVERLAY.md`) are paired with this profile. The profile sets organization-specific positions; the OVERLAY.md sets sector-wide tuning. Both are subordinate to `core/` and to the supervising attorney.

---

## Sector and scope

- **Sector / client type:** education — school districts and public K-12 schools, charter and private schools, colleges and universities, ed-tech companies (B2B and consumer-facing), online-learning, tutoring, assessment, and student-information-system vendors, and the service providers serving any of the above.
- **In-scope activities:** privacy, contracts, employment, regulatory, and product-legal work coloured by student-education-records regimes (FERPA-style), children's-online-privacy regimes (COPPA-style), state student-data-privacy statutes as a category, anti-discrimination process regimes (Title IX-style), accessibility obligations, and mandatory-reporting duties `[Verify current law]` `[verify jurisdiction]`.
- **Out of scope:** specialist education work that routes to a separate practice — special-education / individualized-education-program (IDEA-style) analysis, student-discipline and student-due-process matters, financial-aid / federal-student-aid program compliance, accreditation, athletics-association compliance, tenure and academic-freedom matters, charter authorization, student- and exchange-visitor-visa immigration work, and grievance-process substantive determinations. The overlay surfaces these as routing flags; the work itself is performed by specialist counsel.

## Jurisdictions

- **Primary regulators / oversight bodies (referenced generically — confirm which apply):** the federal education agency and its civil-rights and student-privacy offices; the federal consumer-protection regulator (children's privacy and ed-tech representations); state education agencies and boards; state attorneys general; educator certification and licensing bodies; and, for private ordering, accreditors and athletics associations (non-governmental) `[Verify current law]` `[verify jurisdiction]`. This profile names none of them as authority and asserts no requirement.
- **Jurisdictions of typical concern:** **every U.S. state in which the organization operates, enrolls students, or serves institutional customers** — state student-data-privacy statutes, mandatory-reporting rules, background-screening mandates, and public-entity contracting constraints are jurisdiction-by-jurisdiction `[verify jurisdiction]`. Named focus jurisdictions, if any: `[ORGANIZATION TO FILL]`.
- **Jurisdictions requiring escalation to local or specialist counsel:** every state where a state student-data statute, mandatory-reporting question, certification-board matter, or public-procurement constraint is material; every non-U.S. jurisdiction where student or children's data will be transmitted, stored, or processed (transfer and minors-data analysis) `[verify jurisdiction]`.
- Sector-specific legal rules are always attorney-verification items. This profile does not state them, and states no age threshold, rights-transfer milestone, or deadline.

## Sector gates and escalation thresholds

Conditions that must stop the workflow and route the matter to specialist or supervising attorney before proceeding (mirroring `OVERLAY.md` Section 4):

- Suspected abuse or neglect of a minor, or any mandatory-reporting question — counsel immediately; duties are typically personal, non-delegable, and time-sensitive `[verify jurisdiction]` `[deadline verification required]`; no workflow may delay the question.
- A Title IX-style complaint, sexual-misconduct allegation, or grievance-process design question — specialist process counsel `[Verify current law]`.
- An education-agency complaint, program review, audit, or enforcement contact — preserve records; do not respond without counsel.
- A consumer-protection-regulator inquiry touching children's privacy or ed-tech representations — counsel.
- A confirmed or suspected breach involving student records or minors' data — multiple concurrent frameworks; surface immediately and do not compute deadlines `[Verify current law]` `[verify jurisdiction]`.
- A law-enforcement, immigration-enforcement, or subpoena request for student records — counsel before any response `[Verify current law]`.
- A health-and-safety-emergency disclosure question — counsel; the exception frameworks are narrow and fact-intensive `[Verify current law]`.
- An accessibility complaint, demand letter, or agency inquiry — accessibility counsel `[Verify current law]`.
- A special-education (IDEA-style) dispute or records question — special-education counsel.
- A student-records / health-privacy boundary question (school health services, counseling records, school telehealth) — specialist counsel `[Verify current law]`.
- Discipline of a licensed / certificated educator — labor and licensing counsel; certification-board reporting may attach `[verify jurisdiction]`.
- A product or feature directed to children, or evidence of substantial child use of a general-audience product — children's-privacy counsel before launch or continued operation `[Verify current law]`.
- Any request to identify, profile, or advertise to students — counsel `[Verify current law]` `[verify jurisdiction]`.

## Standard positions

These are the organization's default positions on recurring sector-specific issues. The overlay flags deviations; the supervising attorney confirms. All placeholders are deliberately left as `[ORGANIZATION TO FILL]` because the profile ships without an organization-specific config.

- **Data-sharing-addendum template:** `[ORGANIZATION TO FILL — addendum template name, version, last review date, state-mandated terms incorporated, acceptable fallback positions on deletion, sub-processors, and audit rights, owner.]`
- **School-official designation posture:** `[ORGANIZATION TO FILL — when a vendor is designated under a school-official-style framework; required direct-control and use-limitation language; approval owner.]`
- **Consent posture:** `[ORGANIZATION TO FILL — verifiable-parental-consent mechanism(s) for consumer channels; when school-consent-in-lieu is relied on; required documentation for each.]`
- **Age-screening posture:** `[ORGANIZATION TO FILL — age-assurance mechanics; under-age-discovery protocol (deletion, account conversion, notification).]`
- **Directory-information and media posture:** `[ORGANIZATION TO FILL — designated directory information; opt-out mechanic; clearance owner for media and photography uses involving students.]`
- **Advertising and profiling prohibition:** `[ORGANIZATION TO FILL — position on advertising, profiling, and product-improvement uses of student data; contract-enforcement mechanism.]`
- **Retention and deletion posture:** `[ORGANIZATION TO FILL — retention schedule for student data; deletion mechanics at contract end and on request; deletion-verification owner.]`
- **Subpoena and law-enforcement protocol:** `[ORGANIZATION TO FILL — intake owner for every request for student records; pre-disclosure review and notification steps; response-clearance owner.]`
- **Mandatory-reporting protocol:** `[ORGANIZATION TO FILL — who is trained as a mandatory reporter; internal escalation path that runs alongside (never instead of) the statutory duty; on-call counsel.]`
- **Grievance-process roles:** `[ORGANIZATION TO FILL — coordinator-style role holders; investigator / decision-maker staffing; outside-process-counsel threshold.]`
- **Accessibility posture:** `[ORGANIZATION TO FILL — adopted digital-accessibility conformance target; standard procurement clause; remediation owner.]`
- **Background-screening posture:** `[ORGANIZATION TO FILL — screening scope; re-screening cadence; vendor-personnel flow-down requirements for roles with student contact.]`
- **Breach chain of command:** `[ORGANIZATION TO FILL — who determines which frameworks a student-data incident triggers; who notifies institutions, parents, and regulators; incident-response retainer relationships.]`
- **State-of-operations list:** `[ORGANIZATION TO FILL — every state in which the organization operates, enrolls students, or serves institutional customers, for state-statute and mandatory-reporting analysis.]`

## Heightened-handling rules

The following data categories, populations, or document types require heightened confidentiality and care, in addition to general student-data handling:

- **All data of minors** — heightened sensitivity regardless of which regime formally applies; consent-authority and rights-holder questions surface before any disclosure `[Verify current law]` `[verify jurisdiction]`.
- **Special-education and disability records** — added regimes and added sensitivity; route substantive questions to special-education counsel.
- **School-held health and counseling records** — sit at a contested boundary with health-privacy regimes; route boundary questions to specialist counsel `[Verify current law]`.
- **Disciplinary records and grievance-process files** — process-regime constraints and privacy sensitivity; restrict access.
- **Free-and-reduced-lunch and family financial data** — program-specific confidentiality expectations `[Verify current law]`.
- **Immigration-status information** — heightened sensitivity; route any enforcement-adjacent request to counsel immediately.
- **Biometric data (proctoring, identification)** — state biometric statutes may attach on top of student-data regimes `[verify jurisdiction]`.
- **Mandatory-reporting and abuse-allegation material** — restrict access; route immediately; never summarize into a general-circulation deliverable.
- **Records of minors involved in investigations or litigation** — preservation-and-access controls apply on top of general handling.

## Prohibited assumptions

The agent must never assume any of the following in education matters; each must be surfaced for human confirmation:

- **That any regime applies or does not apply** — student-records, children's-privacy, state student-data statute, anti-discrimination process, or accessibility regime — to any entity, product, or dataset. Always an attorney determination `[Verify current law]` `[verify jurisdiction]`.
- **Whether a mandatory-reporting duty has been triggered, satisfied, or excused.** Always counsel, immediately `[verify jurisdiction]`.
- **Who holds rights over a minor's records** (parent, eligible student, guardian, non-custodial parent). Always surfaced; custody orders route to counsel.
- **That any disclosure exception applies** (directory information, school-official, health-and-safety emergency, subpoena) to a specific disclosure. Always counsel `[Verify current law]`.
- **Any age threshold, rights-transfer milestone, or consent age.** Each is `[Verify current law]` `[verify jurisdiction]`; the overlay never states one.
- **That a product is or is not child-directed**, or that an age-screening mechanism satisfies any regime. Always counsel `[Verify current law]`.
- **That a consent mechanism (parental or school-in-lieu) is valid** for a given use. Always counsel `[Verify current law]`.
- **That a vendor's data use is permitted** under a school-official designation, contract, or statute. Always surfaced against the actual instrument.
- **Compliance with any accessibility standard or conformance level.** Always accessibility counsel and technical assessment `[Verify current law]`.
- **The required shape of any grievance process.** The process architecture is heavily amended and litigated `[Verify current law]`; always specialist counsel.
- **Any deadline** — reporting windows, records-request response times, grievance timelines, breach notifications. Triggering-fact dates are `[deadline verification required]`; the timing frameworks are `[Verify current law]` `[verify jurisdiction]`.
- **The state of the law in any jurisdiction.** Always `[verify jurisdiction]` and specialist counsel where the jurisdiction is material.

## Source-of-truth documents

These are referenced by name and location; **do not paste** the documents themselves into this profile or any deliverable. The organization fills in the location.

- **Student-data-sharing addendum template (current version):** `[ORGANIZATION TO FILL]`
- **Annual student-records notification and directory-information notice:** `[ORGANIZATION TO FILL]`
- **Children's-privacy notice and consent-mechanism documentation:** `[ORGANIZATION TO FILL]`
- **Ed-tech vendor inventory and addendum-status tracker:** `[ORGANIZATION TO FILL]`
- **State student-data-statute register (per operating state):** `[ORGANIZATION TO FILL]`
- **Mandatory-reporting protocol and training records:** `[ORGANIZATION TO FILL]`
- **Grievance-procedure documents and role assignments:** `[ORGANIZATION TO FILL]`
- **Accessibility conformance target, audit results, and remediation plan:** `[ORGANIZATION TO FILL]`
- **Background-screening policy and vendor flow-down terms:** `[ORGANIZATION TO FILL]`
- **Records-retention schedule for student data:** `[ORGANIZATION TO FILL]`
- **Incident-response plan and breach-determination protocol:** `[ORGANIZATION TO FILL]`
- **Subpoena / law-enforcement request protocol and log:** `[ORGANIZATION TO FILL]`
- **Specialist-counsel contact list** — student-privacy, Title IX-style process, special-education, accessibility, labor / certification, children's-privacy, immigration: `[ORGANIZATION TO FILL]`

## Attorney review

The following must be reviewed by a supervising attorney — and, where the matter requires, by a sector specialist — before any deliverable produced with this overlay is used, sent, or relied upon:

- **Student-privacy counsel** — every data-sharing addendum, school-official designation, consent-mechanism design, records-request response, and student-data breach analysis.
- **Children's-privacy counsel** — every child-directed determination, consent-mechanism question, and consumer-facing product launch touching children's data.
- **Title IX-style process counsel** — every grievance-process design question and every investigation intersecting the process regime.
- **Special-education counsel** — every matter touching IDEA-style records, plans, or disputes.
- **Accessibility counsel** — every accessibility complaint, conformance representation, and procurement-clause question.
- **Labor / certification counsel** — every educator-discipline matter, collective-bargaining question, and certification-board reporting question `[verify jurisdiction]`.
- **State-by-state local counsel** — every matter where a state student-data statute, mandatory-reporting rule, or public-procurement constraint is material and the supervising attorney is not admitted in the state `[verify jurisdiction]`.
- **On-call counsel for mandatory-reporting questions** — immediately, in every case, before any other workflow step.

No deliverable produced with this overlay is final until the relevant specialist has reviewed it. The overlay's status remains `experimental` until a supervising education-counsel reviewer has confirmed the framework references, the per-skill tuning notes have been exercised on at least one real matter, and the `[ORGANIZATION TO FILL]` placeholders have been completed.
