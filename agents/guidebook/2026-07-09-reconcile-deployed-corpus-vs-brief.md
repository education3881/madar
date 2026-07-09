# The brief states intent; the commit states fact — reconcile the deployed corpus, not the narrative
**Date:** 2026-07-09 · **Manager** · surfaced by the Edition 03 premature-publish episode (07-07) and found on the 07-09 state check.

## What happened
Brief 28 (07-07) described a conservative plan: *close Edition 02 with Morocco (the one gated piece), hold all fifteen Ed03/04 sprint drafts out of the build, corpus stays 20 EN / 20 AR.* The push block under it used `git add -A`. But on disk the ten Ed03 pieces carried `approved: true` in **both** languages. So the founder's `git add -A` push swept them into the commit, the build rendered them, and the deploy (run 38, green) put **ten pieces live** — a corpus of **30 EN / 30 AR**, not 20/20. The brief's *narrative* said "held"; the repository's *state* said "shipped." The state is what readers got.

It ended well only because the founder ruled *keep-live, verify-in-place* and the retroactive gate cleared Ed03 10/10. The bar held — but by recovery, not by design. The lesson is about the gap, not the outcome.

## The durable rule
**A brief is a plan; a commit is a fact; a deploy is the truth. Never verify the plan — verify the deployed state.** On every run's Step 1, after the git checks, reconcile three things that can silently disagree:
1. **What the last brief *said* shipped** (its narrative + its stats panel).
2. **What is actually `approved: true` on disk** (`grep -rl '^approved: true' web/src/content/articles*`), because that — not the prose — is what the article routes render.
3. **What the live sitemap actually serves** (`web_fetch …/sitemap-0.xml`), because that is what the reader and the crawler see.

When they diverge, the sitemap wins, then the disk, then the brief — and the divergence itself is the headline of the day.

## Why it recurs (the mechanism to design against)
- **`git add -A` on a founder push is a wide net.** It commits whatever is in the working tree, including files a sandbox run wrote but the brief intended to hold. Staging *out of the build directory* only works if the move persists to the founder's tree — bash file-moves in this sandbox often do not (FUSE boundary; see the 07-07 push note). **The reliable hold is the frontmatter flag (`approved: false`), not the directory.** The five Ed04 drafts held correctly *because they were flagged*, not because they were moved.
- **A stats tool that counts on-disk frontmatter will follow the flag error, not catch it.** `madar_stats.py` was counting every `*.md` regardless of `approved`, so it would have reported 35/31 as if published. **Fixed 2026-07-09:** the panel now reports the *approved (live)* corpus as the headline (30/30/100%) and discloses on-disk totals + held-draft counts as a separate line. The deterministic panel is now honest by construction — it can no longer overstate the site while drafts sit held in the content dir.

## Checklist to add to Step 1 (state verification)
- ☐ `approved:true` EN count == `approved:true` AR count (live parity), and == the sitemap's article count.
- ☐ Every held draft is `approved:false` (a *flag*, never merely a moved file).
- ☐ The last brief's stats panel matches `madar_stats.py` **approved** numbers — if not, the brief overstated or the flags slipped.
- ☐ Any `approved:false` piece with `related:` refs is reconciled *before* it flips true (graceful-filtered until then).

## Companions
Extends `2026-07-06-local-build-is-not-the-deploy.md` (#16) and `2026-07-07-deploy-pages-is-its-own-failure-class.md` (#17) with the corpus twin: *origin-commit-is-not-the-brief either.* The deploy has two gates (build + Pages config); the **corpus** has its own gate (the `approved` flag), and the brief is not it. Also pairs with the push-race note: `git add -A` sweeps in-progress files — write the flag you mean.
