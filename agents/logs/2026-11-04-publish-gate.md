# Publish gate — 2026-11-04

**Written before the day's commits, per the CHARTER and the RUNBOOK.** Nothing is published today and
no flag moves. **The gate runs in writing anyway**, and today it has one thing to say that is not
routine: **this run's push publishes two days of commits, not one**, because the 2026-11-03 run failed
before its publish step and the origin has been serving the 2026-11-02 build since Monday.

## What is being published

**No new piece. No flag change. No served byte of the publication changes.**

The day's commits touch:

* `agents/tools/qa_composition.py` — three new gated limbs (assertion 34). **An instrument, not the
  product.**
* `agents/tools/qa_claim_registers.py` — two new classifier states (assertion 35). **An instrument.**
* `agents/stats/claim-registers.json` — 2 rows re-derived from bits already on file, 2 rows updated
  from a genuine re-reading. **Not in `dist`.**
* `agents/guidebook/**`, `agents/logs/**`, `agents/growth/**`, `agents/patches/**`,
  `agents/briefs/2026-11-04-daily-brief.html`, `content-drafts/**`, `CLAUDE.md` — **the operation's own
  record and founder-facing artefacts.** Not the publication.

**`web/src/**` is untouched.** No `dist` byte of any served page differs from the 2026-11-03 build.

**And the carried payload is what this push actually serves to a reader:** the four commits of
2026-11-03, whose served change is the per-language `<meta name="description">` pair on 44 pages —
already gated in writing at `agents/logs/2026-11-03-publish-gate.md`, which was written *before* those
commits and is on file. Nothing is being published today that was not gated on the day it was written.

## The gate, row by row

| Gate | State |
|---|---|
| Editor verdict on file for any piece flipping | **N/A** — no flag moves. The Bahrain draft's Editor verdict (2026-11-02) and Verifier verdict (2026-11-03) are both on file and `approved: false` stands. |
| Arabic Editor's gate | **N/A today, and OWED before the Bahrain flip** — the Arabic composition has not been written. It is tomorrow's content function. |
| Hero still on disk | **N/A** — no piece ships. Owed for Bahrain. |
| Share card (og, raster) on disk | **N/A** — no piece ships. Owed for Bahrain. |
| `npm run build` exit 0 | **PASS** — exit 0, and the full local set green including `build_job_gates`, so the local gate set is the deploy's gate set. |
| All standing assertions green | **PASS** — 38 of 41 gating, all green. The three non-gating ones are named with their reasons in `astro-pages.yml` and in `qa_feed_validators`' own header. |
| Held-slug leak = zero | **PASS, and VACUOUSLY so — stated rather than reported as a win.** There are no held pieces in `web/src/content/`; the Bahrain draft is in `content-drafts/`, which the build never reads. `[madar:withhold-held-assets]` printed *no held pieces; nothing withheld*. Per the 2026-08-09 inversion rule the corpus is in **all-approved** mode, so the assertion that carries weight is the inverse: **`approved:false` count in the build path = 0**, which it is. |
| Gate register derived, not copied | **PASS** — `qa_patch_queue` CLEAN, 0 numeric claims across 9 staged files, 38 of 41 counted in both homes. **It refused today's new patch once**, which is in the QA log. |
| Ruling register's four homes agree | **PASS** — `qa_register_shape` CLEAN. It refused today's filing three times first: a ratio in a sixth home, and then **both** new rows carrying five fields against a six-field header. |
| Founder-facing artefacts render | **PASS** — `qa_artefact_render` OK on 144 artefacts at 1280px; `qa_brief_head` CLEAN on 122 briefs and 21 reviews. **And one defect these two cannot see was caught by reading the brief's own stylesheet** — item 78 — and repaired before the brief was committed. |
| Deploy state verified, not inherited (#71 cl. 2) | **RECORDED** — last green deploy dispatched 2026-11-02 13:00Z; **no deploy since**; four 11-03 commits unserved for two days; the four front doors answer 200 and are serving the 11-02 build. This push dispatches the deploy that carries both days. |

## What is explicitly NOT cleared, and is not being asked to be

The **Bahrain BQA piece** remains four things from its flag, and the fifth is now specified instead of
unknown:

1. Arabic composition — **tomorrow's content function.**
2. Arabic Editor's gate, with the `named humans — gender read from register: 0 of 0` line.
3. Hero still and og card.
4. The `edition:` field — founder **issue #13**, default **2026-11-08**.
5. ~~Archival coverage: UNKNOWN of 5~~ → **3 of 5 unarchived, 2 of them somebody else's and
   single-copy.** The disposition is the **Editor's**, named in
   `content-drafts/2026-11-04-bahrain-bqa-archival-coverage.md`, with the recommendation and its
   reasoning. **This desk does not clear it and does not hold the piece on it.**

Plus, in the flip commit and not after it: the **three forward rails** (item 72).

---

**Signed** · Manager · 2026-11-04 · nothing published, no flag moved, no served byte changed; two days
of already-gated commits carried to the origin by this run's push.
