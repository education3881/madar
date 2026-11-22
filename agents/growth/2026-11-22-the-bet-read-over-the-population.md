# The 2026-11-15 bet, read on its due date over 143 documents instead of 6

**Read 2026-11-22 at the weekly review. Standing-queue item 117.** The reading is repeatable:
`python3 agents/tools/font_payload_population.py . --json agents/stats/2026-11-22-font-payload-population.json`,
81 seconds, no network, no credential. The register it wrote is committed beside this note.

## What the bet asked, and the first honest answer is about the bet's own wording

> *"The reading is two numbers on 2026-11-22: documents measured (**target 138 of 138**) and total bytes
> across the corpus spent on woff2 files that paint fewer than five characters, with the worst page named."*

**Documents measured: 143 of 143.** Not 138 of 138 — and the difference is not a miss, it is the target
having been a **literal about a moving population**. The corpus was 138 served documents when the bet was
written on 2026-11-15; two pieces have shipped since (`bahrain-bqa-five-cycles` 11-09 is before that line,
`england-ofsted-exempt-cohort` 11-21 is after) and the growth function added browse routes on 11-22. A bet
that states its denominator as a number rather than as *the population* is the same defect as
`CLAUDE.md`'s cap-death count, which this same review has now corrected for the third time in fourteen
days. **Every served `.html` in `dist` was rendered; the population is whatever that set is on the day.**

## The second honest answer is that the bet's stated technique could not have worked

The bet was set on `qa_selector_coverage`'s method — *one browser launch over `DOMParser`, 135 documents in
1.9 s* — and said *"nothing new has to be invented; the population just has to be asked."* **`DOMParser`
cannot answer this question at all.** A parsed document has no network stack and no layout engine, and a
woff2 file is transferred only when a layout engine must paint a glyph out of it. The quantity does not
exist in the parse tree; it exists only at render time, which is assertion 39's whole reason for being the
thirty-ninth and not a variant of the other thirty-eight.

So the population had to be **rendered**, 143 times, with its requests logged: **81 seconds**, which is
cheap enough to re-read weekly and far too slow for a build step. *A bet can be fully owned and still be
costed wrong — ownership was the test the bet passed, and the technique was never checked against the
quantity.*

## The reading

| | |
|---|---|
| Documents rendered | **143 of 143** served `.html` in `dist` — **23.8×** assertion 39's six-page sample |
| Corpus font payload | **54,903,800 bytes** summed over every document *(an exposure, not anybody's bill — a reader who opens one page pays that page's line)* |
| Fetches painting fewer than 5 characters | **54**, totalling **3,989,640 bytes** — **7.3%** of the corpus payload |
| Pages carrying at least one | **48 of 143** |
| Fetches painting **ZERO** characters | **0** |
| Worst single ratio | **86,608 bytes for ONE character**, `newsreader-normal-400-600var-latin-ext.woff2` on `/browse/region/europe/` |
| Worst page by wasted bytes | **195,168** on `/browse/region/europe/`, in two fetches |

### The best result is the one the bet did not ask for: zero dead fetches on the whole population

`qa_font_payload` limb 2 — *every fetched woff2 is justified by a glyph the page paints* — is **asserted on
six pages** and has never been read on more. It is **green on 143**. The 2026-10-17 defect class (146,872
bytes fetched to paint nothing) does not exist anywhere in the served corpus. That is the answer
standing-queue item 123 asks for about this gate, obtained by widening the population rather than by
trusting the green, and it is the one number here that an assertion could now safely stand on.

### The largest class is the bilingual chrome, and it is 28% of everything

`amiri-normal-400-arabic.woff2` is fetched on **142 of 143 pages** — **15,415,520 bytes, 28.1% of the whole
corpus payload.** On **22 of those pages**, all under `/browse/country/`, it paints **exactly four
characters at 27,140 bytes each**, and those four characters are **مدار** — the Arabic half of the
wordmark. 2,388,320 bytes, **60% of the whole sub-five-character total**, for one word of brand chrome on
pages whose visible content is otherwise entirely Latin.

### And item 116's character is still in the served bytes, five days after item 116 closed

`newsreader-normal-400-600var-latin-ext.woff2` is fetched on **12 pages for 1,039,296 bytes**, and on
**three of them it paints ONE character**. The character is **`ā`, U+0101** — item 116's character, in item
116's chrome. That row was closed on 2026-11-17 by a repair whose equivalence was proved four ways before a
byte moved (advance-width delta 0.000px in three faces, zero differing pixels at 8×), and the repair was
correct: the **display** wordmark now carries `a` + U+0304. What still carries the precomposed form is the
text beside it — `Madār · مدار` and the wordmark's own accessible description, *"Madār bilingual wordmark.
Latin letters beside…"* — which no reader looks at and which `SiteFooter.astro` line 83 explicitly warns a
future editor not to "correct".

*A correction reaches the instance it was sent to; only an instrument reaches the class.* Item 116 was
closed on the instance the eye could see. This is the first time the class has been counted.

### The limit of this instrument, stated rather than discovered later

This reading logs **requests** and counts **painted runs**; it cannot say **which run caused which
request**. So the attribution above — *this fetch is here because of the wordmark* — is an inference from
co-location, not a measurement. Proving it needs the repair: change the chrome, re-render the population,
read the delta. That is what makes next week's bet a repair-and-re-read rather than a diagnosis, and it is
why the before-numbers are pinned here in a committed register rather than quoted in prose (#136: *a
literal is a measurement that has stopped being taken*).

## Verdict on the bet

**Read, on its due date, by the operation that set it, with no credential and no third party — and it was
read seven days after it was set rather than seven days late, which is what the 11-15 review built item
117 to guarantee.** The bet's own prediction about its *method* was wrong and its own *denominator* was
stale; both were caught by taking the reading rather than by re-reading the sentence. The numbers it asked
for exist, they are in a register, and the instrument that produced them is committed.
