# QA log — 2026-09-25, desktop session (run 2, the workflow lane)

**Run:** desktop, started ~14:11 UTC · **Lane:** `.github/workflows/**` — the one path the
cloud identity cannot write · **Brief:** 85 (`agents/briefs/2026-09-25-daily-brief-desktop.html`)
**Editorial lane taken:** none, deliberately. The cloud run's 09-25 queue head was Rwanda's
commission; this run went nowhere near it.

---

## 0. State verification (before any plan)

| Check | Result |
|---|---|
| `git branch` | `main` |
| local HEAD | `70f54e7` (2026-09-16) |
| `git fetch origin main` | `70f54e7..9f7c488` |
| `origin/main` | `9f7c488` (2026-09-25 addendum) — **local 9 commits behind** |
| ahead of origin | **0** — nothing local was ever pushed and lost |
| `git status` | 2 modified, both from the 09-16 run, both uncommitted for 9 days |
| live origin | current — `qa_live_drift` CLEAN, 120 URLs, 0 drift |
| missed days | **none on the cloud side.** Briefs 76–84 on the origin, 09-17 → 09-25, one per day |

**Named plainly:** the *desktop* lane has landed nothing for nine days. The *publication* has
not missed a day. These are different facts and the second is the one that matters to a reader.

### The mechanism, probed rather than inherited

```
$ ls -la .git/index.lock
-rw------- 1 … 0 Sep 16 04:23 .git/index.lock      # the minute the 09-16 run started
$ rm -f .git/index.lock
rm: cannot remove '.git/index.lock': Operation not permitted
$ touch .git/_probe                                 # succeeds
$ rm -f .git/_probe
rm: cannot remove '.git/_probe': Operation not permitted
```

The mount permits `create` and refuses `unlink`. **Any git operation that takes the index has
been refused since Sep 16 04:23.** Routed around per the RUNBOOK rather than fought: all work
below was done in a clean clone checked out at `origin/main`, and every tracked-file change is
delivered as a patch that applies to `9f7c488` (proved, §4).

---

## 1. Build

```
npm ci        → exit 0
npm run build → 120 page(s) built; 10 asset(s) withheld for 5 held piece(s)
```

`postbuild` halted at `qa_render` — **no headless Chrome in this sandbox.** It failed loudly,
which is correct behaviour and is the assertion working. A Playwright headless shell was
installed and `qa_render` still did not complete inside the run's budget. See §3 for how this
is reported.

## 2. Standing assertions — 21 run, 21 clean

Each invoked **exactly as `astro-pages.yml` invokes it**, not as guessed.

| Assertion | Result |
|---|---|
| `qa_dist_input` | CLEAN — dist real, non-empty, no older than its sources |
| `qa_css_tokens` | CLEAN — 174 files, 69 properties, all defined/fallback/runtime |
| `qa_stable_order` | CLEAN — every dated list newest-first, ties by slug |
| `qa_date_identity` | PASS — 76 datelines + 232 listing dates agree with frontmatter |
| `qa_feed_enclosures` | CLEAN — every enclosure resolves, real byte size, real format |
| `qa_census` | CLEAN — 18 numbers from 12 instruments |
| `qa_geo_fields` | CLEAN — every country resolves; EN/AR twins agree |
| `qa_jsonld` | CLEAN — every promise parses, agrees, dereferences |
| `qa_lastmod` | PASS — 120 URLs, 120 lastmod, newest 2026-09-22 |
| `qa_body_links` | PASS — 196 related promises, 571 source promises, **0 rail dead ends** |
| `qa_reachability` | PASS — every page reachable from its own front door |
| `qa_hreflang_clusters` | PASS — every cluster reciprocal and the sitemap's own set |
| `qa_held_assets` | CLEAN — **5 held slugs contribute no bytes**; 76 approved assets served |
| `qa_robots` | PASS — 1 Sitemap line, derived, target exists |
| `qa_a11y_lang` | PASS — every text node agrees with its resolved language |
| `qa_ar_language` | CLEAN — no Latin controlled vocabulary in Arabic chrome |
| `qa_consumer_surface` | CLEAN — og:locale/type/site_name/image, lastmod, print block |
| `qa_packet_figures` | CLEAN — 4 packets, 19 captions, 39 figures, all trace |
| `qa_live_drift` | **CLEAN — origin matches dist: 120 URLs, 0 drift, 4 heads identical** |
| `qa_feed_validators` | **PASS — 16/16 revalidated 304**, both feeds, 8 connections each |
| `qa_stable_order` / parity | EN 38 / AR 38, parity 100% |

### Not run here, and not claimed as green

`qa_render`, `qa_arabic_shaping`, `qa_arabic_joining` — all three require a real headless
Chrome. **They gate from `postbuild` in CI, where Chrome is present.** Recorded as not-run
rather than folded into a count, per the standing rule that a check which silently does not
run is a green light wired to nothing.

### One self-inflicted false alarm, recorded because it is instructive

`qa_body_links` and `qa_held_assets` first appeared to fail (exit 2, and `qa_held_assets`
printing **76 findings**). Both were being invoked with arguments this run had guessed. Read
off the workflow and re-run, both are clean. **A check run with the wrong argument is not a
finding** — it is #52's shape pointed at the invocation rather than the artefact, and it was
not reported as a defect anywhere.

---

## 3. The repair — issue #7, applied

**What landed in `.github/workflows/astro-pages.yml`:**

1. The two-request cache step (lines 250–266) replaced by
   `python3 agents/tools/qa_feed_validators.py --attempts 6`, per the staged patch.
