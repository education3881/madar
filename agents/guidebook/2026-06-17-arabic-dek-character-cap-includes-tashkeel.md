# Method — capped frontmatter strings count combining marks; a fully-voweled Arabic dek blows the 200-char cap early

**Banked:** 2026-06-17 · **Owner:** Arabic Editor / Web Developer · **Type:** production rule
**Cost when unbanked:** one failed build per AR ship. Caught at the gate on 2026-06-17 (Korea AIDT) — `InvalidContentEntryDataError: dek String must contain at most 200 character(s)`.

## The finding

The content schema caps `dek` at **200 characters**, and Astro/Zod measures **Unicode code points** (JavaScript `string.length`), not rendered glyphs. Arabic tashkeel — fatḥa ◌َ, ḍamma ◌ُ, kasra ◌ِ, the tanwīn ◌ً ◌ٌ ◌ٍ, shadda ◌ّ, sukūn ◌ْ — are **separate code points** that attach visually to the preceding letter but each add **+1** to the count. Madār's Arabic house style is heavily voweled, so a dek that *looks* ~150 characters can be 210+ code points and fail the build. (The EN dek can fail too, but only by being plain long — there is no hidden inflation; the Korea EN dek was simply over-written and also had to be trimmed.)

## The rule

1. **Keep the body fully voweled; keep the *dek* lightly voweled.** In the dek, apply tashkeel only where it genuinely disambiguates (a verb voice, a case ending that changes the reading) — not decoratively. The dek is a search/preview surface, not a recitation surface; light vowelling is correct there anyway.
2. **Count code points before staging**, for every capped string field (`dek`, and `title` if it carries a cap) in **both** language files. Don't eyeball Arabic length.
3. This generalises to **any** Zod-`.max()` string field that may hold Arabic — check it the same way.

## The check (drop into the pre-stage routine / publish gate)

```bash
python3 - "$SLUG" <<'PY'
import re, glob, sys
slug = sys.argv[1]
for f in sorted(glob.glob(f'web/src/content/articles*/{slug}.md')):
    t = open(f, encoding='utf-8').read()
    for field in ('title', 'dek'):
        m = re.search(rf'^{field}:\s*"(.*)"\s*$', t, re.M)
        if m:
            n = len(m.group(1))
            flag = '  <-- OVER 200' if (field == 'dek' and n > 200) else ''
            print(f'{n:4d}  {field:5}  {f.split("/")[-1]}{flag}')
PY
```

Run it with `SLUG=2026-06-17-korea-aidt-reversal`. Green = every dek ≤ 200. Add the line to `qa-<date>.md`.

## Cross-refs
- [[2026-06-15-astro-build-in-sandbox-vite-cache-route]] — the real build that surfaces this (a structural proxy would not have).
- [[2026-06-16-sourcing-one-party-policy-reform-and-vietnamese-transliteration]] — the frontmatter-key-parity ruling; same family of lesson (frontmatter defects build clean or fail loud, but only a real build tells you which).
