> Shared reference material supporting the AgentCounsel legal-research and legal-methodology skills, used to help produce draft legal work product for attorney review — not legal advice.

# Citation Type Taxonomy

This reference gives a reviewer a vocabulary for classifying what *kind* of
citation a passage in a draft actually is, before deciding what verifying it
would require. Different citation forms carry different verification needs
and different hallucination risks — an `id.` is only meaningful in relation
to the citation before it, while a full case citation can be checked in
isolation. This taxonomy does not verify anything itself; it tells a skill
which question to ask for each citation form it finds.

**Attribution.** The set of citation-type categories below is adapted from
the classification scheme used by eyecite, an open-source citation-extraction
library maintained by the Free Law Project, licensed BSD-2-Clause. The
descriptions of each type, the verification needs, and the hallucination-risk
notes are written independently for AgentCounsel; they are not eyecite's
code, docstrings, or documentation text.

---

## How Skills Use This File

`skills/legal-methodology/citation-integrity-check/SKILL.md` and
`skills/legal-methodology/source-validation/SKILL.md` classify each citation
in a draft before assessing its source status or integrity. This taxonomy is
the vocabulary for that classification step — it identifies *what form* a
citation takes; the two skills above still own the questions of *whether it
is real*, *whether it is complete*, and *whether it supports the proposition
asserted*. Legal-research skills that assemble authority-heavy drafts (for
example `skills/legal-research/legal-research-memo/SKILL.md` and
`skills/legal-research/authority-synthesis/SKILL.md`) can also use this
taxonomy while drafting, to keep short-form citations correctly anchored to
the full citation they depend on.

---

## Citation Types

### Full case citation

**What it looks like:** A complete citation to a court decision — case name,
reporter volume, reporter abbreviation, starting page (and pin cite if
applicable), court, and year, e.g. a pattern like `Party A v. Party B, 123
F.3d 456, 460 (9th Cir. 1999)`.

**What a verifier needs:** The citation is self-contained — no earlier
citation in the document is required to resolve it. Verification means
confirming the reporter abbreviation exists (see
`connectors/reporters-and-courts.md`), that the court abbreviation matches a
real court, and that the case can be located under that name and citation.

**Hallucination risk:** This is the highest-risk form, because a fabricated
full citation can look completely well-formed — a plausible party-name
pattern, a real reporter abbreviation, and a page number within a plausible
range, none of which make the case real. A citation "looking right" is not
evidence it exists.

### Short-form case citation

**What it looks like:** An abbreviated citation used after a case has already
been cited in full, typically the case name plus a shortened reference to
the reporter and page, e.g. `Party A, 123 F.3d at 462`.

**What a verifier needs:** The preceding full citation for the same case
somewhere earlier in the document. A short form cannot be verified in
isolation — it is only correct if it actually matches an antecedent full
citation for the same case in the same document.

**Hallucination risk:** A short form can silently drift from its antecedent
— citing a different page, or a short form with no matching full citation
anywhere in the document at all (an orphaned short form), which is itself a
sign the full citation was never actually verified or was dropped in
editing.

### Supra citation

**What it looks like:** A citation using "supra" to refer back to a source
cited earlier by name, without repeating the reporter citation, e.g. `Party
A, supra, at 462` or `Smith, Legal Treatise, supra note 4, at 12`.

**What a verifier needs:** The specific earlier citation or footnote the
supra reference points to. A supra reference is meaningless without
resolving exactly which prior citation it targets — this often requires
matching a footnote number or a uniquely identifying short form.

**Hallucination risk:** A supra reference to a footnote or citation number
that does not exist in the document, or that points to the wrong source
once resolved, silently misattributes a proposition to a citation that never
actually supports it.

### Id. citation

**What it looks like:** A citation of `Id.` or `Id. at [page]`, referring to
the same source as the immediately preceding citation.

**What a verifier needs:** The **immediately preceding** citation in the
document — not the most recent citation of that source anywhere in the
draft, but the one immediately before it. An `Id.` is only correct if nothing
else was cited in between.

**Hallucination risk:** `Id.` is the form most vulnerable to silent drift
during editing — inserting, deleting, or reordering a citation elsewhere in
the document can leave a surviving `Id.` pointing to the wrong source without
any visible change to the `Id.` text itself. Every `Id.` must be re-checked
against its immediately preceding citation whenever the surrounding text is
edited.

### Statutory citation

