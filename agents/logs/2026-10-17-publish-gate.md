# Publish gate — 2026-10-17

**Shape:** a correction to one published English piece, plus a rendering repair to the
Arabic edition's chrome. No new piece, no flag change, no slug added or removed. The gate
is run in writing before the editorial commit, per the RUNBOOK.

---

## 1. What is being published

### (a) `2026-05-28-kuwait-ccet-arabic-tests` — EN only. Five name repairs.

The piece named one programme **four ways in three places**, and all four disagreed with
the register.

| # | Where | Served for 142 days | Now | Register's own words |
|---|---|---|---|---|
| 1 | `sources[]` annotation | `Multi-sensory Structured Arabic Language Programme` | `… Program` | `Multi-sensory Structured Arabic Language Program` |
| 2 | body, first mention | `… Language Programme. The Programme —` | `… Language Program. The Program —` | as above |
| 3 | body, back-reference | `Technical assistance on the Programme` | `… on the Program` | as above |
| 4 | body, closing section | `The **Multi-Sensory** Structured Arabic Language Programme` | `The Multi-sensory … Program` | as above |
| 5 | body, methodology | `the principles of **Multi-Sensory Language teaching**` | `… multi-sensory language teaching` | register carries no such capitalised name; it writes `multi-sensory program`, lower case |

**Register, and how it was read.** International Dyslexia Association, *'The Center for
Child Evaluation & Teaching (CCET): An IDA Global Partner in the Heart of Arabia!'*, Dr.
Gad Elbeheri, February 2013 — the piece's own source 4.

The origin answers **403 to every client available here**, including a Chrome
user-agent (`103 bytes`, a hard bot wall, not a rendering wall). The read is therefore
from the **Wayback snapshot of 2026-04-14** (`web.archive.org/web/20260414151627/…`,
HTTP 200, 85,291 bytes), in served text, and the sentence is quoted rather than
summarised:

> `Multi-sensory Structured Arabic Language Program. This is a one million dollar project that CCET has co…`

One occurrence, that casing, **`Program`**. The same document names the institution
`Center for Child Evaluation & Teaching (CCET)` ten times and never `Centre`.

**Why this is a repair and not a rewrite (#41).** Nothing about the project changed. The
publication wrote the name in **its own house orthography** — `Programme` is Madār's
spelling, and it was applied to a proper name that is not Madār's to spell. No figure
moves: the USD 1M, the four-test battery, the named humans and the dates are untouched,
and `git diff --stat` is five strings in one file.

**The Arabic edition is unchanged and was never wrong.** It carries no Latin form of the
name at all — it renders the programme as «البرنامج العربي مُتعدِّد الحواس المُهَيكَل»,
identically in both of its occurrences, and it renders the methodology as a *description*
(«مبادئ التدريس مُتعدِّد الحواس») where the English had capitalised it into a name.

### (b) Arabic chrome — the rendering repair (standing-queue item 10)

`global.css`, `SiteFooter.astro`, `pages/ar/browse/[...path].astro`. No content file
touched; no frontmatter touched. Detail in §4 and in `agents/logs/qa-2026-10-17.md`.

---

## 2. Verdicts on file

| Gate | State |
|---|---|
| Editor's five-test verdict | **On file** — `content-drafts/verdicts/2026-05-28-kuwait-ccet-arabic-tests.md`, unchanged. This is a correction to an approved piece, not a commission; the frame, the argument and every figure are untouched, so the verdict does not re-open (same disposition as the 10-16 Oman repair). |
| Verifier verdict | **On file**, unchanged, and not re-opened for the same reason. |
| Arabic gate | **Not engaged** — the Arabic article file is byte-identical. The Arabic edition's *chrome* changed and is inspected by render in §4. |
| Editor question raised, NOT self-answered | The body's **first** mention of the institution is correct (`The Center for Child Evaluation and Teaching`) and the **seven** subsequent short-form references read `the Centre`, the house spelling, for a body named `Center`. These are back-references, not restatements of the name, and changing them is a voice decision rather than a correction. Routed to the Editor; **deliberately not changed by this run.** |

## 3. Assets

| Item | State |
|---|---|
| Hero still `web/public/stills/2026-05-28-kuwait-ccet-arabic-tests.svg` | present, unchanged |
| Share card `web/public/og/2026-05-28-kuwait-ccet-arabic-tests.png` | present, unchanged |
| New assets this run | none |
| Held pieces' assets in the build path | none — there are no held pieces |

## 4. Build and assertions

* `npm run build` — **exit 0**.
* **Seventeen `postbuild` gates** — all green. They are chained with `&&`, so exit 0 is
  their verdict collectively; the twelve that print a named line printed `CLEAN`.
* **Twelve CI build-step assertions re-run by hand, each exit code read on its own**, with
  no pipe between an instrument and its verdict: `qa_a11y_lang` 0 · `qa_ar_language` 0 ·
  `qa_body_links` 0 · `qa_consumer_surface` 0 · `qa_dist_input` 0 · `qa_geo_fields` 0 ·
  `qa_held_assets` 0 · `qa_hreflang_clusters` 0 · `qa_jsonld` 0 · `qa_lastmod` 0 ·
  `qa_reachability` 0 · `qa_robots` 0.
* `qa_patch_queue .` — **CLEAN**, and the register it derives is the authority rather than
  any prose: **32 standing assertions · 12 CI build steps · 17 `postbuild` · 29 of 32
  gating**, the three non-gating ones named in the output.
* **Held-slug leak: zero, vacuously** — there are no held pieces, so the assertion is in
  its post-flip (all-approved) mode per the 2026-08-09 inversion rule. `approved: false`
  count in the build path: **0**.
* **Looked at, not inferred** (ruling #16, and the 08-23 perimeter rule): the Arabic
  article footer and the English article footer were rendered in headless Chrome at
  1280×420 with the regions above the footer suppressed, and both were opened. Arabic
  strapline now sets in Amiri, upright, correctly joined, with its tashkeel intact;
  English strapline unchanged in Newsreader italic. The Arabic browse page was rendered
  at 1280×2400: facet names shaped and joined in Amiri, counts still in JetBrains Mono.

## 5. Gate verdict

**PASS.** One English content file corrected against its register in the register's own
words; the Arabic edition untouched and not wrong; three stylesheet files repaired with
both English controls measured unchanged to the byte and both editions rendered and
looked at. Nothing held, nothing new, no flag moved.
