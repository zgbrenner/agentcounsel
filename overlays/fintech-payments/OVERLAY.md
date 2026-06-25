# Fintech and Payments Overlay

This overlay tunes AgentCounsel's existing skills for **fintech and payments** work — money-transmitters, payment processors, payment facilitators (PayFacs), program managers, neobanks and banking-as-a-service (BaaS) providers, card issuers and acquirers, lending and buy-now-pay-later platforms, wallets, remittance and cross-border-transfer services, crypto / digital-asset firms, and the SaaS vendors and sponsor banks that serve them. It is internal configuration material, not legal advice and not legal work product. A supervising attorney reviews it before use.

Fintech is a sector, not a body of law. A payments company's legal work is contracts work, privacy work, regulatory work, financial-crime work, and product-legal work — coloured by money-transmission and money-services-business regimes, by card-network operating rules, by anti-money-laundering (AML) and sanctions obligations, and by sector-specific regulators. This overlay supplies that colouring; it never replaces the underlying skills, the `core/` operating rules, or the supervising attorney.

---

## 1. Scope of the overlay

### Skills this overlay tunes

The overlay is most often loaded alongside skills in these clusters:

- **Contracts** — payment-processing agreements, sponsor-bank / BaaS agreements, network and scheme participation agreements, vendor agreements (KYC / fraud / ledger vendors), vendor-agreement inventory, contract risk review, SOW review.
- **Privacy** — DPA review where account, transaction, and device data are processed; Privacy Impact Assessment for payment flows; DSAR workflow against financial-data records; privacy-policy gap review for a regulated financial entity.
- **Regulatory** — enforcement-risk memos, compliance gap matrices, and rule-change tracking across money-transmission, prudential, and consumer-financial regimes.
- **Financial crime** — KYC / customer-onboarding review and sanctions-screening review tuned for a payments customer base, agents, and counterparties.
- **Product legal** — terms-of-service review, marketing-claims review, and launch review for a payments / lending / crypto product.

The per-skill tuning notes appear in Section 3 below.

### What the overlay is NOT

- It does **not** contain skills. Per `overlays/README.md`, overlays never contain skills.
- It does **not** replace specialist fintech counsel — money-transmission / MSB licensing counsel, banking and prudential-regulatory counsel, consumer-financial-services counsel, BSA / AML and sanctions counsel, card-network-rules counsel, securities counsel (for digital-asset and tokenization questions), and tax counsel all remain required for their respective domains.
- It does **not** provide jurisdiction-specific licensing, chartering, capital, surety-bond, permissible-investment, lending-license, usury, disclosure, or registration guidance. Each of those areas has its own framework that a fintech specialist must apply `[VERIFY current law / jurisdiction]`.
- It does **not** state money-transmission, BSA / AML, OFAC-sanctions, card-network, consumer-financial-protection, securities, or any other requirements. Every regime reference in this overlay is a framework reference, not a statement of law `[VERIFY current law / jurisdiction]`.
- It does **not** state any threshold, dollar amount, transaction limit, reporting trigger, capital figure, bonding amount, or penalty figure. Thresholds vary by regime and by jurisdiction and change over time; each is `[VERIFY current law / jurisdiction]`.
- It does **not** compute filing deadlines, cure periods, network-dispute windows, or any other deadlines.

---

## 2. The fintech regulatory architecture (orientation only — not legal advice)

This section orients an agent loading the overlay. None of it is a statement of law. Every framework reference carries `[VERIFY current law / jurisdiction]` because the payments regulatory landscape spans multiple federal and state regimes, private network rulebooks, and non-U.S. frameworks, each of which is amended on its own cycle `[VERIFY current law / jurisdiction]`.

### 2.1 Who is regulated, and as what

The first question in almost every payments matter is *what is the entity, legally, and which regime captures the activity?* This is fact-intensive and is an attorney determination — the overlay never concludes regulatory status or licensing requirements.

- **Money transmitters / money services businesses (MSBs)** — entities that transmit funds, issue or sell stored value, exchange currency, or perform similar activities may be regulated as money transmitters under state law and as MSBs under federal AML law `[VERIFY current law / jurisdiction]`. The money-transmitter determination is jurisdiction-by-jurisdiction and an attorney determination in every case.
- **Banks, sponsor banks, and BaaS arrangements** — chartered depository institutions and the fintech programs that ride on a sponsor bank's charter sit inside a separate prudential-regulatory regime; the allocation of regulatory responsibility between the bank and the fintech is a fact-intensive determination `[VERIFY current law / jurisdiction]`.
- **Payment facilitators, ISOs, and agents of a payee** — roles defined largely by card-network rules and by state law; classification drives licensing, registration, and flow-down obligations `[VERIFY current law / jurisdiction]`.
- **Lenders, credit providers, and BNPL** — captured by lending-license, usury, disclosure, and consumer-credit regimes that vary by product structure and jurisdiction `[VERIFY current law / jurisdiction]`.
- **Digital-asset and crypto firms** — may be captured concurrently by money-transmission regimes, by securities or commodities regimes, by AML regimes, and by jurisdiction-specific digital-asset frameworks; the classification of any specific token, product, or activity is a specialist determination `[VERIFY current law / jurisdiction]`.

### 2.2 The principal regimes (framework level only)

Each regime has substantial substantive content beyond what is sketched here; the overlay surfaces the framework so that a supervising attorney can apply the current text of the applicable rule. None of the following enumerates a threshold, a dollar figure, or a deadline.

