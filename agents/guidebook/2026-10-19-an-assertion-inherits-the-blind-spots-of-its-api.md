# An assertion inherits the blind spots of the API it measures through

**Ruling #108 · filed 2026-10-19 · QA lane, the standing queue's own head (item 12, 7 days,
seven displacements, the oldest item past the three-displacement threshold)**
**Family: assertion discipline / build determinism — the family's thirty-sixth member.**

---

## What was asked

Standing-queue item 12, opened 2026-10-12 by that day's forward question: **no founder-facing
artefact has ever been checked for LAYOUT.** The 2026-08-23 perimeter rule put the briefs, the
weekly reviews and the memos in scope, and three things have been asserted about them since —
that they **exist**, that they carry a **container**, and (from 2026-10-12) that they **contact
nobody**. All three are properties of the markup. None is a property of the render.

The item named two bites and both were already in hand: Brief No. 01 rendering with a column one
word wide for 137 days, and the 2026-10-12 brief stopping dead after the statistics panel because
a pasted CSS comment was opened and never closed.

## What was built

`agents/tools/qa_artefact_render.py` — standing assertion 33, gated from `postbuild`, which
renders all **127** briefs and weekly reviews in one headless Chrome at a stated 1280px viewport.
Two measurements. **One of them gates and the other deliberately does not, and that split is this
ruling.**

* **A — the tail renders. ASSERTED, 127 of 127 clean, nothing excused.** Two direct oracles: no
  comment node in the rendered DOM carries a closing tag, and the render carries at least 90% of
  the source's own visible characters. Thinnest real margin across the corpus: **98.8%**.
* **B — nothing overflows its container. MEASURED, PRINTED, NOT ASSERTED.** It found **25 of 127
  artefacts overflowing**, in two diagnosed mechanisms, and it is **blind to the mechanism it was
  commissioned for.**

## The finding

**`scrollWidth` does not grow for inline text overflowing an `overflow: visible` block in
Chrome.** Measured, not reasoned: a `white-space: pre` paragraph carrying the 100-character push
command was injected into a clean brief, and the element reported `scrollWidth == clientWidth ==
1028` for text far wider than 1028px, with `documentElement.scrollWidth` unmoved at the 1280px
viewport. The probe saw nothing.

Which means the 25 it *did* find were found for a reason it was not designed around:

