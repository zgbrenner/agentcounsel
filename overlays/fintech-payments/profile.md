# Fintech and Payments Overlay Profile

A sector configuration profile, in the same style as the files under `practice-profiles/`. It records how a team's work in **fintech and payments** differs from the general case.

This profile is **not** legal work product and **not** legal advice. It is internal configuration. It must be reviewed and approved by a supervising attorney — ideally a fintech / payments-specialist attorney — before it is loaded alongside any skill. Organization-specific values are left as `[ORGANIZATION TO FILL]` placeholders because this profile ships with the overlay scaffold, not with a specific organization's configuration.

The overlay's framework references (`OVERLAY.md`) are paired with this profile. The profile sets organization-specific positions; the OVERLAY.md sets sector-wide tuning. Both are subordinate to `core/` and to the supervising attorney.

---

## Sector and scope

- **Sector / client type:** fintech and payments — money-transmitters and money-services businesses, payment processors, payment facilitators (PayFacs) and ISOs, program managers and banking-as-a-service (BaaS) providers, neobanks, card issuers and acquirers, lending and buy-now-pay-later platforms, wallets, remittance and cross-border-transfer services, crypto / digital-asset firms, and the SaaS vendors and sponsor banks that serve any of the above.
- **In-scope activities:** contracts, privacy, regulatory, financial-crime, and product-legal work coloured by money-transmission / MSB regimes, BSA / AML and economic-sanctions obligations, card-network and scheme operating rules, payment-card data-security frameworks, consumer-financial-protection regimes, and (where applicable) securities / commodities frameworks for digital assets `[VERIFY current law / jurisdiction]`.
- **Out of scope:** specialist fintech regulatory work that routes to a separate practice — money-transmission / e-money / lending / digital-asset licensing and chartering, prudential and safety-and-soundness work, BSA / AML and sanctions substantive determinations, securities and commodities classification of tokens and products, card-network-rules interpretation and registration, consumer-financial-disclosure substantive analysis, tax, and funds-safeguarding / insolvency-protection structuring. The overlay surfaces these as routing flags; the work itself is performed by specialist counsel.

## Jurisdictions

- **Primary regulators / oversight bodies (referenced generically — confirm which apply):** state money-transmission / financial-services regulators; federal banking and prudential regulators; the federal consumer-financial-protection regulator; AML and economic-sanctions authorities; securities and commodities regulators (for digital-asset questions); the payment card networks and payment schemes (private rulemakers, not regulators); and the relevant non-U.S. payment, e-money, and conduct authorities where the organization operates `[VERIFY current law / jurisdiction]`. This profile names none of them as authority and asserts no requirement.
- **Jurisdictions of typical concern:** **every U.S. state and every non-U.S. jurisdiction in which the organization serves customers, holds customer funds, or processes payment or KYC data** — licensing, registration, and conduct requirements are jurisdiction-by-jurisdiction `[VERIFY current law / jurisdiction]`. Named focus jurisdictions, if any: `[ORGANIZATION TO FILL]`.
- **Jurisdictions requiring escalation to local or specialist counsel:** every jurisdiction where the activity may require a license, charter, or registration the organization does not hold; every jurisdiction whose sanctions or AML regime may apply concurrently; every jurisdiction into which payment or KYC data will be transmitted, stored, or processed (data-transfer and financial-data-localization analysis); and every jurisdiction in which a sponsor-bank or network arrangement adds local obligations `[VERIFY current law / jurisdiction]`.
- Sector-specific legal rules are always attorney-verification items. This profile does not state them, and states no threshold, dollar amount, or deadline.

## Sector gates and escalation thresholds

Conditions that must stop the workflow and route the matter to specialist or supervising attorney before proceeding (mirroring `OVERLAY.md` Section 4):

