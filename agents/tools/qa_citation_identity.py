#!/usr/bin/env python3
"""
qa_citation_identity — is a 200 still the DOCUMENT we cited?

WHY THIS EXISTS (standing-queue item 18, raised 2026-10-15 as the daily's
forward question, taken 2026-10-22 after six displacements and seven days on
the board — the oldest item past the three-displacement threshold, tied with
item 17 on age and taken on displacement count, 6 against 4)
------------------------------------------------------------------------------
Every instrument this operation owns that touches an outbound promise
classifies it by **status code**. `qa_sources_alive` buckets what came back —
alive, dead, walled, timeout, bad certificate. `qa_body_links` proves the URL
is rendered. `qa_claim_registers` (#111) asks whether anybody, including us,
can still open the register at all. **Not one of them asks whether the bytes
at that URL are still the register the annotation describes.**

The defect is reachable and was reached by hand on 2026-10-15: a dead Kenya
citation's own WordPress permalink `?p=508411` returns **200 while serving a
listing page** with none of the article's text. Healthy by every test we own.
And it compounds with #100 — if a citation's death is the only event that
re-opens a register, a citation that dies **softly** (replaced at its own URL
by a listing, a paywall notice, a section front, a rewritten article) re-opens
nothing and reports healthy forever.

WHERE THE IDENTITY TOKEN COMES FROM, AND WHY IT IS NOT INVENTED
---------------------------------------------------------------
Item 18 specified "a distinctive string from the annotation". The annotation is
*our* prose, so a token chosen out of it would be a token we composed, and
asserting our own paraphrase against somebody else's server is the mistake #85
names on the input side. **It turns out nothing needs inventing.** Madār's
annotations already carry, inside quotation marks, strings this publication
asserts the register PRINTS:

    'Source: School census, Ministry of Education, 2025'
    'declined only marginally'
    « Le PASEC 2024 sera la dernière évaluation internationale »

Those are claims about somebody else's bytes, written by us, dated by us, and
**never once checked against those bytes.** Measured over the 682 source
entries of the 88 approved pieces: **213 of 341 EN entries and 210 of 341 AR
entries carry at least one such fragment** — 362 straight-quoted and 21
guillemetted in English, 335 guillemetted in Arabic. The quotation mark is the
operation's existing, unexploited identity token, and the only one with
evidentiary standing: we are not asking whether a document still *resembles*
what we said, but whether the sentence we put in quotation marks is still
there.

THE SCRIPT BOUNDARY, STATED IN CODE RATHER THAN INFERRED (#109's second half)
----------------------------------------------------------------------------
An Arabic annotation's guillemets frequently hold the Arabic *composition* of
an English or French register's words — Madār composes rather than translates
(#86), so the AR annotation renders the quotation into Arabic. That string is
not in the served document and never was. A check that failed on it would fail
on correct work and be switched off inside a week (#35).

So the comparison is licensed per token: **a token is testable against a
document only if the document carries at least `SCRIPT_FLOOR` characters of the
token's own script.** Arabic token against a document with no Arabic is
`script-mismatch` — a limit of the instrument, printed as such, never a defect.
This is the licence pattern assertion 34 limb 2 uses, applied to an input
instead of a cascade. **The floor is 200 and it is measured rather than chosen;
the first version of this rule used "contains any Arabic glyph at all" and was
wrong within one sweep** — see the comment at `SCRIPT_FLOOR`.

THE TWO HALVES, AND WHY ONLY ONE GATES — the #89/#111 design, reused third
--------------------------------------------------------------------------
  `--emit` (NOT gated, network). Fetches each token-bearing register, reads the
  served text, and records per token whether the quoted string is still there.
  Writes a dated row per URL into `agents/stats/citation-identity.json`. It must
  never gate a build: the far side belongs to ministries, newspapers and
  journals, and somebody else's rewrite at 09:00 is not our build's failure —
  the reason `qa_sources_alive` is one of the three that do not gate, written in
  `astro-pages.yml` where the others are listed.

  `--check` (GATED from postbuild, offline, deterministic). Asserts the register
  **covers the corpus**: every distinct `sources[].url` that supplies at least
  one identity token in an approved piece has a row. No network call, nothing
  known about the world. What it buys is #89's purchase: if the emit quietly
  stops describing some registers, or a piece ships a quotation nobody has ever
  compared against its source, the build fails instead of the measurement
  narrowing in silence.

WHAT IS PRINTED AND DELIBERATELY NOT ASSERTED
---------------------------------------------
The `absent` bucket. A quoted fragment missing from the served text has four
possible causes and only one is a defect of ours: the document was rewritten
(their change), the fragment sits in a PDF or an image or behind a renderer
(our client's limit), the fragment was elided across an ellipsis and our
splitting rejoined it wrong (this tool's limit), or we quoted something the
register never printed (**our** defect). Only a human read separates them. The
tool reports the bucket, names the pieces, and fails on none of it.

Exit codes: 0 clean · 1 defect · 2 cannot measure (emit only, nothing answered).
"""
from __future__ import annotations

