#!/usr/bin/env python3
"""arabic_side_reach.py — standing-queue item 36, measured rather than argued.

A MEASUREMENT, NOT AN ASSERTION, and the distinction is deliberate (#93, and the
precedent set 2026-11-06 by register_coverage.py): every number below is a fact about
today's corpus, no floor over any of them could gate without reddening a build that is
correct, and the file therefore carries no `qa_` prefix and is outside the glob that
counts the standing assertions. The register stays where it is.

WHAT ITEM 36 ASKED (raised 2026-10-23 as the daily's forward question):

  Every name instrument this operation owns is anchored on a LATIN token, so none can
  see into the edition we trust most. #101 makes the Arabic rendering the control for a
  disputed institution precisely because Arabic cannot carry a Latin acronym; #113 then
  measured 0 acronym anchors across all 44 Arabic bodies, by construction; #112 found
  128 of its 134 declined quotation tokens are Arabic. Is an Arabic-side instrument
  possible at all, or is the control permanently hand-read?

WHAT THIS FILE MEASURES, in two parts:

  (1) THE FIRST CUT THE ROW ASKED FOR, verbatim: count the Arabic-side determinations
      #86 and #101 require that are recorded anywhere in a hand-off, against the 44
      pairs that exist. Searched over content-drafts/** for the two mandated hand-off
      lines, mapped to the slug each document is about.

  (2) THE HALF THE ROW CALLED HARD. A boundary the ARABIC artefact supplies, on the
      model of #113: an acronym states how many words a name has, so it is a boundary;
      Arabic has no Latin acronym, so #113 reads 0 there. But Arabic commits a GENDER
      it cannot decline — #86's whole subject — and gender-committing tokens are a
      CLOSED CLASS. A role noun or an attribution verb beside a named human is an exact
      boundary, supplied by the artefact, in the edition no instrument of ours reads.

      And the anchor for the NAME, which Arabic does not supply, is supplied by the
      English edition's capitalisation. So the two editions anchor each other in
      OPPOSITE directions, per property: English supplies the name boundary and commits
      no gender; Arabic commits the gender and supplies no name boundary. That is what
      this file reports, and it is the reason the reach numbers below are stated per
      channel rather than as one rate.

WHAT IT DOES NOT DO: it does not decide any determination is wrong. A gender read off
the register is right and a gender read off the name may be right by luck; separating
them needs the register, which is a read and not a parse (#131). This file reports where
a second channel EXISTS, which is the only thing a parse can honestly report.

Usage:  python3 agents/tools/arabic_side_reach.py .
Exit:   0 always — a measurement cannot fail a build. 2 if the corpus is unreadable.
"""

import re
import sys
from pathlib import Path

# TWO BUCKETS, and the split is the whole correctness of this file.
#
# This desk's FIRST PASS put role nouns and attribution verbs in one list and reported
# 318 "gender commitments" across 44 of 44 AR bodies. That number was a FABRICATED
# measurement of the kind #123 was filed about: Arabic agreement is GRAMMATICAL, so
# `أعلنت الوزارة` — "the ministry announced" — is feminine because وزارة is a feminine
# noun, and nothing about a human was determined at all. A probe wider than its subject
# manufactures the finding it was aimed at. Corrected before it was believed.
#
# BUCKET A — tokens that cannot take a non-human subject and are followed by a PERSONAL
# NAME in this house's prose. An honorific is a boundary the artefact supplies, exactly
# as an acronym is in #113: it states that the next token names a person, and it states
# that person's gender. These are the Arabic edition's determinations about humans.
HUMAN_HONORIFICS = [
    ("الدكتور", "الدكتورة"), ("السيد", "السيدة"), ("الأستاذ", "الأستاذة"),
    ("الشيخ", "الشيخة"), ("البروفيسور", "البروفيسورة"),
]

# BUCKET B — tokens that commit a gender to WHATEVER their subject is, human or not.
# Measured and REPORTED, and deliberately excluded from the human count, because an
# institution's grammatical gender is a property of Arabic and not a claim about anybody.
AGREEMENT_ONLY = [
    ("الوزير", "الوزيرة"), ("المدير", "المديرة"), ("الرئيس", "الرئيسة"),
    ("الباحث", "الباحثة"), ("المسؤول", "المسؤولة"), ("الأمين", "الأمينة"),
    ("المفوض", "المفوضة"), ("المستشار", "المستشارة"), ("النائب", "النائبة"),
    ("المتحدث", "المتحدثة"), ("الخبير", "الخبيرة"), ("المعلم", "المعلمة"),
    ("قال", "قالت"), ("أضاف", "أضافت"), ("صرح", "صرحت"), ("أعلن", "أعلنت"),
    ("كتب", "كتبت"), ("وجد", "وجدت"), ("ذكر", "ذكرت"), ("أوضح", "أوضحت"),
    ("أشار", "أشارت"), ("قدم", "قدمت"), ("شغل", "شغلت"), ("تولى", "تولت"),
]
GENDER_PAIRS = HUMAN_HONORIFICS

