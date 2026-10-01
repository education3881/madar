#!/usr/bin/env python3
"""
qa_pair_frontmatter.py — standing assertion #28: a bilingual pair's two files
agree about everything that is a property of the PIECE rather than of a
language, and they point at each other.

WHY (2026-10-01)
----------------
The forward question written into the 2026-09-30 QA log, tested here before
anything new was added:

    Which claims in `sources[]` are machine-checkable against the document
    itself, rather than against the URL's status code?

The question was asked because `sources[]` is the only prose in this
publication that no instrument reads. The body has the numeral multiset, the
eight trace axes, the four non-numeric rows and `qa_packet_figures` downstream
of it. An annotation has `qa_sources_alive`, which checks third-party
reachability, and nothing else.

**The answer turned out to be a different answer from the one the question
expected, and the useful half of it is this: the cheapest machine-checkable
claim about a document is the one the operation makes TWICE.** A pair's two
annotations describe the same register in two languages. Its URL, its
publication date, its byte count and its serving state are properties of the
document, not of the language the annotation is written in — so the pair is its
own control, offline, with no fetch and no third-party host in the loop.

**What was measured and rejected, recorded here because a negative result that
is not written down gets re-attempted:** a numeral multiset over each shared
annotation, which is the body-level discipline applied one level out. Measured
across the whole corpus — 338 shared annotations in 44 pairs — it disagreed on
**117**, and essentially none of the 117 was a defect. Three structural causes,
all of them deliberate house conventions:

  * **Quote-plus-gloss doubling (#72).** An Arabic annotation carries the
    register's own English sentence AND an Arabic gloss of it, so every figure
    inside a quotation appears twice on the AR side and once on the EN side.
  * **Numeral-word rendering.** EN `876,000` against AR `876 ألف`; EN `20,000`
    against AR `20 ألف`. Same figure, different token count.
  * **ISO against prose dates.** EN `2026-05-22` tokenises to three numbers;
    the AR annotation writes the same date in Arabic month names and tokenises
    to one, or to none.

A check with a 35% false-positive rate on a clean corpus is not a check; it is
a thing somebody turns off in a week (the 2026-09-13 hand-run rule, arrived at
from the other side). The normaliser that would fix it — numeral words in two
languages, decimal and thousands separators, quotation spans — is a larger
instrument than the question implies, and it is named in the QA log as work,
not smuggled in here half-built.

**So this assertion checks the part that is genuinely language-independent**:
the URL set, and every frontmatter field that is a fact about the piece.

WHAT IT FOUND ON ITS FIRST RUN, before it was wired
---------------------------------------------------
`2026-09-19-egypt-baccalaureate-published-first` — row 5 of the Edition 05
wave, banked 09-22, verified 09-23, held — carried **no `arabicVersion:`
field**, alone among 44 English articles. Its Arabic twin pointed at it; it
pointed at nothing. `arabicVersion` is optional in the schema and
`web/src/pages/articles/[...slug].astro` derives three things from it: the
`<link rel="alternate" hreflang>` pair, the `translationPath` the chrome uses
for its *read in Arabic* link, and the reciprocal href in the article footer.
Absent, the English page of that pair would have shipped with **no Arabic
alternate, no link to its twin, and no hreflang cluster** — while the Arabic
page linked back to it.

**The reason no existing assertion could see it is the whole point of this
one.** `qa_hreflang_clusters` enumerates built pages and is green; it is green
because a held piece is not built, and a held piece is exactly what this wave
is. That is the 2026-08-09 flag-sweep inversion read backwards: that rule says
an assertion scoped to a corpus state passes vacuously once the state changes.
This is its mirror — **an assertion scoped to the SERVED corpus is blind to the
corpus that is about to be served**, and a wave that flips as one commit
changes the served corpus by six pairs in one step, with no gate upstream of
it. Twenty-four assertions gate this deploy and twenty-three of them read
`dist`. Every one of them will meet the Egypt pair for the first time on flip
day.

So this check reads `web/src/content/**` — the source files, held pieces
included — and it is the second assertion to do so (`qa_geo_fields` is the
first, 88 pieces against 76 built pages, for the same reason).

WHAT IT ENUMERATES
------------------
For every slug present in both `articles/` and `articles-ar/`:

 1. **Reciprocity.** `arabicVersion` on the EN file names the AR slug and
    `englishVersion` on the AR file names the EN slug. Both directions, because
    the Egypt defect was present in exactly one of them.
 2. **Piece-identity fields byte-identical across the pair**: `date`,
    `edition`, `country`, `countries`, `region`, `level`, `type`,
    `contains_composites`, `approved`, `themes`. These are facts about the
    piece. `title`, `dek` and `hero.alt`/`hero.caption` are deliberately NOT
    compared — those are composed, not translated, and a pair whose deks match
    token for token would be the defect.
 3. **The `related:` rail, as a sequence** — same entries, same order (#42,
    and the source-side companion to assertion 20, which asserts the rendered
    rail against this same frontmatter and therefore cannot see the two
    languages disagreeing with each other).
 4. **`hero.src`** — one still serves both languages.
 5. **The `sources[]` URL multiset.** A register either is or is not in the
    record for a piece, and that is not a language question.

DECLARED ASYMMETRIES
--------------------
Three pairs legitimately cite different URLs, and each is an editorial decision
with a reason, so each is declared below by slug WITH ITS EXACT URL SETS. A
declaration is not a blanket exemption: if a declared pair's asymmetry changes
shape, the check fails and the declaration has to be re-earned. Same discipline
as an assertion kept out of CI carrying its reason at the point where the
others are listed (2026-09-13).

THE RECOGNISER IS PROVED BEFORE THE TREE IS JUDGED (ruling #79)
---------------------------------------------------------------
Eleven fixtures run on every invocation, each one a reading this check has
really made or a defect it exists to catch, and each pinning **the population
examined** as well as the verdict reached — because two of yesterday's
`qa_a11y_lang` fixtures were silent in both the correct and the broken code and
differed only in `checked`. A fixture you cannot make fail is not a fixture.

USAGE
-----
    python3 agents/tools/qa_pair_frontmatter.py [repo-root]

Exit 0 clean, 1 on any defect. No network, no `dist`, no third-party host:
this one is honest to run before the build as well as after it.
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- frontmatter

SCALAR = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$')
INLINE_LIST = re.compile(r'^\[(.*)\]$')


def parse_frontmatter(text):
    """Minimal reader for the shape this repository actually writes.

    Deliberately not a YAML parser. A general parser would accept shapes the
    content files never use and would quietly succeed on a file whose real
    structure had drifted; this one knows the four shapes in use and raises on
    anything else, which is the behaviour an assertion wants.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        raise ValueError("no opening frontmatter fence")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("no closing frontmatter fence")

    data = {}
    key = None
    for raw in lines[1:end]:
        if not raw.strip():
            continue
        m = SCALAR.match(raw)
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            inline = INLINE_LIST.match(val)
            if inline:
                data[key] = [p.strip() for p in inline.group(1).split(",") if p.strip()]
            elif val == "":
                data[key] = []          # a block list or a nested map follows
            else:
                data[key] = _unquote(val)
            continue
        if key == "sources":
            if raw.startswith("  - title:"):
                data.setdefault("sources", [])
                data["sources"].append({"title": _unquote(raw[len("  - title:"):].strip()),
                                        "url": None})
            elif raw.startswith("    url:") and data.get("sources"):
                data["sources"][-1]["url"] = _unquote(raw[len("    url:"):].strip())
            continue
        if raw.startswith("  - "):
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(_unquote(raw[4:].strip()))
            continue
        m2 = re.match(r'^  ([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$', raw)
        if m2 and key:
            data["%s.%s" % (key, m2.group(1))] = _unquote(m2.group(2).strip())
            continue
    return data


