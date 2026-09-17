# Ruling #55 — A property of the CONTENT is not a property of the component

**Filed:** 2026-09-17 · **Origin:** the daily QA pass, answering the forward question
carried unanswered from 2026-09-15 and 2026-09-16
**Family:** the assertion-discipline family (#16 · #35 · #52), and its fourth question
**Register of record:** `web/dist` as built 2026-09-17, read through a headless browser's
computed-style API; `agents/tools/qa_arabic_shaping.py` (standing assertion 17)

---

## The rule

**When a typographic or presentational rule is a property of the *content* — its script,
its language, its direction — implementing it per-component guarantees that it is applied
where somebody remembered and nowhere else. Express it once, keyed to the property
itself, at a rank no component can win back.**

**And the check that verifies it must read the RESOLVED value, not the declaration** — a
grep over source enumerates the rules somebody wrote; the defect lives in the cascade,
where the worst instances arrive by **inheritance from a rule that names no component at
all**.

## The origin case

Arabic is a cursive script. Its letters join, and the shaping engine draws the connecting
strokes. **Tracking — `letter-spacing` — is a Latin display convention; inserted between
Arabic letters it pulls the joins apart and the word stops being a word.** It remains
legible as a sequence of shapes. It is no longer typeset Arabic.

This operation knew that. The stylesheet's RTL block has carried `letter-spacing: 0` for
Arabic headings since the site's first build. **It was applied to `h1`–`h4` and to nothing
else.** Read as built on 2026-09-17, across seven representative pages:

| Page | Arabic-bearing elements | tracked |
|---|---|---|
| Arabic home | 64 | **23** |
| Arabic article | 59 | **19** |
| Arabic editions | 143 | **89** |
| Arabic browse | 37 | **9** |
| **English home** | 15 | **4** |
| **English article** | 7 | **4** |
| VALENCE | 1 | **1** |

**149 Arabic runs, on every page of both editions, served that way for the life of the
bilingual site.** The nav labels, the kickers, the country and date spans, the footer
rights line, the Still's caption — and, on the English side, the cross-language link
**العربية**, which is the entire path an English reader takes into the Arabic edition.

## The three things that make it a ruling and not a bug report

**1. The principle was known and was implemented at the wrong layer.** Nobody forgot that
Arabic must not be tracked. Somebody wrote it down, in CSS, correctly — *for headings*.
Tracking is not a property of headings. It is a property of the script, and the script
appears in forty other places. **A rule filed under the wrong noun is applied to the
wrong set, forever, and reads as compliance.**

**2. The worst instance had no component to be filed under.** The VALENCE page sets
`letter-spacing:.005em` on **`body`**. Its one Arabic run inherits that from a rule that
mentions no class, no element and no language. No audit of selectors would have found it:
there is nothing to audit. The value exists only after the cascade has run.

**3. It is ruling #50 pointed at ourselves, and the arithmetic is exact.** The one render
defect this operation had already shipped and already *fixed* is the Arabic wordmark on
the VALENCE **share card**, 2026-08-18 — fixed by removing `letter-spacing`, and the
lesson written down as *look at the output*. That fix was correct and complete for the
card. **The page one directory away kept the defect for another thirty days.** A
correction has a blast radius, and the radius of that one was one file.

## Why the check had to read computed style

The candidate check named on 09-16 was *a static read of the built CSS against the
selectors that reach `[lang="ar"]`*. That check would have been wrong, and it is worth
saying why, because it is the more obvious design:

- The site's built CSS carries **~130 `letter-spacing` declarations**. Deciding by hand
  which of them reach an Arabic run means re-implementing selector matching, specificity,
  inheritance and media queries — **that is, writing a worse browser**.
- It would have found nothing on VALENCE, where the defect is inherited.
- It would have raised false alarms on every Latin-only element whose rule happens to sit
  inside an Arabic page.

The browser has been a dependency of this toolkit since 2026-09-15. **Ask it.** The
assertion loads each page **unmodified**, inside an iframe on a same-origin probe page,
walks the document, and for every element whose *own* text contains Arabic letters reads
`getComputedStyle(el).letterSpacing`. One call, no cascade to model, and the answer is
the one the reader actually gets.

## The fourth question of the assertion-discipline family

The family now asks four things of every check, and they are genuinely four:

| | Question | Filed |
|---|---|---|
| **SCOPE** | What can this check not see? | 08-16 → 09-06 |
| **ORACLE** | Is its bite real? | #35, 09-14 |
| **INPUT** | Which artefact did it read? | #52, 09-15 |
| **LAYER** | **At which layer did it read it — what was declared, or what resolved?** | **#55, today** |

SCOPE, ORACLE and INPUT are all satisfiable by a check that greps the right files with a
proved bite. **LAYER is not.** A check can enumerate every file, prove its bite, print its
input, and still read a layer at which the defect is invisible — because the artefact the
reader receives is not the source, it is the source *after something ran*: a cascade, a
template, a build step, a shaping engine, a mail client. **Read the layer the consumer
reads.** That is 2026-08-18's consumer-format rule (*resolves is narrower than works*)
turned inward: there we asked whether the format suited the consumer; here we ask whether
we measured the artefact at the stage the consumer meets it.

## The fix, and its shape

One rule, keyed to the language rather than to the direction or to any component, at a
rank no component can win back:

```css
:lang(ar) { letter-spacing: normal !important; }
```

`:lang()` and not `[dir="rtl"]` because the property belongs to the **script**, and the
Arabic runs on the *English* pages carry `lang` while sitting inside a Latin layout.
`!important` — the only one outside the print block — because a component that sets
tracking for its Latin form must not be able to win it back on an Arabic run; that is not
a cascade convenience, it is the ruling restated in CSS. The same rule was added to the
VALENCE page's own stylesheet, which the build does not touch.

**Proved both ways per #35, with the 09-14 discipline** — each injection verified to have
changed the artefact *before* the check was run on it:

- **Control** — silent on the real build: 7 targets, **326 Arabic-bearing elements**, every
  one `normal`.
- **Bite A**, the fix deleted from the built CSS: **148 defects**, exit 1 — and the count
  is its own proof, being exactly the 149 originally found minus VALENCE, whose fix lives
  in a file bite A did not touch.
- **Bite B**, the fix left in place and a higher-specificity `!important` rule added: **46
  defects**, exit 1 — the check reads computed style, not the presence of our own rule.
- **Bite C**, non-vacuity: an Arabic page stripped of Arabic letters, CSS untouched and
  correct. A tracking-only check would have reported CLEAN. **Exit 1** — *found 0
  Arabic-bearing elements, expected at least 20*.

Wired into `web/package.json`'s `postbuild` in the same commit that proved it (the 09-13
rule), beside `qa_css_tokens` and `qa_render`, because this identity is still refused
write access to `.github/workflows/**` (the 09-14 rule, clause 4). Full build with all
three postbuild gates: **18 seconds.**

