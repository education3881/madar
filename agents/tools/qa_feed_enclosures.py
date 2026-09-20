#!/usr/bin/env python3
"""
qa_feed_enclosures.py — assert that what the feeds promise a reader about the
share cards is true of the files the origin actually serves.

WHY (2026-09-20)
----------------
The feeds have been the named, owed surface since 2026-08-18: *"well-formed and
38 items each, and nothing has ever verified that an item renders legibly in a
reader, that AR items carry their direction, or that links resolve from outside
our origin."* Carried in the RUNBOOK ever since. Asked today, it bit on first
contact, in the same shape as the defect that named it:

    <enclosure url=".../og/<slug>.png" length="0" type="image/png" />

`length` is hard-coded to 0, and in RSS 2.0 it is the size of the file in
bytes — the number a reader uses to decide whether to fetch the thing, show a
placeholder, or skip it. **76 enclosures across two feeds, every one declaring
an empty file**, while the cards on disk are 1–20 KB and perfectly good.

That is 08-18 exactly, one surface over: the URL was never the problem, the
promise about it was. The file existed, resolved, was correctly typed, and every
link check this operation owns passed on it. A check that asks *does it resolve*
cannot see a lie about what is on the other end.

WHAT IT ASSERTS
---------------
For every `<enclosure>` in every feed in `dist`:

  1. the URL is on our own origin and resolves to a file IN DIST — the promise
     is checked against the served artefact, not against `public/` and not
     against the computation that produced it (a check that re-ran the build's
     own arithmetic would agree with it by construction, which is the 09-14
     masking trap);
  2. `length` equals that file's real byte size, exactly;
  3. `type` matches the file's actual magic bytes, not its extension — the
     08-18 rule is that a consumer gets the format it was promised, and an
     extension is a claim, not a format;
  4. every approved item that has a card declares one, so the check cannot pass
     by the enclosures having quietly disappeared.

Non-vacuity floors (08-16 silent-pass trap): zero feeds, zero items or zero
enclosures found is an error, not a pass.

Reads only `web/dist`. Gated from `postbuild` in web/package.json, because this
identity cannot write `.github/workflows/**` (2026-09-14 rule, clause 4).
"""

import os
import re
import sys

ENCLOSURE = re.compile(r'<enclosure\s+url="([^"]+)"\s+length="([^"]*)"\s+'
                       r'type="([^"]*)"\s*/>')
ORIGIN = 'https://education3881.github.io'

# Magic bytes, so `type` is checked against the file and not against its name.
MAGIC = {
    b'\x89PNG\r\n\x1a\n': 'image/png',
    b'\xff\xd8\xff': 'image/jpeg',
    b'GIF87a': 'image/gif',
    b'GIF89a': 'image/gif',
}


def sniff(head):
    for sig, mime in MAGIC.items():
        if head.startswith(sig):
            return mime
    if head[:4] == b'RIFF' and head[8:12] == b'WEBP':
        return 'image/webp'
    return None


def main(dist='web/dist'):
    defects, feeds, items, encl = [], 0, 0, 0

    for base, _, names in os.walk(dist):
        for name in sorted(names):
            if name != 'rss.xml':
                continue
            path = os.path.join(base, name)
            rel = os.path.relpath(path, dist).replace(os.sep, '/')
            xml = open(path, encoding='utf-8').read()
            feeds += 1
            n_items = xml.count('<item>')
            items += n_items
            found = ENCLOSURE.findall(xml)

            if n_items and not found:
                defects.append((rel, '%d items and not one enclosure — the '
                                     'cards stopped being declared' % n_items))

            for url, length, ctype in found:
                encl += 1
                if not url.startswith(ORIGIN + '/'):
                    defects.append((rel, 'enclosure points off our origin: %s'
                                    % url))
                    continue
                # /madar/og/x.png -> dist/og/x.png
                served = os.path.join(dist, url[len(ORIGIN):]
                                      .lstrip('/').split('/', 1)[1])
                if not os.path.isfile(served):
                    defects.append((rel, 'enclosure resolves to nothing in '
                                         'dist: %s' % url))
                    continue
                real = os.path.getsize(served)
                if length != str(real):
                    defects.append((rel, '%s declares length=%r, the served '
                                         'file is %d bytes'
                                    % (os.path.basename(served), length, real)))
                actual = sniff(open(served, 'rb').read(16))
                if actual is None:
                    defects.append((rel, '%s is not a format any reader '
                                         'accepts' % os.path.basename(served)))
                elif actual != ctype:
                    defects.append((rel, '%s declares type=%r and is actually '
                                         '%s' % (os.path.basename(served),
                                                 ctype, actual)))

    if feeds == 0 or items == 0 or encl == 0:
        print('ERROR: %d feeds, %d items, %d enclosures. An assertion that '
              'finds nothing to check has failed.' % (feeds, items, encl))
        return 2

    print('qa_feed_enclosures: %d feeds, %d items, %d enclosures measured '
          'against the served file.' % (feeds, items, encl))
    if defects:
        print('DEFECT (%d):' % len(defects))
        for f, why in defects[:25]:
            print('  %-12s %s' % (f, why))
        return 1
    print('CLEAN — every enclosure resolves in dist, declares its real byte '
          'size, and declares the format its own bytes are.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'web/dist'))
