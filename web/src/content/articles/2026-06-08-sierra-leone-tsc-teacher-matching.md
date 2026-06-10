---
title: "The algorithm that decides who teaches in Bo"
dek: "Sierra Leone built an algorithm to send teachers where they're needed most. It placed more of them, more fairly than chance ever did — yet cannot conjure teachers who don't exist."
date: 2026-06-08
country: Sierra Leone
region: Africa
level: K-12
themes: [value of teachers, government-led programs, access]
type: curated
related:
  - 2026-05-25-bo-teacher-chalk
  - 2026-05-31-uruguay-eduia-lab-ceibal
contains_composites: false
arabicVersion: 2026-06-08-sierra-leone-tsc-teacher-matching
sources:
  - title: "EdTech Hub — Getting Teachers Where They're Needed Most: Insights from Sierra Leone's GIS-Supported Preference Matching Algorithm (webinar summary, named speakers, and 2024/25 deployment-cycle figures)"
    url: "https://edtechhub.org/2025/11/20/getting-teachers-where-they-are-needed-most/"
  - title: "EdTech Hub — From Algorithm Outputs to Classroom Impact: A Conversation with Marian Abu, Director of Teacher Management, Teaching Service Commission (4 December 2024)"
    url: "https://edtechhub.org/2024/12/04/strengthening-the-use-of-data-for-decisions-on-teacher-deployment-in-sierra-leone/"
  - title: "EdTech Hub — The Impact of a GIS-supported Preference Matching Algorithm on Teacher Allocation in Sierra Leone (research portfolio: study design, pupil-to-qualified-teacher ratios, 2,341 allocations)"
    url: "https://edtechhub.org/case-study/impact-of-gis-supported-teacher-allocation-sierra-leone/"
  - title: "Frazer, M. M., Adam, T., Godwin, K., Mackintosh, A., & Haßler, B. (2025). Transforming Teacher Deployment: Lessons from a matching algorithm tool [Policy Brief]. EdTech Hub."
    url: "https://doi.org/10.53832/edtechhub.1114"
  - title: "Mackintosh, A., Koutecký, T., Godwin, K., Adam, T., & Frazer, M. (2025). Data-driven teacher deployment in Sierra Leone: Practicalities and quantitative analysis of using a matching algorithm in the 2024/25 deployment cycle [Technical Report]. EdTech Hub."
    url: "https://doi.org/10.53832/edtechhub.1115"
  - title: "Fab Inc. — FabMatch_SLE, the open-source teacher-deployment matching algorithm (public repository)"
    url: "https://github.com/Fab-Inc/FabMatch_SLE"
hero:
  src: "/stills/2026-06-08-sierra-leone-tsc-teacher-matching.svg"
  alt: "An atmospheric composition for Issue 02 — Sierra Leone. A continuous calligraphic line sketches a scatter of school-marks across an open ground; ink lines reach between them, and a single kiln-orange line completes the one match that lands."
  caption: "سكون · The Still · Issue 02 · Sierra Leone"
approved: true
---

We began with a teacher in Bo who rations a tin of chalk across an eleven-week term. The question we left unasked in that first piece was the one a ministry has to answer every recruitment cycle: who decided she would be standing in *that* classroom, in the second city, and not in a better-resourced school nearer the capital? For most of Sierra Leone's recent history the honest answer was *nobody in particular* — and that, it turns out, was the problem worth fixing.

Sierra Leone has one of the highest pupil-to-qualified-teacher ratios in West Africa. The figure is not evenly bad; it is unevenly bad, which is worse. In urban centres the ratio runs around 44 children to one qualified teacher. In rural areas it rises to 76 to one. The schools that most need a trained teacher are, with grim reliability, the schools that teachers least want to be posted to — far from a market, far from family, far from the things that make a low salary survivable. No amount of recruiting fixes a distribution problem if the new teachers simply pool where teachers already are. What changed is that the Commission stopped leaving that distribution to chance — and the first full recruitment cycle to run on its fix, in 2024/25, has now reported what the decision bought, which is why it is worth reading the machine closely rather than taking the headline on faith.

How the Teaching Service Commission used to place them is described, without flinching, by the person who ran the process. "In 2019, we recruited 2,000 teachers and assigned them to schools randomly," Marian Abu, the TSC's Director of Teacher Management, told EdTech Hub in a conversation published in December 2024. "This led to a lot of backlash from parliamentarians and the general public, as we could not justify our decision." In 2020 the Commission asked the World Bank to help it build a recruitment portal to take the randomness out; it added 5,000 teachers that way. "While the portal improved the process," Abu said, "it did not fully address all deployment challenges. That is when we introduced the algorithm."