- A new activity, product, or jurisdiction that may require a license, charter, or registration — licensing counsel `[VERIFY current law / jurisdiction]`.
- A potential or actual sanctions hit, or a transaction touching a sanctioned person, jurisdiction, or activity — sanctions counsel; do not block, reject, or release without counsel `[VERIFY current law / jurisdiction]`.
- Any suspicious-activity-reporting question, or any request touching such a report's existence or content — AML counsel; treat as restricted and do not disclose `[VERIFY current law / jurisdiction]`.
- An examination, investigation, subpoena, civil-investigative-demand, consent-order, or data request from any regulator or network — preserve records; do not respond without counsel.
- A network monitoring-program notice, fine, or high-risk-category designation — network-rules counsel `[VERIFY current network rules]`.
- A confirmed or suspected breach of cardholder data or other financial / KYC data — multiple concurrent notification frameworks; surface immediately and do not compute deadlines `[VERIFY current law / jurisdiction]` `[VERIFY current network rules]`.
- A sponsor-bank arrangement entering, changing, or terminating, or a dispute over regulatory-responsibility allocation — the fintech's and the sponsor bank's counsel `[VERIFY current law / jurisdiction]`.
- A digital-asset product, token, yield feature, or custody arrangement that may implicate securities, commodities, or money-transmission regimes — securities / digital-asset counsel `[VERIFY current law / jurisdiction]`.
- A consumer-complaint pattern, UDAP / UDAAP concern, or fair-lending / adverse-action question — consumer-financial-services counsel `[VERIFY current law / jurisdiction]`.
- A deposit-insurance, pass-through-insurance, or "bank" representation in customer-facing material — counsel clears before use `[VERIFY current law / jurisdiction]`.
- A change of control, ownership change, or material new activity that could trigger a regulator-notice or approval obligation — licensing counsel `[VERIFY current law / jurisdiction]`.
- A customer-funds-safeguarding, FBO-account, or insolvency-protection question — regulatory and bankruptcy / restructuring counsel `[VERIFY current law / jurisdiction]`.

## Standard positions

These are the organization's default positions on recurring sector-specific issues. The overlay flags deviations; the supervising attorney confirms. All placeholders are deliberately left as `[ORGANIZATION TO FILL]` because the profile ships without an organization-specific config.

- **Licensing footprint:** `[ORGANIZATION TO FILL — the jurisdictions in which the organization is licensed or registered, those relying on an exemption or a sponsor bank, the trigger for adding a jurisdiction, and the owner of the licensing register.]`
- **Sponsor-bank arrangement posture:** `[ORGANIZATION TO FILL — sponsor bank(s); allocation of BSA / AML, sanctions, consumer-compliance, and customer-of-record responsibility; acceptable fallback positions on each in a program agreement; program wind-down terms.]`
- **AML-program ownership and fallback positions:** `[ORGANIZATION TO FILL — designated AML compliance officer; owners of CDD / EDD policy, transaction monitoring, and suspicious-activity-reporting determinations; independent-testing cadence.]`
- **Sanctions-screening posture:** `[ORGANIZATION TO FILL — screening tool and lists; list-update cadence; match-handling, escalation, and blocking / rejecting workflow; final decision-maker.]`
- **Customer- and merchant-risk-rating posture:** `[ORGANIZATION TO FILL — risk-rating methodology; prohibited and restricted categories; high-risk-category controls; offboarding process.]`
- **Network-registration and rules posture:** `[ORGANIZATION TO FILL — network registrations held; owner of network-rule-change tracking; chargeback / dispute-handling posture.]`
- **PCI / payment-card data-security posture:** `[ORGANIZATION TO FILL — data-security scope and the effect of tokenization / encryption on it; assessment pathway; remediation process; owner.]`
- **Funds-flow and safeguarding posture:** `[ORGANIZATION TO FILL — how customer funds are held (FBO accounts, permissible investments, segregation); settlement timing; reserve / holdback posture; insolvency-protection structure.]`
- **Consumer-disclosure and error-resolution posture:** `[ORGANIZATION TO FILL — per-product disclosure set; error-resolution and complaint-handling process; UDAP / UDAAP-monitoring owner.]`
- **Deposit-insurance and "bank"-representation posture:** `[ORGANIZATION TO FILL — what may and may not be said about deposit insurance, pass-through insurance, and "bank" status; the clearance owner for every such representation.]`
- **Incident- and breach-notification chain of command:** `[ORGANIZATION TO FILL — who decides whether an incident triggers statutory, network, and contractual notification; who coordinates each flow; incident-response retainer relationships.]`
- **Vendor / third-party-risk-management posture:** `[ORGANIZATION TO FILL — critical-vendor tiering; required diligence and contract terms by tier; oversight-chain (including sub-processor / fourth-party) maintenance.]`
- **Digital-asset product posture (if applicable):** `[ORGANIZATION TO FILL — token / product classification framework; custody model; risk-disclosure posture; specialist-counsel-involvement threshold.]`
- **Lending and credit posture (if applicable):** `[ORGANIZATION TO FILL — usury, finance-charge and APR disclosure, fair-lending, adverse-action, and credit-reporting framework; owner.]`
- **Jurisdiction-of-operations list:** `[ORGANIZATION TO FILL — every jurisdiction in which the organization serves customers, holds customer funds, or processes payment or KYC data, for licensing and conduct analysis.]`

