#!/usr/bin/env python3
"""
qa_census.py — standing assertion #19: the instruments agree about what they
counted, and they agree by NAME and not by arithmetic.

WHY (2026-09-19)
----------------
The forward question carried unanswered from 2026-09-16, 09-17 and 09-18, and
owed for three runs:

    Nothing compares the assertions' counts to one another. Pages built ·
    sitemap <loc> · reachability · jsonld · a11y · hreflang — numbers already
    emitted by eight instruments, that must agree within known offsets and have
    never been read together.

Asked deliberately today, it failed on first contact, and the failure is not
the one the question anticipated. The arithmetic is fine. What is wrong is
underneath it: **three different instruments print the number 120, and they are
counting three different sets of 120 pages.**

    qa_lastmod           120   the sitemap's URL set          = served - {404}
    qa_jsonld            120   dist/**/index.html             = served - {404}
    qa_consumer_surface  120   every *.html except VALENCE    = served - {valence}

Each exclusion is deliberate, stated in its own file, and correct. Nothing here
is a defect in any of the three. The defect is that **the QA log has been
printing them in one grid, on one line, as though they were one number** — and
a reader of that grid (including the next run, including the weekly review)
cannot tell that the middle column and the right-hand column disagree about
which pages exist. Two sets of the same size look identical from a cardinality.

That is the 2026-08-17 orphan lesson arriving from the other side. There, a
difference of exactly one (82 pages against 81 sitemap URLs) went unnoticed
because nothing compared the counts. Here the counts compare perfectly and the
sets do not. **Equal cardinalities are not an agreement; they are the absence of
one particular disagreement.** A page could be dropped from the sitemap and a
different page added to it on the same day and every number above would be
unchanged.

WHAT THIS CHECK ENUMERATES
--------------------------
1. **The populations, derived independently.** The census computes its own
   page sets from `dist` — served HTML, the sitemap's `<loc>` set, the Arabic
   side, the English side, the article pages — and from the content collection
   the piece counts (approved, held). It never takes a number from another
   tool in order to check that tool.

2. **The set relations, asserted BY NAME.** `served - sitemap` must equal the
   declared not-routed set, element for element, and every declared member must
   actually exist; `sitemap - served` must be empty. A difference is NAMED, or
   it is a defect — never absorbed into an offset.

3. **Each instrument's printed number against its own declared population.**
   Every row below states, in a set expression, which population that tool
   means, and why it differs from `served` if it does. The census runs the
   tool, reads the number off its STDOUT, and compares.

   It reads stdout on purpose. The number a tool *prints* is the artefact a
   human, a QA log and the next run actually consume; a tool that computes
   correctly and prints a mislabelled number is a real defect class, and only a
   reader of the printed line catches it. (Found on the first run: qa_dist_input
   printed "120 built page(s)" for a dist containing 121 built pages, because it
   enumerated `index.html` and the branded 404 is not one. Corrected in the same
   commit as this file.)

4. **Non-vacuity.** If fewer than `MIN_ROWS` numbers could be extracted, the
   census FAILS. A census that cannot find the numbers it exists to compare has
   failed, not passed — the 2026-08-16 silent-pass trap, which this file is
   especially exposed to because it reads text it does not own.

WHAT IT DELIBERATELY DOES NOT DO
--------------------------------
It does not check whether any instrument is *right about its own subject*. That
is each instrument's job and each one proves it separately. The census checks
one thing only: that the populations they report are the populations they mean,
and that those populations stand in the stated relations to one another.

It does not cover the two ELEMENT censuses (qa_arabic_shaping's Arabic-bearing
elements, qa_arabic_joining's measured runs). Their population is elements, not
pages, they both need a headless browser, and running Chrome twice more in
`postbuild` to compare two numbers is a poor trade. The disagreement named
between them on 09-18 — assertion 17 counting non-rendered `<title>` and JSON-LD
`<script>` elements among its 326 — was closed today at the source, by fixing
17's selection, not by measuring it here.

It re-runs the instruments rather than reading a cached log. That costs a few
seconds and is the point: a census of yesterday's numbers is a census of
yesterday's site.

PROVED BOTH WAYS per ruling #35, and per the 2026-09-14 rule that the bite is
proved as carefully as the control — every injection verified to have changed
the artefact before the check was run on it:

  CONTROL   today's real 120-URL / 121-page build — CLEAN, 17 numbers from 11
            instruments, every relation held.
  BITE 1    an extra page written into dist and absent from the sitemap (the
            orphan shape of 08-17) — FAILS, NAMING the page. Note what the
            count rows do here: they all stay green, because the census derives
            its expectations from the dist it is reading. The set relation is
            the half that bites, which is the design.
  BITE 2    one <loc> in sitemap-0.xml swapped for a URL the build does not
            serve — served 121, sitemap 120, EVERY cardinality identical to the
            clean build and every arithmetic identity still true — FAILS,
            naming both the URL that appeared and the one that vanished. This
            is the bite the whole file exists for.
  BITE 3    an instrument's printed number altered while its behaviour is not
            (qa_ar_language made to print 58 for the 59 pages it checks) —
            FAILS, naming tool, population, expected and read.
  BITE 4    a pattern edited to match nothing — FAILS, naming the tool whose
            line it could not read, rather than quietly comparing the 16 rows
            it did find. MIN_ROWS is the second net, for a wholesale breakage.

  And a FIFTH result worth more than any of them, recorded because it is the
  trap and not the proof: the first attempt at BITE 3 used a regex that did not
  match the tool's print statement, so the injection never happened — and the
  census printed CLEAN, exactly as it does on a healthy build. A bite that
  fails to change the artefact is indistinguishable from a passing control
  (2026-09-14). Every injection above asserts the file changed before the check
  is run on it, and that assert is what caught this one.

  SIXTH, and the only one found by the census in production rather than on a
  bench: on the first build after today's Egypt draft landed, the census FAILED
  — on itself. It derived "held slugs" as len(held files)//2, because every
  piece in this corpus has always had an Arabic twin. Egypt is English-only
  until its Arabic is composed, so nine held files are five held slugs and the
  halving said four. qa_held_assets was right and the census was wrong. Fixed
  by counting distinct stems. Recorded here because it is the file's own thesis
  turned on the file: an invariant that has held for every piece so far is
  still an assumption, and dividing by it is how an assumption gets welded
  into an instrument.

Exit 0 clean; exit 1 with named defects; exit 2 on a usage or vacuity error.
It does NOT propagate a sibling's exit code: each sibling gates separately, and
a census that failed because qa_lastmod failed would report the wrong defect.
"""
import re
import subprocess
import sys
from pathlib import Path

