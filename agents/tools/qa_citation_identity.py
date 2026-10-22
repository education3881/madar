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
    ("straight-single", re.compile(r"(?<![A-Za-z])'([^'‘’]{10,260})'(?![A-Za-z])")),
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
    verdicts = []
    for tok in tokens:
        if tok["script"] != script:
            verdicts.append({"token": tok["token"][:120], "verdict": "script-mismatch",
                             "token_script": tok["script"]})
            continue
        is_ar = script == "arabic"
        needle = norm(tok["token"], is_ar)
        verdicts.append({"token": tok["token"][:120],
                         "verdict": "found" if needle in doc[is_ar] else "absent"})
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


def report(ordered: list[dict], registers: dict[str, dict]) -> None:
    buckets = collections.Counter(r.get("state") for r in ordered)
    print(f"  {len(ordered)} rows on file")
    for state, n in buckets.most_common():
        print(f"  {state:<20} {n:>4}")
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
