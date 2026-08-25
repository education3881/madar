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

Exit codes: 0 clean · 1 defects found · 2 nothing to check (which is a FAILURE,
per the 08-16 silent-pass trap — an assertion that finds no pages has not passed).
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


def main() -> int:
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
