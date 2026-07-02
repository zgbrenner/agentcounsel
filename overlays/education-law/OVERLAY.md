# Education Overlay

This overlay tunes AgentCounsel's existing skills for **education** work — school districts and public K-12 schools, charter and private schools, colleges and universities, ed-tech companies (B2B and consumer-facing), online-learning, tutoring, assessment, and student-information-system vendors, and the service providers that serve any of them. It is internal configuration material, not legal advice and not legal work product. A supervising attorney reviews it before use.

Education is a sector, not a body of law. An education client's legal work is privacy work, contracts work, employment work, regulatory work, and product-legal work — coloured by student-education-records regimes, children's-online-privacy regimes, the presence of minors as data subjects, anti-discrimination process obligations, accessibility obligations, and mandatory-reporting duties. This overlay supplies that colouring; it never replaces the underlying skills, the `core/` operating rules, or the supervising attorney.

---

## 1. Scope of the overlay

### Skills this overlay tunes

The overlay is most often loaded alongside skills in these clusters:

- **Privacy** — DPA review (becomes a student-data-sharing-addendum review when education records are involved), Privacy Impact Assessment for flows involving minors, DSAR workflow against parent / eligible-student access regimes, privacy-policy gap review for school- and child-facing notices.
- **Contracts** — ed-tech vendor agreements and data-sharing addenda, vendor-agreement inventory, contract risk review.
- **Employment** — employee-policy review (mandatory reporting, background screening, staff interaction with minors), internal investigations that intersect Title IX-style grievance processes.
- **Regulatory** — enforcement-risk memos and compliance gap matrices against education-agency and consumer-protection oversight.
- **Product legal** — terms-of-service review and launch review for child- and student-directed products.

The per-skill tuning notes appear in Section 3 below.

### What the overlay is NOT

- It does **not** contain skills. Per `overlays/README.md`, overlays never contain skills.
- It does **not** replace specialist education counsel — student-privacy counsel, Title IX-style process counsel, special-education counsel, accessibility counsel, immigration counsel (student and exchange-visitor visas), labor counsel for unionized educator workforces, and higher-education regulatory counsel all remain required for their respective domains.
- It does **not** provide special-education / individualized-education-program (IDEA-style) analysis, student-discipline or student-due-process guidance, financial-aid / federal-student-aid program compliance, accreditation analysis, athletics-association compliance, tenure or academic-freedom analysis, or charter-authorization guidance. Each of those areas has its own framework that an education specialist must apply `[verify jurisdiction]`.
- It does **not** state the requirements of any student-records, children's-privacy, anti-discrimination, accessibility, or mandatory-reporting regime. Every regime reference in this overlay is a framework reference, not a statement of law `[Verify current law]`.
- It does **not** conclude whether any institution, vendor, product, or dataset is within scope of any regime — scope determinations are fact-intensive attorney determinations.
- It does **not** state any age threshold, consent age, or rights-transfer age. Those vary by regime and jurisdiction and change over time; each is `[Verify current law]` `[verify jurisdiction]`.
- It does **not** compute deadlines — including mandatory-reporting windows, grievance-process timelines, records-request response times, or breach-notification dates. Every date is `[deadline verification required]`.

---

## 2. The education regulatory architecture (orientation only — not legal advice)

This section orients an agent loading the overlay. None of it is a statement of law. Every framework reference carries `[Verify current law]` because education regimes are funding-conditioned, jurisdiction-layered, and amended on their own rulemaking cycles — several of the process regimes below have been substantially rewritten more than once in recent years `[Verify current law]`.

### 2.1 Who is regulated, and under what

The first question in most education matters is *what kind of entity is this, and which regimes attach to it?* This is fact-intensive and is an attorney determination — the overlay never concludes regime applicability.

- **Educational institutions and agencies receiving public funding** — student-education-records regimes, anti-discrimination process regimes, and accessibility obligations commonly attach as conditions of funding; whether and how they attach turns on the funding, the institution type, and the jurisdiction `[Verify current law]` `[verify jurisdiction]`.
- **Ed-tech vendors serving institutions** — vendors that receive education records may operate under a school-official-style designation, under contract-mandated terms, or under direct statutory obligations imposed by state student-data-privacy statutes `[Verify current law]` `[verify jurisdiction]`. The vendor's classification drives what the contract must say and what the vendor may do with the data.
- **Operators of child-directed online services** — consumer-facing products directed to children, or with actual knowledge of child users, may be captured by children's-online-privacy regimes with verifiable-parental-consent frameworks `[Verify current law]`. The child-directed determination is fact-intensive and an attorney determination.
- **Employers of educators and staff who work with minors** — background-screening mandates, licensure and certification regimes, and mandatory-reporting duties attach to the workforce `[verify jurisdiction]`.

