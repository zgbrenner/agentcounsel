---
name: Open Source License Review
description: "Use when reviewing the open-source licenses present in or proposed for a project to identify compliance obligations and flag compatibility or disclosure risks for attorney review."
practice_area: ip
task_type: review
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The component and license inventory for the project"
  - "The project's distribution model"
  - "How the components are combined and shipped"
outputs:
  - "License-obligations table"
  - "Compatibility and disclosure issues for attorney review"
related_skills:
  - skills/contracts/contract-risk-review/SKILL.md
  - skills/m-and-a/acquisition-diligence-request-list/SKILL.md
tags:
  - ip
  - open-source
  - licensing
  - license-compliance
  - copyleft
---

# Open Source License Review

## Purpose

Produce a structured, attorney-ready review of the open-source licenses present in a software project or proposed for adoption. The review classifies each license by type, identifies the obligations triggered by the project's distribution model, flags copyleft and license-compatibility conflicts, and surfaces components requiring attorney review. This is draft legal work product — not legal advice and not a legal opinion on compliance.

## Use When

- A user asks to "check our open-source dependencies" or "tell me what our OSS obligations are."
- A project is preparing for a product launch, M&A due diligence, or investment round and needs a license inventory review.
- A team is evaluating whether to change how software is distributed (e.g., from internal use to SaaS to binary distribution) and wants to understand the license implications.
- A user has an SBOM (Software Bill of Materials), dependency manifest (`package.json`, `requirements.txt`, `go.mod`, `pom.xml`, `Cargo.toml`, etc.) or similar inventory and wants it reviewed for license risk.
- A user is selecting an open-source license for a new project and wants to understand compatibility with existing dependencies.
- A user has received an OSS compliance audit finding or a license violation notice.

## Required Inputs

- **Component inventory**: a list of open-source components and their associated licenses — from an SBOM, dependency manifest, or manual inventory. Each entry should include: component name, version (if available), and license identifier (SPDX identifier preferred, e.g., `MIT`, `Apache-2.0`, `GPL-3.0-only`).
- **Distribution model**: how the software is or will be delivered. Examples: internal use only (never distributed outside the organization), distributed binary or package (to end users or customers), SaaS / network service (users access the software over a network but receive no binary), open-source release (source code is published). More than one may apply.
- **Proposed outbound license** (if applicable): the license the user intends to apply to their own code.

If the component inventory is not provided, stop and request it. If the distribution model is not provided, flag it as unknown — many license obligations depend on it and the review will be incomplete without it.

## Do Not Use When

- The user needs a full legal compliance opinion or audit — this skill produces a preliminary review; counsel must verify conclusions.
- The matter involves a patent license or patent grant analysis in addition to copyright licensing — refer to patent counsel.
- The user needs to review a proprietary software license or a commercial EULA — use `contract-risk-review`.
- The user needs to evaluate a contributor license agreement (CLA) or inbound contribution policy — refer to a CLA-review skill or counsel.
- The matter involves an OSS-related litigation, injunction, or GPL enforcement action — refer to counsel immediately.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- This is draft legal work product for attorney review. It is NOT legal advice and does NOT constitute a compliance opinion.
- Do not invent license terms, obligations, or conditions. If a license text has not been provided or cannot be verified, flag the component as `[LICENSE TEXT: UNVERIFIED]` and do not assert what the license requires.
- Do not assert that a component's license is `MIT` or `Apache-2.0` or any other identifier based on assumption alone. If the license identifier comes from a manifest or SBOM, note that license identifiers in manifests are often self-reported and must be verified against the actual license file shipped with the component.
- Do not assert that a project is compliant or non-compliant. Use language such as "potential obligation," "flag for attorney review," and "preliminary assessment."
- License compatibility analysis is a legal judgment. Present conflicts and concerns as issues to be evaluated by counsel, not as legal determinations.
- The scope of copyleft obligations (particularly for SaaS/network use and for GPL variants) is actively litigated and interpreted differently across jurisdictions. Do not assert a definitive interpretation.
- Flag every uncertainty with `[CONFIRM: ...]` rather than resolving it silently.
- Preserve confidentiality: component names and distribution models may be commercially sensitive.

## Workflow

1. **Confirm inputs.** Verify that the component inventory and distribution model have been provided. If the inventory is partial or license identifiers are missing for some components, proceed with available information and flag the gaps.

2. **Classify each license by type.** For each component with a known license, assign a preliminary license type:
   - **Permissive**: minimal conditions; attribution typically required (e.g., MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC).
   - **Weak copyleft**: copyleft applies to modifications of the library itself but generally not to the larger work (e.g., LGPL-2.1, LGPL-3.0, MPL-2.0, CDDL-1.0).
   - **Strong copyleft**: copyleft applies to derivative works and combined works; source disclosure may be required (e.g., GPL-2.0, GPL-3.0, AGPL-3.0).
   - **Network copyleft**: copyleft triggered by network access as well as distribution (e.g., AGPL-3.0, EUPL-1.2 in some interpretations).
   - **Source-available / non-OSI-approved**: may restrict commercial use, SaaS, or modification (e.g., BUSL-1.1, SSPL-1.0, Commons Clause additions). Flag these prominently.
   - **Proprietary / Commercial**: no open-source grant; requires separate license. Flag for immediate attorney review.
   - **Unknown / Missing**: license not identified in the inventory; flag for investigation.