import collections
import datetime
import gzip
import html
import json
import pathlib
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

REGISTER = pathlib.Path("agents/stats/citation-identity.json")
EDITIONS = (("articles", "en"), ("articles-ar", "ar"))
UA = "Madar-QA/1.0 (+https://education3881.github.io/madar/)"

# The quotation conventions this corpus actually uses, measured rather than
# assumed: straight single (362 EN), guillemets (21 EN, 335 AR), curly single
# (1 EN), escaped double (4 EN). Curly double is listed because the house style
# allows it and a future piece may carry it; it is not a guess about the past.
QUOTE_PATTERNS = (
    # STRICT APOSTROPHE RULE, shipped 2026-11-23 closing standing-queue item 48.
    # The first version's character class excluded `'` outright, so a match could
    # not cross an English POSSESSIVE apostrophe and the result was not a declined
    # token but NO token: `'South Korea's AI textbooks fail'`, `'Nation's Report
    # Card'`, `'Can't Wait to Learn'` were all invisible, and the row then reported
    # fewer quoted entries for the piece without reporting that it could not read
    # them. A `'` is an apostrophe exactly when a letter stands on BOTH sides of
    # it; anywhere else it is a quotation mark. Measured over the corpus on the day
    # it shipped: 338 -> 372 straight-single tokens, +34, with ZERO regressions
    # against the 338. A looser rule (any FOLLOWING letter) recovers 34 as well and
    # mis-splits two nested quotations, so it is not taken. 0 Arabic spans are
    # affected in either direction, guillemets having no such ambiguity and Arabic
    # no possessive apostrophe - the first instrument defect here that was
    # English-only.
    ("straight-single", re.compile(
        r"(?<![A-Za-z])'((?:[^'‘’]|(?<=[A-Za-z])'(?=[A-Za-z])){10,260})'(?![A-Za-z])")),
    ("curly-single", re.compile(r"‘([^‘’]{10,260})’")),
    ("curly-double", re.compile(r"“([^“”]{10,260})”")),
    ("guillemet", re.compile(r"«\s*([^«»]{10,260}?)\s*»")),
    ("escaped-double", re.compile(r'\\"([^\\]{10,260})\\"')),
)

ARABIC = re.compile(r"[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]")
# The licence is per SCRIPT and the scripts are enumerated, because an
# enumeration cannot report a distinction it cannot hold (#57/#70). Latin is
# last: it is the fallback, not a positive reading.
SCRIPTS = (
    ("arabic", ARABIC),
    ("cyrillic", re.compile(r"[Ѐ-ӿ]")),
    ("greek", re.compile(r"[Ͱ-Ͽ]")),
    ("cjk", re.compile(r"[぀-ヿ一-鿿가-힯]")),
    ("latin", re.compile(r"[A-Za-zÀ-ɏ]")),
)
TASHKEEL = re.compile(r"[ً-ْٰـ]")
ELLIPSIS = re.compile(r"…|\.\.\.|\[…\]|\[\.\.\.\]")
TAGS = re.compile(r"(?is)<(script|style)\b.*?</\1>|<[^>]+>")
WS = re.compile(r"\s+")
PUNCT_FOLD = str.maketrans(
    {
        "‘": "'", "’": "'", "‚": "'", "‛": "'",
        "“": '"', "”": '"', "„": '"',
        "–": "-", "—": "-", "‒": "-", "−": "-", "­": "",
        # U+2011 NON-BREAKING HYPHEN, found by hand and not by theory: Ghana News
        # Agency serves `out‑of‑school` with it and our annotation carries the
        # ASCII hyphen, so the instrument called a headline it still prints
        # `absent`. A hyphen's line-breaking behaviour is typography, not identity.
        "‐": "-", "‑": "-", "⁃": "-",
        " ": " ", " ": " ", " ": " ", " ": " ",
        "​": "", "‌": "", "‍": "", "‎": "", "‏": "",
        "ـ": "",
        "أ": "ا", "إ": "ا", "آ": "ا",
        "ى": "ي", "ة": "ه",
        # The quotation marks themselves go, on BOTH sides and symmetrically.
        # Found by hand, not by theory: the UN's Arabic interview serves
        # `يطلق عليها اسم "مكانّا (مكاننا)" باللغة العربية` and our annotation
        # quotes the same clause without the inner pair, so the instrument
        # reported `absent` on a register that carries our sentence verbatim.
        # A quotation mark inside a quotation is punctuation, not identity.
        '"': "", "'": "",
    }
)
# How much of a script a document must carry before a token in that script can
# be asked of it. MEASURED, not chosen: `decree.om/2026/rd20260012/` serves an
# English decree summary with **14** Arabic characters in 11,775 of text — a
# language-switcher label — and reported an Arabic token `absent` rather than
# `script-absent`, which is a false positive with a confident face. The UN's
# Arabic interview on the same sweep carries **8,874**. The two populations are
# three orders of magnitude apart, so the bar sits between them with room on
# both sides and the numbers are printed here rather than remembered.
SCRIPT_FLOOR = 200


