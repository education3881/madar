#!/usr/bin/env python3
"""
qa_a11y_lang — standing assertion: no text is handed to a screen reader under
the wrong language.

WHY (Quality, 2026-08-25)
------------------------
Third surface of the consumer question, and the first one aimed at a human
rather than a machine. A screen reader chooses its voice and its pronunciation
rules from the nearest `lang` in the accessibility tree. It does not look at the
script of the characters. Arabic inside a subtree that resolves to `lang="en"`
is not read with an accent — it is read as noise, and vice versa.

WHAT IT CHECKS
--------------
For every rendered page, resolve `lang` by INHERITANCE (the nearest ancestor
that declares one, starting at <html>), then flag any text node whose script
disagrees with its resolved language.

Inheritance is the whole point, and the reason this check was written carefully
rather than quickly. A first, naive version looked only at the element holding
the text and reported 40 defects; two of them were the Arabic <em>s on the home
page, which sit inside `<div class="about__col ar" lang="ar">` and are entirely
correct. A check that cannot tell a real defect from an inherited-correct one
will get its real findings ignored. 38 were real: the still colophon.

SCOPE — chrome and headings, not prose.
Ruling #33's corollary stands: Latin script inside Arabic body text and inside
source titles is CORRECT — an institution keeps its own name, and a publication
whose whole claim is named primary sources must print those names as they are.
So `<article>` body prose and the sources block are deliberately exempt. This
checks the furniture we compose ourselves, where a mixed-script string is our
mistake and not the world's.

Exit codes: 0 clean · 1 defects found, OR the self-test fixture disagreeing ·
2 nothing to check (which is a FAILURE, per the 08-16 silent-pass trap — an
assertion that finds no pages has not passed).

THE SELF-TEST FIXTURE (added 2026-09-30, answering the 09-29 forward question)
-----------------------------------------------------------------------------
The 09-29 QA log asked which of the twenty-six fixture-free assertions could
have its original bite frozen into a permanent self-test, and which was cheapest
first. This one, for three reasons: its judgment is `LangAudit`, a pure function
of an HTML string, so a fixture needs no fake `dist`; four distinct wrong
readings are already written down in this docstring as prose; and the two real
bites that proved it on 2026-09-13 are one line each.

The distinction this closes is not the one `qa_census` already covers. A census
can tell you this check enumerated 121 pages; it cannot tell you the check can
still RECOGNISE the defect. `CHROME_CLASS`, `EXEMPT_CLASS` and `CHROME_TAGS` are
guesses about served markup, and a template change can quietly move a string out
of scope — after which the check enumerates everything, finds nothing, and
passes. *A bite run once is a claim about the day it ran; a fixture is a claim
about every day since.*

Each fixture carries `checked` as well as its findings, deliberately. Two of the
readings below are silent in both the correct and the broken code and differ only
in how many text nodes were looked at — a fixture that compares findings alone
cannot see a scope that collapsed.

**One historical bite could NOT be frozen, and that is reported rather than
quietly dropped.** The VOID-element stack bug (`<img>` pushed and never popped)
is unreachable against the current `handle_endtag`, which pops to the nearest
*matching* open tag rather than popping blindly — so removing the `VOID` guard
today changes no reading, because the later fix made the earlier bug
unreproducible. A fixture that cannot be made to fail is not a fixture. The
`VOID` set stays, the stack discipline is frozen instead through the stray-close
reading, and the limb is worth carrying: *some of an instrument's own history
stops being testable once a second defence lands, and the honest record says
which.*
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ARABIC = re.compile(r"[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]")
LATIN_LETTER = re.compile(r"[A-Za-z]")

# SCOPE IS AN ALLOWLIST, DELIBERATELY.
#
# The first version excluded prose by class name, which meant the check's
# correctness depended on guessing the class the markdown renderer happens to
# wrap body text in — and when the guess missed, the run reported Spanish
# pull-quotes and the name "Elsevier" as defects. Crying wolf on correct copy is
# how a standing assertion gets ignored, which is worse than not having one.
#
# So: check only the furniture we compose ourselves, named positively. Inside
# these subtrees a mixed-script string is our mistake. Everywhere else — body
# prose, pull-quotes, source titles — Latin script inside Arabic is CORRECT
# under ruling #33's corollary, because an institution keeps its own name.
CHROME_TAGS = {"header", "footer", "nav", "figcaption"}
CHROME_CLASS = re.compile(r"\b(skip-link|share|share-rail|lang-switch|site-nav|site-header|site-footer)\b")

EXEMPT_TAG = {"script", "style", "title", "code", "pre", "svg"}

# One carve-out INSIDE the chrome allowlist: the sources block sits in
# <footer class="article__footer">, so it inherits chrome scope. Source titles
# are the one place on this site where mixed script is not merely tolerated but
# required — we quote a register by the name it publishes under. Exempt by the
# exact class, now that it has been read off the rendered output rather than
# guessed at.
EXEMPT_CLASS = re.compile(r"\bsources\b")


# Elements that never have an end tag. If these are pushed onto the stack they
# are never popped, and every later `lang` resolves against a frame that should
# have closed — which is how the first run of this check reported `مدار` inside
# `<span lang="ar">` as Arabic-under-English. A stack-based audit is only as
# good as its stack discipline.
VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}


class LangAudit(HTMLParser):
    """Resolve `lang` by inheritance, tolerating real-world unclosed tags."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        # Each frame: (tag, resolved_lang, in_scope)
        self.stack: list[tuple[str, str, bool]] = [("", "", False)]
        self.findings: list[tuple[str, str, str]] = []
        self.checked = 0

    @property
    def lang(self) -> str:
        return self.stack[-1][1]

    @property
    def in_scope(self) -> bool:
        return self.stack[-1][2]

    def handle_startendtag(self, tag: str, attrs) -> None:
        return  # self-closing: contributes no subtree

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in VOID:
            return
        a = dict(attrs)
        lang = (a.get("lang") or self.lang or "").lower()
        if tag in EXEMPT_TAG or EXEMPT_CLASS.search(a.get("class") or ""):
            scope = False
        else:
            scope = (
                self.in_scope
                or tag in CHROME_TAGS
                or bool(CHROME_CLASS.search(a.get("class") or ""))
            )
        self.stack.append((tag, lang, scope))

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID:
            return
        # Pop to the nearest matching open tag. If there is none, this is a
        # stray close tag and the stack must be left alone rather than
        # truncated — either way the stack stays in step with the document.
        for depth in range(len(self.stack) - 1, 0, -1):
            if self.stack[depth][0] == tag:
                del self.stack[depth:]
                return

    def handle_data(self, data: str) -> None:
        if not self.in_scope:
            return
        text = data.strip()
        if not text:
            return
        lang = self.lang
        if not lang:
            return
        self.checked += 1
        base = lang.split("-")[0]
        has_ar = bool(ARABIC.search(text))
        has_la = bool(LATIN_LETTER.search(text))
        if base == "ar" and has_la and not has_ar:
            self.findings.append((lang, "latin-under-ar", text[:70]))
        elif base != "ar" and has_ar:
            self.findings.append((lang, "arabic-under-latin", text[:70]))


