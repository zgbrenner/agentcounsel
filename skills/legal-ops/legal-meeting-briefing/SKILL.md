---
name: Legal Meeting Briefing
description: "Use when preparing a structured briefing for a meeting with legal relevance — assembling background, participants, agenda, key documents, open issues, legal considerations, talking points, and a follow-up action-item tracker from the materials provided."
practice_area: legal-ops
task_type: summarization
jurisdictions: []
risk_level: low
requires_attorney_review: true
inputs:
  - "The meeting context: title and type, date and time, participants and roles, agenda, and the legal team member's role"
  - "The background materials the user provides (correspondence, prior notes, agreements, matter records, deal documents)"
  - "Optional: the negotiation parameters or red lines for a negotiation meeting"
outputs:
  - "Structured meeting briefing pack (details, participants, agenda, background, key documents)"
  - "Open issues, legal considerations, talking points, questions, and decisions needed"
  - "Action-item tracker and preparation-gap list"
related_skills:
  - skills/legal-ops/signature-routing-checklist/SKILL.md
  - skills/corporate/board-minutes/SKILL.md
  - skills/corporate/written-consent/SKILL.md
tags:
  - legal-ops
  - meeting-preparation
  - briefing
  - action-items
  - legal-operations
---

# Legal Meeting Briefing

## Purpose

Produce a structured, review-ready draft briefing for a meeting with legal relevance — a deal review, a board or committee meeting, a vendor call, a regulatory meeting, a litigation discussion, or a cross-functional meeting. The briefing organizes background, participants, agenda, key documents, open issues, legal considerations, talking points, questions, and decisions needed, and sets up a tracker for the action items the meeting produces.

This skill provides workflow discipline and structure. It produces draft work product for review. This is not legal advice. A briefing organizes information for a meeting; it does not decide the legal questions the meeting will address.

## Use When

- A user says "prepare me for this meeting," "build a briefing for this board meeting," or "get me ready for this negotiation."
- A legal team member needs a structured briefing pack before a meeting with legal relevance.
- The user needs a way to capture and track the action items that come out of a meeting.

## Required Inputs

- **Meeting context**: the meeting title and type, date and time, the participants and their roles, the agenda or expected topics, and the legal team member's role in the meeting (advisor, presenter, negotiator, observer).
- **Background materials**: the documents and records the user provides — prior correspondence, prior meeting notes, relevant agreements, matter records, the risk register, or deal documents. The skill briefs from the materials supplied; it does not pull information from calendars, email, CRM, CLM, or other external systems.
- **Negotiation parameters** (for a negotiation meeting): the red lines or non-negotiable positions, if any have been set.

If the meeting context is missing, request it. If background materials are thin, proceed and flag the resulting preparation gaps explicitly.

## Do Not Use When

- The user expects the agent to fetch information from a calendar, email, CRM, CLM, or other connected system — this skill briefs only from materials the user supplies.
- The meeting requires a substantive legal position to be decided before it happens — that is attorney work, not a briefing; route it to the relevant practice-area skill or an attorney.
- The task is to draft a board resolution or written consent — use `written-consent` or `board-minutes`.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft work product for review. This is not legal advice. A briefing organizes information; it does not resolve the legal questions in it.
- Brief only from the materials the user provides. Never invent participants, prior communications, document contents, dates, deal terms, or facts.
- In the legal-considerations section, frame points as issues to raise or verify — not as legal conclusions.
- Do not apply a privilege label to any part of the briefing that the supervising attorney has not authorized; for regulatory meetings, flag privilege considerations as items for the attorney.
- Treat talking points and suggested positions as drafts; the attorney owns what is actually said in the meeting.
- Distinguish: facts drawn from the materials, the briefing's synthesis, issues to raise, and preparation gaps.
- Use `[CONFIRM: ...]` placeholders for anything that cannot be resolved from the materials provided.
- Preserve confidentiality; examples and templates use fictional placeholders only.
- Flag every preparation gap rather than filling it with assumption.

