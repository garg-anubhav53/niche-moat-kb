# NTECH.ST — Nordtech Group AB — §5 Opus Adversarial Red-Team
Date: 2026-07-27 | Analyst: Automated | Grade: **PARK** (downgraded from provisional QUEUED_HOT 10/12)

---

## §5 VERDICT: PARK

**Final Grade: D** · Q 2/5 · F 2/5 · R 2/5 · C 2/5  
**Asymmetry Gate: FAIL** — all 4 conditions unmet  
**Do not buy at current price (~SEK 60–61).** Genuine asymmetry requires SEK 42–50 (18–31% below market) AND acquisition-multiple verification AND two consecutive quarters of ≥27% adj. EBITA with subsidiary disclosure.

---

## 0. THRESHOLD FINDING — PORTFOLIO DESCRIPTION WAS WRONG

The §4 provisional memo attributed to Nordtech four verticals: Opus Dental / Opus Prodentus, Medhelp Care, Adtollo, Docunova. **The Opus red-team could not corroborate a single one.**

- **Opus Systemer AS (Opus Dental)** is 100%-owned by Planmeca Oy (Finnish dental equipment conglomerate) — Planmeca acquired it in 2000 and bought out the founders in September 2016. As of the 2026 Kick Off material, Opus Systemer is described as "strategically important to the **Planmeca group**." There is no linking evidence between Nordtech and Opus Dental in any source.
- **"Opus Prodentus"** returns no trace in any Opus or Planmeca filing — the name is unverifiable and may be fabricated.
- **Nordtech's disclosed portfolio structure**: 19 group companies across three segments — Business Platforms, Operational Solutions, Public Infrastructure. Identified subsidiaries include: InfoMentor (education), Thea Commerce, InformaIT, Benchmarking Alliance, Reqtest, FinMeas, BM System, Leaseright. **No dental asset and no healthcare vertical identified.**

**Implication:** The financial metrics in the §4 baseline (SEK 639M LTM revenue, SEK 182M adj. EBITA, 87% recurring, 23 acquisitions) are confirmed against primary sources (IPO prospectus, Q2 2026 interim). But the entire moat thesis built on dental software switching costs is analysis of a company Nordtech does not own. Every ✓ on moat-related claims in the §4 memo was unwarranted.

---

## 1. CORRECTED FINANCIAL FACTS

| Item | §4 Memo Value | Corrected Value | Source |
|------|--------------|-----------------|--------|
| Shares outstanding | ~50.8M (estimated) | 52,045,972 (fully diluted: 50,086,986 ord + 1,858,612 C1 + 100,374 C2) | IPO prospectus |
| IPO price | N/A stated | SEK 60.00 | MFN prospectus release |
| Current price | ~SEK 58.15 | ~SEK 60.40 (+0.7% in 47 days) | July 2026 |
| Price ATH | N/A | SEK 65.00 (day-1 Jun 10, 2026) | MFN |
| Price ATL | N/A | SEK 56.10 (Jun 26, 2026 — −6.5% below offer) | MFN |
| Cash conversion | 104% ✓ | 91% (Q2 2026); 95% (R12) — declining | Q2 2026 interim |
| Adj. EBITA margin H1 | 29% ✓ | 28% (H1 2026); 29% is LTM-March figure | Q2 2026 interim |
| Gross margin | UNAVAILABLE ⚠ | **52.9% — DISCLOSED** | Q2 2026 interim |
| H1 EBIT (reported) | UNAVAILABLE | SEK −0.8M (after SEK 30.2M IPO costs; adj. EBITA 106.9 − IPO 30.2 ≈ EBIT −0.8) | Q2 2026 earnings |
| EV/EBIT (current) | ~16.7x on adj. EBITA | **~55x on EBIT** | Computed |
| Analyst count | 2 (DNB Carnegie + Nordea) ~ | 2 — BUT BOTH ARE IPO UNDERWRITERS (DNB ran stabilization) | MarketScreener |
| Net debt (absolute) | ~SEK 89M (est.) | UNDISCLOSED — only 0.4x ratio given; includes earn-outs + IFRS 16 | Prospectus note |
| EV/adj. EBITA | ~16.7x | ~17.7x (fully diluted, current price, est. ND) | Computed |

