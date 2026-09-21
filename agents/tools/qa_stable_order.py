#!/usr/bin/env python3
"""
qa_stable_order.py — assert that every list Madar serves is in a DETERMINED
order: newest first, ties broken by slug ascending.

WHY (2026-09-20, ruling #58)
----------------------------
The 09-19 deploy went red on the `verify` job's feed-cache step. While
diagnosing it, this build was byte-compared against the live origin — the same
commit, 8208eb7, built twice on two runners — and **five sitemap pages and both
feeds differed**. Not in content: in ORDER. Same 38 pieces, same byte count,
same-day pieces in a different sequence.

Cause: eight of the nine sort sites in `web/src` compared dates and nothing
else --

    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf())

-- which returns 0 for two pieces published on the same day. `Array.prototype`
`.sort` is stable, so a 0 does not randomise the pair; it silently delegates the
decision to the order `getCollection()` happened to hand the entries over in,
which is filesystem enumeration order, which nobody chose and nothing asserted.
**24 of the 38 approved English pieces sit in a tie group** (16 share
2026-07-07 alone), so most of the corpus had no defined position.

The ninth site, `facetsFor` in taxonomy.ts, already broke its count ties on the
key (`b[1] - a[1] || a[0].localeCompare(a[0])`). The shape was known in this
codebase; it was simply never carried across.

WHAT THIS CHECKS, AND WHY NOT "BUILD IT TWICE"
-----------------------------------------------
The obvious instrument is to build twice and compare. It is the wrong one:
two builds on the SAME runner share a filesystem order, so the control passes
for a reason unrelated to the property. That is the 09-14 trap -- an experiment
whose negative result is indistinguishable from a healthy one.

So this asserts the stronger property, and from a single build: the served
order IS the canonical order. A partial comparator cannot satisfy that except
by luck, and luck is visible here because the expectation is derived from the
CONTENT COLLECTION (frontmatter date + slug, ruling #36) and never read back
off the page being judged (the 09-14 masking trap).

SCOPING -- WHY CONTAINERS AND NOT PAGES
----------------------------------------
The first draft compared each page's whole document-order link sequence. It
FALSE-FAILED on the real build, and the reason is worth keeping: the editions
page renders one block per edition, Edition 04's block ends with
`2026-07-07-us-naep-honesty-gap` and Edition 03's block begins with
`2026-07-07-chad-sudanese-refugee-schooling`. A tie run legitimately spans the
boundary, and across that boundary descending-by-slug is correct. Order is a
property of a LIST, not of a page.

So links are grouped by the smallest enclosing element that holds two or more
of them -- discovered by walking the element stack, never by a hard-coded class
name, so a new list surface is scoped automatically instead of being silently
skipped (the 08-17 orphan lesson: an exemption list is where defects hide).

Non-vacuity floors, per the 2026-08-16 silent-pass trap: zero pages found, zero
lists found, zero feeds found, or a corpus with no tie group at all -- each is
an error, not a pass. The last one matters most: this check is only meaningful
while same-day pieces exist, so it says out loud how many ties it actually
exercised.

Reads only `web/dist` plus the content collection. Gated from `postbuild` in
web/package.json, because this identity cannot write `.github/workflows/**`
(2026-09-14 rule, clause 4).
"""

import os
import re
import unicodedata
import sys
from html.parser import HTMLParser

ART = re.compile(r'^/madar/(?:(ar)/)?articles/([^/]+)/$')


def repo_root(dist):
    d = os.path.abspath(dist)
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, 'web', 'src', 'content')):
            return d
        d = os.path.dirname(d)
    return None


def collection_meta(root):
    """slug -> {date, related, approved, region, countries, themes}, per
    collection, read from frontmatter. Every expectation this check applies is
    derived from the source of truth and never read back off the artefact under
    audit (#36, and the 09-14 masking trap)."""
    out = {}
    for coll, key in (('articles', 'en'), ('articles-ar', 'ar')):
        d = os.path.join(root, 'web', 'src', 'content', coll)
        table = {}
        for name in os.listdir(d) if os.path.isdir(d) else []:
            if not name.endswith('.md'):
                continue
            head = open(os.path.join(d, name), encoding='utf-8').read(8000)
            m = re.search(r'^date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})', head, re.M)
            if not m:
                continue
            rel = []
            r = re.search(r'^related:\s*\n((?:\s*-\s*\S+\n)+)', head, re.M)
            if r:
                rel = re.findall(r'-\s*(\S+)', r.group(1))
            country = _scalar(head, 'country')
            table[name[:-3]] = {
                'date': m.group(1),
                'related': rel,
                # `approved: false` is the hold (#18). Absent means false, per
                # the schema default -- never assumed true.
                'approved': re.search(r'^approved:\s*true\s*$', head, re.M) is not None,
                'region': _scalar(head, 'region'),
                'countries': [c for c in [country] + _inline_list(head, 'countries')
                              if c] or [],
                'themes': _inline_list(head, 'themes'),
            }
        out[key] = table
    return out


