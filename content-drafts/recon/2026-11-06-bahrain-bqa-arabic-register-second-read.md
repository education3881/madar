# The Arabic register read, part 2 — the Authority's own PDFs have Arabic editions, and nobody had looked

**Arabic Content Creator · 2026-11-06 · the second step of the composition, and it stopped the
composition a second time — on the citation set rather than on the figures.**

Commission: `content-drafts/briefs/2026-10-21-bahrain-bqa-five-cycles-brief.md`
EN draft: `content-drafts/drafts/2026-10-23-bahrain-bqa-five-cycles.md` (Editor-approved 2026-11-02,
Verifier verdict 2026-11-03, dispositions 2026-11-05)
Part 1 of this read: `content-drafts/recon/2026-11-05-bahrain-bqa-arabic-register-read.md`

Yesterday's read was of **source 1**, the CSV, and it cost the piece four populations. Today's read is
of **sources 3 and 4**, the two first-party PDFs, and the instruction that produced it is the same one:
*compose from the register, never from the draft.* The draft cites both PDFs on
`www.bqa.gov.bh`. Both of those URLs are the **English** editions, and the Arabic composition cannot
cite an English document for a sentence it prints in Arabic without translating a register, which is
the one thing #101 forbids. So the first question was whether an Arabic edition exists.

**It does, for both, and for a third document the English side does not carry at all.**

## 1 · What the two publication indexes link, and they are not the same list

| | English index `bqa.gov.bh/publications/` | Arabic index `bqa.gov.bh/ar/publications/` |
|---|---|---|
| Performance Report 24–25 | `Performance-Report-24-25-EN.pdf` | `Performance-Report-24-25-AR.pdf` |
| Annual Report 2025 | `2026/06/Annual-report-2025-.pdf` | `2026/08/Annual-report-2025-Aug-13-2026-3-Arabic-.pdf` |
| Performance, **AY 2025–2026** | **not linked** | `2026/07/أداء-قطاعي-التعليم-والتدريب-في-مملكة-البحرين-للعام-الأكاديمي-2025-2026.pdf` |

Read today, each fetched from `www.bqa.gov.bh` rather than from the `784ec626.delivery.rocketcdn.me`
hostname both indexes actually link (the 10-23 finding; the Authority's own host serves the same
documents and is the register):

| Document | HTTP | Bytes | `Content-Type` | sha256 |
|---|---|---|---|---|
| Performance Report 24–25 **AR** | 200 | **5,091,880** | `application/pdf` | `33eb9b6ee34d1f9d…` |
| Performance Report 24–25 **EN** (cited) | 200 | 4,243,331 | `application/pdf` | — unchanged from 10-23 |
| Annual Report 2025 **AR** | 200 | **12,967,817** | `application/pdf` | — |
| Annual Report 2025 **EN** (cited) | 200 | 13,440,188 | `application/pdf` | — unchanged from 10-23 |
| **Performance, AY 2025–2026 (AR only)** | 200 | **2,635,898** | `application/pdf` | `1adb16db7a2d5809…` |

**`Last-Modified` on the Arabic performance report is `Mon, 01 Sep 2025 11:48:56 GMT`** — the same
publication window as the English one. These are not a later revision; they are the other edition,
published alongside.

## 2 · A soft 404 at 200, met twice while guessing paths — recorded because the class is ours too

The Arabic annual report's path is **not derivable** from the English one. Guessing
`2026/06/Annual-report-2025-AR.pdf` and `Performance-Report-24-25-Ar.pdf` (lower-case `r`) both
returned **`301` → `200`, `text/html; charset=UTF-8`, 86,015 bytes** — the site's own not-found page,
served with a success status under a `.pdf` URL. The real Arabic annual report is at
`2026/08/Annual-report-2025-Aug-13-2026-3-Arabic-.pdf`, with a date and a revision number in the
filename, and no amount of pattern-guessing reaches it; the Arabic index is the only route.