* **Seven briefs (2026-08-10 → 08-18)** render the founder's copy-paste push block in `<pre
  class="push">` with `white-space: pre`, and `cd "/Users/vini/Documents/..." && git add -A && …`
  does not wrap. Those documents are **7,277 to 34,254 px wider than the viewport** — the worst
  layout defect in this operation's record, in the artefact the CHARTER names as the
  proof-of-work contract, unseen for 62 days. They were caught because the overflow propagated
  to the document, not because any element reported it.
* **Seventeen briefs (2026-05-28 → 06-17) and one review** set `li { display: grid;
  grid-template-columns: 1.5rem 1fr }` for a hanging bullet. **Grid blockifies its children**, so
  a `<strong>`, `<code>` or `<span class="mono">` written inline inside such an `<li>` becomes its
  own grid item and is auto-placed into the **24px bullet column**, where its text overflows by 11
  to 190px. This is Brief No. 01's "right-hand column one word wide", and the mechanism is the
  same in all eighteen. They were caught because **grid-item** overflow is a thing `scrollWidth`
  does report.

So the instrument finds a real and previously unmeasured defect class, and its sensitivity to the
class item 12 commissioned it for is **unknown**. A check that cannot be shown to fail on the
defect it exists to catch does not gate a build (CLAUDE.md non-negotiables: *prove an assertion
both ways*). It reports, with its blind spot printed beside its findings on every call — the
`qa_third_party_origins` pattern, where `<a href>` and `og:image` are counted, printed and not
asserted with the reason in the output.

## The ruling

**An assertion does not measure its subject. It measures its subject through an API, and the API
has a scope exactly as a check has a scope.** Six times this operation has written down *a green
check is scoped to what it enumerates* (#18 inversion, #33 chrome, #34 orphan, #38
consumer-format, #40 brief perimeter, #77). Every one of those asks what the check **looked at**.
This asks what the check's **ruler is capable of representing** — and a ruler's blind spot is
worse than a scope gap, because a scope gap is visible in the code that enumerates and a blind
spot is visible nowhere at all. `el.scrollWidth` is a plausible, idiomatic, widely-recommended
overflow oracle. It returns a number. The number is silent.

Binding:

1. **A render assertion names the API its oracle rests on and states what that API cannot
   represent**, in the tool's own header, beside its findings — not in a log nobody re-reads.
2. **An oracle is proved on an injection, never on the corpus.** Finding real defects in the
   existing population is not evidence of sensitivity: this probe found 25 and would have missed
   all seven of the worst if their overflow had not happened to propagate to the document.
3. **Where an oracle's sensitivity is unknown, the measurement is printed and not asserted**, and
   the correct oracle is queued by name rather than described as a limitation. Here that is the
   **Range rectangle** — `doc.createRange()` over an element's contents, measuring
   `getBoundingClientRect().right` against the element's padding-box edge, which is a geometric
   question the layout engine must answer honestly. **Standing-queue item 28.**
4. **The four render-class assertions already gating this build rest on oracles nobody has
   interrogated** — `qa_render` reads a raster, `qa_arabic_shaping` and `qa_arabic_joining` read a
   dumped DOM, `qa_feed_direction` reads a rendered feed. Each is now owed the question this
   ruling asks. That is the forward question this run hands on.

## Three oracle errors in one tool, and the harness caught all three

Recorded because the pattern is the ruling in miniature, and because every one of them read as a
pass:

* **The expected tail was derived from the broken artefact.** The first version of `source_text()`
  used Python's `html.parser`, whose recovery from an unclosed comment is the same as a browser's
  — it swallowed the document's tail too. So expected and rendered agreed perfectly, the bite
  passed, and the check read **green on the exact defect it was written for.** This is the
  2026-09-14 trap on the input side: *where does the string I am looking for also legitimately
  appear?* A browser cannot be naive about comments. **A ruler must be**, and the function now
  strips closed comments only, on purpose and with the reason written above it.
* **`textContent` is not what a reader sees.** The text-loss oracle first measured
  `body.textContent`, which **includes the text inside a `<script>` element** — so an unclosed
  `<script>` that swallows the rest of the document measured **117.8% of source**, longer than the
  source. Switched to `innerText`, the same bite measures **53.2%** against a 90% floor.
* **A void injection.** One bite's anchor (`<section` in the document's second half) did not exist
  in the template, so the injection silently did nothing and the check passed. The harness's own
  `changed()` guard — assert the injection changed the file before running the check on it —
  reported **"INJECTION DID NOT CHANGE … bite is void"** and refused to count it. That guard
  exists because of 2026-09-14 and it earned its place again today.

**Proved 18 ways, zero failures, exit code read directly rather than through a pipe** (the 10-17
slip). Control: the lab corpus clean, exit 0. Bites: the real unclosed comment; the same deletion
with no comment node at all; the blind spot itself, asserted to *stay* blind so the next run does
not re-derive it and so the header cannot go quietly stale; a baselined artefact that stops
overflowing, which must be named for deletion; no browser, which must REFUSE with exit 2 rather
than pass; an empty corpus, which must REFUSE rather than report 0 of 0 clean.

## What this does not close

The repair of the 25. It is markup and type surgery on historical artefacts nobody has looked at,
and the right hand for it is the Web Developer with the Designer — **standing-queue item 27**, not
an assertion's to make quietly. The membership list of 25 is kept in the tool beside the number,
because a count with no membership list is this operation's oldest recurring defect (#57), and a
member that stops overflowing is named for deletion so the list can only shrink.