### 2.2 The principal regimes (framework level only)

Each regime has substantial substantive content beyond what is sketched here; the overlay surfaces the framework so a supervising attorney can apply the current text of the applicable rule. None of the following states an age, a timeline, or a threshold.

**Student-education-records regimes (FERPA-style)** — consent-based frameworks governing disclosure of education records, conditioned on public funding `[Verify current law]`. Principal framework elements:
- An "education record" definition that is fact-intensive at the margins (sole-possession notes, law-enforcement-unit records, employment records, treatment records) — classification is an attorney determination.
- Rights held by parents that transfer to the student at a defined age or enrollment milestone `[Verify current law]` — the overlay never states the milestone.
- Consent-based disclosure with enumerated exception categories — commonly including school-official designations, directory information subject to notice and opt-out, health-and-safety emergencies, judicial orders and subpoenas with their own notification frameworks, and studies / audit / evaluation pathways `[Verify current law]`. Whether any exception applies is an attorney determination in every case.
- Access, amendment, and hearing rights for parents / eligible students; annual-notification obligations.
- Enforcement in many frameworks runs through the education agency and funding conditions rather than private suits `[Verify current law]` — enforcement posture is an attorney-verification item.

**Children's-online-privacy regimes (COPPA-style)** — frameworks governing collection of personal information from children by online services `[Verify current law]`. Principal framework elements:
- A child-directed / actual-knowledge scope determination — fact-intensive; audience analysis, content signals, and empirical evidence all figure in.
- Verifiable-parental-consent frameworks with enumerated consent mechanisms; in the school context, some frameworks recognize consent obtained through the school for education-only uses — a constrained pathway with its own limits `[Verify current law]`.
- Notice, data-minimization, retention-limit, and deletion frameworks; restrictions on conditioning participation on excess collection.
- The age threshold defining a "child" is regime-specific and changes with rulemaking; the overlay never states it `[Verify current law]`.
- Age-screening and age-assurance mechanics are themselves regulated design questions that create their own data-protection issues.

**State student-data-privacy statutes (as a category)** — many states regulate ed-tech providers and institutions directly, commonly including advertising and profile-building prohibitions, deletion obligations, contract-term mandates, security requirements, and breach frameworks `[verify jurisdiction]`. The category is state-by-state work; the overlay names no state's statute as authority and asserts no requirement.

**Anti-discrimination and Title IX-style process regimes** — funding-conditioned frameworks prohibiting discrimination on protected bases in education programs, with mandated grievance procedures `[Verify current law]`. Principal framework elements:
- Designated coordinator roles, notice obligations, and published grievance procedures.
- Defined process architecture (intake, supportive measures, investigation, decision-making, appeal) whose required shape has been substantially rewritten in successive rulemaking cycles and is actively litigated — a heavy `[Verify current law]` item in every matter.
- Intersection with employment: when a respondent or complainant is an employee, the education-process regime and employment law run in parallel and neither displaces the other.
- Parallel protected-basis regimes (race, national origin, disability, age) with their own process frameworks `[Verify current law]`.

**Accessibility obligations** — disability-rights regimes reaching physical facilities, digital content and platforms, instructional materials, and procurement `[Verify current law]`. Principal framework elements:
- Obligations attaching to institutions directly and flowing to vendors by contract.
- Digital-accessibility technical standards referenced through regulation, guidance, or settlement practice — the operative standard and conformance level are `[Verify current law]` items.
- Accommodation processes for students and employees, which are individualized, interactive, and jurisdiction-inflected `[verify jurisdiction]`.

