# Healthcare and Life Sciences Overlay Profile

A sector configuration profile, in the same style as the files under `practice-profiles/`. It records how a team's work in **healthcare and life sciences** differs from the general case.

This profile is **not** legal work product and **not** legal advice. It is internal configuration. It must be reviewed and approved by a supervising attorney — ideally a HIPAA-specialist attorney — before it is loaded alongside any skill. Organization-specific values are left as `[ORGANIZATION TO FILL]` placeholders because this profile ships with the overlay scaffold, not with a specific organization's configuration.

The overlay's framework references (`OVERLAY.md`) are paired with this profile. The profile sets organization-specific positions; the OVERLAY.md sets sector-wide tuning. Both are subordinate to `core/` and to the supervising attorney.

---

## Sector and scope

- **Sector / client type:** healthcare and life sciences — hospitals, health systems, payers, providers (including independent practices, multi-specialty groups, and ASCs), digital-health companies (B2B and consumer-facing), life-sciences manufacturers, healthcare-adjacent SaaS, and vendors serving any of the above.
- **In-scope activities:** privacy, contracts, employment, regulatory, and AI-governance work coloured by HIPAA, HITECH, sector-specific data regimes (CMIA, MHMDA, HB 300, SHIELD, others), 42 CFR Part 2 (where SUD records in scope), GINA (where genetic information in scope), and reproductive-health frameworks (where in scope).
- **Out of scope:** specialist healthcare regulatory work that routes to a separate practice — anti-kickback and Stark analysis, FDA device / SaMD / drug-approval work, DEA / controlled-substances and prescribing matters, state-board licensing matters, corporate-practice-of-medicine analysis, billing and coding compliance, ERISA / ACA / MHPAEA insurance-regulation work, clinical-malpractice work, government-program (Medicare / Medicaid / VA / IHS / TRICARE) program-integrity work, and 42 CFR Part 2 substantive analysis. The overlay surfaces these as routing flags; the work itself is performed by specialist counsel.

## Jurisdictions

- **Primary federal regulators:** Department of Health and Human Services (HHS), including the Office for Civil Rights (OCR); FDA; DEA; CMS; ONC; OIG; FTC (for consumer-app and non-covered-entity matters); SAMHSA (for 42 CFR Part 2 questions).
- **State jurisdictions of typical concern:** **every state in which the organization operates or holds patient records** — HIPAA preempts contrary state law only where the state law is not more stringent and does not fall within specified exceptions `[verify current HHS rule]`. Named state regimes the overlay tracks include:
  - California — CMIA and CCPA / CPRA `[verify jurisdiction]`.
  - Texas — HB 300 and broader-than-HIPAA covered-entity definition `[verify jurisdiction]`.
  - Washington — My Health My Data Act (MHMDA) `[verify jurisdiction]`.
  - New York — SHIELD Act intersection with HIPAA `[verify jurisdiction]`.
  - Other state health-data, biometric, mental-health, genetic-information, and reproductive-health regimes — `[verify jurisdiction]`.
- **Jurisdictions requiring escalation to local or specialist counsel:** every U.S. state for state-law-overlay questions on a state-by-state basis; every non-U.S. jurisdiction where data will be transmitted, stored, or processed (data-localization analysis); every jurisdiction in which the organization is licensed to provide care for licensing-board questions.
- Sector-specific legal rules are always attorney-verification items. This profile does not state them.

## Sector gates and escalation thresholds

Conditions that must stop the workflow and route the matter to specialist or supervising attorney before proceeding (mirroring `OVERLAY.md` Section 4):

