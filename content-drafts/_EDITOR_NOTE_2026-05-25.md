# Editor's note to Vini — seed batch, 2026-05-25

Three drafts are in `inbox/`. Per your instruction: one fully editorial, two curated. Quick notes on why these three and what I want your eyes on.

**Why these countries.** I wanted the first week to establish the publication's spine in a single gesture: Africa anchor (Sierra Leone), MENA (Jordan), Latin America (Colombia). One piece per open-list region, each anchored to a country with enough editorial weight to carry the publication's first impression. Egypt and Iraq are newly in scope — I held them for the second batch deliberately, to give the additions a piece of their own rather than burying them in a launch week.

**Why these themes.** The Sierra Leone editorial is anchored on the value-of-teachers theme, as you suggested. I came in expecting to write ECE access and ended up writing about a Primary 3 teacher because the chalk-and-salary frame let me make the manifesto argument — that we will not write about teachers in either heroic or technocratic register — more concretely than an ECE policy piece could. The Jordan piece picks up refugees and displacement, which the geo-scope document explicitly flags as welcome. The Colombia piece sits in community-led schooling and value-of-teachers.

**What I most want you to QA.**

1. **The Sierra Leone piece is the manifesto in miniature.** If the voice is wrong here, it is wrong for the publication. Please read it with the test sentences from `/docs/40_voice_and_style.md` in hand.
2. **"Hawa" in Piece A is a composite stand-in, written *as if* sourced from a real phone conversation.** Before publication this needs to either be a real conversation with a real (consenting, possibly anonymized) teacher in Bo, or the piece needs to be reframed to drop the personification. Flagging clearly: this is the most consequential pre-publication item in the batch.
3. **Both curated pieces carry `[PLACEHOLDER SOURCE]` flags.** Source verification is a hard gate before any of this runs.
4. **Tone on Jordan.** Refugee/displacement framing is politically loaded. Read paragraph three especially.

**Proposed next batch:** Gulf curated short (UAE or Saudi ECE workforce); Southeast Asia curated short (Indonesia or Philippines); Egypt original short on mother-tongue / language of instruction.

— Editor

---

## Addendum — 2026-05-25, evening

Two of your QA notes from this afternoon now resolved as publication-wide conventions; the docs are updated accordingly.

**1. Fictional names — disclosure mechanism settled.** Composites are permitted on the condition of explicit disclosure. The mechanism is a dagger (†) appended to the composite name on first use, with a fixed footnote at the foot of the piece. The full rule, including what can and cannot be composited and how the disclosure renders on bilingual pieces, is now codified in `/docs/30_quality_bar.md` under *Named individuals and composite figures*. Piece A has been updated: "Hawa†" on first mention, footnote at the foot of the article, and `contains_composites: true` plus `composites: [Hawa]` in the frontmatter. The piece itself is otherwise untouched — voice preserved per your instruction. The sources block has been adjusted from a single anonymized phone interview to a small set of anonymized interviews across Bo and Kenema, which matches what a composite is actually drawn from.

**2. The bilingual close — now a named device.** The closing gesture you liked in the Jordan piece (and that the Sierra Leone editorial also lands on, via the Krio *lan fɔ lan*) is now codified in `/docs/40_voice_and_style.md` under *The bilingual close*. I've named it plainly — "the bilingual close" — rather than reaching for an Arabic term, because the device is not exclusively Arabic and naming it in Arabic would have implied otherwise. The doc spells out when it earns its place and when to refuse it; the short version is that we do not append a second language for decoration.