**Mandatory-reporting regimes** — educators and school staff are commonly designated mandatory reporters of suspected child abuse or neglect `[verify jurisdiction]`. Principal framework elements:
- Who must report, what triggers the duty, to whom the report runs, and how fast are jurisdiction-specific `[verify jurisdiction]`; timing is `[deadline verification required]`.
- Reporting duties are typically personal and non-delegable — an institution's internal review does not substitute for an individual's statutory duty `[verify jurisdiction]`.
- The overlay never advises whether, when, or to whom to report. Any mandatory-reporting question routes to counsel immediately (Section 4).

### 2.3 Minors as data subjects — heightened-sensitivity handling

Minors' data runs through nearly every education matter and carries heightened sensitivity regardless of which regime formally applies:

- **Consent and authority** — who may consent, access, or direct deletion for a minor is regime- and jurisdiction-specific, and parental rights shift at age or enrollment milestones `[Verify current law]` `[verify jurisdiction]`. Surface the authority question; never assume the answer.
- **Heightened categories within student data** — disability and special-education records, school-held health and counseling records (which sit at a contested boundary with health-privacy regimes), disciplinary records, free-and-reduced-lunch and family financial data, immigration status, and biometric data (proctoring, identification) each carry added sensitivity and, frequently, added regimes `[verify jurisdiction]`.
- **Profiling and advertising** — building profiles of students or targeting advertising at them is prohibited or restricted under multiple regimes in the category `[Verify current law]` `[verify jurisdiction]`; surface every such use.
- **Retention and deletion** — expectations for minors' data trend shorter and stricter; deletion pathways at contract end are a recurring contract term.

### 2.4 Terminology an agent should recognize and use precisely

These terms recur in education matters and carry specific meanings. The overlay does not redefine them; use them as the law and the sector use them, and confirm with counsel when the substantive meaning matters.

- **Education record, directory information, sole-possession notes** — student-records-regime terms of art.
- **Parent / eligible student** — the rights-holder distinction that shifts at a defined milestone `[Verify current law]`.
- **School-official designation / legitimate educational interest** — the vendor- and staff-access framework under student-records regimes.
- **Verifiable parental consent, child-directed, actual knowledge, age screening** — children's-online-privacy terms of art.
- **Student-data-privacy statute, data-sharing addendum (DSA / DPA-for-schools)** — the state-statute category and its contract instrument.
- **Title IX-style coordinator, supportive measures, grievance procedure** — anti-discrimination-process terms of art.
- **Accommodation, accessible-technology conformance, digital-accessibility standard** — accessibility terms.
- **Mandatory reporter** — a jurisdiction-defined personal reporting duty `[verify jurisdiction]`.
- **SIS (student information system), LMS (learning management system), roster data, proctoring** — ed-tech document and data types.
- **IEP / 504-style plan** — special-education instruments; routing flags to specialist counsel, never analyzed by this overlay.
- **FERPA, COPPA, PPRA, IDEA, Title IX** — regime names an agent will encounter; each is a framework reference only, never a statement of current law `[Verify current law]`.

---

## 3. Per-skill tuning notes

For each skill in the affected clusters below, the overlay names the specific education-layer concerns a supervising attorney should add to the standard review. The overlay does not alter the skill; it adds attorney-verification items.

### Skill: `skills/privacy/dpa-review/SKILL.md`

**Overlay considerations:**

- **Treat as a student-data-sharing addendum** when education records or student data are involved — the generic DPA framework is supplemented by student-records-regime terms (permitted purposes limited to the educational function, school-official-style designation language, no advertising or profile-building, deletion at contract end, parent-access cooperation) `[Verify current law]` `[verify jurisdiction]`.
- **State-statute contract mandates** — several states mandate specific contract terms for ed-tech agreements; confirm the addendum against the applicable state's checklist `[verify jurisdiction]`.
- **Sub-processor flow-down** — every sub-processor touching student data should carry the same restrictions; surface flow-down gaps.
- **Training and product-improvement use** — a vendor's "we use customer data to improve our services" clause is a flagged gap when the inputs are student or children's data; surface for counsel.
- **Breach terms** — student-data breaches may trigger state student-data statutes, general breach statutes, and contract terms concurrently. **Do not compute notification deadlines** — every triggering-fact date is `[deadline verification required]` and each framework is `[Verify current law]` `[verify jurisdiction]`.

### Skill: `skills/privacy/pia-generation/SKILL.md`

**Overlay considerations:**