# Tashkeel and tatweel: stripped before matching, because a composed Arabic body is
# voweled and the register's own tokens are not (the dek-cap lesson, 2026-06-17).
DIACRITICS = re.compile(r"[ـً-ْٰۖ-ۭ]")

EN_FEM = re.compile(r"\b(she|her|hers|herself|Ms\.|Mrs\.)\b")
EN_MASC = re.compile(r"\b(he|him|his|himself|Mr\.)\b")
EN_HONORIFIC = re.compile(
    r"\b(Dr|Professor|Prof|Minister|Sheikh|Sheikha|President|Director|Secretary|"
    r"Commissioner|Ms|Mr|Mrs)\.?\s+([A-Z][\w’'-]+(?:\s+(?:bin|bint|al|Al|el|El)\s+)?"
    r"(?:\s+[A-Z][\w’'-]+){0,3})"
)

HANDOFF_GENDER = "gender read from register"
HANDOFF_ACRONYM = "each expanded in"


def strip_marks(s: str) -> str:
    return DIACRITICS.sub("", s)


def body_of(path: Path) -> str:
    t = path.read_text(encoding="utf-8")
    parts = t.split("---")
    return "---".join(parts[2:]) if len(parts) > 2 else t


def frontmatter_of(path: Path) -> str:
    t = path.read_text(encoding="utf-8")
    parts = t.split("---")
    return parts[1] if len(parts) > 2 else ""


