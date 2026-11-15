# Growth — one macron, 33,736 bytes a page, and the day the date register stopped being a seed

**2026-11-15.** Growth action: **a reader-cost reduction, measured, shipped and proved** — plus the
standing bet's **second** real reading, which is the one that matters, because yesterday it read a true
**zero** and today it had to read a true **change**.

*(No tracker, no third party, no estimate. Return rate is unmeasurable by design and nothing here
pretends otherwise. What this function can read without anyone's permission is what a reader is made to
download, and today it went down.)*

---

## 1 · The action: the wordmark's macron, moved one code point

Standing-queue item 108, limb 2, raised this morning out of item 39's judgment and taken the same day
because it is **not** the face judgment limb 1 is.

**The finding.** `Madār` in the footer — and in the CHARTER-mandated CSS-only header fallback — is the
only text in the display face on most pages. `ā` is **U+0101**. Cormorant Garamond's `latin`
`unicode-range` ends at **U+00FF**. So the precomposed macron falls one code point into the `latin-ext`
cut, and the browser fetches **`cormorant-garamond-normal-400-600var-latin-ext.woff2`, 33,736 bytes, to
paint one character.** The gate has printed `1 chars  33,736 b/char` on every build since assertion 39
shipped; nobody had read the line as a defect.

**The change.** `Madār` → `Madār` — `a` plus **U+0304 COMBINING MACRON**. U+0304 is listed
*inside* Cormorant's `latin` range (Google carves it there precisely so decomposed forms do not pull
latin-ext), so the page paints the macron out of a file it already has.

**Measured by the gate's own server-log probe, before and after:**

| page | before | after | delta | files |
|---|---|---|---|---|
| EN home | 647,276 | **613,540** | −33,736 | 10 → 9 |
| AR home | 295,628 | **261,892** | −33,736 | 7 → 6 |
| EN article | 521,408 | **487,672** | −33,736 | 8 → 7 |
| AR article | 295,628 | **261,892** | −33,736 | 7 → 6 |
| EN editions | 636,664 | 636,664 | — | 9 → 9 |
| AR editions | 334,888 | 334,888 | — | 8 → 8 |

**The two that did not move did not move for a reason, and it is a good one.** The Editions pages print
`Madār` sixteen more times from the editions registry and the inline covers — none of it from the
chrome component — and one of those pages carries a sentence *about the macron itself*. They keep the
fetch because they genuinely need it.

**The corpus-wide total is NOT claimed, and the refusal is the point.** This probe is a **sample of six
of 138** (standing-queue item 41's discipline, stated rather than violated). A static scan cannot close
the gap either: **all 138 served documents still contain a precomposed `ā` somewhere in visible text**
— in the footer rights line, in prose, in the registry — and whether that character triggers *this*
file depends on **which face paints it**, which is a property of render time and not of the document.
On the Arabic home the surviving `ā` is painted by Amiri and costs nothing. *A static answer here would
be an answer about the probe and not about the page* (#93's shape, and the same lesson today's quality
function reached from the other side: a face is chosen per character, at render time).

### Proved, and the control is the one that mattered

Rendered in headless Chrome at the real **22px / 2× device scale**, 108,000 pixels: **before vs after,
0 differing pixels, ink 1,015 both.** At 88px over 154,000 pixels, **0 differing pixels** across four
renderings — precomposed and decomposed, each with the full bundle and with latin-ext deleted.

**Four identical renders is exactly what a broken probe looks like**, so a control was run before any of
it was believed: the same page with the webfont stylesheet removed renders at **ink 4,710 against 3,349
and 6,070 differing pixels.** The webfont was loading. The injection changed the artefact (2026-09-14,
and #123's fabricated-defect lesson pointed at a *fix* instead of a bite).

Full build **exit 0**, all 27 postbuild assertions and all 12 build-job gates green, `qa_font_payload`
CLEAN on both asserted limbs after the change.

**Guarded with a comment and not with a gate, and that is a known gap.** The component now carries nine
lines explaining why the decomposition is deliberate, with the measurement and the date, ending *do not
"correct" this to `ā`*. Nothing asserts it. A future edit types the precomposed form and the 33,736
bytes come back silently on every page. Raised as a queue row rather than left as a hope.

---

## 2 · The bet: the output-bounded date register took its first real change, and the declared error collapsed

The standing bet is `served_dates.py` — the register that makes `<lastmod>` a claim about **served
bytes** rather than about git provenance. Three readings now exist and they are the three that were
needed, in the right order:

| | | |
|---|---|---|
| **2026-11-13** | first contact with a real content change | it moved, and it broke in the half worth breaking |
| **2026-11-14** | a genuinely quiet day | **0 pages moved** — and under the retired provenance resolver every index page's date would have moved |
| **2026-11-15** | a real chrome change | **137 of 138 pages moved**, and the register says so |

**A metric that cannot read zero cannot be trusted to read one; a metric that reads zero and then
cannot read one is just broken.** Yesterday proved the first half and today proves the second, and the
order matters — a register that had read 137 first would have proved nothing at all.

**And the declared error collapsed in one day: 134 seeded → 1.** The register opened on 2026-11-11 with
134 of 138 entries carrying a *seed* rather than an observation — a known error whose size and direction
were derived into the tool's own output yesterday. A chrome change touches every page's served bytes,
so 137 seeds were replaced by real observations this afternoon. **The single survivor is
`/madar/valence/`**, which sits outside the Astro layout by design and so was not touched.

**This discharges standing-queue item 106 by EVENT rather than by DESIGN, and that is recorded rather
than claimed as a win.** Item 106 named the 47 chrome-ceiling seeds as the harmful half of the declared
error — too *late*, upper-bounded, and concentrated on the home pages, About and the Editions pages,
the pages a crawler visits most. All 47 now carry an observation. **Nothing was fixed; the world moved
under the measurement.** The design question the row was raised to answer is untouched and survives as
its own narrower row: *what should a NEW page's seed be, given that the ceiling is the wrong answer and
one observation cannot date a page?* — because the next page this publication serves will be seeded by
the same code that produced the 47.

**One cosmetic consequence, named so the next run does not read it as a fault.** `--check`'s derived
error block now narrates two cohorts of size zero at length — *0 own-source seeds are TOO EARLY … 0
chrome-ceiling seeds are TOO LATE* — which is the tool correctly deriving a description of an empty
set. It is right and it reads oddly. Queued with the row above rather than patched at the end of a run.

---

## Return rate

Unchanged and unmeasurable by design — no tracker, nothing to report, and no estimate offered. The
reader-cost baseline this function keeps instead moved today for the first time since 2026-10-25:
**−33,736 bytes on every page whose only display-face accent was the one in our own name**, measured on
four of six probed pages, with the corpus-wide figure declined rather than guessed.
