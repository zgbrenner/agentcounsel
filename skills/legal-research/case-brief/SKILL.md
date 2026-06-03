---
name: Case Brief
description: "Use when producing a structured brief of a single judicial opinion for attorney review, extracting the facts, procedural posture, issue, holding, reasoning, rule, and weight in a fixed template — with every slot tied to a specific passage in the provided opinion and the case verified against `connectors/courtlistener.md` where applicable."
practice_area: legal-research
task_type: research
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The opinion text (or a verified link to it)"
  - "The matter or research question the brief supports"
  - "The applicable jurisdiction"
  - "Why the case is being briefed (relevance to the matter)"
outputs:
  - "Structured case brief with Holding / Relevance / Weight per case, for attorney review"
related_skills:
  - skills/legal-research/legal-research-memo/SKILL.md
  - skills/legal-research/authority-synthesis/SKILL.md
  - skills/legal-methodology/source-validation/SKILL.md
tags:
  - legal-research
  - case-brief
  - case-law
  - citations
  - irac
---

# Case Brief

## Purpose

Produce a structured, attorney-ready brief of a single judicial opinion. The brief extracts the facts, procedural posture, issue, holding, reasoning, rule, and authority weight into a fixed template, with every slot tied to a specific passage in the opinion the user has provided. It produces draft legal work product for attorney review; it is not legal advice, and it does not determine whether the case binds the operative forum or supports any specific proposition.

The most important disciplines this skill enforces:

- **Every slot is sourced.** No facts, no holding, no rule statement appears in the brief unless it traces to a pinpoint passage in the provided opinion. The skill does not brief the case from memory; it extracts the language of the opinion into slots.
- **The brief pushes back rather than completes.** Where the opinion is ambiguous, the holding is narrow, the reasoning is fact-bound, or the rule is qualified, the brief flags the ambiguity and writes a `[VERIFY: ...]` placeholder rather than smoothing the gap. The attorney is the verifier; the skill is the leash.
- **Authority weight is named, not assumed.** The brief states the court, the date, the precedential level (binding / persuasive / non-precedential), and a *Relevance-to-these-facts* note. Whether the case is *binding in the operative forum* is an attorney-verification item; the skill does not assume.

## Use When

- A specific case has been identified for review and needs a structured brief before being integrated into a memo, brief, or chart.
- A user provides an opinion and asks "what does this case say?" or "is this case relevant to X?"
- A research workflow has surfaced 1–N cases and each needs to be briefed in the same shape before authority synthesis.
- A litigation team needs a structured handoff brief for a case the attorney must read before relying on it.
- A student or new lawyer needs a worked, pinpoint-cited brief of a case to learn how to read judicial opinions.

## Required Inputs

- **The opinion text** — pasted in full, attached, or referenced by a verified URL the skill can read (e.g., a CourtListener URL — see `connectors/courtlistener.md`). The skill **does not brief from memory**; the opinion text must be available in the session.
- **The matter or research question the brief supports** — the legal question the brief will inform. The skill uses this to write the *Relevance-to-these-facts* slot.
- **Jurisdiction and forum of the operative matter** — the forum where the cited authority will be used. Used to label authority weight as binding / persuasive / non-precedential `[verify jurisdiction]`.
- **Why the case is being briefed** — one to two sentences from the user explaining what they want the brief to surface (e.g., "we are evaluating whether the rule announced here applies to a state-court mirror claim").
- Optional: the **claim or argument** for which the case will be cited. If provided, the *Relevance* slot will frame the brief against that specific proposition.

If the opinion text is not available in the session, stop and request it. Do not brief from background knowledge of the case.

## Do Not Use When

- The case has not been read — use `research-plan` first to scope, then locate the case before briefing.
- The task is to synthesize a rule across multiple cases — use `authority-synthesis`.
- The task is a full IRAC research memo — use `legal-research-memo`.
- The case is being briefed to predict an outcome or recommend a course of action — those are attorney determinations; the brief structures the case, it does not advise.
- The opinion is in a language the skill cannot reliably read — stop and request a translation or assistance.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Every slot in the brief traces to a pinpoint passage in the provided opinion, marked with the page, paragraph, or section number the language appears at. No quotation appears in the brief unless it has been verified verbatim against the opinion text. Paraphrases are labeled and flagged for verification.
- Produce draft legal work product for attorney review. This is not legal advice and is not a determination of whether the case binds or persuades any forum.
- **Do not brief from memory.** If the opinion text is not in the session, stop. Do not reconstruct facts, holding, or reasoning from background knowledge of a case the user has named but not provided.
- **Quote verbatim or paraphrase explicitly.** Quotations appear in quotation marks only when the language is taken verbatim from the provided opinion text with a pinpoint cite. Paraphrases are introduced as paraphrases and flagged `[VERIFY: paraphrase — confirm against opinion text]`.
- **Authority weight is `[verify jurisdiction]` by default.** Stating that a case is binding in the operative forum requires knowing the forum's relationship to the issuing court. The skill labels the issuing court, the date, and the precedential level on its face; whether the case is binding *for this matter's forum* is flagged for attorney confirmation.
- **Consult `connectors/` when a verification path is available.** When the session has access to `connectors/courtlistener.md` and the case is in scope (US federal case law and selected state supreme court coverage), confirm the citation form and record the verified opinion URL in the header. A confirmed citation closes "does this case exist with this citation"; it does not confirm "does it stand for the proposition" — that remains attorney work.
- **Holding is the rule the case *actually* decides on its facts.** Do not state a broader rule the court did not adopt. Where the language of the holding could support a narrower or broader reading, flag both and `[VERIFY: scope of holding — attorney to confirm]`.
- **Distinguish holding from dicta.** A passage that is broader than the issue actually decided is labeled "dicta" and not stated as a rule. Dicta may still be relevant; the brief notes it as dicta, not as binding rule statement.
- **Concurrences and dissents are not the holding.** Where they exist, the brief records them as separate sections with their own *Weight* notes (typically `Non-binding`), and does not blend them into the majority holding.
- Use `[CONFIRM: ...]` and `[VERIFY: ...]` placeholders for any slot whose content cannot be tied to a specific passage in the opinion.

