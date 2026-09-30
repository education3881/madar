# QA log — 2026-09-28 · desktop workflow-write lane

**Publish gate: run in writing, below. Nothing ships editorially today. Corpus unchanged.**

---

## 0. State verification, before any plan (and it inverted the plan)

The brief is yesterday's artefact and was not planned from. Read instead: `git branch`,
`git log -15` with dates, `git fetch origin main`, local HEAD vs `origin/main`, `git status`,
the live origin, and the Actions API.

| Read | Result |
|---|---|
| Local HEAD on entry | `70f54e7`, **2026-09-16** |
| `origin/main` | `1cbcbaa`, **2026-09-27** weekly |
| Local commits not on origin | **zero** — HEAD was a pure ancestor |
| Briefs on origin, 09-17 → 09-27 | **eleven, unbroken** |
| Live origin vs `origin/main` | `qa_live_drift` **CLEAN** — 120 URLs, 0 drift |
| `git push --dry-run` from this VM | `could not read Username` — **this lane has no push credentials** |

**No missed day.** The cloud lane has run every day since 09-17 and the site serves its work. The
gap was **this clone's**, not the operation's: frozen **twelve days** at 09-16.

**Why it was frozen — two blockers, both routed around rather than reported:**

1. A **zero-byte `.git/index.lock` dated Sep 16 07:23**. Every git write failed on it for twelve
   days. It cannot be deleted from this VM by default (`Operation not permitted`), which is why
   every desktop push block since has opened with `rm -f .git/index.lock` — the founder's terminal
   was clearing it once per push and the sandbox was re-creating it.
2. **`unlink` is refused in the mount**, so `git checkout --` and `git pull` cannot *replace* a
   file. Renaming the lock out of the way fixed nothing: git still could not update the tree.

Both closed today by requesting delete permission for the folder, once, with the reason. Then
`git pull --ff-only` → **`1cbcbaa`**. Also removed: three `node_modules/.vite*` rename-around
residue directories (`.vite-stale-1783171238`, `.vite-ZAfW9dv2`, `.vitefu-ySFb4OsV`) — the
accumulated cost of twelve days of routing around a delete that could have been asked for.

**The 09-25 desktop block is superseded and was discarded, not merged:**

| Local edit | Disposition |
|---|---|
| `.github/workflows/astro-pages.yml` | **discarded** — applied the *stale* patch (see §1) |
| `content-drafts/_EDITION_05_STATUS.md` | **discarded** — origin's is newer |
| `agents/logs/qa-2026-09-15-desktop.md` §6 addendum | **kept** — unique, and its analysis of the two lanes is correct |
| 09-25 desktop brief / growth / guidebook notes | **kept** as that lane's honest history |
| `agents/tools/patches/2026-09-25-desktop-tracked-files.patch` | **withdrawn** — a whole-tree patch of a 9-day-stale clone |

## 1. The day's finding — two open patches, both green, mutually exclusive

Full reasoning in ruling **#72** and in `agents/patches/WITHDRAWN.md`. In short:

- `2026-09-20-verify-feed-cache-retry.patch` **rewrites** the seventeen lines that
  `2026-09-24-verify-feed-validators.md` **deletes**. Both passed `git apply --check` alone. Both
  were open this morning. **They cannot both land.**
- The survivor was **incomplete**: it inserts a step running `qa_feed_validators.py` into a `verify`
  job that **has never had a checkout**. As written it fails on first dispatch with *no such file*.
  Checkout added, **ordered first** — `actions/checkout` cleans the workspace, so placed after the
  download it deletes `artifact.tar` and the `dist/` the byte-compare needs.
- The survivor's counts were **stale**: *22 of 24* against a true **25**, three days after the review
  that *moved* it declared the queue reconciled. **A move is not a read.**

**Queue state: empty.** Both patches left it — one applied, one withdrawn with its reason, both
ledgered. First time since `agents/patches/` was opened. Issues **#6** and **#7** both close here.

## 2. Assertions — all 25 run this session

Counted off both files rather than remembered: **thirteen** tool invocations in
`astro-pages.yml` (twelve build steps + `qa_feed_validators` now in `verify`), **ten** in
`postbuild`, **two** non-gating. **23 of 25 gate**, up from 22 today.

*(A note on method: the first enumeration of the workflow's assertions was built with the pattern
`qa_[a-z_]+` and returned **twelve**, silently dropping `qa_a11y_lang` because its name has digits.
Widened and re-counted to thirteen. An enumeration built by a pattern is scoped to the pattern —
#51 again, and the third time this month a count was wrong because the rule that produces it was
itself an incomplete enumeration.)*

| Group | Result |
|---|---|
| Build-job steps (12) | `qa_a11y_lang` `qa_ar_language` `qa_body_links` `qa_consumer_surface` `qa_dist_input` `qa_geo_fields` `qa_held_assets` `qa_hreflang_clusters` `qa_jsonld` `qa_lastmod` `qa_reachability` `qa_robots` — **all PASS** |
| `verify` (new, gating) | `qa_feed_validators --attempts 6` — **PASS**, 16/16 revalidated 304 |
| `postbuild`, non-browser (7) | `qa_css_tokens` `qa_stable_order` `qa_date_identity` `qa_feed_enclosures` `qa_chrome_links` `qa_census` `qa_packet_figures` — **all PASS** |
| `postbuild`, browser (3) | `qa_render` (5 targets), `qa_arabic_shaping` (310 Arabic-bearing elements, all `letter-spacing: normal`), `qa_arabic_joining` (12 runs, worst served 0.730 vs 0.9 threshold) — **all PASS** |
| Non-gating (2) | `qa_live_drift` **CLEAN**; `qa_sources_alive` exit 0, findings editorial only |

