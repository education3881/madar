# Manager status — 2026-10-08 (Thursday)

**State verified first, not read off the brief.** Tree clean, `HEAD == origin/main` at `4f63663`,
no dark day. Deploy `37616042671` success, all three jobs green. Yesterday's one named untested
surface — `qa_register_shape` inside a runner — ran there and passed.

## Shipped

- **The standing queue's head, taken by rule for the fourth consecutive morning: self-hosted
  fonts.** Item 4, raised 2026-09-18, 20 days, three displacements, oldest past the threshold. 34
  woff2 faces and five OFL notices under `web/public/fonts/`; the two `preconnect`s and the
  `fonts.googleapis.com` stylesheet gone from `Base.astro`. **Third-party requests per page 3 → 0;
  references across the site 360 → 0.** First [WD] item the rule has ever sent first — the three
  before it were all instruments, so this is the first evidence it surfaces served-byte work too.
- **`qa_third_party_origins`, standing assertion 31, gated from `postbuild`. 28 of 31 gate the
  deploy**, derived by `qa_patch_queue` from three homes. Proved 19 ways, bite first, on a `/tmp`
  copy; the first bite is this morning's own removed markup, not an invented one.
- **Edition 05, blocker 2 closed at 15 days — the fifth and last confirmation read. The edition's
  verification work is finished.** Both items the 09-23 verdict left owed are verified. The
  correction is to the verdict, not the piece: it recorded *"no Internet Archive snapshot exists"*
  twenty minutes after the capture it had itself requested had landed. Repaired in `sources[]`
  only, both editions, equal numeral multisets, 684 citations unchanged.
- **Rulings #91 and #92**, four counts moved for #91 and five for #92, with the register's four
  range homes derived by `qa_register_shape` rather than maintained.
- **Growth: the third-party surface measured at zero, and the Arabic edition measured from the
  reader's side of a blocked network** — 15 faces load with every external host blackholed; 0 with
  the bundle removed, which is where readers behind a blocked vendor have been since 2026-05-25.

## Held, and why

- **The brief template still fetches from the two origins the publication just stopped
  contacting.** Not changed today on purpose: that bundles a shared-template change into a font
  migration, which is the exact reasoning the 09-18 audit used to defer the fonts in the first
  place, and the relative path a brief needs is not guaranteed to resolve from wherever it is
  opened. Named as tomorrow's forward question instead of quietly done.
- **Queue item 8 opened rather than fixed:** `qa_served_manifest --check` compares a git-derived
  date against a working-tree build, so it reports a false *silent content change* on every chrome
  edit. Diagnosed and measured both ways; the fix is a home or a dirty-tree guard, which is a
  design call and not a patch.
- **Nothing on the edition was rushed.** Two blockers remain and neither needs a judgment.

## Queued

- **Tomorrow, first:** the forward question — the properties we gate the publication on that are
  false of the artefacts we render for ourselves.
- **Tomorrow, verify:** the font bundle has never been served by GitHub Pages. If the
  `Content-Type` or path differs, pages fall back silently and **no assertion we own would see
  it** — the check asserts where we do not point, not what arrives. First read of the day.
- **Edition 05, three days to the 10-11 target:** the packet captions' Arabic gate (7 days, now the
  edition's oldest item), the flip rehearsal re-run — made stale a second way today, since 10-01's
  green describes a tree whose every page still called Google — then the held-source sweep and the
  publish gate in writing.
- **For Sunday's review:** the queue's restraint test now reads 4 days against the 28 it was set
  at. That is a pass so large it has stopped discriminating, and I am not rescoring it quietly.

## Honest notes

- **Two things bit on my own work today** and both are recorded where they will be read: the
  register-shape gate caught the ruling file documenting a check, twice; and my own proof harness
  had a guard whose injection never reached the condition it was testing.
- **The commit changes what a reader receives, for the first time in eleven days.** All 119
  `lastmod` values *should* move. A date that does not move is the finding.
- No traffic figure is reported. The site carries no third-party tracker by design, and from today
  no third-party request of any kind — which is asserted, not claimed.

— Manager · 2026-10-08
