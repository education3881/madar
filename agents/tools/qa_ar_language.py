#!/usr/bin/env python3
"""
qa_ar_language.py — assert that an Arabic page is Arabic to the reader.

WHY (2026-08-23)
----------------
Every check we owned passed while every Arabic page in the corpus printed
"Sierra Leone · Africa" to an Arabic reader. Parity counted 38 AR files
against 38 EN files. The pages built. The links resolved. `lang="ar"` and
`dir="rtl"` were present and correct — in fact the worst offender was:

    <span class="piece__country" lang="ar" dir="rtl">{piece.data.country}</span>

markup that ASSERTS the content is Arabic and then puts Latin text inside it.
Nothing we ran read the words. Parity counted files, not language.

WHAT THIS CHECKS, AND WHAT IT DELIBERATELY DOES NOT
---------------------------------------------------
It checks the CHROME — the fields the site itself generates from frontmatter:
byline meta, the marginalia «المرجع الميداني» block, the related-reading meta,
and the country tag on listing pages.

It does NOT check article body text or the sources list, because Latin script
there is CORRECT and required: ruling #28a keeps an institution's own Latin tag
("Universidad de Santiago de Chile", "India TV News (PTI)", "Uruguay XXI") and
never re-initialises it from an Arabic gloss. A check that flagged those would
train the team to ignore it. 8 such hits exist today; all are legitimate.

It also refuses to pass silently. Per the 2026-08-16 trap, an assertion that
finds nothing to check has FAILED, not passed — so a run that locates zero
chrome fields is an error, not a green.

Usage:  python3 agents/tools/qa_ar_language.py <dist-dir>
Exit 0 = clean. Exit 1 = defect. Exit 2 = the check could not check.
"""
import sys, os, re, glob, html

# Controlled vocabularies that must never reach an Arabic reader untranslated.
LATIN_VOCAB = [
    # regions (the schema enum)
    'MENA', 'Africa', 'Asia', 'LatAm-Caribbean', 'Europe', 'N-America', 'Oceania', 'Other',
    # levels
    'K-12', 'ECE', 'Both',
    # themes
    'AI-readiness', 'ECE access', 'access', 'curriculum',
    'education for displaced children', 'female education', 'government-led programs',
    'inspiring stories', 'language and heritage preservation', 'national identity',
    'parent-led projects', 'student wellbeing', 'sustainability', 'value of teachers',
]

# Chrome containers, by class. Each is a field the SITE writes, not the writer.
CHROME_PATTERNS = [
    (r'<p class="kicker-meta"[^>]*>(.*?)</p>', 'byline meta'),
    (r'<aside class="body-right marginalia"[^>]*>(.*?)</aside>', 'marginalia'),
    (r'<span class="related__meta"[^>]*>(.*?)</span>', 'related meta'),
    (r'<span class="piece__country"[^>]*>(.*?)</span>', 'listing country'),
]


# Deliberately-English strings that are CORRECT on an Arabic page.
# A language switch is labelled in its TARGET language — the Arabic page says
# "English version ↗" for exactly the reason the English page says
# «النسخة العربية ↗». Both carry an explicit lang attribute so assistive tech
# switches voice. Allowlisted with the reason, never silently ignored.
ALLOWED_EN = ['English version']


def text_of(fragment: str) -> str:
    # Drop any element that declares itself as another language — a correctly
    # marked-up foreign-language span is not a defect, it is the fix.
    fragment = re.sub(r'<(\w+)[^>]*\slang="en"[^>]*>.*?</\1>', ' ', fragment, flags=re.S)
    return html.unescape(re.sub(r'<[^>]+>', ' ', fragment))


def main(dist: str) -> int:
    pages = sorted(glob.glob(os.path.join(dist, 'ar', '**', 'index.html'), recursive=True))
    if not pages:
        print('ERROR: no Arabic pages found — the check could not check.')
        return 2

    checked = 0
    defects = []
    for page in pages:
        src = open(page, encoding='utf-8').read().split('</head>', 1)[-1]
        for pattern, label in CHROME_PATTERNS:
            for m in re.finditer(pattern, src, re.S):
                checked += 1
                txt = text_of(m.group(1))
                # Any Latin letter run in a chrome field is suspect; the
                # controlled vocabulary makes the report specific.
                hits = [
                    v for v in LATIN_VOCAB
                    if re.search(r'(?<![A-Za-z-])' + re.escape(v) + r'(?![A-Za-z-])', txt)
                ]
                stray = re.findall(r'[A-Za-z][A-Za-z ]{2,}', txt)
                if hits or stray:
                    defects.append((page[len(dist):], label, hits or stray[:3]))

    if checked == 0:
        print('ERROR: 0 chrome fields located across %d Arabic pages.' % len(pages))
        print('An assertion that finds nothing to check has failed, not passed.')
        return 2

    print('qa_ar_language: %d Arabic pages, %d chrome fields checked.' % (len(pages), checked))
    if defects:
        print('DEFECT — Latin script in Arabic chrome (%d):' % len(defects))
        for path, label, hits in defects[:25]:
            print('  %-52s %-16s %s' % (path, label, hits))
        return 1
    print('CLEAN — no Latin-script controlled vocabulary in Arabic chrome.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'web/dist'))
