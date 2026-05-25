# Madār — Design System

**Direction:** 02 — Field Atlas
**Status:** Working spec, v0.1 — codifies the two article mockups in `/design-assets/article-mockups/`.
**Owner:** Designer agent
**Last revised:** 2026-05-25

> A research instrument, not a magazine. The publication treats the places it covers as worth measuring with precision. The design withholds warmth so the writing has to carry it.

---

## 1. Color tokens

Five tokens. No more. Including neutrals. This is non-negotiable.

| Token         | Hex       | Role                                                              | Forbidden uses                                                          |
| ------------- | --------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `--paper`     | `#FAFAF7` | Page ground. Off-white, slightly warm. The default everywhere.    | Never used on type. Never replaced with pure `#FFFFFF`.                 |
| `--ink`       | `#0E1B2C` | Primary text, primary line work, masthead, body type.             | Never replaced with pure `#000000`. Never used as a tint below 80%.     |
| `--orange`    | `#D94F2A` | **Survey marker.** Data accents, micro-numerals, footnote refs, "new" markers on diagrams, kickers. | Never on body type. Never as a background block. Never decorative. If it isn't carrying meaning, it isn't on the page. |
| `--sage`      | `#7A8471` | Secondary data, marginalia, captions, footnote text, prior-state markers on diagrams. | Never as a hero color. Never on display type.                           |
| `--sand`      | `#E8E2D0` | Ground fills inside maps and object photographs. Page-block edges. | Never as a page background. Never behind body type — it competes with `--paper`. |

**Rules of use:**
- A spread should never carry more than two non-neutral colors (`--orange` + `--sage`) at one time, and `--orange` is always the minority.
- The orange-to-sage ratio on any diagram should be: most of the data is sage; orange is what changed, what crossed a threshold, what we want the eye to land on.
- If the article does not need orange, it does not get orange. Some essays in Direction 02 will run with `--paper` + `--ink` only and that is correct.

**Contrast (verified):**
- `--ink` on `--paper`: 14.4:1 — AAA across all sizes.
- `--orange` on `--paper`: 4.5:1 — AA for large display only. Never used on body type for this reason.
- `--sage` on `--paper`: 4.2:1 — AA large only. Captions and marginalia sit at ≥11px and have been designed at this contrast intentionally; for legibility, anything below 12px in sage must be ≥500 weight.

---

## 2. Typography

Two families. One Latin, one Arabic. Both have the same editorial register.

### Latin

| Step             | Family                  | Size (desktop) | Leading | Tracking  | Weight | Used for                          |
| ---------------- | ----------------------- | -------------- | ------- | --------- | ------ | --------------------------------- |
| Display (hero)   | Cormorant Garamond *    | 78–96px        | 1.02    | -0.018em  | 500    | Article title                     |
| H1 (alt-display) | Cormorant Garamond      | 56–64px        | 1.05    | -0.015em  | 500    | Cover / section opener            |
| H2 (subhead)     | Cormorant Garamond      | 28–32px        | 1.10    | -0.012em  | 500    | In-article subheads (with rule prefix) |
| Dek              | Newsreader *            | 19–21px        | 1.45    | normal    | 400 i  | One-sentence subhead under title  |
| Body             | Newsreader              | 18–19px        | 1.62    | normal    | 400    | Long-form reading                 |
| Pull-quote       | Cormorant Garamond i    | 26–30px        | 1.18    | -0.005em  | 400 i  | One per piece, never two          |
| Caption          | JetBrains Mono *        | 10–11px        | 1.6     | 0.02em    | 400    | Figure captions, marginalia       |
| Marginalia       | JetBrains Mono          | 10–11px        | 1.7     | 0.04em    | 400    | Footnotes (left rail), source notes (right rail) |
| Kicker / label   | JetBrains Mono          | 10–11px        | 1.0     | 0.14em uc | 500    | "Field Note 01", "Object 01", etc.|
| Numerals         | JetBrains Mono          | inherits       | —       | 0.04em    | 500    | Footnote markers (always orange)  |

\* *Stand-ins for the commissioned faces.* The production system uses **GT Sectra** (display) and **Söhne / Diatype Mono** (sans/mono). Cormorant Garamond is the closest free Sectra-spirit serif; Newsreader gives the body family the same on-page color as Sectra Text; JetBrains Mono stands in for Diatype Mono. **None of these are the final faces.**

### Arabic

| Step           | Family                | Size (desktop) | Leading | Used for                              |
| -------------- | --------------------- | -------------- | ------- | ------------------------------------- |
| Display (hero) | Amiri *               | 60–84px        | 1.35    | Arabic title and pull-quotes          |
| Body           | Amiri                 | 19–21px        | 1.85–1.9 | Arabic paragraphs                     |
| Caption        | Amiri 400             | 13–14px        | 1.7     | Arabic captions, kashida-aware        |

\* *Stand-in.* The production system uses **Greta Arabic** (display) and **Adelle Arabic** (body). Amiri is the closest editorial-Naskh free pairing. Both production families have the same x-height and color on the page as Sectra Text — this matters more than visual similarity.

