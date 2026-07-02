> Shared reference material supporting the AgentCounsel ai-governance skills, used to help produce draft legal work product for attorney review — not legal advice.

# AI Vendor Terms Red-Flag Catalog

This catalog lists clause patterns and structural features specific to AI vendor agreements — terms of service, API agreements, enterprise licenses, and acceptable use policies — that a reviewer should actively scan for during an AI vendor terms review. Each entry describes the pattern, why it matters, what to check, and which client roles are most exposed. The catalog is organized by topic to support a Red Flags Quick Scan output within the `ai-vendor-terms-review` skill. For general commercial contract patterns (liability caps, indemnity mechanics, termination, auto-renewal), see `skills/contracts/references/red-flags.md`; this catalog covers what is materially different in AI contracts.

This catalog is a review aid. It identifies what to look for and why. Whether a flagged pattern is actually problematic depends on the specific contract language, the client's role and intended use, the data the client will input, and attorney judgment. Every flagged item is a candidate for attorney verification — not a legal conclusion. Patterns describe contract language only; nothing in this catalog asserts what any AI regulation requires `[Verify current law]`.

---

## How to Use This Catalog

For each topic category below:

1. Locate the relevant provision in the document under review (or note its absence — a missing provision is itself a red flag in many contexts).
2. Check the pattern description against the actual language, including any incorporated-by-reference policies (acceptable use policy, usage guidelines, model terms).
3. If the pattern is present, add the item to the AI-Specific Terms Assessment table and the prioritized redline points.
4. Note which client roles are most exposed and whether the client's role and intended use match the exposure profile.
5. Use the per-section **Preferred position / Fallback position** lines to orient the direction of a redline ask — they are starting points for attorney judgment, not standard positions.
6. Flag every finding for attorney review; do not resolve ambiguity silently.

---

## 1. Training and Improvement Rights

### 1.1 Default training on customer inputs or outputs

**Pattern:** The vendor's terms grant it the right to use customer inputs, prompts, files, or generated outputs to train, fine-tune, or "improve" its models or services by default, without an affirmative customer election.

**Why it matters:** Default training rights can expose the client's confidential business information, personal data, and proprietary material to incorporation into models that serve other customers — including competitors — and the exposure may be practically irreversible once training occurs.

**What to check:**
- Quote the training or "service improvement" grant verbatim, including any definitions of "Content," "Customer Data," or "Usage Data" it relies on.
- Distinguish the license needed to operate the service from broader training, improvement, or product-development rights.
- Check whether the grant covers inputs only, outputs only, or both, and whether it extends to metadata and usage telemetry.

**Most exposed:** Client inputting confidential business information, personal data, or proprietary datasets; client in a competitive market where its usage patterns are themselves sensitive.

---

### 1.2 Opt-out that is partial, prospective-only, or operationally buried

**Pattern:** A training opt-out exists but is limited — it applies only to certain product tiers or endpoints, applies only prospectively (data already used for training stays in the model), requires an out-of-band process (email, support ticket, account setting) not reflected in the contract, or can be revoked or narrowed by the vendor.

**Why it matters:** A partial or prospective-only opt-out can leave the client believing it is protected when historical inputs remain in trained models, or when a subset of its usage (free tiers, playground use, certain APIs) still flows into training.

**What to check:**
- Identify the exact scope of the opt-out: which products, endpoints, tiers, and data categories it covers.
- Confirm whether the opt-out is contractual (in the signed terms) or merely an account setting the vendor could change.
- Check whether the opt-out is retroactive or prospective-only, and what happens to data used for training before the opt-out.
- Confirm whether the opt-out survives renewals and terms updates.

**Most exposed:** Enterprise client that assumes an enterprise tier is fully excluded from training; client whose personnel also use free or consumer tiers of the same vendor.

---

### 1.3 "De-identified" or "aggregated" data carve-outs with weak definitions

**Pattern:** The vendor reserves broad rights to use "de-identified," "anonymized," or "aggregated" customer data for any purpose, but the terms do not define the de-identification standard, do not prohibit re-identification, and do not restrict combination with other datasets.

**Why it matters:** An undefined de-identification carve-out can function as a general-purpose data use right. Weakly de-identified data derived from prompts and outputs may remain re-identifiable or competitively revealing, and the carve-out typically survives termination.

