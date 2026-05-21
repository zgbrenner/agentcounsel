# [Sector Name] Overlay

> Template. Copy `overlays/_template/` to `overlays/<sector>/` and replace
> every `[bracketed placeholder]`. Delete this note when done.

This overlay tunes AgentCounsel's existing skills for **[sector / industry /
client type]** work. It is internal configuration material, not legal advice
and not legal work product. A supervising attorney reviews it before use.

## What this sector is

[Two to four sentences describing the sector and the kind of organizations and
matters it covers. State plainly that the sector is a context, not a separate
body of law — the legal work is the library's normal practice-area work,
coloured by this sector.]

## Skills this overlay modifies

List the existing skills this overlay is most often loaded alongside, and how
the sector changes the analysis.

| Skill | How the sector changes the work |
|---|---|
| `skills/[area]/[skill]/SKILL.md` | [What the overlay adds — extra gates, sector terminology, sector-specific risks to scan for.] |
| `skills/[area]/[skill]/SKILL.md` | [...] |

## Sector gates and escalation triggers

Conditions that, in this sector, must stop a workflow and route the matter to a
specialist or supervising attorney before it proceeds.

- [Trigger — e.g., the matter involves a regulated activity that requires a
  licence or authorization. Route to [specialist].]
- [Trigger — e.g., the data in scope includes a sector-specific sensitive
  category. Apply heightened handling and confirm with counsel.]
- [Add the sector's own escalation triggers.]

## Sector context the agent should know

- **Typical regulators / oversight bodies:** [name them generically, or record
  `[ATTORNEY TO CONFIRM]` — do not guess].
- **Key terminology:** [sector terms an agent should recognize and use
  precisely].
- **Common document types:** [documents distinctive to this sector].

## What this overlay does NOT change

- It does not replace any skill, template, or `core/` operating rule.
- It does not state the law of the sector or of any jurisdiction. Sector-
  specific legal rules remain attorney-verification items (`[verify
  jurisdiction]`, `[ATTORNEY TO CONFIRM: ...]`).
- It does not lower the attorney-review requirement. Every deliverable is still
  draft work product for attorney review.

## How to use this overlay

Load it, after the `core/` rules, the practice profile, and the skill, when the
matter is in this sector. See `overlays/README.md`.

## Status

`experimental` — [or `stable` once the overlay has a completed profile, any
sector-specific skills have evals, and a subject-matter expert has reviewed
it]. Recorded in `docs/PRACTICE_AREAS.md`.
