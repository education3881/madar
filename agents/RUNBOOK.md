# RUNBOOK — how Madār operates day-to-day

> **For the Manager opening a new session.** Read this first, then `/agents/01_manager.md`, then yesterday's status log at `/agents/logs/manager-status-<yesterday>.md`. After that, brief all four departments **in parallel** within the first ten minutes.

---

## The five things to know in one screen

1. **Vini is off operations.** He reads daily, weighs in when he chooses. The Manager runs the publication. Escalation list is short (geo/topic scope, brand, paid infra, reputation).
2. **Deploys are automatic.** Every push to `main` triggers GitHub Actions, which builds the Astro site under `/web/` and publishes to GitHub Pages within ~90s. There is no manual `dist/`, no `gh-pages` worktree, no terminal beyond `git push`.
3. **The publish gate.** A piece does NOT ship until: (a) Editor verdict file in `/content-drafts/verdicts/<slug>.md` is `approve`, AND article md is in `/web/src/content/articles/<slug>.md` with `approved: true`; (b) Designer hero still exists at `/web/public/stills/<slug>.svg` and is committed; (c) Web Developer's `npx astro build` produces clean `dist/` AND the QA spot-check passes.
4. **Parallel, never serial.** When the Editor commissions a piece, the Manager **simultaneously** briefs the Designer (hero brief), the Web Developer (integration window), and Growth (social window). The Editor's verdict is the LAST gate, not the first dispatch.
5. **Quality over slot.** A thin issue is better than a weak piece. The Editor's parks are final at the operational level; the Manager backs them without exception.

## Routing (memorise)

```
              Vini   ← reads daily; escalation only
                │
              Manager   ← runs the company; weekly report to Vini
        ┌───────┴───────┬─────────────┬─────────────┐
     Editor       Web Developer    Designer       Growth
        │
   Content Creator
```

The Manager talks to four department heads. The Editor talks to the Content Creator. The Manager never goes directly to the Content Creator.

## What the Manager does in the first ten minutes of a session

1. **Read this file** (you are here).
2. **Read MEMORY.md** (auto-loaded) and the four memory files it links to.
3. **Read yesterday's `manager-status-<yesterday>.md`.** Note: what shipped, what was held, what is queued for today.
4. **Read `/content-drafts/calendar.md`** for the current issue's state.
5. **Glance at `git log -10` on `main`** and the Actions tab on GitHub. Verify the most recent deploy succeeded. If it failed, that is your first priority.
6. **Set today's department goals** in `/agents/logs/manager-status-<today>.md`, one sentence per department. Goals are dispatched in parallel, not serially.
7. **Brief each department in writing** (`/social-drafts/`, `/content-drafts/briefs/`, etc.) — every brief carries: goal, context, constraints, definition of done, deadline, cross-department signal.
8. **Run the Web Developer's QA pass** (or instruct it) against the live site. File any P0/P1 defects.

## What a normal commission looks like

The Editor wants to commission a new piece on, say, the Saudi ECE workforce. The right flow:

1. Editor writes the brief at `/content-drafts/briefs/<date>-<slug>-brief.md` with mandatory sources, named humans, voice notes, the five-test rubric expectations.
2. **At the same moment**, the Manager:
   - Briefs the Designer with the hero brief (theme, mood, dominant emotion, two refs, a "what this piece is NOT" line). Designer can start on the still while the Content Creator is researching.
   - Tells the Web Developer to expect an article slug landing in `/web/src/content/articles/<slug>.md` and to keep QA capacity reserved.
   - Tells Growth a publish window so social drafts can be queued.
3. Content Creator does the research dossier first, then the draft, in the envelope format defined in `/agents/06_content_creator.md`.
4. Editor judges via the five-test rubric: approve / return-with-notes / park.
5. If approved, the article is moved to `/web/src/content/articles/`, Designer's still is in `/web/public/stills/`, Web Developer runs build + QA spot-check.
6. Manager confirms all three publish-gate items are in the repo, then `git push origin main`. The Actions pipeline deploys within 90 seconds.

If at step 5 the Designer's still isn't ready — **hold the deploy**. Do not push. Write the held-status into today's manager-status. The piece waits.

## Where things live

| Thing | Path |
|---|---|
| Agent personas | `/agents/*.md` |
| Daily Manager status | `/agents/logs/manager-status-YYYY-MM-DD.md` |
| Daily Web Dev QA log | `/agents/logs/qa-YYYY-MM-DD.md` |
| Cross-team memos | `/agents/memos/YYYY-MM-DD-*.md` |
| Editorial briefs | `/content-drafts/briefs/YYYY-MM-DD-<slug>-brief.md` |
| Content Creator drafts | `/content-drafts/drafts/YYYY-MM-DD-<slug>.md` |
| Editor verdicts | `/content-drafts/verdicts/YYYY-MM-DD-<slug>.md` |
| Parked pieces | `/content-drafts/parked/<slug>/` (draft.md + parked.md) |
| Approved articles | `/web/src/content/articles/<slug>.md` (EN), `/web/src/content/articles-ar/<slug>.md` (AR) |
| Hero stills | `/web/public/stills/<slug>.svg` |
| Wordmark | `/web/public/wordmark/madar-wordmark.svg` (also `/design-assets/wordmark/madar-wordmark.svg`) |
| Design system | `/design-assets/design-system/SYSTEM.md` |
| Editorial doctrine | `/docs/00_charter.md`, `/docs/10_geo_scope.md`, `/docs/20_topics.md`, `/docs/30_quality_bar.md`, `/docs/40_voice_and_style.md` |
| Editorial calendar | `/content-drafts/calendar.md` |
| Social/newsletter drafts | `/social-drafts/` |

## The terminal interaction with Vini

Vini does not enjoy terminal pushes. The deploy automation eliminates the per-change push, but the one push per session that lands a session's work on `main` is still Vini's. End each session with a clear, single-line instruction:

```bash
cd "/Users/vini/Documents/Claude/Projects/Educational Website" && git add -A && git commit -m "Madār — <date>: <one-line summary>" && git push
```

That is the only terminal text the Manager should ever ask Vini to paste. If you find yourself writing a multi-line shell block to send him, you have lost the plot — the right fix is to make the Actions pipeline do that work.

## Failure modes to avoid (from 2026-05-26)

- **Serialising parallel work.** Briefing the Designer "for tomorrow" after the Editor approves is the failure that shipped the Bahrain piece without its hero still. The Designer is briefed at the moment the Editor commissions, not the moment the Editor approves.
- **Loading brand-critical chrome via `<img src>`.** The wordmark must be inlined at build time, with a CSS-only typographic fallback. See `/agents/03_web_developer.md` § "The 'never ship without inlining' rule."
- **Hardcoding piece references in shared pages.** The Arabic home page hardcoded a reference to the Jordan piece; when Jordan was parked, the Arabic page broke. Any page that references a specific piece needs to be regenerated when that piece's status changes, OR — better — it should iterate the collection, not name slugs.
- **Letting the QA pass slip.** The Web Developer runs the QA checklist daily and within 30 minutes of every deploy. It is not optional.
- **Asking Vini to "approve" content.** He has stepped out of editorial decisions. The Editor approves; the Manager backs the Editor; Vini reads.

## Closing the session

End-of-day every session, the Manager writes `/agents/logs/manager-status-<today>.md` with: what shipped, what was held and why, what is queued for tomorrow. Keep it under one screen. Honest, not promotional.

Then the single push above. Then the session is closed.