**What to check:**
- Quote the de-identification or aggregation carve-out and any definition it relies on.
- Check for a re-identification prohibition and for restrictions on combining de-identified data with other sources.
- Check whether the carve-out is excluded from confidentiality obligations and from deletion obligations on termination.
- Whether a given de-identification standard satisfies applicable data protection frameworks is an attorney question `[Verify current law]`.

**Most exposed:** Client with high-volume or domain-distinctive usage whose "aggregated" patterns would reveal strategy; client with personal-data obligations flowing to its processors.

---

### 1.4 Human review rights over customer content

**Pattern:** The vendor reserves the right for its employees or contractors to review customer inputs and outputs — for abuse monitoring, trust and safety, support, debugging, or model evaluation — with no limits on scope, purpose, personnel, retention, or confidentiality treatment.

**Why it matters:** Unbounded human review means the client's confidential, personal, or privileged material may be read by unidentified vendor personnel (and their contractors), which undermines confidentiality expectations and, where privileged material is input, may bear on the third-party-disclosure analysis for privilege — an attorney-only assessment.

**What to check:**
- What triggers human review (automated flag, random sampling, support request), and is review limited to what triggered it?
- Are reviewing personnel bound by confidentiality obligations, and are contractors and sub-processors covered?
- Is there a zero-retention, no-human-review, or restricted-access tier, and has the client elected it?
- If privileged or work-product material will be input, flag `[ATTORNEY TO CONFIRM: privilege impact under governing jurisdiction's privilege doctrine]`.

**Most exposed:** Client inputting privileged material, trade secrets, personal data, or regulated content.

**Preferred position:** No use of customer inputs or outputs for training or model improvement, stated contractually, covering all tiers and endpoints the client will use, with human review limited to documented abuse-monitoring triggers under confidentiality obligations.
**Fallback position:** A contractual, non-revocable opt-out covering all of the client's usage, retroactive deletion or non-use commitments for previously collected data `[CONFIRM: feasibility with vendor]`, a defined de-identification standard with a re-identification prohibition, and human review limited in purpose, personnel, and retention.

---

## 2. Input/Output Ownership and IP

### 2.1 Output ownership ambiguity or non-assignment

**Pattern:** The terms are silent on who owns generated outputs, grant the customer only a license to outputs rather than an assignment of the vendor's rights (if any), or condition the customer's rights in outputs on compliance with the agreement or the acceptable use policy.

**Why it matters:** If the client's rights in outputs are merely licensed or conditional, a terms violation, non-payment, or termination could strip the client of rights in work product already deployed in its business. Separately, the extent to which AI-generated output is protectable at all is an unsettled attorney-verification question `[Verify current law]`.

**What to check:**
- Quote the output ownership or license grant verbatim; distinguish "assigns" from "grants a license" from silence.
- Identify any conditions on the client's output rights (compliance, payment, tier) and what happens on termination.
- Check for restrictions on output use — commercial restrictions, attribution requirements, prohibitions on using outputs to develop competing models.

**Most exposed:** Client deploying outputs in products, marketing, code, or other assets with ongoing commercial life.

---

### 2.2 No exclusivity — similar outputs may go to other customers

**Pattern:** The terms state (or, by silence, do not negate) that the same or substantially similar outputs may be generated for other customers, and the vendor disclaims any exclusivity or uniqueness in outputs.

**Why it matters:** The client may build branding, product features, or content on outputs that a competitor can lawfully obtain in near-identical form, and the non-exclusivity can undercut claims that the output is proprietary to the client.

**What to check:**
- Is there an express non-uniqueness or non-exclusivity statement about outputs?
- Does the client's intended use depend on exclusivity (branding, distinctive content, competitive differentiation)?
- Are there any mechanisms that reduce overlap (fine-tuned or customer-specific models, and who owns those)?

**Most exposed:** Client using outputs for brand assets, customer-facing content, or differentiated product features.

---

### 2.3 IP indemnity that excludes AI-generated output

**Pattern:** The vendor offers an IP infringement indemnity for the "service" or "software" but expressly or structurally excludes claims arising from generated outputs — or conditions any output indemnity on narrow requirements (specific product tiers, unmodified outputs, use of vendor filters, no knowledge of similarity).

**Why it matters:** For a generative AI service, output-related infringement claims are a primary realistic IP exposure. An indemnity that covers only the platform, not the outputs, leaves the client bearing the risk the client most needs covered.

