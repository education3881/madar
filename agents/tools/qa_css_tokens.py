#!/usr/bin/env python3
"""
qa_css_tokens.py — assert that every CSS custom property the built site READS
is one the built site DEFINES.

WHY (2026-09-14, second run of the day)
---------------------------------------
The 2026-09-09 QA log ended with a named forward question and nobody tested it
for three runs:

    "Today's 404 work turned up two CSS custom properties that did not exist,
     in a file that built cleanly, passed every one of the twelve standing
     assertions, and would have shipped with its Arabic set in the browser's
     default face. An undefined var() does not error; it evaporates.
     Named surface for 09-10: the design tokens are a contract nothing checks."

Asked today, it bit on first contact — on code six hours old. The browse
surface shipped in 51282db (2026-09-14) styles three things with
`var(--color-accent)`:

    .facet:hover            border-color + color
    .piece__country         color
    .piece__link:hover      .piece__title color

This design system has no `--color-accent`. Its accent is `--color-orange`
(#D94F2A). So on all 76 browse pages, in both languages, the country label on
every listed piece rendered in inherited ink and both hover affordances did
nothing — the declaration does not error, it evaporates. The build was clean,
all twelve assertions were green, and the page looked like a page.

WHAT THIS CHECK ENUMERATES, AND WHAT IT DELIBERATELY DOES NOT
-------------------------------------------------------------
It reads `dist` only, because CSS is built for every piece whether or not the
piece is approved — there is no held-file blind spot here of the kind that
made `qa_geo_fields` read source as well.

Three ways a `var(--x)` is legitimately satisfied, and all three are honoured:

  1. a definition somewhere in the built output (`--x: …` in a CSS context);
  2. an in-place fallback (`var(--x, #D94F2A)`) — the declaration cannot
     evaporate, so it is not this check's business;
  3. a RUNTIME setter — VALENCE sets `--c` with `element.style.setProperty`,
     which is correct code that a naive static sweep cries wolf on, and a
     check that cries wolf is a check that gets ignored (#35). The setters are
     DERIVED from the built output rather than kept in a hand-written
     allowlist, so a new runtime token needs no edit here and a REMOVED setter
     stops satisfying its token the moment it goes.

Scope discipline (2026-09-14 ruling, trap 2 — an assertion must not be able to
read its answer off a wider field than the one it checks): uses and definitions
are both read from CSS CONTEXTS ONLY — whole `.css` files, `<style>` blocks,
and `style="…"` attributes — never from prose. A `--word:` in an article body
is text, not a token, and must not be allowed to satisfy anything.

Usage:  python3 agents/tools/qa_css_tokens.py [<dist-dir>]
Exit 0 = clean. Exit 1 = defect. Exit 2 = the check could not check.
"""
import sys, os, re

USE = re.compile(r'var\(\s*(--[A-Za-z0-9_-]+)\s*(,?)')
DEFN = re.compile(r'(--[A-Za-z0-9_-]+)\s*:')
STYLE_BLOCK = re.compile(r'<style[^>]*>(.*?)</style>', re.S | re.I)
STYLE_ATTR = re.compile(r'\sstyle\s*=\s*"([^"]*)"', re.I)
SETTER = re.compile(r"""setProperty\(\s*['"](--[A-Za-z0-9_-]+)['"]""")

CSS_EXT = ('.css',)
MARKUP_EXT = ('.html', '.htm', '.svg', '.xml')
SCRIPT_EXT = ('.js', '.mjs')


def css_regions(path, text):
    """The CSS a browser will actually parse in this file — nothing wider."""
    if path.endswith(CSS_EXT):
        return [text]
    if path.endswith(MARKUP_EXT):
        return STYLE_BLOCK.findall(text) + STYLE_ATTR.findall(text)
    return []


def main(dist='web/dist'):
    if not os.path.isdir(dist):
        print('ERROR: %s does not exist. Build first.' % dist)
        return 2

    used = {}      # token -> {file: count}  (uses with NO fallback)
    fallback = {}  # token -> count          (uses WITH a fallback)
    defined = {}   # token -> first file that defines it
    runtime = {}   # token -> first file whose script sets it
    scanned = 0

    for root, _dirs, names in os.walk(dist):
        for name in sorted(names):
            path = os.path.join(root, name)
            rel = os.path.relpath(path, dist)
            if not (path.endswith(CSS_EXT) or path.endswith(MARKUP_EXT)
                    or path.endswith(SCRIPT_EXT)):
                continue
            try:
                text = open(path, encoding='utf-8', errors='ignore').read()
            except OSError:
                continue
            scanned += 1

            # Runtime setters are read from the WHOLE file: a setter lives in
            # JavaScript, which is never a CSS region.
            for m in SETTER.finditer(text):
                runtime.setdefault(m.group(1), rel)

            for region in css_regions(path, text):
                for m in USE.finditer(region):
                    token, comma = m.group(1), m.group(2)
                    if comma:
                        fallback[token] = fallback.get(token, 0) + 1
                    else:
                        used.setdefault(token, {})
                        used[token][rel] = used[token].get(rel, 0) + 1
                for m in DEFN.finditer(region):
                    defined.setdefault(m.group(1), rel)

    # The 2026-08-16 silent-pass trap: an assertion that finds nothing to check
    # has failed, not passed.
    if scanned == 0:
        print('ERROR: 0 files scanned under %s.' % dist)
        return 2
    if not used and not fallback:
        print('ERROR: 0 var() uses found in %d files. This site is built from '
              'custom properties; finding none means the sweep is looking in '
              'the wrong place.' % scanned)
        return 2
    if not defined:
        print('ERROR: 0 custom-property definitions found in %d files.' % scanned)
        return 2

    defects = []
    by_runtime = []
    for token in sorted(used):
        if token in defined:
            continue
        if token in runtime:
            by_runtime.append((token, runtime[token]))
            continue
        files = used[token]
        defects.append((token, sum(files.values()), len(files), sorted(files)[0]))

    print('qa_css_tokens: %d files scanned; %d distinct properties read without a '
          'fallback, %d defined, %d satisfied by a runtime setter, %d read with a '
          'fallback.' % (scanned, len(used), len(defined), len(by_runtime), len(fallback)))
    for token, where in by_runtime:
        print('  runtime: %s set by setProperty in %s — correct, not a defect.'
              % (token, where))

    if defects:
        print('DEFECT (%d unresolved custom propert%s) — these declarations '
              'evaporate in the browser:' % (len(defects), 'y' if len(defects) == 1 else 'ies'))
        for token, uses, nfiles, example in defects:
            print('  %-28s %4d use(s) across %3d file(s), e.g. %s'
                  % (token, uses, nfiles, example))
        return 1

    print('CLEAN — every custom property the built CSS reads is defined in the '
          'built output, carries its own fallback, or is set at runtime.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'web/dist'))
