> Shared reference material supporting the AgentCounsel antitrust-competition skills, used to help produce draft legal work product for attorney review — not legal advice.

# Antitrust Risk-Indicator Catalog

This catalog lists conduct patterns and structural features that a reviewer should actively scan for during an antitrust review. Each entry describes the pattern, why it matters under competition-law theory (per se, rule of reason, concerted practice, abuse of dominance), what facts and documents to check, and which client roles or postures carry the most exposure. The catalog is organized by **conduct bucket** — not by alphabetical clause name — to support the conduct-bucket scans inside the antitrust skills.

This catalog is a review aid. It identifies what to look for and why. Whether a flagged pattern actually creates competition-law exposure depends on the specific facts, the parties' market position, the governing jurisdiction, and attorney judgment. Most patterns below carry a `[verify jurisdiction]` marker because antitrust treatment varies materially across regimes (US Sherman/Clayton/FTC Act, EU Article 101/102, UK CA98 / DMCC, and other national regimes). Every flagged item is a candidate for attorney verification — never a legal conclusion.

---

## How to Use This Catalog

For each conduct bucket below:

1. Identify the conduct items in scope and the candidate buckets they fall into (an item may fall into more than one bucket).
2. Walk through the patterns in the bucket and record each pattern present in the user's facts or documents, with a verbatim quote or fact citation.
3. Note any pattern whose treatment varies by jurisdiction (`[verify jurisdiction]`) and record the jurisdictions in which it would be reviewed.
4. Add each finding to the deliverable's risk matrix and the attorney-verification list.
5. Where a pattern's treatment depends on market position (market share, dominance, foreclosure of a substantial share), record only user-supplied facts — never invent or extrapolate.
6. Flag every finding for attorney review; do not resolve ambiguity, conclude legality, or approve conduct.

Cross-reference: pricing-algorithm-specific patterns living in their own skill (`pricing-algorithm-risk-triage`) are referenced from Section 4 below rather than duplicated.

---

## 1. Horizontal Collaboration

Patterns arising when two or more actual or potential competitors collaborate (joint venture, R&D collaboration, joint purchasing, joint marketing or distribution, standard-setting, joint bidding).

### 1.1 Collaboration scope creeps beyond legitimate venture purpose

**Pattern:** The collaboration agreement defines a narrow joint purpose (e.g., joint R&D in a specific field, joint purchasing of a specific input) but the operational provisions reach broader competitive conduct — pricing of unrelated products, customer allocation outside the venture, information exchange covering the parties' independent businesses.

**Why it matters:** Ancillary restraints on competition are evaluated against the legitimate venture purpose and must be reasonably necessary and proportionate to that purpose. Restraints broader than the purpose look like naked horizontal conduct. `[verify jurisdiction]`

**What to check:**
- The stated joint purpose, recited verbatim.
- The scope of any non-compete, exclusivity, customer-allocation, or pricing-coordination provision relative to that purpose.
- Whether information exchange under the agreement is limited to what the joint purpose requires.
- Whether the duration of restraints matches the duration reasonably required for the purpose.

**Most exposed:** Parties that are actual competitors on any market reached by the broader provisions; smaller participants whose independent conduct is constrained by the venture documents.

---

### 1.2 Ancillary restraints overreach (duration, geography, product scope)

**Pattern:** Non-compete, non-solicit, exclusivity, or territorial restraints attached to the collaboration extend beyond the venture's term or footprint, or cover products or geographies the venture does not actually address.

**Why it matters:** Restraints that outlast or outgrow the legitimate venture purpose are vulnerable to challenge as standalone horizontal restraints rather than legitimate ancillary terms. `[verify jurisdiction]`

**What to check:**
- Duration of each restraint vs. duration of the venture and post-termination survival.
- Geographic scope of each restraint vs. geographic scope the venture actually serves.
- Product/service scope of each restraint vs. the venture's product/service scope.
- Whether parties retain freedom to compete in adjacent products, geographies, and customer segments.

**Most exposed:** Parties contemplating exit, expansion, or independent conduct in adjacent areas; smaller participants whose independent strategies are constrained.

---

### 1.3 Information exchange embedded in the collaboration agreement

**Pattern:** The collaboration agreement (or its operating annexes) requires the parties to share competitively sensitive data — current pricing, cost build-ups, capacity, customer-specific terms, wages or hiring — even though the joint purpose does not require it.

**Why it matters:** Information exchange between competitors is reviewed independently of the underlying collaboration. Embedding it in a venture document does not insulate it from competition-law scrutiny and can convert a legitimate collaboration into a vehicle for coordination. `[verify jurisdiction]`

**What to check:**
- Categories of data exchanged (current/forward pricing, costs, capacity, customer-specific, wages, future plans).
- Granularity (individual vs. aggregated; identified vs. anonymized), age (current/forward vs. historical), and frequency.
- Recipient scope (clean-team-only? counsel-only? designated individuals? executives? full deal team?).
- Whether less-sensitive alternatives (aggregated, lagged, third-party-mediated) would meet the joint purpose.

**Most exposed:** Participants whose independent commercial decision-making touches the categories shared; participants without internal information-segregation controls.

---

### 1.4 No clean-team boundary between the venture and independent operations

**Pattern:** The same individuals who run the venture also make competitively significant decisions for one or more parties' independent businesses, without segregation, NDA, or carryover controls.