**State money-transmission and MSB licensing** — state-by-state licensing, surety-bond, permissible-investment, net-worth, change-of-control, agent-oversight, and reporting frameworks `[VERIFY current law / jurisdiction]`. Principal framework elements:
- Licensing triggers keyed to the activity and to the location of the customer or transaction; multistate coverage where the entity serves customers nationwide.
- Surety-bond and permissible-investment requirements `[VERIFY current law / jurisdiction]` — the overlay never states the amount or the qualifying-asset categories.
- Change-of-control and ownership-disclosure requirements; advance-notice or approval triggers `[VERIFY current law / jurisdiction]`.
- Agent / authorized-delegate oversight obligations.
- Periodic reporting and examination obligations to the chartering or licensing authority.
- Multistate coordination frameworks for licensing and examination exist; the overlay does not assert which apply to a given entity `[VERIFY current law / jurisdiction]`.

**Bank Secrecy Act / AML framework** — customer identification, customer due diligence, beneficial-ownership, transaction monitoring, suspicious-activity reporting, currency-transaction reporting, and recordkeeping obligations for regulated entities `[VERIFY current law / jurisdiction]`. Principal framework elements:
- A risk-based AML program with the commonly described pillars — designated compliance officer, internal controls, independent testing, training, and risk-based customer due diligence `[VERIFY current law / jurisdiction]`.
- Customer-identification and customer-due-diligence (CDD) frameworks, including enhanced due diligence (EDD) for higher-risk relationships, and beneficial-ownership identification `[VERIFY current law / jurisdiction]`.
- Suspicious-activity and currency-transaction reporting frameworks `[VERIFY current law / jurisdiction]` — the overlay never states the reporting threshold, the filing deadline, or the form. Reporting timing is `[deadline verification required]`.
- Recordkeeping frameworks, including funds-transfer and value-transfer recordkeeping `[VERIFY current law / jurisdiction]`.
- Confidentiality of suspicious-activity reporting — the existence and content of a suspicious-activity report is itself subject to disclosure prohibitions; treat any such material as highly restricted `[VERIFY current law / jurisdiction]`.

**Economic-sanctions framework (OFAC and non-U.S. equivalents)** — prohibitions on dealings with sanctioned persons, jurisdictions, and activities; screening, blocking, rejecting, and reporting obligations `[VERIFY current law / jurisdiction]`. Principal framework elements:
- List-based and jurisdiction-based prohibitions; the lists and programs change frequently `[VERIFY current law / jurisdiction]`.
- Screening of customers, counterparties, beneficial owners, and transaction parties at onboarding and on an ongoing basis.
- Blocking vs. rejecting determinations and the associated reporting obligations `[VERIFY current law / jurisdiction]` — an attorney / sanctions-specialist determination; the overlay never concludes whether to block or reject.
- Strict-liability exposure in many sanctions contexts; the overlay never opines on liability.
- Non-U.S. sanctions regimes may apply concurrently and may diverge from the U.S. program `[VERIFY current law / jurisdiction]`.

**Card-network and scheme operating rules** — the private rulebooks of the payment card networks and other payment schemes govern participation, data security, dispute / chargeback handling, interchange, surcharging, brand use, and prohibited and high-risk categories `[VERIFY current network rules]`. Principal framework elements:
- Participation and registration categories (issuer, acquirer, processor, payment facilitator, ISO, agent) with their respective obligations.
- Dispute, chargeback, and representment frameworks with network-defined windows `[VERIFY current network rules]` — the overlay never states the window length and never computes a dispute deadline.
- Data-security program requirements imposed by the networks `[VERIFY current network rules]` — distinct from, and additional to, statutory data-protection law.
- Brand-use, surcharging, and steering rules that vary by network and by jurisdiction `[VERIFY current network rules]` `[VERIFY current law / jurisdiction]`.
- Prohibited, restricted, and high-brand-risk merchant categories, and the monitoring programs that police them.
- Network rules are private contractual frameworks, not law; they bind through the participation agreements and are enforced by the networks. The overlay treats them as framework references only `[VERIFY current network rules]`.

**Payment-card data-security framework (industry standard)** — the payment-card-industry data-security standard and related industry frameworks impose requirements on entities that store, process, or transmit cardholder data `[VERIFY current standard version]`. Principal framework elements:
- Scope determination keyed to how cardholder data is handled, including the effect of tokenization, point-to-point encryption, and outsourcing on scope.
- Self-assessment vs. independent-assessment pathways depending on the entity's category and volume `[VERIFY current standard version]`.
- The standard is an industry framework, not a statute; contractual and network obligations give it force. The overlay never asserts that any entity is or is not compliant.

**Consumer-financial-protection framework** — federal and state consumer-financial regimes govern disclosures, error-resolution, unfair / deceptive / abusive acts or practices (UDAP / UDAAP), fund-availability, electronic-fund-transfer rights, prepaid-account rules, remittance-transfer disclosures, fair-lending, fair-credit-reporting, and debt-collection conduct `[VERIFY current law / jurisdiction]`. Principal framework elements:
- Electronic-fund-transfer and error-resolution frameworks for consumer accounts, including liability-allocation and investigation timelines `[VERIFY current law / jurisdiction]` — the overlay never states the timeline.
- Remittance-transfer and cross-border-transfer disclosure and cancellation frameworks `[VERIFY current law / jurisdiction]`.
- Prepaid-account and stored-value consumer-protection frameworks `[VERIFY current law / jurisdiction]`.
- Lending and credit disclosure, fair-lending, and credit-reporting frameworks where the entity extends or facilitates credit `[VERIFY current law / jurisdiction]`.
- UDAP / UDAAP exposure attaches broadly to consumer-facing conduct and marketing; surface marketing and disclosure questions for product-legal and consumer-financial-services counsel.

