# Ruling #145 — a constraint about a SCRIPT may not be enforced about a PAGE

**Filed:** 2026-11-16, by the quality function, closing standing-queue item 107.
**Family:** Assertion discipline (member **fifty-eight**).
**Supersedes nothing. Narrows the ENFORCEMENT of #115 and leaves #115's fact untouched.**

## The rule

**A correctness constraint is exact only where it is stated about the thing it is true of. Where the
layer doing the enforcing cannot address that thing, the constraint must be CARRIED by something a
composer authors — and the carrier must be a READ, not a convention.**

Ruling #115 is *Arabic is not slanted*, and it is right. Its enforcement was
`[dir="rtl"] em, [dir="rtl"] i, [dir="rtl"] cite { font-style: normal }` — a statement about a **page**
doing the work of a fact about a **script**. The two coincide only while every emphasised run on an
Arabic page is Arabic, and on 2026-11-16 **56 of 193 were not**: journal titles, Indonesian and Spanish
and Vietnamese terms, three Latin transliterations of one Arabic name, across **ten published pieces**,
upright for 22 days. Italic there is not decoration; it is the Latin script's own disambiguation.

**CSS cannot read the script of a text node.** It selects elements, and a script lives *inside* an
element's text — which is why no CSS-only repair exists: every candidate sets computed `font-style:
italic` on an element that may hold either script, and reds `qa_font_payload` limb 1 on 139 Arabic runs,
**correctly**. So the carrier is an explicit `lang` the Arabic composer writes, and the stylesheet keys
off it: `[dir="rtl"] .body-main em[lang] { font-style: italic }`.

## Three clauses

1. **The `lang` is a read, never a guess.** `kri` because our own English body says *"There is a Krio
   phrase Hawa used"*; `ar-Latn` for a transliterated Arabic name, because the script subtag is the
   honest tag and `en` would be a lie; `id` / `es` / `vi` off the registers' own language. This is #101
   clause 1 applied to a language instead of to a name: *the evidence and the claim ship together.*
2. **Safe by assertion, not by hope.** A rule that re-slants must be unable to slant Arabic. It is: limb
   1 of `qa_font_payload` fails the build on any slanted run carrying an Arabic code point. **The one
   thing the new rule must never do is the one thing a gate already forbids** — which is the shape to
   look for whenever a constraint is loosened. Loosen a rule only where an existing assertion already
   covers the hole.
3. **Write only the selector you can evidence.** The first draft carried `i[lang]` and `cite[lang]`
   beside `em[lang]` for symmetry, and `qa_selector_coverage` **failed the build on both**: markdown
   emits `<em>` and this corpus has no `<i>` or `<cite>` in a body. They were **deleted, not registered
   CONDITIONAL** — a conditional branch is a *template's untaken path*, and no template has this one.
   Three selectors written, one evidenced, and the gate said which.

## What the English edition did, and why it is the method rather than a courtesy

The row prescribed **one** repair for all 56. Reading each token against **the same token in the English
edition of the same piece** (#86, #101) split them into three:

| | N | What it is |
|---|---|---|
| A | 32 | Both editions italicise. The Arabic page is dropping a mark its own pair carries. **Repaired.** |
| B | 24 | **The English body prints it plain.** `*Nature*`, `*Elsevier*` ×4, `*Poynter*` ×2, nine `*«…»*` English quotations. The asterisks are a **script-boundary marker, not emphasis** — markdown offers the composer no other inline device, and in English there is no boundary to mark. **Not repaired**, handed to the Arabic Editor as item 122. |
| C | 2 | Two numeral cells of a three-cell table row whose third cell is **Arabic**. Any repair splits one typographic gesture across a script boundary. **Not a defect.** |

**Class B is the clause worth carrying.** Item 107's own prescription *cannot* reach it: tagging `Nature`
`lang="en"` and slanting it would make the Arabic edition italicise company names the English edition
sets upright — **a new EN/AR disagreement created by the repair**, which is the one outcome #86's method
exists to prevent. *A repair derived from one edition must be checked against the other before it is
applied, not after.*

## General form

*When a rule cannot be addressed to its own subject, it will be addressed to whatever the enforcing
layer can see — and that proxy is correct only while the two coincide. Ask what the rule is **about**,
ask whether the layer can name it, and if it cannot, move the statement to a layer that can rather than
accepting the proxy.* Pointed at a check this is #143; pointed at an **enforcement** it is this, and the
difference matters because a wrong check reports nothing while a wrong enforcement **changes bytes**.

**Evidence:** `agents/logs/qa-2026-11-16.md`; `web/src/styles/global.css`; queue items 107 (closed), 119,
122. Measured 193 elements / 137 Arabic-bearing / 56 Latin-only over served `dist`; 30 runs marked across
six published Arabic pieces; **26 of 30 verified italic by computed style in a browser**, the remaining
four blocked by the rule that earned **#146**.
