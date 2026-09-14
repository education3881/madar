#!/usr/bin/env python3
"""
qa_geo_fields.py — assert the geography fields against their display map, and
assert the optional `countries` list against the piece that declares it.

WHY (2026-09-14)
----------------
Today the schema gained its first new field since launch: `countries`, an
optional ordered list for a continental piece whose honest deliverable is four
rulers crowning four different countries. The field has three consumers — the
English marginalia, the Arabic marginalia, and `madar_stats.py`'s "Countries
covered" count — and every one of them can fail silently:

  * a name not in COUNTRY_AR falls through to the English fallback, which is
    the 2026-08-23 defect (235 Arabic-page fields printing English) reopened
    through a new door;
  * a `countries` list that omits its own `country` makes the marginalia
    contradict the byline on the same page;
  * an EN/AR twin pair whose lists differ makes the two editions of one piece
    claim to have measured different continents;
  * a duplicate inside the list inflates nothing today (`tally_countries`
    de-duplicates) but would inflate any consumer that did not.

THE SHAPE OF THIS CHECK, AND WHY IT READS SOURCE AND NOT ONLY DIST
------------------------------------------------------------------
The piece that introduces the field is HELD (`approved: false`), so it is not
in `dist` and cannot be — that is the whole point of the hold, and of
`qa_held_assets`. An output-side-only assertion would therefore have its first
real run on flip day, which is the one day nobody wants a new check to bite.

So this check has two halves and runs both, always:

  SOURCE half (every run, held or not) — reads the content files. Every
  `country` and every `countries` member in both collections resolves in the
  display map; `country` is a member of `countries`; no duplicates; a
  `countries` list of one is a `country`, not a list; and EN/AR twins declare
  the same set.

  OUTPUT half (only for pieces actually in dist) — the rendered marginalia
  carries the list, in the right script on each side. Pieces absent from dist
  are counted and reported as skipped-because-held, never as passed.

Neither half may pass silently: zero files located, or zero pieces checked in
a collection that has files, is an error (2026-08-16 trap).

Usage:  python3 agents/tools/qa_geo_fields.py [<dist-dir>]
Exit 0 = clean. Exit 1 = defect. Exit 2 = the check could not check.
"""
import sys, os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EN_DIR = os.path.join(ROOT, 'web', 'src', 'content', 'articles')
AR_DIR = os.path.join(ROOT, 'web', 'src', 'content', 'articles-ar')
GEO_TS = os.path.join(ROOT, 'web', 'src', 'lib', 'i18n-geo.ts')

ARABIC = re.compile(r'[\u0600-\u06FF]')
LATIN = re.compile(r'[A-Za-z]')


def display_map_keys():
    """The keys of COUNTRY_AR, read from the TypeScript the site actually uses.

    Derived, not duplicated (#36): a second hand-written list of 50-odd country
    names in this file would drift against the map within a month, and the
    drift would be invisible because both would be "our" data.
    """
    src = open(GEO_TS, encoding='utf-8').read()
    m = re.search(r'COUNTRY_AR[^=]*=\s*\{(.*?)\n\};', src, re.S)
    if not m:
        return None
    keys = set()
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith('//'):
            continue
        km = re.match(r"""^'([^']+)'\s*:|^"([^"]+)"\s*:|^([A-Za-z_][A-Za-z0-9_]*)\s*:""", line)
        if km:
            keys.add(km.group(1) or km.group(2) or km.group(3))
    return keys


def frontmatter(path):
    txt = open(path, encoding='utf-8').read()
    if not txt.startswith('---'):
        return None, ''
    end = txt.find('\n---', 3)
    return txt[3:end], txt[end + 4:]


def scalar(fm, key):
    m = re.search(r'^%s:\s*(.+?)\s*$' % re.escape(key), fm, re.M)
    if not m:
        return None
    v = m.group(1).strip()
    if v[:1] in '"\'' and v[-1:] == v[:1]:
        v = v[1:-1]
    return v


def inline_list(fm, key):
    """Reads `key: [A, B, C]` — the form the corpus uses for themes and here."""
    m = re.search(r'^%s:\s*\[(.*?)\]\s*$' % re.escape(key), fm, re.M)
    if not m:
        return None
    return [x.strip().strip('"\'') for x in m.group(1).split(',') if x.strip()]