**Why it matters:** Without a clean-team boundary, sensitive information learned in the venture can foreseeably influence independent competitive conduct (pricing, hiring, capacity), creating concerted-practice and information-exchange exposure. `[verify jurisdiction]`

**What to check:**
- Named individuals on the venture committee and their independent-business decision rights.
- Existence and scope of any clean-team or information-segregation agreement.
- Downstream restrictions: no-busting, no-carryover, post-venture role limits.
- Audit posture: logs, periodic reviews, exit protocols.

**Most exposed:** Smaller participants whose individual decision-makers wear venture and independent-business hats simultaneously; companies without mature compliance programs.

---

### 1.5 Joint bidding or joint tendering without legitimate-collaboration framing

**Pattern:** Two or more competitors submit a joint bid, divide a tender, or coordinate on response timing/price without a documented joint-venture rationale and without disclosure to the procuring party.

**Why it matters:** Bid-rigging is a hardcore horizontal restraint with criminal exposure in many jurisdictions. Even legitimate joint bidding (e.g., capacity-pooling for an oversized project) typically requires careful structuring, advance disclosure, and competition-law review. `[verify jurisdiction]`

**What to check:**
- The procuring party's tender rules on joint bidding.
- Whether the bidders could realistically bid alone (capacity, financial, technical) — joint bidding by parties that could each bid alone is higher-risk.
- Disclosure of the joint-bid structure to the procuring party.
- Communications between bidders about price, customer allocation, or future tenders.

**Most exposed:** Capable independent bidders coordinating to allocate work; public-procurement contractors subject to criminal bid-rigging exposure.

---

### 1.6 Standard-setting without F/RAND or patent-disclosure framing

**Pattern:** A standard-setting organization (SSO) adopts a technical standard incorporating one or more participants' intellectual property without a clear F/RAND licensing commitment, patent-disclosure rule, or competition-law-consistent operating procedure.

**Why it matters:** Standard-setting creates competition benefits but also creates well-known competition-law risks (patent hold-up, exclusion of non-members, coordination on non-standard topics). SSOs typically need defined F/RAND policies and disclosure rules; absence is a flag. `[verify jurisdiction]`

**What to check:**
- The SSO's IPR policy and disclosure rules.
- Whether the standard-setting process is open to all relevant industry participants.
- Whether SSO meetings or working-group agendas touched price, output, customer allocation, or future commercial planning.
- Whether the standard incorporates any participant's IP and, if so, the F/RAND posture.

**Most exposed:** SSO chair and host entity; participants holding essential patents; participants excluded from membership or working groups.

---

### 1.7 Joint purchasing covering an outsized share of input demand

**Pattern:** A joint-purchasing arrangement among competitors covers a share of input demand large enough that the arrangement materially affects upstream suppliers' pricing or downstream output.

**Why it matters:** Joint purchasing is generally treated more favorably than joint selling, but at sufficient scale it can foreclose suppliers, restrict downstream output, or facilitate downstream coordination on costs. `[verify jurisdiction]`

**What to check:**
- Share of upstream input demand the arrangement aggregates.
- Whether the joint-purchasing entity also coordinates downstream pricing or capacity.
- Whether participants retain the right to purchase independently.
- Pass-through commitments to downstream customers (often a defense).

**Most exposed:** Participants with significant downstream market position; arrangements covering a large share of input demand.

---

## 2. Information Exchange Between Competitors

Patterns arising when actual or potential competitors exchange information directly, through a trade association, through a common consultant or vendor, or through a benchmarking exercise.

### 2.1 Current or future price, capacity, or cost data exchanged identifiably

**Pattern:** Pricing data (list or transaction), production capacity, cost build-ups, or planned commercial moves are exchanged with the originating competitor's identity preserved, on a current or forward-looking basis.

**Why it matters:** Identifiable, current/forward exchange of competitively sensitive data among competitors is the highest-risk category and is treated as a concerted practice in many regimes regardless of whether any explicit agreement is reached. `[verify jurisdiction]`

**What to check:**
- Specific categories exchanged (price, cost, capacity, customers, wages/hiring, future plans).
- Whether data is identified (by company) or aggregated/anonymized.
- Currency (current/forward) vs. historical and the time lag.
- Recipient scope and whether commercial decision-makers receive the data.

**Most exposed:** All participants; participants with market power face heightened exposure under abuse-of-dominance frameworks `[verify jurisdiction]`.

---

### 2.2 Benchmarking with no aggregation or insufficient aggregation

**Pattern:** A benchmarking exercise (in-house, consultant-led, or trade-association-led) produces outputs that allow participants to reverse-engineer individual competitor data points — small participant pool, low aggregation thresholds, repeated cuts that isolate individuals.

**Why it matters:** Aggregation is the principal control on competitor-to-competitor data exchange. Inadequate aggregation defeats the control and converts a legitimate benchmark into a vehicle for tracking individual competitors. `[verify jurisdiction]`

**What to check:**
- Number of participants and the minimum cell size in the output.
- Whether outputs include rankings, percentiles, or breakdowns that allow individual identification.
- Whether the consultant or association applies and audits an aggregation protocol.
- Whether participants can request bespoke cuts that defeat aggregation.

**Most exposed:** Markets with few participants (concentrated industries); participants providing detailed raw inputs without aggregation oversight.

---

### 2.3 No time lag on exchanged data

**Pattern:** Pricing, transaction, or commercial data is exchanged in near-real-time or with a time lag short enough that the data remains commercially actionable.