def dominant_script(text: str) -> tuple[str, int]:
    """Which script is this document WRITTEN IN, not which scripts appear in it.

    The first version of the licence asked whether the document contained any
    glyph of the token's script, and it was wrong twice inside one sweep in both
    directions: `decree.om` serves an English decree with 14 Arabic characters
    of language-switcher label (so an Arabic token read `absent`), and
    `osvita.ua` serves a Ukrainian instrument whose Latin navigation is long
    enough to clear any floor (so an English rendering of a Cyrillic programme
    name read `absent` too). Both are mismatches, not absences.

    The rule is deliberately CONSERVATIVE: a bilingual register — Bahrain's BQA
    prints Arabic and English in the same row — has one dominant script, so a
    token in the other one is declined rather than compared. That trades a
    missed comparison for never making a confident wrong one, which is the right
    direction for an instrument whose output is a candidate list a human reads.
    """
    counts = [(name, len(rx.findall(text))) for name, rx in SCRIPTS]
    name, n = max(counts, key=lambda kv: kv[1])
    return (name, n) if n >= SCRIPT_FLOOR else ("too-short", n)


def token_script(token: str) -> str:
    for name, rx in SCRIPTS:
        if rx.search(token):
            return name
    return "latin"
# Non-distinctive strings: a token this short or this generic would be found in
# almost any document and would make a `confirmed` row mean nothing. Measured
# against the corpus, not invented: every entry below really appears quoted in
# at least one annotation.
STOP_TOKENS = {
    "the ministry", "the commission", "the authority", "the department",
    "ministry of education", "the government", "basic education",
    # THE ANNOTATOR'S OWN ASIDE - the false-positive class the strict apostrophe
    # rule had to name before it could ship (item 48's own condition, and #93's
    # floor: an instrument may not report a measurement it cannot license).
    # A quoted span inside `sources[]` is normally a claim about SOMEBODY ELSE'S
    # bytes, which is the whole premise of this instrument. This one is not: it is
    # the Researcher speaking about the citation, in quotation marks, inside the
    # annotation - a claim about nobody's bytes, which no fetch of any register
    # could ever confirm or refute. It is excluded by NAME and with its reason,
    # never by a heuristic, because the only thing that distinguishes it from a
    # real quotation is what it is ABOUT, and no pattern can read that.
    # NOTE THE SPELLING, AND IT IS THE SECOND FINDING OF THIS REPAIR: this set is
    # compared against the NORMALISED key, not against the annotation's own bytes,
    # and `norm()` deletes the apostrophe. Written in the artefact's spelling
    # (`index's`) the entry matches nothing and the token count does not move -
    # which reads exactly like a correct exclusion. 2026-09-14's second trap, on
    # the exclusion side: assert that the exclusion CHANGED the measurement before
    # believing it did.
    "the date is the indexs, not the articles",
}
BINARY_HINTS = (".pdf", ".xlsx", ".xls", ".docx", ".doc", ".zip", ".ppt", ".pptx")


# ------------------------------------------------------------------ the corpus


def _split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    rest = text[4:]
    i = rest.find("\n---")
    if i < 0:
        return "", text
    return rest[:i], rest[i + 4 :]


def norm(text: str, arabic: bool) -> str:
    """One normaliser for both sides of the comparison, so a match cannot be an
    artefact of which side was cleaned. Typographic quotes, dashes, nbsp and the
    bidi controls fold; Arabic additionally loses tashkeel and its alef/ya/ta
    variants, because a register that prints the same words voweled is the same
    register (the 06-17 tashkeel ruling's shape, on the input side)."""
    out = unicodedata.normalize("NFKC", text).translate(PUNCT_FOLD)
    if arabic:
        out = TASHKEEL.sub("", out)
    return WS.sub(" ", out).strip().casefold()


def served_text(raw: bytes, content_type: str) -> str:
    body = raw.decode("utf-8", "replace")
    if "html" in content_type or "<html" in body[:4000].lower():
        body = TAGS.sub(" ", body)
        body = html.unescape(body)
    return body


def tokens_from(annotation: str) -> list[dict]:
    """Every quoted fragment the annotation offers as the register's own words.

    An elided quotation ('aimed to train … within one year') is split at the
    ellipsis and the longest surviving run is kept: rejoining across an elision
    would assert a sentence the register never printed, which is this tool
    asserting its own artefact (#35's bite-first rule read as an input rule)."""
    found: list[dict] = []
    seen: set[str] = set()
    for convention, pattern in QUOTE_PATTERNS:
        for hit in pattern.findall(annotation):
            for run in ELLIPSIS.split(hit):
                run = run.strip(" ,;:.،؛")
                if len(run) < 14:
                    continue
                script = token_script(run)
                key = norm(run, script == "arabic")
                if len(key) < 14 or key in seen or key in STOP_TOKENS:
                    continue
                seen.add(key)
                found.append({"token": run[:260], "script": script, "convention": convention})
    return found