**What it looks like:** A citation to a statute or code section, e.g. a
pattern like `15 U.S.C. § 78j(b)` or a state-code citation, typically title
or chapter, section symbol, and section number.

**What a verifier needs:** Confirmation of the code, title/chapter, and
section number, and — critically — the **version or effective date**, since
statutory text changes over time and a citation with no version marker is
ambiguous about which version of the law is being cited.

**Hallucination risk:** A plausible-looking but non-existent section number,
or a real section number whose current text has been amended since the date
implicitly assumed by the draft. A statutory citation without an "as of"
date is not verifiable as currently stated law without independent research.

### Regulation citation

**What it looks like:** A citation to a codified administrative regulation,
e.g. a pattern like `17 C.F.R. § 240.10b-5`, or a citation to an agency's
Federal Register document by volume and page.

**What a verifier needs:** The same version-date discipline as a statutory
citation, plus confirmation of which agency issued it — regulations are
amended, and a codified regulation citation with no effective-date anchor
cannot be assumed current.

**Hallucination risk:** A fabricated part or section number under a real
title, or a citation to a rule that has since been superseded, withdrawn, or
stayed without the draft acknowledging that possibility.

### Law-journal citation

**What it looks like:** A citation to a law review or journal article, e.g.
a pattern like `Author Name, Article Title, 100 Some L. Rev. 1 (2020)`.

**What a verifier needs:** The author, title, journal volume/abbreviation,
starting page, and year — all self-contained, similar to a full case
citation, but for secondary rather than primary authority. Confirming
existence does not confirm the article actually supports the proposition
cited to it.

**Hallucination risk:** A fabricated author, title, or journal issue that
reads as entirely plausible — law review citations are especially easy to
invent convincingly because there is no small, checkable universe of
reporters or courts to match against, unlike case citations.

### Unknown / partial citation

**What it looks like:** A citation fragment that does not resolve cleanly
into any of the categories above — a case name with no reporter cite, a
section reference with no code identified, a citation copied with a typo, or
a citation abbreviated so heavily that its type cannot be determined from the
text alone.

**What a verifier needs:** More context before any verification step is even
possible. Do not guess at the missing elements or "complete" the citation
from model background knowledge — treat it as an incomplete citation and
flag it for the source to be supplied or the citation corrected.

**Hallucination risk:** The temptation to silently "fill in" a plausible
missing reporter, section number, or year is the single highest-risk moment
in citation handling. An unknown/partial citation must never be completed
from memory; completing it is how a hallucinated citation gets introduced.

---

## Verification Workflow Per Type

| Citation type | Resolves independently? | What must be checked before verification is even possible | Primary hallucination risk |
|---|---|---|---|
| Full case citation | Yes | Reporter and court abbreviation exist (`connectors/reporters-and-courts.md`); case locatable under that name and cite | Entirely fabricated but well-formed citation |
| Short-form case citation | No — needs its antecedent full citation | Locate and match the earlier full citation for the same case | Drift from, or no match to, the antecedent |
| Supra citation | No — needs the specific earlier reference | Locate and match the exact footnote/citation the supra points to | Wrong or missing target reference |
| Id. citation | No — needs the immediately preceding citation | Confirm nothing else was cited in between | Silent drift after document edits |
| Statutory citation | Yes, with a version caveat | Code, section number, and version/effective date | Fabricated section number; stale version |
| Regulation citation | Yes, with a version caveat | Title, part/section, issuing agency, effective date | Superseded, withdrawn, or stayed rule cited as current |
| Law-journal citation | Yes | Author, title, journal/volume, page, year | Fabricated author, title, or issue |
| Unknown / partial | No | Additional source material or correction from the user | Silently "completing" the citation from memory |

---

## Reviewer Notes

- This taxonomy classifies citation *form*. It does not substitute for the
  source-status classification in
  `skills/legal-methodology/source-validation/SKILL.md` or the integrity
  checks in `skills/legal-methodology/citation-integrity-check/SKILL.md` —
  use this file to identify the type first, then apply those skills'
  workflows.
- For existence checks on case-law reporter abbreviations and court names,
  see `connectors/reporters-and-courts.md`. Existence of a reporter or court
  abbreviation is not existence of the case itself — see that connector's
  scope and limits.
- An unresolved short-form, supra, or `Id.` citation (no matching antecedent
  found in the document) is itself a defect to flag — do not assume the
  antecedent existed and was simply omitted from view.
