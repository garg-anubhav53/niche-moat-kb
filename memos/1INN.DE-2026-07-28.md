# 1INN.DE — innoscripta SE
### §5 Deep-Dive + OPUS Adversarial Red-Team | 2026-07-28 | Run #88

**Verdict up front: the §4 thesis does not survive. GRADE C · TIER PARK.**

The §4 memo scored 9/12 and passed the Asymmetry Gate on five load-bearing claims. Four of the five are
factually wrong, and the fifth is not independent evidence:

1. **"Pure SaaS, annual/multi-year contracts (auto-renewal)"** — **FALSE, per the company's own description.**
   innoscripta charges *"ergebnisorientierte Lizenzgebühren, die nur fällig werden, wenn Kunden die
   Forschungszulage erhalten"* — result-oriented licence fees payable **only if the customer actually receives
   the research allowance.** This is a contingency fee on a government subsidy, recognised per successful
   claim. It is not a subscription, it does not renew, and "<2% churn" is not a defined metric for it.
2. **"IPO proceeds ~€218M raised at IPO"** — **FALSE.** The May 2025 IPO was a **100% secondary placement.**
   All €218M went to founders Michael Hohenester and Alexander Meyer personally. **The company received
   nothing.** The §4 balance-sheet inference ("likely net cash") was built on money that never entered the firm.
   Actual net cash is roughly **€26M** (Q3-2025: ~€39M cash vs ~€13M bank debt) — and a company with 61% EBIT
   margins carrying bank debt is itself a question.
3. **"Analyst PT €216.50 = +199% upside"** — **not independent.** Deutsche Börse **Scale rules require the
   issuer to commission and pay for its own research** from a Capital Market Partner and publish it on its own
   website. Warburg's reports are hosted at `innoscripta.com`. Two buy ratings, zero sells, issuer-funded.
   That is a listing obligation, not price discovery.
4. **"+61% growth, EBIT margin expanding to 67.7%"** — **both are period-selection artefacts.** Derived
   quarterly revenue shows growth decelerating from **+93% (H1-2025) to +41.5% (H2-2025)**, and the company's
   own FY2026 guidance implies a **57.1% EBIT margin — 10.6pts *below* the Q1 figure the §4 memo extrapolated.**
5. **"Binary BSFZ regulation risk; base case is regulatory continuity"** — **the risk was framed wrongly.**
   Germany just *expanded* the programme for 2026. The real, live, non-binary risk is **anti-intermediary
   tightening**: the Bundesrechnungshof has criticised the Forschungszulage for *Mitnahmeeffekte*, lack of
   targeting, and consultant-provision structures since 2019, and **the FZulG is now subject to statutory
   evaluation every two years, for the first time as of 01.01.2026.** The UK ran this exact movie 2022-2025.

Two facts the §4 memo never surfaced: the **lock-up expired 24 May 2026**, and the founders have publicly
stated they will only consider selling more **"bei einer substanziellen und nachhaltigen Erholung des
Aktienkurses gegenüber dem IPO-Platzierungspreis von EUR 120."** They have pre-announced that they sell into
strength. That is a declared supply ceiling sitting directly on top of the entire upside case.

---

## 1. OPUS RED-TEAM — 12 CHECKS

### Check 1 — Re-derive every load-bearing number from primary source → **FAIL**

**The Geschäftsbericht 2025 was never read.** `innoscripta.com/DE_innoscripta_GB_2025.pdf` exists and is
indexed, but returned **HTTP 403 to both curl and WebFetch** (proxy egress policy — the same block hit
eqs-news.com, northdata.com, boersengefluester.de, valueandopportunity.com, substack). Every figure below is
web-search-relayed. **C cannot be raised this run.**

Corrections found anyway:

| Figure | §4 memo | Re-derived | Note |
|---|---|---|---|
| FY2025 revenue | €104.4M | **€103.41M** ~ | EQS preliminary 27 Jan 2026 says "at least €103.4M"; €104.4M appears only in aggregators |
| FY2024 revenue | €64.71M | €64.71M ~ (one source €65.3M) ⚠ | unresolved |
| FY2025 EBIT | €63.6M "EBIT" | **€63.6M *adjusted* EBIT** ~ | **2024 and 2025 EBIT are both adjusted for IPO costs**; €527k of IPO cost was pushed onto the principal shareholders in 2025 |
| FY2024 EBIT margin | 58% | 58.7% adj ~ | |
| Net cash | UNAVAILABLE | **~€26M** ~ (Q3-2025: ~€39M cash, ~€13M bank debt) | then **−€40M dividend paid 22 Apr 2026** |
| Shares outstanding | ~10.0M ~ | **~10.0M** ~ (corroborated: €4.00 DPS × 10.0M ≈ €40M ≈ 94% of NI) | still derived, not confirmed |
| IPO proceeds to company | "~€218M raised" | **€0** ✓ | 100% Umplatzierung |
| BSFZ share | "~16% of applications" | company claims **>27%** of its ≥10-employee target group; ~3,200 applications filed in 2025 | §4 number stale |

**Gross margin — the 96-98% figure is not a real number.** No primary gross-profit line was obtainable. The
96%/97.8%/95.8% figures trace to **issuer-paid Warburg research** and CNBC; SimplyWallSt says **70.8%**. German
issuers frequently report under the *Gesamtkostenverfahren* (total-cost method), which has **no cost-of-sales
line at all** — which is the most likely explanation for a 25-point spread between vendors. **Verdict: gross
margin is ⚠ DISCREPANT and cannot be load-bearing. Do not score it.** The §4 memo's "GM GATE CHECK: PASS
(~96%)" rests on sponsored research.