## Heightened-handling rules

The following data categories, populations, or document types require heightened confidentiality and care, in addition to general financial-data handling:

- **Suspicious-activity-report material** — existence and content are subject to disclosure prohibitions; treat as highly restricted and route to AML counsel `[VERIFY current law / jurisdiction]`.
- **Sanctions investigation and blocking / rejecting material** — restricted; route to sanctions counsel `[VERIFY current law / jurisdiction]`.
- **Cardholder data and authentication data** — payment-card data-security obligations and scope rules apply; tokenization / encryption boundaries affect handling `[VERIFY current standard version]`.
- **KYC / customer-identification documentation and beneficial-ownership data** — high-sensitivity identity data; access-control and retention posture require care `[VERIFY current law / jurisdiction]`.
- **Full account numbers, card numbers, and credentials** — restricted; surface any deliverable that would expose them.
- **Customer-funds and settlement records** — relevant to safeguarding and insolvency-protection; handle with care.
- **Digital-asset custody keys and wallet material** — restricted; route custody questions to specialist counsel.
- **Records of customers or counterparties under investigation, declined, or offboarded** — preservation-and-access controls may apply on top of general handling.
- **Material concerning sponsor-bank examinations or regulator correspondence** — restricted; coordinate with the sponsor bank's counsel.

## Prohibited assumptions

The agent must never assume any of the following in fintech and payments matters; each must be surfaced for human confirmation:

- **The organization's regulatory status or classification** (money transmitter / MSB, lender, e-money issuer, PayFac, agent, bank, or otherwise). Always an attorney determination; surface as a question `[VERIFY current law / jurisdiction]`.
- **Whether a license, charter, or registration is required** in any jurisdiction, or whether an exemption applies. Always licensing counsel `[VERIFY current law / jurisdiction]`.
- **Adequacy of any AML or sanctions program.** Never concluded by the overlay; always BSA / AML and sanctions counsel.
- **Whether any name is a true sanctions match, or whether to block, reject, or release any transaction.** Always sanctions counsel.
- **Whether any event requires a suspicious-activity report**, or any disclosure of such a report's existence or content. Always AML counsel; treat as restricted.
- **Securities or commodities classification of any token, product, yield feature, or arrangement.** Always securities / digital-asset counsel.
- **Compliance with any card-network rule or payment-card data-security standard.** Always network-rules counsel and the relevant assessor `[VERIFY current network rules]` `[VERIFY current standard version]`.
- **Compliance with any consumer-financial-disclosure, error-resolution, remittance, prepaid, lending, fair-lending, or credit-reporting requirement.** Always consumer-financial-services counsel.
- **That any deposit-insurance, pass-through-insurance, or "bank" representation is accurate or permitted.** Always counsel-cleared.
- **Any threshold, dollar amount, transaction limit, capital figure, bond amount, fee, reporting trigger, or penalty.** Each is `[VERIFY current law / jurisdiction]`; the overlay never quantifies.
- **Any filing deadline, cure period, dispute / chargeback window, or notification timeline.** Triggering-fact dates are `[deadline verification required]`; the timing framework itself is `[VERIFY current law / jurisdiction]` `[VERIFY current network rules]`.
- **How customer funds are protected on insolvency**, or whether a funds-safeguarding structure is sufficient. Always regulatory and bankruptcy / restructuring counsel.
- **The state of the law in any jurisdiction.** Always `[VERIFY current law / jurisdiction]` and specialist counsel where the jurisdiction is material.
- **Current rule, list, network-rulebook, or standard version.** Always `[VERIFY current law / jurisdiction]` / `[VERIFY current network rules]` / `[VERIFY current standard version]`; each evolves on its own cycle.