# The site's base path, as astro.config declares it. Derived from the sitemap
# rather than hardcoded where it matters (#36); this constant is only used to
# turn a file path into the URL the sitemap would print for it.
ORIGIN = "https://education3881.github.io"

# Pages the build SERVES that the sitemap deliberately does not route. Each is
# named, each must exist, and anything else appearing in this difference is a
# defect. An exemption list is where defects hide (qa_reachability's own rule),
# so this one is asserted in both directions.
NOT_ROUTED = {
    "/madar/404.html": "the branded 404 (2026-09-09) — served by the host on a "
                       "miss, never a destination a crawler should be given.",
}

# A tool that produced no parseable number is a hole in the census, not a pass.
MIN_ROWS = 12

TIMEOUT = 180


def served_url(dist: Path, page: Path) -> str:
    """The URL the sitemap would print for a built file, or the raw path for a
    file the router does not own (404.html)."""
    rel = page.relative_to(dist).as_posix()
    if rel == "index.html":
        return "/madar/"
    if rel.endswith("/index.html"):
        return "/madar/" + rel[: -len("index.html")]
    return "/madar/" + rel


def populations(dist: Path, content: Path):
    """Every population the census compares, computed here and nowhere else."""
    served = {served_url(dist, p) for p in dist.rglob("*.html")}

    sm = dist / "sitemap-0.xml"
    sitemap = set()
    if sm.exists():
        sitemap = {
            u[len(ORIGIN):] if u.startswith(ORIGIN) else u
            for u in re.findall(r"<loc>([^<]+)</loc>", sm.read_text(encoding="utf-8"))
        }

    ar = {u for u in served if u.startswith("/madar/ar/")}
    en = served - ar
    articles = {u for u in served
                if re.fullmatch(r"/madar/(ar/)?articles/[^/]+/", u)}
    valence = {u for u in served if u.startswith("/madar/valence")}

    # The frontmatter BLOCK, never a fixed prefix of the file. Caught on this
    # file's own first run: a 4,000-character window classified 50 of 84 pieces
    # as held because their `sources[]` lists push `approved:` past character
    # 4,000. An arbitrary window that happens to contain the field today is the
    # 2026-09-14 masking trap wearing a different hat — read the structure.
    approved, held = set(), set()
    for d in ("articles", "articles-ar"):
        for f in sorted((content / d).glob("*.md")):
            text = f.read_text(encoding="utf-8")
            if not text.startswith("---"):
                held.add(f"{d}/{f.stem}")
                continue
            end = text.find("\n---", 3)
            fm = text[3:end if end != -1 else len(text)]
            m = re.search(r"^approved:\s*(true|false)\s*$", fm, re.M)
            # content.config.ts: approved is z.boolean().default(false) — an
            # absent flag is HELD, and the census mirrors the schema rather
            # than guessing.
            (approved if (m and m.group(1) == "true") else held).add(f"{d}/{f.stem}")

    # SLUGS, not files divided by two. The first draft of this file derived a
    # slug count as len(files)//2 on the assumption that every piece has an
    # Arabic twin, and the census bit on the very first build where that was
    # false: 2026-09-19's Egypt draft is English-only until its Arabic is
    # composed, so nine held files are five held slugs and the halving said
    # four. A corpus invariant that has held for every piece so far is still
    # an assumption, and dividing by it is how an assumption gets built into
    # an instrument.
    approved_slugs = {s.split("/", 1)[1] for s in approved}
    held_slugs = {s.split("/", 1)[1] for s in held}

    return {
        "served": served, "sitemap": sitemap, "ar": ar, "en": en,
        "articles": articles, "valence": valence,
        "approved": approved, "held": held,
        "approved_slugs": approved_slugs, "held_slugs": held_slugs,
    }