def _unquote(v):
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        return v[1:-1]
    return v


# ------------------------------------------------------- declared asymmetries
#
# slug -> (en_only_urls, ar_only_urls, reason)
#
# Each set is exact. A pair that gains or loses an asymmetric URL fails, even
# though it is already declared here.

DECLARED = {
    "2026-05-31-indonesia-permen-13-coding-ai": (
        {"https://kemendikdasmen.go.id/siaran-pers/13420-permendikdasmen-112025-dan-132025-"
         "dasar-sinkronisasi-kurikulum-dan-beban-kerja-guru"},
        set(),
        "one EN-only ministry press release on the regulatory architecture around "
        "Permen 13/2025; the Arabic composition carries the regulation itself and "
        "not the architecture note, which it does not lean on",
    ),
    "2026-07-06-morocco-ecoles-pionnieres": (
        {"https://www.men.gov.ma/fr/%C3%A9tablissements-pionniers"},
        {"https://www.men.gov.ma/%D9%85%D8%A4%D8%B3%D8%B3%D8%A7%D8%AA-"
         "%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%AF%D8%A9"},
        "the SAME ministry programme page, cited in each edition's own official "
        "language — French on the EN side, Arabic on the AR side. The cleanest "
        "shape an asymmetry can have: one document, two first-party editions",
    ),
    "2026-09-01-sudan-cant-wait-to-learn": (
        {"https://www.unicef.org/sudan/stories/golden-opportunity-learn",
         "https://www.unicef.org/sudan/stories/new-horizons-education-sudan"},
        {"https://www.unicef.org/sudan/ar/%D8%A2%D9%81%D8%A7%D9%82-%D8%AC%D8%AF%D9%8A%D8%AF"
         "%D8%A9-%D9%84%D9%84%D8%AA%D8%B9%D9%84%D9%8A%D9%85-%D9%81%D9%8A-%D8%A7%D9%84%D8%B3"
         "%D9%88%D8%AF%D8%A7%D9%86/%D9%82%D8%B5%D8%B5",
         "https://www.unicef.org/sudan/ar/%D9%81%D8%B1%D8%B5%D8%A9-%D8%B0%D9%87%D8%A8%D9%8A"
         "%D8%A9-%D9%84%D9%84%D8%AA%D8%B9%D9%84%D9%85/%D9%82%D8%B5%D8%B5",
         "https://news.un.org/ar/interview/2024/01/1127972"},
        "two UNICEF stories cited in their official ARABIC editions on the AR side "
        "and their English editions on the EN side — and the Arabic editions carry "
        "their own, different publication dates (31 Aug 2020 against 27 Aug; 2 Nov "
        "2022 against 1 Nov), so they are different documents and not the same URL "
        "localised. Plus one AR-only UN News Arabic interview, cited solely as the "
        "spelling register for a named human",
    ),
}