def _scalar(head, field):
    m = re.search(r'^%s:\s*(.+?)\s*$' % field, head, re.M)
    if not m:
        return ''
    return m.group(1).strip().strip('"\'')


def _inline_list(head, field):
    """A YAML sequence in either spelling. Six of the 85 content files write
    `themes:` as an indented block rather than inline, and a parser that knew
    only the inline form under-counted three topics into silence -- caught by
    this check's own first run, which is the argument for deriving the
    expectation from the collection rather than from the page."""
    m = re.search(r'^%s:\s*\[(.*?)\]\s*$' % field, head, re.M | re.S)
    if m:
        return [v.strip().strip('"\'') for v in m.group(1).split(',') if v.strip()]
    m = re.search(r'^%s:\s*\n((?:[ \t]+-[ \t]*.+\n)+)' % field, head, re.M)
    if not m:
        return []
    return [v.strip().strip('"\'')
            for v in re.findall(r'^[ \t]+-[ \t]*(.+?)\s*$', m.group(1), re.M)]


def collation_key(value):
    """The comparison form of a display name -- NFD, combining marks dropped,
    lower-cased. The Python half of `collationKey` in web/src/lib/order.ts, and
    it must stay the same three operations: the build sorts facet rows with one
    and this check predicts them with the other (ruling #59)."""
    stripped = ''.join(c for c in unicodedata.normalize('NFD', value)
                       if unicodedata.category(c) != 'Mn')
    return stripped.lower()


def expected_facets(table):
    """The facet rows `facetsFor` derives from an approved collection, in the
    order it derives them: count descending, then the normalised key ascending,
    then the raw key. The keep rules are taxonomy.ts's own -- every region, a
    theme on at least two pieces and fewer than half, a country on at least
    two -- restated here rather than read off the page (#36)."""
    pieces = [v for v in table.values() if v['approved']]
    total = len(pieces)

    def tally(values_of):
        counts = {}
        for p in pieces:
            for v in set(values_of(p)):
                if v:
                    counts[v] = counts.get(v, 0) + 1
        return counts

    rows = []
    for kind, counts, keep in (
        ('region', tally(lambda p: [p['region']]), lambda n: n >= 1),
        ('topic', tally(lambda p: p['themes']), lambda n: 2 <= n < total / 2),
        ('country', tally(lambda p: p['countries']), lambda n: n >= 2),
    ):
        ordered = sorted(counts.items(),
                         key=lambda kv: (-kv[1], collation_key(kv[0]), kv[0]))
        rows.extend((kind, facet_slug(k), n) for k, n in ordered if keep(n))
    return rows


def facet_slug(value):
    """The Python half of `facetSlug`. Same normalisation as the sort key, so a
    row's position and its URL are derived from one function on both sides."""
    s = collation_key(value.strip())
    s = re.sub(r'[\u2019\']', '', s)
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')


class Lists(HTMLParser):
    """Collect article links with the identity of every ancestor element, so a
    link can be assigned to the smallest list that actually contains it."""

    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
            'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.n = 0
        self.links = []          # (ancestor_ids tuple, lang, slug)

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID:
            if tag == 'a':
                pass
            return
        self.n += 1
        self.stack.append((tag, self.n))
        if tag == 'a':
            href = dict(attrs).get('href') or ''
            m = ART.match(href)
            if m:
                self.links.append((tuple(i for _, i in self.stack[:-1]),
                                   m.group(1) or 'en', m.group(2)))

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return


def lists_on(html):
    """-> list of (ancestor_id, [(lang, slug), ...]) in document order.

    Each link is assigned to the SMALLEST enclosing element holding two or more
    distinct article links. Duplicate links to the same piece inside one list
    (a thumbnail and a title pointing at the same article) collapse to their
    first occurrence -- the question is the order of the pieces, not of the
    anchors."""
    p = Lists()
    p.feed(html)
    counts = {}
    for anc, lang, slug in p.links:
        for i in anc:
            counts.setdefault(i, set()).add((lang, slug))
    groups, order = {}, []
    for anc, lang, slug in p.links:
        home = None
        for i in reversed(anc):                     # innermost outward
            if len(counts.get(i, ())) >= 2:
                home = i
                break
        if home is None:
            continue                                # a lone link is trivially ordered
        if home not in groups:
            groups[home] = []
            order.append(home)
        if (lang, slug) not in groups[home]:
            groups[home].append((lang, slug))
    return [(i, groups[i]) for i in order]


