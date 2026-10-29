# Madār (مدار) — repository guide for Claude

This repository **is** the publication and **is** the operation. There is no state
outside it: the editorial charter, the operating rules, the accumulated rulings, the
content in both languages, the QA tools and the daily briefs all live here. A run that
reads this repository has everything it needs.

Read on every run, in this order:

1. `agents/CHARTER.md` — the operating mandate. The five standing functions.
2. `agents/RUNBOOK.md` — the accumulated procedural rules. Long, and load-bearing.
3. The most recent `agents/briefs/*.html` — yesterday's artefact, **not** today's state.
4. `content-drafts/_EDITION_05_STATUS.md` — **the closed-edition record. Edition 05 flipped 2026-10-13
   and there is no live edition.** The file is 5 KB: what shipped, the one item still owed, the standing
   prohibitions, and a pointer. Its 194 KB working ledger was archived on 2026-10-16 under standing-queue
   item 9, because this list had spent three days telling every run to read a shipped wave's history
   before planning. **Standing rule: a wave's status memo is reduced to its record in the flip commit's
   week, and this line names whichever edition is open** — if that is a closed one, the line is stale
   and the run that notices fixes it. **A dated section inside a working ledger is history, not state**
   — read the Log and the newest `RECONCILED AGAINST DISK` block before planning from any section above
   them. A run on 2026-10-04 reported three closed items as open because it read the 09-27 section,
   which was eleven screens above the entry closing them.
5. `agents/logs/WEBDEV-QUEUE.md` — **the operation's one standing queue, and from 2026-10-04 its head is
   binding** (RUNBOOK, *one queue, one head*). **Its ordering was replaced on 2026-10-25 by ruling #116:**
   rows sit in three buckets, and **the head is the oldest DEFECT if any DEFECT is open, otherwise the
   oldest OPEN**. A **DEFECT** names N > 0 artefacts, served or founder-facing, that are wrong **now**; a
   **BLOCKED** item needs a credential, a purchase or a word nobody here holds and is **out of the ordering
   entirely**, read at the weekly review only; everything else is **OPEN**, and the previous run's forward
   question enters at OPEN's head. **Age is `today − Raised` and is NOT written in the row** — the Age and
   Displaced columns were two copies of one derivable number and fifteen of eighteen were stale the day they
   were deleted. The three-displacement threshold is **retired**: it equalled age on every row, which is why
   the tiebreak needed its last rung on 10-25. The run still writes one line naming which head it took and
   what it displaced. **This file is in this list because a binding queue nobody is told to
   read is the same defect as a count nobody is named to maintain.**

## What this publication is

Madār is a bilingual (English + Arabic) publication about early-childhood and K–12
education, written for educators, parents and education regulators. Every piece stands
on **named primary sources read in served text**. The Arabic edition is *composed*, not
translated. Nothing ships without clearing the Editor's five-test rubric in writing.

## Non-negotiables

- **Verify state before planning.** Never plan a day off a brief. Check `git log`,
  compare local against `origin/main`, check `git status`, and confirm the live site.
  Name any missed day plainly. (`agents/guidebook` — state verification.)
- **Quality over slot.** Hold a piece rather than ship it thin. The Editor is the
  filter and the Manager never overrides a park.
- **Held pieces are invisible.** `approved: false` means the piece contributes no
  page, no sitemap entry, no feed item, no `lastmod` date and no bytes. Four standing
  assertions enforce this; do not weaken them.
