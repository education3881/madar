# Ruling #56 — a convenience answer is not the index

**Filed:** 2026-09-18 · **Status:** binding · **Section 1, row 51**
**Earned on:** a deploy that failed on a truthful date, and a document declared unreadable
that four archives were holding the whole time. Same day, same shape, two instruments.

---

## The rule

**When an instrument can answer either with *a* representative case or with *the whole
set*, and you ask the cheap question, you get a well-formed answer to a narrower question
than the one you meant. Read the index, not the summary — and when the summary is all you
have, record which endpoint you asked, because the next run cannot tell from the
conclusion.**

The danger is not that the convenience answer is malformed. It is that it is *perfect*: a
single snapshot, correctly dated, correctly marked 200; a single ceiling, correctly
derived from real commits. Nothing about either output says "there are four more of me"
or "I do not govern that URL." A representative answer read as a complete one produces a
**confident** wrong conclusion, and confidence is what stops the next question being asked.

---

## Origin case A — the archive that said nothing was archived

Source 9 of Edition 05's slot 3 is the Educ'Action interview with CONFEMEN's
secretary-general: the register **ruling #49 was earned on**, cited by number in four
artefacts. Its publisher died — `eduactions.org` answers 404 on every path *including its
root*, which is #54's fourth signature and the one that inverts #54's own prescription.

On **2026-09-17** the run asked the Internet Archive's **availability API**
(`archive.org/wayback/available?url=…`). It returned one snapshot: captured
**2025-04-27**, marked 200. The body could not be read on four routes. The verdict
recorded the honest-looking conclusion — *a snapshot known to exist and unreadable today,
a third state, distinct from both "archived" and "gone"* — and put three options to the
Editor, one of which was **retiring the demonstration ruling #49 stands on**.

On **2026-09-18**, from a different runner, the same availability API returned:

```json
{"url": "https://eduactions.org/3-questions-au-…-internationale/", "archived_snapshots": {}}
```

**Nothing.** For a URL whose capture history is a fact about the past and cannot change.
That alone disqualifies the endpoint as an index: an index does not have moods.

The **CDX index** (`web.archive.org/cdx/search/cdx?url=…`) — the archive's actual,
enumerable holdings — returned **five captures of the same address**:

| capture | bytes |
|---|---|
| 2023-03-27 | 30,634 |
| 2024-02-25 | 29,631 |
| 2024-09-14 | **1,281** |
| 2024-12-05 | 33,123 |
| 2025-04-27 | **5,201** |

Three of the four substantial captures were fetched and read **in full** today, on the
first attempt, through the ordinary playback path. The document was never unreadable.

**And note *which* one the convenience endpoint handed over.** The availability API
returns the capture *closest to the requested time*, which defaulted to the most recent —
**the 5,201-byte outlier**, a fifth the size of its neighbours. The endpoint was not
wrong. It answered "what is the nearest capture?" perfectly, and was read as answering
"what does the archive hold?" The one question it was asked is the one question whose
answer was useless.

**What it nearly cost.** A ruling's origin register retired; a piece's closing
demonstration removed; and a dead-link disposition recorded as *carried on our word*. The
read, once made, did not merely confirm #49 — it strengthened it. The bounding clause
« Avant 2030 qui est le point final de l'ODD4 » sits in the sentence after the headline's
superlative, and the entire answer is given **in reply to the question « Quel est
l'accent mis sur 2030 ? »**. The headline did not drop a qualification; it dropped the
subject being asked about. Nobody could know that without the body.

---

## Origin case B — the ceiling that governed two branches of three

`qa_lastmod` is the output-side twin of `sitemapLastmod.mjs`. The resolver has **three**
branches: article pages (max of their own content file and chrome), the `/valence/` static
page (its own file under `web/public/`, and nothing else), and the index pages (chrome and
the newest approved article). The check computed **one** ceiling —
`max(newest approved content commit, newest chrome commit)` — and applied it to every URL.

That bound is correct for two branches and describes the third not at all: `web/public` is
in neither content nor chrome.

On **2026-09-17** commit `bd3c48e` edited `web/public/valence/index.html` — the #55 Arabic
fix, applied to the one page the build does not style. The page's served bytes genuinely
changed. The resolver emitted the truthful date. **The check failed the deploy**, and the
whole of the 09-17 work — ruling #55, assertion 17, the slot-3 verification verdict — sat
on `main` unserved for a day, for a defect in the instrument and not in the site.

The half nobody had noticed is the reason this is a **strengthening**: under one global
ceiling, `/valence/`'s date was only ever tested for being too *large*. Any value below
the ceiling passed, including a date with no relationship whatever to the file the page is
built from. **The one URL the check failed on is the one URL it had never actually
checked.** Proved by construction: with a scratch commit raising the chrome ceiling above
valence's file date, a fabricated `/valence/` lastmod between the two prints **PASS** on
the old check and **DEFECT** on the new one, in the same breath.