# Fields that are facts about the piece, not about the language it is in.
IDENTITY_FIELDS = ["date", "edition", "country", "countries", "region", "level",
                   "type", "contains_composites", "approved", "themes"]


# --------------------------------------------------------------- the audit

def audit(pairs, declared):
    """Pure function. pairs: [(slug, en_fm, ar_fm)]. Returns (defects, checked).

    `checked` is part of the verdict, not decoration: a recogniser whose scope
    silently empties reads green on findings alone (qa_a11y_lang, 2026-09-30).
    """
    defects = []
    checked = {"pairs": 0, "fields": 0, "rails": 0, "urls": 0,
               "declarations_used": 0, "annotations_shared": 0}
    notes = []

    for slug, en, ar in pairs:
        checked["pairs"] += 1

        if en.get("arabicVersion") != slug:
            defects.append(
                "%s — the EN file's arabicVersion is %r, not the slug. The English "
                "page would serve no hreflang alternate, no translationPath and no "
                "link to its Arabic twin"
                % (slug, en.get("arabicVersion")))
        if ar.get("englishVersion") != slug:
            defects.append(
                "%s — the AR file's englishVersion is %r, not the slug. The Arabic "
                "page would serve no hreflang alternate and no link back"
                % (slug, ar.get("englishVersion")))

        for f in IDENTITY_FIELDS:
            if f not in en and f not in ar:
                continue
            checked["fields"] += 1
            if en.get(f) != ar.get(f):
                defects.append(
                    "%s — %s is a fact about the piece and the pair disagrees: "
                    "EN %r, AR %r" % (slug, f, en.get(f), ar.get(f)))

        checked["rails"] += 1
        if list(en.get("related") or []) != list(ar.get("related") or []):
            defects.append(
                "%s — the related rail differs across the pair (sequence compared, "
                "not set): EN %r, AR %r"
                % (slug, en.get("related"), ar.get("related")))

        checked["fields"] += 1
        if en.get("hero.src") != ar.get("hero.src"):
            defects.append("%s — hero.src differs across the pair: EN %r, AR %r"
                           % (slug, en.get("hero.src"), ar.get("hero.src")))

        en_urls = [s["url"] for s in en.get("sources") or [] if s.get("url")]
        ar_urls = [s["url"] for s in ar.get("sources") or [] if s.get("url")]
        checked["urls"] += len(en_urls) + len(ar_urls)
        checked["annotations_shared"] += len(set(en_urls) & set(ar_urls))
        en_only = set(en_urls) - set(ar_urls)
        ar_only = set(ar_urls) - set(en_urls)

        if en_only or ar_only:
            if slug in declared:
                d_en, d_ar, reason = declared[slug]
                checked["declarations_used"] += 1
                if en_only == d_en and ar_only == d_ar:
                    notes.append("%s — declared asymmetry, unchanged (%d EN-only, "
                                 "%d AR-only): %s"
                                 % (slug, len(en_only), len(ar_only), reason))
                else:
                    defects.append(
                        "%s — this pair has a DECLARED asymmetry and its shape has "
                        "changed, so the declaration no longer describes it. "
                        "Declared EN-only %d / AR-only %d; found EN-only %d / "
                        "AR-only %d. Re-earn the declaration or fix the pair"
                        % (slug, len(d_en), len(d_ar), len(en_only), len(ar_only)))
            else:
                defects.append(
                    "%s — the pair's sources cite different registers and nothing "
                    "declares why: %d EN-only, %d AR-only. A register either is or "
                    "is not in the record for a piece, and that is not a language "
                    "question (#42)" % (slug, len(en_only), len(ar_only)))

    for slug in declared:
        if not any(s == slug for s, _e, _a in pairs):
            defects.append(
                "%s — declared as an asymmetric pair and there is no such pair. A "
                "stale exemption is an exemption nobody can fail" % slug)

    return defects, checked, notes