The algorithm is the piece. It belongs to a family of matching systems descended from the Nobel-recognised work on stable assignment — the same deferred-acceptance logic used to place medical residents into hospitals and health workers into clinics in countries from the United States to Ethiopia. Built with the technical partner Fab Inc. and released as open source, it does something a portal cannot. It first ranks schools by need — pupil-to-payroll-teacher ratio, remoteness, learning indicators — so the hungriest schools are served first. It then reads two sets of preferences at once: schools list the attributes they want (experience, willingness to stay), and teachers, through the Teacher Management Information System, name the schools they would prefer. When more than one teacher fits the same post, the rules break the tie in favour of female teachers, then higher qualifications, then longer service — a deliberate correction in a country with one of the lowest shares of women in secondary teaching in the region. Abu gives the kind of example a spreadsheet never shows you: "we have a lot of chemistry teachers in the district headquarters, but not in Falaba district or Bonthe district." The machine is for getting the chemistry teacher to Falaba.

What the first full cycle produced, in 2024/25, is on the record and worth stating precisely. The Commission recruited 2,341 teachers; all of those selected had passed its licensing examination. Sixty-four percent were deployed to schools with a pupil-to-payroll-teacher ratio above 100 — the genuinely overwhelmed ones. Fifty-seven percent went to districts the ministry classifies as disadvantaged. And for the first time, every teacher added to the payroll could state a preferred school: 54 percent were matched to it, and only 7 percent ended up more than five kilometres from the option they had named. The Chairman of the TSC, Lans Keifala, no longer signs every teacher's registration form by hand; staff no longer travel the country to verify what district officers submit on paper. The placement can now be defended in public, line by line, which is the quiet thing that ends the parliamentary backlash Abu described.

Now the inconvenient half, which sits in the same paragraph because that is where it belongs. The algorithm can only place teachers who pass the licensing exam, and too few do — distance-education trainees fail at the highest rates — so the pool the system draws from is smaller than the need it is meant to meet. A subtler failure is Abu's own, and she names it: a newly approved school that has not yet been issued a school identification number is invisible to the algorithm, which will not deploy anyone to a school it cannot see, even as teachers from that school are picked up and sent elsewhere. "These newly approved schools have been left worse off than they were before we introduced the algorithm," she said; about 14 percent of teachers deployed in the cycle were touched by the problem. The TMIS does not yet talk cleanly to the Annual School Census; the Commission is thin on the digital capacity the new system demands; and teachers, at first, were told too little about how the matching worked, which cost the process trust it had to earn back. None of this unmakes the gains. It is simply the cost of a real system rather than a press release about one.

Abu is careful about the word *success*, and the care is instructive. The proof of a deployment algorithm is not where teachers land in September; it is whether they are still there when the Annual School Census counts them the following year. Retention is the test, and the test had not yet been marked when she spoke. A publication that wanted the triumphant version would skip that sentence. We are keeping it, because it is the most honest thing said in the entire record.

The wider lens comes from someone who has watched this problem for two decades on another continent. Gregory Elacqua, principal economist at the Inter-American Development Bank, set the Sierra Leone case beside the centralised teacher-assignment reforms of Ecuador, Peru, Chile and Brazil. His sharpest observation is about preference itself: Sierra Leonean teachers may name only one school, while Ecuadorian and Peruvian teachers can rank ten or more, and the deferred-acceptance logic produces fairer matches the more schools a teacher is allowed to rank. Asked for one choice, people game it — they name the school they think they can get, not the one they want. Latin America has begun layering machine learning on top: Ecuador sends alerts when a teacher's preferred school is oversubscribed, nudging a second choice before the match is locked; Brazil runs recommendation engines that advertise hard-to-staff schools the way a platform advertises anything else. It is the same lineage we traced in Uruguay's Ceibal lab — a public system treating allocation as a design problem rather than an act of fate.

Which returns us to Bo. The teacher there was, in an earlier era, placed by no one in particular. She is now placed by a system that can say, in public and with a figure attached, why she is where she is — and that, asked to be honest, will also tell you it could not reach the school down the road that still has no number, and cannot yet promise she will stay. Both of those are true. A country with too few teachers built the machine anyway, because a defensible placement is better than a random one, and because the inconvenient parts are the parts you can actually fix next.

— *The Editors*