def read_corpus(root: pathlib.Path) -> tuple[dict[str, dict], list[dict]]:
    """url -> {tokens, pieces}; plus a per-piece record for the printed reading."""
    registers: dict[str, dict] = {}
    pieces: list[dict] = []
    for folder, lang in EDITIONS:
        base = root / "web" / "src" / "content" / folder
        for path in sorted(base.glob("*.md")):
            front, _ = _split_frontmatter(path.read_text(encoding="utf-8"))
            if "approved: true" not in front:
                continue
            titles = re.findall(r'^\s*-\s+title:\s*"(.*)"\s*$', front, re.M)
            urls = re.findall(r'^\s*url:\s*"(.*)"\s*$', front, re.M)
            key = f"{path.stem}:{lang}"
            record = {"slug": path.stem, "lang": lang, "entries": len(titles),
                      "shape_ok": len(titles) == len(urls), "tokens": 0, "quoted_entries": 0}
            if record["shape_ok"]:
                for annotation, url in zip(titles, urls):
                    toks = tokens_from(annotation)
                    if not toks:
                        continue
                    record["tokens"] += len(toks)
                    record["quoted_entries"] += 1
                    slot = registers.setdefault(url, {"tokens": [], "pieces": [], "_keys": set()})
                    if key not in slot["pieces"]:
                        slot["pieces"].append(key)
                    for tok in toks:
                        k = norm(tok["token"], tok["script"] == "ar")
                        if k in slot["_keys"]:
                            continue
                        slot["_keys"].add(k)
                        slot["tokens"].append(dict(tok, cited_by=key))
            pieces.append(record)
    for slot in registers.values():
        slot.pop("_keys", None)
    return registers, pieces


# ------------------------------------------------------------------- the world