- **Minor-data categorization** — surface whether the flow includes minors' data and which heightened categories (Section 2.3) are present; categorization is an attorney determination.
- **Consent-authority mapping** — record who consents or exercises rights for each data subject population (parent, eligible student, school-in-lieu) and flag the authority question for counsel `[Verify current law]`.
- **Regime mapping** — surface which regimes plausibly attach (student-records, children's-privacy, state student-data statutes, health-privacy boundary) without concluding applicability.
- **Profiling, advertising, and analytics uses** — surface each such use of student data as a flagged item; several regimes in the category restrict them `[Verify current law]` `[verify jurisdiction]`.
- **Age-assurance mechanics** — where the product screens for age, surface the screening design and its own data-collection footprint for review.

### Skill: `skills/privacy/dsar-workflow/SKILL.md`

**Overlay considerations:**

- **Parent / eligible-student access is a distinct framework** from consumer data-subject-rights regimes — scope (education records), requester authority, response mechanics, and amendment / hearing rights differ materially `[Verify current law]`.
- **Requester-authority verification** — confirm who holds the rights (parent, eligible student, guardian, non-custodial parent under court orders) before any disclosure; surface custody-order questions to counsel.
- **Concurrent frameworks** — a single request may trigger a student-records regime, a state student-data statute, and a consumer-privacy statute in parallel; surface the tracks and do not collapse them `[verify jurisdiction]`.
- **Subpoenas and law-enforcement requests** — student-records regimes carry their own judicial-order and subpoena frameworks, often with prior-notification elements `[Verify current law]`. Route every such request to counsel before response.
- **Response timing** — records-request response windows are regime-specific; every date is `[deadline verification required]`.

### Skill: `skills/privacy/privacy-policy-gap-review/SKILL.md`

**Overlay considerations:**

- **Layered notices** — an education organization may owe an annual student-records notification, a directory-information notice with opt-out mechanics, a children's-privacy notice, and a general consumer privacy policy; confirm the review distinguishes them and flags inconsistencies `[Verify current law]`.
- **Child- and parent-facing readability** — children's-privacy frameworks impose notice-content requirements distinct from adult-facing policies `[Verify current law]`.
- **No-advertising representations** — where the organization or product represents that student data is never used for advertising or profiling, surface the representation against actual data flows.
- **State-statute disclosures** — state student-data statutes may require specific disclosures or published vendor lists `[verify jurisdiction]`.

### Skill: `skills/contracts/contract-risk-review/SKILL.md`

**Overlay considerations:**

- **Data-sharing addendum presence** — an ed-tech or vendor contract touching student data without a student-data-sharing addendum (or equivalent terms) is a flagged gap; surface existence, version, and execution status.
- **School-official-style designation language** — where the vendor's access is premised on a school-official-style designation, confirm the contract contains the use-limitation and direct-control language that framework presumes `[Verify current law]`.
- **Accessibility warranties** — surface whether the contract contains digital-accessibility conformance representations and remediation obligations; institutions frequently carry the underlying obligation and need the flow-down `[Verify current law]`.
- **Background-screening and minor-contact flow-downs** — for vendors whose personnel interact with students, surface screening, supervision, and reporting flow-downs `[verify jurisdiction]`.
- **Public-entity contracting constraints** — districts and public institutions carry procurement, open-records, records-retention, and governing-board-approval constraints that alter standard commercial terms `[verify jurisdiction]`. Surface, do not assume.

### Skill: `skills/contracts/vendor-agreement-status/SKILL.md`

**Overlay considerations:**

- **Ed-tech vendor inventory** — for each vendor receiving student data, confirm: contract and data-sharing addendum executed? current template version? state-mandated terms present for each operating state? deletion-at-termination mechanics in place? Surface vendors without addenda as flagged exposure.
- **Consent-basis register** — record for each vendor whether access rests on a school-official-style designation, parental consent, school-consent-in-lieu, or another basis; surface unknowns `[Verify current law]`.
- **Sub-processor chains** — where a vendor uses subcontractors touching student data, the restriction chain must continue; surface chain gaps.
- **Free / teacher-adopted tools** — classroom tools adopted without procurement are a recurring inventory gap; surface any known shadow-adoption channel.

### Skill: `skills/employment/employee-policy-review/SKILL.md`

**Overlay considerations:**

- **Mandatory-reporting policy** — confirm policies identify who is a mandatory reporter, the escalation path, and training cadence, without stating the statutory trigger or timeline (each is `[verify jurisdiction]` `[deadline verification required]`); confirm the policy does not suggest internal review substitutes for a personal statutory duty.
- **Background screening and licensure** — confirm policies address pre-hire screening, periodic re-screening, and certification / licensure verification for roles with student contact `[verify jurisdiction]`.
- **Staff–student interaction and communication policies** — boundaries, one-to-one communication channels, and electronic-communication rules are recurring policy elements; surface gaps.
- **Title IX-style process interface** — confirm employee policies mesh with the institution's grievance procedures (coordinator roles, non-retaliation, parallel-track handling) `[Verify current law]`.
- **Union and tenure layers** — collective-bargaining agreements and tenure frameworks alter discipline mechanics; route to labor / higher-education counsel where applicable `[verify jurisdiction]`.

### Skill: `skills/employment/internal-investigation/SKILL.md`

**Overlay considerations:**

- **Mandatory-reporting gate first** — before and during any investigation touching possible abuse or neglect of a minor, the mandatory-reporting question routes to counsel immediately; an internal investigation never delays or substitutes for a statutory report `[verify jurisdiction]` `[deadline verification required]`.
- **Title IX-style process intersection** — where the conduct falls within a grievance-process regime, the mandated process architecture (coordinator, investigator / decision-maker separation, supportive measures, appeal) constrains how an employment investigation may run; surface the parallel tracks and route process design to specialist counsel `[Verify current law]`.
- **Minor witnesses and complainants** — interviews of minors raise consent, notification, and welfare questions; route protocol design to counsel `[verify jurisdiction]`.
- **Records handling** — investigation records touching students may themselves become education records or otherwise regulated records; surface the classification question.
- **Certification-board reporting** — discipline of licensed / certificated educators may trigger separate reporting to certification bodies `[verify jurisdiction]`; route to counsel.

### Skill: `skills/regulatory/enforcement-risk-memo/SKILL.md`

**Overlay considerations:**

- **Multi-regulator posture** — education matters can attract the federal education agency and its civil-rights office, the consumer-protection regulator (children's privacy, ed-tech representations), state education agencies, and state attorneys general concurrently. Address enforcement posture at the framework level only `[Verify current law]` `[verify jurisdiction]`. **Do not cite specific enforcement actions, resolution agreements, or penalty figures.**
- **Funding-condition exposure** — for funding-conditioned regimes, enforcement can run through program review and funding conditions rather than fines; surface the posture without predicting outcomes `[Verify current law]`.
- **Private-litigation channels** — protected-basis claims and state-statute claims can proceed in parallel to agency enforcement; surface as parallel tracks.

### Skill: `skills/regulatory/compliance-gap-matrix/SKILL.md`

**Overlay considerations:**

- **Multi-regime spine** — structure the matrix around the regimes that plausibly attach: student-records regime, children's-online-privacy regime, state student-data statutes per operating state, anti-discrimination process regime, accessibility obligations, and mandatory-reporting program `[Verify current law]` `[verify jurisdiction]`.
- **Notification and consent artifacts** — annual notifications, directory-information notices, consent records, and school-official designations are distinct gap categories.
- **Vendor / addendum program** — the ed-tech inventory and addendum-coverage status is its own gap category (see the vendor-agreement-status tuning above).
- **Training and reporting program** — mandatory-reporter training, grievance-process role training, and accessibility-procurement checks are recurring gap categories.

### Skill: `skills/product-legal/terms-of-service-review/SKILL.md`

**Overlay considerations:**

- **Contracting with minors** — minors' capacity to contract is limited and jurisdiction-specific `[verify jurisdiction]`; surface who the contracting party is (institution, parent, student) and whether the terms match.
- **Consent architecture** — confirm the terms and consent flow match the claimed basis (verifiable parental consent, school-consent-in-lieu, institutional contract) `[Verify current law]`.
- **Student-data commitments** — no-advertising, no-profiling, deletion, and data-ownership representations in the terms must match the data-sharing addendum and actual practice; surface mismatches.
- **Arbitration and class-waiver clauses** — enforceability against minors and public-entity customers raises distinct questions `[verify jurisdiction]`; surface for counsel.

### Skill: `skills/product-legal/launch-review/SKILL.md`

**Overlay considerations:**

- **Child-directed determination gate** — before launch, surface whether the product or feature is directed to children or likely to attract child users; the determination is fact-intensive and routes to counsel `[Verify current law]`. The overlay never clears a launch.
- **Consent-mechanism readiness** — surface whether the required consent mechanism (verifiable parental consent or school-consent-in-lieu) is built, tested, and documented `[Verify current law]`.
- **State-statute readiness** — for each launch state, surface state student-data-statute obligations as a readiness category `[verify jurisdiction]`.
- **Accessibility readiness** — surface the digital-accessibility conformance posture for the launch surface `[Verify current law]`.
- **Age-gate and default settings** — surface age-screening design, default privacy settings for minors, and any feature (messaging, location, user-generated content) that raises child-safety questions for counsel.

---

## 4. Escalation triggers specific to education

Conditions that, in this sector, must stop a workflow and route the matter to an education-specialist or supervising attorney before proceeding:

- **Suspected abuse or neglect of a minor, or any mandatory-reporting question.** Route to counsel immediately. Reporting duties are typically personal, non-delegable, and time-sensitive `[verify jurisdiction]` `[deadline verification required]`. The overlay never advises whether, when, or to whom to report, and no workflow may delay the question.
- **A Title IX-style complaint, sexual-misconduct allegation, or grievance-process design question.** Specialist process counsel; the mandated process architecture is heavily amended and litigated `[Verify current law]`.
- **An education-agency complaint, program review, audit, or enforcement contact.** Stop, preserve records, do not respond without counsel.
- **A consumer-protection-regulator inquiry touching children's privacy or ed-tech representations.** Route to counsel.
- **A confirmed or suspected breach involving student records or minors' data.** Multiple concurrent frameworks (state student-data statutes, general breach statutes, contracts). Triggering-fact dates are `[deadline verification required]`; each framework is `[Verify current law]` `[verify jurisdiction]`. Surface immediately; do not compute deadlines.
- **A law-enforcement, immigration-enforcement, or subpoena request for student records.** Student-records regimes carry their own disclosure and notification frameworks `[Verify current law]`; route before any response.
- **A health-and-safety-emergency disclosure question** (threat assessment, welfare concern). The exception frameworks are narrow and fact-intensive `[Verify current law]`; route to counsel.
- **An accessibility complaint, demand letter, or agency inquiry.** Accessibility counsel `[Verify current law]`.
- **A special-education (IDEA-style) dispute or records question.** Special-education counsel; out of this overlay's scope.
- **A boundary question between student-records and health-privacy regimes** (school health services, counseling records, telehealth in schools). Specialist counsel `[Verify current law]`.
- **Discipline of a licensed / certificated educator.** Separate certification-board reporting may attach `[verify jurisdiction]`; labor and licensing counsel.
- **A product or feature directed to children, or evidence of substantial child use of a general-audience product.** Children's-privacy counsel before launch or continued operation `[Verify current law]`.
- **Any request to identify, profile, or advertise to students.** Surface for counsel; restricted under multiple regimes in the category `[Verify current law]` `[verify jurisdiction]`.

---

## 5. Standard education-counsel positions to surface (as questions, not conclusions)

These are recurring negotiation and documentation positions an education team needs to answer. The overlay surfaces the question; the organization (via `profile.md`) fills in the position; the supervising attorney confirms.

- **Data-sharing-addendum template.** Which addendum template and version does the organization use, which state-mandated terms does it incorporate, and what are the acceptable fallback positions on deletion, sub-processors, and audit rights?
- **School-official designation posture.** When does the organization designate a vendor under a school-official-style framework, what direct-control language is required, and who approves the designation `[Verify current law]`?
- **Consent posture.** For consumer-facing products: which verifiable-parental-consent mechanism? For school channels: when is school-consent-in-lieu relied on, and with what documentation `[Verify current law]`?
- **Age-screening posture.** What age-assurance mechanics does the organization use, and what happens on under-age discovery (data deletion, account conversion, notification)?
- **Directory-information and media posture.** What is designated directory information, what is the opt-out mechanic, and who clears media and photography uses involving students?
- **Advertising and profiling prohibition.** What is the organization's position on advertising, profiling, and product-improvement uses of student data, and how is it enforced in contracts?
- **Retention and deletion posture.** Retention schedules for student data; deletion mechanics at contract end and on request; who verifies deletion.
- **Subpoena and law-enforcement protocol.** Who receives and reviews every request for student records before any response; what notification steps precede disclosure `[Verify current law]`?
- **Mandatory-reporting protocol.** Who is trained as a mandatory reporter, what is the internal escalation path that runs alongside (never instead of) the statutory duty, and who is on-call counsel `[verify jurisdiction]`?
- **Grievance-process roles.** Who holds the coordinator-style roles, how are investigator / decision-maker separations staffed, and which matters go to outside process counsel `[Verify current law]`?
- **Accessibility posture.** Which digital-accessibility conformance target does the organization adopt, what procurement clause is standard, and who owns remediation `[Verify current law]`?
- **Background-screening posture.** Screening scope, re-screening cadence, and vendor-personnel flow-downs for roles with student contact `[verify jurisdiction]`.
- **Breach chain of command.** Who determines which frameworks a student-data incident triggers, who notifies institutions / parents / regulators, and who is on the incident-response retainer?

---

## 6. Loading sequence and interaction with other overlays

When this overlay is loaded, the agent should observe the load order described in `overlays/README.md`:

1. `core/` operating rules (the absolute floor).
2. The relevant practice profile from `practice-profiles/`.
3. The selected skill's `SKILL.md`.
4. This overlay's `OVERLAY.md` and `profile.md`.

This overlay frequently runs alongside other overlays where they exist — for example, the healthcare overlay for school-health, counseling, and academic-medical-center matters, or the fintech-payments overlay for tuition- and campus-payment matters. When multiple overlays apply, each adds gates and verification items; none subtracts. If two overlays appear to conflict on a position, the supervising attorney resolves; the agent surfaces the conflict and does not silently pick.

The overlay is also designed to compose with the cluster-level reference catalogs (`skills/contracts/references/red-flags.md`, `skills/antitrust-competition/references/risk-indicators.md`, `skills/securities-capital-markets/references/issue-spotting-frameworks.md`) — those catalogs handle the cross-sector patterns; this overlay adds the education-layer attorney-verification items on top.

---

## 7. What this overlay does NOT do

- **No regime-applicability conclusion.** The overlay never concludes that a student-records, children's-privacy, anti-discrimination, accessibility, or state-statute regime applies or does not apply to any entity, product, or dataset. Always counsel `[Verify current law]` `[verify jurisdiction]`.
- **No mandatory-reporting determination.** The overlay never advises whether, when, or to whom to report; it routes the question to counsel immediately.
- **No age, milestone, or threshold statement.** Rights-transfer ages, child-definition ages, and consent ages are `[Verify current law]` `[verify jurisdiction]` in every case.
- **No exception clearance.** The overlay never concludes that a directory-information, school-official, health-and-safety-emergency, or subpoena exception applies to a specific disclosure.
- **No grievance-process design.** Process architecture under Title IX-style regimes is specialist-counsel work `[Verify current law]`.
- **No special-education, student-discipline, financial-aid, accreditation, athletics, or visa guidance.** Each routes to its specialist.
- **No accessibility-conformance opinion.** The overlay surfaces the conformance question; it never concludes a product or site conforms.
- **No deadline computation.** Reporting windows, response times, and notification dates are `[deadline verification required]` in every case.
- **No jurisdiction-of-the-week opinion.** Every jurisdiction-specific note carries `[verify jurisdiction]`; the overlay surfaces the question, never concludes.

---

## How to use this overlay

Load it, after the `core/` rules, the relevant practice profile, and the chosen skill, when the matter involves education facts. See `overlays/README.md` for the load order.

The overlay sharpens the skill for the sector. It adds gates, terminology, and attorney-verification items; it never replaces the skill, the `core/` rules, or the supervising attorney.

## Status

`experimental` — built under the overlays/ scaffold and modeled on the healthcare and fintech-payments overlays; deliberately the lightest of the three, per the expansion plan. To be promoted to `stable` once a supervising education-counsel reviewer has confirmed the framework references, the per-skill tuning notes have been exercised on at least one real matter, and `profile.md` has been completed for the organization. Recorded in `docs/PRACTICE_AREAS.md`.