**Net cash: resolved directionally, and it is small.** ~€26M net at Q3-2025, then a €40M dividend out the door
in April 2026, partly refilled by H1-2026 earnings. Call it **€25M ± €20M ~**. It is not a fortress; it is a
working-capital balance in a business that pays out ~100% of what it earns.

### Check 2 — "Too good to be true" is a DATA ALARM → **FAIL (alarm fires)**

At €73.90 (28 Jul 2026, ~11:01 CET) × ~10.0M shares = **~€739M cap**, EV ≈ **€714M**:
**6.9x EV/Sales · 11.2x EV/adj-EBIT (FY2025) · 8.9x EV/EBIT on FY2026 guidance · 17.3x P/E · 5.4% dividend yield.**

A 61%-EBIT-margin, 35-60%-growth business at 8.9x forward EBIT is not an overlooked gem. It is an alarm. Three
independent explanations were found, and all three are real:

- **The IPO failed at €120.** Priced at €120 for a €1.2B valuation, it **broke issue on day one** and has never
  recovered. Only 18.2% of the company was offered. The market declined to pay €120 for 18% of it. The €216.50
  "consensus" asks you to believe the market was wrong by 3x on a name it has now priced continuously for
  14 months.
- **The PT is issuer-funded** (Check 1). Under Scale rules the issuer must commission its own research. A
  +199% "gap to target" produced by a report the company pays for and hosts is not a mispricing signal.
- **A headcount/margin cross-check does not reconcile.** **831 employees at Dec-2025** on €103.41M revenue =
  **€124k revenue per employee** — a labour-intensive services ratio, not a SaaS one (SaaS runs €200-400k).
  Departmentally: 39.5% engineering, **34.8% finance & operations, 25.7% sales & marketing.** A 61% EBIT margin
  implies **total** operating cost of ~€40M. 831 heads (66% Germany) at any plausible loaded cost, plus a
  quarter of the company in sales & marketing, plus offices in Germany/Austria/India/US, does not obviously fit
  inside €40M. This may resolve cleanly in the annual report (mid-year hiring ramp, low-cost India delivery,
  scraper-inflated headcount). **It was not resolvable here. It is ⚠ and it is the single highest-value item on
  the human checklist.**

**The 40% decline from IPO is a signal, not an entry.** ‑47% from the 52-week high, ‑31% over 12 months, and
**‑15.8% in the 30 days to ~9 July 2026** — *after* a Q1 print of +57% revenue and a 67.7% EBIT margin. A stock
that falls on numbers like those is a market rejecting the durability of the numbers, not a market that hasn't
noticed them.

### Check 3 — Strip one-offs → clean operating earnings → **FAIL (a legislated one-off is inside the guidance)**

Reported EBIT is **adjusted** for IPO costs in both 2024 and 2025 — small, disclosed, acceptable.

The material one-off is upstream and the §4 memo missed it entirely. **The FZulG parameters were materially
widened effective 01.01.2026:**

| Parameter | Pre-2026 | From 2026 |
|---|---|---|
| Eligible-expense cap per group/yr | €10M | **€12M** |
| Own-labour (Eigenleistung) flat rate | €70/h | **€100/h (+42.9%)** |
| Overhead flat rate on eligible personnel cost | — | **+20%** |
| Overhead/operating costs eligible | no | yes (projects started after 31.12.2025) |
| Max relief | — | €3.0M (SME 35% → €4.2M) |
| Duration of enhanced terms | — | **~2026-2030 (befristet)** |

innoscripta's fee is a percentage of the grant obtained. **The same client, filing the same projects, with the
same effort, generates a materially larger fee in 2026 purely because the statute changed.** A meaningful slice
of the ≥€140M / +35% guidance is therefore a **legislated price increase, not share gain or volume growth** —
and it is **time-limited to ~2030.** This is precisely the "strip the one-off" failure mode: the guidance is
being scored as operating momentum when part of it is a statutory step-up with a stated expiry.

Secondary: **the 20% overhead flat rate was introduced explicitly because it *"vereinfacht die Antragstellung
erheblich"*** — it substantially simplifies the application. innoscripta's entire pitch is taming the
bureaucracy. The legislature is reducing the bureaucracy.

### Check 4 — Score each item once → **FAIL (double- and triple-counting)**

- **Regulatory dependence** was scored as *Moat clarity = 2* ("BSFZ regulatory process lock-in") **and** listed
  as Risk #1 ("binary regulatory risk"). The same fact cannot be the moat and the kill risk.
- **The €216.50 PT** drove *Valuation gap = 2* **and** Gate criterion #2 (magnitude) **and** Gate criterion #1
  (mispriced now) — one issuer-paid document carrying three separate scores.