Fixed by deriving the ceiling **per URL, from the same rule the resolver uses**, with the
static set discovered from the filesystem rather than named in the check — so a second
static page inherits the bound without anyone remembering to add it (#36). Not by widening
the global ceiling to include `web/public`: a held piece's hero still and share card live
under `web/public/stills` and `web/public/og`, and a ceiling that rose with them would
rise every time a held draft was touched, re-opening the exact leak (`9886987`, `642fef2`)
the file was written to close. **Widening a bound to admit one honest case admits every
dishonest one that shares its address.**

---

## Why these are one ruling

Both are an instrument answering a narrower question than the one asked, in a form that
does not advertise the narrowing:

* *"Is this archived?"* answered by **one nearby capture**, read as the holdings.
* *"What is the newest thing this site could honestly claim?"* answered by **the bound for
  most pages**, read as the bound for all of them.

And both were invisible for the same reason: **a representative answer is well-formed.**
There is no error to notice. The 09-17 run did nothing careless — it probed four routes,
recorded its failures by layer, and named a new state honestly. It asked the wrong
endpoint, once, and everything downstream inherited the narrowing.

**Family placement.** The enumeration family has asked, in order: what can this check not
*see* (08-16 → 09-06)? is its bite *real* (#35)? which *artefact* did it read (#52)? at
which *layer* (#55)? This one asks the question underneath all four: **which question did
the instrument actually answer?** #52's nearest sibling — #52 says an instrument that
cannot name the artefact it read is worthless; this says an instrument that cannot name
the *question it answered* is worse, because it looks like it answered yours.

---

## Binding corollaries

1. **Before concluding a document is gone or unreadable, query the index, not the
   availability endpoint.** For the Internet Archive that is the **CDX API**. #54's
   procedure gains a step: *publisher root → search by headline → **enumerate the
   archive's captures** → read one.*
2. **When several captures exist, prefer the one whose size agrees with its neighbours**,
   never the one nearest in time. A capture a fifth the size of its siblings is a failed
   crawl, and "most recent" is not "most complete."
3. **Repeat the probe on a different day and a different client before recording a
   refusal as a fact about the world** — #20, and today's disagreement with yesterday's
   API is its cleanest vindication yet.
4. **An assertion that twins a function twins every branch of it.** Before writing the
   check, enumerate the branches from the function's own source and say in the check which
   branch governs which input. A twin that models the common branch passes for the common
   case and fails, *wrongly*, on the branch it forgot — which is the worst failure an
   assertion has, because it looks exactly like a defect in the thing being checked.
5. **Never widen a bound to admit an honest case.** Narrow it per input instead. A bound
   widened to let one true thing through lets through everything else at that address.
6. **A conclusion drawn from a one-shot endpoint carries the endpoint's name in the
   record**, so a later run can tell what was actually asked rather than re-deriving it
   from a conclusion.

---

## Amendment, filed here rather than numbered — the oracle that could not run

Not a separate rule; a consequence of one, and it needs to be findable.

The 09-17 QA log carried a forward question and named a candidate oracle for it: *render
one known Arabic string and measure its advance width against the same string with
`letter-spacing` forced; if the two widths are identical the font is not shaping.* Tested
on 2026-09-18 **before anything was built on it**, and it fails on a perfectly healthy
page, twice over:

1. **It cannot run on this site at all.** Ruling #55's own fix — filed the same day, in
   the same artefact — is `:lang(ar){letter-spacing:normal!important}`. Tracking can no
   longer be forced onto an Arabic element here. Measured: forced-tracking width equals
   natural width **to the pixel** on all four probe strings. The proposed check would read
   its own failure condition on a correct page.
2. **The inference was wrong anyway.** Forcing tracking widens a shaped run and an
   unshaped one alike, so the comparison measures tracking, not joining.

**A rule and the instrument proposed to succeed it were written hours apart in the same
log, and they are incompatible.** Nobody was careless: the fix was composed in the
cascade's vocabulary and the oracle in the renderer's, and neither author was the other's
reader. The general form: **a forward question is a hypothesis, not a work order.** The
09-13 rule already says the next run *tests* the named surface before adding anything new
— today is the first time testing it returned *no*, and the practice is vindicated by
exactly that. A named candidate implemented on trust would have shipped a check that fires
on every correct build.

The oracle that does work — compare the run against itself with **U+200C ZERO WIDTH
NON-JOINER** between every letter pair, which is the known-unshaped case by construction,
in the same font on the same page — is standing **assertion 18** (`qa_arabic_joining.py`),
landed and gated today. A second finding from the same bench, recorded because it is the
kind of thing that gets rediscovered: **`مدار` is a bad probe string.** Dal and alef do not
join leftward, so a correctly shaped `مدار` measures 0.972 of its own de-joined self and no
threshold can tell it from a broken one, where `بببب` measures 0.433. *The probe is chosen
for joining density, never for being ours.*

---

## Related

[[2026-09-17-a-property-of-the-content-is-not-a-property-of-the-component]] (#55) ·
[[2026-09-16-a-404-is-not-a-death-certificate]] (#54) ·
[[2026-09-15-a-claim-inherits-the-scope-of-its-register]] (#51) ·
[[2026-09-14-a-superlative-has-a-horizon]] (#49)