- **A figure is cited as read.** Never composed from a pattern, never averaged across
  registers, never carried from a search summary. See the ruling register in
  `agents/guidebook/INDEX.md` — currently **#1–#120**, and binding. **This range is
  ASSERTED, not remembered:** standing assertion 30, `qa_register_shape`, derives it from
  §3's own rows and fails the build when this sentence disagrees with them. Do not hand-edit
  it to match a memory; file the ruling and let the gate tell you the number.
  *(A filing run moves four counts always — §3's range, §3's heading, §1's count line and
  this one — plus a conditional fifth when the ruling joins a register family that keeps a
  running member count. The rule, both its amendments and the reasoning that earned them are
  in the RUNBOOK; the day-by-day record of every move this line made between 2026-09-20 and
  2026-10-08 is archived at `agents/guidebook/ARCHIVE-2026-09-20_2026-10-08-ruling-range-moves.md`.
  It was moved out of this file on 2026-10-10 under **ruling #94**, because 7,650 bytes of
  audit trail for a number a gate now maintains is a cost every run pays before it can do
  any work — and on 2026-10-09 that cost took the whole run.)*

- **The run has an envelope, and it can see itself approaching HALF of it.** `madar-daily.yml` and
  `madar-weekly.yml` pass **`--max-turns 180`** and set **`timeout-minutes: 90`**. Both numbers live in
  `.github/workflows/**`, which this identity cannot write, so they are recorded here — **and recording a
  number is not measuring it.** From 2026-10-18 the measurable half is measured: `python3
  agents/tools/run_envelope.py .` parses both numbers out of the workflow file and reports elapsed and
  remaining **wall clock** against the run's own `run_started_at`, readable with the `actions: read` grant
  the job already holds. **That half was observable from inside for the five runs that believed the whole
  envelope was dark** (ruling #105). The **turn** axis genuinely is dark — nothing in the agent step counts
  turns — and the tool prints it as UNMEASURABLE on every call, because a green clock is not a green
  envelope: the run that lost 10-11 to `error_max_turns` had minutes to spare. **Commit and push
  at the close of every standing function — never once at the end** (RUNBOOK, ruling #96). On 2026-10-11
  the daily run spent 181 turns doing a full day's work, including the Edition 05 gate judgment that was
  the edition's last blocker, and delivered **nothing**: one turn past the cap cost the whole day, because
  the only commit was planned for the end and no disk survives the run. A staged block is not a waiting
  block; it is a lost one.

- **Prove an assertion both ways.** A new check must be shown to stay silent on a
  known-good control *and* to fail on the defect it exists to catch. Prove the bite as
  carefully as the control: an injection that fails to change the artefact reads
  exactly like a passing control.
- **Never invent a traffic number.** The site carries no third-party tracker by
  design. Say so rather than estimating.
- **Count against the population, never against yesterday's number.** Ruling #57, earned four weeks
  running. A count that agrees with itself every day can disagree with the thing it counts for a
  month: the assertion-discipline family's member count was arithmetically perfect for five
  consecutive filings and wrong by three the whole time, because the rule that moves it was written
  after three members had already joined. **A point-of-filing rule fixes a count's future and leaves a
  step discontinuity where it was written; it never reconciles backward.** And count the *shape* too —
  five rows of the canonical ruling register carried three columns in a four-column table while every
  row count and range check ever run on it passed (2026-10-04).

## Layout

| Path | What it holds |
|---|---|
| `web/` | The Astro site. `src/content/articles` (EN) and `articles-ar` (AR). |
| `agents/` | CHARTER, RUNBOOK, guidebook (rulings), briefs, logs, growth notes, tools. |
| `agents/tools/` | **Thirty-nine** standing QA assertions plus `madar_stats.py`, `build_font_bundle.py` (a generator) and `lastmod_tree_guard.py` (a **precondition** shared by the two instruments that compare a `<lastmod>`, added 2026-10-15 closing standing-queue item 8 — it refuses a comparison between a git-derived date and a working-tree build, exit **4 = REFUSED**, and it is not an assertion because the count globs `qa_*.py` and a precondition fails no build on its own) and `run_envelope.py` (added 2026-10-18 closing standing-queue item 11 — **where this run stands against the envelope in the two lines above**, parsed from the workflow file and never copied, with the wall clock measured from `run_started_at` and the **turn axis printed as UNMEASURABLE** so a healthy clock cannot be read as a healthy envelope; exits 0 / 3 = BANK NOW / 2 = cannot measure / 4 = REFUSED, and `--log` accumulates each function's cost in `agents/stats/run-envelope.jsonl`). Python 3, no deps — except `qa_render.py`, `qa_arabic_shaping.py`, `qa_arabic_joining.py`, `qa_feed_direction.py` and `qa_font_payload.py`, which need a headless Chrome, and `qa_claim_registers.py`, whose gated `--check` half is offline and deterministic while its ungated `--emit` half asks an archive about every register this publication cites. |
| `content-drafts/` | Recon, commissions, verdicts, edition status memos. Not published. |
| `.github/workflows/` | Deploy (`astro-pages.yml`) and the autonomous runs. |

## Build and QA

```bash
cd web && npm ci && npm run build            # must exit 0; the TWENTY-FOUR postbuild gates run here
cd web && npm run gates                      # the TWELVE workflow build steps, alone (postbuild runs them too)
python3 agents/tools/qa_pair_frontmatter.py .     # reads SOURCE files, held pieces included
python3 agents/tools/qa_patch_queue.py .         # prints the whole gate register, derived
python3 agents/tools/madar_stats.py --log        # regenerates the brief's stats panel
```

**`npm run build` is TWO-THIRDS of the gate set, and a green postbuild reads exactly like a green deploy.**
Twelve of the thirty-five gating assertions are steps in `astro-pages.yml`'s build job and run nowhere
else; `npm run build` runs the other twenty-four. **On 2026-10-20 that cost a day of publication**: the growth
function shipped 80 dangling JSON-LD `@id`s, `qa_jsonld` failed the build job, deploy and verify were
skipped, and the origin served the 10-19 build for two days while five commits sat on `main`. The run
built four times and called the gates green. `npm run gates` →
`agents/tools/build_job_gates.py` closes it: it parses the twelve out of the workflow file and runs
them, derived rather than copied — **and the line above it in this file said eleven, because a list in
prose is maintained by nobody.** It is a **runner, not an assertion** (the count globs `qa_*.py`, so the
register still reads 39 / 12 / 24 / **36 of 39** — these twelve always gated the deploy; what changed is
where they can be *reached*), and **it is wired into `postbuild`**, closing standing-queue item 30 the
same afternoon it opened: a runner somebody must remember is 2026-09-13's *a habit, not a gate*. The cost
was assumed and then measured — **twelve gates in 1.88 s, a full build with all thirty-two in 32 s** —
and proved by **re-injecting the 10-20 regression**, which now turns `npm run build` red on this machine
where it exited 0 four times that day. **From 2026-10-21 a green local build is the deploy's own gate
set**, so the second command below is a diagnostic rather than a duty.

Use `npm run build`, not `npx astro build`: **twenty-four** of the thirty-nine assertions
(`qa_css_tokens`, `qa_render`, `qa_arabic_shaping`, `qa_arabic_joining`, `qa_stable_order`,
`qa_date_identity`, `qa_feed_enclosures`, `qa_feed_direction`, `qa_chrome_links`, `qa_census`,
`qa_packet_figures`, `qa_pair_frontmatter`, `qa_patch_queue`, `qa_served_manifest`, `qa_register_shape`,
`qa_third_party_origins`, `qa_bridge_coverage`, `qa_artefact_render`, `qa_composition`, `qa_claim_registers`, `qa_citation_identity`, `qa_acronym_evidence`, `qa_annotation_figures`, `qa_font_payload`) are gated from `postbuild` in `web/package.json`,
because an autonomous run is refused write access to `.github/workflows/**`. **`qa_packet_figures`
is the first gate that is not handed `dist`** — it takes the repository root, because a
distribution caption is never built; it is in `postbuild` because that is where a gate this
identity can wire lives, not because it has anything to do with the build. **`package.json`
is a second, equal home for gates** — a reader asking "what gates the deploy?" must read both
files (issue #6, default C applied 2026-09-20).

**The build must run in a full git checkout** (`fetch-depth: 0`). The sitemap's
`lastmod` resolver reads file dates out of git history and fails loudly — correctly —
in a shallow clone. This bit us once already; do not "fix" it by weakening the guard.

`.github/workflows/astro-pages.yml` runs twelve assertions as build steps, twenty-four more
arrive through `postbuild`, and then a `verify` job byte-compares the published
artifact against the live origin. **36 of the 39 gate the deploy**; of the three that do
not, two (`qa_live_drift` — the `verify` byte-compare is strictly stronger;
`qa_sources_alive` — someone else's 404 is not our build's failure) say why in the
workflow file. **The third, `qa_feed_validators` (added 2026-09-24), is the first whose
reason cannot be written where the others are** — it belongs in the `verify` job and this
identity cannot write `.github/workflows/**`, so its reason lives in the tool's own header
and the one-line patch is staged at `agents/patches/` — **one home for the patch queue, moved
there 2026-09-27** when the weekly review found the queue split across two directories with
this file naming one and issue #7 naming the other. Applying that patch makes it
**37 of 39**. A green run means the bytes are actually served, not merely built.

**A staged patch is frozen prose about a moving count (2026-09-27).** The queued issue-#6
patch sat unapplied for seven days asserting *21 assertions, 19 gating, seven from
`postbuild`* while four assertions landed; applying it on any day after 09-22 would have
written stale counts into `astro-pages.yml`, where this identity could not then correct
them. Every open patch is now re-read against current state at each weekly review and
refreshed or withdrawn. The counts in this section were re-verified **2026-09-29 by counting
both files** — twelve build steps in `astro-pages.yml`, twelve `postbuild` entries in
`web/package.json`, twenty-seven tools in `agents/tools/`, and the three non-gating ones named
below. They moved that day with assertion 27, `qa_patch_queue`, at the point of filing, **and again on
2026-10-01 with assertion 28, `qa_pair_frontmatter`** — thirteen `postbuild` entries, twenty-eight tools,
25 of 28 gating, all three derived by `qa_patch_queue` rather than counted by hand. `qa_pair_frontmatter`
is the **second** gate not handed `dist` and the second to read `web/src/content/**` directly, because a
held piece is not built and the six held pieces are what the next flip commit serves (ruling #81).
**They moved again on 2026-10-25 with assertion 39, `qa_font_payload` (ruling #115, standing-queue
item 20 closed at 8 days and seven displacements, by the tiebreak's fourth and LAST rung — items 20 and 21
tied on age and on displacements and shared a raising commit, so raise order decided it)** — **twenty-four**
`postbuild` entries, **thirty-nine** tools, **36 of 39 gating**, all three derived by `qa_patch_queue` rather
than counted by hand. **It is the first assertion whose subject is a quantity that is not in `dist` at all.**
Every one of the other thirty-eight reads a byte that EXISTS; a woff2 is transferred only when the layout
engine must paint a glyph out of it, so what a reader actually downloads is a product of the page, the
cascade, the `unicode-range` carve and the browser's matching — and it exists nowhere until render time.
Two defects of the class were found by hand eight days apart in one lane: **2026-10-17, 146,872 bytes
fetched to paint nothing**, and **today, 131,100 bytes to paint 29 characters**, because two `<em>` tags
slanted Arabic on both home pages. The stylesheet had already said *Arabic is not slanted* twice, both
times per component, so neither reached the third instance; **one rule took the Arabic home page from
426,728 to 295,628 bytes, −30.7%.** Limb 1 (no slanted Arabic) and limb 2 (no dead fetch) are asserted;
payload totals, fetches justified by punctuation alone, and the **89 painted Arabic runs whose own stack
names no bundled Arabic family** are measured and NOT asserted, because a floor above today's reality reds
every build (#93's reasoning). Three controls green, bite 1 red on both limbs — **and bite 2, the real
10-17 defect restored exactly, did NOT bite**: the Arabic strapline ends in a full stop and U+002E is inside
every Latin subset, so those 146,872 bytes were never a dead fetch but a fetch justified by the cheapest
glyph in the file. *A bite aimed at a real published defect is the only one that can tell you where the
limb's edge actually is.* Previously moved on 2026-10-24 with assertion 38, `qa_annotation_figures` (ruling #114, standing-queue
item 19 closed at 8 days and seven displacements)** — **twenty-three** `postbuild` entries, **thirty-eight**
tools, **35 of 38 gating**, all three derived by `qa_patch_queue` rather than counted by hand. **It is the
first assertion whose subject is the OPERAND every other citation instrument takes as given.** Four
instruments compare something against the `sources[]` annotation and nothing had ever compared the
annotation against anything; every numeric check this operation owns reads a **body**, and the annotation
block is **served**. So a figure printed only in an annotation is a published figure outside all of them:
**2,026 annotation quantities, 423 in no body of either edition, across 40 of 44 pieces** *(restated 2026-10-24 by the content function's licence a2, from the 2,033 / 430 the ruling was filed with)* — and the 19 that
the pair rescues are #42 on a figure, prose in one edition and a citation in the other. Item 19 asked for a
classifier and the classifier was unnecessary, because **a digit is an exact boundary the artefact
supplies**. Its register is **hand-written and `--emit` writes nothing**, because a tool that seeds its own
licence is a check reading its answer off the field it supplements; the 232 seeded `UNTRACED` entries are a
known error with a known size and the count prints on every run. Six bites red, three controls green — **and
the first bite did not bite**, changing the file outside the brackets the check read and exiting 0 like a
passing control, which is how the item's own wording was found to be hiding 43% of its subject: *a bite
aimed at the specification tests the specification.* **Previously moved on 2026-10-23 with assertion 37, `qa_acronym_evidence` (ruling #113, standing-queue item 17 closed at 8 days and five displacements, an item two runs had declared UNACTIONABLE AS SPECIFIED)** — **twenty-two** `postbuild` entries, **thirty-seven** tools, **34 of 37 gating**, all three derived by `qa_patch_queue` rather than counted by hand. **It is the first assertion built on a boundary the artefact supplies rather than one the check has to guess.** Item 17 asked whether a name-boundary assertion is possible at all; two detectors said no and both were right — word-initials returned **3** across 44 pieces *and would have missed the very instance that earned #101* (`KESSHA` is not `KSSHA`), and a wide institution-name recogniser returned **46 across 28 of 44**, two populations 36 apart with nothing able to adjudicate between them. **A name's boundary is not a textual property in general; it is one exactly when the name carries an acronym**, because the acronym states how many words and which letter each begins with. Letting a word supply a *prefix* rather than one letter makes the anchor that defeated the first detector the thing that makes it exact. **Four of its fifteen anchors — 26.7% — are not evidenced in the annotations of the piece that prints them** (`KJSEA`, `PSLE`, `TMIS`, `J-PAL`), handed to the Web Developer as item 35 rather than fixed by the instrument that found them, because two of the four registers cannot be read from this runner and #101 clause 1 demands the register's own wording. **And the first of the four is on the piece that earned #101, eight days after that correction shipped** — *a correction reaches the instance it was sent to; only an instrument reaches the class.* **0 anchors across all 44 Arabic bodies, by construction**, which makes yesterday's asymmetry true twice: the edition #101 FORCES to answer the name question is the edition no instrument of ours can read the answer from. Three bites red with controls green either side, bite 2 being the literal 103-day published defect; **and the Arabic count read 1 before the code was right**, two Latin acronyms 180 characters of Arabic apart read as neighbouring words because adjacency was counted in tokens rather than in text. **Previously moved on 2026-10-22 with assertion 36, `qa_citation_identity` (ruling #112, standing-queue item 18 closed at 7 days and six displacements)** — **twenty-one** `postbuild` entries, **thirty-six** tools, **33 of 36 gating**, all three derived by `qa_patch_queue` rather than counted by hand. It is the first assertion whose subject is whether a document somebody else serves is still the document we CITED — every other instrument that touches an outbound promise classifies it by status code, and a citation that dies softly at 200 reports healthy forever. The identity token needed no inventing: 386 of 682 source entries already quote their registers verbatim inside quotation marks — **529 tokens over 218 registers, claims about somebody else's bytes that nothing had ever compared against those bytes.** It reuses `qa_claim_registers`'s split for the third time (network `--emit` gates nothing, offline `--check` gates coverage), because somebody else's rewrite at 09:00 must not stop this publication deploying. **Comparable on 90 of 170 asked, and 31 of those 90 — 34.4% — no longer serve a quotation we attributed**; 14.2% of the population and 18.2% of the asked are the same number wearing the units of the world, which is #111's denominator lesson one day later. Two of the four causes are **ours** and are queued for repair rather than fixed by the instrument that found them. **And the sharp half: 128 of 134 declined tokens are Arabic** — the incapacity that makes the Arabic edition the forced control for a NAME (#101) makes it structurally incapable of carrying the evidence for a SENTENCE, so #86 gains a second clause. Proved five bites with controls green either side and eleven readings of the comparison against synthetic served bytes, every injection asserted to have changed the artefact first — **and the fifth bite did not bite on its first run**, stripping four of five quotation conventions and exiting 0, which reads exactly like a passing control. **Previously moved on 2026-10-21 with assertion 35, `qa_claim_registers` (ruling #111, standing-queue item 15 closed at 7 days and six displacements)** — **twenty** `postbuild` entries, **thirty-five** tools, **32 of 35 gating**, all three derived by `qa_patch_queue` rather than counted by hand. **It is the first assertion whose subject is a claim's RE-VERIFIABILITY — a property of the world rather than of anything this operation produces** — and that is why only one of its two halves can gate. It reuses `qa_served_manifest`'s split with the modes the other way round: the **network** half (`--emit`) asks an archive whether a snapshot of each cited register exists, and gates nothing, because an archive.org outage must not stop this publication deploying; the **offline** half (`--check`) gates from `postbuild` and asserts that the register *covers the corpus*, so a citation nobody has ever asked an archive about fails the build instead of narrowing the measurement in silence. What it found is in the ruling: of 342 cited registers 205 have been asked so far, **40 of them hold no snapshot anywhere — 19.5% — and 12 of those also refuse us**, and the claim-level join concentrates all of it — **20 published figures, every one of them on a single piece.** A per-URL sweep reports that as a rate spread over the corpus; the claim-level unit reports one piece whose spine cannot be re-opened. Proved four bites with controls green on either side of each, every injection asserted to have changed the artefact first. **And the pacing is measured, not chosen:** the first emit asked all 342 with six workers, got 100 answers and then 242 consecutive 429s — *a row that reads `archive-unknown` because we were throttled is an observation about us, not about the world* — so the emit carries a request budget and tops the register up across runs. **Previously moved on 2026-10-20 with assertion 34, `qa_composition` (ruling #109, standing-queue items 14 and 13 closed together)** — **nineteen** `postbuild` entries, **thirty-four** tools, **31 of 34 gating**, all three derived by `qa_patch_queue` rather than counted by hand. **It is the first assertion whose subject is an ASSEMBLY rather than an artefact** — it asserts a property that no file in the corpus can violate on its own. Item 14 asked whether the *build* can ask a composition question at all or whether composition is only ever visible to a render; the answer is a boundary in three parts, and it is written into the tool's header. What the build can see is the **collision** (two inlined fragments writing the same full selector into one cascade, two pages describing one JSON-LD `@id`, two feeds sharing a `<guid>`); what only a render can see is the **consequence** (which rule wins, what it then paints). So the tool gates the precondition and says so. Limb 2 — each inlined cover's kicker fill equals its registry accent, which is item 13's property — is **licensed by limb 1 and withheld when limb 1 fails**, because a declared value is the computed value exactly when nothing else can match the element; that is how item 13's browser probe was answered without a browser. Measured while building it and recorded because four of five surfaces came back clean: 13 inline `<style>` blocks across 135 served documents with 0 collisions, 266 JSON-LD `@id` with 2 described on more than one page and 0 disagreements, 88 feed items with 0 shared `guid` or `link` across the two feeds, 396 hreflang alternates reciprocal, 134 canonicals and 134 `og:url` with none shared. Proved three bites and one control, each injection asserted to have changed the artefact first. **And the harness produced two false positives before the code was right, both the same shape:** bare class tokens read the repaired scoping as a 5-way collision, and a facet probe read a documented `>= 2` bar as 33 missing pages — *a composition check's error rate is set by whether it knows the intended assembly.* Previously moved on 2026-10-10 with assertion 32, `qa_bridge_coverage` (ruling #93, standing-queue item 1)** — **seventeen** `postbuild` entries, **thirty-two** tools, **29 of 32 gating**, all three derived by `qa_patch_queue` rather than counted by hand. **It is the first assertion whose subject is not the publication and not this repository's prose, but the STEP THAT CARRIES the other assertions' conclusions to the reader.** Item 1 asked which gating assertion is wired where it cannot observe its subject; the answer, enumerated, is **none of them** — all read `dist` or the repository root, both of which exist in the `build` job where all 29 run. The wrong home belongs to the **bridge**: only the `verify` job's byte-compare promotes a claim about `dist` into a claim about the origin, and it compares **six files of 257 — 2.3%**, with **zero of the 133 assets a page loads**, including the 34 fonts added two days earlier. It takes the repository root, not `dist` — the **fifth** such gate — because it parses the workflow file. The ratio is **measured and deliberately not asserted** (widening the bridge needs a workflow write this identity does not have, and a floor above today's reality would red every build until a patch nobody can apply lands); what it asserts is that bridge members exist, that every `.html` member is a page the sitemap claims, and that **the bridge spans both editions and both feeds.** Proved 13 ways, bite first, on /tmp copies — **and the harness caught the tool overcounting the bridge while its control printed the correct total**, because the verify job names both feeds twice and the two lists overlap exactly. Previously moved on 2026-10-08 with assertion 31, `qa_third_party_origins` (the self-hosted fonts, standing-queue item 4)** — **sixteen** `postbuild` entries, **thirty-one** tools, **28 of 31 gating**, all three derived by `qa_patch_queue` rather than counted by hand. **It is the first assertion whose subject is the publication's *privacy posture*, which until 2026-09-18 was a sentence in the CHARTER with no number behind it and until today was a measurement with no gate behind it.** It asserts one thing: no page fetches anything automatically from an origin we do not own. The whole design is a classification the 09-18 audit wrote before any code existed — **by who initiates the fetch, never by origin** — because this publication points at ~180 external origins on purpose and a check that counted those would report our own method as our largest defect and be switched off inside a week. `<a href>` and `og:image` are counted and printed and **not** asserted, with the reason in the output. Proved **19 ways**, bite first, on a copy of `dist`, and the first bite is the markup removed from `Base.astro` this morning rather than an invented one. *(Also corrected today: `qa_patch_queue` printed its first home's label as `agents/tools/*.py` while the glob has always been `qa_*.py` — harmless for nine days, misleading from the moment this day added the first non-assertion tool to that directory.)* Previously moved on 2026-10-07 with assertion 30, `qa_register_shape` (ruling #90) — **fifteen** `postbuild` entries, **thirty** tools, **27 of 30 gating**, all three derived by `qa_patch_queue` rather than counted by hand. **It is the first assertion whose subject is this repository's own prose rather than the publication**, and the first to make one of this file's own counts a build failure: the ruling range in the non-negotiables above is now derived from §3's rows, which is the 09-27 amendment's fourth home closed by an instrument instead of by a habit. It takes the repository root, not `dist` — the **fourth** such gate — because a markdown table is never built. Previously moved on 2026-10-06 with assertion 29, `qa_served_manifest` (ruling #89) — fourteen
`postbuild` entries, twenty-nine tools, **26 of 29 gating**, all three derived by `qa_patch_queue`
rather than counted by hand. **It is the first assertion whose gated half and asserting half are
different modes of the same tool, and the distinction is load-bearing rather than tidy.** `--emit`
writes a per-URL fingerprint of the served bytes into `dist` and is gated from `postbuild`, because if
it ever fails to run the chain of memory breaks and the *next* build has no baseline; `qa_census` reads
it as a sixteenth instrument and asserts its routed-page count against the sitemap's own `<loc>` set, so
a manifest that quietly stops describing some pages fails the build instead of narrowing in silence.
`--check` fetches the manifest the **origin** is currently serving and is **not** gated — its home is the
`build` job after `npm run build`, which this identity cannot write, so the reason lives in the tool's
header and the step is staged at `agents/patches/2026-10-06-build-served-manifest-check.md`. **The
`verify` job is the wrong home and that is worth knowing rather than guessing:** verify compares the
artifact it just published against the origin, so origin == artifact by construction and the manifest
would be compared against itself — a check in the wrong home, passing forever, which is standing-queue
item 1's subject reached from the other side.

**And the weekly re-read was not enough — the queue is now GATED (ruling #75, 2026-09-29).** The
09-27 review executed the rule above in full, and the patch was **wrong again the next morning**
because assertion 26 landed on the Monday: a queue reconciled weekly against a count that moves
daily holds a wrong number six days in seven. `git apply --check` returned 0 on every day it was
wrong, because it proves a patch *lands*, never what it then *asserts*. **Standing assertion 27,
`qa_patch_queue.py`**, derives the register from its three real homes — `agents/tools/`, this
workflow's build steps, and `web/package.json` — reads every numeric claim in `agents/patches/`,
and fails the build on any disagreement. **Run it to read the register rather than trusting this
paragraph:** `python3 agents/tools/qa_patch_queue.py .`. The re-staged issue-#6 patch now states
**no count at all** and points at that derivation, so it carries zero numeric claims and cannot go
stale again — *a number that lives in three files should be asserted from them, never copied into a
fourth, least of all into a file the run that finds the error cannot edit.*

**A red `verify` job is not automatically a red publication.** On 2026-09-23 the deploy
failed on a feed-validator step while the byte-compare in the same job passed — the check
was wrong, not the site (ruling #63). Read which step failed before planning a repair.

**These three counts drifted for seven days and were corrected at the 2026-09-20 weekly
review, moved again on 2026-09-22 by the run that added assertion 22 (`qa_date_identity`,
ruling #60), again on 2026-09-23 by the run that added assertion 23 (`qa_packet_figures`),
and again on 2026-09-24 by the run that added assertion 24 (`qa_feed_validators`, ruling
#63) — at the point of filing, per the 09-20 rule, rather than
waiting for a Sunday — and again on 2026-09-26 by the run that added assertion 25
(`qa_chrome_links`, ruling #67 — a rule that named a check and never produced a file, so the count
had no way to notice it missing).** They read 14 / 13-of-14 / eleven while the operation had built seven new
assertions and wired five of them — in the one file every run is told to read first. The
weekly review now prints the ratio (`N of M gate the deploy`) and reconciles it against
both homes; if this paragraph and that ratio ever disagree, the workflow files are the
state and this paragraph is the stale one.

## Writing

House voice: plain, specific, unhurried. Short declarative sentences. No marketing
register, no exclamation marks, no hype. A hedge that appears in a source's citation
must appear in the sentence that uses it — the annotation and the sentence are written
from the same open register. Prefer the source's own grammar over a firmer paraphrase.

## Commit messages

Single line, ASCII, no `!` and no `$` (they break in zsh history expansion, twice
already). Keep the detail in the brief, not the subject line.
