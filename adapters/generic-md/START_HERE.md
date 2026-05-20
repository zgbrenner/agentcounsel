# Start Here — Generic Markdown Use

A short walkthrough for using one AgentCounsel skill inside any AI assistant or legal agent.

## Step 1 — Find the right skill

Open `WORKFLOW_ROUTER.md` and match your task ("review this NDA," "build a timeline," "review a DPA") to a skill. If you would rather browse, use `SKILLS_INDEX.md`.

## Step 2 — Load the core rules

Copy the files in `core/` into your assistant as context. These are the operating rules every skill depends on:

- Draft legal work product only; attorney review is required.
- Never invent authority, citations, quotations, facts, or deadlines.
- Separate facts, assumptions, law, analysis, strategy, and verification items.
- Identify jurisdiction, governing law, posture, and the relevant date.
- Preserve confidentiality and privilege.

You can paste these once per session and reuse them.

## Step 3 — Load the skill

Copy the chosen `SKILL.md` (and any file in its `templates/` folder) into the same context.

## Step 4 — Give the assistant a clear instruction

Tell the assistant, in substance:

> Use the AgentCounsel skill below. Follow its Workflow and Output Format, and follow the AgentCounsel core rules. Produce draft legal work product for attorney review. Do not invent legal authority, citations, or deadlines. Flag anything uncertain with placeholders.

Then provide the skill's **Required Inputs** — the document, the facts, the client role, the jurisdiction, and so on.

## Step 5 — Check the inputs gate

If you cannot supply a Required Input, expect the skill to stop and ask. Do not let the assistant proceed by guessing. Missing inputs become `[CONFIRM: ...]` placeholders.

## Step 6 — Review before use

The output is a **draft**. Before anyone relies on it:

- Complete the skill's Attorney Verification Checklist.
- Verify every citation, quotation, date, and fact.
- Resolve every placeholder.
- Have a qualified, licensed legal professional review and adopt the work.

## Tips

- **One skill at a time.** Load only the skill you need; do not paste the whole library.
- **Mind confidentiality.** Only use AI tools approved for the client and the matter. See `SECURITY.md`.
- **Reuse the core rules.** They are the same for every skill.