**PPA amortization bridge (inferred):** H1 adj. EBITA SEK 106.9M − IPO costs SEK 30.2M → unadjusted EBITA ~SEK 76.7M → EBIT SEK −0.8M → implied PPA amortization ~SEK 77.5M H1 = **~SEK 155M annualized** (~72% of adj. EBITA). This is the recurring cost of the serial-acquisition model, not a one-off.

---

## 2. TWELVE FAILURE MODE VERDICTS

**FM1 — Arithmetic:** LIKELY FALSE (as an error claim). Math holds within tolerance. Real defects: stale price (58.15 vs 60.40), ordinary-only share count, trailing March EBITA, net debt from ratio not absolute.

**FM2 — Too Good to Be True: CONFIRMED_RISK.** Three ✓ claims are wrong: cash conversion 104% (actually 91/95% and declining), margin 29% current (actually 28% H1), gross margin "unavailable" (actually disclosed at 52.9%). A 52.9% gross margin is materially below SaaS-grade (75–85%), implying heavy services/implementation/hosting in COGS.

**FM3 — Strip One-Time Items: CONFIRMED_RISK.** PPA amortization ~SEK 155M annualized is 72% of adj. EBITA and is NOT a one-off — it is the treadmill cost of the acquisition model. EV/EBIT is ~55x. When comparing to VMS peers (Vitec, Topicus, Constellation) who also carry PPA and are also valued on EV/EBITA, the metric is legitimate in principle — but Nordtech's intangible base is only ~5 years old and therefore amortising faster, so EV/EBITA flatters Nordtech **more** than it flatters the established peers.

**FM4 — Double-Counting: CONFIRMED_RISK.** The "coverage void" framing is inverted: the two analysts are DNB Carnegie (IPO joint global coordinator, ran stabilization) and Nordea (joint global coordinator). That is conflicted underwriter research, which is worse than zero independent coverage. The 26% spread between their PTs (Nordea SEK 73, DNB Carnegie SEK 92) signals the model is unsettled. The discount to VMS peers is triple-explained by legitimate risk: 47-day track record, ~SEK 3.1bn micro/small cap, 28% free float, no independent research.

**FM5 — Catalyst Specificity: PLAUSIBLE_RISK.** Q3 is weakly informative. The Q2 acquisition was a company with only ~SEK 12M annual sales (~1.6% of run-rate revenue). The 41% acquired growth will annualise out. No subsidiary-level revenue/margin disclosure makes Q3 unfalsifiable as a test of discipline.

**FM6 — Base Rate: CONFIRMED_RISK.** The "3 of 4 Nordic/European VMS re-rate" claim in §4 has no documented provenance and is survivorship bias — the population was built from the survivors (Constellation, Topicus, Vitec) while de-rated roll-ups (Storskogen −85%, Embracer impairments) are reclassified out of the category. **Hard data obtained:** Vitec (the best-documented Nordic VMS benchmark) paid ~9x EBITA initially, ~12x all-in including earn-outs for its 2024 cohort. This is NOT the 5–7x Constellation folklore the §4 "VMS discipline" rests on.

**FM7 — C-Cap Hard Rule: CONFIRMED_RISK.** C should be 2/5, not 3/5. Under the hard rule, no ✓ survives on unverified claims — and here several claims carrying ✓ are demonstrably wrong (cash conversion, margin, gross margin "unavailable"). With C=2 the grade cannot exceed C.

**FM8 — Revenue Quality: PLAUSIBLE_RISK, leaning confirmed.** ARR SEK 678M (+45%) against ~SEK 768M annualised revenue = 88% recurring — internally consistent. But 52.9% gross margin argues against pure SaaS quality. Portfolio is misidentified, so the SaaS-grade assumption has no evidentiary basis.