**Securities and commodities overlay (digital assets and tokenization)** — certain digital-asset products, tokens, yield features, and structured arrangements may implicate securities or commodities regimes concurrently with money-transmission and AML regimes `[VERIFY current law / jurisdiction]`. The classification of any specific token or arrangement is a specialist determination; the overlay never concludes whether an instrument is a security or how it is regulated.

### 2.3 Jurisdiction and cross-border layers

Payments are inherently cross-border, and a single flow can touch many regimes at once. Each note below carries `[VERIFY current law / jurisdiction]`:

- **Multistate U.S. licensing** — an entity serving U.S. customers nationwide may need authorization in many states; the analysis is state-by-state and is an attorney determination `[VERIFY current law / jurisdiction]`.
- **Non-U.S. payment and e-money regimes** — many jurisdictions regulate payment institutions, e-money issuers, and money-remittance businesses under their own authorization, safeguarding, and conduct frameworks `[VERIFY current law / jurisdiction]`. The overlay names none of them as authority and asserts no requirement.
- **Cross-border data transfer** — account, transaction, device, and KYC data moving across borders implicates data-protection transfer frameworks alongside financial-data-localization rules in some jurisdictions `[VERIFY current law / jurisdiction]`.
- **Travel-rule-style value-transfer recordkeeping** — funds-transfer and value-transfer recordkeeping and information-sharing frameworks apply in many regimes, including to certain digital-asset transfers `[VERIFY current law / jurisdiction]`.

The overlay carries `[VERIFY current law / jurisdiction]` on every jurisdiction-specific note. None of the above is a statement of any jurisdiction's law.

### 2.4 The sponsor-bank / BaaS layer

A large share of fintech activity rides on a sponsor bank's charter. This arrangement creates a distinct set of framework concerns `[VERIFY current law / jurisdiction]`:

- **Allocation of regulatory responsibility** between the bank and the fintech program — who owns BSA / AML, who owns consumer-compliance, who owns complaint handling, who owns the customer relationship of record.
- **Third-party-risk-management expectations** that flow from the bank's regulators onto the fintech as the bank's service provider `[VERIFY current law / jurisdiction]`.
- **Funds-flow and settlement mechanics**, including how customer funds are held, whether they are held for-benefit-of customers, and how funds are protected on insolvency `[VERIFY current law / jurisdiction]`.
- **Deposit-insurance representations** — claims about pass-through deposit insurance are tightly constrained and frequently mis-stated; surface every such claim for the bank's and the entity's counsel `[VERIFY current law / jurisdiction]`.
- **Program wind-down and exit** — what happens to customers, funds, and data if the bank or the program terminates the relationship.

The overlay surfaces these as framework concerns and routing flags; the substantive allocation is an attorney determination, typically requiring both the fintech's and the sponsor bank's counsel.

### 2.5 Terminology an agent should recognize and use precisely

These terms recur in fintech and payments matters and carry specific meanings. The overlay does not redefine them; use them as the law and the industry use them, and confirm with counsel when the substantive meaning matters.

- **MSB / money transmitter / money services business** — AML- and state-licensing-regulated activity categories.
- **PayFac (payment facilitator), ISO (independent sales organization), acquirer, issuer, processor, agent of a payee** — payments-ecosystem roles, defined largely by network rules and state law.
- **Sponsor bank, BaaS (banking-as-a-service), program manager** — bank-fintech-partnership roles.
- **KYC, CDD, EDD, CIP, beneficial ownership** — customer-identification and due-diligence terms of art.
- **BSA / AML, SAR, CTR, AML program** — Bank-Secrecy-Act and anti-money-laundering terms of art. Treat suspicious-activity-report existence and content as restricted `[VERIFY current law / jurisdiction]`.
- **OFAC, SDN, blocking, rejecting, screening** — economic-sanctions terms of art.
- **PEP (politically exposed person), sanctions screening, adverse-media screening** — onboarding-risk terms.
- **Chargeback, dispute, representment, interchange, surcharging, steering** — card-network terms of art.
- **PCI DSS, cardholder data, tokenization, point-to-point encryption (P2PE)** — payment-card data-security terms.
- **EFT, error resolution, Reg-E-style consumer protections, fund availability, prepaid account, remittance transfer** — consumer-financial-protection terms (referenced generically; the overlay states no rule) `[VERIFY current law / jurisdiction]`.
- **UDAP / UDAAP** — unfair, deceptive, (and) abusive acts or practices.
- **Usury, finance charge, APR, lending license, BNPL** — credit-and-lending terms.
- **Stored value, e-money, for-benefit-of (FBO) account, permissible investments, surety bond, net worth, change of control** — money-transmission prudential terms.
- **Stablecoin, custody, wallet (custodial / non-custodial), on-ramp / off-ramp, travel rule** — digital-asset terms.
- **Settlement, clearing, ACH-style transfer, RTP-style instant transfer, push-to-card** — funds-movement terms (referenced generically).
- **Pass-through deposit insurance** — a constrained representation; surface every claim for counsel.

---

## 3. Per-skill tuning notes