def links_in_order(html):
    """Every article link on the page, document order, no grouping.

    Used for article pages, whose one list is defined by the SOURCE
    (`related:`) rather than by the markup — so the rail's contract does not
    depend on the container structure at all. An earlier draft grouped these
    too and would silently skip a rail of exactly one item, because a single
    link has no enclosing element holding two."""
    p = Lists()
    p.feed(html)
    return [(lang, slug) for _, lang, slug in p.links]


def feed_items(xml):
    out = []
    for link in re.findall(r'<link>([^<]+)</link>', xml):
        m = ART.match(link.replace('https://education3881.github.io/madar',
                                   '/madar'))
        if m:
            out.append((m.group(1) or 'en', m.group(2)))
    return out


def canonical(items, meta):
    """Newest first, ties broken by slug ascending -- the same total order
    web/src/lib/order.ts applies at build time."""
    return sorted(items, key=lambda p: (
        [-int(x) for x in meta[p[0]][p[1]]['date'].split('-')],
        p[1],
    ))


ARTICLE_PAGE = re.compile(r'^(?:(ar)/)?articles/([^/]+)/index\.html$')
BROWSE_HUB = re.compile(r'^(?:(ar)/)?browse/index\.html$')
BROWSE_FACET = re.compile(
    r'^(?:(ar)/)?browse/(region|topic|country)/([a-z0-9\-]+)/index\.html$')
FACET_UL = re.compile(r'<ul class="browse__facets"[^>]*>(.*?)</ul>', re.S)
FACET_LINK = re.compile(
    r'href="/madar/(?:ar/)?browse/(region|topic|country)/([a-z0-9\-]+)/"')


def facet_lists(html):
    """The facet rows a browse page serves, one list per `browse__facets` <ul>,
    in document order.

    Scoped to that element and not to the page: a facet page's <head> carries
    its own URL four times over (canonical, og:url, both hreflang alternates),
    and a sweep over the whole document reads those as rows. That is the 09-14
    masking trap from the other side -- a string found where it also
    legitimately appears."""
    return [FACET_LINK.findall(block) for block in FACET_UL.findall(html)]


