# Recon — Estonia: AI Leap / TI-Hüpe, the national AI-in-schools deployment
**Date:** 2026-07-06 · **Researcher → Editor** · **Status: PROCEED**

## 1. The instrument
- **Name:** AI Leap / TI-Hüpe — national education-innovation programme; run by the **AI Leap Foundation (SA TI-Hüpe)**, initiated by President Alar Karis with the Ministry of Education and Research (HTM); public-private co-funding (HTM matches private lead partners: Telia, Targa Tuleviku Fond, Skaala).
- **Date:** Announced Feb 2025; teacher phase from Aug/Sept 2025; student app from Jan 2026.
- **Links:** HTM announcement: https://www.hm.ee/en/news/estonia-announces-groundbreaking-national-initiative-ai-leap-programme-bring-ai-tools-all · Programme site (primary documentation): https://tihupe.ee/en/ · First-year report, 9 Jun 2026: https://tihupe.ee/en/3385/
- What deployed: paid **ChatGPT (OpenAI) or Gemini (Google)** for upper-secondary teachers + **ITI**, a tutor-style learning app for grades 10-11 co-developed with Estonian researchers and OpenAI that withholds direct answers; PLC-based teacher training; both vendors signed data agreements (no LLM training on student data, agreed data centres — The Innovator interview with HTM's Riin Saadjärv, 10 Oct 2025).

## 2. Figures
- **Wave-1 target, Feb 2025: 20,000 students (grades 10-11) + 3,000 teachers from 1 Sept 2025** — ANNOUNCED — HTM (link above).
- **Year 1 actual: 154 of 156 upper-secondary schools participated; ~5,000 teachers; 20,000 students (grades 10-11)** — MEASURED — AI Leap first-year report, 9 Jun 2026: https://tihupe.ee/en/3385/
- **Student app slipped Sept 2025 → January 2026** because minors' data-protection rules weren't ready (amendment to the Basic Schools and Upper Secondary Schools Act required) — MEASURED (timeline fact) — ERR, 28 Aug 2025: https://news.err.ee/1609780941/students-may-not-be-interested-in-using-ai-developed-with-state-participation + first-year report ("in January, students were given access to ITI").
- **End-of-year teacher survey: 94% of participating teachers used AI in their work; 63% redesigned teaching; two-thirds set tasks where AI is permitted/required; self-reported saving ~2 hrs/week** — MEASURED (survey, self-report) — first-year report.
- **ITI usage: >12,000 students used the app by year end; ~4,000 weekly active; ~10,000 learning sessions/week** — MEASURED (app telemetry) — first-year report. (Interim: ~7,700 activated / 47% weekly as of Mar 2026 — EU Digital Skills & Jobs good-practice note: https://digital-skills-jobs.europa.eu/en/impact-shapers/good-practices/ai-leap-estonia)
- **PLCs or equivalent teacher-collaboration structures operating in ~two-thirds of schools** — MEASURED (programme report).
- **Impact study: University of Tartu + Stanford + OpenAI; ~100 schools, >9,000 students; surveys Mar & May 2026; analysis begins summer 2026** — ANNOUNCED design; **no learning-outcome results exist yet as of 2026-07** — first-year report (study lead Jaan Aru, UT).
- **2026/27: extension to the whole upper-secondary level; earlier plan of +38,000 students +2,000 teachers via vocational schools now "under preparation/consideration" at HTM** — ANNOUNCED — tihupe.ee front page + Kallas in first-year report.
- Pre-programme baseline: **64-90% of Estonian students already used AI tools** — MEASURED (UT research cited by programme): https://tihupe.ee/en/

## 3. Voice (qualifies — 2025 named school-level operator)
- **Emma Loore Sinitamm, educational-technology lead, Mustamäe Riigigümnaasium (Tallinn public high school, 1,100 students)**: "They are using it anyway, we can't block them, so we might as well teach them how to use it wisely." And, operationally sceptical: "ChatGPT Edu is not as good as regular ChatGPT for some functions… We will see if the students actually use [it]. Most of them want to use the programs they already use." — The Innovator (Jennifer L. Schenker), 10 Oct 2025: https://theinnovator.news/estonias-ai-leap/
- Support voices: **Riin Saadjärv, HTM head of education technology** (same piece): "The model is designed in a way that doesn't give an answer… At first the students didn't like it at all"; and "easier to move a graveyard than to change a single thing in the school system." **Ivo Visak, CEO, AI Leap Foundation** (ERR, 28 Aug 2025): "If you have a device in your pocket that answers everything, and now we're suddenly offering a model that asks you annoying questions instead, why would anyone use it?"
- Student texture (named 10th-graders, Gustav Adolf High School) — ERR, 18 Jan 2026: https://news.err.ee/1609914094/students-on-ai-use-at-school-best-aspect-is-how-it-saves-time

## 4. Status as of 2026-07
- Year 1 closed with the 9 Jun 2026 report + presidential roundtable (Kadriorg). Expansion to all upper-secondary grades confirmed for Sept 2026; vocational/basic-school extension still a ministry decision, not a commitment — a quiet softening of the Feb 2025 roadmap.
- Honest tensions on record: student adoption of the deliberately "annoying" tutor app is the programme's own stated top question (Visak); ~4,000 weekly actives against 20,000 enrolled is the real number to watch; UT/Stanford outcome data not yet analysed; Institute of the Estonian Language published its Estonian-language model benchmark early June 2026 (development steering).
- Legal basis for minors' data fixed via amendment process flagged Aug 2025; no opt-out controversy found — participation is school-level voluntary (154/156 joined) and classroom use is explicitly discretionary ("how often and in which ways… up to students and teachers").

## 5. Proposed angle
Estonia is the rare case where the state answered "students already use AI" not with a ban and not with raw ChatGPT, but with a purpose-built pedagogical constraint: ITI, an app engineered to refuse the direct answer. The deployment mechanics are the story — teachers first (paid ChatGPT/Gemini from August 2025, trained through in-school professional learning communities, nine regional coordinators), students only five months later, because the data-protection law for minors had to be amended before a state app could touch them. Year 1 produced deployment-grade numbers, honestly labelled: 154 of 156 gymnasiums in, 94% of teachers using AI, 63% redesigning teaching — but only ~4,000 of 20,000 students using the tutor app weekly, and the programme's own CEO conceding that an app that "asks you annoying questions" must out-compete the answer machine already in every pocket. Learning outcomes are deliberately unclaimed until the Tartu-Stanford study reports. Contrast with Morocco (certify practice, then scale) and India (scale first, litigate consent later): Estonia sequenced law → teachers → students, and published its own weak numbers. That is the deployment discipline worth writing about.

## 6. Risks / guardrail notes
- Do NOT say "ChatGPT in every classroom": teachers get ChatGPT/Gemini; students get ITI. Feb 2025 coverage (ChatGPT Edu for students) was superseded — the piece must reflect the shipped architecture.
- 94%/63%/2-hrs are self-reported survey figures from the programme's own survey — label as such; ITI telemetry (12,000 / 4,000 / 10,000 sessions) is programme-reported, not independently audited.
- No measured learning outcomes yet — any "it works" framing is premature by the programme's own design; results summer 2026+.
- Wave-1 teacher figure moved (3,000 announced → 4,700 supported → ~5,000 reported); use ANNOUNCED vs MEASURED labels, don't average.
- OpenAI/Google are funders-adjacent partners; never cite OpenAI's blog as spine (openai.com page exists — colour only).
- tihupe.ee is the operator's own site: primary for programme facts, promotional in tone — pair with ERR for friction (delays, student reluctance).

## Verdict sought from Editor
PROCEED — figures on HTM/programme-report primaries with honest MEASURED/ANNOUNCED separation; 2025 named school-level operator (Sinitamm, Mustamäe Riigigümnaasium) with usable critical quotes. Strong contrast piece if Morocco takes the slot; strong standalone if Editor wants the non-MENA option.