For each skill in the affected clusters below, the overlay names the specific fintech-layer concerns a supervising attorney should add to the standard review. The overlay does not alter the skill; it adds attorney-verification items.

### Skill: `skills/contracts/contract-risk-review/SKILL.md`

**Overlay considerations:**

- **Regulatory-role allocation** — for payment-processing, sponsor-bank / BaaS, and program-management agreements, surface how the contract allocates BSA / AML, sanctions, consumer-compliance, complaint-handling, and customer-of-record responsibility between the parties. A contract that is silent on these allocations is a flagged gap `[VERIFY current law / jurisdiction]`.
- **Network-rules flow-down** — payment-processing and sponsorship agreements typically flow down card-network and scheme operating rules. Surface the flow-down's existence and breadth; the overlay does not interpret the network rules `[VERIFY current network rules]`.
- **Funds-flow, settlement, and FBO mechanics** — surface how customer funds move and are held (including for-benefit-of-customer structures), settlement timing, reserve and holdback rights, and what happens to funds on default or insolvency `[VERIFY current law / jurisdiction]`.
- **Change-of-control and licensing triggers** — note whether a transfer, ownership change, or new activity could trigger a licensing, registration, or regulator-notice obligation. Surface the question; route to licensing counsel `[VERIFY current law / jurisdiction]`.
- **Indemnity and liability adequacy** — for payments matters, assess whether the liability cap bears any relationship to realistic exposure: regulatory penalties, network fines and assessments, chargeback and fraud losses, breach-notification costs, and reserve clawbacks. Vendor and processor caps often run well below realistic payments exposure.
- **Audit and examination rights** — confirm audit rights support the entity's own regulatory-examination and third-party-risk-management needs, not just a generic security-attestation substitute.
- **Termination and wind-down** — surface customer-transition, funds-return, and data-return mechanics on termination, which in payments carry consumer-protection and funds-safeguarding weight.

### Skill: `skills/contracts/vendor-agreement-status/SKILL.md`

**Overlay considerations:**

- **Critical-vendor inventory** — for each vendor in the payments stack (sponsor bank, processor, KYC / identity vendor, sanctions- and fraud-screening vendor, ledger / wallet infrastructure, dispute / chargeback vendor), confirm: contract executed? current version? regulatory-role allocation clear? flow-down obligations in place? termination / data-return / funds-return mechanics in place? Surface vendors missing these as flagged exposure.
- **Third-party-risk-management coverage** — sponsor-bank arrangements push third-party-risk-management expectations onto the fintech; surface whether each critical vendor relationship is covered by the entity's third-party-risk-management program `[VERIFY current law / jurisdiction]`.
- **Subcontractor / fourth-party chains** — where a vendor relies on its own subcontractors that touch funds, KYC data, or cardholder data, the oversight chain must continue. Surface chain gaps.
- **Network-registration status** — for processors, PayFacs, and ISOs, surface whether required network registrations are current `[VERIFY current network rules]`.
- **Data-handling addendum vs. financial-data terms** — confirm the vendor's data-protection terms match the sensitivity of the financial, transaction, device, and KYC data actually processed.

### Skill: `skills/privacy/dpa-review/SKILL.md`

**Overlay considerations:**

- **Financial-data sensitivity** — account numbers, card data, transaction histories, balances, device and behavioral signals, and KYC documentation are high-sensitivity categories. Confirm the DPA's safeguards, sub-processor controls, and breach terms match that sensitivity `[VERIFY current law / jurisdiction]`.
- **Cardholder-data scope** — where cardholder data is processed, confirm the DPA addresses payment-card data-security obligations and tokenization / encryption boundaries that affect scope `[VERIFY current standard version]`. Surface the question; the overlay never asserts compliance.
- **Cross-border transfer plus financial-data-localization** — supplement the generic transfer analysis with any financial-data-localization or in-jurisdiction-processing constraints that some regimes impose on payment or KYC data `[VERIFY current law / jurisdiction]`.
- **Sanctions- and AML-driven retention** — financial-crime regimes impose recordkeeping obligations that interact with data-minimization and deletion commitments; surface the tension and route to AML counsel `[VERIFY current law / jurisdiction]`. Do not collapse a deletion commitment into a recordkeeping obligation, or vice versa.
- **Breach-notification interplay** — payment-data incidents can trigger statutory breach-notification, network-incident-reporting, and contractual-reporting obligations concurrently. **Do not compute notification deadlines** — every triggering-fact date is `[deadline verification required]`, and each notification framework is `[VERIFY current law / jurisdiction]` `[VERIFY current network rules]`.
- **Definitions audit** — confirm the DPA's definitions of "personal data," "cardholder data," "breach," and "security incident" track the applicable frameworks rather than an idiosyncratic vendor-supplied definition.

### Skill: `skills/privacy/pia-generation/SKILL.md`

**Overlay considerations:**

- **Data-category mapping** — surface the payment-flow data categories (account, card, transaction, device, geolocation, KYC / identity documents, beneficial-ownership data) and flag categorization as an attorney determination.
- **Purpose-and-use mapping** — distinguish payment-execution uses from fraud-prevention, credit-decisioning, marketing, and model-training uses, each of which carries a different privacy and consumer-financial posture `[VERIFY current law / jurisdiction]`.
- **Automated decisioning** — where the flow includes automated fraud-scoring, credit-decisioning, or risk-based account actions, surface fair-lending, adverse-action, and automated-decisioning considerations for product-legal and consumer-financial-services counsel `[VERIFY current law / jurisdiction]`.
- **Financial-crime cross-reference** — confirm the PIA notes the AML / sanctions recordkeeping and screening data flows without asserting compliance with any AML obligation.
- **Cross-border processing** — surface every cross-border data movement for transfer-mechanism and financial-data-localization review `[VERIFY current law / jurisdiction]`.