**Arabic rules:**
- Arabic is **never** sized smaller than its Latin counterpart on the same page. Same optical weight, same color (`--ink`), same authority.
- Arabic body text uses kashida-friendly families. No geometric/web-UI Arabic faces for body type.
- Every piece on an Arabic-speaking geography carries at minimum one Arabic paragraph, set as a **parallel reading**, not a translation. The Editor writes the parallel paragraph; the Designer holds the line that it gets real estate.
- `dir="rtl"` and `lang="ar"` on every Arabic block. Not optional.

---

## 3. Grid

A 12-column grid on desktop, collapsing predictably.

| Breakpoint | Columns | Gutter | Max width  | Outer padding |
| ---------- | ------- | ------ | ---------- | ------------- |
| ≥ 1280px   | 12      | 24px   | 1280px     | 32px          |
| 1024–1279  | 12      | 20px   | fluid      | 32px          |
| 720–1023   | 6       | 16px   | fluid      | 24px          |
| < 720      | 4       | 12px   | fluid      | 20px          |

**Article reading grid (within the 12-col):**
- Left rail (footnotes/marginalia): cols 1–2 (≈ 17%)
- Main column: cols 3–9 (≈ 58%)
- Right rail (source notes, glossary): cols 10–12 (≈ 25%)

**Baseline:** 8px. All vertical rhythm snaps to multiples of 8.

**Mobile collapse:** the left rail (numbered footnotes) disappears below 720px; its content is referenced inline via `<sup>` numerals and surfaced in a single "Notes" block at the end of the piece. The right rail moves below the main column, never above it.

---

## 4. Hero treatment — taxonomy

The publication does not have a hero "template." Every piece commissions one of four categories of artwork. Each category has a posture, a fit, and a failure mode.

### (a) Commissioned cartography
**What:** A custom map drawn for a single piece. Always credited like a photograph. Always carries a scale bar, a compass, a legend, source attribution, projection note.
**When appropriate:** Pieces about geographic distribution, catchment, district-level data, infrastructure, movement of students/teachers/families.
**What makes it succeed:** The map reveals something the prose alone cannot — an irregularity, a clustering, an absence. The data is the figure; the geography is the ground.
**What kills it:** Decorative cartography. A map that exists to "be visual" rather than to argue. Maps without scale bars, legends, or source lines.
**Example in this issue:** *The Twenty-Mile Walk* — Sierra Leone district map.

### (b) Commissioned object documentation
**What:** A single physical object — textbook, uniform, blackboard, exercise book, school sign — photographed (or, in this mockup phase, rendered) on a neutral ground with a ruled scale and a museum-style object record card (catalogue number, dimensions, year, publisher, page count).
**When appropriate:** Pieces about a specific artefact whose physicality carries the argument: curriculum change, material conditions, design of an instrument.
**What makes it succeed:** The object is treated like a specimen — the publication is the museum, the article is the wall label. Restraint of the framing carries it.
**What kills it:** Lifestyle photography. The object as "context" rather than as subject. Multiple objects in one frame.
**Example in this issue:** *The Civics Page That Changed Three Times* — Grade 7 civics textbook, 2018 edition.

### (c) Commissioned isotype / diagram
**What:** A data drawing — not a chart from a charting library. A figure made for the page, by hand, sometimes using the small "person" or "centre" symbol Madār commissions for the publication. Sage / orange palette. Sourced and credited.
**When appropriate:** Quantitative claims where the structure of the data (a bimodal distribution, a band-by-band comparison, an inequality) is the point.
**What kills it:** Generic bar charts. Pie charts (never). Charts whose axes aren't labelled with units.
**Example in this issue:** *Figure 02 — Student-teacher ratio* (Sierra Leone); *Figure 02 — Page 42 across three editions* (Jordan).

### (d) The "no image" essay — large headline on empty page
**What:** No hero artwork at all. The headline, set huge in the display face, is the picture. The facing space is half-empty by design — the empty space is not a mistake; it is the design.
**When appropriate:** Essays where the argument is interior rather than evidentiary. Reflective pieces. Polemics. Single-source memoirs. Anything where an image would diminish the prose by competing with it.
**What kills it:** Using this treatment because the commission failed. The empty page must be a choice, not a defeat. The Editor and Designer agree, before any commission begins, when a piece is in this category — it isn't a fallback.
**Frequency:** Roughly one in seven pieces. Less than that and the device weakens. More than that and the publication looks like it can't afford imagery.