def collection(d):
    out = {}
    for p in sorted(glob.glob(os.path.join(d, '*.md'))):
        fm, _ = frontmatter(p)
        if fm is None:
            continue
        out[os.path.basename(p)[:-3]] = {
            'path': p,
            'country': scalar(fm, 'country'),
            'countries': inline_list(fm, 'countries'),
            'approved': (scalar(fm, 'approved') or 'false').lower() == 'true',
        }
    return out


def main(dist='web/dist'):
    keys = display_map_keys()
    if not keys:
        print('ERROR: could not read COUNTRY_AR from %s.' % GEO_TS)
        return 2

    en, ar = collection(EN_DIR), collection(AR_DIR)
    if not en or not ar:
        print('ERROR: 0 article files located (EN %d, AR %d).' % (len(en), len(ar)))
        return 2

    defects = []
    checked = 0
    with_list = []

    for label, coll in (('EN', en), ('AR', ar)):
        for slug, d in coll.items():
            checked += 1
            c, cs = d['country'], d['countries']
            if not c:
                defects.append((label, slug, 'no country field'))
                continue
            if c not in keys:
                defects.append((label, slug, 'country not in display map: %s' % c))
            if cs is None:
                continue
            with_list.append((label, slug))
            if len(cs) < 2:
                defects.append((label, slug, 'countries has %d entry; a list of one is a country' % len(cs)))
            if len(set(cs)) != len(cs):
                defects.append((label, slug, 'countries contains a duplicate: %s' % cs))
            if c not in cs:
                defects.append((label, slug, 'country %r is not a member of countries %s' % (c, cs)))
            for name in cs:
                if name not in keys:
                    defects.append((label, slug, 'countries member not in display map: %s' % name))

    # EN/AR twins must claim the same set.
    for slug, d in en.items():
        if slug in ar:
            a, b = d['countries'], ar[slug]['countries']
            if (a or []) != (b or []):
                defects.append(('PAIR', slug, 'EN countries %s != AR countries %s' % (a, b)))

    # ---- OUTPUT half: only for pieces that are actually in dist. ----
    rendered = skipped = 0
    if os.path.isdir(dist):
        for label, slug in with_list:
            sub = 'ar/articles' if label == 'AR' else 'articles'
            page = os.path.join(dist, sub, slug, 'index.html')
            if not os.path.exists(page):
                skipped += 1
                continue
            rendered += 1
            html = open(page, encoding='utf-8', errors='replace').read()
            m = re.search(r'<aside class="body-right marginalia"[^>]*>(.*?)</aside>', html, re.S)
            block = m.group(1) if m else ''
            src = (en if label == 'EN' else ar)[slug]['countries'] or []
            # Read the LIST LINE, not the whole marginalia block. The primary
            # `country` is already printed on the line above, so a block-wide
            # search would report the list as rendered when only the primary
            # survived — the check would be masked by the very field it exists
            # to supplement. The <p> carries Astro's scoped-CID attribute, so
            # the tag pattern must allow attributes.
            line = re.search(r'<p[^>]*>\s*(?:Measured|المقيسة)\s*·(.*?)</p>', block, re.S)
            line_txt = line.group(1) if line else ''
            if not line_txt:
                defects.append((label, slug, 'declares `countries` but renders no list line in the marginalia'))
                continue
            if label == 'EN':
                missing = [n for n in src if n not in line_txt]
                if missing:
                    defects.append((label, slug, 'countries not rendered in marginalia: %s' % missing))
            else:
                block = line_txt
                # The Arabic marginalia must carry the list in ARABIC, so the
                # English names must be ABSENT and Arabic script present.
                leaked = [n for n in src if re.search(r'(?<![A-Za-z])%s(?![A-Za-z])' % re.escape(n), block)]
                if leaked:
                    defects.append((label, slug, 'Latin country name in Arabic marginalia: %s' % leaked))
                if not ARABIC.search(block):
                    defects.append((label, slug, 'Arabic marginalia carries no Arabic script'))

    if checked == 0:
        print('ERROR: 0 pieces checked. An assertion that finds nothing to check has failed.')
        return 2

    print('qa_geo_fields: %d pieces checked (EN %d / AR %d); %d declare `countries`; '
          'output half: %d rendered, %d held and not in dist.'
          % (checked, len(en), len(ar), len(with_list), rendered, skipped))
    if defects:
        print('DEFECT (%d):' % len(defects))
        for lab, slug, why in defects[:25]:
            print('  %-5s %-46s %s' % (lab, slug, why))
        return 1
    print('CLEAN — every country resolves in the display map; every `countries` list '
          'contains its own `country`; EN/AR twins agree.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'web/dist'))