### Skill: `skills/privacy/dsar-workflow/SKILL.md`

**Overlay considerations:**

- **Recordkeeping-obligation conflict** — financial-crime and other financial-services recordkeeping obligations may require retention of data a deletion or access request would otherwise reach; surface the conflict and route to AML / regulatory counsel `[VERIFY current law / jurisdiction]`. Never resolve a deletion request against a regulatory-retention obligation without counsel.
- **Suspicious-activity-report material** — any data tied to suspicious-activity reporting is subject to disclosure prohibitions; a subject-access request does not reach it, and its existence may not be disclosed `[VERIFY current law / jurisdiction]`. Surface and route; do not include such material in a response.
- **Identity-verification for sensitive financial records** — heightened verification is appropriate before disclosing financial-account data; surface the verification posture.
- **Concurrent frameworks** — a single request may trigger multiple data-subject-rights regimes plus financial-services-specific access rules; surface the parallel tracks and do not collapse them into one workflow `[VERIFY current law / jurisdiction]`.

### Skill: `skills/privacy/privacy-policy-gap-review/SKILL.md`

**Overlay considerations:**

- **Financial-privacy notice layer** — a regulated financial entity may owe a distinct financial-privacy notice with its own content, timing, and opt-out framework, separate from a general consumer-facing privacy policy `[VERIFY current law / jurisdiction]`. Confirm the gap review distinguishes the two and flags any inconsistency.
- **Information-sharing and opt-out** — financial-privacy frameworks frequently regulate sharing with affiliates and non-affiliated third parties and require specific opt-out mechanics `[VERIFY current law / jurisdiction]`.
- **Marketing and consumer-financial disclosure** — surface UDAP / UDAAP exposure in privacy and marketing language; route consumer-facing claims to product-legal and consumer-financial-services counsel.
- **Crypto / digital-asset disclosures** — where the entity offers digital-asset products, surface risk-disclosure, custody, and not-deposit-insured-style framing for counsel `[VERIFY current law / jurisdiction]`.

### Skill: `skills/regulatory/enforcement-risk-memo/SKILL.md`

**Overlay considerations:**

- **Multi-regulator posture** — payments matters can attract state money-transmission regulators, federal banking and consumer-financial regulators, AML / sanctions authorities, and the card networks concurrently. Address enforcement posture at the framework level only `[VERIFY current law / jurisdiction]`. **Do not cite specific enforcement actions, consent orders, or settlement amounts.** Enforcement specifics age fast and create false-precision risk.
- **Penalty frameworks** — reference penalty exposure at the framework level only; do not state dollar amounts, per-violation figures, or network-fine schedules — each is `[VERIFY current law / jurisdiction]` `[VERIFY current network rules]` and an attorney-verification item.
- **Network-fine and assessment posture** — the networks impose their own monitoring programs, fines, and assessments distinct from regulatory penalties `[VERIFY current network rules]`. Surface at the framework level; do not quantify.
- **Strict-liability sanctions exposure** — sanctions enforcement is, in many contexts, strict-liability; surface the posture and route to sanctions counsel `[VERIFY current law / jurisdiction]`.
- **Concurrent jurisdictions** — a single event can attract multiple regulators and the networks at once; surface as parallel tracks.

### Skill: `skills/regulatory/compliance-gap-matrix/SKILL.md`

**Overlay considerations:**

- **Multi-regime spine** — structure the gap matrix around the regimes that actually apply to the entity — money-transmission / MSB licensing, BSA / AML, sanctions, card-network rules, payment-card data security, and consumer-financial protection — rather than a single generic compliance framework `[VERIFY current law / jurisdiction]`.
- **AML-program elements** — surface the commonly described AML-program elements (compliance officer, internal controls, independent testing, training, risk-based CDD) as distinct gap categories `[VERIFY current law / jurisdiction]`.
- **Sanctions-screening program** — surface screening coverage (customers, counterparties, beneficial owners, transaction parties), list-update cadence, and blocking / rejecting / reporting procedures as a distinct gap category `[VERIFY current law / jurisdiction]`.
- **Licensing register** — for each jurisdiction in which the entity operates, surface the licensing / registration status as a gap category; the overlay never concludes whether a license is required `[VERIFY current law / jurisdiction]`.
- **Network-rules and PCI program** — surface network-registration currency and payment-card data-security scope and assessment status as distinct gap categories `[VERIFY current network rules]` `[VERIFY current standard version]`.
- **Consumer-financial controls** — surface disclosure, error-resolution, complaint-handling, and UDAP / UDAAP-monitoring controls as distinct gap categories `[VERIFY current law / jurisdiction]`.
- **Sponsor-bank oversight** — where a sponsor-bank arrangement exists, surface the third-party-risk-management and oversight obligations as a distinct gap category `[VERIFY current law / jurisdiction]`.

### Skill: `skills/regulatory/rule-change-summary/SKILL.md`

**Overlay considerations:**