2. **`actions/checkout@v4` added as the `verify` job's first step** — not in the staged patch.
3. The comment block rewritten to describe the mechanism that is actually there, and the
   stated-reasons list beside `qa_live_drift` extended with this tool's reason (09-13 rule).
   **Ratio returns to 22 of 24 gating.**

### The defect in the staged patch

The `verify` job had **no checkout**. It downloads the build artifact and probes the origin
with `curl`, and until this change no step in it read a file out of the repository. Applied
verbatim, the new step exits 2 on *no such file* — **a gate that was red half the time would
have become red every time.**

Second trap, underneath: `actions/checkout` **cleans the workspace by default**, so a checkout
placed after `download-artifact` deletes `artifact.tar` and the `dist/` the byte-compare reads.
Ordered first, with the reason in the file.

Checkout is shallow on purpose — nothing in `verify` reads git history; the `fetch-depth: 0`
rule governs the build job's sitemap `lastmod` resolver, which this job does not run.

### Proved both ways (#35)

| | Workspace | Exit | Output |
|---|---|---|---|
| **Control** | verify-shaped, repo present | **0** | `PASS — feeds revalidate, and every validator names the same bytes` |
| **Bite** | verify-shaped, artifact only — *the job as it stood this morning* | **2** | `can't open file '…/qa_feed_validators.py'` |

**The bite is not simulated.** It is the current state of the file, which is the strongest
form of that proof available here — there is no question of whether the injection was real.

### Structural proof of the edit

YAML parsed and asserted: `verify` has 5 steps; **checkout is index 0**, download index 1; the
byte-compare still **precedes** the feed step (so it cannot false-pass on a stale origin);
exactly one feed-validator step; its `run` body byte-exact. All assertions passed.

---

## 4. The patch for tracked files — and why it exists

Three tracked files needed changes that the cloud run also touched today, so editing them in
the stale working tree would have broken the fast-forward. They are delivered as
`agents/tools/patches/2026-09-25-desktop-tracked-files.patch`, applied **after** the pull:

- `agents/guidebook/INDEX.md` — ruling #66's four counts (§1 row 61, §1 count line, §3 heading,
  §3 register row), moved in one commit per the 09-20 rule.
- `agents/tools/patches/2026-09-24-verify-feed-validators.md` — amended in place to record that
  it landed, what it got wrong, and the checkout requirement, for the next hand that reads it.
- `content-drafts/_EDITION_05_STATUS.md` — the log entry, and the correction of the 09-16 claim.

**Proved before handing over:** `git apply --check` against a pristine `9f7c488` → clean;
applied → register re-counted on the result: **66 rows, 1–66, no gaps, no duplicates.**

`.github/workflows/astro-pages.yml` is edited in the working tree directly rather than through
the patch, for a stated reason: it is **byte-identical between `70f54e7` and `origin/main`**
(verified by `diff`), so the fast-forward carries the modification cleanly.

---

## 5. Deliberate non-actions, each with a reason

| Not done | Why |
|---|---|
| Content lane | The cloud run holds Rwanda; the lane rule gives the second run a lane no earlier line claims. |
| `madar-daily-operation` disabled | Its `enabled: true` contradicts its own description. Whether a manual-only daily keeps a live cron is the founder's call, not a run's — and today that live cron is what applied issue #7. Flagged in the brief with three options. |
| `history.jsonl` snapshot appended | `madar_stats.py --log` was run; this morning's run already logged a **byte-identical** entry for today. A duplicate line records a run, not a change. Reverted, and said so in the brief under the panel. |
| 09-16 block pushed as written | Its central claim is false. It lands corrected. |
| Third route for Zambia's four unreachable URLs | Belongs to the Verifier's confirmation read, not to a workflow run. Still owed. |

---

## 6. Publish gate — IN WRITING

**Nothing ships editorially today.** Recorded in the required form so the absence is deliberate
and not an omission:

| Gate item | State |
|---|---|
| Editor pair verdict | **n/a** — no piece proposed for flip |
| Arabic Editor verdict / AR full pass | **n/a** — no AR content changed |
| Approval flips | **none.** `approved: false` unchanged on all 5 held slugs |
| Hero stills / og cards on disk | unchanged; `qa_held_assets` CLEAN — held pieces contribute **0 bytes** |
| `astro build` clean | **yes** — exit 0, 120 pages |
| Corpus | **38 EN / 38 AR, parity 100%, 35 countries** — unchanged |
| Served bytes changed by this run | **none.** Every file touched is outside `web/` |
| Wave rail integrity | intact — 4 pieces still mutually rail-bound, `qa_body_links` 0 dead ends |

**Two Arabic register questions remain owed to the Arabic Editor** (¶48 dual under negation;
¶60 «دعوتان») from 2026-09-15. Unchanged by this run and still owed before the wave flips.

---

## 7. What this run could not structurally see

Per the standing rule that every quality log names its own blind spot for the next run to test:

1. **Three assertions did not run here** (Chrome). This log's "21 clean" is 21 of 24, stated as
   such, and the remaining three have not been observed by this run at all.
2. **The workflow edit is unexecuted.** Every proof above is of the *tool* and of the *file's
   structure*. Whether GitHub runs it as intended is unobservable from here — which is
   precisely ruling #66's own warning turned on this run's work. **It is verified when `verify`
   goes green, and not before.**
3. **How many times the desktop schedule actually fired** between 09-17 and 09-24 is not
   readable from the task store — only that it was *able* to, every morning. Stated at the
   strength the register supports (#51).

**Forward question for the next run:** *which other operating facts in the RUNBOOK were
verified by reading a description rather than the field that enforces it?* #66 found two in an
hour and neither was being looked for. The repository asserts a good deal about tokens,
permissions, schedules and identities that nothing re-probes.