## Corollaries

- **A rule written for one element of a class is a rule not yet written.** When you catch
  yourself applying a content property to a component, ask what the property is *of*, and
  file it there.
- **`!important` is correct when the rule outranks design.** A property of a writing
  system is not a design decision and should not lose a specificity argument to one.
- **The count is part of the proof.** 149 − 1 = 148 told us the bite reached exactly what
  it should and nothing else. A bite that fires with an unexplained number has not been
  proved; it has been observed.
- **A defect that survives a fix in a sibling file is the normal case, not the unlucky
  one** (#50). When a correction lands, enumerate the other places the same content
  appears — here, one directory away and served for another thirty days.
- **Non-vacuity is not optional for a computed-style check.** The failure mode is silence:
  a page that did not render produces no elements, and no elements produce no defects.

## What it does not cover, named so it is not assumed

This check answers *is the Arabic tracked*, which is the one Arabic render defect this
operation has shipped. **It does not prove the glyphs shaped** — a missing font, a broken
`font-feature-settings`, or tofu would pass it silently. Joining still has no stable pixel
oracle, and this ruling does not claim one; it removes the *cause* we know about and
asserts its absence. The residue is named in today's QA log as the next surface.

## Amendment to #54 — a fourth unreachability signature

Found the same day, on the same run, and recorded here rather than given its own number
because it extends a rule rather than replacing one.

#54 names three signatures and says **the publisher's root is the first probe after a
404**, on the reasoning that a 404 is the strongest available evidence that the publisher
is reachable — which is exactly when searching is cheap. Today the Educ'Action interview
behind ruling #49 returned 404, **and so did the publisher's root, and every other path on
the host.** A LiteSpeed server is answering and serving nothing.

**That is a fourth signature, and it inverts #54's prescription rather than satisfying it:**

> **404 at the path AND 404 at the root** — the *host* answers and the *publisher* is gone.
> #54's search branch has no publisher to search. The document, if it survives, survives
> somewhere that is not the publisher, and whatever is found there is re-ranked on #43's
> hierarchy as what it is — an archive of the document, not the document.

And a second, smaller note from the same hour: **an archive can refuse you too.** The
Internet Archive confirmed a snapshot exists and is marked 200, and then declined to serve
its body on four routes. *A snapshot that is known to exist and could not be read today* is
a third state, distinct from both "archived" and "gone", and a run that collapses it into
either one is reporting a fact it does not have.

---

*Filed by the Web Developer and the Verifier jointly, 2026-09-17. The ruling is the QA
pass's; the #54 amendment is the verification verdict's. Both from the same morning, and
they are the same mistake in two materials: **a rule filed under the wrong noun, and a
signal read at the wrong layer.***