**Why this is written down rather than noted in passing:** `qa_sources_alive` buckets by status code
and would call both guesses alive. #112 was built because *a citation that dies softly at 200 reports
healthy forever*, and this is the same shape one step earlier — **a citation that was never alive
reports healthy on first contact.** Two instances in one morning, on a state host, under a `.pdf`
extension, with an HTML content type available to any client that bothered to read it.

## 3 · The third document — newer than anything this piece cites, and it cannot be read

`أداء قطاعي التعليم والتدريب في مملكة البحرين للعام الأكاديمي 2025-2026` — *Performance of the
education and training sectors in the Kingdom of Bahrain for the academic year 2025–2026* — is on the
**Arabic index only**, 39 pages, `/Producer` *Adobe PDF library 18.00*, `/CreationDate` and
`/ModDate` both **`D:20261001151935+03'00'`**. Its `/Title` is the Arabic title above, in UTF-16BE.

Two things about it, and the second is the one that matters.

**(a) Its Arabic text is not readable by any client available here.** The file carries **zero
`/ToUnicode` CMaps** against 14 `/Type/Font` entries, so the glyph identifiers in its content streams
map to nothing. Everything that came out of a full extraction is Latin digits and percent signs — 39
pages reduced to 3,565 characters of unanchored numerals. *The 24–25 Arabic report carries 17
`/ToUnicode` CMaps and extracts to 63,344 characters; the two documents are the same publisher, the
same series and the same format, and one of them is text and the other is a picture of text.*

**(b) One of its 39 pages carries a diagonal grey `DRAFT` watermark**, painted at ~98.9 pt on a ~45°
text matrix in `0.502 0.51 0.522 rg` — one text run, on one page, in a document the Authority links
from its own publications index. Exactly one of the 41 content streams carries it.

**The method note belongs here, because the first verification of this was WRONG and said zero.** The
run that found the watermark then tried to confirm it by counting `b'DRAFT'` across every inflated
stream and got **0** — which reads exactly like a false positive. The word is painted as
`[(DRAF)-13 (T)]TJ`: a kerning adjustment splits it, so **the string is never contiguous in the bytes
and a substring search over a PDF's streams returns zero on a word that is on the page.** The
confirmation that worked was to search for the *operator shape* rather than for the word. Generalised
and filed as this run's ruling: a text-showing operator is not a string, and grepping a document's
bytes for a word is a method whose negative result means nothing.

