# Core Rule: Output Format Rules

Part of the AgentCounsel core operating rules. Read together with the other files in `core/`.

Consistent structure makes legal work product easier to review, safer to rely on, and harder to misread. These rules govern how every deliverable is formatted, on top of any format defined by the specific skill.

## Label the draft

Every deliverable opens with a short status line, for example:

> **Draft legal work product for attorney review. Not legal advice.**

Where appropriate, add a privilege designation for the attorney to confirm (for example, "Privileged & Confidential — Attorney Work Product").

## Separate the layers

Keep these categories visibly distinct — separate sections, never blended:

- **Facts** — what is established by a source document or by the client.
- **Assumptions** — what the analysis takes as given but has not confirmed.
- **Law / Authority** — applicable authority, each item verified or flagged for verification.
- **Analysis** — how the law and facts interact; reasoning and options.
- **Strategy** — practical recommendations and considerations, clearly marked as optional and for attorney judgment.
- **Verification items** — open questions and things a person must check.

A reader must always be able to tell which layer a statement belongs to.

## Use placeholders, not guesses

Mark every gap with a visible placeholder rather than filling it. Use the general forms for any gap, and the specific forms for common cases:

- `[CONFIRM: ...]` — information the user or attorney must supply.
- `[VERIFY: ...]` — authority or a factual claim that must be checked.
- `[ATTORNEY TO CONFIRM: ...]` — a point of legal judgment.
- `[Attorney to insert authority]` — a stated legal proposition with no verified authority behind it.
- `[Verify current law]` — a point that depends on law that may have changed.
- `[Confirm local rule]` — a procedural or local-rule point to check against the specific forum.
- `[citation needed]` — a legal proposition that needs supporting authority.
- `[pin cite needed]` — a citation that needs a specific page or paragraph reference.
- `[verify jurisdiction]` — a point that depends on an unconfirmed jurisdiction.
- `[deadline verification required]` — any date or deadline; never compute one.

Never silently resolve a gap. See `core/source-and-citation-discipline.md` for the placeholder vocabulary.

## Standard deliverable skeleton

Unless a skill specifies otherwise, structure a deliverable as:

1. **Heading block** — draft label, matter reference, prepared-for, date, privilege designation.
2. **Summary** — a short, plain-language overview.
3. **Body** — the skill-specific analysis, using the layered sections above.
4. **Assumptions** — every assumption made.
5. **Verification items** — open questions and items to check.
6. **Attorney verification checklist** — the baseline checklist plus any skill-specific items.

## Style

- Plain, precise language. Define terms of art on first use.
- Short paragraphs; tables and lists where they aid review.
- State uncertainty directly; do not hedge into vagueness.
- No hype, no overstatement of confidence, no filler.
- Clean Markdown, so the deliverable stays portable across tools.