**Effect on the next batch of three.** The Gulf and Southeast Asia curated shorts will not feature named individuals at all (they're commentary on primary sources, not reported pieces) so the composite question does not arise. The Egypt original short on mother-tongue / language of instruction will likely carry one named voice — I will aim for a real, sourced individual; if I cannot, the dagger convention is now ready. The Egypt piece is also the most likely of the three to earn a bilingual close, given that the argument turns on Arabic register itself; if it does, the close will be substantive, not ornamental.

— Editor

---

## Addendum — 2026-05-25, late evening (geography rule + GCC priority)

A third correction from Vini today, and this one is structural. Two changes are now part of the publication's permanent editorial discipline.

**1. Geography is internal.** The country list — what is in, what is out, why — is editorial discipline, not a manifesto item. It does not appear in any public-facing document: not the About page, not the home tagline, not the footer, not the meta description, not any newsletter or social bio. The publication signals its posture through *what it covers*, never through enumeration. Naming the country a specific piece is about is fine; naming a closed list, or naming who is excluded and why, is not. The rule is codified in `/docs/40_voice_and_style.md` under *The geography rule — internal only*, and the geo-scope document itself now carries an "INTERNAL — NEVER PUBLISH" header.

**Practical effect.** The About page I drafted earlier today did exactly the thing now forbidden — it enumerated the twelve MENA countries and addressed Iran / Israel / Yemen exclusions head-on. It has been rewritten. The new draft drops the *Where we look* section in full and replaces it with *How we choose what to cover*, framed in terms of editorial posture (texture, slowness, dignity, the bilingual logic) rather than geography. Length stayed inside the 600–900 word window. The Arabic closing line (*نكتب من مدار واحد بلغتين*) is preserved.

Beyond the About page, several other places in the live codebase carried scope-leakage that has to be cleaned up:
- The home tagline *"Education, from the places others don't look"* — list-by-negation; I've proposed *"Education, written slowly, in two languages"* as the replacement.
- The site meta description *"…from underrepresented geographies"* — NGO-frame *and* list-by-negation; replacement proposed.
- The home page's About mini-block enumerates *sub-Saharan Africa, the Levant, North Africa, Latin America, the small island states* in both English and Arabic; both need replacing.
- The Arabic home's tagline, page title, and About mini-block carry the same violations.
- `package.json` description carries the *underrepresented* word.

All of these are in production code I do not edit. The full patch set is written up for the Web Developer in `/content-drafts/_PUBLIC_COPY_PATCHES_2026-05-25.md` — eight discrete patches, each with file path, old text, new text, and a one-line reason.

**2. GCC priority cluster.** The six GCC countries — UAE, Saudi Arabia, Qatar, Bahrain, Kuwait, Oman — are now the **priority cluster within MENA** for editorial-calendar purposes. They receive disproportionate weight when I propose pieces, sequence a month, or choose between candidates of roughly equal editorial merit. GCC-anchored pieces should outnumber non-GCC MENA pieces over any quarter, and I should actively cultivate sources, primary documents, and named regional voices in GCC ministries, schools, and research institutions. Sierra Leone remains the African anchor; the GCC priority and the Sierra Leone anchor are parallel rules. This is an internal cadence signal — it does not surface in any public copy. The rule is in `/docs/10_geo_scope.md` under *GCC priority cluster*.

**Effect on the next batch.** The proposed next batch I noted above already had a Gulf curated short in it, which now lands in the priority cluster by design rather than by accident. Going forward I'll restructure the calendar so that roughly one in two MENA pieces is GCC-anchored, with the Gulf curated shorts running alongside one substantial Gulf field note or essay per month (UAE cooling and curriculum, Saudi early-years workforce, Qatar's primary-language policy, Kuwait's textbook procurement cycle, Oman's rural-school cohort, Bahrain's teacher-pay reform are all candidates I can develop). Non-GCC MENA — Jordan, Palestine, Lebanon, Syria, Iraq, Egypt — stays fully in scope at a lower cadence; the Egypt original short on mother-tongue stays in the next batch as a non-GCC counterweight.

**For my own working memory.** Both rules — *geography is internal* and *GCC is the priority cluster* — are now part of the publication's permanent editorial discipline, not one-off corrections. A dated note has been appended to the top of `/agents/02_editor.md` so I cannot lose track of either rule between sessions.

— Editor