**FM9 — Moat 3/5/10yr: UNVERIFIABLE.** Cannot be scored. The asset the §4 memo built the moat around (Opus Dental) is not owned by Nordtech. Any competitive analysis of Scandinavian dental software is analysis of Planmeca, not NTECH.ST.

**FM10 — Hunt the Flipping Disclosure: CONFIRMED_RISK (partial).** 
- (a) Acquisition multiples: UNVERIFIABLE directly, but **implied**. ROIC + organic growth = 22% with organic at 7–9% → implied ROIC ~13–15%. Consistent with paying 8–12x EBITA. Inconsistent with 5–7x discipline. Constellation-class acquirers run ROIC 25%+; 13–15% against Swedish WACC ~9–10% is only marginally value-creative.
- (d) **CONFIRMED:** Founders Nils Bergman and Pål Hodann sold shares at IPO, alongside Karl-Johan Persson (H&M), Fredrik Österberg, Jens von Bahr (Evolution), Nicklas Storåkers (Avanza), Martin Randel, Peter Dahlberg — **SEK ~442M of secondary sold at IPO.**
- Earn-outs: quantum undisclosed — UNVERIFIABLE.

**FM11 — Trigger Tests Load-Bearing Variable: CONFIRMED_RISK.** A single quarter's aggregate margin cannot separate discipline from mix. Better trigger conditions in §6 below.

**FM12 — Asymmetry Already Captured: CONFIRMED_RISK. This is the strongest finding.** IPO at SEK 60; touched 65.00 on day one; fell to **56.10 (−6.5% below offer) by June 26**; now ~60.40 (+0.7% in 47 days). The stabilisation manager bought **1,845,599 shares (88% of the 2,106,190 greenshoe, ~SEK 108M) defending the price.** Over-allotment was exercised for only **260,591 shares (12%)**, with stabilisation terminated early. This is the textbook signature of a **broken IPO**. The only two covering analysts are the banks that sold the deal.

---

## 3. CRITICAL RISKS CONFIRMED

**CONFIRMED_RISK:**
1. Portfolio description in §4 memo is uncorroborated and probably wrong (§0 above).
2. **Broken IPO:** 88% of greenshoe consumed by stabilisation, 12% exercised, early termination (FM12).
3. Both analysts are IPO underwriters; "coverage void" is inverted (FM4).
4. H1 reported operating profit **SEK −0.8M**; implied PPA amortisation ~72% of adj. EBITA; EV/EBIT ~55x (FM3).
5. Memo's ✓ claims inaccurate: cash conversion 91/95% not 104%; margin 28% not 29%; gross margin 52.9% not "unavailable"; price stale (FM2, FM7).
6. Implied ROIC ~13–15% — not Constellation-class; benchmark acquirer Vitec pays 9–12x all-in not 5–7x (FM6, FM10a).
7. Founders + celebrity-investor cohort sold SEK ~442M secondary at IPO; lock-up expires ~Dec 2026 / Jun 2027 (FM10d).
8. §4 base rate unsourced and survivorship-biased (FM6).

**PLAUSIBLE_RISK:**
9. Acquired-company margin dilution: H1 incremental acquisitions contributed SEK 86M sales on SEK 14M adj. EBITA = **16.3% margin** vs. 28.5% group. If next SEK 200M of acquired revenue arrives at 16.3%, group margin falls to ~25.5% through the 27% threshold with no operational failure.
10. Acquisition engine stalling: a SEK 12M-revenue deal in IPO quarter cannot sustain 41% acquired growth (FM5).
11. Revenue quality unestablished; 52.9% GM argues against SaaS-grade (FM8).
12. **Lock-up overhang:** 180 days = ~Dec 7, 2026 (right on the proposed Q3 catalyst window); management 360 days = ~Jun 2027.