# Each row: the tool, its argv, and the numbers it prints — every one of them
# named with the SET it means, so the number can never again be read as "pages".
#   key       a stable label for the log
#   pattern   the printed line, with exactly one capturing group
#   expect    population size this number must equal, as a set expression
#   means     why that population and not `served`; printed on every clean run
ROWS = [
    ("qa_dist_input", ["qa_dist_input.py", "{dist}"], [
        ("built pages", r"qa_dist_input: (\d+) built page\(s\)",
         lambda P: len(P["served"]),
         "served — every *.html the build emits, the 404 page included"),
    ]),
    ("qa_chrome_links", ["qa_chrome_links.py", "{dist}"], [
        ("pages", r"qa_chrome_links: (\d+) page\(s\)",
         lambda P: len(P["served"]),
         "served — every pointer on every page the build emits, the 404 page "
         "included; its chrome is emitted by the same layout"),
    ]),
    ("qa_hreflang_clusters", ["qa_hreflang_clusters.py", "{dist}"], [
        ("sitemap URLs", r"sitemap URLs (\d+)",
         lambda P: len(P["sitemap"]), "the sitemap's own <loc> set"),
        ("pages", r"· pages (\d+)",
         lambda P: len(P["served"]), "served"),
        ("clusters+no-alternate", r"· clusters (\d+) · no-alternate pages (\d+)",
         lambda P: len(P["sitemap"]),
         "2x clusters + no-alternate pages must exhaust the sitemap set"),
    ]),
    ("qa_body_links", ["qa_body_links.py", "{dist}"], [
        ("approved pages", r"approved pages (\d+)",
         lambda P: len(P["articles"]),
         "article pages in dist — a held piece contributes none (#18)"),
    ]),
    ("qa_lastmod", ["qa_lastmod.py", "{dist}"], [
        ("URLs", r"— (\d+) URLs, (\d+) lastmod",
         lambda P: len(P["sitemap"]),
         "the sitemap set; every URL in it carries exactly one lastmod"),
    ]),
    ("qa_held_assets", ["qa_held_assets.py", "--dist", "{dist}"], [
        ("held slugs", r"qa_held_assets: (\d+) held slug\(s\)",
         lambda P: len(P["held_slugs"]),
         "held slugs — distinct stems, a piece with no Arabic twin yet counted once"),
        ("approved slugs", r"(\d+) approved slug\(s\)",
         lambda P: len(P["approved_slugs"]),
         "approved slugs — distinct stems"),
    ]),
    ("qa_reachability", ["qa_reachability.py", "{dist}"], [
        ("whole site pages", r"whole site, from /index\.html: pages (\d+)",
         lambda P: len(P["served"]), "served"),
        ("English side", r"English side, from /index\.html: pages (\d+)",
         lambda P: len(P["en"]), "served minus the Arabic side"),
        ("Arabic side", r"Arabic side, from /ar/index\.html: pages (\d+)",
         lambda P: len(P["ar"]), "served under /ar/"),
    ]),
    ("qa_jsonld", ["qa_jsonld.py", "{dist}"], [
        ("pages", r"qa_jsonld: pages (\d+)",
         lambda P: len(P["served"]) - len(NOT_ROUTED),
         "dist/**/index.html — the routed pages; the 404 is not one"),
    ]),
    ("qa_a11y_lang", ["qa_a11y_lang.py", "{dist}"], [
        ("pages", r"pages: (\d+)",
         lambda P: len(P["served"]), "served"),
    ]),
    ("qa_ar_language", ["qa_ar_language.py", "{dist}"], [
        ("Arabic pages", r"qa_ar_language: (\d+) Arabic pages",
         lambda P: len(P["ar"]), "served under /ar/"),
    ]),
    ("qa_consumer_surface", ["qa_consumer_surface.py", "{dist}"], [
        ("pages checked", r"pages checked: (\d+)",
         lambda P: len(P["served"]) - len(P["valence"]),
         "served minus VALENCE, which is outside the Astro layout by design"),
        ("sitemap <loc>", r"sitemap <loc>: (\d+) · <lastmod>: (\d+)",
         lambda P: len(P["sitemap"]), "the sitemap set"),
    ]),
    ("qa_geo_fields", ["qa_geo_fields.py", "{dist}"], [
        ("pieces", r"qa_geo_fields: (\d+) pieces checked",
         lambda P: len(P["approved"]) + len(P["held"]),
         "CONTENT files, not pages — held pieces included, which is why this "
         "number exceeds qa_body_links' approved pages by exactly the held set"),
    ]),
    # Assertion 22, added 2026-09-22 with the assertion itself. Its dateline
    # population is the article-page set, the same one qa_body_links names, so
    # #57 applies: if the two ever print the same number for different sets,
    # this row is where that shows.
    ("qa_date_identity", ["qa_date_identity.py", "{dist}"], [
        ("article datelines", r"PASS — (\d+) article datelines",
         lambda P: len(P["articles"]),
         "article pages in dist — every one must carry a dateline that agrees "
         "with its own frontmatter, which is why this equals qa_body_links' set"),
    ]),
]


