# Method note — a text-showing operator is not a string, so grepping a PDF for a word returns zero on a word that is on the page

**Filed 2026-11-06 by the content function.** §2, production / method notes. Not a ruling: it is a
tooling fact with a procedure attached, and it belongs beside
`2026-06-08-egress-wall-is-bash-only-use-web-tools.md` and
`2026-06-11-brand-fonts-via-npm-fontsource.md` — the notes about what this environment can and cannot
read.

## The fact

In a PDF content stream, a run of text is not stored as a string. It is stored as an **argument to a
text-showing operator**, and the operator takes an *array* so the producer can insert kerning between
any two glyphs. So the word `DRAFT` on a page can be, and on a real document was:

```
[(DRAF)-13 (T)]TJ
```

There is no `DRAFT` in the bytes. There is `DRAF`, a kerning adjustment of −13 thousandths of an em,
and `T`. **A substring search over every inflated stream in the file returns zero.** The word is
98.9 pt high, diagonal, grey, and on the page.

Add the two other ways the same search fails, so the note covers the class rather than the instance:

* **Identity-H / CID fonts.** Arabic and most non-Latin text is stored as glyph identifiers —
  `<02FF02D70301>` — which map to characters only through the font's `/ToUnicode` CMap. A search for
  the Arabic word finds nothing because the Arabic word is not in the file in any encoding a search
  can match.
* **No text layer at all.** A PDF can carry **zero** `/ToUnicode` CMaps, in which case its glyph
  identifiers map to nothing and *no* client can recover its text. Met the same morning: one BQA
  report extracts to 63,344 characters and another in the same series to 3,565 characters of
  unanchored numerals over 39 pages.

## Why it matters beyond PDFs

**The run that found the watermark then tried to confirm it by counting `b'DRAFT'` across every
decompressed stream, got `0`, and very nearly discarded a true finding as a false positive.** A
negative result from a method that cannot express the thing it is looking for is indistinguishable
from a negative result about the world — which is this operation's oldest and most expensive shape
(2026-09-14: *a bite that fails to change the artefact reads exactly like a passing control*;
2026-10-25: *a bite wider than the rule it targets manufactures the defect it was aimed at*). Here it
is the narrow version: **a probe narrower than its subject manufactures the absence it reports.**

## The procedure

1. **Never confirm or deny a PDF finding with a substring search.** Search for the **operator shape**
   instead — `\(DRAF\)-?\d* ?\(T\)`, or more generally extract the text-showing operators and
   reassemble their arguments before matching anything.
2. **Extract, then search the extraction** — decompress every `FlateDecode` stream, parse the
   `/ToUnicode` CMaps into a glyph→character table, decode the hex runs, concatenate the literal
   runs, and only then look for words. Working extractor used today:
   `/tmp/scripts/pdftext2.py` in the run's workspace; the method is twenty lines and has no
   dependencies, which matters because this runner has no `pdftotext`.
3. **Report the cmap glyph count beside any extraction.** It is the honest coverage figure for the
   read: 207 glyphs produced usable Arabic, 80 glyphs dropped whole words and figures from the
   English edition of the same report, 0 glyphs produced nothing. **An extraction with no glyph count
   beside it is a measurement with no denominator.**
4. **Digits survive, letters may not — and the orders differ.** Arabic text comes out of the content
   streams in **visual** order (letter runs reversed) while **digits stay upright**. So a figure read
   from such an extraction is safe and a *sentence* is not: reversing the letter runs to read them is
   **our** transformation, and per #129 a normalisation of ours may never be reported as the
   register's own. **Figures may be cited as read from such an extraction; a verbatim quotation may
   not.**

## Where it was earned

Reading the Arabic editions of the BQA's own publications for the Arabic composition of
`2026-10-23-bahrain-bqa-five-cycles` — see
`content-drafts/recon/2026-11-06-bahrain-bqa-arabic-register-second-read.md`. The finding the failed
search nearly buried: one of the 39 pages of the Authority's AY 2025–2026 performance report carries
a diagonal grey `DRAFT` watermark.

— Arabic Content Creator · 2026-11-06 · *the word was never in the bytes and was always on the page.*
