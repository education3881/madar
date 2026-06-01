# Arabic Editor — 2026-06-01 verdict: Indonesia / Qatar / Uruguay AR companions

## Scope

Three Arabic companion pieces, drafted today in fusha against EN articles published 2026-05-31. These close the AR-side gap left after the 2026-05-31 override-mode run, in which three fresh EN pieces shipped and AR translations were sequenced for a later day. Today is that day.

| # | Piece | EN slug | AR file on disk | Status |
|---|---|---|---|---|
| 1 | Indonesia — Permen 13 / Coding & AI | `2026-05-31-indonesia-permen-13-coding-ai` | `web/src/content/articles-ar/2026-05-31-indonesia-permen-13-coding-ai.md` | **approved** |
| 2 | Qatar — Spark / Humanity.io | `2026-05-31-qatar-humanity-spark-strategy` | `web/src/content/articles-ar/2026-05-31-qatar-humanity-spark-strategy.md` | **approved** |
| 3 | Uruguay — Plan Ceibal / EduIA Lab | `2026-05-31-uruguay-eduia-lab-ceibal` | `web/src/content/articles-ar/2026-05-31-uruguay-eduia-lab-ceibal.md` | **approved** |

## Rubric pass — five tests

For each AR piece I applied the Editor's standing five-test rubric — sourcing reality, specificity, why-now, dignity, long-arc — and the AR-specific tests for fusha register fit, named-human transliteration, and source-block bilingual integrity. Source URLs in each AR frontmatter were verified against the EN source block; same URLs, AR-language source-title summaries.

### 1. Indonesia

- **Sourcing reality:** all three Indonesian-language quotes carried in the AR body match the EN quotes letter-for-letter; the English gloss in the AR is a transparent translation, not a paraphrase. The Ministry press release URL resolves and contains the verbatim quotes. The Jakarta Globe dispatch URL resolves and contains the Pujianto quote and the 59,000-school figure. The Tempo English piece on the post-October-2024 ministerial posture resolves.
- **Specificity:** the rollout architecture (30 computers, one class per day, no specialised teacher) is preserved at sentence-level in AR. The phased start (grades 5/7/10) and the 2025–2026 academic year are kept exact.
- **Why-now:** the piece holds the September 2024 → July 2025 → August 2025 arc through which the regulation became visible. Holds.
- **Dignity:** Principal Pujianto's name is preserved in transliteration, his quote is rendered with the operational candour it carries in EN — no improvement, no rhetorical flattening.
- **Long-arc:** the 2013-Curriculum / Independent-Curriculum / Permen-13 succession is held as a twelve-year arc, not three discrete reforms. Reads in AR the way the EN reads.
- **AR register:** fusha-analytic. Tashkeel used selectively on key analytical verbs and on potentially-ambiguous nouns. Foreign terms (Permendikdasmen, Kurikulum 2013, Kurikulum Merdeka) preserved in Latin script with AR explanation in parentheses where first introduced.

### 2. Qatar

- **Sourcing reality:** the Al Nuaimi quote on the 44% → doubling target is preserved letter-for-letter in AR with the EN behind it. The Yiannouka quote on AI accelerating is preserved. The minister-handoff date (12 November 2024) is preserved.
- **Specificity:** four STEM schools, ~500 students each, 2,000 collective; *Humanity.io* as the WISE 12 theme with its 24–25 November 2025 dates and five thematic tracks — all preserved.
- **Why-now:** the 18-month-mark test (May 2026 = now) is kept as the active editorial frame; the AR reader is positioned at the same moment the EN reader is.
- **Dignity:** the named ministers (Al Nuaimi as architect; Al-Khater as implementer) are both rendered as institutional figures, neither flattered nor diminished. The transition is described as "untroubled in public record" in AR as in EN.
- **Long-arc:** the strategy as inherited document, not single-author project — held.
- **AR register:** fusha-analytic, slightly more formal than the Indonesia piece in keeping with the regulator-and-ministerial subject. The reader is placed inside a GCC strategy document and the AR register matches.

### 3. Uruguay

- **Sourcing reality:** all three Spanish-language quotes (Haim on origin and equity; Haim on the bet being large; Orsi's "Hacemos historia, haciendo futuro") are preserved letter-for-letter with AR gloss. Source URLs verified against EN.
- **Specificity:** the 205,000-students / 10,000-teachers / 85%-urban-coverage numbers preserved exactly. The 3-million-devices, 100%-Wi-Fi, 22,300-Campus-del-Sur participants figures kept. The 18-year-anniversary timing and the 28 March 2025 launch date kept.
- **Why-now:** the bet is open; the first publishable evidence is 12–18 months out; the 2027 anniversary will arrive mid-bet — all held in AR.
- **Dignity:** Haim is rendered as institutional successor, Folgar (her predecessor) as institutional continuity figure, four named presidents as the political weather the institution endured. None diminished.
- **Long-arc:** this is the AR piece most about long-arc, by construction. The 19-year compounding is the editorial gravity and the AR translation holds it.
- **AR register:** fusha-analytic with a slightly slower cadence to match the subject's tempo — institutional, multi-decadal, modest in claim. The piece reads, in AR, in the same key as Madār's other long-arc institutional pieces (Mosul Library; FQSE Sierra Leone).

## Named-human transliterations applied

- Abdul Mu'ti → عبدالمعطي (no honorific; matches Indonesian convention as used in the EN)
- Toni Toharudin → طوني توهارودين
- Pujianto → بُجِيانتو
- Buthaina bint Ali Al Jabr Al Nuaimi → بثينة بنت علي الجبر النعيمي
- Lolwah Al-Khater → لولوة الخاطر
- Stavros Yiannouka → ستافروس يانوكا
- Mohammed bin Abdulrahman → الشيخ محمد بن عبدالرحمن
- Laila Lalami → ليلى العلمي
- Mo Gawdat → مو غودة
- Abhijit Banerjee → أبهيجيت بانرجي
- Anousheh Ansari → أنوشه أنصاري
- Omar Al Shogre → عمر الشغري
- Lady Mariéme Jamme → ليدي مارييم جامي
- Fiorella Haim → فيوريلا حايم
- Yamandú Orsi → يامانْدُو أورسي
- Leandro Folgar → ليانْدْرو فولغار
- Tabaré Vázquez → تاباري فاسكيز
- José Mujica → خوسيه موخيكا
- Luis Lacalle Pou → لويس لاكاييه بو

All renderings cross-checked for internal consistency. The Orsi name is rendered with sukun on the long-vowel cluster to disambiguate vowelisation; same for Folgar.

## Cross-language frontmatter integrity

Each AR file's `englishVersion` field points to the matching EN slug. Each EN file's `arabicVersion` field has been added by the Manager in this session to point to the matching AR slug. The Astro article layout will render the "Read in [the other language]" link on both sides once the build completes.

## Carried-forward style notes (not edited, for future drafts)

- **Indonesia** — the choice to preserve "Permendikdasmen" / "Kurikulum" terms in Latin script is editorially correct for a fusha-analytic piece on Indonesian policy; the next Indonesia piece (if any) should reuse this convention rather than introduce AR neologisms.
- **Qatar** — the rendering of "Humanity.io" as a Latin-script slogan inside an AR sentence is editorially correct; the suffix-`.io` joke does not translate, and the AR sentence makes that visible in its analysis paragraph.
- **Uruguay** — the Spanish-language quotes inside the AR body need an AR translation in italics alongside, not a replacement; the current draft does this correctly.

## Verdict

All three AR pieces approved for publication. `approved: true` is set in each file's frontmatter. The pieces are ready for the Manager's publish-gate pass.

— Arabic Editor