**What to check:**
- Does the indemnity expressly cover third-party claims that outputs infringe copyright or other IP?
- List every condition and carve-out (customer prompts designed to elicit infringing output, modified outputs, disabled safety features, tier restrictions).
- Whether the indemnity is carved out of the liability cap (see `skills/contracts/references/red-flags.md`, Section 1.4).

**Most exposed:** Client publishing, distributing, or commercializing outputs; client generating code, images, or long-form content.

---

### 2.4 No indemnity for training-data claims

**Pattern:** The terms provide no vendor indemnity — or an express exclusion — for third-party claims that the vendor's model was trained on infringing, unlicensed, or unlawfully collected data, even where the claim is directed at the customer's use of the model or its outputs.

**Why it matters:** Claims arising from the vendor's own training-data practices are entirely within the vendor's control and knowledge, yet the exclusion places the resulting risk on the customer, who has no visibility into the training corpus.

**What to check:**
- Does any indemnity or warranty address the provenance or lawfulness of training data?
- Is there an express exclusion for training-data-related claims?
- Are there any vendor representations about training-data licensing, and are they contractual or marketing statements?

**Most exposed:** Client in a litigation-exposed industry or a jurisdiction with active training-data disputes `[verify jurisdiction]`.

**Preferred position:** Customer owns outputs (vendor assigns any rights it has), unconditioned by AUP compliance, with a vendor IP indemnity expressly covering both the service and generated outputs, including training-data-provenance claims, uncapped or subject to a meaningfully higher cap.
**Fallback position:** An unconditional, perpetual, irrevocable license to outputs surviving termination; an output indemnity with only narrow, conduct-based carve-outs (e.g., prompts deliberately designed to reproduce identified third-party works); and an express warranty or representation regarding training-data licensing `[ATTORNEY TO CONFIRM: adequacy for the client's use]`.

---

## 3. Confidentiality Interplay

### 3.1 Prompts and outputs excluded from Confidential Information

**Pattern:** The confidentiality clause defines Confidential Information in a way that excludes — expressly or by omission — customer prompts, inputs, files, or generated outputs, or the AI-specific terms state that submitted content is governed by the data-use clause "notwithstanding" the confidentiality clause.

**Why it matters:** The client may assume its NDA-grade confidentiality expectations cover what it sends to the model, when the operative terms route prompts and outputs into a weaker data-use regime with training, human-review, or de-identification rights. The gap is easy to miss because it lives in the interaction between two clauses.

**What to check:**
- Map the definition of Confidential Information against the definitions of "Customer Content," "Inputs," and "Outputs" — do they overlap or exclude one another?
- Look for order-of-precedence or "notwithstanding" language subordinating confidentiality to data-use rights.
- Check whether outputs the vendor generates are treated as the vendor's confidential information, restricting the client's own use or disclosure.

**Most exposed:** Client inputting trade secrets, deal information, source code, or privileged material.

---

### 3.2 Retention of prompts for abuse monitoring with no limits

**Pattern:** The vendor retains prompts, inputs, and outputs for abuse monitoring, trust and safety, or legal compliance, with no stated retention period, no deletion commitment, no access controls described, and retention rights that survive termination or override deletion requests.

**Why it matters:** Unbounded retention extends the window of exposure for everything the client submits — breach risk, legal process directed at the vendor, human review — and can conflict with the client's own retention schedules and data-subject deletion obligations.

**What to check:**
- Is a maximum retention period stated for abuse-monitoring copies? Quote it, or flag its absence with `[CONFIRM: retention period for monitoring copies]`.
- Do abuse-monitoring retention rights override the deletion obligations elsewhere in the agreement or the DPA?
- Is a zero-retention or reduced-retention option available for the client's tier, and has it been elected?
- How does the vendor handle legal process seeking retained prompts (notice to customer, challenge rights)?

**Most exposed:** Client with regulatory retention/deletion obligations; client inputting privileged or highly sensitive material.

**Preferred position:** Customer inputs and outputs are expressly within Confidential Information, with the confidentiality clause taking precedence over data-use terms, and abuse-monitoring retention limited to a short, stated period with access controls and deletion on expiry.
**Fallback position:** An express statement that data-use rights do not diminish confidentiality obligations, a stated maximum retention period for monitoring copies, restricted access with confidentiality obligations on reviewers, and notice (where lawful) before disclosure of retained content to third parties.

---

## 4. Model Behavior and Change Management

### 4.1 Unilateral model swaps or deprecations without notice

