---
name: Trademark Clearance Triage
description: "Use when a user wants a preliminary triage of a proposed brand name, product name, or logo before engaging trademark counsel for a formal clearance search."
practice_area: ip
task_type: triage
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The proposed brand name, product name, or logo"
  - "The goods and services it will be used for"
  - "The target markets and jurisdictions"
outputs:
  - "Trademark clearance triage summary with a preliminary signal for trademark counsel"
related_skills:
  - skills/ip/cease-and-desist-response/SKILL.md
  - skills/ip/infringement-triage/SKILL.md
  - skills/contracts/contract-risk-review/SKILL.md
tags:
  - ip
  - trademark
  - brand-clearance
  - triage
  - naming
---

# Trademark Clearance Triage

## Purpose

Produce a structured preliminary triage of a proposed trademark — a brand name, product name, slogan, or logo — to identify obvious concerns and orient the client before engaging trademark counsel for a formal clearance search and opinion. This is draft legal work product for attorney review. It is NOT a clearance opinion, NOT a freedom-to-operate determination, and does NOT constitute a legal finding that any mark is available for use or registration.

## Use When

- A user asks to "check if a name is available" or "see if we can trademark this."
- A user wants to know if a proposed brand name, product name, or slogan is likely to face trademark issues.
- A client is in early brand development and wants a structured starting point before commissioning a full clearance search.
- A user needs a triage summary to brief trademark counsel efficiently.
- A user asks what a formal trademark clearance process involves and what inputs counsel will need.

## Required Inputs

- **The proposed mark**: exact name, slogan, or description of the logo/design element.
- **Goods and/or services**: a plain-language description of the products or services the mark will identify (e.g., "mobile app for personal finance," "organic coffee beans sold online").
- **International Classification (Nice Classes)**: if the user knows the relevant class(es), capture them; if unknown, note that class identification is an attorney task and provide a general description only.
- **Geographic markets**: primary and secondary markets (e.g., United States, EU, Canada).
- **Intended use**: whether use has already begun (use-in-commerce) or is planned (intent-to-use), and approximate timing.

If the proposed mark text is not provided, stop and request it before proceeding. If goods/services or geographic market are not provided, flag them as unknown and note that the triage will be incomplete without them.

## Do Not Use When

- The user needs a formal trademark clearance opinion or freedom-to-use determination — refer to trademark counsel.
- The user has received a cease-and-desist letter and needs to respond (use `cease-and-desist-response`); responding to an opposition or cancellation proceeding is separate, attorney-directed work.
- The document to review is a license agreement, co-existence agreement, or assignment — use `contract-risk-review`.
- The user needs a copyright analysis (use `dmca-takedown` for DMCA takedown matters) or a patent search — general copyright clearance and patent work are outside the scope of this triage.

## Legal Safety Rules

- This triage is draft legal work product for attorney review. It is NOT a clearance opinion, NOT legal advice, and does NOT mean the mark is available for use or registration.
- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available. Do not invent trademark registration numbers, application serial numbers, owner names, filing dates, or opposition history. If the user has not provided registry data and no verified research tool has been used, state that no registry search has been conducted.
- **Consult `connectors/uspto.md` when a verification path is available** to confirm that a referenced trademark registration or application exists and to record its serial/registration number, owner of record, and TSDR prosecution status as facts for counsel — for existence and status only, never to conclude that a mark is available, distinctive, registrable, or free of conflict, and never to compute a renewal or response date (which stays `[deadline verification required]`); when no such tool is available, state that no registry search has been conducted.
- Do not assert that a mark is clear, available, or registrable. Use language such as "preliminary risk signal" and "factors for counsel to evaluate."
- Do not invent case law, statutory text, or USPTO/EUIPO/UKIPO guidance. If citing a legal concept (e.g., likelihood-of-confusion factors), characterize it as a general framework and flag it for attorney verification.
- Characterize the mark's distinctiveness as a preliminary, unverified assessment only. Distinctiveness characterization is always an attorney verification item.
- Separate facts provided by the user from analytical observations and from items requiring attorney or registry verification.
- Flag every uncertainty with `[CONFIRM: ...]` rather than resolving it silently.