**Build:** `npm run build` → **120 pages**, exit 0. Held-asset withholding correct: **12 assets
withheld for 6 held pieces**.

**The three browser assertions could not run on this VM** — no headless Chrome, and no root to
install its shared libraries (`libXdamage.so.1` missing; `sudo` refused by the no-new-privileges
flag). Chrome installed via `@puppeteer/browsers` still would not start. Routed to the cloud
container, which has Chromium: `dist/` and `agents/tools/` tarred, staged, all three run there, all
three clean. **Recorded because a check that silently does not run is a green light wired to
nothing** — `qa_render` says exactly that in its own failure text, and refused to pass. It was right
to.

`qa_sources_alive --held-only --sample 6`: 4 ok, 1 tls, 1 walled. The `mineduc.gov.rw` certificate
**expired 23 Sep and the documents still serve at 200** — ruling #70's finding, still live five days
on, correctly bucketed with its layer. Both findings sit on **held** pieces and are editorial
decisions, not build defects.

## 3. YAML integrity after two hand-edits to the workflow

`yaml.safe_load` parses. Job/step census after the edits: **build 18 steps · deploy 1 · verify 5**
(checkout → download-artifact → byte-compare → feed validators → IndexNow). Verified by parsing the
file, not by reading the diff.

## 4. Publish gate — in writing

| Condition | State |
|---|---|
| Editor verdict required? | **No** — nothing editorial ships. Corpus unchanged: 38 EN / 38 AR, 35 countries. |
| Arabic Editor verdict required? | **No** — no AR content touched. |
| Approved flips | **None.** Six pieces remain `approved: false`; wave gate targets 2026-10-11. |
| Hero stills on disk | Unchanged; 12 held assets correctly withheld at build. |
| `astro build` clean | **Yes** — 120 pages, exit 0. |
| All standing assertions | **25 of 25 run, all clean.** |
| Held-slug leak | **Zero** across pages, sitemap, feeds and assets. |
| Live drift | **CLEAN.** |

**Gate verdict: PASS for a non-editorial push.** What ships is the workflow repair, the patch-queue
reconciliation, ruling #72, this log, the growth note and the brief.

## 5. Owed to the weekly (2026-10-04)

1. **The lane question, and it is now a decision with evidence.** The `madar-daily-operation`
   desktop schedule fired today against a clone twelve days stale while the cloud lane ran
   correctly. This run found real work only it could do — `.github/workflows/**` is unwritable by
   the cloud identity — but that is **one function, not five**, and a lane that plans a full day off
   a frozen checkout produced the stale-patch application on 09-25. **Recommendation: narrow this
   schedule to the workflow-write function, or retire it and route workflow patches through the
   founder channel.** Put to the founder in today's brief.
2. **The cloud daily's declared time is wrong by five hours.** `madar-daily.yml` cron is
   `23 4 * * *`; the last four runs actually started **09:23–10:02 UTC**. Already off minute 0, so
   the usual remedy is spent and the cause is elsewhere. The charter advertises ~08:00 Asia/Dubai;
   the brief lands nearer 13:30. **Not touched today** — diagnosing it is not the same as guessing at
   it, and this lane has had enough of applying repairs it has not proved.
3. **The patch queue is empty.** Nothing to reconcile next Sunday, for the first time. The new
   cross-patch rule from #72 therefore gets its first real test only when a patch is next queued —
   note that it is **untested**, per #67.

## 6. Found while writing the brief — the statistics history had been double-logging for six weeks

`madar_stats.py --log` appends a dated snapshot to `agents/stats/history.jsonl`, and the charter's
whole reason for that file is that **week-over-week deltas accumulate in it.** Running it twice today
(once to read the panel, once to regenerate it) produced two identical rows — which is how the file
came to be read at all.

**It had 94 rows for 82 distinct dates.** Eleven were byte-identical duplicates, across nine dates
spanning **2026-08-17 to 2026-09-27**: 08-17, 08-18, 08-23 (three rows), 08-25, 08-30, 09-08, 09-10,
09-14 (four rows) and 09-27. Six weeks of it. **Any delta computed off this file was computed off
double-counted days**, and nothing asserted otherwise because the file has **no key and no assertion** —
it is append-only by design and a log that claims nothing cannot be caught claiming something false.

**The first fix was wrong and is worth recording as a near miss.** Deduplicating *by date* looked
obviously right and removed thirteen rows. But **2026-09-14 carries four rows of which two are
genuinely distinct** — `ar_total` 41 / `held_ar` 3 against `ar_total` 42 / `held_ar` 4 — because two
real runs executed that day, the last desktop run and the first cloud run, and the corpus moved between
them. A by-date dedupe keeps the *first* row per date, so it would have silently discarded the later
and more advanced of the day's two real measurements. **One row per day was never the invariant.**

Corrected to remove only **byte-identical** rows, first occurrence kept, order preserved:
**94 → 83**, then today's snapshot appended once → **84 rows, 83 distinct dates, 09-14 retaining both
of its distinct snapshots, zero byte-identical duplicates.**

**Owed to the weekly, and routed to the Assertions Engineer:** this file wants an assertion —
*no two byte-identical rows, and every row's `as_of` parseable and non-decreasing* — which is the
enumeration-with-no-count shape (#57, #70, #72) arriving in a data file rather than in prose or a
check. Note also that the tool appends unconditionally: **a run that reads the panel twice corrupts the
history**, which is a defect in the tool and not in the operator. Both belong to the same owner.