**Pattern:** The vendor may modify, replace, retrain, or deprecate the underlying model — or reroute requests to a different model — at any time, at its discretion, with no or minimal notice and no customer consent right.

**Why it matters:** A model change can silently alter output quality, tone, accuracy, safety behavior, and compliance characteristics that the client validated before deployment. Workflows, evaluations, and downstream approvals built on one model's behavior may not hold for its replacement.

**What to check:**
- Quote the change/modification clause; identify what can change (model, features, endpoints, terms) and on what notice.
- Is there a minimum notice period for material changes or deprecations, and is "material" defined?
- Does the client get a termination or refund right if a change materially degrades the service for its use case?
- Does the change right extend to the terms themselves (rolling terms) — see also `skills/contracts/references/red-flags.md`, Section 11.1.

**Most exposed:** Client with validated, regulated, or customer-facing deployments whose behavior was tested against a specific model.

---

### 4.2 No version pinning or stability commitment

**Pattern:** The terms offer no mechanism to pin a specific model version, no commitment to maintain a version for a stated period, and no advance-notice window before a pinned version is retired.

**Why it matters:** Without version pinning, the client cannot guarantee reproducibility of results, cannot re-run validations against the version in production, and cannot control when it absorbs behavioral change — a particular problem where the client's own governance or regulatory posture requires change control `[Verify current law]`.

**What to check:**
- Is version pinning available, contractual, and included in the client's tier?
- What is the minimum supported lifetime of a pinned version and the notice before retirement?
- Is there a documented migration path (parallel availability of old and new versions for testing)?

**Most exposed:** Client with change-control obligations (regulated industries, safety-relevant uses); client whose outputs feed automated downstream decisions.

---

### 4.3 Benchmark or quality commitments absent or non-binding

**Pattern:** All statements about model accuracy, performance, benchmark results, or output quality live in marketing materials, model cards, or documentation that the contract excludes ("the service is provided without warranty; documentation is for information only"), leaving no contractual performance standard for the model itself.

**Why it matters:** The client's purchase decision typically rests on claimed model quality, yet the contract may make every quality claim non-binding — so degradation, even severe, may breach nothing. Combined with 4.1, the vendor can change the model and disclaim the consequences.

**What to check:**
- Identify every performance-related statement and whether it is inside or outside the contractual documents.
- Is there any objective, measurable quality or accuracy commitment, or an SLA that covers output quality (not just uptime)?
- Does an entire-agreement clause expressly exclude documentation, model cards, and marketing claims?

**Most exposed:** Client that selected the vendor based on benchmark or accuracy claims; client with quality-sensitive use cases.

**Preferred position:** Contractual version pinning with a stated minimum version lifetime, advance written notice of material model changes and deprecations, a parallel-availability migration window, and at least documentation-conformance treated as a contractual commitment.
**Fallback position:** A defined notice period before material model changes or deprecations affecting the client's endpoints, a termination-and-refund right if a change materially degrades the client's validated use, and vendor cooperation in re-validation after material changes.

---

## 5. Usage Restrictions and Dependencies

### 5.1 Acceptable use policy incorporated by reference and changeable unilaterally

**Pattern:** The agreement incorporates an acceptable use policy, usage guidelines, or model-specific policies by URL, and the vendor may update those policies at any time, with continued use constituting acceptance — sometimes with violation of the (changeable) policy as a suspension or termination trigger.

**Why it matters:** The client's permitted use is defined by a document the vendor can rewrite unilaterally. A use case that is compliant at signing can become a terminable violation later, without the client's consent and possibly without effective notice.

**What to check:**
- List every document incorporated by reference; confirm each was actually provided for review — flag any that were not.
- Quote the policy-update mechanism and notice terms; check whether policy violation triggers suspension or termination and on what process.
- Is there a commitment that policy changes will not materially restrict the client's disclosed use case, or a termination right if they do?

**Most exposed:** Client whose use case sits near policy boundaries; client with long integration lead times that make forced exit costly.

---

### 5.2 Restrictions that block the client's actual use case

**Pattern:** The acceptable use policy or usage terms restrict categories that overlap the client's intended use — e.g., restrictions on legal, medical, financial, or employment-related uses, automated decision-making, minors, high-risk domains, or generating advice — stated broadly enough to capture the client's deployment.