## Workflow

1. **Identify the meeting.** Confirm the title, type, date and time, participants and roles, agenda, and the legal team member's role. Request anything missing.

2. **Assess preparation needs by meeting type.** Determine what the briefing must cover:

   | Meeting type | Key preparation needs |
   |---|---|
   | Deal review | Contract status, open issues, counterparty history, approval requirements |
   | Board or committee | Legal-department update, risk-register highlights, pending matters, resolutions needed |
   | Vendor call | Agreement status, open issues, relationship history, negotiation objectives |
   | Regulatory meeting | Matter background, compliance posture, prior communications, privilege considerations |
   | Litigation discussion | Case status, recent developments, strategy, settlement parameters |
   | Cross-functional | Legal implications of the business decision, risk assessment, compliance requirements |

3. **Organize the materials.** Sort the materials the user provided against the briefing structure. Note which expected materials were not provided.

4. **Synthesize the background.** Write a short summary of the relevant history, the current state, and why the meeting is happening.

5. **Build the core sections.** Assemble the participant table, the agenda or expected topics, the key-documents list, and the open-issues table.

6. **Draft legal considerations, talking points, questions, and decisions.** Frame legal considerations as issues to raise or verify. Draft talking points, questions to raise, and decisions needed — each as a draft for the attorney.

7. **Capture red lines.** For a negotiation meeting, record the red lines or non-negotiable positions from the user's input; do not invent them.

8. **Identify preparation gaps.** List materials that could not be found, information that appears outdated, and questions that remain unanswered.

9. **Set up the action-item tracker.** Provide a tracker for the action items the meeting will produce, with a one-owner, one-deadline discipline.

10. **Assemble the briefing** and label it a draft.

## Output Format

Deliver the following sections in order:

**DRAFT MEETING BRIEFING — FOR REVIEW**

1. **Meeting Details** — title, date and time, duration, location or link, and the legal team member's role.

2. **Participants** — table: name, organization, role, key interests, notes.

3. **Agenda / Expected Topics** — the topics, each with brief context.

4. **Background and Context** — a short synthesis of the relevant history and current state.

5. **Key Documents** — the relevant documents, each with a brief description and where it is found.

6. **Open Issues** — table: issue, status, owner, priority, notes.

7. **Legal Considerations** — the legal issues relevant to the topics, framed as issues to raise or verify.

8. **Talking Points** — draft points to make, with supporting context.

9. **Questions to Raise** — the questions and why each matters.

10. **Decisions Needed** — the decisions, with options and a draft recommendation for each.

11. **Red Lines / Non-Negotiables** — for a negotiation meeting, the positions that cannot be conceded (from the user's input).

12. **Prior-Meeting Follow-Up** — outstanding action items from prior meetings with these participants.

13. **Preparation Gaps** — information that could not be found or verified, and questions for the user.

14. **Action-Item Tracker** — table: number, action item, owner, deadline, priority, status — for use during and after the meeting.

## Attorney Verification Checklist

- [ ] The meeting type and the legal team member's role have been correctly identified.
- [ ] Every fact, participant, document reference, and date in the briefing traces to a material the user provided; none was invented.
- [ ] The legal-considerations section frames points as issues to raise or verify, not as legal conclusions.
- [ ] Any privilege consideration — particularly for a regulatory meeting — has been reviewed by the supervising attorney, and no unauthorized privilege label has been applied.
- [ ] Talking points and draft recommendations have been reviewed and adopted, adjusted, or rejected by the attorney before the meeting.
- [ ] Red lines and non-negotiable positions reflect instructions actually given, not assumptions.
- [ ] The preparation gaps have been reviewed and addressed where they are material to the meeting.
- [ ] Each action item in the tracker has exactly one owner and a specific deadline.
- [ ] The briefing has been checked for completeness and accuracy before it is used.
