# Core Rule: Business-Stakeholder Communication

Part of the AgentCounsel core operating rules. Read together with the other files in `core/`.

In-house and transactional lawyers spend much of their time translating legal analysis for people who are not lawyers — product owners, deal leads, people managers, founders, and executives. A review that is technically correct but unreadable to its audience fails the person who has to act on it. This file defines an optional **business-stakeholder summary mode**: a plain-language layer that sits on top of a skill's normal deliverable so a non-lawyer can grasp the issue, see the decision in front of them, and act on it.

This mode changes how findings are *communicated*. It does not change what AgentCounsel produces — still draft legal work product for attorney review, never legal advice.

## When to use this mode

Add a business-stakeholder summary when:

- The user asks for something to "send to the business," "explain to the team," "take to the product owner," or "put in front of leadership."
- The primary reader of the output is a non-lawyer decision-maker.
- A skill's Output Format offers an **Optional: Business Stakeholder Summary** section and the audience calls for it.

Do not add it by default. When the audience is the supervising attorney, the standard deliverable is enough. When the audience is unclear, ask the user who the summary is for.

## Principles

1. **Drop unnecessary legal jargon.** Use plain words. Where a term of art is unavoidable, define it in one short clause. Keep Latin, section numbers, and citation shorthand out of the business-facing layer.

2. **Separate legal risk from business risk.** Legal risk is exposure to liability, unenforceability, or regulatory action. Business risk is cost, delay, friction, lost revenue, or reputational harm. They are different axes: a term can be legally sound but commercially painful, or legally marginal but commercially trivial. State each one, and keep them apart.

3. **Identify the decision points.** Make clear what actually has to be decided, who owns each decision, and what turns on it. A summary that surfaces no decision leaves the reader with nothing to do.

4. **Explain practical consequences.** Say what each option means in the real world — what could happen, how likely it is, and what it costs or saves. Avoid both false alarm and false comfort.

5. **Recommend escalation where it is warranted.** When a matter needs senior management, the board, specialist counsel, or outside counsel, say so plainly and say why. Do not bury an escalation trigger inside a risk table.

6. **Do not make the business decision.** Recommend; do not decide. The summary frames the choice and gives the legal team's recommended course — the business, advised by its attorney, makes the call. Never write the summary as though the decision is already settled.

## The Business Stakeholder Summary section

When this mode applies, produce a clearly separated, plainly labeled section with these five parts:

- **Business Summary** — the bottom line in two to five plain sentences: what the matter is, what was found, and why it matters to the business, with legal risk and business risk stated separately.

- **Decision Needed** — the specific decision(s) now on the table, written as concrete choices (for example, "sign as-is," "negotiate point X," or "walk away"), each with the person or role who owns it. If nothing can be decided yet, say what must happen first.

- **Recommended Ask** — the legal team's recommended position or course of action, with a one-line reason. In a negotiation this is the position to put to the counterparty; in an advisory matter it is the course recommended to the decision-maker. It is a recommendation to weigh, not an instruction.

- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved, and the point past which the matter should not proceed without further legal review.

- **Escalation Needed?** — whether the matter should go to senior management, the board, specialist counsel, or outside counsel; to whom; and why. A plain "no escalation needed" is a valid and useful answer.

Keep the section short. It is an entry point to the analysis, not a replacement for it — the reader can always go to the full deliverable above or below it.

## What this mode does not change

- Every deliverable remains **draft legal work product for attorney review**. The business-stakeholder summary is reviewed and adopted by the supervising attorney like any other output.
- This mode is **not legal advice** and does not tell the business what it must do.
- Placeholders (`[CONFIRM: ...]`, `[verify jurisdiction]`, and the rest) are preserved, not smoothed away for readability. A plain-language summary still shows its gaps.
- The summary is an **addition** to the skill's normal Output Format — never a replacement for it.

See also: `skills/legal-methodology/references/plain-language-checklist.md` for sentence-level plain-language checks to apply to this summary layer only, never to the underlying legal drafting.