---

## 4. GRADE REVISION (final)

| Dimension | §4 Provisional | §5 Final | Reason |
|-----------|---------------|----------|--------|
| Q (Quality) | 4/5 | **2/5** | Cannot score on misidentified portfolio; 52.9% GM, ~0% EBIT, 13–15% ROIC, 16.3% incremental acquired margins |
| F (Floor) | 3/5 | **2/5** | Adjusted metrics strong; reported EBIT ~0; cash conversion deteriorating; net income unconfirmed; net debt absolute undisclosed |
| R (Return) | 3/5 | **2/5** | Broken IPO, underwriter-only coverage, Dec lock-up expiry, SEK 442M insider monetisation, unquantified earn-outs |
| C (Confidence) | 3/5 | **2/5** | Multiple ✓ claims falsified; C-cap rule applies |
| **Total** | **10/12** | **8/20** | |
| **Grade** | QUEUED_HOT | **PARK (Grade D)** | |

**Asymmetry Gate (all 4 required):**
1. **Mispriced now?** NO — at ~15.7–17.7x EV/adj. EBITA, NTECH is roughly fair for a 5-year roll-up with ~13–15% ROIC, ~0% EBIT, and broken-IPO price action.
2. **Realistic bull ≥2x?** CONDITIONAL — requires re-rating to 25x+ VMS peer, execution of 28%+ EBITA margin, and acquisition multiple confirmation. Not achievable in <12 months at current price.
3. **Upside skewed above downside?** NO — lock-up overhang + broken IPO + insider monetisation = asymmetry already partially captured by the tape.
4. **Discrete trigger OR CORE-grade quality (Q≥4)?** NO — Q=2/5, no CORE quality; Q3 earnings weakly falsifiable; Dec lock-up = negative trigger risk.

**ALL 4 GATE CONDITIONS FAIL → ASYMMETRY_GATE_FAIL → PARK**

---

## 5. BUY-ZONE (if monitoring)

On est. LTM-Jun adj. EBITA ~SEK 205M, 52.05M diluted shares, ND ~SEK 82M:

| EV/adj. EBITA | Implied price | vs. SEK 60.40 |
|---|---|---|
| 11x | SEK 41.8 | −31% |
| 12x | SEK 45.7 | −24% |
| 13x | SEK 49.6 | −18% |
| 15x | SEK 57.5 | −5% |
| ~15.7–17.7x (current) | SEK 60–65 | fair |
| 22x (underwriter PT basis) | SEK 85+ | analyst target |

**Genuine asymmetry requires ~11–13x → SEK 42–50, i.e. 18–31% below market.** Even then, entry gated on verifying acquisition multiples AND operational track record (see §6).

---

## 6. REVISED TRIGGER CONDITIONS (replace "Q3 margin ≥27%")

A single aggregate margin print is not falsifiable. All four required, by Q1 2027 (3 quarters of data):
1. **Disclosed acquisition multiples** (including earn-outs) on a per-deal or cohort basis. If undisclosed → treat as ≥9x → PARK.
2. **Adj. EBITA margin ≥27% for two consecutive quarters** with organic margin stated separately from acquired mix.
3. **Reported operating profit (post-PPA) positive and rising** ex-IPO costs — proves amortisation is a legacy drag, not a treadmill.
4. **Cash conversion stabilised ≥95%** with capitalised development costs disclosed. The 104→95→91% trend must stop.

Clean disconfirmation: **acquired revenue added at <20% adj. EBITA margin for two more cohorts** = mechanical margin decay → thesis dead regardless of headline.

---

## 7. SOURCES