- **Multi-source change tracking** — relevant changes can come from state licensing authorities, federal regulators, AML / sanctions authorities, and the card networks; surface which source a tracked change comes from and treat the network rulebooks as a distinct source `[VERIFY current network rules]`.
- **No statement of the changed rule's content** — summarize that a change exists and where to verify it; do not state the operative text, threshold, or effective date as authority `[VERIFY current law / jurisdiction]`.
- **Effective-date discipline** — never compute or assert a compliance deadline arising from a rule change; flag every date `[deadline verification required]`.

### Skill: `skills/financial-crime/kyc-onboarding-review/SKILL.md`

**Overlay considerations:**

- **Risk-based CDD / EDD framework** — confirm the onboarding flow distinguishes standard from enhanced due diligence on a risk basis, and that beneficial-ownership identification is addressed for entity customers `[VERIFY current law / jurisdiction]`. The overlay surfaces the framework; it never concludes that any specific program is adequate.
- **Customer categories specific to payments** — surface heightened-risk categories common in payments (money-services-business customers, high-risk merchant categories, cross-border / remittance customers, digital-asset customers, PEPs) and route categorization to AML counsel `[VERIFY current law / jurisdiction]`.
- **Agent and sub-merchant onboarding** — for PayFac, ISO, and program-manager models, surface that agents, sub-merchants, and authorized delegates may carry their own onboarding-diligence obligations `[VERIFY current law / jurisdiction]` `[VERIFY current network rules]`.
- **Recordkeeping and retention** — surface the recordkeeping framework without stating the retention period `[VERIFY current law / jurisdiction]`.
- **Sanctions screening at onboarding** — confirm the onboarding flow includes sanctions and watchlist screening; route the screening logic to the sanctions-screening review.
- **No conclusion on customer admissibility** — the overlay never concludes whether a specific customer may or must be onboarded, declined, or offboarded; surface as an attorney / compliance determination.

### Skill: `skills/financial-crime/sanctions-screening-review/SKILL.md`

**Overlay considerations:**

- **Screening scope** — confirm screening covers customers, counterparties, beneficial owners, and transaction parties, at onboarding and on an ongoing basis, against current lists `[VERIFY current law / jurisdiction]`. The lists change frequently; list-update cadence is itself a control to surface.
- **Blocking vs. rejecting** — the blocking / rejecting determination and any associated reporting is a sanctions-specialist determination; the overlay never concludes which applies `[VERIFY current law / jurisdiction]`.
- **Strict-liability posture** — surface that sanctions exposure is, in many contexts, strict-liability, and that screening-process gaps carry weight independent of intent `[VERIFY current law / jurisdiction]`.
- **Cross-border / multi-regime screening** — non-U.S. sanctions regimes may apply concurrently and may diverge; surface the multi-regime question `[VERIFY current law / jurisdiction]`.
- **Match-handling and false-positive workflow** — surface the alert-disposition, escalation, and documentation workflow; documentation discipline is enforcement-sensitive.
- **No hit / no-hit conclusion** — the overlay never concludes whether a name is or is not a true match; surface as a compliance / counsel determination.

### Skill: `skills/product-legal/terms-of-service-review/SKILL.md`

**Overlay considerations:**

- **Required consumer-financial disclosures** — payments, lending, and stored-value products carry mandated disclosure, error-resolution, fund-availability, and (for cross-border) remittance frameworks that a generic terms-of-service review does not capture `[VERIFY current law / jurisdiction]`. Surface the question; route to consumer-financial-services counsel.
- **Deposit-insurance and custody framing** — surface any deposit-insurance, pass-through-insurance, "your money is safe," or custody representation for counsel; these are tightly constrained and frequently mis-stated `[VERIFY current law / jurisdiction]`.
- **Fees, holds, reserves, and account-closure terms** — surface fee-disclosure, holdback / reserve, and unilateral-closure or fund-freeze terms for UDAP / UDAAP and consumer-financial review `[VERIFY current law / jurisdiction]`.
- **Dispute and chargeback terms** — confirm consumer-facing dispute terms are consistent with both the applicable consumer-financial framework and the network rules `[VERIFY current law / jurisdiction]` `[VERIFY current network rules]`.
- **Arbitration, class-waiver, and governing-law clauses** — surface for review against the applicable consumer-financial and state-law constraints `[VERIFY current law / jurisdiction]`.
- **Crypto / digital-asset risk terms** — where digital-asset products are offered, surface custody, risk-disclosure, and not-deposit-insured framing `[VERIFY current law / jurisdiction]`.

### Skill: `skills/product-legal/marketing-claims-review/SKILL.md`

**Overlay considerations:**

- **UDAP / UDAAP exposure** — payments and lending marketing is a frequent source of unfair / deceptive / abusive-practice exposure; surface every superlative, comparative, "free," "instant," "no fees," "FDIC-insured," "bank account," or guaranteed-approval claim for substantiation and consumer-financial review `[VERIFY current law / jurisdiction]`.
- **Deposit-insurance and "bank" claims** — claims of deposit insurance or that a non-bank is a "bank" are tightly constrained; surface every such claim for counsel `[VERIFY current law / jurisdiction]`.
- **Credit and lending advertising** — APR, finance-charge, and credit-availability claims carry specific advertising-disclosure frameworks `[VERIFY current law / jurisdiction]`.
- **Crypto / digital-asset promotion** — yield, return, and safety claims for digital-asset products carry heightened scrutiny and may implicate securities frameworks `[VERIFY current law / jurisdiction]`. Route to securities and consumer-financial counsel.
- **Rewards and referral programs** — surface promotional-terms, disclosure, and abuse-control questions for review.

### Skill: `skills/product-legal/launch-review/SKILL.md`