## Workflow

1. **Confirm inputs.** Verify that the proposed mark, goods/services description, and at least one target geographic market have been provided. If any are missing, stop and request them. Record the inputs exactly as provided; do not paraphrase the mark.

2. **Characterize the mark on the distinctiveness spectrum.** Assess — preliminarily and without asserting legal certainty — where the mark falls among: generic, descriptive, suggestive, arbitrary, or fanciful. Note that this characterization is for orientation only and must be confirmed by counsel. Flag any mark that appears generic or merely descriptive as carrying elevated registration risk.

3. **Identify obvious concerns.** Without conducting a registry search, note:
   - Whether the mark is a common English word, phrase, or acronym that may be in wide use.
   - Whether the mark is geographically descriptive or primarily merely a surname.
   - Whether the user has mentioned any known prior users, existing marks, or industry context that raises conflict signals.
   - Whether the mark includes terms that may be refused (laudatory, deceptive, primarily merely descriptive, scandalous — as applicable and without asserting a legal ruling).

4. **Identify goods/services classification.** Provide a general description of the likely Nice Class(es) based on the goods/services description, with the explicit caveat that class identification must be confirmed by counsel or a trademark professional. Do not assert a definitive class.

5. **Outline the screening searches a formal clearance would cover.** List the categories of search a professional clearance typically includes (e.g., USPTO TESS/TSDR, state trademark registries, common law use searches, domain name registries, relevant international registries). Do not represent that these searches have been conducted.

6. **Identify what counsel will need.** Summarize the inputs, decisions, and documents trademark counsel will require to conduct a proper clearance, file an application, or advise on registrability.

7. **Generate a preliminary risk signal.** Assign a preliminary signal — **Elevated**, **Moderate**, or **Lower** — based solely on the inputs and obvious factors identified, with an explicit note that this signal is not a legal opinion and may change materially after a proper search.

8. **Assemble the output.** Label it clearly as a preliminary triage draft for attorney review.

## Output Format

Deliver the following sections in order:

**1. Triage Summary**
- Proposed mark (verbatim), goods/services, target markets, intended use, and date of triage.
- Preliminary risk signal: Elevated / Moderate / Lower (with caveat that this is not a legal opinion).

**2. Distinctiveness Characterization (Preliminary)**
- Where the mark appears to fall on the generic–fanciful spectrum, and why, as a preliminary assessment only.
- Flags for descriptiveness, surname issues, geographic descriptiveness, or other registrability concerns.

**3. Obvious Concerns**
- Bulleted list of concerns identifiable from the mark itself and the user-provided context, without registry search.
- Each concern labeled `[CONFIRM: ...]` where attorney verification is required.

**4. Goods/Services and Classification Notes**
- Plain-language description of the goods/services and likely Nice Class(es), with caveat.
- Note any breadth or specificity issues in the description that counsel should address.

**5. Formal Clearance Scope (What a Proper Search Would Cover)**
- Bulleted checklist of search categories a professional clearance typically covers.
- Explicit statement that none of these searches have been conducted as part of this triage.

**6. What Counsel Will Need**
- Bulleted list of inputs, decisions, and documents for the engaging attorney.

**7. Assumptions and Open Items**
- All facts assumed or inferred, and all items flagged for resolution before the triage can be relied upon.

## Attorney Verification Checklist

- [ ] The proposed mark text, goods/services description, and target markets have been confirmed with the client.
- [ ] A full professional clearance search (federal, state, common law, international as applicable) has been commissioned and reviewed.
- [ ] The distinctiveness characterization has been evaluated by counsel; no registrability conclusion has been drawn from this triage alone.
- [ ] No trademark registration numbers, application status data, or ownership information has been asserted without verified registry research.
- [ ] The Nice Class(es) and identification of goods/services have been confirmed by a trademark professional.
- [ ] No legal authority, statutory text, or case law has been asserted without verification.
- [ ] Counsel has confirmed that use of the mark will not begin until clearance is complete.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved before the triage is relied upon for any business or legal decision.
- [ ] Client has been advised that this triage is not a clearance opinion and does not establish that the mark is available for use or registration.
