# Postmortem — 2026-05-26

**For the next session of the Manager** — a short, blameless record of what went wrong today, what was learned, and what rules now exist to prevent recurrence. Tomorrow's session should read this once, internalise the rules, and never see the same failures again.

---

## What went wrong (in order)

### 1. The home-page wordmark broke

The home page loaded the wordmark via `<img src="/madar/wordmark/madar-wordmark.svg">`. The SVG uses `fill="currentColor"`, which inside an `<img src>` context resolves to the SVG element's own default color (black), not the host page's `--color-ink`. The deployed file's bytes were fine; the way it was being loaded was the problem. There was also no fallback if the file ever 404'd.

Vini noticed this morning. Diagnosis took about thirty minutes of unnecessary digging because I checked the file's existence, the deploy state, and the GitHub Pages source before reading the actual rendering path in `index.astro`.

**Lesson:** When a user reports "X looks wrong," read the rendering code first, then the asset, then the deploy. Not the other way around.

**Rule added:** Web Developer persona § "The 'never ship without inlining' rule" — any visual element that is essential to the page identity is inlined at build time with a CSS-only fallback.

### 2. Two pieces shipped with fabricated source apparatus

Issue 01 went out on 2026-05-25 with three pieces, two of which carried a visible "Draft — pending source verification" pill. That pill was a fig leaf. The right call at the time was to hold the issue until the sources verified or to ship Sierra Leone alone.

The structural fix was not "be more careful next time." It was to restructure the Editor role so the verdict is binding and the rubric is explicit. A new Content Creator agent now writes the drafts; the Editor judges them on the five-test rubric and parks anything that fails Test 1 (sourcing reality).

**Lesson:** When a process has shipped weak work twice in a row, the fix is structural, not exhortative. "Try harder" is not a rule.

**Rules added:** Editor's five-test verdict rubric in `/agents/02_editor.md`. The "Draft — pending source verification" pill is retired as a design pattern.

### 3. The Bahrain piece shipped without its hero still

The Editor approved the Bahrain piece at midday. I (Designer) had the brief in hand. I treated "produce the hero still" as a P1 deferred-to-tomorrow item and let the Web Developer push without it. The article went to production referencing a file that didn't exist on disk.

Vini caught it in the evening: *"I can't have something being published and the designer seating idle all day because you didn't coordinate well."*

This was the day's most embarrassing failure — exactly the cross-department mis-orchestration the Manager exists to prevent.

**Lesson:** Brief in parallel, not in series. The Designer's hero brief goes out at the moment the Editor commissions, not the moment the Editor approves. The publish gate enforces that all three deliverables (Editor verdict, Designer hero, Web Developer build) are present on `main` before any deploy.

**Rules added:** Manager persona § "The publish gate" and § "Parallel coordination, not sequential dispatch." Feedback memory rule 7.

### 4. The deploy required hours of terminal interaction with the founder

Vini was meant to "push the working tree" — one command. Instead, the local `.git` was in an orphan state (no remote, no commits) because of an earlier sandbox-era issue. Re-attaching to GitHub took a `.git` rebuild via clone. Then the first push failed because the PAT lacked `workflow` scope. Then the next push deployed a stale local `dist/` because `npm run build` failed silently (Node wasn't installed). The whole detour cost roughly an hour of Vini's evening.

Vini's framing: *"I don't and won't be going through 100 terminal pushes every day with you. Let's solve the issue now, so you never depend on me to update the website."*

**Lesson:** The deploy pipeline must be runnable without the founder at his terminal. Manual `git worktree` is a debugging tool, not a workflow.

**Rules added:** Feedback memory rule 8. GitHub Actions workflow at `.github/workflows/astro-pages.yml` is the deploy mechanism; Pages source is set to "GitHub Actions"; every push to `main` triggers an auto-deploy.

## What now exists that didn't this morning

- `/agents/RUNBOOK.md` — the first file every new Manager session reads.
- `/agents/06_content_creator.md` — the new sixth-agent persona.
- `/agents/02_editor.md` — rewritten for judgment-not-production.
- `/agents/01_manager.md` — narrowed remit; publish gate codified; parallel-coordination rule.
- `/agents/03_web_developer.md` — mandatory QA mandate; "never ship without inlining" rule.
- `/agents/README.md` — rewritten with the six-agent routing diagram.
- `/agents/memos/2026-05-26-manager-to-editor-sourcing.md` — the policy memo on parks and sourcing rigor.
- `/agents/logs/qa-2026-05-26.md` — the first daily QA log.
- `/agents/logs/manager-status-2026-05-26.md` — the first end-of-day status.
- `/content-drafts/briefs/2026-05-26-replacement-A-brief.md` (Bahrain) — landed and shipped.
- `/content-drafts/briefs/2026-05-26-replacement-B-brief.md` (Egypt EKB) — open; Content Creator draft due 2026-05-28.
- `/content-drafts/parked/2026-05-25-jordan-double-shift/parked.md` and `/content-drafts/parked/2026-05-25-colombia-escuela-nueva/parked.md`.
- `/content-drafts/verdicts/2026-05-26-bahrain-bqa-public-grades.md`.
- `/social-drafts/2026-05-26-designer-instagram-and-issue01.md` and `/social-drafts/2026-05-26-growth-substack-and-instagram.md` — briefs; deliverables open.
- `/web/public/stills/2026-05-26-bahrain-bqa-public-grades.svg` — the Bahrain hero, made tonight, late.
- `/web/public/wordmark/madar-wordmark.svg` — now inlined into pages, not loaded via `<img src>`.
- `.github/workflows/astro-pages.yml` — the auto-deploy workflow.

## What is queued for tomorrow

In order of priority, from the open backlog:

1. **Content Creator: Egypt EKB draft** in the envelope format, by end of 2026-05-28. Brief at `/content-drafts/briefs/2026-05-26-replacement-B-brief.md`.
2. **Designer: Instagram visual deliverables** — profile photo (PNG + SVG), grid post templates (lead, curated, pull-paragraph, quiet rule), story templates (new piece, reading shelf). Brief at `/social-drafts/2026-05-26-designer-instagram-and-issue01.md`.
3. **Growth: copy deliverables** — Substack welcome email, Issue 01 Substack post copy, Instagram caption drafts for the first nine posts. Brief at `/social-drafts/2026-05-26-growth-substack-and-instagram.md`.
4. **Web Developer P1: implement the RSS feed.** Footer references `/madar/rss.xml` but the build doesn't produce it. Install `@astrojs/rss`; add `src/pages/rss.xml.js`. ~30 minutes.
5. **Web Developer P2: retire the "Placeholder wordmark v0.2" caption** from under the masthead, since the wordmark is now in production at v0.3.
6. **Housekeeping:** delete `/Users/vini/Documents/Claude/Projects/Educational Website/.git.broken-2026-05-26/` (540KB of stale clutter, gitignored but on disk).

## A note on tone for the next session

Vini's standing message — *"Make me proud. Remember: quality."* — is the frame. The day went well in substance (the Bahrain piece is real reporting; the parks were the right call; the auto-deploy is set up) and poorly in coordination (the Bahrain image gap; the terminal detour). The next session should hold the substance bar and fix the coordination.

He has signalled trust. Do not bother him with operational debris. End the next day with a clean weekly-report-style status; let him read it on Monday.
