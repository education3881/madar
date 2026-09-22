# Ruling #60 — A date is not a moment

**Filed:** 2026-09-22 (daily run, testing the 2026-09-21 forward question)
**Family:** Assertion discipline / build determinism — with #57, #58, #59
**Standing assertion earned:** 22, `qa_date_identity.py`
**Status:** Binding.

---

## The ruling

**A calendar date is a day. An instant is a point on a timeline. They are not the
same kind of thing, and every conversion between them invents a timezone.**

Where a publication stores a day (`2026-09-19`) and renders a day (*September 19,
2026*), nothing in between may quietly become a moment. If a parser turns the day
into an instant, that instant is **pinned to the zone the value was parsed in**,
explicitly, at every point it is read back out — never to the machine that happens
to be formatting it.

## Origin

`web/src/content/config.ts` declares `date: z.coerce.date()`. Zod's coercion hands
the bare `YYYY-MM-DD` string to `new Date()`, which parses a date-only ISO string
as **UTC midnight**. Eight `Intl.DateTimeFormat` instances — four English, four
Arabic, one per route that prints a dateline — then formatted that instant with
**no `timeZone` option**, which means each asked the build machine what day the
instant was.

Every runner behind UTC answers with the day before.

Proved today, against the served shape and not against the source: the same
commit, built once under `TZ=UTC` and once under `TZ=America/Los_Angeles`,
produced **116 of 121 pages different**, and the Singapore piece dated
`2026-07-07` printed *July 6, 2026* in English and the Arabic equivalent in
Arabic-Indic digits. The publication's own CI is UTC and the operation's calendar
is Asia/Dubai (UTC+4); both land on the correct side of midnight. **Four months of
correct datelines were luck, not a guard.**

After the fix — `timeZone: 'UTC'` named at all eight sites — a Los Angeles build
is byte-identical to a UTC build across all 121 pages. That is #58's test applied
to the clock: *the build is a function of its sources.*

## Why nothing saw it

Every instrument this operation owns reads `dist` and compares it to itself, or to
the origin, or to another instrument. **Nothing compared a rendered date to the
frontmatter that produced it.** The three date-shaped surfaces that *are* checked
are checked on other grounds: `qa_lastmod` asserts the sitemap's dates against a
git ceiling (file provenance, not frontmatter); `qa_ar_language` asserts the
Arabic listing date is in Arabic-Indic **digits** (script, not value);
`qa_feed_enclosures` never reads `pubDate`. A shifted date passes all three — it
is a well-formed date, in the right script, with a plausible provenance. It is
simply the wrong day.

And the defect is invisible from inside the machine that has it: on a UTC runner
there is nothing to see, which is why the 09-21 log had to *predict* it rather
than trip over it.

## Corollaries

1. **The zone belongs to the value, not to the viewer.** A publication date is a
   fact about the day a piece was filed. It does not change when the reader
   travels, and it must not change when the builder does.
2. **`toISOString()` is not a counterexample, it is the same rule obeyed.** The
   sitemap resolver and the JSON-LD builder were already correct, because they
   serialise in UTC by construction. The defect lived only where a *human-facing*
   format was chosen, which is where a locale and a zone are both required and
   only the locale had ever been thought about.
3. **#59's corollary 3 predicted half of this and stopped one field short.**
   That ruling caught `Intl.DateTimeFormat('ar')` numbering in `latn` — the same
   constructor, the same missing explicitness, a different option. A ruling that
   names one unspecified default should be read as a prompt to enumerate the
   others on the same call.
4. **The assertion must not be able to read its answer off the thing it checks.**
   `qa_date_identity` builds its expected strings in Python from month tables
   transcribed out of `en-US` and `ar-EG`, so it shares no clock, no locale and no
   formatter with the site. An assertion that asked `Intl` what the date should be
   would agree with the defect.

## The assertion, and what proving it cost

`agents/tools/qa_date_identity.py` — 76 article datelines and 232 listing dates,
each compared to its own piece's frontmatter, in the language the page is written
in, Arabic in Arabic-Indic digits. Gated from `web/package.json` `postbuild`, per
the 2026-09-14 rule (an autonomous run cannot write `.github/workflows/**`, so an
assertion is gated somewhere the build actually runs and says where). Registered
in `qa_census` against `qa_body_links`' population, per #57.

Proved six ways — control clean on the real build, and five bites: the pre-fix
Los Angeles build (308 findings), one listing date moved a day (1 finding), an
article page stripped of its dateline, an Arabic listing date reprinted in Latin
digits, one article page deleted from the build (the population floor), and the
`postbuild` gate itself failing a real `npm run build` with the regression
reinstated in one file.

**Two traps caught while proving it, both of them #35's *prove the bite as
carefully as the control*:**

- **The first draft failed its own control.** Its carrier regex closed on a fixed
  `</div>|</p>`, so one `<span class="piece__date">` on the editions index
  swallowed every list item after it and paired nine dates with the first slug on
  the page. A known-good build reported 46 findings. The fix was to capture the
  element's own tag name and close on that — the 2026-09-14 trap on the input
  side, an assertion scoped wider than the thing it checks.
- **The Latin-digits bite did not bite, and the tool still said PASS.** A carrier
  whose contents the language's date pattern cannot match was being *skipped*, so
  the real 09-21 defect — nine Arabic pages printing `7 يوليو 2026` — walked
  through it while the total quietly fell from 232 to 231. A date carrier that
  yields nothing readable is now a finding, not a skip. **A total that moves is a
  check that stopped checking something.**

## Binding

1. Every conversion between a stored day and a rendered day names its zone
   explicitly, at the point of formatting.
2. Any new date surface — a format, a sort, a bucket, a feed field — is added
   with its zone named in the same commit, and `qa_date_identity`'s carrier list
   is extended to it in that commit or the surface states why it is out.
3. A rendered value is asserted against **the field that produced it**, not
   against another rendering of the same field. The three date checks that
   existed all compared a date to something other than its own frontmatter, and
   that is exactly why all three were green.

*Related:* [[2026-09-21-a-comparator-with-no-locale-asks-the-machine]] ·
[[2026-09-20-a-comparator-that-returns-zero-is-a-decision-delegated]] ·
[[2026-09-19-equal-counts-are-not-an-agreement]]