# ----------------------------------------------------------------- fixtures
#
# Each fixture is a reading this check has really made, or a defect it exists
# to catch. `want_defects` is the count; `want_checked` pins the population.

def _pair(**kw):
    """A minimal well-formed pair, overridable field by field."""
    slug = kw.pop("slug", "2026-01-01-fixture")
    en = {"date": "2026-01-01", "edition": "5", "country": "Rwanda",
          "region": "Africa", "level": "Both", "type": "curated",
          "contains_composites": "false", "approved": "false",
          "themes": ["access"], "related": ["a", "b"],
          "arabicVersion": slug, "hero.src": "/stills/%s.svg" % slug,
          "sources": [{"title": "x", "url": "https://one.example/"},
                      {"title": "y", "url": "https://two.example/"}]}
    ar = dict(en)
    ar.pop("arabicVersion")
    ar["englishVersion"] = slug
    ar["sources"] = [dict(s) for s in en["sources"]]
    ar["related"] = list(en["related"])
    ar["themes"] = list(en["themes"])
    for k, v in kw.items():
        side, _, field = k.partition("__")
        (en if side == "en" else ar)[field] = v
    return (slug, en, ar)


FIXTURES = [
    ("control — a well-formed pair is silent",
     [_pair()], {}, 0,
     {"pairs": 1, "fields": 10, "rails": 1, "urls": 4,
      "declarations_used": 0, "annotations_shared": 2}),

    ("the Egypt reading of 2026-10-01: EN carries no arabicVersion",
     [_pair(en__arabicVersion=None)], {}, 1, None),

    ("the mirror of it: AR carries no englishVersion",
     [_pair(ar__englishVersion=None)], {}, 1, None),

    ("approved disagrees — half a pair live is the worst defect this can hold",
     [_pair(ar__approved="true")], {}, 1, None),

    ("date disagrees — one dateline per piece, not one per language",
     [_pair(ar__date="2026-01-02")], {}, 1, None),

    ("the rail lost an entry on one side",
     [_pair(ar__related=["a"])], {}, 1, None),

    ("the rail is REORDERED, not changed — set equality would read this green",
     [_pair(ar__related=["b", "a"])], {}, 1, None),

    ("hero.src differs — one still serves both languages",
     [_pair(ar__hero_src="/stills/other.svg")], {}, 1, None),

    ("an UNDECLARED source asymmetry",
     [_pair(ar__sources=[{"title": "x", "url": "https://one.example/"},
                         {"title": "z", "url": "https://three.example/"}])], {}, 1, None),

    ("a DECLARED asymmetry is silent, and the declaration is consumed",
     [_pair(ar__sources=[{"title": "x", "url": "https://one.example/"},
                         {"title": "z", "url": "https://three.example/"}])],
     {"2026-01-01-fixture": ({"https://two.example/"}, {"https://three.example/"},
                             "fixture reason")},
     0, {"pairs": 1, "fields": 10, "rails": 1, "urls": 4,
         "declarations_used": 1, "annotations_shared": 1}),

    ("a declared asymmetry whose SHAPE changed is not exempt",
     [_pair(ar__sources=[{"title": "x", "url": "https://one.example/"},
                         {"title": "z", "url": "https://four.example/"}])],
     {"2026-01-01-fixture": ({"https://two.example/"}, {"https://three.example/"},
                             "fixture reason")},
     1, None),
]