# Every fixture is a reading this check has really made, on this site's own
# markup shapes. Format: (what it is evidence of, html, expected findings as
# (kind, resolved-lang), expected count of text nodes checked).
SELF_TEST = [
    ("the bite of 2026-09-13 — 'Skip to content' in English on all 40 Arabic "
     "pages, the first thing a screen reader announces",
     '<html lang="ar"><body><a class="skip-link" href="#main">Skip to content'
     '</a></body></html>',
     [("latin-under-ar", "ar")], 1),

    ("the same bite reached by TAG instead of class — an English nav label on "
     "an Arabic page",
     '<html lang="ar"><body><nav class="site-nav"><a href="/">Editions</a>'
     '</nav></body></html>',
     [("latin-under-ar", "ar")], 1),

    ("the 38 real defects of 2026-09-13 — the still colophon, Arabic served "
     "under lang=en",
     '<html lang="en"><body><figure><figcaption>سكون</figcaption></figure>'
     '</body></html>',
     [("arabic-under-latin", "en")], 1),

    ("the naive version's false positive — an Arabic span that DECLARES its "
     "own lang inside English chrome is correct, and inheritance must see it",
     '<html lang="en"><body><footer><span lang="ar">مدار</span></footer>'
     '</body></html>',
     [], 1),

    ("the sources carve-out — a register keeps the name it publishes under "
     "(#33's corollary), and the sources block sits inside article chrome",
     '<html lang="ar"><body><footer class="article__footer">'
     '<ul class="sources"><li>Elsevier, Amsterdam</li></ul></footer>'
     '</body></html>',
     [], 0),

    ("the wolf-cry the allowlist was written to stop — a Spanish pull-quote in "
     "Arabic body prose is correct and must not even be looked at",
     '<html lang="ar"><body><article><blockquote>Todos los niños aprenden'
     '</blockquote></article></body></html>',
     [], 0),

    ("the mixed-script rule, which is a rule and not an oversight — Latin "
     "inside an Arabic caption that also carries Arabic is allowed",
     '<html lang="ar"><body><footer>سكون · The Still · Curated 51</footer>'
     '</body></html>',
     [], 1),

    ("stack discipline, frozen where the VOID bite could not be — a stray "
     "close tag must leave the stack alone; popping blindly takes the footer "
     "with it and silently empties this check's scope",
     '<html lang="en"><body><footer></div><span lang="ar">مدار</span> Madar'
     '</footer></body></html>',
     [], 2),
]