def main(dist='web/dist'):
    root = repo_root(dist)
    if root is None:
        print('ERROR: could not locate web/src/content above %s' % dist)
        return 2
    meta = collection_meta(root)
    if not meta['en'] or not meta['ar']:
        print('ERROR: 0 content files read. An assertion that finds nothing '
              'to check has failed.')
        return 2

    defects, pages, lists_seen, rails, feeds, ties = [], 0, 0, 0, 0, 0
    browse_pages = 0
    facet_rows = {lang: expected_facets(meta[lang]) for lang in ('en', 'ar')}
    # A facet tie group is where the locale-dependent comparator of ruling #59
    # could show: two keys of the same kind on the same count. Counted out loud
    # for the same reason the date ties are (2026-08-16 silent-pass trap) --
    # with no tie anywhere, the row order is fixed by the counts alone and this
    # half of the check is green without having judged anything.
    facet_ties = 0
    for lang in ('en', 'ar'):
        groups = {}
        for kind, _slug, count in facet_rows[lang]:
            groups.setdefault((kind, count), 0)
            groups[(kind, count)] += 1
        facet_ties += sum(1 for n in groups.values() if n > 1)

    def known(label, items):
        unknown = [s for lang, s in items if s not in meta[lang]]
        if unknown:
            defects.append((label, 'links a slug absent from the content '
                                   'collection: %s' % unknown[:3]))
        return not unknown

    def judge_dated(label, items):
        """A date-ordered list: newest first, ties broken by slug."""
        nonlocal ties
        if not known(label, items):
            return
        want = canonical(items, meta)
        groups = {}
        for lang, s in items:
            groups.setdefault(meta[lang][s]['date'], set()).add(s)
        ties += sum(1 for v in groups.values() if len(v) > 1)
        if items != want:
            first = next(i for i in range(len(items)) if items[i] != want[i])
            defects.append((label, 'order diverges at position %d: serves %s, '
                                   'canonical is %s'
                            % (first + 1, items[first][1], want[first][1])))

    def judge_rail(label, lang, slug, items, served):
        """An article page's `related:` rail. Its order is EDITORIAL -- the
        sequence declared in frontmatter -- not a date order. Judging it
        against the date order is the 09-14 scoping trap: the right check
        applied to the wrong list. RelatedReading drops slugs it cannot
        resolve, so the promise is the declared sequence filtered to what the
        build actually serves."""
        want = [s for s in meta[lang][slug]['related'] if (lang, s) in served]
        got = [s for _, s in items]
        if got != want:
            n = min(len(got), len(want))
            at = next((i for i in range(n) if got[i] != want[i]), n)
            defects.append((label, 'related rail diverges at position %d '
                                   '(serves %d, declares %d): serves %s, '
                                   'frontmatter declares %s'
                            % (at + 1, len(got), len(want),
                               got[at] if at < len(got) else '<nothing>',
                               want[at] if at < len(want) else '<nothing>')))

    served = set()
    html_pages = []
    for base, _, names in os.walk(dist):
        for name in sorted(names):
            path = os.path.join(base, name)
            rel = os.path.relpath(path, dist).replace(os.sep, '/')
            if name.endswith('.html'):
                html_pages.append((rel, path))
                m = ARTICLE_PAGE.match(rel)
                if m:
                    served.add((m.group(1) or 'en', m.group(2)))
            elif name == 'rss.xml':
                feeds += 1
                judge_dated(rel, feed_items(open(path, encoding='utf-8').read()))

    for rel, path in html_pages:
        pages += 1
        html = open(path, encoding='utf-8', errors='replace').read()
        m = ARTICLE_PAGE.match(rel)
        if m:
            # An article page carries exactly one list: its related rail. Every
            # article link on it that is not the page's own self-link belongs
            # to that rail -- asserted, not assumed, so a second list appearing
            # here fails loudly instead of being silently skipped.
            #
            # "Self-link" is matched on the SLUG and not on (lang, slug): the
            # language switch in the chrome points at the same piece in the
            # other edition, and it is the page itself, not an item in its rail.
            lang, slug = m.group(1) or 'en', m.group(2)
            items, seen = [], set()
            for it in links_in_order(html):
                if it[1] == slug or it in seen:
                    continue
                seen.add(it)
                items.append(it)
            rails += 1
            if known(rel, items):
                judge_rail(rel, lang, slug, items, served)
        else:
            hub, fac = BROWSE_HUB.match(rel), BROWSE_FACET.match(rel)
            if hub or fac:
                browse_pages += 1
                lang = (hub or fac).group(1) or 'en'
                canon = [(k, s) for k, s, _ in facet_rows[lang]]
                if hub:
                    # The hub renders one <ul> per kind; concatenated they are
                    # the canonical order entire.
                    want = canon
                else:
                    # A facet page renders one <ul>: "Elsewhere in the archive",
                    # which is the canonical order minus this page's own row,
                    # truncated to nine. WHICH nine is a function of the order,
                    # so this surface fails on a permutation the hub could
                    # survive by rendering the same rows in a different place.
                    self_row = (fac.group(2), fac.group(3))
                    want = [r for r in canon if r != self_row][:9]
                got = [r for block in facet_lists(html) for r in block]
                if got != want:
                    n = min(len(got), len(want))
                    at = next((i for i in range(n) if got[i] != want[i]), n)
                    defects.append((rel, 'facet rows diverge at position %d '
                                         '(serves %d, corpus implies %d): '
                                         'serves %s, corpus implies %s'
                                    % (at + 1, len(got), len(want),
                                       '/'.join(got[at]) if at < len(got) else '<nothing>',
                                       '/'.join(want[at]) if at < len(want) else '<nothing>')))
            for i, items in lists_on(html):
                lists_seen += 1
                judge_dated('%s [list %d]' % (rel, i), items)

    if pages == 0 or lists_seen == 0 or feeds == 0 or rails == 0 or browse_pages == 0:
        print('ERROR: %d pages, %d dated lists, %d rails, %d feeds, %d browse '
              'pages. An assertion that finds nothing to check has failed.'
              % (pages, lists_seen, rails, feeds, browse_pages))
        return 2
    if facet_ties == 0:
        print('ERROR: not one facet kind holds two keys on the same count. The '
              'row order is then fixed by the counts alone and the tie-break '
              'this half exists to judge was never consulted.')
        return 2
    if ties == 0:
        print('ERROR: not one dated list contains two pieces sharing a date. '
              'This check can only bite on a tie; with no tie anywhere it is '
              'green and worthless (2026-08-16 silent-pass trap).')
        return 2

    print('qa_stable_order: %d pages, %d dated lists, %d feeds, %d related '
          'rails, %d browse pages; %d date tie groups and %d facet tie groups '
          'actually exercised.'
          % (pages, lists_seen, feeds, rails, browse_pages, ties, facet_ties))
    if defects:
        print('DEFECT (%d):' % len(defects))
        for lab, why in defects[:25]:
            print('  %-52s %s' % (lab, why))
        return 1
    print('CLEAN — every dated list is newest-first with ties broken by slug, every '
          'related rail is in its declared order, and every browse page serves the '
          'facet rows the corpus implies; no list depends on filesystem enumeration '
          'order or on the build machine\'s locale.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'web/dist'))
