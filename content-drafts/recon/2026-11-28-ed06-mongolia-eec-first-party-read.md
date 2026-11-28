# Edition 06, piece 7 — Mongolia. The door walked, the register read, and the figures parsed

**Run 2026-11-28 by the evening content run, executing step 1 of
`content-drafts/recon/2026-11-28-ed06-seventh-piece-door-test.md` verbatim: *walk `eec.mn`'s link set.***

The door test left three instructions in order. The first was walked and it returned a piece. The second
(`kemendikdasmen.go.id`) and third (the edition stops at six) were not reached and are not needed today.

## 1. What `eec.mn` actually serves, and where

`eec.mn` is the **Боловсролын үнэлгээний төв** — the Education Evaluation Centre, Mongolia's national
assessment body and the organisation that runs PISA for Mongolia. All readings below are direct from this
cloud runner, 2026-11-28, no archive in the loop except where the row says so.

| Object | Result | Bytes | What it is |
|---|---|---|---|
| `https://eec.mn/` | **200** | **574,233** | **The register.** `https://www.eec.mn/` serves the same byte count |
| `https://eec.mn/pages/-olonulsiinunelgee` | 200 | 15,729 | **290 characters of text.** The PISA page's own URL is an empty shell |
| `https://eec.mn/news` | 200 | 17,044 | 344 characters of text. Shell |
| `https://eec.mn/publications` | 200 | 18,101 | 445 characters of text. Shell |
| `https://eec.mn/news/cmwyq21zw00596204k81jljfo` | 200 | 21,404 | 291 characters. Content fetched client-side (`ClientPageRoot` in the flight payload). Shell |
| `https://moe.gov.mn/` | **200** | 103,152 | **552 characters of text. A wall** (#26). Not tested by the door test, which tried `mecs.gov.mn` and `esis.edu.mn` |
| `https://moe.gov.mn/feed` | 200 | **28** | `serice under construction` — the ministry's RSS, misspelling and all |
| `https://unelgee.eec.mn/` | 200 | 2,960 | subdomain, no PISA |
| `https://bi.eec.mn` | 522 | 16 | Cloudflare origin timeout |
| `https://chadla.eec.mn` | 200 | 12,724 | answers 200 to any path; a catch-all, not a file store |

**THE FINDING THAT MADE THE WALK WORK, AND IT INVERTS RULING #26.** The door test recorded that `eec.mn`
*"extracts to 5,370 characters of real served Mongolian text, so it is not a wall"* and that its *"front
page carries no `pisa`"*. **Both halves were measured correctly and both are misleading**, because this
site puts the text in a place neither measurement looks: the root document carries **ten
`data-advanced-source` attributes**, each a URL-encoded JSON object holding one page's complete `html`
and `css`. Decoded, they run 7,096 to 29,747 characters. The string `pisa` occurs **283 times in the root
document and 0 times in its extracted text** — because every occurrence is inside a percent-encoded
attribute.

So the shape is the exact inverse of #26's wall: **a page's own URL serves a shell and the site root
serves that page's full text.** #26 says a figure rendered at runtime is not citable. Here nothing is
rendered at runtime — the bytes are served, they are simply served from the wrong URL. **The citable
object is `https://eec.mn/`, and a citation pointing at `https://eec.mn/pages/-olonulsiinunelgee` would
be a citation to 290 characters of chrome.** Any piece built on this register cites the root and says
why.

*Method, so nobody pays for it twice: `href` sweep of the root → 27 absolute URLs; then
`re.findall(r'data-advanced-source="([^"]+)"')` → 10 blocks; `urllib.parse.unquote` each; strip tags.
Block 0 is the PISA page, 29,747 characters decoded, 15,722 characters of text.*

## 2. What Mongolia says about itself, in Mongolian, in served text

All of this is block 0 of the root document — the page the register titles *PISA ҮНЭЛГЭЭНИЙ ТУХАЙ* under
the kicker *OECD · Олон улсын үнэлгээ*.

- **Mongolia has sat PISA twice.** *"Монгол Улс 2022 онд анх удаа PISA үнэлгээнд амжилттай хамрагдаж"* —
  in 2022 Mongolia took part for the first time — with **7,276** fifteen-year-olds.
- **PISA 2025: 191 schools and 7,146 students.** *"Монгол Улсын хэмжээнд түүврээр сонгогдсон 191
  сургуулийн 7146 сурагч хамрагдсан."* The register's own stat tiles repeat **191** and **7146** beside
  **91 улс** (91 countries) and **760,000+ суралцагч**.
- **The law is the reason, and it names the interval.** *"Боловсролын ерөнхий хуулийн 35.6-р зүйлд
  'Боловсролын чанарыг гурван жил тутам олон улсын эрх бүхий байгууллагаар үнэлүүлнэ' гэж заасны дагуу"* —
  General Education Law article 35.6: education quality is to be assessed every three years by an
  authorised international body. **Mongolia's participation is a statutory obligation, not a decision taken
  cycle by cycle.**
- **What Mongolia added this cycle.** 2022 ran the student and school-principal questionnaires only; 2025
  added the student ICT-use questionnaire, a **science teacher** questionnaire answered by **1,331**
  teachers, and a **parent** questionnaire. The register sets the two lists side by side in a table.
- **The major domain switched between Mongolia's two cycles.** The register's own cycle table: **PISA 2022
  — major Mathematics**, minor science and reading; **PISA 2025 — major Science**, minor reading and
  mathematics. Fourth domains: 2022 creative thinking, 2025 *Цахим орчинд суралцахуй* (learning in the
  digital world).
- **The cycle becomes four-yearly from 2029.** *"Энэхүү үнэлгээ нь 2029 оноос эхлэн 4 жилийн циклээр
  зохион байгуулагдана."*
- **The timeline, printed as four steps:** 2022 first participation · 2024 field trial · **2025.03–05**
  main study · **2026.09 Үндэсний үр дүн** — the national results presented to the public.

## 3. The thing the register says exists and does not serve

Block 0 carries two links to Mongolia's own reports, by name, as buttons:

| Linked by the register as | URL | Result |
|---|---|---|
| **ПИСА-2025 Үндэсний тайлан** (PISA 2025 National Report) | `www.eec.mn/wp-content/uploads/2026/09/PISA-2025-үндэсний-тайлан.pdf` | **404**, 8,388 bytes of HTML |
| ПИСА-2022 Үндэсний тайлан | `eec.mn/wp-content/uploads/2024/11/ПИСА-2022-тайлан.pdf` | **404**, 8,388 bytes of HTML |

Tested on `https://www.eec.mn`, `https://eec.mn` and `http://eec.mn`, and on `chadla.eec.mn`,
`unelgee.eec.mn` and `bi.eec.mn`. Percent-encoded both ways — with the precomposed `ү` (U+04AF) and with
the decomposed `у`+U+0308 — because a Cyrillic path is exactly where an encoding error would fake a 404.
Both forms return the same 404. **The Internet Archive holds no snapshot of either file**
(`archive.org/wayback/available` returns `"archived_snapshots": {}` for both).

The cause is visible in the paths: `wp-content/uploads/…` is a WordPress tree, and this register is now a
Next.js application. **The site was rebuilt and the uploads did not come with it, so the register's own
PISA page links its own national report into a tree that no longer exists.** That is a statement about a
file move, not about Mongolia's willingness to publish — the register says in writing that the report was
presented in September 2026, and the operation has no basis to doubt it.

**So Mongolia is the exact counter-case to this edition's Uruguay piece.** Uruguay's own account of its own
results was fetched, hashed and reproduced. Mongolia's own account is **named by its author, dated, linked,
and not served.**

## 4. The named human, and the honest provenance

The **live** register names no person anywhere in its ten decoded pages: no director, no coordinator, no
author. `/pages/` has no about-us route and the rebuilt site has no leadership page.

The archive holds the page the rebuild deleted. Capture **`20260417030826`** of
`https://www.eec.mn/zakhirlin-mendchilgee` (110,004 bytes) opens:

> **Боловсролын үнэлгээний төвийн захирал Э.Цэрэнцоодол**

— *E. Tserentsoodol, Director of the Education Evaluation Centre*, over a signed greeting setting out the
centre's short, medium and long-term aims, in which **PISA-2022 is named in the short-term list**. That
page is **404 on the live site**. It is the newest first-party naming of the post available: the newest
capture of that page is this one, and the newest capture of the root (`20260901180306`, 26,787 bytes)
names nobody and carries no `PISA`. The organisational-structure page (capture `20260418073354`) lists
**four departments and not one person**.

**What may therefore be written, and nothing beyond it:** that the body answering for Mongolia's PISA
figures is the Education Evaluation Centre; that the last time the centre's own register named the person
at its head, on 17 April 2026, it was Э.Цэрэнцоодол; and that the register as rebuilt names no one. **A
claim that he holds the post today is NOT supported** and must not appear. He says nothing about PISA 2025
and must not be made to.

## 5. The OECD side — hash reproduced, nine tables, one absence

Chapter 2 re-fetched from the capture the source index declares
(`agents/guidebook/2026-11-27-oecd-pisa-2025-volume-i-chapter-2-source-index.md`, capture
**`20261104162528`**). `curl` with no `--compressed` returns the **279,017-byte** raw gzip; decompressed it
is **2,426,000 bytes**, sha256 **`e5a429b011ff90e5676417dda3cf5358b2f72b940ee068fae3faa96a6f068a71`** —
**the declared hash, reproduced for the fifth independent time.** The index's warning earned its place:
three different byte counts belong to three different objects of one capture, and only the decompressed
one is the document the OECD served.

**The #162 sweep, run as the ruling requires.** Every cell reading `Mongolia` across all fourteen numbered
tables: **29 occurrences, nine tables — I.2.1, I.2.3, I.2.4, I.2.6, I.2.8, I.2.10, I.2.11, I.2.12,
I.2.13** — plus seven in running prose. **Mongolia has no row in I.2.9.**

| Table | Mongolia | OECD average-35 in the same table |
|---|---|---|
| I.2.1 science mean | **424**; not statistically different from Serbia, Romania, Costa Rica, Georgia, Moldova, Bulgaria, Kazakhstan, Malaysia | the table prints no numeric average (the Qatar verdict's repair 5) |
| I.2.3 science + subscales | 424 · 425 · 421 · 421 | 482 |
| I.2.4 computational problem solving | **443**; not different from Israel, Romania, Serbia, Albania\*, Peru | — |
| **I.2.6 change 2022→2025** | **science +12 · reading −4 · mathematics −6** | **−3 · −14 · −9** |
| I.2.8 low / top performers | **−6.6** pp · **+0.1** pp | +1.2 · −0.3 |
| **I.2.9 decennial trend** | **ABSENT** | −7 · −27 · −24 |
| **I.2.10 socio-economic gap** | **disadvantaged +19 · advantaged +8 · gap −11** | **+5 · −8 · −13** |
| I.2.11 low/top by SES quarter | −11.4 · −2.2 · 0.0 · +0.4 | −0.7 · +1.6 · +0.5 · −2.3 (Poland row shown for shape) |
| **I.2.12 change by gender** | **girls +16 · boys +7 · gap (boys − girls) −9** | −2 · −3 · −1 |
| I.2.13 low/top by gender | −8.7 · −4.3 · +0.2 · 0.0 | +1.0 · +1.4 · −0.2 · −0.4 |

### Why Mongolia cannot be in I.2.9, read off the table's own note

I.2.9's note, verbatim and **fuller than this operation has previously quoted it**:

> *"Only countries and economies that can compare results in all three subjects in PISA 2025 and at least
> two previous assessments among PISA 2015, PISA 2018 and PISA 2022 are shown. The average decennial trend
> is the average change, per 10-year period, between PISA 2015 and PISA 2025, calculated by a linear
> regression. The average decennial trend is only computed for countries with comparable data in at least
> three PISA assessments over the period considered."*

Mongolia's first PISA was 2022. **It has one previous assessment among the three named, and two
assessments in total.** The note asks for two previous and the trend asks for three in total. **Mongolia
fails both conditions, and the register states both.** This is a deduction from two served statements —
the table's note and the centre's own *анх удаа* — and must be presented as this publication's deduction
with both operands named, never as something the OECD says about Mongolia.

### The derived counts, computed from the parsed tables and attributable to nobody but us

**I.2.6** — 75 entries, **74 systems** plus the `OECD average-35` row. Ranked by the table's own note *"in
descending order of the change in science performance"*.
- **Science rose in 30 of the 74.** All three subjects rose in **12**.
- **Science rose while reading AND mathematics both fell in 13**, and **Mongolia's +12 is the largest of
  the 13**; Uruguay's +9 is next, then Austria, Brazil and Italy at +6.
- **11 systems rose further than Mongolia in science and 3 sit at exactly +12** — the United Kingdom,
  Mongolia and El Salvador. **So no ordinal is written for Mongolia**: a rank inside a tie is a statement
  about sort order, not about a country (axis #24).
- Mongolia's three figures are each better than the `OECD average-35` row's, **and two of the three are
  falls.** 29 of the 74 beat the average row on all three.

**I.2.10** — 74 entries, **73 systems** plus the average row.
- **The gap narrowed in 49 of the 73.** Of those 49, **34 narrowed with the advantaged column falling** —
  the pattern the `OECD average-35` row itself shows, +5 / −8 / **−13** — and **15 narrowed with both ends
  rising.**
- **Mongolia is one of the 15**, with the others: Georgia, the United Arab Emirates, Montenegro, Jordan,
  the Slovak Republic, Thailand, New Zealand\*, North Macedonia, Uruguay, the United Kingdom, Bulgaria,
  Italy, Chile and Romania.
- Mongolia is **12th of 73** on the disadvantaged column, where no tie exists at +19 — but the figure
  carries more than the rank: Uzbekistan's +85 and Georgia's +55 are of another order.

### The prose that names Mongolia, quoted because it is where the chapter hedges

1. *"The widest gaps in science performance in favour of girls (about 20 score points or more) were
   observed in North Macedonia, Jordan, Slovenia, Finland, Mongolia, Bulgaria, the Kurdistan Region (Iraq)
   and the Palestinian Authority, (in ascending order)"* — the stray comma before *(in ascending order)* is
   the register's.
2. *"the gender gap widened in Mongolia, mainly driven by an increase in mean performance among girls (by
   16 score points) while boys' performance remained more stable."* **The chapter's own hedge is
   *more stable* for a boys' figure of +7**, and the house rule requires that hedge in any sentence that
   uses it.
3. *"Croatia, Jordan, Bulgaria, Mongolia and the Palestinian Authority (in ascending order) where the share
   of boys who did not attain proficiency Level 2 is larger than the corresponding share of girls by
   between 10 and 16 percentage points."*

**The standing limit of this register, unchanged:** I.2.6, I.2.8, I.2.10 and I.2.12 mark statistical
significance **by cell colour**, and a colour is not in served text. No sentence of any piece built here
may say that a Mongolian movement is or is not statistically significant on this register's authority.

## 6. What this is worth, and what it costs

Walked in one evening from one instruction. **Two open doors the door test named were enough; the second
one (`kemendikdasmen.go.id`) was not needed and stays unwalked for the next run.** `moe.gov.mn` is a new
measurement — open, and a wall.

**The Editor's standing condition is addressed in the brief, not here**, because whether a name read from
a seven-month capture of a replaced site satisfies *a named human from a reachable non-OECD register* is a
judgment and not a measurement, and this file only measures.