- **The 61% EBIT margin** was scored under *Business quality = 2* **and** again under *Floor quality* ("€42M+
  NI annual; cash-generative").
- **Free float 18.2%** was scored as an insider-alignment positive ("founder ownership 81.8%") and separately
  as Risk #2 and Risk #5. In fact it is one thing and it is negative: the founders' 82% is not alignment, it is
  the overhang — they have already converted €218M of it to cash.

Cleaned, the §4 total is nearer **5-6/12**, not 9/12.

### Check 5 — Absence of a catalyst is not a catalyst → **FAIL**

*Catalyst proximity = 1* was granted for "earnings Aug 20, 2026." That is a routine H1 print. The §4 memo
itself conceded "no hard-dated binary event."

The re-rating mechanism is unstated and, on inspection, **absent**: there is no independent analyst to initiate
(Scale research is issuer-commissioned by rule), no index inclusion path at 18.2% float, no strategic review,
no buyback, and no dated regulatory decision in the bull direction. Q1-2026 already printed +57% revenue and a
67.7% EBIT margin — **and the stock fell 15.8% in the following weeks.** The empirical answer to "does a beat
re-rate this stock" was delivered eight weeks ago, and it was **no**.

### Check 6 — Base rate must include the failures → **FAIL (no analog re-rated)**

| Analog | Setup | Outcome |
|---|---|---|
| **UK R&D tax-credit advisory boutiques (2022-2025)** | Contingency-fee intermediaries on a government R&D credit — *the exact model* | **DECIMATED.** HMRC grew R&D compliance headcount ~100 → **>500 (+500%)** since 2020; opens compliance checks on ~**1 in 5 claims (17% of 2023-24)**; created an **R&D Agent Compliance Management team (Dec 2023) with the power to refuse to process claims prepared by a named adviser**; worked with the ASA to strip adviser advertising. **6 in 10 R&D-active firms cut R&D spend** as a result. No listed winner emerged. |
| **CompuGroup Medical (COP.DE)** ~ | German regulatory-mandated healthcare IT; mandate-driven high-margin revenue | De-rated ~85% from the 2021 peak once the mandated cycle normalised. Stayed cheap. |
| **Fabasoft (FAA.DE)** — this KB's own logged failure | German/Austrian government-locked software, coverage void, "initiation will re-rate it" | **Never re-rated.** The coverage void was the equilibrium, not a temporary condition. |
| **EU/China solar subsidy cohort** | Equity value = a slice of a government subsidy | Germany cut EEG 15%, Italy cut FiTs, UK cut large-scale FiT 70%, China's "5.31" (2018) cancelled utility-scale FiTs → **hundreds of billions of RMB of market value destroyed.** |

I could not name **a single** listed contingency-fee intermediary on a government subsidy that re-rated and
held the re-rating. Per METHOD, **that makes R low even if the moat is real, and I am saying so explicitly.**

**Base rate: 0 of 4. The swing factor was never the credit itself — it was the tax authority's posture toward
the intermediaries.** In every case the underlying incentive survived; the intermediaries did not.

### Check 7 — No hard-rule overrides → **FAIL (C stays 2; grade capped at C)**

C could **not** be improved this run. The annual report is 403-blocked; so is every fetch host tried. Nothing
load-bearing has been read from a primary filing. Unresolved after this run: gross-margin definition, personnel
cost, revenue-recognition trigger point, receivables/contract assets, year-end cash and debt, share count,
auditor, related-party dealings, the fee percentage, and the churn definition. **C = 2 → grade capped at C,
regardless of everything else.** Resolvable ≠ resolved.

### Check 8 — Decompose revenue quality → **FAIL (it is not SaaS)**

The company's own description, in German, on its own site: revenue is **"ergebnisorientierte Lizenzgebühren,
die nur fällig werden, wenn Kunden die Forschungszulage erhalten"** — result-oriented licence fees due only
when the customer receives the grant. Corroborated independently: *"the unique revenue model (success fee
instead of software fees)"* was cited as a **reason the IPO flopped.*

Consequences the §4 memo did not draw:

- **Nothing is contracted or recurring.** There is no subscription, no committed ARR, no renewal. Each year's
  revenue is re-won claim by claim and is contingent on a **third party (the BSFZ) issuing a certificate.**
  This is the revenue-quality profile of a contingency-fee advisory firm, not of software.
- **"<2% churn" is undefined here** and cannot be verified. It appears in investor materials, not in anything
  primary. In a per-claim success-fee model the meaningful metric is repeat-filing rate, which is not disclosed.
- **The revenue is lumpy in a way subscriptions are not.** Derived quarterly (from Q1'25 €25.6M, H1'25 €44.1M,
  9M'25 €70.7M, FY'25 €103.41M):

  | | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 |
  |---|---|---|---|---|---|
  | Revenue | €25.6M | **€18.5M** | €26.6M | €32.7M | €40.3M |
  | QoQ | — | **‑27.7%** | +43.8% | +22.9% | +23.2% |

  A ‑28% sequential quarter inside a "recurring SaaS" year. **H1-2025 grew +93% YoY; H2-2025 grew +41.5%.**
  The headline "+61%" is the average of a sharp deceleration.
- **831 employees, €124k revenue/head, 34.8% in finance & operations and 25.7% in sales & marketing.** That is
  the shape of a claim-preparation factory with a software front end and a very large sales motion.

The §4 memo's answer to "is 20-30% one-time/advisory?" is worse than 20-30%: **arguably 100% of it is
transaction-contingent.** The honest reframe is that the 61% margin is not a SaaS margin — it is the take rate
of an intermediary skimming a legislated subsidy, and its level is set by statute as much as by the business.

### Check 9 — Moat durability 3/5/10 years → **FAIL at 5 and 10 years**