- Confirmed or suspected breach affecting 500+ individuals — HIPAA-specialist counsel and (per the organization's protocol) the breach-response team.
- OCR investigation, audit notice, or data request — HIPAA counsel.
- DEA or state-board licensing inquiry on a prescriber or pharmacy matter — DEA / state-board specialist counsel `[verify jurisdiction]`.
- 42 CFR Part 2 records or substance-use-facility involvement — Part 2 specialist counsel.
- Genetic-information involvement — GINA-aware counsel.
- Reproductive-health information — post-Dobbs specialist counsel; state-by-state analysis `[verify jurisdiction]`.
- Pediatric data — minor-consent specialist; COPPA review if consumer-app facing.
- Clinical decision support, diagnostic, or treatment-recommendation software — FDA SaMD counsel.
- Anti-Kickback or Stark implication in any commercial arrangement — fraud-and-abuse counsel.
- Information-blocking question — ONC specialist.
- Government-program contract — government-contracts counsel.
- Telemedicine across state lines — healthcare-regulatory counsel.
- Consumer-facing health entity claiming HIPAA-non-applicability — confirm covered-entity status and FTC Health Breach Notification Rule / state-law overlay before proceeding.

## Standard positions

These are the organization's default positions on recurring sector-specific issues. The overlay flags deviations; the supervising attorney confirms. All placeholders are deliberately left as `[ORGANIZATION TO FILL]` because the profile ships without an organization-specific config.

- **BAA template:** `[ORGANIZATION TO FILL — name of current BAA template, version, last review date, location, owner.]`
- **BAA fallback positions:** `[ORGANIZATION TO FILL — acceptable fallback positions on sub-BA approval mechanism, breach-notification reporting timeline (BA-to-CE), indemnity scope, liability cap, audit-rights scope, and audit-cost allocation.]`
- **Vendor-supplied BAA acceptance threshold:** `[ORGANIZATION TO FILL — below what risk threshold is vendor-paper BAA acceptable; what are the must-change terms; what is the escalation path for vendor refusal to negotiate.]`
- **Insurance and indemnity floor for BAAs:** `[ORGANIZATION TO FILL — minimum cyber-liability insurance limits; minimum indemnity scope; whether indemnity is uncapped for breach-notification costs; named-insured posture.]`
- **De-identification posture:** `[ORGANIZATION TO FILL — whether the organization accepts vendor-side de-identification; required method (Safe Harbor or Expert Determination); required documentation; specialist counsel involvement threshold.]`
- **AI-vendor PHI-training posture:** `[ORGANIZATION TO FILL — whether vendors may use PHI inputs for training, fine-tuning, or product improvement; under what de-identification posture; with what contractual representations.]`
- **Breach-notification chain of command:** `[ORGANIZATION TO FILL — who decides whether an event is a "breach"; who signs notification letters; who coordinates HHS and media notification; on-call rotation; incident-response retainer relationships.]`
- **Incident-response retainers:** `[ORGANIZATION TO FILL — forensic vendor, notification-letter vendor, call-center vendor, credit-monitoring vendor.]`
- **Workforce sanctions framework:** `[ORGANIZATION TO FILL — graduated-sanctions matrix; documentation flow; reporting-to-licensing-boards posture.]`
- **State-of-operations list:** `[ORGANIZATION TO FILL — every state in which the organization operates, holds patient records, or has workforce, for state-law-overlay analysis.]`
- **Government-program contract inventory:** `[ORGANIZATION TO FILL — list of in-scope government healthcare program contracts and the compliance-flow-down owner for each.]`

## Heightened-handling rules

The following data categories, populations, or document types require heightened confidentiality and care, in addition to general PHI handling:

- **Psychotherapy notes** — separate stricter protection under HIPAA `[verify current HHS rule]`.
- **42 CFR Part 2 records** — separate consent and disclosure regime; route to Part 2 counsel.
- **Genetic information** — GINA-aware handling; route to specialist where genetic data is in scope.
- **Reproductive-health information** — post-Dobbs heightened sensitivity; state-by-state analysis `[verify jurisdiction]`; consider information-segregation and access-restriction measures.
- **Pediatric records** — minor-consent rules vary by care type and jurisdiction `[verify jurisdiction]`.
- **HIV / AIDS information, sexually-transmitted-infection information, and mental-health records** — many states impose stricter handling `[verify jurisdiction]`.
- **Workforce-member PHI** — workforce members are also patients in many organizations; access controls and audit posture require dual consideration.
- **Public figures, VIPs, and high-profile patient records** — access-control and audit posture should be heightened; OCR has historically prioritized inappropriate-access investigations involving high-profile patients.
- **Records of organization personnel involved in litigation or investigation** — preservation-and-access controls may apply on top of HIPAA.

## Prohibited assumptions

The agent must never assume any of the following in healthcare matters; each must be surfaced for human confirmation:

- **Covered-entity, business-associate, or subcontractor-BA status.** Always an attorney determination; surface as a question.
- **Conduit-exception applicability.** The exception is narrow and contested; always specialist counsel.
- **PHI classification of any specific dataset.** Always an attorney determination.
- **Adequacy of any de-identification methodology.** Never concluded by the overlay; always specialist (and, for Expert Determination, qualified-expert) determination.
- **HIPAA preemption of any state-law provision.** Always an attorney determination on a state-by-state basis `[verify jurisdiction]`.
- **Any breach-notification deadline.** Triggering-fact dates are `[deadline verification required]`; the timing framework itself is `[verify current HHS rule]`.
- **Any civil-money-penalty tier, dollar amount, or enforcement-outcome prediction.** Always specialist counsel; the overlay never quantifies.
- **FDA SaMD applicability to any specific tool or use case.** Always FDA counsel.
- **Anti-Kickback / Stark exception applicability to any commercial arrangement.** Always fraud-and-abuse counsel.
- **Information-blocking exception applicability.** Always ONC specialist.
- **42 CFR Part 2 applicability or substantive treatment.** Always Part 2 specialist counsel.
- **Telemedicine licensing across any state line.** Always state-board / healthcare-regulatory counsel.
- **State-of-the-law in any U.S. state.** Always `[verify jurisdiction]` and specialist counsel where the state is material.
- **Current SEC / HHS / FDA / DEA / ONC / OIG / FTC rule version.** Always `[verify current rule version]`; rule architecture evolves continuously.

## Source-of-truth documents

These are referenced by name and location; **do not paste** the documents themselves into this profile or any deliverable. The organization fills in the location.

- **HIPAA compliance manual:** `[ORGANIZATION TO FILL]`
- **Notice of Privacy Practices (NPP) current version:** `[ORGANIZATION TO FILL]`
- **BAA template (current version):** `[ORGANIZATION TO FILL]`
- **Subcontractor-BA template (where used):** `[ORGANIZATION TO FILL]`
- **Workforce-training materials and completion records:** `[ORGANIZATION TO FILL]`
- **Sanctions policy and historical sanctions log:** `[ORGANIZATION TO FILL]`
- **Risk analysis (Security Rule) — most recent version and update cadence:** `[ORGANIZATION TO FILL]`
- **Incident-response plan and breach-determination protocol:** `[ORGANIZATION TO FILL]`
- **Vendor inventory and BAA-status tracker:** `[ORGANIZATION TO FILL]`
- **State-law-overlay register** (per state of operation): `[ORGANIZATION TO FILL]`
- **OCR / state-AG / FTC enforcement contact log:** `[ORGANIZATION TO FILL]`
- **Specialist-counsel contact list** — HIPAA, FDA, DEA, fraud-and-abuse, ONC, Part 2, GINA, state-board, professional-liability: `[ORGANIZATION TO FILL]`

## Attorney review

The following must be reviewed by a supervising attorney — and, where the matter requires, by a sector specialist — before any deliverable produced with this overlay is used, sent, or relied upon:

- **HIPAA-specialist counsel** — every BAA, breach-analysis, NPP gap finding, OCR-correspondence draft, Security Rule gap-matrix finding, and right-of-access response.
- **Privacy officer (if a covered entity)** — every HIPAA workforce-policy change, sanctions determination, and breach-notification path determination.
- **FDA-SaMD-specialist counsel** — every AI use case implicating clinical decision support or device-regulated software, before deployment.
- **DEA / state-board counsel** — every matter touching prescribing, controlled substances, or licensed-clinician scope of practice.
- **Fraud-and-abuse counsel** — every commercial-arrangement matter implicating AKS or Stark.
- **42 CFR Part 2 specialist** — every matter touching SUD records or facilities.
- **GINA-aware counsel** — every matter touching genetic information.
- **State-by-state local counsel** — every matter where the state-law overlay is material and the supervising attorney is not admitted in the state `[verify jurisdiction]`.
- **Information-blocking specialist (ONC)** — every matter touching IT-developer, HIE/HIN, or provider information-sharing obligations.
- **Government-contracts counsel** — every matter touching VA, IHS, FEHB, Medicare/Medicaid, or TRICARE program contracts.
- **Professional-liability / malpractice counsel** — every matter where AI-supported clinical decisions or provider-borne liability is in play.

No deliverable produced with this overlay is final until the relevant specialist has reviewed it. The overlay's status remains `experimental` until a supervising healthcare-counsel reviewer has confirmed the framework references, the per-skill tuning notes have been exercised on at least one real matter, and the `[ORGANIZATION TO FILL]` placeholders have been completed.