## Workflow

1. **Confirm inputs.** Verify the opinion text is available, the matter context is provided, the operative jurisdiction is identified, and the brief's purpose is clear. If any required input is missing, stop and request it.

2. **Header block.** Record the case name, citation, issuing court, date, and (if available via connector) the verified opinion URL. Note the operative matter's jurisdiction and the brief's purpose.

3. **Connector verification.** If the case is in scope per `connectors/courtlistener.md`, confirm the citation form and record the verified URL. If the connector is unavailable or the case is out of scope, retain a `[VERIFY-CITE: citation form not connector-verified]` flag in the header.

4. **Procedural posture.** Identify the procedural posture of the opinion (motion to dismiss, summary judgment, appeal from final judgment, etc.) and any prior history relevant to the holding. Pinpoint cite.

5. **Facts.** Extract the legally relevant facts from the opinion's own statement of facts. Pinpoint cite each. Do not import facts from the user's matter; if the user's facts differ, note the divergence in *Relevance*.

6. **Issue(s).** State the legal question(s) the court actually decides, in the court's own words where possible. Pinpoint cite. Limit to one Issue per case unless the court squarely decides more than one.

7. **Holding.** State the court's resolution of each Issue. Pinpoint cite. Do not generalize beyond the language of the holding; if the holding is narrow, the brief states it narrowly.

8. **Reasoning.** Summarize the court's reasoning, with pinpoint cites to the key passages. Distinguish the controlling reasoning (the path to the holding) from alternative or supplementary reasoning.

9. **Rule.** State the rule the case announces (if any), pinpoint cited. Where the court did not announce a new rule but applied an existing one, the *Rule* slot says so and identifies the applied rule as drawn from the opinion's own framing.

10. **Concurrences and dissents.** For each significant concurrence or dissent, write a short block: who wrote it, what they would have decided differently, pinpoint cite, *Weight* = Non-binding.

11. **Dicta watch.** Identify any passages that read as broader than the holding and label them as dicta with a pinpoint cite.

12. **Relevance to these facts.** Write a one-paragraph slot tying the case to the matter the brief supports. Where the user's facts diverge from the case's facts, surface the divergence. Where the holding is narrower than the use the user is contemplating, say so and flag for attorney attention.

13. **Weight.** Record the precedential weight on its face (e.g., "Federal Circuit Court of Appeals, 2018, precedential opinion"). Add `[verify jurisdiction]` next to "Binding / Persuasive / Non-precedential" classification for the operative forum.

14. **Assumptions and open items.** Note every assumption made (about jurisdiction relationship, about scope of holding, about applicability) and list open items for attorney verification.

15. **Assemble the brief** and label it as a draft for attorney review.

## Output Format

A case brief with the following sections, in order:

1. **Header** — case name, full citation, issuing court, date filed, verified opinion URL (if connector-verified), operative-matter context, brief's purpose, privilege designation.
2. **Procedural posture** — one paragraph, pinpoint cited.
3. **Facts** — bullet list, pinpoint cited per bullet.
4. **Issue(s)** — numbered if more than one, each pinpoint cited.
5. **Holding** — one or two sentences per Issue, pinpoint cited.
6. **Reasoning** — short paragraphs, pinpoint cited.
7. **Rule** — the rule (if any) the case announces, pinpoint cited.
8. **Concurrences and Dissents** — one short block per separate opinion, pinpoint cited, with *Weight*.
9. **Dicta watch** — list of passages broader than the holding, pinpoint cited.
10. **Relevance to these facts** — one paragraph.
11. **Weight** — issuing court, date, precedential status on its face; `[verify jurisdiction]` flag for binding-vs-persuasive in the operative forum.
12. **Assumptions** — explicit list.
13. **Open items / Attorney verification** — checklist.

The brief is capped at one case. Briefing multiple cases against the same Question Presented is the role of `authority-synthesis`, which consumes case briefs as inputs.

## Attorney Verification Checklist

- [ ] The case as cited exists and the citation form is accurate (connector-verified where possible).
- [ ] Every quotation in the brief is verbatim and pinpoint-cited to the opinion text.
- [ ] Every paraphrase has been verified against the opinion text and the *paraphrase* flag has been resolved.
- [ ] The Issue(s) stated are the ones the court actually decides — not a broader question the brief introduced.
- [ ] The Holding is stated no more broadly than the language of the opinion supports.
- [ ] Dicta has been distinguished from the holding and not relied on as binding rule.
- [ ] Concurrences and dissents have been read and their Weight is correctly labeled.
- [ ] The case is binding / persuasive / non-precedential in the operative forum, as flagged `[verify jurisdiction]`.
- [ ] The *Relevance to these facts* slot is accurate; any divergence between the case's facts and the matter's facts has been surfaced.
- [ ] All `[CONFIRM: ...]` and `[VERIFY: ...]` placeholders have been resolved before the brief is relied upon.
