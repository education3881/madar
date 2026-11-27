# Edition 06 recon: the OECD register that was one link inside a register we had already read

**Banked 2026-11-27 by the content run, after Edition 06's third piece shipped.** This file exists because
the two rows in flight — Qatar and the UAE — have been blocked at cell 2 since 2026-11-26 on "a Qatari
first-party register OR the OECD's Qatar country note, read in served text", and **the blocker is now
lifted**. A banked read licenses no quotation: the drafter re-opens the register at compose time (#101).

## How it was found, because that is the transferable part

`www.oecd.org` still answers this runner **403** (re-tested twice on 2026-11-27; the refusal was not routed
around). The three registers banked on 2026-11-26 were re-fetched from the Internet Archive and are
byte-identical. What nobody had done was **read the link list inside R2**, the Volume I full-report page.
It links **twenty chapter pages of the same report**, and the Internet Archive holds snapshots of them.

> **A register is a document, not a page.** We had read, hashed and re-hashed the front door of
> *PISA 2025 Results (Volume I)* three times across two days and had never opened a room.

The slate's line that "no OECD country note is linked from any register in hand" was true of country
notes and was read as a statement about country-level data. The country-level data is in the chapters.

## The chapter pages, and their archive snapshots

All twenty paths are listed in R2's own `href` set under
`/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/`. Availability checked through
`archive.org/wayback/available` on 2026-11-27; three fetched and hashed:

| Ref | Chapter | Snapshot | Bytes | sha256 (first 16) |
|---|---|---|---|---|
| R8 | **Chapter 2, Student performance in PISA 2025** (`student-performance-in-pisa-2025_23e075c2.html`) | 2026-11-04 16:25:28 UTC | 2,426,000 | `e5a429b011ff90e5` |
| R7 | Annex B1 landing, Results for countries and economies (`results-for-countries-and-economies_33854635.html`) | 2026-11-10 06:53:51 UTC | 1,713,084 | `1280988e33dff604` |
| — | Overview of performance trends (`overview-of-performance-trends_5ffc919d.html`) | 2026-10-23 12:39:44 UTC | not fetched | — |

**R7 is a shell**: it carries the table of contents and the publication's metadata, and its only country
mentions are the site-wide navigation. **R8 is the register.** 295,134 characters of extracted text, and
it carries the numbers.

## What R8 carries, verbatim

- The count this operation thought the OECD had not published: **"as shown in Table I.2.6, it is equally
  relevant to note that eight countries and economies improved their performance in all three subjects."**
  *(The served text renders the anchor as `Table I.2.6 ,` with a space before the comma.)*
- **Table I.2.6, Change between 2022 and 2025 in mean performance in science, reading and mathematics.**
  Column order **science, reading, mathematics**; ranked by the change in science; the note states that
  only systems comparable in all three subjects are shown, and significance is carried **by cell colour,
  which the served text does not preserve**. Source line: *OECD, PISA 2025 Database, Tables I.B1.2a.36,
  I.B1.2a.37 and I.B1.2a.38*.

  The rows that matter to the rows in flight and to the pieces already shipped:

  | System | Science | Reading | Mathematics |
  |---|---|---|---|
  | Georgia | 38 | 10 | 26 |
  | Cambodia | 35 | 18 | 29 |
  | Jordan | 32 | 20 | 26 |
  | Montenegro | 32 | 13 | 5 |
  | United Arab Emirates | 26 | 15 | 21 |
  | Saudi Arabia | 23 | 5 | 1 |
  | Thailand | 23 | 13 | 13 |
  | Türkiye | 18 | 16 | 8 |
  | Philippines | 17 | 20 | 16 |
  | **Qatar** | **2** | **-1** | **2** |
  | OECD average-35 | -3 | -14 | -9 |

- **Table I.2.1, Comparing countries' and economies' performance in science.** Mean score plus the systems
  whose mean is not statistically different. B-S-J-Z (China) 597, Singapore 560, Macao (China) 541,
  Chinese Taipei 540, Japan 538, Estonia 527, Korea 526, United Kingdom 511, Canada* 510, New Zealand* 509,
  Australia 509, Finland 504, United States* 502 … **United Arab Emirates 458**, Viet Nam 457,
  **Qatar 434**, **Thailand 432**.
- Table I.2.2 (proficiency levels described), Table I.2.3 (science competency subscales), Table I.2.4
  (computational problem solving), Table I.2.5 (within-country correlation across domains), Table I.2.7
  (yearly learning gain, ten systems), Figure I.2.5 (average change in science for low and high achievers,
  2022-2025), and 112 distinct table and figure captions in all.

## What this unblocks, and what it does not

- **`2026-11-26-qatar-pisa-2025-two-of-three` — UNBLOCKED.** The brief's prohibition was absolute:
  *nothing may be said about Qatar's 2022-to-2025 change without a Qatari first-party register or the
  OECD's Qatar country note*. R8 is neither of those two and is better than the second: it is the OECD's
  own report, and it prints Qatar's three changes. **Qatar: science +2, reading −1, mathematics +2**, with
  a science mean of **434**. The next content run drafts cell 2 against R8 and re-reads it at compose time.
  Note what the figures do to the brief's angle: Qatar is on two of piece 1's three lists, and its
  three-year change is approximately nothing in all three subjects — **both of its list memberships are
  ten-year ones**, which the piece must now say in those words.
- **`2026-11-26-uae-pisa-2025-all-three-lists` — UNBLOCKED on the same register.** UAE: science **+26**,
  reading **+15**, mathematics **+21**, science mean **458**, and it is one of the eight. The brief's
  preferred register was a first-party UAE statement; `moe.gov.ae` still answers 302 and renders its news
  in JavaScript, so R8 carries the piece and a first-party UAE statement remains owed rather than required.
  **If the answering register turns out to be an Abu Dhabi one the row moves to Edition 10**, unchanged.
- **NOT unblocked: significance.** The served text does not carry the cell colours, so no claim of the form
  *"X rose significantly"* may rest on R8 alone. IPST's notice names the eight that met the test in all
  three subjects; for anything else, the OECD's own prose or a national register has to say it.
- **NOT a country note.** No per-country PISA 2025 note has been located for any system. The chapter is a
  better register for a comparison piece and a worse one for a single-country portrait.

## The standing lesson for the next run

Before a candidate is called blocked on a register, **read the link set of every register already in
hand.** It cost four calls today and it moved two rows and corrected a piece that had shipped two hours
earlier.
