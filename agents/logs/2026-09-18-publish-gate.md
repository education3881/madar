# Publish gate — 2026-09-18

**Run in writing before the commit, per the CHARTER. Outcome: NOTHING FLIPS TODAY, and
nothing was going to.** The gate is recorded anyway because two **held** editorial files
were edited in this run, and a held file that has been edited is a file whose hold has to
be re-verified rather than assumed.

## What changed in the content collection

| File | Change | Flag |
|---|---|---|
| `articles/2026-09-14-africa-best-system-ruler.md` | ruler-two crown widened to the register's four (Editor decision 1); source 9 locator moved to the Internet Archive capture, annotation rewritten (Editor decision 5) | `approved: false` — **unchanged** |
| `articles-ar/2026-09-14-africa-best-system-ruler.md` | the same two changes, composed in Arabic | `approved: false` — **unchanged** |

No other content file was touched. **No `approved:` value changed anywhere in the
repository**, verified by grep over both collections: 76 approved, 8 held, exactly as
yesterday.

## The gate items, stated rather than assumed

| Item | State |
|---|---|
| Editor five-test pair verdict | on file, 09-15 PASS |
| Verifier verdict | on file, 09-17 FAIL-5 → **all five now closed** (3 in-run on 09-17, items 3 and 5 today) |
| Arabic Editor gate | on file, 09-14 PASS + 09-15 addendum |
| Arabic Editor, two register questions (¶48, ¶60) | **still owed** — routed 09-15, unanswered |
| Hero still and og card | on disk, withheld from `dist` by the build |
| Confirmation reads, all three pairs | **owed at the gate**, none done |
| Reciprocal `related:` edges into row 4 | **owed at the flip commit** |
| `qa_sources_alive --held-only --sample 0` | **cannot be scheduled** — P1, third day |
| `astro build` clean | yes, exit 0 |
| Standing assertions | 16 of 16 gated, all green |
| Held-slug leak | **zero** — `qa_held_assets` CLEAN; `qa_lastmod` confirms 8 held files contribute no date |

**Four items are open and three of them are operational.** The wave does not flip until
they close. Today's work removed the last *editorial* obstruction, which is a different
thing and is not a gate.

## Checks re-run specifically because held files were edited

- `qa_body_links` — **PASS**. The new Internet Archive locator renders on the built page,
  and a source URL that did not resolve would have failed here.
- `qa_geo_fields` — **CLEAN**. Re-run because Editor decision 3 considered adding Gabon
  and Burkina Faso to `countries:` and decided against; the field is unchanged at five and
  every name still resolves in the display map.
- `qa_held_assets` — **CLEAN**. Both edited files are still held and still contribute no
  bytes; their still and og card are still withheld.
- `qa_lastmod` — **PASS**. Editing a held file moved no live `<lastmod>`, which is the
  2026-09-08 invariant checked against the artefact rather than assumed from the code.
- Numeral multiset, both languages, after every edit — **EN 110 / AR 103, zero
  Arabic-only figures**; the seven English-only tokens are the grade labels.

## Assets

No new hero still, no new og card, no asset added or removed. Nothing to place and nothing
to withhold that was not already withheld.

## Verdict

**GATE NOT CROSSED, DELIBERATELY.** The commit carries two edited held drafts, one repaired
standing assertion, one new standing assertion, four written decisions, one ruling and the
day's logs. It publishes no new page, no new sitemap entry, no new feed item and no new
date. Corpus stays at **38 EN / 38 AR**.

— Manager · 2026-09-18