- [MFN — prospectus & pricing](https://www.mfn.se/a/stockholm-nordtech-group/nordtech-publishes-prospectus-and-announces-price-for-its-initial-public-offering-and-listing-of-its-ordinary-shares-on-nasdaq-stockholm)
- [MFN — first day of trading](https://mfn.se/a/stockholm-nordtech-group/first-day-of-trading-in-nordtechs-shares-on-nasdaq-stockholm)
- [Nordtech Q2 2026 interim](https://www.tradingview.com/news/modular_finance:307e13f56bffb:0-nordtech-interim-report-q2-2026/)
- [Stabilisation ended early / greenshoe](https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/3228868/nordtech-ends-share-stabilisation-early-as-over-allotment-option-partially-exercised/)
- [Stabilisation detail](https://www.sahmcapital.com/news/content/nordtech-says-dnb-carnegie-carries-out-stabilization-in-1845599-shares-ends-period-early-2026-07-09)
- [DNB Carnegie PT 92](https://www.marketscreener.com/news/dnb-carnegie-initiates-coverage-of-nordtech-with-a-buy-rating-and-a-target-price-of-92-kronor-ce7f51dbd989f625)
- [Nordea PT 73](https://www.marketscreener.com/news/nordea-initiates-coverage-of-nordtech-with-a-buy-rating-and-target-price-of-73-kronor-ce7f51dad18df027)
- [IPO costs weigh on profit](https://www.tipranks.com/news/company-announcements/stockholm-nordtech-boosts-sales-and-margins-but-ipo-costs-weigh-on-profit)
- [Plandent — Opus Dental still Planmeca](https://www.plandent.com/sv/mjukvara/Opus-Dental/)
- [Opus 2016 founder buyout](https://www.opusdental.com/sv/nyheter-1/opus-flyttar1/)

---

## 8. DILIGENCE NOTES (for any future revisit)

**Critical open questions requiring primary filing access:**
1. What are the actual portfolio companies across all three segments (Business Platforms, Operational Solutions, Public Infrastructure)? What is their vertical and GM breakdown?
2. What acquisition multiples did Nordtech pay (EV/EBITA initial + earn-out) for each of the 23 acquisitions?
3. What is the absolute net debt figure (separated from earn-outs, IFRS 16, and minority commitments)?
4. What is the recurring revenue composition? ARR (true SaaS) vs. maintenance on perpetual licenses vs. other recurring?
5. What is net income and net income margin?
6. What do the retained stakes of founders Bergman and Hodann represent post-IPO? Any lock-up details beyond the disclosed 180/360-day windows?

**Context for Opus Dental research (sub-agents):** Extensive research was conducted on Opus Dental (Planmeca Oy), DigiDOT (Norwegian national dental EPJ procurement), Frenda AB (Swedish public dental winner), Muntra AB (cloud-native challenger), and regulatory forcing functions (NLL Sweden, FM→SFM Norway, EHDS EU). This research is documented in the session transcript but is now moot for NTECH.ST thesis purposes — it applies to a company (Planmeca/Opus Systemer) Nordtech does not own.

---

## Trust Summary
- SEK 639M LTM revenue, SEK 182M adj. EBITA, 23 acquisitions, IPO June 10 2026 at SEK 60: ✓ (prospectus)
- H1 2026: SEK 383.9M revenue (+50%), SEK 106.9M adj. EBITA (28% margin), SEK −0.8M EBIT: ✓ (Q2 interim)
- Gross margin 52.9%, cash conversion 91/95% (declining): ✓ (Q2 interim — corrects §4)
- Shares 52.05M fully diluted, IPO price SEK 60: ✓ (prospectus)
- 88% greenshoe stabilisation, early termination: ✓ (MFN release + Globe & Mail)
- Both analysts = IPO underwriters: ✓ (MarketScreener)
- Portfolio companies: UNVERIFIABLE (prospectus PDF proxy-blocked; Nordtech's disclosed segments confirmed, specific subsidiaries partial)
- Acquisition multiples paid: UNVERIFIABLE
- Net income: UNVERIFIABLE
- Absolute net debt: UNVERIFIABLE
- SEK ~442M secondary sold by founders/investors at IPO: ~ (confirmed directionally via IPO release)
