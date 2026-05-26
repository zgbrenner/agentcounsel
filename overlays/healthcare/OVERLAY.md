# Healthcare and Life Sciences Overlay

This overlay tunes AgentCounsel's existing skills for **healthcare and life sciences** work — hospitals, health systems, payers, digital-health companies, providers, life-sciences manufacturers, healthcare-adjacent SaaS, and the vendors that serve them. It is internal configuration material, not legal advice and not legal work product. A supervising attorney reviews it before use.

Healthcare is a sector, not a body of law. A healthcare client's legal work is contracts work, privacy work, employment work, regulatory work, and AI-governance work — coloured by HIPAA, by sector-specific data regimes, and by sector-specific regulators. This overlay supplies that colouring; it never replaces the underlying skills, the `core/` operating rules, or the supervising attorney.

---

## 1. Scope of the overlay

### Skills this overlay tunes

The overlay is most often loaded alongside skills in these clusters:

- **Privacy** — DPA review (becomes BAA review when PHI is involved), Privacy Impact Assessment, DSAR workflow, privacy-policy gap review.
- **Contracts** — vendor agreements involving PHI, vendor-agreement inventory, contract risk review, SOW review.
- **Employment** — employee-policy review (HIPAA training and sanctions), internal investigations of suspected unauthorized PHI access.
- **Regulatory** — enforcement-risk memos, compliance gap matrices.
- **AI governance** — AI vendors processing PHI; AI use cases that touch clinical decision support or FDA-regulated software-as-a-medical-device (SaMD).

The per-skill tuning notes appear in Section 3 below.

### What the overlay is NOT

- It does **not** contain skills. Per `overlays/README.md`, overlays never contain skills.
- It does **not** replace specialist healthcare counsel — HIPAA counsel, healthcare regulatory counsel, FDA counsel, state-board licensing counsel, and 42 CFR Part 2 specialist counsel all remain required for their respective domains.
- It does **not** provide jurisdiction-specific clinical-practice, scope-of-practice, licensing, prescribing, telemedicine-permission, controlled-substances, billing-fraud, anti-kickback (AKS), Stark, or insurance-regulation guidance. Each of those areas has its own framework that a healthcare specialist must apply `[verify jurisdiction]`.
- It does **not** state HIPAA, HITECH, GINA, COPPA, 42 CFR Part 2, FDA, DEA, OCR, or state-law requirements. Every rule reference in this overlay is a framework reference, not a statement of law `[verify current rule version]`.
- It does **not** compute breach-notification deadlines or any other deadlines.

---

## 2. The HIPAA architecture (orientation only — not legal advice)

This section orients an agent loading the overlay. None of it is a statement of law. Every framework reference carries `[verify current HHS rule]` because HIPAA's implementing rules have been amended multiple times and continue to evolve `[verify current SEC- and HHS-rule architecture at time of review]`.

### 2.1 Who is regulated under HIPAA

- **Covered entities** — generally health plans, healthcare clearinghouses, and healthcare providers that transmit health information in connection with covered transactions `[verify current HHS rule]`. The covered-entity determination is fact-intensive and is an attorney determination — the overlay never concludes covered-entity status.
- **Business associates** — generally a person or entity that creates, receives, maintains, or transmits Protected Health Information (PHI) on behalf of a covered entity in connection with a covered function `[verify current HHS rule]`. Includes most SaaS vendors that process PHI, claims processors, billing companies, transcription services, cloud-hosting providers (subject to conduit-exception analysis), and many AI vendors processing PHI.
- **Subcontractor business associates** — a business associate of a business associate. Subcontractor BAs are themselves regulated and require a BAA with their upstream BA `[verify current HHS rule]`.
- **Hybrid entities, organized health care arrangements, and affiliated covered entities** — structural concepts that affect how HIPAA applies to large organizations. Always an attorney determination.

### 2.2 PHI vs. de-identified data

- **Protected Health Information (PHI)** — individually identifiable health information held or transmitted by a covered entity or business associate, with limited statutory exceptions. The PHI determination is fact-intensive.
- **De-identification** — HIPAA recognizes two methods: the "Safe Harbor" method (removal of specified categories of identifiers) and the "Expert Determination" method (formal statistical analysis by a qualified expert) `[verify current HHS rule]`. The overlay does **not** enumerate the Safe Harbor identifiers and does **not** assert that either method has been satisfied in any specific case. De-identification is an attorney and (for Expert Determination) qualified-expert determination.
- **Limited Data Set** — a partial de-identification with separate Data Use Agreement (DUA) requirements `[verify current HHS rule]`.
- **Re-identification risk** — even where formal de-identification has been claimed, residual re-identification risk may exist and may be material; specialist review required.

### 2.3 The principal HIPAA rules (framework level only)

Each rule has substantial substantive content beyond what is sketched here; the overlay surfaces the framework so that a supervising attorney can apply the current text of the rule.