**Why it matters:** The client may be in breach from day one, or dependent on an informal vendor assurance that the restriction "isn't meant for them." Breach of use restrictions typically triggers suspension rights and voids indemnities.

**What to check:**
- Map each restriction against the client's stated intended use, item by item; flag every arguable overlap with `[CONFIRM: vendor position on this use case]`.
- Check for "high-risk" or domain-specific carve-outs that require additional terms, human oversight, or disclosures.
- Whether a restricted-use framing tracks any regulatory category is an attorney question `[Verify current law]`.

**Most exposed:** Client in a regulated or sensitive domain (legal, health, finance, HR, insurance, education).

---

### 5.3 Rate limits, throttling, and suspension at vendor discretion

**Pattern:** The vendor may impose, change, or reduce rate limits, quotas, or capacity — or suspend access — at its discretion, without notice, without a commitment to the limits in effect at signing, and without a remedy for the resulting disruption.

**Why it matters:** For a production dependency, discretionary throttling is functionally a partial suspension right. The client's application can be degraded or halted without breach by the vendor, and suspension "for suspected violation" can be exercised on a unilateral, subjective standard.

**What to check:**
- Are the client's committed capacity, rate limits, and quotas stated in the order form or left to discretion?
- What are the suspension triggers, notice requirements, and reinstatement process? Flag "sole discretion" standards (see `skills/contracts/references/red-flags.md`, Section 11.2).
- Is there an SLA covering availability for the client's endpoints, and does throttling count as unavailability?

**Most exposed:** Client with latency- or volume-sensitive production deployments; client without a fallback provider.

**Preferred position:** All usage policies fixed as of the signature date for the term (or changeable only with notice and a no-material-restriction commitment), an express vendor acknowledgment that the client's described use case is permitted, and committed capacity stated in the order form with suspension limited to defined, objective triggers after notice and cure.
**Fallback position:** Advance notice of policy changes with a penalty-free termination right if a change materially restricts the client's use, written pre-clearance of the client's use case, and suspension limited to good-faith, documented violations with prompt notice and reinstatement on cure.

---

## 6. Data Protection Interplay