def run(tools: Path, argv, dist: Path):
    """Run a sibling from the REPOSITORY ROOT, whatever our own cwd is.

    Found on this file's first run under `postbuild`, where npm sets cwd to
    `web/`: qa_body_links and qa_held_assets resolve the content collection as
    the relative path `web/src/content`, so from `web/` they look for
    `web/web/src/content` and exit 2 and 1 respectively. Latent until now only
    because the workflow has always invoked them from the root. The census is
    the first caller to invoke them from anywhere else, and the honest fix is
    for the census to name the environment it judges in (#16) rather than to
    inherit one — a sibling's answer must not depend on who called it.
    """
    root = tools.parent.parent
    cmd = [sys.executable] + [str(tools / a) if a.endswith(".py")
                              else a.format(dist=dist) for a in argv]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=TIMEOUT, cwd=str(root))
    except subprocess.TimeoutExpired:
        return None, "timed out after %ds" % TIMEOUT
    out = (p.stdout or "") + (p.stderr or "")
    if p.returncode >= 2 and not out.strip():
        return None, "exited %d with no output" % p.returncode
    return out, None


def main(argv):
    if len(argv) < 2:
        print("usage: qa_census.py <dist>", file=sys.stderr)
        return 2
    dist = Path(argv[1]).resolve()
    if not dist.is_dir():
        print("FAIL — no such dist: %s" % dist)
        return 2
    tools = Path(__file__).resolve().parent
    content = dist.parent / "src" / "content"
    if not content.is_dir():
        print("FAIL — no content collection beside the dist at %s" % content)
        return 2

    print("qa_census: %s" % dist)
    P = populations(dist, content)
    defects = []

    # ---- 1. the set relations, by name ----------------------------------
    if not P["sitemap"]:
        print("FAIL — the sitemap yielded zero URLs. A census with nothing to "
              "compare has failed, not passed.")
        return 2

    extra = P["served"] - P["sitemap"]
    missing = P["sitemap"] - P["served"]
    declared = set(NOT_ROUTED)

    for u in sorted(extra - declared):
        defects.append("served but not routed and not declared: %s — either "
                       "route it or declare it in NOT_ROUTED with a reason "
                       "(08-17: an unlinked page is a promise never made)" % u)
    for u in sorted(declared - extra):
        defects.append("NOT_ROUTED declares %s, which the build does not serve "
                       "— an exemption list is where defects hide" % u)
    for u in sorted(missing):
        defects.append("the sitemap routes %s, which the build does not serve "
                       "— a crawler is being sent to a 404" % u)

    if P["en"] | P["ar"] != P["served"] or P["en"] & P["ar"]:
        defects.append("the EN/AR split does not partition the served set")

    # ---- 2. what each population IS, printed every run ------------------
    print("qa_census: served %d · sitemap %d · EN %d · AR %d · article pages %d "
          "· content pieces %d (approved %d / held %d)"
          % (len(P["served"]), len(P["sitemap"]), len(P["en"]), len(P["ar"]),
             len(P["articles"]), len(P["approved"]) + len(P["held"]),
             len(P["approved"]), len(P["held"])))
    for u, why in sorted(NOT_ROUTED.items()):
        print("  served, not routed: %s — %s" % (u, why))

    # ---- 3. every instrument's printed number against its population ----
    read = 0
    for key, argv_t, checks in ROWS:
        out, err = run(tools, argv_t, dist)
        if out is None:
            defects.append("%s: %s" % (key, err))
            continue
        for name, pattern, expect, means in checks:
            m = re.search(pattern, out)
            if not m:
                tail = [l for l in out.splitlines() if l.strip()][-1:] or ["(no output)"]
                defects.append(
                    "%s: could not read its own '%s' line. The census cannot "
                    "compare a number it never found — this is a failure, not "
                    "a pass. Pattern: %s | its last line: %s"
                    % (key, name, pattern, tail[0][:160]))
                continue
            read += 1
            want = expect(P)
            got = [int(g) for g in m.groups()]
            if key == "qa_hreflang_clusters" and name == "clusters+no-alternate":
                got_val = got[0] * 2 + got[1]
                shown = "2x%d + %d = %d" % (got[0], got[1], got_val)
            else:
                if len(got) > 1 and len(set(got)) != 1:
                    defects.append("%s: '%s' printed %s — the same population "
                                   "twice, disagreeing with itself"
                                   % (key, name, got))
                    continue
                got_val, shown = got[0], str(got[0])
            status = "ok " if got_val == want else "BAD"
            print("  %s %-22s %-12s %-22s expected %d — %s"
                  % (status, key, name, shown, want, means))
            if got_val != want:
                defects.append(
                    "%s printed %s for '%s'; the population it means (%s) has "
                    "%d member(s). Either the tool is counting the wrong set or "
                    "it is printing the wrong label — both are defects in the "
                    "number a log will quote."
                    % (key, shown, name, means, want))

    # ---- 4. non-vacuity --------------------------------------------------
    if read < MIN_ROWS:
        print("FAIL — only %d of %d numbers could be read. A census that cannot "
              "find the numbers it exists to compare has failed, not passed."
              % (read, MIN_ROWS))
        return 1

    if defects:
        print("\nqa_census: %d defect(s) across %d number(s) read"
              % (len(defects), read))
        for d in defects:
            print("  DEFECT: %s" % d)
        return 1

    print("CLEAN qa_census — %d numbers from %d instruments, each against the "
          "population it names; served and sitemap differ by exactly the "
          "declared not-routed set, by name." % (read, len(ROWS)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