**Why it matters:** Historical, sufficiently lagged data carries lower coordination risk; current and near-current data carries higher risk because it remains useful for competitive decisions. The required lag depends on the data's commercial shelf life and the governing framework. `[verify jurisdiction]`

**What to check:**
- Lag from data generation to exchange.
- Whether the data's commercial usefulness diminishes within the lag period (e.g., a six-month lag is more meaningful for stable list prices than for spot prices).
- Frequency of exchange (annual aggregate vs. monthly identifiable).
- Whether the lag protocol is documented and audited.

**Most exposed:** Participants in fast-moving markets where short lags remain commercially meaningful.

---

### 2.4 Competitor-specific reports distributed without aggregation

**Pattern:** A trade association, consultant, or shared vendor distributes reports that present competitor-specific data (rankings, named-company breakdowns, "your performance vs. Competitor X").

**Why it matters:** Even with historical or post-period data, identifying competitors by name in commercial-performance reports raises concerted-practice and information-exchange concerns and undermines the aggregation defense. `[verify jurisdiction]`

**What to check:**
- Whether competitors are identified by name or by anonymized code in outputs.
- Whether anonymized codes are stable across reports (allowing tracking).
- Whether outputs are restricted to counsel or limited decision-makers within recipients.
- Whether the consultant/association has an antitrust-policy framing for the report series.

**Most exposed:** Participants who rely on the reports to set price, capacity, or commercial strategy; participants whose internal recipients include commercial decision-makers.

---

### 2.5 Trade-association or consultant lacks an antitrust-policy framing

**Pattern:** The information-exchange exercise (whether trade-association-led, consultant-led, or directly bilateral) lacks an antitrust policy, opening statement, meeting protocol, minutes review, or counsel oversight.

**Why it matters:** Without a documented antitrust framing, the absence of policy is itself a flag and any contested exchange is reviewed without the benefit of compliance infrastructure. `[verify jurisdiction]`

**What to check:**
- Existence of a written antitrust policy and whether it is current.
- Antitrust statement read at meeting opening or recited in the protocol.
- Counsel presence or pre-clearance of agendas and outputs.
- Minutes-review and side-meeting controls.

**Most exposed:** Trade-association staff; participating companies' compliance functions; companies with prior enforcement history.

---

### 2.6 Shared vendor or consultant as conduit for competitor data

**Pattern:** A single vendor, consultant, or analytics provider serves multiple competing customers and shares aggregated, semi-aggregated, or individually identifiable data among them, or feeds outputs derived from their combined inputs back to each.

**Why it matters:** A vendor or consultant acting as an information hub among competitors can create indirect information-exchange exposure even if no two competitors ever speak. Cross-reference Section 4 for pricing-algorithm specifics. `[verify jurisdiction]`

**What to check:**
- The vendor's customer base on the relevant market and whether it includes the user's direct competitors.
- The vendor's data-handling protocol: aggregation, anonymization, retention, segregation across customers.
- Whether outputs delivered to one customer are derived from inputs received from competing customers.
- Audit and contractual controls on the vendor.

**Most exposed:** Industries with concentrated vendor ecosystems; participants relying on a single vendor that also serves direct competitors.

---

## 3. Vertical Restraints

Patterns arising in distribution, dealer, franchise, marketplace, supply, and licensing relationships between participants at different levels of the supply chain.

### 3.1 Resale Price Maintenance (RPM) in jurisdictions treating it per se illegal

**Pattern:** The supplier mandates a minimum resale price, prohibits discounting below a stated level, or conditions supply, rebates, or marketing support on the dealer's adherence to a price floor.

**Why it matters:** Treatment of RPM varies sharply by jurisdiction. Some US states retain per se treatment under state law; EU/UK treat RPM as a hardcore restriction under VBER; many other jurisdictions treat it as per se or near-per-se illegal. `[verify jurisdiction]`

**What to check:**
- Whether the price obligation is mandatory (RPM) or genuinely advisory (suggested resale).
- Termination, rebate, or supply consequences for non-adherence.
- Whether enforcement mechanics (monitoring, complaints from other dealers, threats of cut-off) convert a nominally advisory program into RPM.
- Existence of state-law overlays for US matters and per-jurisdiction treatment globally.

**Most exposed:** Suppliers with branded products; dealers facing termination for discounting; jurisdictions with per se RPM treatment.

---

### 3.2 Minimum Advertised Price (MAP) policy with enforcement crossing into RPM

**Pattern:** A MAP policy that on its face restricts only advertised prices is operated so as to restrict actual transaction prices — for example, by penalizing dealers who advertise compliance and then discount in-cart, or by sharing dealer transaction prices across the dealer network.

**Why it matters:** Unilateral MAP policies are generally lower-risk than RPM in many jurisdictions, but enforcement mechanics that reach transaction price can convert a MAP policy into RPM with the higher-risk treatment that follows. `[verify jurisdiction]`

**What to check:**
- The verbatim text of the MAP policy.
- The enforcement protocol: who monitors, what triggers consequences, what consequences follow.
- Whether dealer-to-dealer communication or supplier-to-dealer information sharing reaches transaction price.
- Whether the policy is genuinely unilateral or includes any agreement element with dealers.

**Most exposed:** Branded-goods suppliers; e-commerce-heavy distribution networks; jurisdictions where MAP/RPM distinction is narrowly drawn.

---

### 3.3 Wide MFN / parity clauses (covering all channels or all customers)