def fetch(url: str, timeout: float = 25.0) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": UA, "Accept": "*/*", "Accept-Encoding": "gzip, identity"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read(2_500_000)
            if (r.headers.get("Content-Encoding") or "").lower() == "gzip":
                try:
                    raw = gzip.decompress(raw)
                except Exception:
                    pass
            return {"status": r.status, "ctype": (r.headers.get("Content-Type") or "").lower(),
                    "raw": raw}
    except urllib.error.HTTPError as exc:
        return {"status": exc.code, "ctype": "", "raw": b"", "note": "HTTPError"}
    except Exception as exc:
        return {"status": None, "ctype": "", "raw": b"", "note": type(exc).__name__}


# ------------------------------------------------------- WHICH FORM did it match
#
# STANDING-QUEUE ITEM 50, raised 2026-10-28 as the day's forward question, taken
# 2026-11-24 as the oldest OPEN row on a board with no DEFECT open (27 days).
#
# The row's finding, and it was measured rather than hypothesised: FOUR
# instruments of ours ask whether a quoted string is IN a document and none asks
# whether it is the string the document LEADS WITH. `restofworld.org` serves both
# `South Korea's AI textbooks fail after rushed rollout` (its <title>) and
# `AI-powered textbooks fail to make the grade in South Korea` (its <h1>), and
# BOTH are in the document. So a substring search over served text confirms a
# <title>-derived quotation forever and would have confirmed the wrong one of
# those two. #119 says a quotation mark promises a NAMED FORM; this instrument
# flattened every document to text before comparing and so could not tell the
# forms apart.
#
# The fix needs no network, which is why the row called it the first cut: the
# forms are in the bytes this tool ALREADY FETCHES, and only `served_text()` was
# throwing them away by stripping the tags before anybody looked.
#
# THE STANDING, PER FORM, AND IT IS A HIERARCHY RATHER THAN A LIST:
#   body        the token is in running text and in no headline form - the
#               ordinary case for a quotation from a SENTENCE, and the strongest
#               evidence this tool can get, because nothing else on the page
#               could have produced it.
#   h1          EVIDENCE. The form the document itself leads with.
#   title       WARNING. A tab's string, written for a tab, and routinely not
#               the headline the page prints.
#   og:title    WARNING. Written for somebody else's card, by a plugin, and the
#               form most likely to carry a publisher's house suffix.
#   headline    WARNING. JSON-LD, written for a crawler.
#   slug        COUNTERFEIT. A token that matches only the de-slugified URL path
#               is a token we recovered from the ADDRESS of the document, and the
#               address is ours to read, not theirs to print.
#
# PRINTED AND NOT ASSERTED, for the reason the `absent` bucket is printed: the
# form a register leads with belongs to the register's publisher, a `title`-only
# match is a warning about OUR annotation and not a defect in their document, and
# the repair - re-open the register and re-quote its own leading form - runs
# through a human read. Gating it would red the build on somebody else's CMS
# (#93, and the same reasoning `qa_claim_registers` gives for its network half).
# WHAT IS ASSERTED is one thing and it is in our lane: a `found` token in a row
# observed on or after FORM_EPOCH must CARRY its form, so an emit that silently
# stops recording forms fails the build instead of narrowing the measurement in
# silence (#89's purchase, third reuse).

FORM_EPOCH = "2026-11-24"   # the day the field shipped. Rows observed before it
# are NOT reconciled backward and the count of them is printed on every check -
# a point-of-filing rule fixes a count's future and leaves a step discontinuity
# where it was written, so the step is declared rather than discovered later
# (2026-10-04 second amendment, limb 2).

FORM_STANDING = {"h1": "evidence", "body": "running-text", "title": "warning",
                 "og:title": "warning", "headline": "warning", "slug": "COUNTERFEIT"}

_H1 = re.compile(r"(?is)<h1\b[^>]*>(.*?)</h1>")
_TITLE = re.compile(r"(?is)<title\b[^>]*>(.*?)</title>")
_OG = re.compile(r"""(?is)<meta[^>]+(?:property|name)\s*=\s*["']og:title["'][^>]*>""")
# QUOTE-AWARE ON PURPOSE, and it was found by being wrong on OUR OWN pages within
# an hour of shipping. The first version read `content\s*=\s*["'](.*?)["']`, which
# stops at the first quote character of EITHER kind — so an og:title containing a
# literal apostrophe inside a double-quoted attribute was truncated at the
# apostrophe, and `The teacher in Bo who still uses last term's chalk` was read as
# `The teacher in Bo who still uses last term`. It under-reads the form rather than
# over-reading it, so the failure mode is a token credited to a weaker form than
# the one that actually carries it — the exact error this limb exists to stop. The
# attribute's own opening quote is captured and the same character is required to
# close it.
_CONTENT = re.compile(r"""(?is)content\s*=\s*("|')(.*?)\1""")
_JSONLD = re.compile(r'(?is)"headline"\s*:\s*"((?:[^"\\]|\\.){3,300})"')
_INNER_TAGS = re.compile(r"(?s)<[^>]+>")


def _plain(fragment: str) -> str:
    return WS.sub(" ", html.unescape(_INNER_TAGS.sub(" ", fragment))).strip()


def headline_forms(raw: bytes, ctype: str, url: str) -> dict[str, list[str]]:
    """The document's own statements of its own name, read from the BYTES.

    Not from `served_text()`: that strips every tag, which is exactly the step
    that makes all forms indistinguishable. Each form may legitimately appear
    more than once (two <h1>s, a per-section JSON-LD block), so every form holds
    a LIST and a token is credited to the form if it matches any member - a
    document with two <h1>s has two things it leads with, and choosing one of
    them would be this tool inventing the answer."""
    forms: dict[str, list[str]] = {}
    if "html" in (ctype or "") or b"<html" in raw[:4000].lower():
        body = raw.decode("utf-8", "replace")
        h1s = [_plain(x) for x in _H1.findall(body)]
        if any(h1s):
            forms["h1"] = [x for x in h1s if x]
        titles = [_plain(x) for x in _TITLE.findall(body)]
        if any(titles):
            forms["title"] = [x for x in titles if x]
        ogs = []
        for tag in _OG.findall(body):
            m = _CONTENT.search(tag)
            if m and _plain(m.group(2)):
                ogs.append(_plain(m.group(2)))
        if ogs:
            forms["og:title"] = ogs
        heads = [_plain(x.encode().decode("unicode_escape", "replace"))
                 if "\\u" in x else _plain(x) for x in _JSONLD.findall(body)]
        if any(heads):
            forms["headline"] = [x for x in heads if x]
    # The slug is a form of the headline that the PUBLISHER wrote and the ADDRESS
    # carries, and it is the one form that is present even when the body is not.
    path = urllib.parse.urlsplit(url).path.rstrip("/").rsplit("/", 1)[-1]
    slug = re.sub(r"\.(html?|php|aspx?)$", "", path)
    slug = re.sub(r"[-_+]+", " ", urllib.parse.unquote(slug)).strip()
    if len(slug) >= 14:
        forms["slug"] = [slug]
    return forms


def standing_of(form: str, forms: dict[str, list[str]]) -> str:
    """What a form's match is WORTH, which is not a property of the form alone.

    THE THIRD STATE WAS FOUND BY THE FIRST READING AND SHIPPED THE SAME HOUR.
    Of the first 20 tokens classified, 3 matched a form other than the <h1> — and
    2 of those 3 documents serve NO <h1> AT ALL (`allafrica.com`,
    `demagog.org.pl`). Calling those a warning about our annotation would be a
    confident wrong reading: we cannot have quoted the wrong form on a document
    that declares only one. The warning is about US; this is about THEM, and a
    bucket that cannot tell them apart would hand a human a list in which two of
    every three entries are the instrument's own limit (#57/#70 — an enumeration
    cannot report a distinction it cannot hold, which is this corpus's most
    expensive single lesson).
    """
    base = FORM_STANDING[form]
    if base == "warning" and "h1" not in forms:
        return "warning-no-h1-served"
    return base


def classify_form(token: str, is_ar: bool, forms: dict[str, list[str]]) -> tuple[str, list[str]]:
    """Which of the document's own name-forms carries this token.

    Order is the hierarchy above, best first, so the reported form is the
    STRONGEST standing the token can claim - a token in both the <h1> and the
    <title> is evidence, not a warning. `body` is returned when the token is in
    the served text and in none of the forms, and it is deliberately ranked
    second rather than last: a sentence quoted from a document's prose is the
    ordinary, healthy case this instrument was built for."""
    needle = norm(token, is_ar)
    hits = [name for name in ("h1", "title", "og:title", "headline", "slug")
            if any(needle in norm(v, is_ar) for v in forms.get(name, []))]
    if not hits:
        return "body", []
    for name in ("h1", "title", "og:title", "headline", "slug"):
        if name in hits:
            return name, hits


def compare(url: str, tokens: list[dict], got: dict) -> dict:
    """One register, one dated reading. The verdict per token, then the row."""
    status = got.get("status")
    row: dict = {"status": status, "note": got.get("note", ""), "ctype": got.get("ctype", "")[:80]}
    if status is None:
        row["state"] = "unreached"
        return row
    if status in (401, 403, 429):
        row["state"] = "walled"
        return row
    if status != 200:
        row["state"] = "dead"
        return row
    binary = any(url.lower().split("?")[0].endswith(ext) for ext in BINARY_HINTS) or (
        got["ctype"] and not any(t in got["ctype"] for t in ("html", "text", "xml", "json"))
    )
    if binary:
        row["state"] = "unreadable-format"
        return row
    text = served_text(got["raw"], got["ctype"])
    script, chars = dominant_script(text)
    row["written_in"] = f"{script}:{chars}"
    doc = {True: norm(text, True), False: norm(text, False)}
    forms = headline_forms(got["raw"], got["ctype"], url)
    row["forms_read"] = sorted(forms)
    verdicts = []
    for tok in tokens:
        if tok["script"] != script:
            verdicts.append({"token": tok["token"][:120], "verdict": "script-mismatch",
                             "token_script": tok["script"]})
            continue
        is_ar = script == "arabic"
        needle = norm(tok["token"], is_ar)
        if needle not in doc[is_ar]:
            # A token absent from the served TEXT may still sit in a form the
            # text never carries - an og:title or a JSON-LD headline is in the
            # <head> and `served_text()` keeps it, but a slug is in the address
            # and nothing in the body holds it. So the forms are consulted here
            # too, and a token found ONLY in the slug is reported as the
            # counterfeit it is rather than as an absence.
            form, hits = classify_form(tok["token"], is_ar, forms)
            if form == "body":
                verdicts.append({"token": tok["token"][:120], "verdict": "absent"})
            else:
                verdicts.append({"token": tok["token"][:120], "verdict": "found",
                                 "form": form, "forms": hits, "h1_served": "h1" in forms,
                                 "standing": standing_of(form, forms)})
            continue
        form, hits = classify_form(tok["token"], is_ar, forms)
        verdicts.append({"token": tok["token"][:120], "verdict": "found",
                         "form": form, "forms": hits, "h1_served": "h1" in forms,
                         "standing": standing_of(form, forms)})
    row["tokens"] = verdicts
    kinds = {v["verdict"] for v in verdicts}
    if "found" in kinds:
        row["state"] = "confirmed" if kinds <= {"found", "script-mismatch"} else "partial"
    elif kinds == {"script-mismatch"}:
        row["state"] = "script-mismatch"
    else:
        row["state"] = "absent"
    return row


def emit(root: pathlib.Path, budget: int, spacing: float, stale_days: int) -> int:
    registers, _ = read_corpus(root)
    if not registers:
        print("FAIL qa_citation_identity — no quoted identity token found anywhere in the "
              "approved corpus (silent-pass trap)")
        return 1
    today = datetime.date.today().isoformat()
    cutoff = (datetime.date.today() - datetime.timedelta(days=stale_days)).isoformat()

    path = root / REGISTER
    rows: dict[str, dict] = {}
    if path.exists():
        rows = {r["url"]: r for r in json.loads(path.read_text(encoding="utf-8")).get("registers", [])}

    def owed(url: str) -> bool:
        row = rows.get(url)
        if row is None or row.get("state") in (None, "not-yet-asked", "unreached"):
            return True
        if len(row.get("tokens", [])) != len(registers[url]["tokens"]) and row.get("state") in (
            "confirmed", "partial", "absent", "script-absent"
        ):
            return True  # the annotation gained or lost a quotation since we asked
        # ITEM 50: a row whose confirmed token carries no FORM is owed, because the
        # form is read from the bytes and the bytes are not on file. This is #111's
        # top-up pattern rather than a backfill: the budget paces it across runs,
        # and a row re-read for its form is also re-read for its identity, so
        # nothing is spent on a weaker reading than the one the row already had.
        if any(v.get("verdict") == "found" and "form" not in v
               for v in row.get("tokens", [])):
            return True
        return str(row.get("observed", "")) < cutoff

    queue = [u for u in sorted(registers) if owed(u)][:budget]
    print(f"qa_citation_identity --emit · {len(registers)} registers carry a quoted identity token "
          f"({sum(len(v['tokens']) for v in registers.values())} tokens) · {len(rows)} rows on file · "
          f"{sum(1 for u in registers if owed(u))} owed · asking {len(queue)} this run "
          f"(budget {budget}, {spacing}s apart)")

    asked = unreached = 0
    for url in queue:
        got = fetch(url)
        row = {"url": url, "pieces": registers[url]["pieces"], "observed": today}
        row.update(compare(url, registers[url]["tokens"], got))
        if row["state"] == "unreached":
            unreached += 1
            rows.setdefault(url, row)
        else:
            rows[url] = row
        asked += 1
        if asked < len(queue):
            time.sleep(spacing)

    for url, slot in registers.items():
        rows.setdefault(url, {"url": url, "pieces": slot["pieces"], "observed": today,
                              "state": "not-yet-asked", "status": None, "note": "", "ctype": ""})
        if url in rows:
            rows[url]["pieces"] = slot["pieces"]

    if asked and unreached == asked:
        print(f"CANNOT MEASURE qa_citation_identity — nothing answered for any of the {asked} "
              "registers asked; register left as it was")
        return 2

    ordered = [rows[u] for u in sorted(rows)]
    out = root / REGISTER
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"observed": today, "registers": ordered}, indent=1,
                              ensure_ascii=False) + "\n", encoding="utf-8")
    report(ordered, registers)
    print(f"\n  written to {REGISTER}")
    return 0


def form_census(rows: list[dict]) -> tuple[collections.Counter, list[tuple[str, dict]]]:
    """Which of its own name-forms does each confirmed quotation sit in."""
    counts = collections.Counter()
    flagged: list[tuple[str, dict]] = []
    for r in rows:
        for v in r.get("tokens", []):
            if v.get("verdict") != "found":
                continue
            form = v.get("form", "unrecorded")
            counts[form] += 1
            if form in ("title", "og:title", "headline", "slug"):
                flagged.append((r["url"], v))
            # DERIVED from the row's own `forms_read`, never read off the stored
            # `standing` string, because the standing was written by whichever
            # version of this tool took the reading and the forms list is the
            # observation itself (#75: a number that lives in two places is
            # asserted from the one that is evidence).
            if FORM_STANDING.get(form) == "warning" and "h1" not in r.get("forms_read", []):
                counts["_no_h1"] += 1
    return counts, flagged


def print_form_census(rows: list[dict]) -> None:
    counts, flagged = form_census(rows)
    total = sum(counts.values())
    if not total:
        return
    print(f"\n  WHICH FORM DID IT MATCH — {total} confirmed token(s), item 50 (PRINTED, NOT ASSERTED):")
    total -= counts["_no_h1"]
    for form in ("body", "h1", "title", "og:title", "headline", "slug", "unrecorded"):
        if counts[form]:
            print(f"    {form:<12} {counts[form]:>4}   {FORM_STANDING.get(form, 'predates the field')}")
    if counts["_no_h1"]:
        print(f"    {'(of which)':<12} {counts['_no_h1']:>4}   matched a non-h1 form on a document that "
              "serves NO <h1> — the instrument's limit, not our defect")
    if flagged:
        print(f"\n  {len(flagged)} token(s) confirmed ONLY by a form that is not the document's <h1> —")
        print("  a candidate list for a re-quote, not a defect list; the form belongs to their publisher:")
        for url, v in sorted(flagged, key=lambda x: x[0])[:12]:
            print(f"    {v['form']:<9} {v.get('standing',''):<21} {url[:74]}")
            print(f"        {v['token'][:92]}")
        if len(flagged) > 12:
            print(f"    … and {len(flagged) - 12} more")


def report(ordered: list[dict], registers: dict[str, dict]) -> None:
    buckets = collections.Counter(r.get("state") for r in ordered)
    print(f"  {len(ordered)} rows on file")
    for state, n in buckets.most_common():
        print(f"  {state:<20} {n:>4}")
    print_form_census(ordered)
    missing = [r for r in ordered if r.get("state") in ("absent", "partial")]
    if missing:
        print("\n  QUOTATIONS NOT FOUND IN THE SERVED TEXT — a candidate list, not a defect list:")
        for r in sorted(missing, key=lambda x: x["url"])[:14]:
            print(f"    {r['state']} · {r.get('status')} · {r['url'][:94]}")
            print(f"        cited by {', '.join(r.get('pieces', []))}")
            for v in r.get("tokens", []):
                if v["verdict"] != "found":
                    print(f"        {v['verdict']:<13} {v['token'][:86]}")
        if len(missing) > 14:
            print(f"    … and {len(missing) - 14} more")


# -------------------------------------------------------------------- the gate


def check(root: pathlib.Path) -> int:
    registers, pieces = read_corpus(root)
    tokens = sum(len(v["tokens"]) for v in registers.values())
    approved = [p for p in pieces if p["entries"]]
    print(f"qa_citation_identity --check · {len(approved)} approved pieces · "
          f"{sum(p['entries'] for p in approved)} source entries · "
          f"{sum(p['quoted_entries'] for p in approved)} carry a quoted identity token · "
          f"{tokens} tokens over {len(registers)} distinct registers")
    if not registers or not tokens:
        print("FAIL qa_citation_identity — zero identity tokens extracted from an approved corpus "
              "that carries 682 source entries (silent-pass trap: a check that finds nothing to "
              "check has failed, not passed)")
        return 1

    by_lang = collections.Counter()
    for p in approved:
        by_lang[p["lang"]] += p["quoted_entries"]
    print(f"  quoted entries by edition: " + " · ".join(f"{k} {v}" for k, v in sorted(by_lang.items())))
    unpaired = [f"{p['slug']}:{p['lang']}" for p in approved if not p["shape_ok"]]
    if unpaired:
        print(f"  NOTE: {len(unpaired)} piece(s) whose title and url lines do not pair one-to-one, so "
              f"no token is attributed for them: {', '.join(unpaired[:6])}")

    path = root / REGISTER
    if not path.exists():
        print(f"FAIL qa_citation_identity — no register at {REGISTER}; run --emit")
        return 1
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = {r["url"]: r for r in data.get("registers", [])}
    required = {"url", "pieces", "observed", "state"}
    missing = sorted(set(registers) - set(rows))
    malformed = sorted(u for u, r in rows.items() if not required <= set(r))
    orphans = sorted(set(rows) - set(registers))
    print(f"  register observed {data.get('observed')} · {len(rows)} rows · "
          f"{len(orphans)} orphan row(s) kept on purpose — a withdrawn quotation's observation is "
          "history and deleting it would lose the only record of it")

    answered = [r for r in rows.values() if r.get("state") not in (None, "not-yet-asked")]
    buckets = collections.Counter(r.get("state") for r in rows.values() if r["url"] in registers)
    print("  state as last observed: " + (" · ".join(f"{k} {v}" for k, v in buckets.most_common())
                                          or "nothing asked yet"))
    print(f"  CANDIDATE LIST, NOT ASSERTED: {buckets['absent'] + buckets['partial']} register(s) of "
          f"{len(answered)} asked no longer serve a quotation we attributed to them. Four causes, one "
          "of them ours; only a human read separates them, so this fails nothing.")

    # ---- ITEM 50's GATED LIMB: a form recorded, or the field has stopped working.
    # In our lane and therefore gated, where the form's STANDING is not (#93): if a
    # future emit drops the field, every `found` token silently loses the one thing
    # that distinguishes an <h1> from a tab's string, and the census above would
    # keep printing a smaller total with no sign that anything had changed.
    formless, pre_epoch, post_epoch = [], 0, 0
    for u, r in rows.items():
        found = [v for v in r.get("tokens", []) if v.get("verdict") == "found"]
        if not found:
            continue
        if str(r.get("observed", "")) < FORM_EPOCH:
            pre_epoch += 1
            continue
        post_epoch += 1
        if any("form" not in v for v in found):
            formless.append(u)
    print(f"  item 50 — {post_epoch} row(s) observed on or after {FORM_EPOCH} carry a confirmed "
          f"token and must record its form; {pre_epoch} row(s) predate the field and are DECLARED "
          "rather than reconciled backward, their forms arriving as each row's reading comes due")
    print_form_census([r for r in rows.values() if r["url"] in registers])

    if formless:
        print(f"\nFAIL qa_citation_identity — {len(formless)} row(s) observed on or after "
              f"{FORM_EPOCH} hold a `found` token with no recorded form:")
        for u in formless[:8]:
            print(f"  {u[:110]}")
        print("Run: python3 agents/tools/qa_citation_identity.py . --emit")
        return 1

    if missing or malformed:
        if missing:
            print(f"\nFAIL qa_citation_identity — {len(missing)} register(s) supply a quoted identity "
                  "token and have no row:")
            for u in missing[:12]:
                print(f"  {u[:110]}")
                print(f"      cited by {', '.join(registers[u]['pieces'])}")
            if len(missing) > 12:
                print(f"  … and {len(missing) - 12} more")
        if malformed:
            print(f"FAIL qa_citation_identity — {len(malformed)} row(s) missing required fields")
            for u in malformed[:6]:
                print(f"  {u[:110]}")
        print("Run: python3 agents/tools/qa_citation_identity.py . --emit")
        return 1
    print(f"CLEAN qa_citation_identity — every one of {len(registers)} quotation-bearing registers "
          "has a dated reading on file")
    return 0


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    root = pathlib.Path(args[0]).resolve() if args else pathlib.Path.cwd()
    if not (root / "web" / "src" / "content").is_dir():
        print(f"FAIL qa_citation_identity — {root} is not the repository root")
        return 1
    budget, spacing, stale = 30, 1.5, 30
    for a in argv[1:]:
        if a.startswith("--budget="):
            budget = int(a.split("=", 1)[1])
        elif a.startswith("--spacing="):
            spacing = float(a.split("=", 1)[1])
        elif a.startswith("--stale-days="):
            stale = int(a.split("=", 1)[1])
    if "--emit" in argv:
        return emit(root, budget, spacing, stale)
    return check(root)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