## Source-of-truth documents

These are referenced by name and location; **do not paste** the documents themselves into this profile or any deliverable. The organization fills in the location.

- **AML / BSA compliance program and policies:** `[ORGANIZATION TO FILL]`
- **Sanctions / OFAC compliance program and screening procedures:** `[ORGANIZATION TO FILL]`
- **Customer-identification, CDD / EDD, and beneficial-ownership procedures:** `[ORGANIZATION TO FILL]`
- **Licensing register and exemption analysis (per jurisdiction):** `[ORGANIZATION TO FILL]`
- **Sponsor-bank / BaaS program agreement(s) and responsibility-allocation matrix:** `[ORGANIZATION TO FILL]`
- **Card-network registration records and rule-change tracker:** `[ORGANIZATION TO FILL]`
- **Payment-card data-security scope documentation and assessment record:** `[ORGANIZATION TO FILL]`
- **Customer-funds-safeguarding / FBO-account and settlement documentation:** `[ORGANIZATION TO FILL]`
- **Consumer-disclosure set, error-resolution procedures, and complaint log:** `[ORGANIZATION TO FILL]`
- **Marketing-claims substantiation file and deposit-insurance-representation register:** `[ORGANIZATION TO FILL]`
- **Vendor inventory and third-party-risk-management records:** `[ORGANIZATION TO FILL]`
- **Incident-response plan and breach-determination protocol:** `[ORGANIZATION TO FILL]`
- **Digital-asset product / token classification and custody documentation (where applicable):** `[ORGANIZATION TO FILL]`
- **Specialist-counsel contact list** — money-transmission / licensing, banking / prudential, BSA / AML, sanctions, network-rules, consumer-financial-services, securities / digital-asset, tax, and bankruptcy / restructuring: `[ORGANIZATION TO FILL]`

## Attorney review

The following must be reviewed by a supervising attorney — and, where the matter requires, by a sector specialist — before any deliverable produced with this overlay is used, sent, or relied upon:

- **Money-transmission / licensing counsel** — every licensing-footprint question, new-jurisdiction or new-activity launch, change-of-control event, and exemption-reliance determination.
- **Banking / prudential and BaaS counsel** — every sponsor-bank program agreement, responsibility-allocation determination, and funds-safeguarding question.
- **BSA / AML counsel** — every AML-program finding, CDD / EDD policy, beneficial-ownership question, and suspicious-activity-reporting determination.
- **Sanctions counsel** — every potential sanctions hit, blocking / rejecting determination, and sanctions-program finding.
- **Securities / digital-asset counsel** — every token, product, yield-feature, or custody question that may implicate securities or commodities regimes, before launch.
- **Network-rules counsel** — every network-registration, chargeback / dispute, and monitoring-program matter `[VERIFY current network rules]`.
- **Consumer-financial-services counsel** — every consumer-disclosure, error-resolution, UDAP / UDAAP, fair-lending, adverse-action, remittance, prepaid, and credit-reporting matter.
- **Data-security / PCI assessor and counsel** — every payment-card data-security scope and assessment matter `[VERIFY current standard version]`.
- **Bankruptcy / restructuring counsel** — every customer-funds-safeguarding and insolvency-protection matter.
- **Local / specialist counsel by jurisdiction** — every matter where the jurisdiction-specific framework is material and the supervising attorney is not admitted or qualified there `[VERIFY current law / jurisdiction]`.
- **Tax counsel** — every matter where the structuring of funds flows, fees, or digital-asset transactions raises a tax question.

No deliverable produced with this overlay is final until the relevant specialist has reviewed it. The overlay's status remains `experimental` until a supervising fintech-counsel reviewer has confirmed the framework references, the per-skill tuning notes have been exercised on at least one real matter, and the `[ORGANIZATION TO FILL]` placeholders have been completed.
