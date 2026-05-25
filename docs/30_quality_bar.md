# Editorial Quality Bar

Standards that apply to every piece, regardless of format.

## Universal requirements

Every published piece must:

1. **Name a specific place** — country at minimum, ideally a city/district/school.
2. **Name a specific time** — a year, a school term, a date, a "since 2022" — not vague present tense.
3. **Cite at least one primary source** — a ministry document, a named educator quoted from a named publication, peer-reviewed research, a local newspaper. Wikipedia is a starting point, never a source.
4. **Have a human in it** — a named person whose presence in the story is not decorative. Anonymized students/teachers are acceptable when there's a clear reason for anonymity (which is then stated).
5. **Have a clear editorial frame** — the piece must answer the question "why is the editor showing me this *now*?" in its first 100 words.
6. **Pass the dignity check** — no romanticization of poverty, no white-savior framing, no implication that local educators need rescue. When in doubt, ask: would the people described recognize themselves in this piece?

## Format-specific bars

### Curated link with commentary (daily, ≤300 words)
- The link is to a primary source or to serious local journalism, not to an aggregator
- The commentary adds *interpretation*, not summary
- It states explicitly what the curator finds notable and why

### Original short piece (occasional, 500–1,200 words)
- One clear thesis stated by the second paragraph
- Two or more named sources or institutions
- A specific recommendation or open question by the end

### Original long-form essay (weekly, 1,500–2,500 words)
- A thesis the reader could not have arrived at by skimming a press release
- Three or more named sources, at least one of which is local to the geography
- A structural arc — not a list of points
- An ending that is earned, not a summary

## What gets rejected

- Anything where the only sources are international institutions describing local realities
- Anything that uses "developing countries" or "the Global South" as the unit of analysis
- Headlines that pose a question the piece doesn't answer
- Pieces whose interest is largely in a famous person's name
- "Listicles" (5 things, 7 ways, etc.)
- Any piece on an out-of-scope country (see [`10_geo_scope.md`](./10_geo_scope.md))
- Any piece on higher education

## Named individuals and composite figures

Most pieces will name real people — teachers, ministers, researchers, students — whose existence and circumstances the Editor has personally verified through interviews, named publications, or primary documents. That is the default and the preferred mode.

The publication also permits **composite figures**: invented stand-ins assembled from interviews with multiple people, published reporting, and the Editor's regional knowledge. Composites are an editorial tool, not a shortcut. They are appropriate when the underlying reality is well-sourced but no single individual can be named (anonymity requests, second-hand interviews, syntheses of repeated patterns across many conversations). They are **not** appropriate as a substitute for reporting the Editor has not done.

### The disclosure rule

Composite figures are permitted **only with explicit disclosure** that is visible to a reader who lands on a single article without context.

**Mechanism (publication-wide standard):** a dagger (†) is appended to the composite name on its **first use in the piece**, and a short footnote appears at the foot of the article, above the sources block, reading exactly:

> *† Names marked with a dagger are fictional composites. Biographical scaffolding — region, school type, salary band, professional background — is drawn from interviews and published reporting cited above. Claims about specific government programs, official salary figures, and statistical facts are sourced independently and apply to real institutions, not to the composite individual.*

Why this mechanism and not the alternatives: an italic editor's note at the head of the piece protects the reader but visually frames the whole article as fiction-adjacent, which is wrong — most of what's in such a piece is sourced fact. An inline bracketed tag ("Hawa [composite]") works but breaks the prose rhythm on every first mention and reads as defensive. The dagger is the lightest visible mark that still does the disclosure work; it is a centuries-old typographic convention for "see footnote"; and it keeps the disclosure precise (composite *name*, not composite *piece*).

### What can vary in a composite, what cannot

May be composited:
- The individual's name, exact age, exact school, exact district
- Personal scene detail (the milk-tin holding chalk, the Saturday tutoring) so long as the type of detail is corroborated across multiple real interviews
- Direct-quoted phrases, **only if** they are phrases the Editor has heard repeatedly across sources in the same language register, and only if the footnote makes the composite nature unambiguous

May **not** be composited — these must be independently sourced even when the human in the piece is composite:
- Specific government programs, policies, dates, ministerial actions
- Salary figures, fee figures, enrolment figures, any statistic
- Claims about specific named institutions (a real school, a real ministry, a real union)
- Quoted statements attributed to real, named third parties

### Bilingual pieces

When a piece runs in both English and Arabic (or carries a substantial Arabic passage, e.g. a bilingual close — see [`40_voice_and_style.md`](./40_voice_and_style.md)), the dagger and its footnote must appear in **both languages**. The Arabic footnote uses the dagger symbol identically (†), with the disclosure rendered in Arabic prose of equivalent register. The disclosure is not a translation exercise: it is a parallel statement, and it is the Editor's responsibility to write it directly in Arabic, not to machine-translate the English.

### Frontmatter flag

Any piece containing one or more composite figures carries `contains_composites: true` in its frontmatter, and lists the composited first names under `composites: [name1, name2]`. This is for editorial tracking, not for reader display.

## Fact-checking protocol

Before publication, the Editor verifies:

- Every named person exists and holds the role attributed to them (as of the writing date)
- Every cited number can be traced to a primary source via a working URL
- Every quoted statement is sourced to a publication, not paraphrased into a quote
- Every place name and spelling matches the local convention (Arabic transliteration in particular)

If any fact cannot be verified, the claim is either removed or hedged explicitly ("according to [source], though we could not independently verify…").
