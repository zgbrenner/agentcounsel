# Scanned Documents

Many matters arrive as scanned PDFs — a signed contract, a filed pleading, a
handwritten note, a fax of an exhibit. Before any of that reaches a skill, it
usually passes through OCR (optical character recognition), which turns the
pixels of a scanned page into machine-readable text. This page covers what
that step means for a skill's source discipline, and how to prepare scanned
material safely.

## Why this matters

`core/source-and-citation-discipline.md` requires that every quotation, date,
and figure in a deliverable trace to a source the agent actually reviewed. An
OCR engine can misread a digit, drop a line, garble a signature block, or
silently skip a stamped exhibit number — and the resulting text looks exactly
like clean, reliable input. If that text is treated as the document, an OCR
error becomes a "fact" the skill quotes with confidence. The failure is
invisible precisely because OCR output reads fluently, the same failure mode
`docs/SAFETY_MODEL.md` describes for model hallucination.

## The core discipline

**OCR output is a transcription of an image, not the document itself.**
Treat it accordingly:

1. **Label extracted text as an OCR transcription**, not as the source
   document. A citation map or source log entry for a scanned page should
   say so — for example, "OCR transcription of `exhibit-4.pdf`, p. 3," not
   simply "`exhibit-4.pdf`, p. 3."
2. **Verify every quotation, number, and date against the page image**
   before it enters a deliverable. This is the same verification the source-
   and-citation-discipline rule already requires of any quoted material — a
   scan just means the "source" a reviewer checks against is the page image,
   not the OCR text.
3. **Record page and exhibit provenance for every extraction.** Note which
   page, exhibit number, or bates range a fact or quotation came from, so a
   reviewer (or an attorney) can pull the original page image and check it
   without re-scanning the whole document.

None of this is optional for material facts, quotations, or figures a
deliverable relies on. Treat an unverified OCR transcription the same way
`core/source-and-citation-discipline.md` treats an unverified citation: flag
it, do not assert it as settled.

## Tool options

AgentCounsel adds no OCR dependency to the repository — Markdown-only, no
runtime (see `AGENTS.md`). The tools below are external, installed and run
separately by the user; naming them here is documentation, not an
endorsement or a repository dependency.

- **[MinerU](https://github.com/opendatalab/MinerU)** — a document-parsing
  pipeline aimed at PDF-to-structured-text conversion, including layout and
  table extraction. It ships under a custom, Apache-derived license with its
  own additional terms — read MinerU's own license file before adopting it,
  rather than assuming standard Apache-2.0 terms apply.
- **[marker](https://github.com/VikParuchuri/marker)** — a PDF-to-Markdown
  conversion tool, useful when the target format for a converted document is
  Markdown itself (matching the format skills and matter workspaces use).
- **Plain [Tesseract](https://github.com/tesseract-ocr/tesseract)** or
  **[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF)** — a general-purpose
  OCR engine, or a wrapper that adds an invisible, searchable text layer to
  an existing scanned PDF while leaving the original page images intact.
  Useful when the goal is a searchable PDF rather than an extracted-text file.
- **Word's built-in OCR** (Microsoft Word / OneDrive's "Convert scanned PDF
  to Word document" or Office Lens-style capture) — the lowest-setup option
  for a user who already works in Word and only needs a rough first pass.

Pick based on what the matter needs: a searchable original (OCRmyPDF), a
Markdown-native extraction (marker), a layout-aware structured extraction
(MinerU, with its license read first), or a quick Word-native pass with no
new tool to install (Word's built-in OCR).

## OCR-quality red flags

Some source material degrades OCR accuracy predictably. Treat each of the
following as a reason to flag the affected extraction with
`[CONFIRM against original: ...]` rather than trusting the transcription:

- **Handwriting** — signatures, handwritten notes, interlineations, and
  filled-in blanks are the least reliable OCR category.
- **Tables** — column and row structure is easily scrambled; numbers can
  shift into the wrong cell without any visible error in the output text.
- **Stamps and seals** — date stamps, notary seals, filing stamps, and
  case-number stamps are often skipped entirely or misread as stray text.
- **Marginalia and annotations** — handwritten margin notes, highlighting,
  and redaction marks frequently do not survive OCR, or survive as noise.
- **Low-resolution or poorly scanned exhibits** — faxed pages, multiple
  generations of photocopying, skewed scans, and low-contrast pages produce
  the highest raw error rates.
- **Multi-column layouts** — OCR can interleave text from adjacent columns
  out of reading order.
- **Mixed or non-English text** — footnotes, seals, or exhibits in a
  different language than the OCR engine's configured language setting are
  especially unreliable.

Every flagged item should carry `[CONFIRM against original: <what to check
and where>]` — for example, `[CONFIRM against original: dollar figure in
Table 2, row 4, against exhibit-7.pdf p. 6]` — so the placeholder tells a
reviewer exactly what to pull up and check, consistent with the placeholder
conventions in `core/source-and-citation-discipline.md`.

## Feeding a matter workspace

When a scanned document is converted and used in a `matter-workspaces/`
instance, list it in the workspace's documents index with three fields:

- the **conversion method** used (for example, "OCRmyPDF," "MinerU,"
  "Word built-in OCR," or "manually transcribed" if no tool was used);
- the **verification status** — unverified, spot-checked, or verified
  against the original page images; and
- any **open `[CONFIRM against original: ...]` items** still outstanding for
  that document.

This lets `source_log.md` and `citation_map.md` (see `docs/MATTER_WORKSPACES.md`)
show, for every source-dependent statement, not just which document it came
from but whether the transcription of that document has actually been
checked.

## See also

- `docs/SOURCE_VALIDATION.md` — the broader claim-support classification this
  page's verification step feeds into.
- `core/source-and-citation-discipline.md` — the placeholder and
  source-hierarchy rules this page applies to scanned material specifically.
