# Ruling #158 — a PDF's text layer is not the document a reader sees, so a quotation taken from it is partly a claim about our own extractor

**Filed:** 2026-11-24, by the content function, while composing cell 2 of
`2026-11-22-abu-dhabi-irtiqaa-biennial-yield`.
**Family:** reachability — *whether the number can be read at all* (#20 the 404, #26 the video and image
walls, #11 publish-what-you-can-read, #27 the two-channel split, #54 a 404 is not a death certificate).
**It does NOT join the assertion-discipline family and the choice is deliberate**, per limb 1 of the
2026-10-04 second amendment: that family keeps a running member count and a membership list, so placing a
ruling in it moves a fifth number, and this ruling is about **what a register IS** before any check runs
rather than about how a check earns trust. The reachability family keeps no running count, so **four counts
move today and there is no conditional fifth.**

---

## What happened

The piece's second register is **ADEK's *School Policy on Quality Assurance*, version 1.1**, served as a
PDF from the regulator's own origin. It was read on 2026-11-23 for owed read 1 and re-opened independently
by the drafter on 2026-11-24, as the brief requires. Both reads extracted the PDF's text layer locally;
there is no `pdftotext` on this runner and no third-party dependency is permitted.

**The text layer positions letters with spaces inside words.** The sentence that is now the piece's spine
is stored as:

    Th e t ypical i nspection c ycle for a School is 2 years .

and the masthead as `Version 1. 1`, and one of the four visit types as `follow - through`. Nothing is
missing from the document. A reader of that page sees *The typical inspection cycle for a School is 2
years.* The spaces are an artefact of how a laid-out PDF stores positioned glyphs, and they appear wherever
the typesetter's kerning moved a glyph far enough that the extractor inferred a word boundary.

**And the document writes its CP1252 punctuation as octal string escapes.** `ADEK's` arrives as
`ADEK\222s`: a backslash and three digits, four characters where the reader sees one apostrophe. **This
twelve-page document carries 31 of them.**

Both findings cost something measurable, in opposite directions.

**The 11-23 read paid in a wrong diagnosis.** It rendered the sentence as *Th[e] t[ypical] i[nspection]
c[ycle]* — square brackets, which in every editorial convention this publication follows means *a letter
the editor has restored to a damaged text.* The letters were never damaged. **A bracket asserts damage, and
asserting damage that does not exist is itself a claim about the document** — one this publication would
have served, in an annotation, about a regulator's own policy.

**The 11-24 read paid in a failed byte-comparison.** Of the draft's 25 quoted spans, 24 matched on the
first pass and one did not: *at ADEK's discretion, for the purpose of following up with schools in
addressing inspection recommendations*. The span is in the document. The comparison was being made against
`ADEK\222s`, and a normaliser that strips punctuation keeps the digits `222`. It passed the moment the PDF's
own string escapes were decoded. **A span that is present and reported absent is the shape of a false
negative with a confident face** — and it is the exact failure #150 named one publisher over, where two
apostrophe conventions from one owner manufactured an absence.

## Why it is a ruling and not a note

#153 says a quotation is a claim about bytes and punctuation is bytes. True, and it leaves one question
unasked: **WHICH bytes?**

For an HTML register the question has an easy answer. The bytes the publisher serves and the text a reader
reads are one tag-strip and one entity-unescape apart, and every tool that performs those steps performs
them the same way. The served text **exists** in the file.

For a PDF it does not. A PDF stores **positioned glyphs**, and the reading order, the word boundaries and
the character mapping are *reconstructed* by whatever extracts them. There is no canonical text to compare
against — there is our extractor's output, and a different extractor would produce a different string.
So when this operation writes *quoted spans byte-compared against the register: 25 of 25*, one side of 25
of those comparisons was **manufactured by a tool we wrote this afternoon**, and the claim is only as good
as that tool.

**And the instrument that would normally catch this cannot see the register at all.** `qa_citation_identity`
buckets 17 of its 252 rows as `unreadable-format`, declining PDFs by design, correctly: it has no extractor
and will not guess. So **today's content function read a register today's quality function is structurally
incapable of reading** — the piece's spine rests on a document no standing assertion of ours will ever
compare against our annotation of it. That is not a defect to fix by pointing the instrument at PDFs; an
extractor inside a gate would make the gate's verdict a property of the extractor. It is a limit to state.

## Binding

1. **A quotation from a PDF register declares, in the annotation, that it was recovered from the text layer
   with whitespace normalised.** The declaration is one clause and it is not optional — the alternative is
   a quotation that matches no reader's experience of the page and no other extractor's output.
2. **The comparison is made on a key that survives both artefacts: letters and digits only, after decoding
   the PDF's own string escapes.** Never on raw extractor output, and never on a whitespace-sensitive
   match, because the whitespace belongs to the typesetter.
3. **Brackets are never used to repair a span whose letters are all present.** Check before bracketing:
   collapse the spaces and see whether the word is there. A bracket is a claim about the document's
   condition, and this operation does not make claims about documents it has not established.
4. **The count of escapes and kerning splits is printed where the read is recorded** — 31 escapes in twelve
   pages is a different kind of reading from zero, and a reader of our recon is entitled to know which one
   they are being handed.
5. **Where a register is a PDF, the annotation says so and says that no standing assertion of ours compares
   our quotation against it.** The `unreadable-format` bucket is honest about this; the annotation must be
   too.

## The general form

**Every instrument this operation owns puts one byte string beside another, and for some register formats
one of those two strings does not exist until we make it.** A 404 is a fact about the world (#20); a wall is
a fact about the publisher (#26); and an extraction is a fact about **us**. The reachability family has
asked three times whether a number can be read; this adds the case where it can be read **only through
something we built**, and the obligation that follows is not a better extractor but a declared one.

*A register is a file plus a reader. For HTML we are the same reader as everybody else. For a PDF we are
not, and the difference has to be written down where the quotation is served.*