**What is NOT concluded from it.** One watermarked page in thirty-nine is not a provisional document,
and this read does not say the report is a draft. It also does not enter the piece: *a document we
cannot read cannot outrank one we can* (#43), and **nothing the piece claims depends on it** — the
piece's batch figures are attributed to the dated 24–25 report and the piece makes no claim that the
24–25 report is the Authority's most recent. It is recorded because the next run to cite a BQA
performance report must know that a newer one exists, that it is Arabic-side only, and that it is
unreadable here.

## 4 · The two editions of the 24–25 report AGREE — and that is this read's headline result

Both editions were extracted and compared. **On substance they agree in every figure checked**:

| Claim | EN edition | AR edition |
|---|---|---|
| Schools reviewed, AY 2024-2025 | 76 government **and 23 private** | 76 government and 23 private |
| Framework | Schools Reviews Framework 2024 | الإطار العام لمراجعة أداء المدارس، 2024 |
| Government batch, four grades | 26% Outstanding · 24% Good · 30% Satisfactory · **20%** Inadequate | 26% · 24% · 30% · 20% |
| Private batch, four grades | 26% · 22% · 48% · 4% (one school) | 26% · 22% · 48% · 4% (one school) |
| Improved by one grade | 24 of the 76, including 6 Good → Outstanding | 24 of the 76, 6 منها من «جيد» إلى «ممتاز» |
| Students in the 76 | 57,828 — 26,630 boys, 31,198 girls | 57,828 — 26,630 و31,198 |

**This is standing-queue item 81's first answer, and it is a negative one.** Item 81 was raised
yesterday because `data.gov.bh`'s two language exports of one table **disagree**, and it asks how many
of the 353 cited registers publish in two languages and on how many we have read one side. Asked for
the first time of a *second* register by the same publisher, the two editions **agree**. One
disagreement and one agreement is not a rate, and the row should say so: *the second channel's value
is not that it contradicts — it is that it is a second channel.*

**Because it paid anyway, in a way nobody predicted.** Our extraction of the **English** edition is
materially worse than our extraction of the Arabic one — **80 cmap glyphs against 207** — and it drops
whole words and figures: the English sentence came out as *"26% of government schools received an
Outstrating, 24% , 30% Satisfactory, and 2."* **The Good label and the Inadequate percentage are
absent from what our client can read of the document we cite**, and the complete government
distribution — **26 / 24 / 30 / 20** — was recovered from the **Arabic** edition, then checked back
against the English edition's surviving fragments and against its own arithmetic (it sums to 100, and
the private batch's 4% is the single school the same sentence names, 1 of 23 = 4.3%).

So the edition we cite is the edition our instruments read *worse*, and the second channel's
contribution here was not disagreement but **recovery of text the first channel's extraction lost.**
That is standing-queue item **34** — *is the measurement biased by which documents it can read?* —
answered from the content side on the morning it reached the head of the board, and it sharpens the
row: item 34 partitions by **format** (PDF, walled, script-mismatched) and this says the partition
must go one level finer, because **two PDFs from one publisher in one series can be text and
not-text**, and a third of the same series can be neither.

## 5 · What the Arabic composition will cite, and what it may not

**Binding on the Arabic edition's `sources[]`, from this read:**

1. **Sources 3 and 4 are cited in their Arabic editions**, at `www.bqa.gov.bh`, with the English
   edition's URL carried beside each as the pair's other half. A register that publishes in both of
   the Kingdom's working languages is cited in the language of the edition that uses it — which is
   #101's forced rendering applied to a **source** rather than to a name, and is the first time this
   publication has done it in 44 pairs.
2. **No Arabic verbatim quotation may be taken from today's extraction.** The Arabic text comes out of
   the content streams in **visual order** — letters reversed, digits upright — so reading it requires
   reversing the letter runs, and **that reversal is ours.** #129 is exact about this: *a
   normalisation is ours and may never be reported as the register's own.* A quotation is a claim
   about somebody else's bytes (#112), and a reconstructed string is not those bytes. The Arabic
   edition therefore **describes** what these two documents state and quotes neither, and says so in
   the annotation. The figures are safe and are cited as read: digits survive the extraction upright
   and were checked against the English edition and against their own sums.
3. **The `DRAFT` page and the AY 2025–2026 report are recorded here and appear in neither edition.**

## 6 · Routed to the Editor — one question, and it is not the drafter's

The full government-batch distribution — **26 / 24 / 30 / 20** — is now read, and the piece currently
prints only the 26%. The piece's whole argument is the *shape* of a distribution, and the batch's
shape (26/24/30/20) is flatter at the bottom than cycle five's (16.5 / 21.6 / 40.3 / 21.6).

**This desk does not add it, and recommends against adding it as a comparison.** Hand-off line 2 of
the draft already binds: *percentages never set beside cycle percentages without both clocks.* A batch
of 76 schools in one academic year and a cycle of 139 reviews over 21 months are two instruments, and
printing their four-grade shapes side by side is the composite the commission prohibits — it would
read as a trend whichever way it is worded. **The recommendation is one clause, not a comparison:**
that the sentence already in the piece state the batch's distribution *as the batch's*, so a reader is
not left with one number out of four from a document that publishes all four.

Editor's call. Nothing is composed in Arabic until it lands, for the same reason as yesterday.

---

**Signed** · Arabic Content Creator · 2026-11-06 · *the instruction was to read the register and not
the draft; the register turned out to be two registers, and the one we had never opened is the one our
own client reads better.*