**Overlay considerations:**

- **Licensing-readiness gate** — before launch into any jurisdiction, surface whether the activity could require a money-transmission, lending, e-money, or other license or registration there; route to licensing counsel `[VERIFY current law / jurisdiction]`. The overlay never clears a launch.
- **AML / sanctions-program readiness** — surface whether the AML program, CDD / EDD flows, and sanctions screening are in place for the launch population `[VERIFY current law / jurisdiction]`.
- **Sponsor-bank and network readiness** — where the product rides a sponsor bank or a network, surface bank-approval, network-registration, and program-agreement status `[VERIFY current law / jurisdiction]` `[VERIFY current network rules]`.
- **Consumer-disclosure readiness** — surface that required disclosures, error-resolution processes, and complaint handling are in place for the launch population `[VERIFY current law / jurisdiction]`.
- **Data-security and PCI scope** — surface the payment-card data-security scope and assessment posture for the launch architecture `[VERIFY current standard version]`.
- **Geographic gating** — surface whether the launch is correctly geo-gated to authorized jurisdictions and away from sanctioned ones `[VERIFY current law / jurisdiction]`.

---

## 4. Escalation triggers specific to fintech and payments

Conditions that, in this sector, must stop a workflow and route the matter to a fintech-specialist or supervising attorney before proceeding:

- **A new activity, product, or jurisdiction that may require a license, charter, or registration** (money transmission, e-money, lending, digital-asset, or similar). Route to licensing counsel; the overlay never concludes a license is or is not required `[VERIFY current law / jurisdiction]`.
- **A potential or actual sanctions hit, or a transaction touching a sanctioned person, jurisdiction, or activity.** Stop; route to sanctions counsel; do not block, reject, or release without counsel `[VERIFY current law / jurisdiction]`.
- **A suspicious-activity-reporting question, or any request touching suspicious-activity-report existence or content.** Treat as restricted; route to AML counsel; do not disclose `[VERIFY current law / jurisdiction]`.
- **An examination, investigation, subpoena, civil-investigative-demand, consent-order, or data request from any regulator or network.** Stop, preserve records, do not respond without counsel.
- **A network monitoring-program notice, fine, or high-risk-category designation** `[VERIFY current network rules]`. Route to network-rules counsel.
- **A confirmed or suspected breach of cardholder data or other financial / KYC data.** Multiple concurrent notification frameworks (statutory, network, contractual). Triggering-fact dates are `[deadline verification required]`; each framework is `[VERIFY current law / jurisdiction]` `[VERIFY current network rules]`. Surface immediately; do not compute deadlines.
- **A sponsor-bank arrangement entering, changing, or terminating**, or a dispute over the allocation of regulatory responsibility. Route to both the fintech's and the sponsor bank's counsel `[VERIFY current law / jurisdiction]`.
- **A digital-asset product, token, yield feature, or custody arrangement** that may implicate securities, commodities, or money-transmission regimes. Route to securities and digital-asset counsel `[VERIFY current law / jurisdiction]`.
- **A consumer-complaint pattern, UDAP / UDAAP concern, or fair-lending / adverse-action question.** Route to consumer-financial-services counsel `[VERIFY current law / jurisdiction]`.
- **A deposit-insurance, pass-through-insurance, or "bank" representation** in any customer-facing material. Surface for counsel before use `[VERIFY current law / jurisdiction]`.
- **A change of control, ownership change, or material new activity** that could trigger a regulator-notice or approval obligation. Route to licensing counsel `[VERIFY current law / jurisdiction]`.
- **Cross-border processing or movement of payment or KYC data** to another jurisdiction. Surface data-transfer and financial-data-localization questions `[VERIFY current law / jurisdiction]`.
- **A customer-funds-safeguarding, FBO-account, or insolvency-protection question.** Route to regulatory and (where relevant) bankruptcy / restructuring counsel `[VERIFY current law / jurisdiction]`.

---

## 5. Standard fintech-counsel positions to surface (as questions, not conclusions)

These are recurring negotiation and documentation positions a payments team needs to answer. The overlay surfaces the question; the organization (via `profile.md`) fills in the position; the supervising attorney confirms.