**Pattern:** A most-favored-nation or parity clause requires the counterparty to offer the user terms (price, availability, features) at least as favorable as those offered to any other customer, channel, or platform — not limited to the user's own direct channel.

**Why it matters:** Narrow MFNs (parity with the counterparty's own direct channel) are generally treated more favorably; wide MFNs (parity across competing platforms or all channels) can dampen price competition between platforms, deter entry, and have drawn enforcement attention in multiple jurisdictions. `[verify jurisdiction]`

**What to check:**
- The comparator scope: own channel only (narrow) vs. competing platforms or all customers (wide).
- Direction: which platform/customer is favored relative to which.
- Whether the clause covers price only or extends to non-price terms (availability, exclusives, features).
- Market context: counterparty's share of upstream supply; existence of competing platforms.

**Most exposed:** Online platforms and marketplaces; dominant intermediaries; suppliers signing wide MFNs with large platforms.

---

### 3.4 Exclusivity foreclosing a substantial share of the relevant market

**Pattern:** A single-brand exclusivity, requirements contract, or de facto exclusivity covers customers or distribution channels representing a large share of the market over a meaningful term.

**Why it matters:** Exclusivity is generally lawful but becomes problematic when it forecloses a substantial share of the market to rivals, especially where the imposing party has market power. Foreclosure analysis is fact-intensive. `[verify jurisdiction]`

**What to check:**
- Share of demand or supply covered by the exclusivity arrangement(s) collectively.
- Duration and termination triggers.
- Counterparties' realistic alternatives and switching costs.
- Whether the imposing party has market power or dominance (a question for counsel, not for the skill).

**Most exposed:** Dominant or near-dominant suppliers; participants in industries with high switching costs; counterparties without realistic alternatives.

---

### 3.5 Online-sales or marketplace restrictions

**Pattern:** The distribution arrangement restricts the dealer's right to sell online, prohibits sales through specified marketplaces, restricts use of price-comparison tools, restricts geographic scope of passive online sales, or applies dual pricing (different wholesale price for online vs. offline sales).

**Why it matters:** Online-sales restrictions, absolute marketplace bans, and dual pricing have drawn close scrutiny in many jurisdictions and are treated as hardcore restrictions or active-enforcement areas under several frameworks (e.g., EU/UK VBER). `[verify jurisdiction]`

**What to check:**
- The verbatim restriction language.
- Whether the restriction is absolute (e.g., "no sales via online marketplaces") or qualitative (e.g., authorized-dealer criteria).
- Whether dual pricing is in place and the magnitude of the differential.
- The supplier's justification (brand image, service quality, anti-counterfeiting) and whether the restriction is calibrated to that justification.

**Most exposed:** Branded-goods suppliers using selective distribution; e-commerce-heavy dealer networks; suppliers in jurisdictions with active online-sales enforcement.

---

### 3.6 Dual distribution conduct (supplier competing with its dealers)

**Pattern:** The supplier sells directly to end customers and also distributes through independent dealers, while exchanging competitively sensitive information with those dealers or imposing restraints that protect its direct channel.

**Why it matters:** Dual distribution creates a horizontal element within the vertical relationship. Information shared with dealers can become competitor-to-competitor exchange; restraints can protect the supplier's direct channel in ways that look like horizontal coordination. `[verify jurisdiction]`

**What to check:**
- Categories of information shared with dealers (price, customer, capacity, planning).
- Whether the supplier's direct channel competes with the dealer's territory or customer base.
- Restraints protecting the direct channel (territory, customer-class, pricing).
- Whether information-segregation controls are in place between the supplier's sales side and its wholesale side.

**Most exposed:** Suppliers operating both direct-to-consumer and dealer channels in the same market; suppliers in jurisdictions with explicit dual-distribution frameworks.

---

### 3.7 Selective-distribution criteria that exclude qualifying dealers

**Pattern:** Selective-distribution criteria are written so as to exclude dealers who meet objective service or qualification standards but who are disfavored on commercial grounds (e.g., online-only dealers, discount dealers).

**Why it matters:** Selective distribution is generally permissible when criteria are objective, qualitative, applied uniformly, and proportionate to a legitimate purpose. Criteria that operate as commercial discrimination can be challenged as restrictive vertical conduct. `[verify jurisdiction]`

**What to check:**
- Selection criteria as written and as applied.
- Whether qualifying dealers have been declined; the stated reasons.
- Whether criteria de facto exclude online-only or low-price dealers.
- The supplier's justification and proportionality to that justification.

**Most exposed:** Online-only dealers seeking authorization; discount-positioned dealers; suppliers in jurisdictions with rigorous selective-distribution review.

---

## 4. Pricing-Related Conduct

Patterns arising from loyalty pricing, bundled discounts, predatory pricing, public pricing communications, and algorithmic pricing. For algorithmic-pricing specifics, this section cross-references `skills/antitrust-competition/pricing-algorithm-risk-triage/SKILL.md`; do not duplicate that skill's analysis here.

### 4.1 Below-cost or predatory-pricing flags requiring economic analysis

**Pattern:** Prices on one or more products fall below an appropriate cost measure (average variable cost, average avoidable cost, long-run average incremental cost) for a sustained period, especially in a market where the user has market power.

**Why it matters:** Below-cost pricing by a dominant or near-dominant participant can be challenged as predatory under several frameworks; the analysis is highly fact-intensive and requires an economic-expert pass. `[verify jurisdiction]`

**What to check:**
- The cost measure being used and whether it is consistent with the governing framework.
- Duration of below-cost pricing.
- Market position (user-supplied share; dominance question for counsel).
- Recoupment posture (a required element under some US frameworks; not under EU Article 102).

**Most exposed:** Dominant or near-dominant participants; participants in markets with high barriers to entry; participants whose pricing follows a competitive entry.

---

### 4.2 Loyalty or bundled discounts conditioned on share or exclusivity

**Pattern:** Discounts, rebates, or marketing support are conditioned on the customer taking a specified share of its requirements from the supplier, on exclusivity, or on bundled purchases across multiple products.

**Why it matters:** Share-conditional, retroactive, and bundled discount structures by a dominant participant raise abuse-of-dominance concerns in several jurisdictions (notably EU Article 102) and can be reviewed under rule-of-reason or section-2 frameworks elsewhere. Cliffs, market-share thresholds, and retroactive applicability heighten concern. `[verify jurisdiction]`

**What to check:**
- Whether discounts are unconditional, share-conditional, or exclusivity-conditional.
- Whether discount applies prospectively (incremental) or retroactively (rebate on all units once threshold is met).
- Cliffs and market-share thresholds; magnitude of the discount.
- Bundling across products and whether bundled discount can be defeated by competitor offering only the contested product.

**Most exposed:** Dominant or near-dominant participants; loyalty schemes covering a substantial share of customer demand; jurisdictions with active rebate-framework enforcement.

---

### 4.3 Hub-and-spoke pattern via a shared vendor or platform

**Pattern:** Two or more competitors use the same vendor, platform, or analytics provider, and the vendor pushes recommendations, pricing signals, or outputs derived from the competitors' combined inputs back to each.

**Why it matters:** A vendor that aggregates competitor data and feeds derived outputs back to each customer can create concerted-practice exposure even without competitor-to-competitor communication. Cross-reference `skills/antitrust-competition/pricing-algorithm-risk-triage/SKILL.md` for the full algorithmic treatment. `[verify jurisdiction]`

**What to check:**
- The vendor's customer base on the relevant market.
- Whether the vendor's outputs to one customer are derived from inputs received from competing customers.
- Data-segregation, aggregation, and access-control posture across the vendor's customers.
- Whether participants are aware of the vendor's competitor-overlap.

**Most exposed:** Concentrated industries with a small set of pricing or analytics vendors; participants without vendor-diligence controls.

---

### 4.4 Public price-signaling patterns

**Pattern:** Prices, capacity, or planned commercial moves are publicly announced, posted, or communicated in a way that is reasonably designed to be detected by competitors and to invite parallel response (end-of-day posting; rapid public follow-the-leader; earnings-call language signaling future pricing intentions).

**Why it matters:** Public signaling has been treated as evidence of, or as a stand-alone basis for, concerted-practice claims in several frameworks. The risk is amplified where prices change frequently and competitors observe each other in near-real-time. `[verify jurisdiction]`

**What to check:**
- Forum and granularity of public price/capacity communications.
- Timing patterns: whether announcements precede competitor follow-on responses on detectable cadence.
- Public statements from executives about future pricing intentions or "discipline" calls.
- Whether automated competitor-monitoring tools react detectably to the user's public signals.

**Most exposed:** Concentrated industries; markets with frequent price changes; industries with active investor-communication channels.

---

### 4.5 Algorithmic-pricing risk indicators (cross-reference)

**Pattern:** The user deploys a pricing recommender, dynamic-pricing engine, optimizer, or pricing-as-a-service product that ingests competitor data (directly, via shared vendor, or pooled) or produces outputs detectable by competing algorithms.

**Why it matters:** Algorithmic pricing implicates the patterns in 4.3 and 4.4 above plus its own framework questions on hub-and-spoke, signaling, concerted practice, and abuse-of-dominance. The full review lives in `skills/antitrust-competition/pricing-algorithm-risk-triage/SKILL.md`; treat this entry as a routing flag only. `[verify jurisdiction]`

**What to check:**
- Whether any pricing-algorithm deployment is in scope.
- Whether the algorithm ingests competitor data and what kind (direct, via shared vendor, pooled).
- Whether the algorithm's outputs are externally observable.
- The override, audit, and governance posture.

**Most exposed:** Participants in concentrated industries using common vendors; participants without override or audit controls; markets with public price posting.

---

## 5. Merger / Integration Conduct (Pre-Closing)

Patterns arising between signing and closing (or before signing where a transaction is in active diligence). For the full pre-closing review, see `skills/antitrust-competition/gun-jumping-clean-team-checklist/SKILL.md` and `skills/antitrust-competition/information-sharing-clean-team-review/SKILL.md`.

### 5.1 Premature integration of pricing, sales, or sensitive commercial planning

**Pattern:** The parties begin integrating pricing decisions, joint sales planning, customer-account allocation, or capacity planning before closing — or before the relevant notification waiting period expires.

**Why it matters:** Gun-jumping rules (US HSR / Section 1; EU Article 7 standstill / Article 101; equivalent national regimes) restrict pre-closing integration of competitively sensitive decision-making. Premature integration creates enforcement and unwinding exposure. `[verify jurisdiction]`

**What to check:**
- Decisions touched jointly pre-closing: pricing, customer commitments, capacity, hiring, capex above thresholds, joint communications.
- Whether decisions occurred before signing, between signing and notification, during the waiting period, or after waiting-period expiration.
- Whether the operate-in-ordinary-course covenant in the purchase agreement constrained or permitted the conduct.
- Whether counsel pre-cleared each integration step.

**Most exposed:** Parties that are actual competitors on any market; transactions notified in multiple jurisdictions; transactions with extended review periods.

---

### 5.2 Absence of clean-team protocol for diligence and integration planning

**Pattern:** Competitively sensitive information flows between the parties pre-closing without a documented clean-team protocol — no defined membership, no NDA scope, no segregation from competitive decision-makers, no retention/destruction or carryover restrictions.

**Why it matters:** Without a clean-team protocol, sensitive information can foreseeably influence each party's independent competitive conduct, creating both gun-jumping and information-exchange exposure. The risk persists if the deal does not close (carryover) and after closing (spillover to non-deal contexts). `[verify jurisdiction]`

**What to check:**
- Existence and scope of a clean-team agreement.
- Named clean-team members and their independent-business decision rights.
- Information categories crossing to the clean team and the recipient scope.
- Retention, destruction, and post-deal carryover controls.

**Most exposed:** Smaller deal teams without specialized antitrust counsel; first-time merger participants; transactions where diligence began before counsel was engaged.

---

### 5.3 HSR or non-US notification gaps

**Pattern:** The transaction may meet a notification threshold in a jurisdiction in which no filing has been planned, or has been notified in some jurisdictions but not others.

**Why it matters:** Closing without required notification triggers gun-jumping liability and unwinding risk. Reportability analysis is highly fact-intensive and varies by jurisdiction (HSR thresholds, EU EUMR turnover tests, UK CMA jurisdictional tests, national notification regimes globally). Reportability is an attorney determination. `[verify jurisdiction]`

**What to check:**
- Each party's revenue, assets, and sales footprint per jurisdiction.
- Each potentially-applicable notification regime's thresholds.
- Any prior or contemporaneous transactions with the same counterparty (aggregation).
- Foreign investment, sector-specific, and national-security overlays.

**Most exposed:** Cross-border transactions; transactions with global revenue footprints; transactions involving regulated industries.

---

### 5.4 Joint customer or supplier outreach pre-closing

**Pattern:** The parties make joint announcements to customers, suppliers, or employees referencing the transaction; conduct joint sales calls; or coordinate commercial communications.

**Why it matters:** Joint commercial outreach pre-closing is a leading gun-jumping risk indicator and can convert otherwise-permitted integration-planning into prohibited operating coordination. `[verify jurisdiction]`

**What to check:**
- Communications inventory: customer, supplier, employee outreach referencing the deal or the other party.
- Joint sales calls, joint commercial proposals, joint pricing discussions.
- Joint employee communications (especially about post-closing roles or compensation).
- Whether each communication was pre-cleared under the gun-jumping protocol.

**Most exposed:** Parties with overlapping customer bases; sales-led integration efforts; transactions with announced synergy targets.

---

### 5.5 Operate-in-ordinary-course covenant exceeded by acquirer control

**Pattern:** Pre-closing covenants in the purchase agreement go beyond protecting the target's value (ordinary-course protection) to allow the acquirer to direct or veto the target's pricing, output, customer-contract, hiring, capex, or strategic decisions.

**Why it matters:** Pre-closing covenants that hand operational control to the acquirer can be challenged as gun-jumping even where filings have been made and waiting periods observed. The line between value-protection and acquirer-control is a critical attorney judgment. `[verify jurisdiction]`

**What to check:**
- Each consent right, with its threshold and scope.
- Affirmative covenants that require pre-closing acquirer involvement.
- Restrictive covenants and the conduct they prohibit.
- The character of each covenant: ordinary-course-protection, acquirer-control, consent-gated, or ambiguous (a question for counsel).

**Most exposed:** Strategic acquirers with overlap; transactions with long expected pendency; transactions with significant integration-planning carveouts.

---

## 6. Monopolization / Abuse of Dominance (Unilateral Conduct)

Patterns arising from a single firm's conduct where the firm has or approaches market power. Dominance and market-power determinations are attorney tasks; the patterns below identify the conduct types most often reviewed under monopolization/dominance frameworks.

### 6.1 Refusal-to-deal patterns

**Pattern:** A participant declines to supply, license, or grant access to a counterparty (potential entrant, downstream rival, complementor) on commercial terms — or terminates an existing supply or license relationship.

**Why it matters:** Refusal to deal is generally permitted but can be challenged under monopolization or abuse-of-dominance frameworks where the refusing party has market power, where the input/access is genuinely indispensable, and where the refusal forecloses competition. The frameworks differ materially across jurisdictions. `[verify jurisdiction]`

**What to check:**
- The refusing party's market position (user-supplied share; dominance is for counsel).
- The indispensability of the input/access to the requesting party.
- Prior dealing relationship and the stated reason for refusal or termination.
- Available alternatives and the requesting party's ability to replicate the input.

**Most exposed:** Owners of essential facilities or platforms; participants with market power on input markets; participants terminating long-standing supply relationships.

---

### 6.2 Tying or bundling on a dominant product

**Pattern:** The supplier conditions the sale, licensing, or attractive pricing of a product on which it has market power on the customer's purchase or use of a second product.

**Why it matters:** Tying and bundling by a dominant or near-dominant supplier raises abuse-of-dominance concerns in several jurisdictions. The analysis turns on market power on the tying product, separate-products analysis, anticompetitive effects on the tied market, and justifications. `[verify jurisdiction]`

**What to check:**
- Whether the tying and tied products are commercially distinct.
- Whether the supplier has market power on the tying product.
- The mechanism: contractual condition, technical integration, pricing penalty.
- The justification (interoperability, quality control) and proportionality.

**Most exposed:** Dominant or near-dominant suppliers; platforms bundling adjacent services; sectors with active tying enforcement (technology, payments, healthcare).

---

### 6.3 Margin squeeze

**Pattern:** A vertically integrated supplier with market power on an upstream input sets the input price for downstream rivals at a level that prevents an equally efficient downstream competitor from earning a normal margin.

**Why it matters:** Margin squeeze is recognized as an abuse-of-dominance theory in several jurisdictions (notably EU Article 102) and as a section-2 theory in some US case law. The analysis requires careful input and output price/cost comparison. `[verify jurisdiction]`

**What to check:**
- The supplier's market position on the input market (user-supplied; dominance for counsel).
- The relationship between the input price charged to downstream rivals and the downstream price charged by the supplier's own downstream affiliate.
- Whether the spread permits an equally efficient downstream competitor to earn a normal margin.
- Economic analysis (typically required) of cost and price benchmarks.

**Most exposed:** Vertically integrated dominant suppliers; regulated network industries; markets with significant downstream rivals dependent on the upstream input.

---

### 6.4 Exclusionary contracting

**Pattern:** A dominant or near-dominant participant uses exclusivity, loyalty, requirements, or share-conditional discounts (see 4.2) at a scale that forecloses rivals from a substantial share of the market.

**Why it matters:** Exclusionary contracting by a participant with market power is a longstanding monopolization / abuse-of-dominance theory. Foreclosure analysis is fact-intensive. Cross-reference 3.4 (exclusivity) and 4.2 (loyalty/bundled discounts). `[verify jurisdiction]`

**What to check:**
- Aggregate share of demand or supply covered.
- Counterparties' alternatives and switching costs.
- The participant's market position (user-supplied; dominance for counsel).
- Duration and termination of the arrangements.

**Most exposed:** Dominant or near-dominant suppliers; markets with high barriers to entry; counterparties without realistic alternatives.

---

### 6.5 Predatory innovation or product hopping

**Pattern:** A dominant participant makes product changes whose principal effect is to disadvantage rivals or complementors rather than to deliver consumer benefit (e.g., a minor formulation change that resets exclusivity, an API change that breaks competitor interoperability without a stated functional gain).

**Why it matters:** Product design changes by a dominant participant can be challenged where the change's principal effect is exclusionary and its consumer-benefit justification is weak. The frameworks are unsettled and jurisdiction-specific. `[verify jurisdiction]`

**What to check:**
- The product change and its stated business rationale.
- Effects on rivals' or complementors' ability to compete.
- Whether the change is reversible or interoperable.
- Internal documents on the change's rationale and expected competitive effects.

**Most exposed:** Dominant participants in pharmaceutical, technology, and platform markets; participants making interoperability-affecting changes.

---

## 7. Labor-Market Conduct

Patterns arising in agreements or conduct affecting hiring, recruiting, wages, or worker mobility between competing employers.

### 7.1 No-poach agreements between competing employers

**Pattern:** Two or more employers agree, formally or informally, not to hire, recruit, or solicit each other's employees.

**Why it matters:** No-poach agreements between competing employers are treated as per se illegal restraints in some jurisdictions (US DOJ has pursued criminal cases under this theory) and as restrictive horizontal conduct in others. Treatment varies sharply. `[verify jurisdiction]`

**What to check:**
- Whether the agreement is between competing employers (actual or potential competitors for labor).
- Whether it is naked (standalone) or ancillary to a legitimate collaboration (e.g., a JV).
- Scope (all employees? specific roles? specific geographies?).
- Documentation (written agreement, email exchanges, HR-to-HR communications).

**Most exposed:** Industries with concentrated employer demand for specialized roles; HR functions without antitrust training; companies in jurisdictions with criminal no-poach enforcement.

---

### 7.2 Wage-fixing or compensation-coordination patterns

**Pattern:** Two or more employers agree on, exchange information about, or coordinate on wages, salaries, bonuses, or other compensation terms.

**Why it matters:** Wage-fixing among competing employers is treated as a hardcore restraint in many jurisdictions and as criminal in some (US). Even information exchange on compensation can be challenged under information-exchange frameworks. `[verify jurisdiction]`

**What to check:**
- Direct discussions about wage levels, ranges, increases, or bonus structures with competitors.
- Compensation-benchmarking exercises that fail aggregation/lag protocols (cross-reference Section 2).
- Trade-association surveys or HR-consortium activity covering compensation.
- HR-to-HR communications.

**Most exposed:** Industries with concentrated employer demand; HR benchmarking exercises without antitrust framing; companies with prior labor-market enforcement history.

---

### 7.3 Non-solicit clauses in commercial agreements between competitors

**Pattern:** A commercial agreement between actual or potential competitors (JV, supply agreement, licensing) includes a non-solicit clause restricting each party from hiring the other's employees.

**Why it matters:** Non-solicit clauses ancillary to a legitimate collaboration are generally evaluated for proportionality and scope; standalone non-solicits between competitors can be treated as no-poach agreements. The line is jurisdiction- and fact-specific. `[verify jurisdiction]`

**What to check:**
- Whether the non-solicit is genuinely ancillary to a legitimate collaboration.
- Scope: which employees, which roles, which geographies, which durations.
- Whether the scope is calibrated to the protected business interest (typically only employees who had material exposure to the collaboration's confidential information).
- Survival period after termination.

**Most exposed:** Joint-venture parties; outsourcing customer/provider pairs; M&A counterparties with extended pendency.

---

### 7.4 Non-compete clauses between competing employers' departing employees

**Pattern:** Non-compete clauses with departing employees that restrict their re-employment by competitors, particularly where multiple competing employers in the same industry use similar clauses.

**Why it matters:** Non-competes are primarily evaluated under employment-law frameworks but increasingly under competition-law frameworks where industry-wide use restricts labor-market mobility. Treatment is rapidly evolving in several jurisdictions. `[verify jurisdiction]`

**What to check:**
- Whether non-competes are standard across competing employers in the industry.
- Scope (geographic, temporal, role) and consideration.
- Jurisdiction-specific limits and recent enforcement or rulemaking developments `[verify jurisdiction]`.
- Whether use of non-competes has been coordinated among competing employers (separate horizontal concern).

**Most exposed:** Industries with industry-wide non-compete practice; participants in jurisdictions with active non-compete reform; participants with prior labor-market enforcement history.

---

## 8. Trade-Association Activity

Patterns arising in trade-association membership, meetings, working groups, statistics programs, and informal contacts around association activity. For full meeting review, see `skills/antitrust-competition/trade-association-meeting-review/SKILL.md`.

### 8.1 Minutes record competitor-sensitive discussion

**Pattern:** Meeting minutes (board, members' meeting, committee, working group) record discussion of price, costs, customer-specific terms, capacity, output, future commercial plans, market allocation, or boycott of third parties.

**Why it matters:** Minutes documenting competitor-sensitive discussion are direct evidence of concerted practice and information-exchange exposure. They are routinely sought in enforcement actions. `[verify jurisdiction]`

**What to check:**
- Each agenda item and what the minutes record about the discussion.
- Verbatim quotes where available.
- Attendees and their roles at the discussion.
- Whether counsel was present and whether minutes were reviewed by counsel.

**Most exposed:** Association staff; participating companies whose representatives spoke; companies in concentrated industries.

---

### 8.2 Agenda items implying coordination

**Pattern:** Agenda items framed in terms that suggest coordination — "market conditions and outlook," "pricing discussion," "responding to customer demands," "industry discipline," or topics with no legitimate trade-association purpose.

**Why it matters:** Agenda framing is itself reviewed in enforcement. Items implying coordination are flags whether or not the discussion stayed within bounds. `[verify jurisdiction]`

**What to check:**
- Each agenda item's verbatim title and description.
- Whether the item has a legitimate trade-association purpose (legislative advocacy, industry standards, training, sponsor recognition).
- Whether counsel pre-cleared the agenda.
- Whether the item, as discussed, stayed within bounds (cross-reference 8.1).

**Most exposed:** Association staff drafting agendas; participating companies without internal agenda-review controls.

---

### 8.3 Off-agenda hallway / dinner / side-meeting discussion

**Pattern:** Pre- or post-meeting communications, dinners, social events, or side meetings involving competitor representatives, with potentially competitively sensitive discussion.

**Why it matters:** Off-agenda informal contacts are a leading vehicle for unmonitored competitor discussion and a recurring fact pattern in enforcement actions. Documented attendance + later parallel conduct creates significant inferential exposure. `[verify jurisdiction]`

**What to check:**
- Inventory of pre/post-meeting events and side meetings.
- Attendees at each, including who attended dinner, breakouts, social events.
- Topic awareness: what was discussed (per the user's recollection or notes).
- Whether the association policy addresses informal contacts and whether participants observe it.

**Most exposed:** Companies sending sales/commercial representatives to associations; concentrated industries where the same individuals attend repeatedly.

---

### 8.4 Statistics or benchmarking program with insufficient aggregation

**Pattern:** An association-administered statistics or benchmarking program produces outputs that allow tracking of individual competitors (cross-reference Section 2.2).

**Why it matters:** Association-administered programs concentrate exposure on the association and on each participating company. Aggregation, anonymization, lag, and counsel oversight are the principal controls. `[verify jurisdiction]`

**What to check:**
- Aggregation rules and minimum cell sizes.
- Whether output formats allow identification of individual competitors.
- Time lag between data collection and output distribution.
- Counsel pre-clearance of program design and outputs.

**Most exposed:** Association staff; participating companies in concentrated industries; programs producing detailed competitor-level cuts.

---

### 8.5 Association activity that crosses into joint commercial conduct

**Pattern:** Association activity goes beyond advocacy, education, and standards into joint commercial conduct — joint negotiation with suppliers or customers, group boycotts, collective decisions on output or capacity, joint pricing recommendations.

**Why it matters:** Trade associations are generally a permitted forum for industry coordination on non-commercial topics. Activity that crosses into joint commercial conduct triggers full hardcore-restraint review and can be treated as per se in several frameworks. `[verify jurisdiction]`

**What to check:**
- Each association activity that touches commercial conduct.
- Whether the activity has a documented antitrust-counsel framing (e.g., legitimate joint-purchasing structure with documented controls).
- Boycott or collective-refusal language in association communications.
- Joint pricing recommendations, model price lists, or pricing guidance.

**Most exposed:** Association staff; concentrated industries with active joint-purchasing or joint-negotiation activity; associations without dedicated antitrust counsel.

---
