# Manager status — 2026-11-20 (Friday)

## What shipped

- **Quality — standing-queue items 44 AND 46 CLOSED together**, at 25 and 24 days, by **one** instrument,
  because item 44's own row asked for one. **Standing assertion 43, `qa_emitted_dates`**: every date a
  template emits is derived from the tree and none from the clock. Register **43 tools / 12 build steps /
  28 `postbuild` entries / 40 of 43 gating**, derived by `qa_patch_queue`. Limbs 1–4 compare two emitted
  channels; **limb 5 reads `web/src/**` and asserts the clock is never consulted**, which is the only limb
  any instrument here owns that can see a build-clock date — such a date agrees with itself across any two
  builds in one period. Eight bites red, five controls green, two of them controls that had to stay
  silent. **Item 44's prescribed precondition was evaluated and found unnecessary**, with the reason in
  the tool's header: both operands of every comparison are emitted by one build, and the file reads git
  not at all.
- **Content — cell 7 of eight FILLED** on `2026-11-12-england-ofsted-exempt-cohort`. Hero still and og
  card drawn, inspected, rejected once and redrawn. **Staged at `design-assets/` and deliberately not in
  `web/public/`** — see below.
- **Growth — the archive's first structured data.** Both editions pages served 45 article links each and
  emitted **no JSON-LD at all**; 42 of the other 44 listing pages have carried a full `CollectionPage`
  since October. **0 → 4 nodes a side, 0 → 46 list members a side, 398 → 404 distinct `@id`.** The
  default `itemListOrder` was refused as a false claim about an edition-grouped archive.
- **Research — ruling #152**, *a two-state flag cannot name the state the work is in*. Four count homes
  moved; the enumeration family keeps no running count, so there is no conditional fifth.
- **Brief 136 and this file.**

## What was held, and why

- **The England piece.** One cell left — cell 8, the flip — carrying **six conditions** (two from the
  Arabic gate, four from the Verifier, one of which reaches a reader) plus the rail step's forward edges
  into three older pieces. Quality over slot; it ships the day its own gate closes. Last piece published:
  `bahrain-bqa-five-cycles`, **2026-11-09**.
- **The cell-7 assets are outside `web/public/` on purpose, and the reason was measured.**
  `heldAssets.mjs` withholds by **held** slug read out of the content collection. A piece six cells into
  its gate has no file in `web/src/content/` at all: not approved, not held, **absent**. A card placed in
  `web/public/og/` today would be served at a guessable URL while its article page 404s — the 2026-09-09
  defect verbatim. **`qa_held_assets` was run against a scratch `dist` with the orphan card in it and
  exited 0, printing CLEAN.** Both limbs correct, both blind. Queue item **140**; ruling **#152**.
- **Item 124 named for the sixth consecutive day and not promoted** at 4 days against a 25-day head. It
  remains the board's strongest candidate for a deliberate break of oldest-first, and the run that breaks
  it does so in writing.
- **The home pages' missing `ItemList` was raised, not built** (item 141): whether the six pieces a home
  leads with are a *list* or a *selection* is the Editor's claim about what the home page is.

## Queued

- **Tomorrow's head: item 47 at 25 days** — the only overflow gate we own reads the artefacts, never the
  publication, and at exactly one viewport width.
- **Content tomorrow: cell 8**, the flip, with its six conditions and its forward rails.
- Raised today: **139** (the forward question — limb 5 enumerated a directory and the served perimeter is
  wider: `astro.config.mjs` and `valence/index.html`, both clean by hand, asserted by nothing), **140**
  (invert `qa_held_assets` limb 1 from a list to a complement), **141** (home pages' list node), **142**
  (`about` is one Place and one piece declares five countries).

## Board

**78 open — 0 DEFECT, 75 OPEN, 3 BLOCKED.** Counted by reading the three bucket tables, not against
yesterday's total (#57). Arrived at 76; two closed (44, 46), four raised.

## State

`HEAD` == `origin/main` at the close of each function; five function commits, none saved for the end
(#96). Strand **0** at the open — yesterday's five commits were carried by a successful deploy on that
exact SHA, observed rather than assumed. Corpus unchanged at **45 EN / 45 AR**, 100% parity, zero
`approved: false`. No visitor number anywhere; no tracker by design.