**Privacy Rule** — limits use and disclosure of PHI; establishes individual rights; sets minimum-necessary standards `[verify current HHS rule]`. Principal framework elements:
- Permitted and required uses and disclosures (treatment, payment, healthcare operations; required-by-law; public-health; oversight; judicial / administrative proceedings; law enforcement; decedents; cadaveric organ/tissue donation; research; serious threat to health or safety; specialized government functions; workers' comp).
- Authorizations for uses and disclosures not otherwise permitted (including marketing, sale of PHI, and most psychotherapy-note disclosures), with content and core-element requirements.
- Individual rights: notice (NPP), access, amendment, accounting of disclosures, restrictions, confidential communications, and the right to receive certain disclosures of PHI in electronic form.
- Minimum-necessary standard applied to non-treatment uses, disclosures, and requests.
- Administrative requirements: workforce training, sanctions, safeguards, complaint process, mitigation, anti-retaliation, and policy-and-procedure documentation.

**Security Rule** — administrative, physical, and technical safeguards for electronic PHI (ePHI); risk-analysis and risk-management requirements `[verify current HHS rule]`. Principal framework elements:
- Administrative safeguards — security management process (including risk analysis and risk management), assigned security responsibility, workforce security, information access management, security awareness and training, security incident procedures, contingency plan, evaluation, and BAA / contract requirements.
- Physical safeguards — facility access controls, workstation use, workstation security, and device and media controls.
- Technical safeguards — access control, audit controls, integrity, person or entity authentication, and transmission security.
- Implementation specifications are characterized as either "required" or "addressable"; "addressable" is **not** "optional" — it requires the entity to assess and document the determination `[verify current HHS rule]`.
- Documentation requirements run alongside each safeguard.

**Breach Notification Rule** — notification obligations following a breach of unsecured PHI; running to individuals, to HHS, and, for breaches above the relevant threshold, to media `[verify current HHS rule]`. Principal framework elements:
- "Breach" definition with the statutory exceptions (good-faith access, inadvertent intra-organizational disclosure, recipient-could-not-reasonably-have-retained) and the four-factor risk-of-compromise assessment.
- Notification content requirements (description of incident, types of PHI involved, steps individuals can take, the entity's response, and contact information).
- Notification methods (written, substitute, urgent).
- Separate timing for individual notification, HHS notification, and (for breaches above the threshold) prominent-media-outlet notification.
- BA-to-CE reporting framework, contractual reporting timelines, and the CE's downstream notification triggers.
- Discovery-date vs. occurrence-date distinction: notification timing runs from the date of **discovery**, not the date the breach occurred. "Discovery" is the date the covered entity knew, or by exercising reasonable diligence would have known, of the breach `[verify current HHS rule]`. The overlay does not compute or assert a discovery date — it is fact-intensive and is an attorney determination.
- Outer deadlines and content requirements live in the rule itself `[verify current HHS rule]` — the overlay **does not compute notification deadlines**.

**Enforcement Rule** — OCR investigations, civil money penalty tiers, willfulness gradations, corrective-action plans, resolution agreements `[verify current HHS rule]`. Principal framework elements:
- Complaint intake and investigation pathways; compliance reviews; audits.
- Culpability tiers (lack of knowledge; reasonable cause; willful neglect with timely correction; willful neglect without timely correction).
- Per-violation and per-calendar-year CMP caps `[verify current HHS rule]` — figures are adjusted periodically and are an attorney-verification item.
- Resolution agreements and corrective-action plans as the typical endgame for material matters.
- Affirmative defenses, mitigating circumstances, and the documented-compliance posture as factors.
- State AG parallel enforcement authority under HITECH.
- DOJ criminal enforcement for willful violations (specialist counsel only).

The overlay does **not** cite specific enforcement actions, settlement amounts, or CMP figures — those age fast and create false-precision risk.

**HITECH Act amendments** — expanded direct liability of business associates; expanded breach-notification framework; tiered CMPs and willfulness gradations; expanded state AG enforcement authority; meaningful-use / promoting-interoperability framework; subsequent regulatory rounds (Omnibus Rule, Right-of-Access Initiative, NPRM cycles, reproductive-health rulemaking) have continued to evolve the framework `[verify current HHS rule]`.

### 2.4 State-law overlays and HIPAA preemption

HIPAA preempts contrary state law except where the state law is more stringent or falls within specified exceptions `[verify current HHS rule]`. The preemption analysis is fact-intensive and is an attorney determination in every case.

Common state-law overlays that frequently apply on top of HIPAA — each `[verify jurisdiction]`:

- **California** — Confidentiality of Medical Information Act (CMIA) and California Consumer Privacy Act / California Privacy Rights Act (CCPA / CPRA) intersections with HIPAA, including the sensitive-personal-information framework. CMIA has substantive provisions distinct from HIPAA.
- **New York** — SHIELD Act intersection with HIPAA, plus state-specific reporting and consent requirements `[verify jurisdiction]`.
- **Texas** — Texas Medical Records Privacy Act (HB 300) and broader-than-HIPAA covered-entity definition `[verify jurisdiction]`.
- **Washington** — My Health My Data Act (MHMDA), which applies to consumer health data outside of HIPAA's covered universe `[verify jurisdiction]`.
- **Other states** — many states have enacted health-data, biometric, mental-health, or genetic-information statutes that overlay HIPAA `[verify jurisdiction]`. Always confirm the state's framework with specialist counsel.

The overlay carries `[verify jurisdiction]` on every state-specific note. None of the above is a statement of any state's law.

### 2.5 Substance-use disorder records (42 CFR Part 2)

A separate federal regime governing records of identity, diagnosis, prognosis, or treatment of any patient in connection with substance-use-disorder programs. Part 2 has been amended in recent years to align more closely with HIPAA but remains a distinct regime with separate consent and disclosure requirements `[verify current HHS / SAMHSA rule]`. Part 2 questions route to Part 2 specialist counsel — not handled by the standard HIPAA workflow.

### 2.6 Genetic information (GINA)

The Genetic Information Nondiscrimination Act restricts use of genetic information in employment, health insurance, and related contexts. GINA defines "genetic information" broadly (including family medical history) and overlays separate requirements that the standard HIPAA workflow does not capture `[verify current EEOC / HHS rule]`. GINA questions route to GINA-aware counsel.

### 2.7 Reproductive-health information in the post-Dobbs landscape

State-by-state developments on reproductive-health-information access, disclosure, and out-of-state-provider protections, plus HHS rulemaking on reproductive-health-information disclosure, create a rapidly-changing layer on top of HIPAA `[verify jurisdiction]` `[verify current HHS rule]`. Always escalate matters involving reproductive-health information to specialist counsel.

### 2.8 Pediatric data

Health data of minors raises HIPAA-plus-COPPA overlays (when consumer-app facing) and state-by-state minor-consent rules for specific care types (mental health, reproductive health, substance use) `[verify jurisdiction]`. Pediatric matters route to specialist counsel.

### 2.9 Other regimes the overlay frequently touches

Each of these is its own framework with its own architecture, regulator, and enforcement posture. The overlay surfaces them as routing flags; specialist counsel performs the substantive analysis.

- **FDA software-as-a-medical-device (SaMD) and clinical-decision-support (CDS)** — separate FDA framework for software meeting the device definition under §201(h) of the FD&C Act; CDS has its own carve-outs and limits, and the line between regulated SaMD and enforcement-discretion CDS is fact-intensive and evolving `[verify current FDA rule]`. SaMD analysis touches device-classification (Class I/II/III), 510(k) / De Novo / PMA pathway, Quality System Regulation, post-market surveillance, and adverse-event reporting. Always route to FDA-specialist counsel.
- **DEA and state controlled-substances rules** — prescribing, e-prescribing, dispensing, disposal, Prescription Drug Monitoring Program (PDMP) reporting, and registration requirements `[verify jurisdiction]`. Telemedicine prescribing of controlled substances is a separately evolving area `[verify current DEA rule]`. Route to DEA / state-board counsel.
- **Anti-Kickback Statute (AKS) and Stark Law** — AKS is a federal criminal anti-fraud statute (with civil-monetary-penalty and FCA overlays); Stark is a strict-liability physician self-referral statute. Both have detailed safe harbors and exceptions; the safe-harbor / exception analysis is fact-intensive and an attorney determination in every case `[verify current OIG / CMS rule]`. Touched arrangements include physician compensation, leases of healthcare-related space, professional-services agreements, joint ventures, value-based-care arrangements, and many digital-health vendor relationships. Always fraud-and-abuse counsel; the overlay never opines.
- **False Claims Act (FCA) exposure** — improper claims submission, including AKS-induced claims, can trigger qui-tam exposure; relator-driven investigations are common in healthcare `[verify current DOJ / OIG rule]`. Route to FCA / healthcare-litigation counsel.
- **Information-blocking rules (21st Century Cures Act, ONC)** — provider, IT-developer, and HIE/HIN obligations regarding electronic-health-information sharing, with eight defined exceptions; enforcement is via OIG civil money penalties (developers, networks) and CMS provider disincentives `[verify current ONC rule]`. Specialist counsel.
- **FTC Health Breach Notification Rule** — applies to non-HIPAA-covered vendors of personal health records and related entities; consumer-facing health apps frequently fall within scope `[verify current FTC rule]`. Distinct notification framework from HIPAA's.
- **Federal grant or government-program contracts** — VA, Indian Health Service, FEHB, Medicare / Medicaid, TRICARE contracts add data-localization, FAR / DFARS, CUI-handling, and program-specific compliance flow-downs. Route to government-contracts counsel for the substantive flow-down analysis.
- **Corporate practice of medicine and fee-splitting doctrines** — many states restrict ownership and control of medical practices, profit-sharing with non-licensed entities, and management-services-organization (MSO) structures `[verify jurisdiction]`. Healthcare-regulatory counsel.
- **State telemedicine licensing and standard-of-care** — state-by-state licensing, modality, prescribing, and standard-of-care rules `[verify jurisdiction]`. Healthcare-regulatory counsel.
- **No Surprises Act / price-transparency rules** — billing-and-coverage framework for out-of-network claims; specialist counsel.
- **Mental Health Parity and Addiction Equity Act (MHPAEA), ERISA, ACA** — group health plan and benefits-regulation overlays; specialist insurance / ERISA counsel.

### 2.10 Terminology an agent should recognize and use precisely

These terms recur in healthcare matters and carry specific meanings. The overlay does not redefine them; use them as the law and the industry use them, and confirm with counsel when the substantive meaning matters.

- **PHI / ePHI** — Protected Health Information / electronic PHI.
- **Covered entity (CE), business associate (BA), subcontractor BA** — HIPAA-regulated parties.
- **BAA** — Business Associate Agreement; HIPAA-required contract between CE and BA (and between BA and subcontractor BA).
- **NPP** — Notice of Privacy Practices; the CE's HIPAA-required notice.
- **Designated record set** — the records subject to the HIPAA right of access.
- **Psychotherapy notes** — separately defined and separately protected.
- **Safe Harbor / Expert Determination** — the two HIPAA de-identification methods.
- **Limited Data Set / Data Use Agreement (DUA)** — partial de-identification with separate contracting.
- **Minimum necessary** — the HIPAA standard for non-treatment uses, disclosures, and requests.
- **Treatment, Payment, and Healthcare Operations (TPO)** — permitted-disclosure categories under the Privacy Rule.
- **Authorization** — a HIPAA-defined consent instrument with required core elements.
- **Workforce member** — HIPAA-defined; broader than employees.
- **Hybrid entity, organized health care arrangement (OHCA), affiliated covered entity (ACE)** — structural designations for large organizations.
- **Risk analysis, risk management** — required Security Rule elements with distinct documentation expectations.
- **Addressable vs. required** — Security Rule implementation-specification categories; "addressable" is not optional.
- **Breach, unsecured PHI, four-factor assessment** — Breach Notification Rule terms of art.
- **Resolution agreement, corrective action plan (CAP)** — Enforcement Rule terms of art.
- **OCR, OIG, ONC, SAMHSA, CMS** — federal agencies the overlay routinely touches.
- **SaMD, CDS** — FDA software classifications.
- **AKS, Stark, FCA, CMP** — fraud-and-abuse acronyms.
- **EHR / EMR, HIE / HIN** — electronic health-record / health-information-exchange terms.
- **PDMP** — Prescription Drug Monitoring Program.
- **FERPA, COPPA, GINA, CMIA, HB 300, MHMDA, SHIELD** — adjacent / state-law regimes.
- **CMIA, 42 CFR Part 2, EMTALA, HITECH, HIPAA Omnibus Rule** — additional federal frameworks.

---

## 3. Per-skill tuning notes

For each skill in the affected clusters below, the overlay names the specific HIPAA-layer concerns a supervising attorney should add to the standard review. The overlay does not alter the skill; it adds attorney-verification items.

### Skill: `skills/privacy/dpa-review/SKILL.md`

**Overlay considerations:**

- Treat as a **Business Associate Agreement (BAA)** when PHI is involved, not just a DPA. BAA-specific terms required by the HIPAA Privacy Rule supplement the generic DPA framework `[verify current HHS rule]` — at minimum: permitted and required uses and disclosures of PHI by the BA; safeguards required by the Security Rule for ePHI; reporting of unauthorized uses or disclosures and security incidents; flow-down to subcontractors; access, amendment, and accounting-of-disclosures cooperation; HHS Secretary access; return or destruction of PHI at termination.
- **Sub-processor approval** in the generic DPA becomes the **Subcontractor BA flow-through requirement**: every subcontractor of the BA that creates, receives, maintains, or transmits PHI on behalf of the BA must itself be subject to a BAA with terms no less stringent than the upstream BAA `[verify current HHS rule]`.
- **Breach notification timeline analysis** becomes HIPAA breach notification — distinct from GDPR's 72-hour controller-to-supervisory-authority deadline and from state breach-notification statutes. Multiple notification flows: BA to covered entity, covered entity to individuals, covered entity to HHS, and (above the relevant threshold) covered entity to media. **Do not compute notification deadlines** — every triggering-fact date is `[deadline verification required]` and the timing framework itself is `[verify current HHS rule]`. Note that contractual BA-to-CE reporting timelines vary widely (24 hours, 48 hours, 5 days, "without unreasonable delay," etc.); each contract frames this differently.
- **Cross-border transfer analysis** is supplemented by data-localization considerations for PHI under contracts with VA, Indian Health Service, certain DoD healthcare programs, and other government healthcare programs. Some federal programs prohibit or restrict offshore processing of PHI `[verify current contract terms]`.
- **State-law layers** — California CMIA, Texas HB 300, Washington MHMDA, New York SHIELD, others — may add substantive requirements beyond HIPAA, including stricter breach-notification timing or content `[verify jurisdiction]`.
- **Definitions audit** — confirm the BAA's definitions of "PHI," "ePHI," "breach," "security incident," "unsuccessful security incident," and "permitted uses and disclosures" track the HIPAA rule text rather than an idiosyncratic vendor-supplied definition.
- **Liability and indemnity interplay** — note whether the BAA's liability is capped to a sum that bears any relationship to realistic OCR penalty exposure or to breach-notification costs (notification mailings, credit monitoring, call center, forensic investigation, regulator response). Most vendor-supplied BAAs cap liability far below realistic exposure.

### Skill: `skills/privacy/pia-generation/SKILL.md`

**Overlay considerations:**

- **PHI categorization** — surface whether PHI, de-identified data, or Limited Data Set categories are involved, and flag the categorization itself as an attorney determination (the overlay never concludes de-identification has been achieved).
- **Covered-entity / business-associate determination** — surface the entity's status as a question; do not conclude.
- **Minimum-necessary framework** — confirm the PIA tests use, disclosure, and access against the minimum-necessary standard as a framework, without asserting compliance.
- **Sectoral overlays** — note 42 CFR Part 2 (substance-use), GINA (genetic), reproductive-health, pediatric, mental-health, and any state-specific overlays.
- **Security Rule cross-reference** — confirm the PIA's safeguards section maps to the Security Rule's administrative, physical, and technical safeguard categories without claiming Security Rule compliance.
- **Risk-analysis interaction** — the HIPAA Security Rule has a separate risk-analysis requirement; the PIA does not satisfy it. Surface the distinction.
- **Use of de-identified data downstream** — if downstream uses involve re-linkage or augmentation with other datasets, flag re-identification risk for specialist review.

### Skill: `skills/privacy/dsar-workflow/SKILL.md`

**Overlay considerations:**

- **HIPAA right-of-access** is a distinct framework from CCPA / GDPR / state-privacy-statute access rights. Scope of records (designated record set), timing, format, fees, denial grounds, and patient-vs-personal-representative authorization differ materially `[verify current HHS rule]`.
- **Designated record set** — the right of access reaches the designated record set, which is defined by the covered entity's actual record system, not by a generic "personal data" notion.
- **Personal representatives, parents, and minors** — authorization rules differ from non-healthcare frameworks and are jurisdiction- and care-type-specific `[verify jurisdiction]`.
- **Psychotherapy notes** — separately protected with stricter rules `[verify current HHS rule]`.
- **42 CFR Part 2 records** — separate consent and disclosure rules; an access request reaching Part 2 records does not run through HIPAA alone.
- **Fee limits** — HIPAA caps fees for individual access; vendor systems often default to broader fee posture `[verify current HHS rule]`.
- **Format and delivery** — HIPAA-specific rules on electronic copies, format, and third-party-recipient delivery `[verify current HHS rule]`.
- **Concurrent CCPA / state-law request** — a single request may trigger multiple frameworks; surface the parallel-track question and do not collapse into one workflow.

### Skill: `skills/privacy/privacy-policy-gap-review/SKILL.md`

**Overlay considerations:**

- **Notice of Privacy Practices (NPP)** — for covered entities, the HIPAA NPP is a regulated document with content, format, availability, posting, and acknowledgment requirements distinct from a general consumer-facing privacy policy `[verify current HHS rule]`.
- **NPP vs. website privacy policy** — many healthcare entities operate both. Confirm the gap review distinguishes the two and flags any inconsistency.
- **State-law layers** — CMIA, HB 300, MHMDA, SHIELD, and others may require disclosures beyond the HIPAA NPP `[verify jurisdiction]`.
- **Marketing, sale, and authorization** — HIPAA's marketing and sale-of-PHI authorization framework is stricter than general consumer-privacy frameworks `[verify current HHS rule]`.
- **Research, fundraising, underwriting** — HIPAA has specific authorization / opt-out frameworks for these activities `[verify current HHS rule]`.
- **Consumer-facing digital-health entities** — entities that operate consumer-facing apps may be outside HIPAA's covered universe but inside state-law (MHMDA, CMIA) or FTC Health Breach Notification Rule scope `[verify jurisdiction]`. Always confirm covered-entity status before assuming HIPAA framing.

### Skill: `skills/contracts/contract-risk-review/SKILL.md`

**Overlay considerations:**

- **BAA flow-down** — when the contract is with or through a vendor that will create, receive, maintain, or transmit PHI, the contract should pair with (or contain) a BAA. Surface the BAA's existence, version, and execution status. If the contract has data-handling provisions without a BAA where one would be expected, flag prominently.
- **Anti-Kickback and Stark exposure** — many healthcare commercial arrangements (referral arrangements, physician compensation, leases of healthcare-related space, professional-services agreements with referring providers) implicate AKS and Stark. The overlay does **not** opine on AKS / Stark; surface the question and route to fraud-and-abuse counsel.
- **Information-blocking** — IT-developer, health-information-network, and provider contracts may implicate ONC information-blocking rules `[verify current ONC rule]`.
- **Government-program contracts** — VA, IHS, FEHB, Medicare/Medicaid, TRICARE contracts add FAR/DFARS-style obligations, data-localization, and program-specific compliance flow-downs.
- **Indemnity and liability adequacy** — for vendors processing PHI, assess whether the liability cap bears any relationship to realistic OCR penalty exposure, breach-notification costs, and reputational harm. Vendor caps often run well below realistic healthcare exposure.
- **Audit rights** — for healthcare matters, audit rights frequently need to support HHS Secretary access and the covered entity's own compliance audit needs, not just a generic SOC 2 substitute.

### Skill: `skills/contracts/vendor-agreement-status/SKILL.md`

**Overlay considerations:**

- **BAA inventory** — for each vendor that creates, receives, maintains, or transmits PHI, confirm: BAA executed? current template version? subcontractor flow-down in place? termination/data-return mechanics in place? Surface vendors without BAAs as a flagged exposure.
- **Tiered vendor categorization** — distinguish BA-required vendors from conduit-exception candidates (the conduit exception is narrow and contested; an attorney determination in every case) `[verify current HHS rule]`.
- **Data-handling addendum vs. BAA** — many vendors provide a generic DPA when a BAA is required, or vice versa. Surface the mismatch.
- **Cloud, AI, and analytics vendors** — these are frequently BA-required even when the vendor markets the relationship as "we don't really see your data."
- **Sub-BA chains** — where a vendor uses subcontractors, the BA chain must continue. Surface BAA-chain gaps.
- **Government-program flow-downs** — VA, IHS, and other government healthcare program contracts may require specific flow-down clauses.

### Skill: `skills/ai-governance/ai-vendor-terms-review/SKILL.md`

**Overlay considerations:**

- **BAA required when AI vendor processes PHI** — most AI vendors that receive PHI inputs are business associates; a BAA is required `[verify current HHS rule]`. Surface the BAA status as a gate.
- **Compound privilege + PHI issue** — the AI-vendor-terms-review skill already includes the privilege / third-party-disclosure workflow. In healthcare, the same vendor terms simultaneously implicate (a) the privilege analysis if privileged material will be input AND (b) the BAA / PHI analysis. Both run in parallel and route to both privilege counsel and HIPAA counsel.
- **Training-data use of PHI** — the use of PHI to train, fine-tune, or improve models implicates HIPAA's use-and-disclosure framework. A vendor's generic "we use customer data to improve our service" clause is generally **not** acceptable when the inputs are PHI `[verify current HHS rule]`. Surface this gap explicitly.
- **De-identification by the vendor** — some AI vendors propose de-identifying PHI inputs server-side and using the de-identified outputs for training. The de-identification methodology and adequacy is an attorney and qualified-expert determination; the overlay never concludes adequacy. Surface the methodology for specialist review.
- **Output handling** — outputs of an AI system processing PHI may themselves be PHI. Confirm the AI vendor's terms treat outputs as PHI where appropriate.
- **Clinical decision support (CDS)** — if the AI vendor's tool functions as CDS for clinical providers, FDA SaMD analysis may apply alongside HIPAA `[verify current FDA rule]`. Route to FDA-specialist counsel.
- **Sub-processor chain** — every AI sub-processor (model-hosting infrastructure, embedding databases, vector stores, retrieval-augmented-generation services, monitoring tools) that touches PHI must be in the BA chain.
- **Trust-and-safety review of inputs** — some AI vendors' terms permit access to inputs for safety or moderation review. In healthcare this can constitute a use or disclosure of PHI requiring authorization or a permitted-use justification.

### Skill: `skills/ai-governance/ai-use-case-intake/SKILL.md`

**Overlay considerations:**

- **Clinical decision support flag** — surface CDS questions and route to FDA-SaMD counsel `[verify current FDA rule]`. Some uses are within FDA's enforcement-discretion zone; others are not. The overlay never concludes.
- **FDA SaMD scope** — software that meets the device definition under §201(h) of the FD&C Act may be subject to FDA regulation as SaMD `[verify current FDA rule]`. Always route.
- **Diagnostic or treatment-recommendation use** — the use case itself may convert a vendor tool from a low-regulatory-touch product into FDA-regulated software. Surface as a routing flag.
- **Provider liability vs. vendor liability** — provider-borne malpractice exposure from AI-supported clinical decisions is jurisdiction-specific and evolving `[verify jurisdiction]`. Route to professional-liability and malpractice counsel.
- **Population-level analytics on PHI** — even non-clinical analytics use cases may implicate HIPAA, state-law (MHMDA, CMIA), GINA, and reproductive-health-information rules. Surface as gates.
- **Patient-facing chatbots and triage** — consumer-facing health chatbots raise FDA, state-board (corporate practice of medicine, telemedicine), and consumer-protection questions. Route to healthcare regulatory counsel.
- **Research vs. operations vs. treatment** — the HIPAA framework treats these uses differently. Surface the use-case classification as an attorney question.

### Skill: `skills/employment/employee-policy-review/SKILL.md`

**Overlay considerations:**

- **HIPAA workforce training** — covered entities and BAs must train workforce members on HIPAA privacy and security policies and procedures `[verify current HHS rule]`. Confirm the policy addresses training scope, frequency, documentation, and refresher cadence.
- **Sanctions policy** — required element of HIPAA compliance; confirm the policy describes graduated sanctions for workforce violations and the documentation flow `[verify current HHS rule]`.
- **Minimum-necessary workforce training** — the minimum-necessary standard reaches workforce access to PHI; training and role-based access controls should align.
- **Access controls and audit-logging** — workforce-facing policies should address audit-logging expectations and the consequences of inappropriate-access events.
- **GINA and reproductive-health policies** — confirm employee handbooks address genetic-information non-discrimination and (in implicated jurisdictions) reproductive-health-information considerations `[verify jurisdiction]`.
- **BYOD and remote work** — for workforce members accessing ePHI from personal devices or off-premises, confirm policies address device security, lock-screen, encryption, and reporting of lost devices.
- **Reporting channel for suspected violations** — confirm the policy provides a confidential reporting channel and protections against retaliation.

### Skill: `skills/employment/internal-investigation/SKILL.md`

**Overlay considerations:**

- **Unauthorized PHI access (snooping) investigations** — these are a recurring healthcare-specific investigation type. The workflow involves access-log review, witness interviews, comparison against minimum-necessary justifications, and graduated sanctions per the sanctions policy.
- **Breach-notification interaction** — an investigation finding of unauthorized access may trigger breach-notification analysis under the HIPAA Breach Notification Rule, with separate notification flows. Surface the breach-notification question as a parallel-track item; route to HIPAA counsel for the notification determination `[verify current HHS rule]`.
- **Documentation discipline** — HIPAA enforcement is documentation-sensitive. Confirm the investigation documents the access pattern, the policy violated, the workforce member's explanation, the sanctions applied, and the breach-notification analysis.
- **Workforce-member privilege and union considerations** — many healthcare employers are subject to collective-bargaining-agreement procedures; route to labor counsel where applicable.
- **42 CFR Part 2 records** — investigations involving Part 2 records add separate consent and disclosure constraints.
- **Reproductive-health-related access** — heightened sensitivity post-Dobbs; route to specialist counsel `[verify jurisdiction]`.
- **Reporting to licensing boards** — workforce members with state-licensed roles (RN, MD, NP, pharmacist) may trigger separate reporting obligations to state licensing boards depending on the conduct and jurisdiction `[verify jurisdiction]`. Route to licensing-board counsel.

### Skill: `skills/regulatory/enforcement-risk-memo/SKILL.md`

**Overlay considerations:**

- **OCR enforcement posture** — OCR is the principal HIPAA enforcement agency. Address enforcement posture at the framework level: complaint-driven investigation, compliance review, breach-report-driven investigation, and audit `[verify current HHS rule]`. **Do not cite specific enforcement actions or settlement amounts.** Enforcement specifics age fast and create false-precision risk.
- **Civil money penalty tiers** — HIPAA / HITECH establishes tiered CMPs keyed to culpability (lack of knowledge, reasonable cause, willful neglect with timely correction, willful neglect without correction) with caps per violation and per calendar year `[verify current HHS rule]`. Reference at the tier-framework level only; do not state dollar amounts (the figures are adjusted periodically and are an attorney-verification item).
- **Resolution agreement and corrective-action-plan posture** — the overlay surfaces this as the standard enforcement endgame for material matters but does not predict outcome.
- **State AG enforcement** — under HITECH, state AGs have parallel HIPAA enforcement authority; CMIA, HB 300, MHMDA, SHIELD, and other state regimes also carry their own enforcement frameworks `[verify jurisdiction]`.
- **DOJ criminal enforcement** — willful HIPAA violations can carry criminal penalties; specialist counsel only.
- **FTC overlay** — FTC enforcement under §5 (deception/unfairness) and the Health Breach Notification Rule may overlay or substitute for HIPAA enforcement in the consumer-app / non-covered-entity space `[verify current FTC rule]`.
- **Concurrent jurisdictions** — a single breach may attract OCR, state AG, FTC, and licensing-board attention concurrently; surface as parallel tracks.

### Skill: `skills/regulatory/compliance-gap-matrix/SKILL.md`

**Overlay considerations:**

- **HIPAA gap-analysis spine** — Privacy Rule, Security Rule, Breach Notification Rule, Enforcement Rule, plus state-law overlays. The gap matrix should map controls to the rule sections rather than to a generic privacy framework.
- **Security Rule administrative / physical / technical safeguards** — each category has required and addressable specifications. Surface "addressable" as a documentation-of-decision posture, not as optional `[verify current HHS rule]`.
- **Risk analysis and risk management** — separate required elements of the Security Rule with specific documentation expectations.
- **Workforce-training and sanctions documentation** — distinct gap categories.
- **BAA-program audit** — the gap matrix should include a BAA-program element (template currency, sub-BA chain integrity, vendor inventory completeness, vendor-rated risk).
- **Breach-notification policies and incident-response procedures** — separate gap category.
- **State-law overlays** — for each in-scope state, surface the overlay rule's gap categories.
- **42 CFR Part 2 program** (if SUD program in scope), **GINA program** (if genetic data in scope), **FDA SaMD program** (if device-regulated software in scope) — each as a separate gap category routed to specialist counsel.

---

## 4. Escalation triggers specific to healthcare

Conditions that, in this sector, must stop a workflow and route the matter to a healthcare-specialist or supervising attorney before proceeding:

- **Confirmed or suspected breach affecting 500+ individuals.** Different notification path (individual + HHS + media). Triggering-fact date is `[deadline verification required]`; the timing framework itself is `[verify current HHS rule]`. Surface immediately; do not compute deadlines.
- **OCR investigation, audit notice, or data request received.** Stop, preserve records, do not respond without HIPAA counsel.
- **DEA or state-board licensing inquiry on a prescriber or pharmacy matter.** Route to DEA / state-board specialist counsel `[verify jurisdiction]`.
- **42 CFR Part 2 records or substance-use-facility involvement.** Part 2 specialist counsel.
- **Genetic-information involvement (GINA).** Surface and route to GINA-aware counsel `[verify current EEOC / HHS rule]`.
- **Reproductive-health information in the post-Dobbs landscape.** Specialist counsel; state-by-state analysis `[verify jurisdiction]`.
- **Pediatric data** — under-13 may add COPPA scope when in consumer-facing context; minor-consent rules vary by jurisdiction and care type `[verify jurisdiction]`.
- **Clinical decision support, diagnostic, or treatment-recommendation software.** FDA-SaMD counsel `[verify current FDA rule]`.
- **Anti-Kickback Statute or Stark Law implication** in a commercial arrangement (referral relationships, physician compensation, healthcare-space leases, professional-services agreements with referring providers). Fraud-and-abuse counsel `[verify current OIG / CMS rule]`.
- **Information-blocking complaint or developer / provider posture question.** ONC information-blocking specialist `[verify current ONC rule]`.
- **Government-program contract** (VA, IHS, FEHB, Medicare/Medicaid, TRICARE) with healthcare-specific compliance terms. Government-contracts counsel.
- **Consumer-facing health app entity claiming HIPAA-non-applicability.** Confirm covered-entity status; FTC Health Breach Notification Rule and state-law (MHMDA, CMIA) overlays may apply outside HIPAA `[verify jurisdiction]`.
- **Cross-border processing of PHI** to a non-U.S. jurisdiction, including AI-vendor offshore processing. Surface data-localization and program-contract restrictions.
- **Telemedicine across state lines** — state-by-state licensing and corporate-practice-of-medicine analysis `[verify jurisdiction]`. Route to healthcare regulatory counsel.

---

## 5. Standard healthcare-counsel positions to surface (as questions, not conclusions)

These are recurring negotiation and documentation positions a healthcare team needs to answer. The overlay surfaces the question; the organization (via `profile.md`) fills in the position; the supervising attorney confirms.

- **BAA template version control.** Which BAA template version is the organization using? When was it last reviewed? What fallback positions are acceptable on key terms (sub-BA approval mechanism, breach-notification timeline, indemnity, liability cap, audit rights)?
- **Vendor-supplied BAA vs. organization-template BAA.** What is the organization's default posture on accepting a vendor-supplied BAA? Below what risk threshold is vendor-paper acceptable? What are the must-change terms in a vendor-supplied BAA?
- **Insurance and indemnity floor for BAAs.** Minimum cyber-liability insurance limits; minimum indemnity scope (HIPAA violations, breach notification costs, regulatory fines, defense costs); whether the indemnity is uncapped for breach-notification costs.
- **Reporting timelines.** Every BAA frames BA-to-CE reporting differently (24 hours? 48 hours? 5 days? "without unreasonable delay"?). Route to attorney; surface the contract's actual posture without asserting which is correct under the rule `[verify current HHS rule]`.
- **Sub-BA approval mechanism.** Prior written approval per sub-BA, prior written approval for new categories, or general authorization with a maintained list? What objection rights does the CE retain?
- **Audit rights scope.** SOC 2 in lieu? Annual right? Triggered-only right? What is the cost-allocation posture?
- **De-identification mechanics.** Is the organization willing to accept vendor-side de-identification? Under what method (Safe Harbor or Expert Determination)? What documentation does the organization require? Always specialist counsel; the overlay never approves.
- **Training data and AI development use of PHI.** What is the organization's policy on permitting vendors to use PHI inputs for model training, fine-tuning, or product improvement? What about de-identified-by-the-vendor data?
- **Breach-notification chain of command.** Who decides whether an event is a "breach" (vs. unauthorized acquisition / disclosure that is not a breach)? Who signs notification letters? Who coordinates media notification (for 500+ events) and the HHS notification?
- **Incident-response retainer.** Forensic vendor on standing retainer? Notification-letter vendor? Call-center vendor? Credit-monitoring posture?
- **Workforce-sanctions framework.** Graduated sanctions for snooping vs. inadvertent access vs. willful misuse? Documentation flow? Reporting to licensing boards where applicable?
- **Right-of-access response time and format defaults.** How does the organization handle electronic copies, alternative formats, third-party-recipient delivery, and the fee posture for individual access requests? Who handles HIPAA right-of-access requests vs. CCPA / state-law access requests when they arrive together?
- **NPP currency and acknowledgment posture.** How often is the NPP reviewed? What triggers an out-of-cycle update (rule change, NPRM finalization, material practice change)? What is the acknowledgment-collection posture for new patients and for existing patients on NPP updates?
- **Risk analysis cadence.** How often does the organization update its Security Rule risk analysis? What triggers an out-of-cycle update (material system change, breach, M&A)?
- **Vendor-tiering rubric.** Does the organization tier BAs by sensitivity, volume of PHI, or system criticality? How does the tier drive diligence, BAA-template selection, audit frequency, and incident-response expectations?
- **M&A diligence posture.** What HIPAA / state-law diligence does the organization run on acquired entities? Successor-liability framing? Pre-close vs. post-close access posture?
- **AI training data and synthetic data.** Beyond the per-vendor question, what is the organization's framework for using PHI to train its own internal models? What documentation does it require?

---

## 6. Loading sequence and interaction with other overlays

When this overlay is loaded, the agent should observe the load order described in `overlays/README.md`:

1. `core/` operating rules (the absolute floor).
2. The relevant practice profile from `practice-profiles/`.
3. The selected skill's `SKILL.md`.
4. This overlay's `OVERLAY.md` and `profile.md`.

This overlay frequently runs alongside other overlays where they exist — for example, a fintech-payments overlay for healthcare-payment matters, or an education overlay for academic-medical-center matters. When multiple overlays apply, each adds gates and verification items; none subtracts. If two overlays appear to conflict on a position, the supervising attorney resolves; the agent surfaces the conflict and does not silently pick.

The overlay is also designed to compose with the cluster-level reference catalogs (`skills/contracts/references/red-flags.md`, `skills/antitrust-competition/references/risk-indicators.md`, `skills/securities-capital-markets/references/issue-spotting-frameworks.md`) — those catalogs handle the cross-sector patterns; this overlay adds the healthcare-layer attorney-verification items on top.

---

## 7. What this overlay does NOT do

- **No HIPAA training content.** Workforce training is its own deliverable; this overlay does not produce it.
- **No breach-notification letters.** Letter generation is a downstream drafting task. When a notification-drafting skill exists, route to it; until then, route to specialist counsel.
- **No de-identification opinion.** The overlay never concludes that Safe Harbor or Expert Determination has been satisfied. Always specialist counsel — for Expert Determination, a qualified statistician or equivalent expert.
- **No covered-entity / business-associate determination.** Surface as a question for counsel.
- **No conduit-exception application.** The conduit exception is narrow and contested. Always specialist counsel.
- **No clinical-practice, scope-of-practice, licensing, prescribing, telemedicine-permission, or controlled-substances guidance.** Route to state-board / DEA counsel.
- **No insurance-regulation guidance** (state insurance commissioner, ACA / MHPAEA / ERISA-plan compliance). Route to insurance counsel.
- **No fraud-and-abuse opinion** (AKS, Stark, civil monetary penalty, FCA exposure). Route to fraud-and-abuse counsel.
- **No FDA SaMD or device-regulation opinion.** Route to FDA counsel.
- **No information-blocking opinion.** Route to ONC counsel.
- **No 42 CFR Part 2 opinion.** Route to Part 2 specialist counsel.
- **No state-law-of-the-week opinion.** Every state-specific note carries `[verify jurisdiction]`; the overlay surfaces the question, never concludes.

---

## How to use this overlay

Load it, after the `core/` rules, the relevant practice profile, and the chosen skill, when the matter involves healthcare or life-sciences facts. See `overlays/README.md` for the load order.

The overlay sharpens the skill for the sector. It adds gates, terminology, and attorney-verification items; it never replaces the skill, the `core/` rules, or the supervising attorney.

## Status

`experimental` — the first overlay built under the overlays/ scaffold. To be promoted to `stable` once a supervising healthcare-counsel reviewer has confirmed the framework references, the per-skill tuning notes have been exercised on at least one real matter, and `profile.md` has been completed for the organization. Recorded in `docs/PRACTICE_AREAS.md`.