- **3yr — MODERATE.** Genuine assets: ~3,200 filings/yr, **>27% share of the ≥10-employee applicant pool**,
  accumulated data on what the BSFZ accepts, brand names (Ferrero, BearingPoint, Jack Wolfskin, Wella, ING),
  and a sales machine competitors lack. The 2026 parameter widening is a tailwind. This holds.
- **5yr — WEAK.** Three converging pressures. (a) **Share runway is far smaller than claimed.** The §4 framing
  — 2,100 clients ÷ 180,000 eligible firms = 1.2% penetrated — is the wrong denominator. Against *actual
  applicants* (**48,863 total BSFZ applications 16.09.2020-31.03.2026**), innoscripta is already at ~25-27%.
  Tripling share means displacing Deloitte/EY/PwC/KPMG plus a crowded Mittelstand adviser field. (b) **The
  legislature is simplifying the process** (20% overhead flat rate, €100/h flat own-labour rate) — every
  simplification shrinks the pain innoscripta is paid to remove. (c) **The enhanced parameters are befristet to
  ~2030.**
- **10yr — MELTING.** The deliverable is a structured natural-language description of an R&D project mapped to
  a statutory definition. That is the single most LLM-native artefact in professional services. **Competitors
  already advertise it** — "Forschungszulage Beratung 2026 – **Jetzt mit KI-Assistent**" is a live listing, and
  the German Förderberatung field (Banhoek, Clever Funding, Steinbeis, PNO, Skill-Sprinters, deutsche-
  fördermittelberatung, and others) is crowded, not empty. DATEV or a Big-4 shipping an LLM-assisted FZulG
  module against a customer base that already holds the payroll and cost-centre data collapses innoscripta's
  data-aggregation advantage and its take rate simultaneously. **Clusterix is a feature with a sales force in
  front of it, not an architecture.** A certification moat protects against a competitor swapping in; it does
  not protect against the workflow being rewritten.

### Check 10 — Hunt the disclosure that flips the thesis → **FOUND**

The thesis-flipping risk is **not** "Germany abolishes the Forschungszulage." Germany just expanded it. The
flip risk is **anti-intermediary tightening**, and the machinery is already in motion:

1. **The FZulG is now statutorily evaluated every two years, for the first time as of 01.01.2026.** The
   evaluation is happening now. The §4 memo does not mention it.