**Other categories Madār reserves the right to add later** (not in v0.1): commissioned illustration in the literary sense (a single illustrator's work across an issue's spine, à la *The New York Review of Books*); commissioned typography (a piece's title set as a one-off lettering commission). Both require a roster the publication does not yet have.

---

## 4b. The Still

The hero taxonomy is the publication's *documentary* discipline — what Madār chooses to look at, and how it looks. **The Still** is the publication's *illustrated* gesture — a hand-drafted SVG composition of a single continuous calligraphic line (or a few overlapping lines, possibly in different colours from the five-token palette) that draws the article's subject as one flowing gesture, like a pen that never lifts.

Every piece carries exactly one. Same five-token palette as the rest of the system, but used as the *colour of the line itself* rather than as filled volumes underneath.

### What it is (v0.4 · 2026-05-25)

A single composition built from one register only: **the line.**

1. **A continuous calligraphic line.** One `<path>` (or a small stack of paths reading as one gesture) that lands on the paper-cream ground and flows from beginning to end without lifting. The line draws a concrete object or scene from the article — a chalkboard with last term's writing inside it, an open textbook page, a small schoolhouse with a flag — but draws it *interpretively*: the line should make the reader *feel* the subject, not see it diagrammed. The drawing is calligraphic — the line breathes, varies stroke-width, occasionally flourishes — not architectural.
2. **Multi-line and multi-colour permitted, when earned.** A second or third line in another palette token (sage, kiln-orange, sand) is welcome when the piece carries a specific reason for it: in Field Note 02 (Jordan), three lines in three colours draw the same textbook page three times, encoding the civics page that changed three times; in Field Note 01 (Sierra Leone), a short orange line is the stick of chalk on the ledge; in Curated 01 (Colombia), a sage line traces the mountain ridges behind the schoolhouse. **Default is one line in ink unless the piece earns more.**
3. **No filled volumes underneath.** The previous (v0.3) convention of soft atmospheric colour volumes is **retired**. The ground is paper-cream (`#FAFAF7`) only — no gradients, no filters, no translucent washes, no Gaussian blur, no grain. The discipline of *the line is everything* is now the convention.

**The convention is: one continuous calligraphic line (or a few overlapping lines, possibly in different colours) drawing the article's subject as one unlifted gesture. The line IS the image; the ground is paper-cream.**

The reference register has two anchors: (1) the line-based work of **Hassan Massoudy** — calligraphic Arabic gesture as continuous, variable-pressure brush; (2) the continuous-line illustration work catalogued under *Again Around the Line* on Behance — one unlifted stroke that draws a recognisable subject. The deeper inspiration is the way an Arabic letter is one continuous gesture from initial form through medial to final, where the line *is* the meaning. The publication is reaching for: **a single calligraphic line that draws the article's subject in one breath, the way an Arabic word flows from its first letter to its last.**

The **phone-wallpaper test** is the operative standard: if a reader would not save the composition to their phone as a lock-screen image, it is not a Still. Beauty is the threshold, not a bonus.

It coexists with the documentary hero; it does not replace it. The map / object / isotype / empty-page treatment in §4 is the article's *instrument*; the Still is the article's *illustrated atmosphere*. A Field Atlas piece without a documentary hero is unfinished; a Field Atlas piece without a Still is missing its illustration.

### What it is not

- **Not a logo.** It does not repeat. Each piece gets its own.
- **Not a diagram.** No grids. No tally marks. No labelled axes. No legend. If it can be read as a chart, it has failed and must be redrawn.
- **Not a chart-dressed-as-art.** The previous *Signature Mark* convention (rule-derived geometric compositions with captioned rules) is retired. A composition that reads as an *encoding of the argument* belongs in §4c (isotype/diagram), not here.
- **Not pure abstraction.** The previous *mood-only Still* convention (atmospheric volumes alone, no representational subject) is retired as of v0.3 (2026-05-25). A composition that reads only as *weather* — with no concrete figure for the reader to attach to — fails.
- **Not atmospheric.** The previous v0.3 convention of *soft colour volumes underneath a line drawing* is retired as of v0.4 (2026-05-25). The volumes fought the line for attention; readers split their gaze between the watercolour ground and the ink figure, and the picture stopped being *one decided thing*. **There are no filled volumes underneath the line.** The ground is paper-cream (`#FAFAF7`) only.
- **Not architectural.** The line is not CAD-perfect. It does not have ruler-straight edges, uniform stroke-width, vector-perfect corners, or geometrically-precise curves. A composition that reads as *blueprint* or *technical drawing* has drifted out of register. Treatment: redraw the line as one calligraphic gesture with variable stroke-width, breathing curves, and the occasional flourish — the line of a hand, not a machine.
- **Not over-illustrated.** The subject is drawn in a few continuous strokes with confident weight variation. The drawing is *minimal* — no cross-hatching, no rendered shadows, no cartoonish detail, no decorative ornament. If it reads as cartoon or as too-realistic, it has drifted out of register.
- **Not multi-stroke geometric assembly.** Stacking little rectangles and triangles to "build" the subject (a schoolhouse as a rectangle plus a triangle plus a smaller rectangle for a door) is the failure of v0.3-round-3. The Still is not Lego. It is a calligraphic line that flows through the subject as one gesture.
- **Not stock art.** No generic abstract gradients pulled from a free-art site. The Still is drawn for the piece, against the piece's subject.
- **Not a hero alternative.** When an article's hero category is "no image" (§4d), the Still *still* runs — its presence does not contradict the no-image discipline. The empty-page essay carries one Still, sized at ~60% scale, placed at the foot.

### The rule (load-bearing)

> **The Still is a single continuous calligraphic line — or a few overlapping lines, possibly in different colours from the five-token palette — that draws the article's subject as one flowing gesture, like a pen that never lifts. No filled volumes, no gradients, no soft atmospheric backgrounds. The line IS the image; the ground is paper-cream.**

The line is drawn from the article's *subject* — the most concrete object or scene the prose is about — but drawn *interpretively*, not literally. A chalkboard becomes a single flowing gesture that suggests *chalkboard-ness*: the rectangular outline, the chalk-line written inside, the stand beneath, all in one continuous stroke. The viewer should feel *teacher-and-board*, not see a technical drawing of a board.

Example pairings (v0.4):
- *The teacher in Bo who still uses last term's chalk* (Sierra Leone) → **one continuous ink line landing at the upper-left, breathing its way around the chalkboard's outline, flowing inward to write the partial word and half-erased tally arithmetic, exiting at the lower edge into the two-legged stand and a soft floor-line. A second short line in kiln-orange is the stick of chalk on the ledge with a small drift of dust.** Two lines, two colours (ink + orange).
- *The civics page that changed three times* (Jordan) → **three continuous lines drawn from beginning to end without lifting the pen, each one rendering the same open textbook page in slightly offset positions and ink colours: ink for the oldest edition, sage for the second, kiln-orange for the third. Three editions of one continuous gesture, layered as a palimpsest.** Three lines, three colours — the piece earns the multi-colour invitation.
- *Escuela Nueva at fifty* (Colombia) → **one continuous ink line landing at the lower-left footpath, rising into the small rural schoolhouse — walls, pitched roof, flag rising from the apex — dipping back to draw the door and two windows, then flowing out as the footpath continues to the right. A second line in sage traces the mountain ridges behind.** Two lines, two colours (ink + sage).

The line-subject is logged in the Stills gallery file alongside the SVG so the convention is auditable. The Still carries no caption text on the page. A short colophon line under the composition names the article number and the Still maker, and that is all.

### Where it lives in the layout

The Still occupies a **dedicated full-width composition placed mid-article, between two body sections** — never inside a section, never at the open. In print it runs **bleed-edge** (full-trim, no frame); on web it runs **full-width of the article container**, breaking the body grid, with no caption rail to its right — the composition takes the whole reading width.

In v0.1 the position is: **after the second body subhead, before the third subhead, OR between the Arabic section and the secondary figure, whichever produces a longer visual rest in the page rhythm.** The Designer decides per piece.

For "no image" essays, the Still is reduced to ~60% of normal size and placed at the foot of the body, above the article footer.

### Constraints

- **Same five-token palette.** No new colours. The five tokens (ink, orange, sage, sand, paper-cream) appear here as the *colour of the line itself* — never as filled volumes. Default line colour is ink (`--ink`). A second or third line may be drawn in orange (`--orange`), sage (`--sage`), or sand (`--sand`) when the piece earns it. The ground is always paper-cream (`--paper`); no exceptions.
- **No volumes, no gradients, no filters, no grain.** The v0.3 atmospheric register is retired. The composition is *line on paper-cream*, full stop. `<linearGradient>`, `<radialGradient>`, `<filter>` (Gaussian-blur, turbulence, etc.), and `<rect>` fills underneath the line are all forbidden in the Still as of v0.4. The discipline of *the line is everything* makes the publication's illustrated voice unambiguous.
- **Continuous-line subject, mandatory.** The line draws a concrete element from the article's subject as one unlifted gesture (or a small number of unlifted gestures). The line is calligraphic: variable stroke-width, organic curvature, occasional flourish. **Variable stroke-width is achieved in SVG by stacking 2–3 paths at the same approximate shape with subtly different `stroke-width` values (e.g., 3.0 / 1.8 / 0.9) and slightly offset positions, creating the impression of a brush varying pressure.** All paths use `stroke-linecap="round"` and `stroke-linejoin="round"` to keep the line breathing. `fill="none"` on every line path; no exceptions.
- **No registration marks. No corner ticks. No scale annotations. No mono captions inside the composition.** Those are the documentary hero's vocabulary; the Still is the other side of the publication's grammar.
- **Hand-drafted SVG.** Built by the design lead inline in the article HTML (or as a standalone file referenced from the Astro template). No bitmap exports. No images embedded. No external dependencies. The Still is part of the document, not an asset linked to it.
- **Substantial.** A meaningful Still carries at minimum **80 lines of meaningful `d=…` path data and ~120 lines total SVG.** The line should look like someone *drew* it, not generated it. The cumulative gesture-paths (stacked weights, multiple line-colours) accumulate into a composition that breathes.
- **Finite.** The composition reads as *completed*, not as a sample from an infinite series. No tiled noise, no infinite-canvas effect. A Still has a centre of attention — which is, in v0.4, the line-drawn subject itself.

### Sourcing — how the Still gets made on zero budget

The Still is **produced in-house by the design lead, in SVG, against the article's mood-words.** This is the primary and default path. It is not a commissioned artwork. The publication does not commission Stills in v0.1.

Two adjacent paths exist for occasional use, never as a default:

- **Public-domain artwork from regional cultural archives** — the Wellcome Collection, Internet Archive, Rijksmuseum Open Access, the Met Open Access, Smithsonian Open Access, and regional library digitization projects. Where a piece's geography has a strong archival record (Maghreb miniatures, West African textile catalogues, Levant lithographs from early-20th-century Beirut presses), a public-domain artefact may be colour-graded into the Madār palette and used as the Still — provided the artefact itself is a *gesture*, not a documentary photograph. License: CC0 or explicit public-domain. License notes logged alongside the file.
- **Free-source photography**, under the rules in §4d below — never as the Still itself, only as secondary breathing room mid-article.

The publication does not use AI-generated abstract art for the Still. The temptation is real; the failure mode is louder. AI compositions read as ambient noise to a reader, and the Still must read as *decided*.

### Failure modes — when a Still fails

- **Diagrammatic drift.** The composition has accidentally become a chart. Diagnosis: there is a grid, a series of equal units, an axis-like baseline, or a tally rhythm read as data. Treatment: redraw — the line must read as *picture*, not as *chart*.
- **Pure abstraction.** The composition is mood-only — a vague flowing line with no recognisable subject. Diagnosis: a reader cannot say in one sentence what the line draws. Treatment: redraw the line as a concrete element from the article's subject, interpretively but recognisably.
- **Atmospheric drift (NEW failure mode, v0.4).** Soft colour volumes, gradients, blurs, or grain washes have appeared underneath the line. Diagnosis: the v0.3 register has crept back. The reader's eye splits between the watercolour ground and the ink figure, and the picture stops being *one decided thing*. Treatment: delete all `<linearGradient>`, `<radialGradient>`, `<filter>`, and `<rect>` fills underneath the line. Ground must be paper-cream only.
- **Architectural / CAD-perfect line (NEW failure mode, v0.4).** The line is too clean — ruler-straight edges, uniform stroke-width, geometrically-precise curves, vector-perfect corners. Diagnosis: the drawing reads as a blueprint or a wireframe rather than as a hand. Treatment: vary stroke-width across the path by stacking 2–3 paths at different weights (e.g., 3.0 / 1.8 / 0.9); allow small wobble and breath in the curves; let the corners round, not snap.
- **Multi-stroke geometric assembly (NEW failure mode, v0.4).** The subject was built by stacking little rectangles and triangles like Lego — a schoolhouse as a rectangle plus a triangle plus a smaller rectangle for a door, all as separate primitives. Diagnosis: the composition reads as *parts* rather than as *one gesture*. Treatment: redraw the subject's outline as one continuous bezier sequence; the door and windows may dip back inside, but the perimeter must flow as one breath.
- **Over-illustrated.** The drawing has become cartoonish, decorative, or too literal — cross-hatching, rendered shadows, faces with expressions, scenes with too many objects. Diagnosis: the line stops being *minimal* and starts being *decorated*. Treatment: strip the drawing back to its essential strokes; the subject should read in three to six confident gesture-paths, not thirty fussy ones.
- **Decorative use of any colour.** A colour has spread because it is attractive, not because the piece earns it. The default Still is one line in ink; a second or third line in another palette token must answer a specific question the piece is asking (Sierra Leone: *what's on the ledge?* — orange chalk; Jordan: *what changed?* — three editions in three colours; Colombia: *what's behind the school?* — sage mountains). If a line cannot answer such a question, it does not belong.
- **Fails the phone-wallpaper test.** A reader would not save it. Treatment: ask whether the line draws something specific, whether the line breathes calligraphically, whether the picture reads as *one decided thing*. If two of those are no, the composition is not finished.
- **Drifts toward the documentary hero's register.** Hairline strokes, registration ticks, mono-font annotations, measured tally marks — these are the §4 vocabulary leaking into §4b. Strip them out.

### Convention name

Called **the Still** throughout the system spec, briefs, and contributor notes. The Arabic term used in bilingual briefs is **سكون** (*sukūn* — *stillness, calm, the diacritical sign for absence of vowel*), which sits alongside the documentary brief in any commission package. The publication does not refer to it as a "vignette," an "ornament," a "spot," or — any longer — a "Signature Mark." Discipline of naming is part of discipline of practice; the previous name (Signature Mark · *tawqīʿ*) is retired with v0.1 as of 2026-05-25.

### Version history of the Still convention

The Still convention has evolved across the v0.1 design pass:

- **v0.1** (2026-05-25) — *Signature Mark · tawqīʿ*. Rule-derived geometric compositions with captioned rules. Retired: read as chart-dressed-as-art.
- **v0.2** (2026-05-25) — *Mood-only abstraction.* Painterly soft volumes alone, no representational subject. Retired: too still, nothing concrete to attach to.
- **v0.3** (2026-05-25) — *Atmospheric volumes + continuous-line subject.* Soft colour volumes (ground) + a continuous-line drawing of a concrete subject (figure). Retired in two stages: first the line drifted toward filled-shape object illustration (round 3); then the volumes themselves were retired (round 4) because they fought the line for attention.
- **v0.4** (2026-05-25, current) — *Single continuous calligraphic line on paper-cream.* The line IS the image; the ground is paper-cream. Multi-line and multi-colour permitted when the piece earns it (Sierra Leone: orange chalk; Jordan: three editions in three colours; Colombia: sage mountains). Inspiration: Hassan Massoudy's calligraphic gesture; the way an Arabic letter is one unlifted breath from initial to final form.

---

## 4c. Free-source photography — secondary breathing room

Photography is not used as a hero treatment and is not used as the Still. Both are forbidden. Stock photography in the hero slot remains forbidden in §6.

Photography is permitted in one position only: **as secondary breathing room mid-article, inside long pieces** (3,000 words and above), where the reading rhythm benefits from a wider-than-text visual rest that is not a diagram and not a Still. A piece carries at most **one** photographic rest; a piece may carry zero.

### Sources (license-checked)

- **Unsplash** — CC0-equivalent license. Attribution to the photographer is encouraged but not required by the license. Madār credits photographers in the article footer regardless.
- **Pexels** — Pexels License, free for editorial and commercial use, no attribution required. Madār credits regardless.
- **Museum Open Access** — Wellcome Collection (CC0 / CC-BY for some items), Rijksmuseum Public Domain, Met Open Access (CC0), Smithsonian Open Access (CC0), Internet Archive (mixed — license per item).
- **Library of Congress Free to Use and Reuse**, **NYPL Public Domain Collections**, **NASA Image Library** (public domain) — used for archival or scientific imagery where the documentary register is appropriate.

**Not used:** Getty / Shutterstock / Adobe Stock (paid). Flickr without an explicit CC0 / CC-BY tag (license confusion). Any "free with credit to photographer" image where the credit obligation has not been read and logged. Pinterest scrapes (license unknown, never acceptable).

### Treatment

Photography in Madār is **colour-graded into the publication's palette before it appears on the page**. A raw stock photograph carries a stock-photograph register that would kill the publication. Treatment is one of:

- **Duotone**, `--ink` to `--paper`, with mid-tone shifted slightly warm into `--sand` — used for atmospheric / landscape rests.
- **Muted desaturated grade**, 35–45% saturation, with a 4–6% `--paper` overlay to lift the highlights into the page tone — used for documentary or archival photographs where colour information matters.
- **Sage tint**, `--sage` overlay at 8–12%, used for photographs of distance, road, sky, water.

All photographs carry **a 1–2% film-grain overlay** to match the painted register of the Still and to break the digital flatness that stock photography arrives with.

### Position and credit

The photographic rest sits **full-width** of the article container, between two body subheads, and **never adjacent** to the Still (the two atmospheric events do not stack). The credit line — *Photograph: [name] / [source] / [license]* — sits in the right marginalia rail in `--sage` mono, never as a caption inside the image.

### Failure modes

- **Stock register.** The image looks like a corporate landing page. Diagnosis: untreated colour, generic composition, "concept" subject matter (lightbulbs, handshakes, sunsets-with-a-person). Treatment: do not use this image; find an archival or specific one.
- **Documentary slippage.** The photograph reads as evidence (a real child in a real classroom). Diagnosis: the article's hero is the cartography or object documentation; the photograph is competing for that role. Treatment: remove. The Still and the hero are sufficient.
- **Untreated colour.** The grade has not been applied. Diagnosis: the photograph clashes with the page palette. Treatment: re-grade or remove.

---

## 5. The macron as system motif

The horizontal bar over the *ā* in *Madār* is the smallest, most repeatable unit of the brand. It appears in six places besides the wordmark:

1. **Scale bars on maps.** The macron is, conceptually, a scale bar over a single letter. Every cartographic hero carries one literal scale bar that visually echoes the macron above.
2. **Rule lines under section openers.** A 38px horizontal bar precedes every H2 subhead. The reader picks up the rhythm without noticing it.
3. **Subheads have it on the left** (rule before text), **the masthead has it below** (rule with two terminal ticks under the wordmark). These are the only two positions. The rule does not float, does not center decoratively, does not appear without a clear anchor.
4. **Folio underlines.** Page numbers and figure numbers sit under a short rule.
5. **Object record cards.** Dimensions, year, edition — the field labels in object documentation are separated from their values by the same horizontal stroke.
6. **Pull-quote rule.** A 2px vertical rule on the left (LTR) or right (RTL) of every pull-quote — this is the macron rotated 90°, used as a marginal indicator. The orange is reserved for this single typographic event in the body.

**What the macron is not:** decoration. The bar appears only where it has a job — measuring, separating, anchoring. A horizontal stroke without a job is noise.

---

## 6. What the system forbids

- **Infographic-spam.** No chart that exists because we have the data. Every diagram earns its space.
- **Decorative use of orange in the documentary frame.** Orange is data, *in the documentary frame*. If it isn't carrying a meaning the reader can name from the caption, it's wrong. The Still (§4b) is the one place orange is permitted to breathe atmospherically — but only there, and only as a soft wash, not a marker.
- **Arabic as visual flavor.** Arabic is not used as ornament — not on covers, not on dividers, not as a "regional gesture." Arabic is text, set with the same care as English, sized at the same authority, written by someone who is writing, not transliterating.
- **Stock photography in the hero slot.** Ever. The order of preference for the hero is: commissioned cartography / object documentation / isotype > "no image" treatment > nothing. Stock is below "nothing." Free-source photography is permitted *only* as secondary breathing room inside long pieces, under the rule in §4c — palette-graded, never as the hero, never as the Still.
- **AI illustration as default.** AI is a tool inside a commissioning brief, not a replacement for commissioning. When used, the prompt and post-process are logged in `/design-assets/prompts.md`. AI-generated abstract compositions are forbidden in the Still — see §4b.
- **Gradients, drop shadows, skeuomorphism in the documentary frame.** A 1px line is sufficient there. Two-color discipline is the identity of the documentary discipline. The Still (§4b) is the carve-out: gradients, Gaussian blur, and grain are the Still's working vocabulary and are correct *there*. They do not migrate out of §4b into headers, figures, masthead, or hero diagrams.
- **Helvetica, Inter, system-UI as type defaults.** The system fonts only show up as fall-backs and only because the production faces aren't free.
- **Centre-aligned body type.** Asymmetric, left-aligned (or RTL-right-aligned). The page is composed, not centred.
- **More than one pull-quote per piece.** One is striking; two is decorative.
- **Hero "templates."** Every piece is commissioned individually. The category is templated; the artwork is not.

---

## 7. Mobile considerations

Field Atlas is a desktop-first system that does not break on phones.

**What collapses:**
- The 12-col grid → 4-col below 720px. Body column becomes full-width; rails move below or disappear.
- Left rail (footnotes) is hidden; footnote markers (sup-numbers) remain inline and link to a single Notes block at the article's foot.
- Right rail (sources, glossary, read-next) drops below the body column with a thin top rule.
- Object record card collapses from 4 columns to 2.
- Masthead: the three-column header (left meta · wordmark · right tagline) stacks; wordmark stays centred.

**What does not change:**
- Type sizes shrink modestly (body 19→17.5px, display max-capped). The relative rhythm is preserved.
- The hero diagram is full-width and remains the first thing the reader sees. SVG scales without rasterizing.
- Colors and the orange-discipline are identical.
- Arabic sections render `dir="rtl"` correctly at every breakpoint.

**Hero adaptation at narrow widths:**
- **Cartography:** the map scales to fit. Compass, scale bar, and legend remain visible at full-width. Below 480px, the legend reflows below the map.
- **Object documentation:** the object centres in frame; dimension callouts remain. The object record card (catalogue / edition / publisher / dimensions) becomes a 2×2 grid below the image.
- **Isotype/diagram:** the isotype shrinks proportionally. If the symbol-set becomes unreadable below 360px, the diagram swaps to a vertical layout (rows become stacked rows) — this is decided per figure, not globally.
- **"No image" treatment:** the large headline scales down but remains the entire first screen. The empty space is preserved proportionally.

---

## 8. Component inventory (v0.1)

What the mockups demonstrate, named for the Web Developer:

- `Masthead` — three-zone header with wordmark, ticked rule, meta strip
- `MetaStrip` — pre-title field note locator (region · time · format)
- `TitleBlock` — kicker + meta column on left, display title + dek on right
- `HeroFigure.cartography` — bordered frame, head row (Figure N · n=), inline SVG, foot caption with credit line
- `HeroFigure.object` — bordered frame, head row, inline SVG of object, ObjectRecord 4-column card
- `BodyGrid` — left footnote rail / main column / right source rail
- `Subhead` — H2 with macron rule
- `Pullquote` — orange vertical rule + display italic + monospace citation
- `Figure.isotype` / `Figure.diagram` — secondary in-article diagram with caption
- `Still` — full-bleed (print) / full-width (web) painterly SVG composition, no caption rail, atmospheric breath between body sections (§4b)
- `PhotoRest` — full-width photographic breathing room, palette-graded with grain, credit in right marginalia (§4c, long pieces only)
- `ArabicSection` — full-width RTL block with parallel reading + glossary in mono
- `ArticleFooter` — three-column byline / commission credit / publish meta
- `Colophon` — issue line + copyright

Each of these will get a production spec for the Web Developer in `/design-assets/specs/` once the wordmark and the first commission are in.

---

## 9. What's locked vs. what's open

**Locked:**
- Palette tokens (five colors, named roles)
- Type roles (display / body / mono / Arabic) — though the specific commissioned faces are open
- Grid (12 / 6 / 4)
- Hero taxonomy (the four categories)
- The Still convention (one per piece, painterly/lineal, mood-derived, produced in-house in SVG against logged mood-words — §4b)
- The free-source photography rule (secondary rest only, palette-graded, max one per long piece — §4c)
- Macron motif rules
- Forbiddens

**Open — for founder review:**
- The commissioned wordmark (placeholder: Cormorant Garamond + Amiri). First commission.
- The production typefaces (placeholders: Cormorant Garamond, Newsreader, JetBrains Mono, Amiri; production: GT Sectra, Söhne or Diatype Mono, Greta Arabic, Adelle Arabic). Cost-dependent.
- The first commissioned cartographer / object-documentarian. House style is set by the first three issues' commissions.
- Issue cadence and length — design system can support a daily/weekly/monthly cadence equally; throughput question is the Manager's.

---

*This document supersedes the visual decisions in the mood-board. When this document and the mood-board disagree, this document wins.*

---

## 10. The home page

The home is the publication's masthead-page. It is the first impression. It is composed, not assembled.

### Masthead treatment

The home masthead is **vertical and centred**, unlike the article masthead which is a three-column header. On the home page, the bilingual wordmark sits at the centre of a generous vertical block, sized to roughly 120px tall on desktop — large enough to read as the publication's title, small enough to leave most of the first screen as white space. Directly beneath the wordmark sits the ticked rule (the macron motif, sized up from the article masthead's 64px to 120px wide to match the wordmark's optical weight). Beneath the rule sits the bilingual tagline.

The home masthead breathes more than the article masthead does. The article masthead is a navigation bar; the home masthead is a *book cover.*

### The bilingual tagline

The home tagline is one short editorial sentence, set in both scripts at equal weight. The Latin sets in marginalia mono (12px, 0.14em letter-spacing, uppercase, 78% opacity); the Arabic sets in Amiri at 17px, lower-case (Arabic has no case), 85% opacity. Both lines sit at the same optical weight. The tagline is **never** set in display type — display type belongs to the wordmark and to article titles. The home page does not carry a display-type subtitle below the wordmark; the wordmark itself does that work.

The tagline proposed in v0.1: *"Education, from the places others don't look"* / *«التعليم من الأماكن التي لا يُنظر إليها»*. Two readings of the same orientation, written in parallel — the same convention as the in-article parallel Arabic paragraph.

### Still-thumbnails as piece cards

The home's "This week" section lists the issue's pieces as a three-up grid (one-up on mobile). **Each card carries a small Still thumbnail** — a 3:2 aspect-ratio SVG that telegraphs the piece's full mid-article Still. The thumbnail is *not* a cropped or scaled-down copy of the article Still; it is a redrawn miniature, built from the same gradient and filter vocabulary, that conveys the Still's *register* at 360×240px without trying to reproduce every line.

The convention is load-bearing for the home's identity: a reader scanning the home should be able to tell, before reading any title, that the three pieces are atmospherically distinct — Sierra Leone reads as a dawn-warmed horizon; Jordan reads as layered washes with a thin line; Colombia reads as interlocking earth pools. The thumbnail is the publication's visual table of contents.

**Rules for the thumbnail:**
- Same palette discipline as the parent Still. Same five tokens, used atmospherically.
- Same `<defs>` vocabulary: gradients, blur filter, grain filter. The thumbnail is built from the same parts as the full Still, scaled down.
- ~50–80 lines of meaningful SVG, considerably lighter than the full Still's 80+ lines — the thumbnail is a miniature, not a reduction.
- No text on the thumbnail. No caption. The piece card's mono meta strip (type label + country) sits *below* the thumbnail, not inside it.
- Linked: the thumbnail is the piece's primary affordance from the home — clicking it opens the article.

The card below the thumbnail carries, in order: a meta strip (piece-type label in orange + country tag in ink-at-65%), the article title in display type at 28px, a one-sentence dek in body italic at 16px, and a byline + reading-time + hero-category line in sage mono.

### The language switcher

Madār is bilingual at the page level, not bilingual within a page (with the single exception of the in-article parallel Arabic paragraph). The language switcher therefore lives in **two places**:

1. **Top utility bar**, right side: `EN · عربي`. The active language is rendered in orange at 100% opacity; the inactive language is in ink at 65% opacity. The dot between the two is in ink at 30% opacity (a neutral separator, not a decoration).
2. **Footer**, right column under a "Language" label. Same visual treatment.

Both placements are required — the top bar is for readers who arrive knowing they want the Arabic edition; the footer is for readers who have read down the page and now want to try the other script. The two are kept visually identical so the convention reads as one switcher placed twice, not two different switchers.

**Rule:** the switcher never carries flags. Language is not nationality. The Arabic edition is for any reader of Arabic, regardless of geography; the English edition for any reader of English. Flags would reduce the rule. The publication does not reduce the rule.

### Section breaks — the macron divider

Between major sections on the home (between *This week* and *About Madār*, between *About* and the footer), a single **macron divider** runs — a 1px ink rule, 80px wide, centred, with two terminal ticks at each end (same gesture as the masthead rule, scaled down). This is the macron motif from §5, doing the work of a horizontal rule between page sections.

The macron divider is the only horizontal-rule treatment on the home. No other dividers. No coloured bands between sections. The page's structure is held by white space and by the single rule.

### About mini-block

A short bilingual About block sits between *This week* and the footer. Two paragraphs in English (left column), two in Arabic (right column). Both columns end with a small orange "Read the About page →" link in the same marginalia register as the section kickers. The full About lives at a separate URL; the mini-block is the entry, not the substance.

The About block is the only piece of the home that uses body type at body size (17.5px). The thumbnails and the cards use display + mono; the masthead uses display + mono; the About is the page's only place where the publication's *body voice* speaks. That asymmetry is intentional — the home should feel like the cover of a book, with one paragraph of front-matter to set the tone.

### Generous white space

The home runs at the same 1280px max-width as the article pages, with the same outer padding. But the vertical rhythm is intentionally looser: the masthead has 4rem of padding above and 3rem below; the *This week* section has 3.5rem of padding; the About has 3rem; the section gap between *This week* and *About* is held by the macron divider plus 2rem of margin on either side. The page should breathe — it is the publication's first impression and should feel like a serious publication's masthead-page, not a content farm.


