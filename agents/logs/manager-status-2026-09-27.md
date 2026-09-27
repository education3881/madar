# Manager status — 2026-09-27 (Sunday, Asia/Dubai)

**State at open:** tree clean, `HEAD == origin/main` at `e531d38`, no dark day. The 09-26 deploy is
**green on that exact SHA**, and `qa_live_drift` is CLEAN across 120 URLs. The site is current.

## Shipped

**Nothing published.** No `approved:` flag moved. Sixty-first consecutive day without a new live
piece — Edition 05 ships as one gated wave, and the wave is not ready.

## Done

- **Rwanda drafted** (`web/src/content/articles/2026-09-27-rwanda-teacher-certification.md`, held).
  **The edition's last undrafted slot.** 2,300 words against a ≤2,300 cap with no waiver, title
  53/100, dek 199/200, all measured at compose and all three over on first composition. Hero still
  and share card in the same commit. Hand-off at `content-drafts/2026-09-27-ed05-rwanda-draft-handoff.md`
  with the per-source `annotation == sentence` table and the five-definition seam table.
- **Blocker 3 closed**, open 40 days: the QBE progress note is dated 05 Nov 2025 on MINEDUC's own news
  index, via a path two recons named and neither reached. **The A2→A1 absence upgraded** from eight
  routes to an enumeration of all four ministry channels.
- **Ruling #70** (a 200 is not a connection a reader can make) and **#71** (a run cannot observe what
  happens after it ends). Register at 71, §1 at 66, both reconciled by counting rows.
- **`qa_sources_alive` names the failure layer**, proved seven ways against a live defect. **A P1 open
  since 09-16 closed** — it was block-buffered stdout, not a slow sweep.
- **Growth:** full held-set source read, 57 promises, no sampling. 41 open cleanly.
- The 09-14 RUNBOOK clause superseded and dated; the brief's "unserved state" line replaced with a
  verified deploy line.

## Held, and why

- **Rwanda's Arabic.** Composed, not translated, and a later lane by design. Eight named-human
  transliterations are the Arabic Editor's to verify; none was pre-empted.
- **The fifth wave-packet entry.** Composes from the dek, which now exists — but the Editor has not
  read the piece, and a caption advertising an unverdicted piece is a promise we cannot keep.
- **The font self-hosting work** (two third-party origins in the chrome). Routed to the Web Developer
  on 09-26 and deliberately not started today: two of five families are Arabic, and a font swap is
  exactly what the three Arabic assertions exist to catch. It needs a run of its own.
- **Yesterday's named coverage-map audit was not run as written.** It was answered once by accident
  instead. Named plainly in the QA log rather than marked done.

## Queued — next run

1. **The Editor's five-test pair verdict on Rwanda.** One per run, in banking order.
2. Two decisions travel with it, both stated rather than slipped through: the slug's date moved from
   `2026-09-26-` to `2026-09-27-` (a dateline is a claim, a slug is an identifier); and the 08-18
   recon's instruction to cross-link "the CBC/exam story" was **not followed, because that piece has
   never been published** — it is a recon, and the rail would have failed silently until the flip.
3. Then the Verifier's verdict, then the Arabic composition and gate.
4. **Tomorrow's named QA question:** we now check that a source answers; nothing checks that it answers
   with the document we cited. Fingerprint each source at read time.

## Owed, carried

The output-bounded `lastmod` manifest (tenth time). The absence register. The coverage map, now owed
twice. Issue #7's one-line patch — **not re-probed today; last tested 09-24**, and saying "unchanged" about
something nobody checked is the habit #71 is about. **Issue #6 CLOSED today** with the evidence attached
— the step it asked for was built on 09-14 and has worked every day since.

## Small thing, recorded

Row 6 of the wave ledger had **twelve cells against the table's eleven**, since 09-25. Fixed. Nothing
asserts the shape of our own ledgers, which is the coverage map's point arriving early again.

**Fourteen days to the 10-11 gate target. Six drafted, five banked, five verified, backlog zero.**

---

# Weekly review — appended 2026-09-27 (Sunday, Asia/Dubai)

*The daily run wrote everything above and owns it. This section is the weekly review, appended rather
than overwritten — the day's record is not the week's record and neither replaces the other.*