- **Licensing footprint and posture.** In which jurisdictions is the organization licensed or registered, in which is it relying on an exemption or a sponsor bank, and what is the trigger for adding a jurisdiction? Always an attorney determination `[VERIFY current law / jurisdiction]`.
- **Sponsor-bank arrangement posture.** Which sponsor bank(s), what is the allocation of BSA / AML, sanctions, consumer-compliance, and customer-of-record responsibility, and what are the acceptable fallback positions on each in a program agreement?
- **AML-program ownership.** Who is the designated AML compliance officer, who owns CDD / EDD policy, who owns transaction monitoring, and who signs off on suspicious-activity-reporting determinations?
- **Sanctions-screening posture.** Which screening tool and lists, what list-update cadence, what is the match-handling and blocking / rejecting workflow, and who makes the final call?
- **Customer-risk-rating and high-risk-category posture.** How does the organization risk-rate customers and merchants, which categories are prohibited or restricted, and what is the offboarding process?
- **Network-registration and rules posture.** Which network registrations does the organization hold, who tracks network-rule changes, and what is the chargeback / dispute-handling posture `[VERIFY current network rules]`?
- **PCI / data-security posture.** What is the organization's payment-card data-security scope (and the effect of tokenization / encryption on it), assessment pathway, and remediation process `[VERIFY current standard version]`?
- **Funds-flow and safeguarding posture.** How are customer funds held (FBO accounts, permissible investments, segregation), how is settlement timed, and how are funds protected on insolvency `[VERIFY current law / jurisdiction]`?
- **Consumer-disclosure and error-resolution posture.** What disclosures does each product carry, what is the error-resolution and complaint-handling process, and who owns UDAP / UDAAP monitoring?
- **Deposit-insurance and "bank" representation posture.** What may and may not be said about deposit insurance, pass-through insurance, and "bank" status, and who clears every such representation `[VERIFY current law / jurisdiction]`?
- **Breach- and incident-notification chain of command.** Who decides whether an incident triggers statutory, network, and contractual notification; who coordinates each notification flow; who is on the incident-response retainer?
- **Vendor / third-party-risk-management posture.** How does the organization tier critical vendors, what diligence and contract terms are required by tier, and how is the oversight chain (including sub-processors / fourth parties) maintained `[VERIFY current law / jurisdiction]`?
- **Digital-asset product posture** (if applicable). What is the organization's framework for classifying tokens and products, for custody, and for risk disclosure, and what is the specialist-counsel-involvement threshold `[VERIFY current law / jurisdiction]`?
- **Lending and credit posture** (if applicable). What is the organization's framework on usury, finance-charge and APR disclosure, fair-lending, adverse-action, and credit-reporting `[VERIFY current law / jurisdiction]`?
- **Change-of-control and regulatory-notice posture.** What corporate events trigger a regulator-notice or approval obligation, and who owns the filing `[VERIFY current law / jurisdiction]`?
- **Recordkeeping and retention posture.** How does the organization reconcile financial-crime and financial-services recordkeeping obligations with data-minimization and deletion commitments `[VERIFY current law / jurisdiction]`?

---

## 6. Loading sequence and interaction with other overlays

When this overlay is loaded, the agent should observe the load order described in `overlays/README.md`:

1. `core/` operating rules (the absolute floor).
2. The relevant practice profile from `practice-profiles/`.
3. The selected skill's `SKILL.md`.
4. This overlay's `OVERLAY.md` and `profile.md`.

This overlay frequently runs alongside other overlays where they exist — for example, a healthcare overlay for health-payment and health-savings-account matters, or an education overlay for tuition- and campus-payment matters. When multiple overlays apply, each adds gates and verification items; none subtracts. If two overlays appear to conflict on a position, the supervising attorney resolves; the agent surfaces the conflict and does not silently pick.

The overlay is also designed to compose with the cluster-level reference catalogs (`skills/contracts/references/red-flags.md`, `skills/antitrust-competition/references/risk-indicators.md`, `skills/securities-capital-markets/references/issue-spotting-frameworks.md`) — those catalogs handle the cross-sector patterns; this overlay adds the fintech- and payments-layer attorney-verification items on top.

---

## 7. What this overlay does NOT do

- **No licensing or registration opinion.** The overlay never concludes whether a money-transmission, e-money, lending, digital-asset, or other license or registration is required, in any jurisdiction. Always licensing counsel `[VERIFY current law / jurisdiction]`.
- **No statement of any threshold, dollar amount, transaction limit, capital figure, bond amount, fee, or penalty.** Each is `[VERIFY current law / jurisdiction]`.
- **No AML-program-adequacy opinion.** The overlay surfaces the program framework; it never concludes that a program is adequate. Always BSA / AML counsel.
- **No sanctions determination.** The overlay never concludes whether a name is a true match, whether to block or reject, or whether a transaction is permitted. Always sanctions counsel.
- **No suspicious-activity-reporting determination, and no disclosure of suspicious-activity-report material.** Always AML counsel; treat such material as restricted.
- **No securities or commodities classification of any token, product, or arrangement.** Always securities / digital-asset counsel.
- **No network-rules interpretation.** The card-network and scheme rulebooks are private frameworks the overlay references only; interpretation and registration questions go to network-rules counsel `[VERIFY current network rules]`.
- **No PCI / data-security compliance opinion.** The overlay never concludes that any entity is or is not compliant `[VERIFY current standard version]`.
- **No consumer-financial-disclosure opinion** (electronic-fund-transfer, remittance, prepaid, lending, fair-lending, credit-reporting). Route to consumer-financial-services counsel.
- **No deposit-insurance or "bank"-status clearance.** The overlay surfaces every such representation for counsel; it never clears one.
- **No funds-safeguarding or insolvency-protection opinion.** Route to regulatory and bankruptcy / restructuring counsel.
- **No deadline, filing window, cure period, or dispute-window computation.** Every date is `[deadline verification required]`.
- **No jurisdiction-of-the-week opinion.** Every jurisdiction-specific note carries `[VERIFY current law / jurisdiction]`; the overlay surfaces the question, never concludes.

---

## How to use this overlay

Load it, after the `core/` rules, the relevant practice profile, and the chosen skill, when the matter involves fintech or payments facts. See `overlays/README.md` for the load order.

The overlay sharpens the skill for the sector. It adds gates, terminology, and attorney-verification items; it never replaces the skill, the `core/` rules, or the supervising attorney.

## Status

`experimental` — built under the overlays/ scaffold and modeled on the healthcare overlay. To be promoted to `stable` once a supervising fintech-counsel reviewer has confirmed the framework references, the per-skill tuning notes have been exercised on at least one real matter, and `profile.md` has been completed for the organization. Recorded in `docs/PRACTICE_AREAS.md`.