def _fix_hero(p):
    """_pair() takes hero_src as a kwarg because '.' is not a Python name."""
    slug, en, ar = p
    for side in (en, ar):
        if "hero_src" in side:
            side["hero.src"] = side.pop("hero_src")
    return (slug, en, ar)


def run_fixtures():
    failures = []
    for name, pairs, declared, want_n, want_checked in FIXTURES:
        pairs = [_fix_hero(p) for p in pairs]
        defects, checked, _notes = audit(pairs, declared)
        if len(defects) != want_n:
            failures.append("%s — expected %d defect(s), got %d: %s"
                            % (name, want_n, len(defects), defects))
        if want_checked is not None and checked != want_checked:
            failures.append("%s — population examined changed: expected %r, got %r"
                            % (name, want_checked, checked))
    return failures


# --------------------------------------------------------------------- main

def collect(root):
    en_dir = root / "web/src/content/articles"
    ar_dir = root / "web/src/content/articles-ar"
    pairs, lonely = [], []
    for p in sorted(en_dir.glob("*.md")):
        slug = p.stem
        a = ar_dir / p.name
        if not a.exists():
            lonely.append("EN %s has no Arabic twin" % slug)
            continue
        pairs.append((slug, parse_frontmatter(p.read_text(encoding="utf-8")),
                      parse_frontmatter(a.read_text(encoding="utf-8"))))
    for p in sorted(ar_dir.glob("*.md")):
        if not (en_dir / p.name).exists():
            lonely.append("AR %s has no English twin" % p.stem)
    return pairs, lonely


def main(argv):
    root = Path(argv[1] if len(argv) > 1 else ".").resolve()

    failures = run_fixtures()
    if failures:
        print("qa_pair_frontmatter: FAIL — the recogniser is broken, so its "
              "verdict on the tree means nothing. %d fixture(s) failed:"
              % len(failures))
        for f in failures:
            print("  - %s" % f)
        return 1
    print("qa_pair_frontmatter — recogniser proved on %d fixture(s)" % len(FIXTURES))

    pairs, lonely = collect(root)
    if not pairs:
        print("qa_pair_frontmatter: FAIL — 0 pairs found under "
              "web/src/content/. An assertion with nothing to check has "
              "failed, not passed.")
        return 1

    defects, checked, notes = audit(pairs, DECLARED)
    defects = [d for d in defects] + lonely

    held = sum(1 for _s, e, _a in pairs if e.get("approved") != "true")
    print("qa_pair_frontmatter: %d pair(s) — %d approved, %d held — %d identity "
          "fields, %d rails, %d source URLs, %d shared annotations, %d/%d "
          "declarations used"
          % (checked["pairs"], checked["pairs"] - held, held, checked["fields"],
             checked["rails"], checked["urls"], checked["annotations_shared"],
             checked["declarations_used"], len(DECLARED)))
    for n in notes:
        print("  note: %s" % n)

    if defects:
        print("FAIL qa_pair_frontmatter — %d defect(s):" % len(defects))
        for d in defects:
            print("  - %s" % d)
        return 1

    print("CLEAN qa_pair_frontmatter — every pair points at itself from both "
          "sides and agrees with itself about every fact that belongs to the "
          "piece rather than to a language. Held pieces included, which is the "
          "whole reason this one reads source files and not dist.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