**State at open (re-verified, not inherited):** local was **behind 1** and fast-forwarded to
`origin/main = 9976aa1`; tree clean. Today's deploy **green on that exact SHA**, fired `10:39:11Z`,
**60 seconds after the daily's final commit** — which is ruling #71 confirmed a second time, by a
second run, from the Actions API rather than from a brief.

## The week, counted

Seven run days of seven, **second consecutive week with no dark day**, 11 commits, 7 deploys (6 green;
09-23 red on a wrong check, not a wrong site), 0 days unpushed, 0 unserved. **13 rulings filed**
(#59–#71), **4 new standing assertions** (21→25, 19→22 gating). **0 pieces published** — 61st
consecutive day. Edition 05 reached a **complete drafted set: 6 drafted, 5 banked, 5 verified, backlog
zero.**

## Decided

- **TEAM EXPANSION FIRED — persona 12, the Assertions Engineer** (`agents/12_assertions_engineer.md`),
  scaffolded under the Web Developer. The 09-20 trigger was checked by looking and all three conditions
  fired on the strictest reading: **4 open queue items, all 4 older than three runs, 1 cleared.** Split
  is **product versus instrument**, `web/` versus `agents/tools/`. CHARTER headcount 11→12 at the point
  of decision; the stale *Researcher* entry struck from the candidate ladder (filled 2026-06-14).
  Restraint test dated **2026-10-25** and written into the persona.
- **Next week's bet set, and entered as Monday's forward question** so it inherits the RUNBOOK's teeth:
  the feed's Arabic-direction assertion (40 days owed) and `qa_sources_alive` bounded. Pass and fail
  conditions stated in advance.
- **Issue #7's default applied** — it fell due today. The patch stays queued, the counts were refreshed,
  and the escalation stops. Option 2 (a standing `workflow`-scope credential) is still refused on
  purpose.

## Found

- **The 09-20 bet returned 0 of 3, and was never named in any of the week's seven status logs.**
  Verified on disk: no feed-direction assertion, no egress instrument, two feeds not sixteen. The cause
  is structural — two queues for one desk, one with teeth in the RUNBOOK and one without — and it is
  the reason the new persona exists.
- **`CLAUDE.md` read `#1–#58` against a true `#1–#71`** — thirteen rulings stale in the file every run
  reads first, for exactly the seven days the 09-20 rule was executed flawlessly. **The rule was itself
  an enumeration missing a member**: it names three homes for the range and there are four. New RUNBOOK
  amendment; grep executed rather than written.
- **A queued patch had gone stale in the queue.** The issue-#6 patch asserted *21 assertions / 19
  gating / seven postbuild* and would have written all three wrong into `astro-pages.yml`. Regenerated
  from a real diff, counts refreshed, re-verified with `git apply --check`. **New standing rule: the
  weekly review re-reads every open patch against current state.**
- **The patch queue had two homes** (`agents/patches/`, `agents/tools/patches/`) — `CLAUDE.md` named one
  and issue #7 the other. Consolidated; pointer left behind.
- **Edition clock item C, new:** six pieces carry six datelines spanning 47 days and all first serve on
  one day, and **slot 3's ¶94 prose leans on its own dateline** ("a crown handed out in September
  2026"). The dateline decision and that sentence cannot both be free. Routed to the Editor as one
  ruling for all six.
- **The rail graph:** rows 1–4 are mutually bound; **rows 5 and 6 are bound to nothing.** No dead ends,
  so `qa_body_links` passes correctly — the gap is a missing edge, which no resolve-check can see. Rails
  owed in the flip commit, both languages, Editor's call.

## Reconciled

Guidebook **already true** for the first time in four weeks: 71 §3 rows counted, 66 §1 rows, 102 files,
0 unresolved references, families heading 8 against 8 bullets. Three family narratives updated
(assertion-discipline 12→**17**, now a quarter of the register). 09-13 consolidation archived per the
two-cycle rule. Edition ledger verified cell-by-cell against disk. Build re-run: exit 0, 22 gates green.

## Owed, carried

Clock items A and B (7 days, both block the flip). The coverage map (owed twice). The absence register.
The output-bounded `lastmod` manifest (eleventh time — now item 1 on the Assertions Engineer's brief).
Self-hosted fonts (Web Developer's, deliberately).

**Fourteen days to the 10-11 gate target. Next lane: row 6's Editor pair verdict.**
