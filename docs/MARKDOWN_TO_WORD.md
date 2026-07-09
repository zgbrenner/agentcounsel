# From Markdown draft to Word redline

Every AgentCounsel skill produces a plain Markdown deliverable. Most lawyers do
not redline in Markdown — they redline in Word, with tracked changes, firm
styles, and a signature block their document-management system recognizes.
This page is the bridge between the two: turning a skill's Markdown output
into a `.docx` a supervising attorney can open, mark up, and circulate.

AgentCounsel stays Markdown-only (see "No code in a skill" in `AGENTS.md`).
Nothing below adds a dependency to the library itself — it is guidance for
converting a finished draft on your own machine, using tools you install
separately.

## The pandoc path

[Pandoc](https://pandoc.org/) is a free, external document-conversion tool
(GPL-licensed) that reads Markdown and writes `.docx`, among many other
formats. It is not part of this repository and nothing here bundles it — you
install it yourself (`brew install pandoc`, your package manager, or the
installer on pandoc's site), then run it against a skill's output file.

The basic conversion:

```
pandoc draft.md --reference-doc=firm-template.docx -o draft.docx
```

`draft.md` is the Markdown file a skill produced (or that you saved from a
chat). `firm-template.docx` is your own firm's Word template — the one with
the firm's fonts, margins, heading styles, and page setup already configured.
Pandoc uses the Markdown file for **structure** (headings, tables, lists,
emphasis) and the reference doc for **formatting** (what a Heading 2 or a table
looks like). The output, `draft.docx`, is a Word file dressed in the firm's
own house style, ready to open in Word and turn on Track Changes.

If you do not have a firm template handy, generate a starting point from
pandoc's own defaults and then edit its styles in Word to match your firm:

```
pandoc -o custom-reference.docx --print-default-data-file reference.docx
```

Open `custom-reference.docx` in Word, adjust the built-in styles (Title,
Heading 1–3, Body Text, Table Grid, and so on) to match the firm's standard,
save it, and use it as the `--reference-doc` for every future conversion.
Build it once per firm or practice group; reuse it for every draft.

## What survives conversion, and what to check

Pandoc converts Markdown structure faithfully in most cases:

- **Headings** (`#`, `##`, `###`) become Word heading styles, which is what
  makes the reference-doc styling work and what lets Word build a table of
  contents if the firm template has one configured.
- **Tables** — the risk tables, key-terms tables, and negotiability tables
  most skills produce — convert to native Word tables.
- **Bulleted and numbered lists**, bold/italic emphasis, and blockquotes
  (used for the "Draft for attorney review" framing) all carry over.

What needs a manual check before the draft goes to an attorney:

- **Placeholders.** This library's entire safety model depends on
  `[CONFIRM: ...]`, `[VERIFY: ...]`, `[deadline verification required]`, and
  similar bracketed placeholders staying **visible** in the reviewed document.
  Pandoc does not strip them, but Word's default styling can make bracketed
  text easy to skim past, and a careless "accept all" during editing can
  delete one along with the surrounding sentence. Before sending the `.docx`
  to the attorney, run a **find pass in Word** (Ctrl/Cmd+F for `[CONFIRM`,
  `[VERIFY`, `[ATTORNEY TO CONFIRM`, `[deadline verification`) and
  highlight every hit. A placeholder that silently disappears in conversion
  or editing is exactly the failure mode this library exists to prevent —
  never treat the `.docx` as final until that pass is done.
- **Nested or unusual Markdown** — deeply nested lists, tables inside list
  items, or footnote-style syntax some skill templates do not use — can
  render imperfectly. Skim the converted document once against the source
  Markdown for structural drift, especially around tables.
- **The draft/attorney-review label.** Confirm the "Draft legal work product
  for attorney review — not legal advice" framing every skill's Output Format
  carries is still present and visible near the top of the converted document.

## Optional: turning placeholders into Word comments

Some teams prefer their firm's placeholders to show up as native Word
**comments** anchored to the flagged text, rather than as inline bracketed
text. That conversion is not something pandoc does out of the box, and it is
outside what this repository's own tooling covers — `scripts/` is Python
standard library only, with no third-party dependencies (see `AGENTS.md`).

Teams that want this can write a small local script using
[python-docx](https://python-docx.readthedocs.io/) (MIT-licensed, installed
separately with `pip install python-docx`) to scan the converted `.docx` for
the placeholder patterns and re-insert each one as a comment on the adjacent
run. This is genuinely optional, external-tool scripting — it does not belong
in this repository's `scripts/` directory, and it does not change the
underlying safety rule: every placeholder must still be visibly resolved (or
visibly unresolved) before an attorney relies on the document.

## PDF, if that's what's needed instead

The same tool produces a PDF directly, without the Word round-trip, for
drafts that only need to be read or filed rather than redlined:

```
pandoc draft.md -o draft.pdf
```

A firm-branded PDF is possible too, with a LaTeX or HTML template argument to
pandoc, but that is a separate setup from the `--reference-doc` approach above
and worth doing only if PDF is the team's primary distribution format.

## See also

- `core/output-format-rules.md` — why placeholders exist and what they mean.
- `docs/ATTORNEY_REVIEW_GATE.md` — the review gate a converted draft still has
  to pass before anyone relies on it.
- `docs/CHOOSE_YOUR_WORKFLOW.md` — choosing among skills, packs, and
  workspaces before you get to the point of exporting a draft at all.