def main(root: Path) -> int:
    en_dir = root / "web/src/content/articles"
    ar_dir = root / "web/src/content/articles-ar"
    if not en_dir.is_dir() or not ar_dir.is_dir():
        print("REFUSED: content collections not found", file=sys.stderr)
        return 2

    en = {p.stem: p for p in sorted(en_dir.glob("*.md"))}
    ar = {p.stem: p for p in sorted(ar_dir.glob("*.md"))}
    pairs = sorted(set(en) & set(ar))

    print("arabic_side_reach — standing-queue item 36")
    print(f"  pairs on disk ............. {len(pairs)}  (EN {len(en)}, AR {len(ar)})")
    print()

    # ---- (1) the first cut: hand-off records of the two Arabic-side determinations ----
    drafts = sorted((root / "content-drafts").rglob("*.md"))
    g_slugs, a_slugs = set(), set()
    docs_unpublished = []
    for d in drafts:
        try:
            t = d.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if HANDOFF_GENDER not in t and HANDOFF_ACRONYM not in t:
            continue
        # The document must be ABOUT the pair, and the test for that is its own filename.
        # First pass matched the slug anywhere in the text and attributed the Bahrain
        # commission's hand-off lines to the PREDECESSOR piece, which that draft merely
        # names in `related:`. A mention is not a subject (#113's boundary question, in
        # the smallest possible form).
        hits = [s for s in pairs if s in d.name]
        if len(hits) != 1:
            docs_unpublished.append(d.relative_to(root))
            continue
        if HANDOFF_GENDER in t:
            g_slugs.add(hits[0])
        if HANDOFF_ACRONYM in t:
            a_slugs.add(hits[0])

    print("1 · THE FIRST CUT THE ROW ASKED FOR")
    print(f"  pairs with a #86 'named humans - gender read from register' hand-off line "
          f"... {len(g_slugs)} of {len(pairs)}")
    print(f"  pairs with a #101 'acronyms expanded ... each expanded in sources[]' line "
          f"... {len(a_slugs)} of {len(pairs)}")
    for s in sorted(g_slugs | a_slugs):
        print(f"    {s}  [{'86' if s in g_slugs else '--'}/{'101' if s in a_slugs else '---'}]")
    print(f"  documents carrying a mandated hand-off line about a slug that is NOT a")
    print(f"  published pair ............................................ {len(docs_unpublished)}")
    for d in docs_unpublished:
        print(f"    {d}")
    print()

    # ---- (2) the boundary the Arabic artefact supplies ----
    rows = []
    for slug in pairs:
        ar_text = strip_marks(body_of(ar[slug]) + "\n" + frontmatter_of(ar[slug]))
        en_text = body_of(en[slug]) + "\n" + frontmatter_of(en[slug])
        agree = 0
        for m, f in AGREEMENT_ONLY:
            for tok in (m, f):
                agree += len(re.findall(
                    rf"(?<![\w؀-ۿ]){re.escape(tok)}(?![\w؀-ۿ])", ar_text))
        masc = fem = 0
        toks_m, toks_f = set(), set()
        for m, f in GENDER_PAIRS:
            cm = len(re.findall(rf"(?<![\w؀-ۿ]){re.escape(m)}(?![\w؀-ۿ])", ar_text))
            cf = len(re.findall(rf"(?<![\w؀-ۿ]){re.escape(f)}(?![\w؀-ۿ])", ar_text))
            masc += cm
            fem += cf
            if cm:
                toks_m.add(m)
            if cf:
                toks_f.add(f)
        en_f = len(EN_FEM.findall(en_text))
        en_m = len(EN_MASC.findall(en_text))
        names = {re.sub(r"\s+", " ", g[1]).strip() for g in EN_HONORIFIC.findall(en_text)}
        rows.append({
            "slug": slug, "ar_masc": masc, "ar_fem": fem,
            "ar_tokens": sorted(toks_m | toks_f),
            "en_fem": en_f, "en_masc": en_m, "en_names": sorted(names),
            "agree": agree,
        })

    with_ar = [r for r in rows if r["ar_masc"] + r["ar_fem"] > 0]
    with_en_pron = [r for r in rows if r["en_fem"] + r["en_masc"] > 0]
    ar_only = [r for r in with_ar if r["en_fem"] + r["en_masc"] == 0]
    both = [r for r in with_ar if r["en_fem"] + r["en_masc"] > 0]
    with_names = [r for r in rows if r["en_names"]]

    print("2 · THE BOUNDARY THE ARABIC ARTEFACT SUPPLIES")
    print(f"  BUCKET B, excluded and printed: tokens that commit a gender to whatever")
    print(f"  their subject is, human or not ............................ "
          f"{sum(r['agree'] for r in rows)} across "
          f"{len([r for r in rows if r['agree']])} of {len(pairs)} AR bodies")
    print(f"    This was this file's first answer and it was WRONG: Arabic agreement is")
    print(f"    grammatical, so a feminine verb beside a feminine institution determines")
    print(f"    nothing about a person. Bucket A follows and is the real population.")
    print()
    print(f"  AR pieces carrying at least one HONORIFIC gender commitment "
          f"....... {len(with_ar)} of {len(pairs)}")
    print(f"  total gender-committing tokens across the 44 AR bodies "
          f"........ {sum(r['ar_masc'] + r['ar_fem'] for r in with_ar)}"
          f"  (masc {sum(r['ar_masc'] for r in with_ar)}, fem {sum(r['ar_fem'] for r in with_ar)})")
    print(f"  EN pieces carrying at least one gendered pronoun or title "
          f"..... {len(with_en_pron)} of {len(pairs)}")
    print(f"  EN pieces where an honorific anchors a NAME (the name boundary) "
          f".. {len(with_names)} of {len(pairs)}, "
          f"{sum(len(r['en_names']) for r in with_names)} distinct names")
    print()
    print(f"  BOTH channels present (AR commits, EN has a gendered form to disagree) "
          f".. {len(both)}")
    print(f"  ONE channel only (AR commits a gender NOTHING on the EN side can contradict) "
          f".. {len(ar_only)}")
    print()
    for r in sorted(ar_only, key=lambda r: -(r["ar_masc"] + r["ar_fem"]))[:12]:
        print(f"    AR-only  {r['slug']}  masc {r['ar_masc']} fem {r['ar_fem']}  "
              f"{' '.join(r['ar_tokens'][:4])}")
    print()
    for r in sorted(both, key=lambda r: -(r["ar_masc"] + r["ar_fem"]))[:8]:
        print(f"    both     {r['slug']}  AR masc {r['ar_masc']} fem {r['ar_fem']}  "
              f"| EN masc {r['en_masc']} fem {r['en_fem']}  | names {len(r['en_names'])}")
    print()
    print("3 · THE REACH, STATED AS A FRACTION AND NOT IMPLIED (item 41)")
    print("  This parse reads a CLOSED CLASS of 5 honorific pairs and no others, so a role")
    print("  noun outside the list is invisible to it: the count is a FLOOR on the Arabic")
    print("  edition's gender commitments, never a census. The EN name anchor is an")
    print("  honorific-anchored pattern and misses every name introduced without a title,")
    print("  which is #113's first detector failing for #113's reason.")
    print("  What is NOT a floor and IS exact: a piece with zero gendered forms on the EN")
    print("  side and a non-zero count on the AR side has ONE channel, whatever the")
    print("  detector's reach, because a detector cannot invent an EN pronoun that is")
    print("  absent. That number is the one this file exists to produce.")
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1] if len(sys.argv) > 1 else ".")))