3. **Identify obligations triggered by the distribution model.** For each license type, note which obligations are triggered given the stated distribution model:
   - **Attribution and notice**: nearly all permissive licenses require retaining copyright notices and license text.
   - **Source disclosure**: strong copyleft licenses typically require making corresponding source code available when distributing binaries.
   - **License propagation**: some copyleft licenses require the outbound license on the combined/derivative work to be the same or compatible license.
   - **Network trigger**: AGPL-3.0 and similar licenses may require source disclosure when the software is offered as a network service, even without binary distribution.
   - **Notice files**: Apache-2.0 requires a NOTICE file to be included; document which components trigger this.
   - **Patent retaliation clauses**: some licenses (Apache-2.0, GPL-3.0) include patent grant and retaliation terms; flag for patent counsel review if relevant.

4. **Flag copyleft conflicts.** Identify components where the copyleft license may be incompatible with the proposed outbound license or with other components in the project. Common conflict patterns to flag:
   - GPL-2.0 and GPL-3.0 are incompatible in combined works without the "or later" clause.
   - LGPL-2.1 and GPL-3.0 compatibility depends on upgrade clauses.
   - Apache-2.0 and GPL-2.0 have a known compatibility tension (flag for attorney analysis; GPL-3.0 is generally considered compatible with Apache-2.0).
   - Proprietary or source-available components mixed with strong copyleft may create conflicts.
   Do not assert a definitive incompatibility conclusion; flag each as requiring attorney analysis.

5. **Flag missing and unknown licenses.** For any component where the license is not identified, unknown, or where the stated identifier could not be verified against actual license text: flag with `[LICENSE: UNKNOWN — INVESTIGATE]` and note that use of a component with an unknown license is a legal risk that must be resolved before distribution.

6. **Identify components requiring priority attorney review.** Produce a prioritized flag list:
   - **Priority 1**: AGPL, GPL, or other strong/network copyleft in a distributed or SaaS product; proprietary components; unknown licenses.
   - **Priority 2**: LGPL components in statically linked or tightly integrated use; source-available components with commercial restrictions; patent grant or retaliation clauses relevant to the business.
   - **Priority 3**: Permissive components where attribution obligations have not been tracked or fulfilled; notice file requirements.

7. **Assess outbound license compatibility** (if a proposed outbound license was provided). Note whether the proposed outbound license is compatible with the license obligations identified for inbound components, and flag incompatibilities for attorney analysis.

8. **Assemble the output** as specified in the Output Format below. Label the full output as a preliminary review draft for attorney review.

## Output Format

Deliver the following sections in order:

**1. Review Summary**
- Project name (if provided), distribution model, outbound license (if provided), date of review.
- Total components reviewed; count by license type; count of flagged items by priority.
- Overall risk signal: Elevated / Moderate / Lower — with explicit caveat that this is a preliminary triage, not a compliance opinion.

**2. Per-Component Obligations Table**

| Component | Version | License Identifier | License Type | Key Obligations | Flags |
|---|---|---|---|---|---|
| (name) | (version) | (SPDX ID or `[UNKNOWN]`) | (type) | (attribution, source disclosure, notice file, etc.) | (priority flag or none) |

Each row should be concise. Use `[CONFIRM: ...]` for any cell requiring verification.

**3. Prioritized Issues List**
- **Priority 1 — Requires Immediate Attorney Review**: bulleted list with brief explanation for each issue.
- **Priority 2 — Requires Attorney Analysis**: bulleted list.
- **Priority 3 — Compliance Hygiene**: bulleted list of attribution and notice obligations to track.

**4. License Compatibility Notes**
- Summary of any copyleft compatibility concerns between inbound licenses, and between inbound licenses and the proposed outbound license.
- Each item labeled as preliminary and flagged for attorney analysis.

**5. Recommended Next Steps**
- What additional information is needed (license texts for unknown components, clarification of distribution model, etc.).
- What counsel should focus on.
- Whether any commercial license or dual-license option should be explored.

**6. Assumptions and Open Items**
- All facts assumed or inferred, and all `[CONFIRM: ...]` items requiring resolution.

## Attorney Verification Checklist

- [ ] The component inventory is complete and reflects the actual dependencies shipped or executed in the distribution.
- [ ] Each license identifier has been verified against the actual license text shipped with the component, not only the manifest-declared identifier.
- [ ] The distribution model is accurately characterized; any planned changes to distribution (e.g., moving from internal to SaaS or binary release) have been accounted for.
- [ ] All components flagged as Priority 1 have been individually reviewed by counsel.
- [ ] Network copyleft exposure (AGPL-3.0 and equivalents) has been evaluated for the SaaS or API-service distribution model.
- [ ] Copyleft compatibility conflicts identified in this review have been analyzed and resolved by counsel.
- [ ] Attribution, notice, and NOTICE file obligations have been inventoried and a compliance plan is in place.
- [ ] Unknown license components have been investigated and resolved before distribution.
- [ ] Patent grant and patent retaliation clauses have been reviewed where relevant to the business.
- [ ] The proposed outbound license has been confirmed as compatible with all inbound licenses by counsel.
- [ ] No license terms have been asserted or relied upon without verification of the current, applicable license text.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved before the review is relied upon for distribution, M&A, or compliance purposes.
