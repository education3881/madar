# Manager status — 2026-05-27 (end of day)

**From:** Manager
**To:** Vini
**Subject:** A push-content day. What went out, what was deliberately held back, what waits on you.

---

## The directive you gave this morning

You opted in for one day. You asked for the minimum-good amount of content. You chose Option 5: pull Egypt forward, plus produce Arabic versions of the two approved pieces. The implicit constraint, as always, was the quality bar — no shortcuts that compromise the five-test rubric.

We delivered all three. The publication moves from 2 EN / 0 AR to 3 EN / 2 AR in a single day, with no parks, no placeholders, no provisional sources. The build is clean; the working tree is ready to push. The only thing between this and the live site is your terminal.

## What shipped (in source; awaiting push)

1. **Egypt — *Egypt's Knowledge Bank at ten, and what it now ships through the front door*** (Curated 03 · Issue 01 · Replacement B). Pulled forward from its 2026-05-28 deadline because the source verification cleared cleanly today. Two named institutional figures bracketing a decade: Dr. Tarek Shawki (2015 AUC quote, founding) and Prof. Ayman Ashour (2025 Elsevier announcement quote, AI integration). Five primary-source URLs verified live today + one AUC source + one Arabic-press citation from Youm7 (15 June 2025). Approved by the Editor with the five-test rubric. Lives at `/web/src/content/articles/2026-05-27-egypt-ekb-decade.md`. Verdict at `/content-drafts/verdicts/2026-05-27-egypt-ekb-decade.md`.
2. **Sierra Leone — Arabic version**. *المعلِّمة في «بو» التي ما زالت تستخدم طباشير الفصل الماضي.* All editorial beats preserved, including the composite-character convention (Hawa / هَوَى, dagger footnote translated), the Krio phrase *Lan fɔ lan*, and every source citation with Arabic-translated titles + verbatim URLs. Lives at `/web/src/content/articles-ar/2026-05-25-bo-teacher-chalk.md`.
3. **Bahrain — Arabic version**. *البحرين تُقَيِّم مدارسها، بالاسم، على الملأ.* All five BQA sources preserved with Arabic-translated titles, Dr. Maryam Hasan Mustafa quoted in Arabic, four-grade scale rendered in the standard ministry register (*ممتاز · جيد · مُرضٍ · غير مُرضٍ*). Lives at `/web/src/content/articles-ar/2026-05-26-bahrain-bqa-public-grades.md`.

## What was structurally new today

- **The Arabic article route now exists.** Before today, the `articles-ar` collection had no dynamic route to render its pieces. The Web Developer scaffolded `/web/src/pages/ar/articles/[...slug].astro`, mirroring the EN route's structure with Arabic typography, RTL layout, and Arabic-Indic numerals on the sources list. The AR home page was already prepared (yesterday's cleanup) to surface the AR collection when populated; with two pieces in it, the placeholder block is now retired and both pieces appear on `/ar/`.
- **Bilingual cross-links wired both ways.** The EN articles now declare `arabicVersion:` in frontmatter; the AR articles declare `englishVersion:`. Both dynamic routes render a small monospace cross-language link in the title block. Readers can hop registers on any of the four bilingual pieces.

## What was deliberately not done

The Editor's verdict on the Egypt piece flagged two honestly-noted gaps. Both were accepted, with reasons in writing.

- **K-12 was not centred** in the Egypt piece, against the brief's preference. The verifiable news of the platform's tenth year is in the research tier (the June 2025 AI integration), and a K-12-centred piece would have required a named teacher or student we could not verify in open press today. A K-12-specific brief on `study.ekb.eg` is now on the calendar for a future cycle.
- **No named teacher or student user** in the Egypt piece. Two institutional figures bracketing a decade carry the piece's argument; the Bahrain piece established that institutional voice alone can do the work when the piece is about institutional posture. Different evidence registers for different pieces; this is a deliberate editorial stance, not an oversight.

## What I need from you, in order of priority

The same single ask as yesterday. The sandbox cannot push.

```bash
cd "/Users/vini/Documents/Claude/Projects/Educational Website"
git add -A
git status   # sanity-check the file list
git commit -m "Madār — 2026-05-27: Egypt EKB at ten + Arabic versions of Sierra Leone and Bahrain"
git push
```

Within roughly a minute of the push, the live site goes from 2 EN / 0 AR to 3 EN / 2 AR. The `/ar/` home will surface both Arabic pieces. The EN home will surface Egypt alongside Bo and Bahrain. Cross-language links on each piece will work. The Web Developer will run the post-deploy QA checklist within 30 minutes of the push (the checklist already covers cross-language link integrity).

## What's queued for the rest of the week

- **2026-05-28 — Designer.** Hero still for the Egypt piece. Brief incoming from the Editor today. Curated 03 register, matching Bahrain's tonal weight.
- **2026-05-28 — Web Dev.** Daily QA pass on the live site, with the new bilingual cross-link integrity check folded in. The one open P1 (`/rss.xml` referenced in footer but not built) is still scheduled for this fix.
- **2026-05-29 — Editor.** Brief for the K-12-specific EKB piece (the one we did not write today). Working title: *What `study.ekb.eg` actually does, and what its teachers actually use it for.*
- **2026-06-02 — Editor.** Issue 02 anchors. The slate is at `/content-drafts/_ISSUE_02_SLATE.md` — your call on the three to greenlight is still open. Default if you don't weigh in by EOD Monday: the Editor's recommendation (Saudi HCDP, Oman ECE, Senegal daara).

## A note on what today demonstrated

You asked, this morning, for the minimum-good amount of content the Editor and Content Creator could produce in one day. The honest ceiling we set was three pieces if at least one was a translation rather than fresh research. We hit that ceiling, with no compromises on the rubric — five verified sources on the Egypt piece, two named figures, an honest architecture note flagging where the piece diverges from the brief, and an Editor's verdict that accepted the divergence with reasons.

The lever that made today possible was the Arabic translation work. Fresh research at the publication's quality bar is a one-piece-per-day-per-Content-Creator ceiling. Translation, with the source already verified, is a different unit of work. The Editor's bandwidth scales differently across the two. Worth keeping in mind for the next high-volume day: if you want more than one new piece, the second and third should be translations of pieces whose sources have already cleared, not fresh research running parallel to a primary draft. The two parked pieces from 2026-05-26 are the negative proof of this; today's clean run is the positive one.

The publication is bilingual today in a way it was not yesterday. That is a real threshold for Madār.

— Manager