For the full data-protection review, route to `skills/privacy/dpa-review/SKILL.md` (the data processing agreement itself) and `skills/privacy/vendor-privacy-diligence/SKILL.md` (the vendor's privacy posture). The patterns below are the AI-terms features that most often undermine those documents.

### 6.1 AI terms overriding the DPA

**Pattern:** The AI-specific terms (training rights, retention for monitoring, de-identified data use, human review) conflict with the data processing agreement, and the order of precedence puts the AI terms first — or is silent, leaving the conflict unresolved.

**Why it matters:** A DPA that limits processing to documented instructions can be hollowed out by AI terms granting training and improvement rights over the same data. Which document controls determines whether the client's data-protection position actually holds `[Verify current law]`.

**What to check:**
- Locate the order-of-precedence clause; determine which document controls on data-use conflicts.
- Cross-check every AI-terms data right (training, retention, de-identification, human review) against the DPA's purpose limitation and instruction clauses; list each conflict.
- Confirm the DPA actually covers the AI service and endpoints in scope — not just the vendor's general SaaS offering.
- Route to `skills/privacy/dpa-review/SKILL.md` for the substantive DPA review.

**Most exposed:** Client acting as controller for personal data submitted to the service.

---

### 6.2 Sub-processing of model providers not disclosed

**Pattern:** The AI service is built on one or more third-party foundation models or hosting providers, but the terms and sub-processor list do not disclose the underlying model provider, its role, its data-use rights, or its location — or reserve the right to change model providers without notice.

**Why it matters:** The client's data may flow to an undisclosed third party whose own terms permit training or retention, outside the client's DPA and diligence. A change of underlying model provider is simultaneously a sub-processor change and a model-behavior change (see Section 4).

**What to check:**
- Is the underlying model provider (if any) identified as a sub-processor, with its processing role and location?
- Do the client's data-use protections (no-training, retention limits) flow down to the model provider contractually?
- Is there a sub-processor change-notice and objection mechanism, and does it cover model-provider swaps?
- Route to `skills/privacy/vendor-privacy-diligence/SKILL.md` for the diligence workflow.

**Most exposed:** Client with cross-border transfer constraints or sector-specific data rules `[verify jurisdiction]`.

**Preferred position:** The DPA expressly controls over the AI terms for all personal-data processing; all sub-processors including underlying model providers are disclosed with locations and roles; no-training and retention protections flow down contractually to every sub-processor.
**Fallback position:** A written reconciliation of each identified conflict between the AI terms and the DPA, disclosure of the current model provider(s) with advance notice and an objection or termination right on changes, and vendor confirmation `[CONFIRM: in writing]` that its model providers cannot train on the client's data.

---

## 7. Liability Allocation

### 7.1 AI-specific disclaimers combined with encouraged reliance

**Pattern:** The terms broadly disclaim responsibility for output accuracy, completeness, bias, discrimination, hallucination, or fitness for any purpose — while the vendor's marketing, documentation, or product design encourages the customer to rely on outputs for exactly those purposes. Often paired with a clause requiring the customer to independently verify all outputs.

**Why it matters:** The disclaimer allocates to the customer the core risk of the product failing at its advertised function. Where the customer cannot practically verify every output (high-volume or automated uses), the "customer must verify" clause may be an obligation the deployment cannot satisfy — creating a built-in breach or negligence narrative against the client.

**What to check:**
- Quote each AI-specific disclaimer (accuracy, bias, hallucination, non-reliance) verbatim.
- Compare the disclaimer scope against the client's intended use and against the vendor claims the client relied on in selecting the service.
- Is the verification obligation on the customer compatible with the client's actual deployment (volume, automation, user population)?
- Check whether any affirmative warranty survives (documentation conformance, service description) — see `skills/contracts/references/red-flags.md`, Section 12.1.

**Most exposed:** Client with customer-facing, automated, or decision-supporting deployments; client whose end users will rely on outputs.

---

### 7.2 Liability caps and exclusions that carve out AI-related harms

**Pattern:** The limitation of liability excludes from recovery — or fails to carve out from the cap — the categories where AI harm is most likely to land: output-related claims, discrimination or bias claims, data used in training, IP infringement by outputs, and regulatory penalties. Meanwhile the general cap is fee-based and low relative to the exposure.

**Why it matters:** The general contract analysis (see `skills/contracts/references/red-flags.md`, Section 1) applies with extra force because AI-related losses are typically consequential, hard to quantify, and can arise at scale (many users, many outputs) from a single model behavior. A fee-based cap can be trivial against a scaled harm.

**What to check:**
- List what is excluded from liability entirely versus what is capped; identify where output-related, training-data, and discrimination claims fall.
- Is the IP-output indemnity (Section 2.3) carved out of the cap or trapped under it?
- Compare the cap to a realistic scaled-harm scenario for the client's deployment, not just contract value.
- Check for a super-cap or uncapped treatment for data-protection breaches and confidentiality breaches involving inputs.

**Most exposed:** Client deploying at scale to end users; client in a domain where a single systematic output error propagates widely.

**Preferred position:** Affirmative warranties of documentation conformance; output-related and training-data IP claims, confidentiality breaches, and data-protection breaches carved out of the cap or subject to a meaningfully higher super-cap; no blanket exclusion of AI-related harm categories.
**Fallback position:** A super-cap (multiple of fees) for the highest-exposure categories given the client's use, deletion of any customer verification obligation the deployment cannot operationally satisfy — or its restatement as commercially reasonable procedures — and an express statement that the disclaimers do not limit the vendor's indemnity obligations.

---

## 8. Regulatory and Compliance Posture

Regulatory regimes bearing on AI systems vary by jurisdiction and are evolving; this section describes contract patterns only and asserts nothing about what any regime requires `[Verify current law]` `[verify jurisdiction]`.

### 8.1 Vendor disclaims all regulatory responsibility

**Pattern:** The terms place sole responsibility for legal and regulatory compliance of the client's use — including any obligations arising from the AI system itself — on the customer, with the vendor disclaiming any responsibility for the compliance characteristics of its own model or service.

**Why it matters:** Some compliance obligations may as a practical matter be dischargeable only with vendor cooperation or information the vendor alone holds (training-data characteristics, evaluation results, system design). A total disclaimer can leave the client formally responsible for things it cannot actually verify or control `[Verify current law]`.

**What to check:**
- Quote the compliance-allocation clause; identify exactly what compliance responsibility is placed on the customer.
- Identify which of the client's anticipated compliance tasks depend on vendor-held information or conduct.
- Check whether the vendor makes any compliance-facing commitments about its own service (e.g., it will not knowingly cause the service to violate law) or none at all.

**Most exposed:** Client in a regulated sector, or deploying in a jurisdiction with AI-specific obligations `[verify jurisdiction]`.

---

### 8.2 No cooperation commitments for impact assessments or audits

**Pattern:** The terms contain no obligation on the vendor to cooperate with, or provide information for, the customer's risk or impact assessments, regulatory inquiries, or audits relating to the AI system — or affirmatively prohibit disclosure of vendor information to regulators without consent.

**Why it matters:** If the client's governance framework or a regulator asks for information about the model, an uncooperative vendor with no contractual duty to assist can leave the client unable to respond. A consent requirement before regulator disclosure can put the client in direct conflict with a compulsory process.

**What to check:**
- Is there any cooperation, information, or assistance obligation covering assessments, regulatory inquiries, or audits? Quote it or flag its absence.
- Does confidentiality language restrict the client from sharing vendor information with its regulators, auditors, or advisors? Is there a legal-process carve-out?
- Is cooperation free, cost-reimbursed, or priced at vendor discretion?

**Most exposed:** Client subject to assessment, audit, or supervisory obligations for its AI deployments `[Verify current law]`.

---

### 8.3 Transparency artifacts unavailable or non-contractual

**Pattern:** Model cards, system cards, evaluation summaries, safety testing results, or training-data descriptions are unavailable, provided only under separate NDA at vendor discretion, or expressly excluded from the contract so the vendor bears no responsibility for their accuracy or continued availability.

**Why it matters:** These artifacts are frequently the only substantive basis for the client's own model risk assessment and downstream disclosures. If they are non-contractual, the vendor can withdraw or change them, and the client has no remedy if they were inaccurate.

**What to check:**
- Which transparency artifacts exist, which were provided, and whether the contract incorporates any of them or disclaims them all.
- Is there a commitment to keep artifacts current as the model changes (link to Section 4)?
- Is the client permitted to rely on and reference the artifacts in its own assessments and customer disclosures?
- Route to `model-risk-triage` if the substance of the model's risk characteristics needs assessment.

**Most exposed:** Client whose governance process or downstream customers require documented model information.

**Preferred position:** A mutual compliance-cooperation clause covering assessments, audits, and regulatory inquiries with a legal-process disclosure carve-out; identified transparency artifacts incorporated into the agreement with an accuracy representation and an update commitment.
**Fallback position:** A reasonable-cooperation commitment at defined cost treatment, an express right to disclose vendor information to regulators and auditors under confidentiality, and contractual delivery of at least a current model/system card and evaluation summary `[CONFIRM: which artifacts the vendor will commit to]`.

---

## 9. Service Continuity

### 9.1 Model or endpoint sunset without a migration path

**Pattern:** The vendor may retire the service, a model, or an endpoint the client depends on, with short or no notice, no commitment to a successor, no parallel-running period, and no wind-down assistance — sometimes with sunset framed as a "modification" rather than a termination, avoiding termination protections.

**Why it matters:** An AI integration is typically deeply embedded (prompts, evaluations, fine-tuning, downstream workflows are model-specific). A sunset without a migration window can strand the client's investment and force an unplanned re-validation on a replacement model or vendor.

**What to check:**
- What notice applies to retirement of the service, a model, or an endpoint? Is it different from (and weaker than) termination notice?
- Is there a committed migration path — successor model availability, parallel running, migration assistance, and at whose cost?
- Do wind-down rights (data export, continued access for transition) apply to sunsets as well as termination — see `skills/contracts/references/red-flags.md`, Section 4.4.

**Most exposed:** Client with deep, production-embedded integration and long re-validation cycles.

---

### 9.2 Export of fine-tunes, embeddings, or derived assets denied

**Pattern:** The terms give the client no right to export fine-tuned model weights, adapters, embeddings, vector indexes, prompt libraries stored in the platform, or evaluation data — or state that fine-tunes and derived artifacts belong to the vendor or are deleted (not delivered) on termination.

**Why it matters:** Fine-tunes and embeddings often embody substantial client investment and client data, yet may be technically or contractually locked to the vendor. Denied export converts them into switching costs and can mean client-data-derived assets persist with, or die with, the vendor.

**What to check:**
- Who owns fine-tuned models, adapters, and embeddings created from the client's data? Quote the ownership and license language.
- Is there an export right, in what format, at what cost, and within what post-termination window?
- On termination, are fine-tunes and derived artifacts deleted, retained by the vendor, or delivered to the client? How does this interact with the training-rights analysis in Section 1?

**Most exposed:** Client that has invested in fine-tuning, embedding pipelines, or platform-resident prompt/evaluation assets.

**Preferred position:** Defined minimum notice for any model, endpoint, or service sunset with a parallel-availability migration window and reasonable migration assistance; client ownership of fine-tunes and derived artifacts built on its data, with a contractual export right in usable format surviving termination.
**Fallback position:** Sunset notice at least as long as the client's realistic re-validation cycle with a pro-rata refund and penalty-free exit; where weight export is refused, delivery of the underlying training/tuning datasets, configurations, and evaluation data plus certified deletion of the vendor-held fine-tune `[CONFIRM: what the vendor can technically deliver]`.

---

## 10. Audit and Records

### 10.1 No access to logs or usage records

**Pattern:** The terms give the client no right to access, export, or retain logs of its own usage — prompts, outputs, timestamps, model versions used, safety-filter events — or the vendor's log retention is short, discretionary, or unavailable at the client's tier.

**Why it matters:** Logs are the client's evidence base: for incident investigation, disputes about what the system produced, its own compliance and governance records, and defending claims arising from outputs. Without log access, the vendor holds the only record of what happened.

**What to check:**
- What logging exists, what the client can access or export, in what format, and for how long logs are retained.
- Do logs capture the model version serving each request (link to Section 4 — without this, model-change impact cannot be reconstructed)?
- Can the client require log preservation for a dispute or investigation (litigation-hold cooperation)?
- Note the tension with Section 3.2: the goal is client access to its own records, not unlimited vendor retention.

**Most exposed:** Client with record-keeping or supervisory obligations `[Verify current law]`; client anticipating disputes over specific outputs.

---

### 10.2 No incident notification for model-level failures

**Pattern:** Breach or incident notification covers security incidents only (unauthorized access to data), with no obligation to notify the client of model-level failures — safety regressions, systematic output errors, guardrail failures, poisoning or manipulation events, or incidents discovered in the vendor's own monitoring that affect the client's use.

**Why it matters:** A model-level failure can harm the client's users and business without any data breach occurring. If the vendor learns its model has been producing systematically wrong or harmful outputs and has no duty to tell affected customers, the client continues operating on a defective system and absorbs the downstream exposure.

**What to check:**
- Quote the incident/breach notification clause; identify whether its trigger reaches model behavior and service-integrity failures or only data security.
- Is there a notification timeframe, a defined severity threshold, and a commitment to remediation information the client can act on?
- Does any status page or trust-center commitment exist, and is it contractual or informational?
- Cross-check against the security-incident analysis in `skills/privacy/dpa-review/SKILL.md` — the DPA's breach clause rarely covers model-level failures.

**Most exposed:** Client with end-user-facing deployments; client with its own downstream notification obligations `[Verify current law]`.

**Preferred position:** Contractual client access to complete logs of its own usage (including model version per request) with defined retention and export, litigation-hold cooperation, and a contractual duty to notify the client within a defined period of model-level failures materially affecting its use, with remediation detail.
**Fallback position:** Export of core usage logs on request within a stated window, vendor preservation of logs on written notice of a dispute, and notification of vendor-identified incidents materially affecting the client's tier or endpoints `[CONFIRM: severity threshold and timeframe]`.

---

## Reviewer Notes

- A red flag is a prompt to look closely and flag for attorney attention — not a conclusion that a clause is unenforceable, unlawful, or unacceptable.
- Whether a flagged pattern is a problem depends on the client's role, intended use, data sensitivity, leverage, and risk tolerance — all of which are for the attorney to assess.
- The **Preferred position / Fallback position** lines state the direction of a redline ask, not final clause language and not standard positions; where a practice profile (`practice-profiles/ai-governance.md`) is loaded, its Standard Positions take precedence as the benchmarking source, and any conflict is resolved by the attorney.
- Nothing in this catalog states what any AI, data protection, or consumer protection regulation requires. Every regulatory consideration is described generically and must be verified `[Verify current law]` `[verify jurisdiction]`.
- This catalog is not exhaustive. AI vendor terms evolve quickly; unusual or product-specific provisions not listed here may still warrant a flag.
- See `skills/ai-governance/ai-vendor-terms-review/SKILL.md` for the full review workflow.
- See `skills/contracts/references/red-flags.md` for general commercial contract patterns that also apply to AI agreements.