2. **The Bundesrechnungshof has attacked the programme repeatedly since before it existed** — a 2019
   pre-legislative report doubting it could be implemented effectively or efficiently; **two 2021 reports to
   the Bundestag Finance Committee** ("Steuerbefreiung der Forschungszulage in Frage gestellt" / "Mangelnde
   Zielgenauigkeit"); the 2022 subsidy-evaluation report; the 2023 annual-report supplement. Its findings:
   **significant Mitnahmeeffekte (deadweight), the relief "often does not directly reach the companies doing
   the research," and problematic consultant-provision structures channelling benefit to intermediaries rather
   than researchers.** innoscripta, taking a success-fee slice of ~27% of all qualifying claims, is a textbook
   instance of the structure the national audit office named.
3. **The UK precedent shows exactly what the remedy looks like** (Check 6): 5x compliance headcount, 1-in-5
   claims checked, and an **agent-level sanction under which the authority refuses to process claims prepared
   by a named adviser.** Applied in Germany, that is not a haircut — it is a single point of failure for 100%
   of revenue.
4. **§ 9a StBerG prohibits contingency fees in tax matters** for tax advisers, with narrow exceptions.
   innoscripta positions itself as a software licensor, not a Steuerberater. **Whether a success-based licence
   fee for producing the substantive content of a tax-relief application is "Hilfeleistung in Steuersachen"
   under §§ 2/5 StBerG is a live legal question I could not resolve, and I found no case law or enforcement
   action against innoscripta.** Flagged as UNRESOLVED, not as a finding. But it is the correct place to look.
5. **The company itself makes regulatory stability a guidance condition.** The 25 Feb 2026 ad-hoc bases the
   ≥€140M/≥€80M guidance on the order situation, scalability, **and "stabile regulatorische
   Rahmenbedingungen."** Management has told you which variable the guidance is contingent on.

**TAM correction:** the §4 memo's "1.2% penetration of 180,000 eligible companies" overstates runway by an
order of magnitude. Measured against firms that actually file, innoscripta is a ~27%-share incumbent, and 2026
growth is substantially a legislated fee uplift (Check 3) rather than penetration.

### Check 11 — The trigger must test the load-bearing variable → **FAIL**

Load-bearing variable: **the durability of a contingency-fee intermediary's take rate on the German
Forschungszulage.**

The 20 Aug 2026 H1 print reports revenue and EBIT. It **cannot** test that variable — revenue can print big for
a reason that has nothing to do with the thesis (the 2026 statutory parameter widening mechanically inflates
fees per claim) or small for a reason that has nothing to do with it (BSFZ processing timing shifting
certificates across a quarter boundary). **A print that can move either way for reasons unrelated to the
thesis is unfalsifiable. Reject it as the trigger.**

**The informative triggers are the ones nobody scored:** the **FZulG biennial evaluation output (from 2026)**,
any **Bundesrechnungshof or BMF follow-up on intermediary/consultant structures**, any **BSFZ tightening of
evidentiary standards or rejection rates**, and **post-lock-up founder disposals** (director's dealings).

### Check 12 — Is the asymmetry already captured? → **FAIL (there is no asymmetry to capture)**

Live: **€73.90 (28 Jul 2026)** vs the §4 anchor of €72.50 — the stock has not run, so nothing was "paid out."
The asymmetry fails for the opposite reason: **it never existed at the stated magnitude.**

Strip the issuer-paid €216.50 and ask what an independent buyer pays for this cash stream. A founder-controlled
(≈82%), 18.2%-float, ~100%-payout intermediary whose revenue is a contingent slice of a government subsidy
under statutory biennial review, with enhanced terms expiring ~2030 and no contracted recurring revenue,
supports something like **8-12x EBIT**. It trades at **8.9x FY2026E EBIT.** **It is inside its own defensible
range. The Gate's ≥2x magnitude test fails.**

And the upside has a declared ceiling: the founders have stated they will consider selling **only on a
substantial and sustained recovery toward the €120 IPO price.** From 82% ownership, into an 18% float. Any
move toward €120 mechanically summons supply. Meanwhile the lock-up **expired 24 May 2026**, and the stock fell
15.8% in the weeks after.

**The market is not failing to discover this name. It is pricing a policy-duration annuity as a policy-duration
annuity.**

---

## 2. RISK PROFILE

**Load-bearing assumption.** That a success-fee intermediary can hold a ~27% share and an undisclosed take rate
on the German Forschungszulage through a statutory biennial evaluation, standing Bundesrechnungshof criticism
of exactly this structure, an LLM-driven collapse in the cost of producing the deliverable, and a ~2030 sunset
of the enhanced parameters. Everything else — margin, growth, valuation — is downstream of this one sentence.

**Clean operating earnings and what it is actually worth today.** FY2025 clean: **revenue €103.41M, adjusted
EBIT €63.6M (61.1%), net income €42.61M, OCF €40.8M** (cash conversion ~96% of NI — genuinely good, and the one
place the bull case is stronger than I expected). Net cash ~€25M ±. At €73.90 × ~10.0M shares: **cap €739M,
EV ~€714M, 11.2x trailing / 8.9x forward EV/EBIT, 17.3x P/E, 5.4% yield.** Fair value on an independent
8-12x FY2026E EBIT of €80M, plus net cash: **€67-99/share.** **The stock sits mid-range.** To reach the
sponsored €216.50 you must apply ~26x EBIT to contingency-fee revenue on a sunsetting statutory programme —
that is the heroic part, and it is not available.

**Informative trigger (what actually tests the key risk).** *Not* the 20 Aug 2026 print. The real tests:
(i) the **FZulG biennial evaluation** (first due from 01.01.2026) and any BMF/Bundesrechnungshof follow-up on
intermediary structures; (ii) any **BSFZ move on evidentiary standards, rejection rates, or adviser
accreditation** — the UK's agent-sanction template; (iii) **director's dealings** post-24-May-2026;
(iv) disclosure of the **fee percentage and the repeat-filing rate**, which would convert "churn <2%" from
marketing into a metric.

**Moat durability.** 3yr MODERATE (share, data, sales machine, 2026 tailwind) · 5yr WEAK (share runway
overstated, legislature actively simplifying, terms sunset ~2030) · 10yr MELTING (LLM-native deliverable;
AI-assistant competitors already advertising; DATEV/Big-4 module risk).

**Revenue-quality decomposition.** **0% contracted recurring software.** ~100% transaction-contingent success
fees, recognised per successful claim, contingent on a third-party certifier. Growth decomposes into
**volume/share gain (H1'25 +93% → H2'25 +41.5%, decelerating)** plus, from 2026, **a legislated fee uplift**
(cap €10M→€12M, own-labour rate €70→€100/h, +20% overhead allowance) that is a one-time step with a ~2030
expiry. 831 employees at €124k revenue/head, a quarter of them in sales & marketing — a services cost shape
wearing a software label.

**The disclosure that would flip the thesis.** A German equivalent of HMRC's R&D Agent Compliance Management
regime — any BSFZ/BMF measure that restricts, accredits, or sanctions intermediaries, or any evaluation finding
that adopts the Bundesrechnungshof's language on consultant-provision structures. Because the fee is contingent
on certification, an authority that can refuse to process a named adviser's filings can zero the revenue line
without touching the subsidy. Secondary flip: any § 9a StBerG / § 5 StBerG challenge to the success-fee model.
Third: the annual report showing that the 61% margin does not reconcile to personnel cost.

**Return if nothing re-rates.** Honestly, **not bad, and this is the strongest part of the bull case.** FY2026
guidance of €140M/€80M EBIT implies ~€54M net income (≈€5.40 EPS) at the FY2025 conversion rate; at the
demonstrated ~94% payout that is **~€5.05 DPS ≈ 6.8% yield on a €73.90 cost.** So: a mid-to-high single-digit
cash yield with residual growth optionality, for as long as the programme and the take rate hold. **But that is
the profile of a high-yield policy-duration annuity with an unpriced tail — not a compounder.** You are not
being paid to wait for a re-rate; you are being paid a coupon on legislation, and the founders are collecting
~82% of that coupon alongside you.

---

## 3. SCORES

**Q — Business Quality: 2/5.** Real growth, real margins, real cash conversion (OCF €40.8M vs NI €42.61M), no
client concentration (>2,100 clients, none >0.9% ~). **But:** revenue is 100% transaction-contingent on a
government programme with a statutory biennial review and a ~2030 sunset; the moat is a sales machine plus a
document workflow that LLMs commoditise; ~100% of earnings are paid out, so there is no reinvestment runway
despite a claimed 180,000-company TAM; the founders control ~82%, already extracted €218M in a pure secondary,
and have declared they sell into strength. A 61% margin on a legislated take rate is not the same asset as a
61% margin on contracted software.

**F — Downside Floor: 2/5.** Profitable, ~5.4% yield, no meaningful capex. **But:** net cash is only ~€25M
(and there is bank debt), ~100% payout means the balance sheet never builds a buffer, there is no asset floor,
and the earnings floor is entirely policy-contingent — a single adviser-directed measure can take revenue to
near zero, which is precisely what makes the floor unquantifiable rather than merely thin.

**R — Re-Rate Likelihood: 2/5.** No dated catalyst that tests the load-bearing variable. No independent
initiation mechanism (Scale research is issuer-commissioned by rule; 2 buy ratings, both bought). 18.2% float
with a founder who has publicly pre-committed to selling on a recovery toward €120 — a declared supply ceiling.
Q1-2026 beat spectacularly and the stock fell 15.8%. **Base rate: 0 of 4 analogs re-rated.**

**C — Confidence: 2/5 (HARD CAP, unchanged).** No primary filing read — the Geschäftsbericht 2025 PDF returned
403 to every method available, as did every other fetch host. FY2025 revenue conflicts across sources
(€103.41M / €104M / €104.4M); FY2024 conflicts (€64.71M / €65.3M); EBIT is *adjusted*; gross margin ranges
70.8%-97.8% across vendors; share count is derived, not confirmed; the headcount-vs-margin cross-check does not
reconcile; the fee percentage, revenue-recognition trigger, receivables, year-end cash/debt, auditor and
related-party disclosures are all unread. **Per METHOD, C=2 caps the grade at C.**

---

## 4. GRADE AND TIER

```
GRADE: C  ·  TIER: PARK (re-open on trigger)
Q 2/5 · F 2/5 · R 2/5 · C 2/5
```

**Asymmetry Gate: FAIL (2 of 4).**
1. Mispriced now? **NO** — 8.9x FY2026E EBIT sits inside an independent 8-12x range for a contingency-fee,
   policy-duration, 100%-payout, founder-controlled intermediary. The only fair value above it is issuer-paid.
2. ≥2x magnitude? **NO** — once the sponsored €216.50 is stripped, defensible fair value is €67-99.
3. Skew? **NO** — capped upside (founder supply arrives on any move toward €120) against an unquantifiable
   regulatory tail. Not asymmetric; arguably inverted.
4. Trigger? **NO** — the Aug-20 print is unfalsifiable w.r.t. the load-bearing variable, and standalone quality
   is not CORE-grade (Q=2, F=2).

**Why PARK and not WATCH:** WATCH is reserved for names that would be CORE or CATALYST but for low C. This is
neither — Q<4 and F<4 rule out CORE, R<4 rules out CATALYST. Raising C would not change the tier. **Not
QUALITY BENCH either:** the Bench requires Q≥4 and a moat durable over years; this moat is weak at 5 years and
melting at 10.

**Why C and not D:** the business is real, the cash conversion is real, the dividend is real, and the 2026
statutory widening is a genuine near-term tailwind. This is not a value trap dressed as a company. It is a
decent business whose *asymmetry* does not exist at today's price and whose *durability* is unknowable from
outside the filing.

**Buy-zone: none named.** A price alone does not fix this. **Re-open trigger (any one):**
(a) the FZulG biennial evaluation completes with **no** adverse finding on intermediary/consultant structures
**and** the enhanced parameters are extended beyond 2030; (b) the annual report is read and the 61% margin
reconciles to personnel cost, **and** the fee percentage and repeat-filing rate are disclosed; (c) the founders
convert to a genuine lock (multi-year commitment not conditioned on a €120 recovery) or the float rises above
~35% through a marketed secondary at a market-clearing price; (d) genuinely independent (non-issuer-funded)
coverage initiates.
**Downgrade to D/KILL on:** any BSFZ/BMF measure restricting or accrediting intermediaries; any § 9a/§ 5 StBerG
challenge to the success-fee model; disclosure of material post-lock-up founder selling.

```
Financial baseline: rev FY2023 ~€33.5M est → FY2024 €64.71M ~ → FY2025 €103.41M ~ (+59.8%) · GM ⚠ DISCREPANT
  (70.8%-97.8% across vendors; no primary line; likely Gesamtkostenverfahren artefact — NOT load-bearing) ·
  adj EBIT margin 58.7% (FY24) → 61.1% (FY25) ~, FY26 guided 57.1% implied · NI €42.61M ~ · OCF €40.8M ~ ·
  net cash ~€25M ± €20M ~ (Q3-25: ~€39M cash / ~€13M bank debt; less €40M dividend Apr-26) · shares ~10.0M ~
  (derived, unconfirmed) · dividend €4.00 paid 22 Apr 2026 = ~94% payout, 5.4% yield · price €73.90
  (28 Jul 2026) · cap ~€739M · EV ~€714M · EV/S 6.9x · EV/EBIT 11.2x trailing / 8.9x FY26E · P/E 17.3x
  [financials/1INN.DE.md — REQUIRES CORRECTION: revenue, IPO proceeds, revenue model, gross margin]
Financials verified against primary filing: NO — Geschäftsbericht 2025 PDF returned HTTP 403 to curl and
  WebFetch; northdata, eqs-news, boersengefluester, valueandopportunity all 403. All figures web-search-relayed.
Base rate: "Contingency-fee intermediaries on a government R&D subsidy re-rated 0 of 4 identified analogs
  (UK R&D advisory boutiques, CompuGroup, Fabasoft, EU/China solar); the swing factor was never the subsidy —
  it was the tax authority's posture toward the intermediaries."
Skeptic's checklist: 0 CONFIRMED, 3 PLAUSIBLE, 2 UNVERIFIED, 5 RED-FLAG
  RED-FLAG: (2) revenue durability — no contracted recurring revenue; every euro contingent on a third-party
    certificate under a statute evaluated biennially · (4) moat stickiness — LLM-native deliverable, AI-assistant
    competitors already live, legislature actively simplifying the process · (5) programme concentration — ~100%
    of revenue from one German statute (client concentration itself is fine) · (7) accounting quality — annual
    report unread; EBIT is "adjusted"; 831 employees vs a €40M total cost base does not obviously reconcile ·
    (8) ownership & dilution — 100% secondary IPO paid €218M to founders, company got €0; lock-up expired
    24 May 2026; founders publicly pre-committed to selling on a recovery toward €120
  UNVERIFIED: (1) revenue-recognition trigger point · (6) pricing power — fee % undisclosed; the 2026 uplift is
    legislated, not negotiated
  PLAUSIBLE: (3) competitive capture · (9) input/supply dependency · (10) management credibility
Open questions (what would raise C): the fee percentage · the revenue-recognition trigger (certificate vs cash) ·
  receivables and contract assets · year-end 2025 cash and total debt · personnel expense vs the 61% margin ·
  the gross-margin definition · confirmed share count · the auditor and any related-party dealings · the churn
  definition and repeat-filing rate · the FZulG evaluation timetable and terms of reference
Buy-zone / upgrade trigger / downgrade trigger: see §4 above — no buy-zone; PARK pending regulatory clarity
Asymmetry-to-risk in one sentence: You are being offered a ~5-7% cash yield and residual growth at 8.9x forward
  EBIT — which is fair, not cheap — on a contingency-fee slice of a German subsidy that its own national audit
  office has criticised for enriching intermediaries, whose enhanced terms expire ~2030, whose first statutory
  biennial evaluation is underway now, whose deliverable is the most LLM-automatable artefact in professional
  services, and whose 82% owners already took €218M off the table at €120 and have announced they will sell
  more the moment the price recovers — so the upside is capped by declared insider supply while the downside is
  a single administrative measure of the kind the UK already implemented.

HUMAN VERIFICATION CHECKLIST (before any capital):
  1. OPEN THE GESCHÄFTSBERICHT 2025 (innoscripta.com/DE_innoscripta_GB_2025.pdf or the EN equivalent; I was
     egress-blocked on every host) AND RECONCILE THE 61% EBIT MARGIN TO PERSONNEL EXPENSE. 831 employees
     (66% Germany) at Dec-2025 against a total operating cost base of roughly €40M is the single number that
     did not add up in this review. Read the Personalaufwand line, the headcount note, and whether the P&L uses
     Gesamtkostenverfahren (which would also explain the 70.8%-vs-97.8% gross-margin spread). If the margin
     does not reconcile, nothing else in this memo matters. THIS IS THE MOST IMPORTANT UNRESOLVED ITEM.
  2. READ THE REVENUE-RECOGNITION POLICY AND THE FEE STRUCTURE. Confirm in writing that fees are success-based
     and contingent on the customer receiving the Forschungszulage; establish the recognition trigger (BSFZ
     certificate? tax-office assessment? cash?), the fee percentage, and the size of trade receivables and
     contract assets at 31 Dec 2025. This determines whether "recurring SaaS" is defensible at all — I do not
     believe it is, and the §4 memo's entire quality score rests on it.
  3. VERIFY THE OWNERSHIP AND SUPPLY PICTURE. Confirm the IPO was a 100% Umplatzierung with €0 to the company;
     confirm the 24 May 2026 lock-up expiry; pull all director's-dealings notifications since that date; and
     read the 17 Jun 2025 EQS release in full — specifically the statement that a later disposal is considered
     only on "a substantial and sustained recovery of the share price versus the EUR 120 IPO placement price."
     If founders have begun selling, the upside case is over regardless of fundamentals.
  4. ESTABLISH THE FZulG EVALUATION AND THE INTERMEDIARY RISK. The FZulG is evaluated every two years, first as
     of 01.01.2026. Obtain the terms of reference and timetable, read the Bundesrechnungshof reports (2019 draft
     opinion; the two 2021 reports to the Finance Committee on Steuerbefreiung and Zielgenauigkeit; the 2022
     subsidy-evaluation report), and check whether the BSFZ or BMF has consulted on adviser accreditation,
     evidentiary standards, or rejection rates. Benchmark against HMRC's R&D Agent Compliance Management regime,
     which can refuse to process claims prepared by a named adviser — that is the mechanism that would zero this
     revenue line without touching the subsidy.
  5. CONFIRM THE ANALYST COVERAGE IS ISSUER-PAID AND DISCOUNT IT ACCORDINGLY. Deutsche Börse Scale requires the
     issuer to commission its own research from a Capital Market Partner and publish it on its own website;
     Warburg's reports are hosted at innoscripta.com. Verify the number of genuinely independent analysts (I
     found 2 rated / 4 forecasting, all apparently sell-side-sponsored or aggregator-derived). If none are
     independent, the €216.50 "consensus" must be removed from the valuation case entirely — the entire §4
     Asymmetry Gate passed on it.
  6. CONFIRM SHARE COUNT, YEAR-END CASH AND TOTAL DEBT from the balance sheet. Everything here is derived
     (10.0M shares back-solved from the €4.00 dividend and the €1.2B/€120 IPO valuation; net cash from a single
     German-language secondary citation of Q3-2025). A company with 61% EBIT margins carrying ~€13M of bank
     debt while paying out ~100% of earnings deserves an explanation.
```

---

*Sources (all web-search-relayed; **no primary filing accessible** — proxy egress policy returned HTTP 403 on
curl and WebFetch for innoscripta.com, eqs-news.com, northdata.com, publisher.boersengefluester.de,
valueandopportunity.com and substack.com):*

*EQS-News 27 Jan 2026 (preliminary FY2025: revenue ≥€103.4M vs €64.71M, net €42.61M, adj. EBIT margin 58.2%→61.1%,
~3,200 applications filed, >27% share of the ≥10-employee target group) · EQS ad-hoc 25 Feb 2026 (FY2026 guidance
≥€140M revenue / ≥€80M EBIT, expressly premised on "stabile regulatorische Rahmenbedingungen") · Q1 2026 release
(revenue €40.3M, EBIT €27.3M, 67.7% margin) · EQS 22 Apr 2026 (AGM 21 Apr 2026: €4.00 dividend approved, 91.7%
of capital represented, all items >97.6%) · EQS-News 17 Jun 2025 (founders' Hohenester/Meyer Beteiligungs-UGs to
buy up to €12M of stock "zur Unterstützung des Aktienkurses"; later disposal only on "substanzieller und
nachhaltiger Erholung ... gegenüber dem IPO-Platzierungspreis von EUR 120") · MarketScreener lock-up notice
(certain ordinary shares locked to 24 May 2026) · IPO coverage (finanzen.net, onvista, Börsen-Zeitung, 4investors,
boersengefluester "IPO mit Turbowachstum"): 21-23 May 2025, €120/share, €1.2bn valuation, 1.82M shares, **pure
secondary — €218M to the two founders, €0 to the company**, broke issue on day one · innoscripta.com business-model
pages and marktundmittelstand.de / wirtschaftskurier.de / goingpublic.de / deraktionaer.de (COO Schwertlein):
"ergebnisorientierte Lizenzgebühren, die nur fällig werden, wenn Kunden die Forschungszulage erhalten"; ~2,100
clients; competitors named as KPMG/EY/Deloitte/PwC · valueandopportunity.com 02 Feb 2026 (success fee instead of
software fees + decelerating quarterly growth cited as why the IPO flopped) · Q3-2025 interim (9M revenue €70.7M
vs €39.2M, EBIT €40.8M, 57.8% margin; ~€39M cash vs ~€13M bank liabilities) · H1-2025 (€44.1M, +93%) · Q1-2025
(€25.6M, EBIT €16.3M) · Revelio Labs headcount (831 at Dec-2025, +14.7%; 66% Germany; 39.5% engineering / 34.8%
finance & ops / 25.7% sales & marketing) · Deutsche Börse / Heuking / boerse-frankfurt on Scale research
obligations (issuer commissions and pays its own Capital Market Partner from 01 Apr 2022; must publish on its own
website) · Warburg Research reports hosted at innoscripta.com (031125, 040226; PT €210-225) · BSFZ
(bescheinigung-forschungszulage.de): 48,863 applications received 16.09.2020-31.03.2026; guidance version 10/2025
of 29.10.2025 · FZulG (gesetze-im-internet.de) and 2026 reform coverage (clever-funding.de, steinbeis, PNO,
banhoek, vbu-berater, martinmeng.de): cap €10M→€12M, Eigenleistung €70→€100/h, +20% Gemeinkostenpauschale,
overhead/operating costs eligible for projects begun after 31.12.2025, enhanced terms befristet ~2026-2030,
**statutory evaluation every 2 years, first as of 01.01.2026** · Bundesrechnungshof: 2019 report on the FZulG
draft, the 2021 two-part report to the Bundestag Finance Committee (Steuerbefreiung in Frage gestellt / mangelnde
Zielgenauigkeit), the 2022 subsidy-evaluation report and the 2023 annual-report supplement (Mitnahmeeffekte;
relief "often does not directly reach the companies doing the research"; consultant-provision structures) ·
GOV.UK "HMRC's approach to R&D tax reliefs 2023 to 2024", mscrnd.com, bmmagazine.co.uk (compliance headcount
~100→>500 since 2020; ~17% of 2023-24 claims checked; R&D Agent Compliance Management team from Dec 2023 with
power to refuse to process a named agent's claims; ASA action on adviser advertising; 6 in 10 R&D-active firms
cut R&D spend) · § 9a StBerG (gesetze-im-internet.de) · price €73.90 at 28 Jul 2026 ~11:01 CET (LYNX/aggregator;
snapshot.py returned null for 1INN.DE — no Yahoo quote, no SEC CIK).*