def run_self_test():
    """Read each fixture through the same LangAudit the tree goes through, so a
    fixture that passes is a statement about the code that actually runs.
    Returns the failures; an empty list means the recogniser still reads what it
    is known to have read."""
    failures = []
    for label, html, want_findings, want_checked in SELF_TEST:
        audit = LangAudit()
        audit.feed(html)
        got = sorted((kind, lang) for lang, kind, _ in audit.findings)
        if got != sorted(want_findings) or audit.checked != want_checked:
            failures.append((label, sorted(want_findings), want_checked,
                             got, audit.checked))
    return failures


def main() -> int:
    # The instrument is proved before the tree is judged. `qa_census` already
    # asserts that this check enumerates 121 pages; nothing but a fixture can
    # assert that it would still recognise the defect on one of them.
    st = run_self_test()
    if st:
        print("FAIL qa_a11y_lang — the language recogniser no longer reads what "
              "it is known to have read. %d fixture(s) failed:" % len(st))
        for label, want_f, want_c, got_f, got_c in st:
            print("    fixture: %s" % label)
            print("    expect : %s · %d text node(s) checked"
                  % (want_f or "no finding", want_c))
            print("    got    : %s · %d text node(s) checked"
                  % (got_f or "no finding", got_c))
        print("  A clean sweep read through a broken recogniser is the "
              "2026-08-16 silent pass. Fix the recogniser, not the site.")
        return 1
    print("qa_a11y_lang — recogniser proved on %d fixture(s) drawn from "
          "readings this check has really made." % len(SELF_TEST))

    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "web/dist")
    pages = sorted(dist.rglob("*.html"))
    if not pages:
        print(f"FAIL(2): no HTML found under {dist} — nothing to check is not a pass.")
        return 2

    total = 0
    checked = 0
    for page in pages:
        audit = LangAudit()
        try:
            audit.feed(page.read_text(encoding="utf-8"))
        except Exception as exc:  # a page we cannot parse is a defect, not a skip
            print(f"FAIL: {page} — unparseable ({exc})")
            total += 1
            continue
        checked += audit.checked
        for lang, kind, snippet in audit.findings:
            total += 1
            print(f"  {page.relative_to(dist)} [{kind}, lang={lang}] {snippet}")

    print(f"\npages: {len(pages)} · text nodes checked: {checked} · defects: {total}")
    if total:
        print("FAIL(1): text served under a language it is not written in.")
        return 1
    print("PASS: every checked text node agrees with its resolved language.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
