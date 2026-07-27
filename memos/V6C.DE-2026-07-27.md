# V6C.DE — Viscom SE
### §5 Deep-Dive + Adversarial Red-Team | 2026-07-27 | Run #68

**Verdict up front: the §3.5 thesis does not survive. GRADE D · TIER PARK.**

Four load-bearing claims from the §4 screen are wrong, stale, or scored more than once:

1. **"Trading at book equity €44M"** — it is not. After a Q1 2026 loss the screen never saw, book is ~€39.8M against a €44.25M cap: **~1.11x book, and 3.4x NCAV.** Not a Graham backstop.
2. **"FY2026 first positive EBIT guidance in 2+ years"** — false. FY2025 carried the **numerically identical** €80-90M / 2-5% EBIT guidance, was reaffirmed on 13 Nov 2025 with seven weeks to run, and delivered **-2.2%**.
3. **"2x at 15x EBIT on €7-8M"** — the *margin* is precedented (7.6% in FY2022), but the 2x needs **€96-99M revenue AND a 12-15x multiple** on a **60.36%-founder-controlled** micro-cap with €10-30k/day of liquidity and three consecutive years of missed EBIT guidance. The multiple is the heroic part.
4. **Scored-once discipline was breached three times**, inflating the §4 total from a true ~5.5-6/12 to the reported 9/12.

Two risks the screen never surfaced at all: a **50%-of-share-capital authorised-capital dilution overhang** put to the 5 June 2026 AGM, and **Europe — 57% of revenue — running a structurally negative EBIT margin.**

---

## 1. Business Overview + Moat Assessment

### What it is
Viscom SE (Hanover; listed 1998; AG→SE conversion completed 5 Jun 2024; ISIN DE0007846867, Xetra V6C) builds inspection systems for electronics manufacturing: solder-paste inspection (SPI), 3D AOI, X-ray/AXI, inline CT, conformal-coating and bond inspection, plus OEM X-ray tubes. ~460-500 employees (⚠ mwb research says ~462; company materials ~500).

**Revenue concentration stacks in one direction:** ~**70% automotive** (mwb), **top-5 customers ≈62% of revenue** (FY2023; ⚠ from the Viscom *AG* single-entity HGB report, group-level FY2024/25 not found), and **57% Europe**. There is no diversification cushion — the same end market, the same handful of customers, the same region.

Self-description: *"European market leader in PCB inspection systems, among the top three worldwide, No. 1 in automotive inspection solutions."*

### Moat — red-teamed
The "top three worldwide" claim does not survive peer sizing.

| Player | FY2025 revenue | FY2025 growth | Q1 2026 growth |
|---|---|---|---|
| Koh Young (KOSDAQ 098460) | KRW 232.7bn ≈ **€145-155M** | **+14.9%** | **+42%** (OP +209%) |
| ViTrox (KLSE 0097) — board-inspection segment alone | RM ~514M ≈ **€105M** | group **+52.7%** | Q4'25 +95% |
| Test Research (TWSE 3030) | not disclosed; **mcap ~€2.5bn** | — | — |
| **Viscom** | **€81.7M** | **-2.9%** | **-27.4%** |
| Saki (private, JP) | ~$54M ? scraper-grade | — | — |

**Viscom is #4-6 globally, not top-3.** Koh Young holds ~52% of 3D SPI with 24,000+ installations across 3,800+ customers, and ~50% of its revenue is 3D AOI — direct overlap, not an adjacent business.

**Moat claims that hold up:**
- **AXI / inline CT is genuinely defensible ground.** Koh Young is optical-only and does not compete here. Viscom's X-ray franchise (X7056-II, OEM X-ray tubes) and inline CT are real technical assets; the June 2026 battery-cell CT order proves commercial traction, and mwb's semiconductor thesis (micro-bumps, photonics, power semis) rests on it.
- **German automotive traceability reputation** — 30 years of qualification into European Tier-1 quality systems. Requalifying an inspection vendor on a running automotive line is genuinely costly, which is why the installed base decays slowly rather than collapsing.
- **Gross margin rose in a downturn** (61.2% FY2024 → ~64.7% FY2025 ~), weak evidence of pricing discipline.

**Moat claims that break:**
- **The AI/algorithm layer is being commoditized.** Viscom's vVision/vAI stack (productronica 2025) is table stakes — Koh Young's KAP already cuts setup up to 70%, and AI-native entrants (DaoAI "5-minute setup, no CAD"; Jutze; Instrumental $80M+; Elementary Robotics $47.5M) attack precisely the hand-tuned-algorithm expertise that *was* the German differentiator. AI raises inspection demand, but that demand is accruing elsewhere: Koh Young's semiconductor-packaging inspection revenue grew **+79% YoY** on AI-server demand.
- **The sponsored bull case concedes the margin problem in writing.** mwb research's initiation cites *"limited pricing flexibility," "sharp swings in demand,"* a fixed-cost structure with procurement, R&D and production *"all anchored in Germany,"* and *"cheaper, 'good enough' Asian alternatives, which make a sustainable expansion of margins inherently difficult."* When the issuer-paid analyst concedes structural margin pressure, that is the ceiling.
- **The CT/battery niche is contested**, not owned: VisiConsult/VCbattery (ERDF-funded for inline battery CT), Comet Yxlon, Nordson Dynamic Planar CT, Saki 3D-CT.

### Moat durability — 3 / 5 / 10 years (scored separately, failure mode #9)
- **3yr — WEAK-MODERATE.** Installed-base inertia and automotive requalification cost protect the existing fleet. New wins are already being lost: -27.4% in the same quarter Koh Young's *core SMT* grew ~38%.
- **5yr — WEAK.** Defensible ground narrows to AXI/CT + European automotive — the worst-positioned end market in the industrial economy. The scale gap compounds: an €82M-revenue company cannot out-spend a €150M competitor on R&D indefinitely from a high-cost jurisdiction.
- **10yr — WEAK / MELTING.** If AI commoditizes defect classification, the residual moat is X-ray hardware physics (tubes, detectors, CT reconstruction) — real, but a much smaller business against better-capitalized rivals (Nordson, Comet, Waygate).

**Moat verdict: a regional installed-base + X-ray-hardware moat, not an algorithm moat.** The §4 screen credited "proprietary 3D AOI algorithms" — exactly the layer AI is eroding.

---

## 2. Financial Baseline — Re-derived from Primary Disclosure (failure mode #1)

Every figure re-derived for a *single stated period* from EQS ad-hoc/corporate releases, then arithmetic-checked against adjacent periods. **Corrections to the §3.5 baseline flagged in bold.**

### Income statement
| | FY2022 | FY2023 | FY2024 | FY2025 | Trust |
|---|---|---|---|---|---|
| Revenue | €105.5M | €118,780K | €84,082K | **€81,705K** | ✓ |
| YoY | +32% | +12.6% | -29.2% | **-2.8%** | ✓ |
| Gross margin | — | 62.5% | 61.2% | **~64.7%** | **⚠ aggregator-only — NOT confirmed from filing** |
| EBIT (reported) | **€8.1M** | €6,611K | **-€11,818K** | **-€1,815K** | ✓ (**§3.5 said "~-€14M" FY2024 — WRONG**) |
| EBIT margin | **7.6%** | 5.6% | -14.1% | -2.2% | ✓ |
| EBIT before special effects | — | — | **-€7,095K** | -€1,815K | ✓ (FY24 excl. €4,723K restructuring) |
| Net result | — | €3,040K ~ | **-€9,629K** (EPS -€1.06) | **-€5,625K** | ✓ (**§3.5 said "~-€6.6M implied" — actual -€5,625K**) |
| Order intake | — | — | €75,050K | **€80,982K (+8%)** | ✓ |

**Correction to my own first-pass read (failure mode #1 applied to this memo): the peak EBIT margin is 7.6% (FY2022 at €105.5M revenue), not 5.6%.** This materially improves the bull case versus a "margin never achieved" framing and is corrected throughout §3.

### Quarterly bridge (derived, all cross-checks pass)
| | Revenue | EBIT |
|---|---|---|
| Q1 2025 | €19,789K | +€24K (0.1%) |
| 9M 2025 | €56,751K | -€1,769K (-3.1%) |
| FY2025 | €81,705K | -€1,815K (-2.2%) |
| **⇒ Q4 2025 (derived)** | **€24,954K** | **-€46K (~0%)** |
| **Q1 2026** | **€14,360K (-27.4%)** | **-€3,994K** |

**Q4 2025 ran at a €99.8M annualised revenue rate and produced approximately ZERO EBIT.** The §3.5 model assumed €100M revenue → €7-8M EBIT. Viscom's own most recent quarter at that run-rate delivered €0. *(Caveat: Q4 carries the year-end inventory/receivable write-downs discussed below, so this understates a clean run-rate — but the burden of proof now sits with the bull.)*

### Q1 2026 detail (✓, arithmetic verified)
Revenue €14,360K (-27.4%) · EBIT **-€3,994K** (vs +€24K) · order intake €21,808K (+7.0%: 21,808/20,385 = 1.0698 ✓) · backlog €26,644K (+29.9% vs €20,515K ✓) · **Q1 book-to-bill 1.52** — genuinely strong.

### Regional P&L — the decomposition that matters (failure mode #8)
| Region | FY2024 rev | FY2024 EBIT margin | FY2025 rev | FY2025 EBIT margin | Rev YoY |
|---|---|---|---|---|---|
| **Europe** | €49,869K (59.3%) | **-26.1%** (-€13,011K) | €46,849K (**57.3%**) | **-7.5%** | **-6.1%** |
| **Asia** | €21,624K (25.7%) | -0.1% | €24,175K (29.6%) | **+2.7%** | **+11.8%** |
| **Americas** | €12,589K (15.0%) | +4.7% | €10,681K (13.1%) | **+1.8%** | **-15.2%** |
| **Total** | **€84,082K** ✓ | -14.1% | **€81,705K** ✓ | -2.2% | -2.8% |

Regional revenue sums to reported group revenue **exactly** in both years — this split is ✓ CONFIRMED. *(Regional EBIT margins sum to ~-€2.67M vs reported -€1.815M; ~€0.85M sits in unallocated/consolidation — margins are ~ directionally sound, not exact.)*

**This is the single most damaging decomposition in the file: 57% of revenue sits in a region that is shrinking AND structurally loss-making. The only growing region (Asia, 30%) earns 2.7%, and the only historically profitable region (Americas) shrank 15% and saw its margin more than halve.** A 2-5% group margin is arithmetically unreachable without fixing Europe, and Europe merely got *less bad*.

### Balance sheet
| | Dec 31 2024 | Dec 31 2025 | Mar 31 2026 (est.) | Trust |
|---|---|---|---|---|
| Total assets | €94,640K ~ | **€90,648K** | — | ✓ Dec-25 |
| Current assets | — | **€59,810K** | — | ✓ |
| Current liabilities | — | **€35,585K** | — | ✓ |
| Non-current liabilities (derived) | — | €11,041K | — | ~ |
| Total equity | €50,680K ~ | **€44,022K** | **~€39,800K** | ✓ Dec-25; **derived Mar-26** |
| Equity ratio | 53.6% | **48.6%** | ~46% est. | ✓ |
| Cash | €5,530K ~ | **€3,908K** | — | ✓ Dec-25 |
| Bank overdraft | €9,880K ~ | **UNCONFIRMED** | — | **? floor-critical, unresolved** |
| Net debt incl. IFRS16 | ~€16M est. | **~€18-25M est.** | — | **⚠ UNVERIFIED** |

Overdraft datapoints: €9,880K (Dec-24 ~), €15,880K (Jun-25 ~). **Dec-2025 could not be obtained.** Floor-critical; stays `?`.

### Shares, price, cap — re-derived and now reconciled
- **Issued: 9,020,000 no-par shares** ✓ (Satzung, €1.00/share). **Treasury 1.50%** (bought back 2008/09) ⇒ **outstanding ≈ 8,885,000.**
- **9,020,000 × 0.985 × €4.98 = €44.25M** — this *exactly* reconciles the quoted market cap, resolving the ⚠ share-count discrepancy. **§3.5's 8.88M was numerically right but back-solved circularly from cap ÷ price; it is now confirmed by mechanism.**
- Price **€4.98-4.99** (Jul 27 2026) ✓ — **€5.50 on Jul 6 2026, i.e. -9% in three weeks.**
- **Market cap €44.25M ✓ · EV ≈ €44.25M + ~€21M = ~€65M ~ · EV/Sales (FY2025) = 0.80x**
- **Ownership: Heuser + Pape (founders, incl. foundations) 60.36% · treasury 1.50% · free float 38.14% ≈ 3.44M shares ≈ €17M.**

### The Graham question (Task H) — answered
- **NCAV = current assets €59,810K − TOTAL liabilities €46,626K = €13,184K = €1.48/share.**
- **Price €4.98 = 3.4x NCAV. Definitively NOT a net-net, and not close.**
- BVPS €4.95 (Dec-25) → **~€4.48 (Mar-26 est.)**. At €4.98 the stock trades **above** book. The §3.5 "Ben Graham backstop" framing is wrong.

### Clean operating earnings (failure mode #3)
- **FY2024 clean EBIT = -€7,095K** (reported -€11,818K less €4,723K restructuring) ✓
- **FY2025 EBIT = -€1,815K**, with no restructuring add-back. FY2025 was depressed by *"valuation adjustments on inventories and receivables"* — but **receivable write-downs also hit FY2024**, so these are recurring, not one-off, and **no add-back is justified.**
- Q1 2026's -€3,994K is volume/mix, i.e. operating.

**Clean operating earnings are NEGATIVE (≈ -€1.8M FY2025; -€4.0M in Q1 2026). There are no clean operating earnings to capitalize.** Every "15x EBIT" figure in the §3.5 note is applied to a *forecast* — produced by a management team that has missed its own EBIT forecast three years running. This name cannot be valued on EV/EBIT; only on book or EV/Sales.

---

## 3. Adversarial Red-Team — 12 Failure Modes

### #1 · Re-derive every load-bearing number — **SEVERITY: HIGH · PROBABILITY: CONFIRMED · VERDICT: FAIL (4 errors, incl. one of mine)**
- FY2024 EBIT is **-€11,818K**, not "~-€14M"; FY2024 net **-€9,629K**, not -€9.44M.
- FY2025 net result is **-€5,625K** (reported), not "~-€6.6M implied."
- Share count: §3.5 back-solved 8.88M from cap ÷ price (circular), then used it to validate the cap. Correct chain is 9,020,000 issued − 1.50% treasury = 8.885M outstanding.
- **My own first-pass error, corrected:** peak EBIT margin is **7.6% (FY2022)**, not 5.6% (FY2023). This makes the bull case *better* than my initial read and is corrected in #11 and the Gate.
- Contamination caught and discarded: a "Viscom Q1 2026" query returned "total assets €2,758.6M, equity ratio 44.0%" — that is **ISIN DE0005089031, a different company**. Also flagged: aggregators surface Viscom **AG single-entity HGB** figures (€105.2M rev / €1.6M EBIT for 2023) that conflict with **group IFRS** (€118.78M / €6.611M). **Group IFRS used throughout.**

### #2 · "Too good to be true" = DATA ALARM — **SEVERITY: MEDIUM · PROBABILITY: HIGH · VERDICT: TWO ALARMS — one defused, one live**
- **Alarm A — the 64.71% gross margin. DEFUSED but DOWNGRADED.** A 64.7% "gross margin" on a hardware maker looks software-like. Resolution: this is a German **Rohertrag** (revenue less *material* cost) with **personnel below the line in OpEx** — not comparable to a US gross margin including manufacturing labour. The series 62.5% → 61.2% → ~64.7% is internally consistent, so not fabricated — **but it could not be confirmed from the primary filing: ✓ → ⚠ aggregator-only.** The breakeven analysis in #11 is deliberately constructed to be *robust to this uncertainty*.
- **Alarm B — the price target. LIVE ALARM.** mwb research's PT ran **€4.80 (May 2025 initiation) → €5.00 (Apr 2026) → €6.00 (May 2026) → €8.00 (late May 2026)** — a **67% target raise inside ~6 weeks**, and the €6→€8 raise came *after* the FY2025 EBIT miss and the re-issue of the same guidance. **mwb research is explicitly issuer-paid** (a Deutsche Börse Capital Market Partner marketing research packages to issuers: *"from low-cost entry-level packages to convenient all-inclusive services"*). Consensus is **3-4 analysts**. **Not an independent valuation anchor; must not be used as fair value.**

### #3 · Strip one-offs → value on CLEAN operating earnings — **SEVERITY: HIGH · PROBABILITY: CONFIRMED · VERDICT: FAIL**
Clean operating earnings are negative (FY2024 -€7.1M ex-restructuring; FY2025 -€1.8M; Q1 2026 -€4.0M). Worse, the "one-offs" depressing FY2025 — inventory and receivable valuation adjustments — **also appeared in FY2024**, making them a recurring feature of the cost base rather than an add-back. **A thesis that must invent the earnings it then capitalizes is not an earnings thesis.**

### #4 · Score each item ONCE — **SEVERITY: MEDIUM · PROBABILITY: CONFIRMED · VERDICT: FAIL in §4, corrected here**
- *"Trading at book equity €44M"* → scored in **Valuation gap (2/2)** AND **Floor quality (1.5/2)**. One fact, two lifts — and it is now false.
- *"FY2026 first positive EBIT guidance"* → **Valuation gap** AND **Catalyst proximity** AND implicitly **Business quality**. One fact, three lifts — and it is not "first."
- *"64.7% GM"* → **Moat clarity** AND **Business quality**.
Scored once each, the §4 total falls from 9/12 to **~5.5-6/12** — below the QUEUED threshold entirely. **V6C.DE should not have reached the deferred queue.**

### #5 · Absence of a catalyst ≠ catalyst — **SEVERITY: LOW · PROBABILITY: LOW · VERDICT: PASS**
Genuine dated events exist (H1 2026 report ~mid-Aug 2026; FY2026 print Feb 2027). §3.5 honestly scored Catalyst proximity only 1/2. No coverage-void inflation either — the name *is* covered (thinly, and partly by a paid house), so no discovery-runway claim was available to dress up. This is the one failure mode the §4 screen handled correctly.

### #6 · Base rate must include the FAILURES — **SEVERITY: HIGH · PROBABILITY: CONFIRMED · VERDICT: FAIL (§4 named no failures)**
Analog set: European small-cap capital-equipment makers in a trough guiding a margin recovery.

*Re-rated:* **SÜSS MicroTec** (2023-25, swing factor: advanced packaging/AI) · **PVA TePla** (2020-21, semis/SiC) · **Aixtron** (2016-21, GaN/SiC).
*Failed:* **Manz AG** — guided recovery repeatedly, European battery-equipment market collapsed, **insolvent 18 Dec 2024** (revenue €250M 2023 → €170-180M 2024E) · **LPKF Laser** — serial recovery guidance, serial misses, multi-year de-rating · **Viscom itself, FY2025** — guided 2-5% EBIT, delivered -2.2%.

**Base rate: 3 of 6 re-rated. In every winner the swing factor was a SECULAR end-market inflection (semis / advanced packaging / AI) lifting revenue 50-100%+ — never a cost-cut plus a hoped-for cyclical bounce. In every failure, management guided a recovery the end market never delivered.**

Applied here: the secular inflection **is happening in 2026** (SEMI forecasts a record $139bn equipment year; SMT equipment +8.7% to $6.82bn) — **and Viscom is not in it.** Its core is European automotive electronics: Top-100 supplier revenue -4.6% in 2025, German carmakers -4% in Q1 2026, German auto-supplier sentiment sharply down in June 2026, and decisively for a capex vendor, *"capital expenditure is falling as firms opt to preserve liquidity rather than invest in plant expansions."*

### #7 · No hard-rule overrides — **SEVERITY: HIGH · PROBABILITY: CONFIRMED · VERDICT: ENFORCED**
C = 2. Per METHOD, **C<4 caps the grade**, and "resolvable with one lookup" is not a licence — the lookups were **attempted and blocked by egress policy** (see the C-score). Unresolved facts that could each justify a *permanent* discount: Dec-2025 net debt, FY2025 operating cash flow, group-level customer concentration, capitalized development costs, the AGM authorised-capital vote outcome. **No override granted.**

### #8 · Decompose revenue quality — **SEVERITY: HIGH · PROBABILITY: CONFIRMED · VERDICT: FAIL — revenue quality is LOW**
- **~100% project/equipment revenue.** Lumpy, recognized on delivery/acceptance. Q1 2026's collapse was explicitly *"lower revenue recognition"* + *"changed product mix"* — timing-dependent and mix-fragile.
- **No disclosed recurring base.** Service is described as an *"opportunity"* arising because customers are *optimizing existing capacity* — a euphemism for "they aren't buying new machines." Service revenue quantum: **UNVERIFIED**.
- **Customer concentration is severe:** top-5 ≈62% of revenue (FY2023 ~), ~70% automotive. A single Tier-1 pausing capex moves the whole P&L.
- **Regional decomposition is the killer** (table in §2): Europe is 57% of revenue, shrinking 6%, and running a **-7.5% EBIT margin**. Asia (+2.7% margin) is the only grower and is only 30% of revenue. **Profit and growth do not live in the same place, and neither lives in the largest segment.**
- **The battery vertical has already failed twice:** a ~€4M order cancellation from a battery customer hit FY2024 order intake, and battery inspection **missed expectations again in 2025**.

### #9 · Moat durability 3/5/10yr — **SEVERITY: HIGH · PROBABILITY: HIGH · VERDICT: FAIL**
Scored separately in §1: **3yr WEAK-MODERATE · 5yr WEAK · 10yr WEAK/MELTING.** §4 credited "proprietary 3D AOI algorithms" — the exact layer AI is commoditizing. The durable residual is X-ray/CT hardware physics: real, but a smaller business against better-capitalized rivals.

### #10 · Hunt the disclosure that FLIPS the thesis — **SEVERITY: CRITICAL · PROBABILITY: CONFIRMED · VERDICT: THESIS FLIPPED (three separate disclosures)**

**(a) The guidance record — the finding of this memo.**
§3.5 called FY2026's 2-5% EBIT guidance *"the first positive EBIT guidance in 2+ years."* It is not:

| FY | Guidance (set / last confirmed) | Actual | Verdict |
|---|---|---|---|
| 2022 | Raised Oct 2022: rev €95-100M, EBIT €4.7-8.0M | rev €105.5M, EBIT €8.1M (7.6%) | **BEAT** |
| 2023 | rev €110-120M, EBIT 5-10%. Confirmed 14 Nov 2023 | rev €118.78M ✓, EBIT €6.611M (5.6%) — **bottom of range**. Dividend cut 3 months later *"to preserve liquidity"* | **HIT AT THE FLOOR** |
| 2024 | **CUT TWICE**: 23 May 2024 profit warning → EBIT "slightly negative"; 6 Aug 2024 → EBIT b.s.e. **-3% to -9%** | rev €84.08M ✓; **order intake €75.05M — BELOW the corridor even after two cuts**; EBIT b.s.e. -€7.095M (bottom of the twice-cut range); reported -€11.818M | **DOUBLE CUT, STILL MISSED** |
| 2025 | rev €80-90M, **EBIT 2-5% (€1.6-4.5M)**. Confirmed May, **14 Aug**, and **13 Nov 2025** | rev €81.705M ✓; **EBIT -€1.815M** — sign flip, ~€3.4M below the floor of the range | **SEVERE MISS** |
| **2026** | rev €80-90M, **EBIT 2-5% (€1.6-4.5M)** — **numerically identical to FY2025** | Q1 EBIT **-€3.994M** (€4.0M worse than Q1 2025); guidance **confirmed** May 12 and Jun 4 | **in progress** |

**Revenue guidance is reliable — they hit the top line every year. EBIT guidance is not: it has landed at or below the bottom of the guided range for three consecutive years (2023, 2024, 2025).** Management reaffirmed a positive €1.6-4.5M EBIT on **13 November 2025**, seven weeks from year-end, then printed **-€1.815M**. The FY2026 "catalyst" is a **copy-paste of a guidance that has already failed**, issued by an **unchanged** management team.

**(b) A 50%-of-share-capital dilution authority.** The "Genehmigtes Kapital 2021" expired 7 June 2026; the **AGM of 5 June 2026** put to vote the creation of **new authorised capital of up to €4,500,000 / 4,500,000 new shares — ~50% of existing share capital** — exercisable for cash *and/or* non-cash contributions. Against three consecutive loss years, an equity ratio falling 53.6% → 48.6%, cash of €3.9M, an actively-drawn overdraft and a share price near its 52-week low, this is a **live overhang, not boilerplate**. ⚠ The vote outcome and final wording are **UNVERIFIED**. *The §4 screen recorded "dilution: none identified" — technically true historically, and materially misleading prospectively.*

**(c) The governance loop.** Founders **Heuser + Pape control 60.36%** (partly through foundations, which typically never sell — so there is **no takeover-premium optionality** either). Co-founder Pape sits on the **supervisory board** overseeing co-founder Heuser on the **management board**, while together they control the votes that elect that supervisory board. **No CEO or CFO turnover through the entire 2023-2026 collapse**; the management board shrank 4→3 in 2023 without replacement. Minorities have no lever. METHOD lists *"structural-discount value trap (controlled co)"* as a reject-on-sight anti-pattern.

### #11 · The trigger must test the LOAD-BEARING variable — **SEVERITY: HIGH · PROBABILITY: HIGH · VERDICT: PARTIAL PASS — a valid trigger exists, and it points DOWN**

**The load-bearing variable is operating leverage: does OpEx stay at the restructured trough level while revenue recovers?**

Derive OpEx from OpEx = (Revenue × GM) − EBIT:
| | FY2022 (est.) | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Gross profit | ~€65.4M | €74,238K | €51,458K | €52,871K |
| EBIT | €8,100K | €6,611K | -€11,818K | -€1,815K |
| **⇒ OpEx** | **~€57.3M** | **€67,627K** | **€63,276K** | **€54,686K** |
| OpEx / revenue | ~54.3% | 56.9% | 75.3% | 66.9% |

**OpEx is genuinely down €12.9M (-19.1%) from 2023 — the restructuring (145 staff, €4.723M charge) is real.** This is the strongest fact in the bull case. Note also that FY2022 carried €57.3M of OpEx on €105.5M of revenue, so the cost base is now *below* the level that supported a 7.6% margin year.

**Breakeven revenue = FY2025 revenue + (FY2025 EBIT loss ÷ GM):**
- at GM 64.71% → 81.705 + 1.815/0.6471 = **€84.51M**
- at GM 61.2% → 81.705 + 1.815/0.612 = **€84.67M**

**Breakeven is ~€84.6M regardless of the gross-margin assumption** — which is why the ⚠ on GM does not undermine this. Above breakeven, each €1M of revenue drops through at the GM rate.

**FY2026 EBIT ≈ (Revenue − €84.6M) × 0.647:**

| FY2026 revenue | Implied EBIT | In the guided band (€1.6-4.5M)? |
|---|---|---|
| €80M (**low end of guidance**) | **-€2.98M** | ✗ |
| €84.4M (**the analyst's own estimate**) | **-€0.07M** | ✗ |
| €85M (**guidance midpoint**) | +€0.32M | ✗ |
| €87.1M | +€1.68M | ✓ (just) |
| €90M (top of guidance) | +€3.49M | ✓ |

**The FY2026 EBIT guidance is only reachable in an €87-90M revenue window — the top ~30% of the company's own guided revenue range. At its own midpoint, EBIT is approximately ZERO. At the bottom of its own range, Viscom loses ~€3M.** And the sell-side revenue estimate of €84.4M — from the issuer-paid house carrying a BUY and an €8.00 target — **implies EBIT of roughly zero.** The bull's own revenue number does not support the bull's own EBIT number.

Required run-rate: €87.1M needs **€72.7M in Q2-Q4 = €24.25M/quarter** vs a Q2-Q4 2025 average of €20.6M — **+17.5% YoY in each of three consecutive quarters**, in a year that opened -27.4%. Backlog of €26.6M covers ~1.1 quarters.

**The trigger: the H1 2026 report (~mid-August 2026, ~3 weeks out).** It tests the load-bearing variable *directly* — H1 revenue and H1 EBIT jointly reveal the revenue trajectory and whether OpEx held. Not a noisy proxy; a valid trigger under #11.

**But a valid trigger is not a bullish trigger, and the arithmetic says its likely content is a guidance cut.** Note the pattern: in both 2024 and 2025 the company was *still confirming guidance* at the half-year stage — so a mid-August confirmation carries little information, while a cut would be decisive. The trigger is **asymmetric in the wrong direction**: it can disconfirm, but confirmation would be nearly meaningless given the base rate.

### #12 · Is the asymmetry already CAPTURED? — **SEVERITY: MEDIUM · PROBABILITY: MEDIUM · VERDICT: NOT captured — but there was never much to capture**
The stock is **-9% in three weeks** (€5.50 Jul 6 → €4.98 Jul 27) and well off its 52-week high, so the move has gone *against* holders rather than away from buyers — nothing has been paid out.

But that is the wrong question. Repriced honestly against fair value:

| Method | Assumptions | Equity value | Per share |
|---|---|---|---|
| Book value | Mar-26 est. €39.8M, 1.0x | €39.8M | **€4.48** |
| Normalized EBIT, 10x | mid-cycle rev €90M → EBIT €3.5M; less €21M net debt | €14M | **€1.58** |
| Normalized EBIT, 15x | same | €31.5M | **€3.55** |
| EV/Sales 0.8x | on €85M revenue, less €21M net debt | €47M | **€5.29** |

**Defensible fair-value range ≈ €1.58-€5.29, centred ~€3.50-4.50. The stock trades at €4.98 — at or ABOVE the centre of its own fair-value range.** The real answer to #12 is not "already captured" but **never present.**

---

## 4. Final Verdict

### Asymmetry Gate — applied explicitly

**1. Mispriced NOW vs fair value? — ✗ FAIL.**
€4.98 vs a defensible fair-value centre of €3.50-4.50. Trading at ~1.11x book, 3.4x NCAV, 0.80x EV/Sales, with negative clean operating earnings and a breakeven revenue (~€84.6M) *above* its own guidance midpoint (€85M). Not cheap; on normalized earnings, arguably dear.

**2. Bull ≥2x realistic? — ✗ FAIL (on the multiple, not the margin).**
2x = €88.5M cap. With ~€21M net debt that needs **EV ~€109.5M** → **€7.3M EBIT at 15x** or **€9.1M at 12x**. On the drop-through model that implies **revenue €96-99M** (+18-21% vs FY2025).
- *The margin is precedented:* 7.6% EBIT in FY2022 at €105.5M revenue, with a cost base then *higher* than today's. Credit where due — this is not a never-achieved margin.
- *The revenue is the first hurdle:* €96-99M requires ~+20% growth from a base that just fell 27% in Q1, with 57% of revenue in a shrinking, loss-making region, against competitors growing 15-52%.
- *The multiple is the heroic part:* a **60.36%-founder-controlled** company with **€10-30k/day of liquidity**, a **€17M free float**, **three consecutive years of missed EBIT guidance**, and a **50% dilution authority** does not clear 12-15x EBIT. It clears 8-11x. At 10x on €8M EBIT: €80M EV − €21M = **€59M cap = 1.33x, not 2x.**
**2x requires a full revenue recovery AND a re-rating multiple the governance/liquidity profile does not support.**

**3. Upside > downside (skew)? — ✗ FAIL.**
Upside: +33% to the 3-4 analyst consensus (~€6.60), +61% to the issuer-paid €8.00, ~2x only on the stacked case above. Downside: a second consecutive guidance miss takes book to ~€38-40M and would plausibly re-rate to 0.7-0.85x book = **€27-34M cap = €3.05-3.80/share = -25% to -40%**. A revenue relapse toward €70M implies EBIT ≈ **-€9.4M**, equity to ~€30M, rising overdraft dependence, and the 50% authorised capital drawn at a distressed price — the Manz path. **Roughly symmetric at best, negatively skewed on the base case.**

**4. Discrete trigger? — ✓ PASS (the only leg that passes).**
H1 2026 report ~mid-August 2026 tests the load-bearing variable directly — though it is asymmetric in the wrong direction (a confirmation would be uninformative given that guidance was also confirmed at the half-year in both 2024 and 2025).

**GATE RESULT: 1 of 4 — FAIL.** Not a live CANDIDATE.
Bench (WATCHLIST) requires Q≥4 with a durable moat, failing the gate *only on price*. Q=2, the moat is not durable, and it fails on three legs. **→ PARK**, with a named re-entry trigger rather than a hard kill, because the order momentum and the FY2027 CT backlog are genuinely real.

**Separately, a near-disqualifying practical constraint:** free float is **€17M** at **€10-30k/day** of traded value. A €500k position is 17-45 days of *total* market volume — ~85-225 trading days at 20% participation. METHOD allows sub-$20M only *"with a clear liquidity path."* There is none. **The binding size constraint here is the float, not the market cap.**

### Scores

**Q — Business Quality: 2/5**
Real niche technology (AXI/CT, OEM X-ray tubes), a genuine 19% OpEx reduction, and a precedented 7.6% peak margin. Against: revenue -31% from 2023; #4-6 globally, not top-3; core SMT rivals grew 15-52% while it shrank; ~100% project revenue with no disclosed recurring base; **top-5 customers ~62%, automotive ~70%, Europe 57% and loss-making**; AI eroding the algorithm layer; German cost base vs "good enough" Asian competition (conceded by its own paid analyst); dividend cut then suspended three years. A sub-scale cyclical equipment maker, not a franchise.

**F — Downside Floor: 2/5**
Equity ratio 48.6%, no going-concern language surfaced — not distressed today. But the floor is *eroding, above the price, and dilutable*: book fell €6.7M in FY2025 and ~€4.2M more in Q1 2026; cash €3.9M against an actively-drawn overdraft; net debt ~€18-25M **unverified**; three consecutive EBIT-loss years with a fourth likely; 3.4x NCAV so no Graham backstop; **a 50%-of-capital authorised issuance that can dilute the floor itself**; and Manz shows this exact profile reaching zero.

**R — Re-Rate Likelihood: 2/5**
Genuine positives, fairly stated: order intake +8% FY2025 and +7% Q1 2026, backlog +30%, Q1 book-to-bill **1.52**, order guidance **raised** to €90-100M on 4 Jun 2026, a real FY2027 inline-CT battery order, and semiconductor/microelectronics/OEM-tube optionality that mwb builds its FY2027 case on. Against: EBIT guidance missed at or below the bottom of the range three years running; the FY2026 band is unreachable below €87M revenue; coverage is 3-4 analysts with the loudest issuer-paid and a 67% target raise in six weeks; the core end market is in its worst contraction in a generation; 60.36% control means no M&A path. A dated trigger exists whose most likely content is negative.

**C — Confidence / Data Quality: 2/5** *(capped)*
Headline P&L (revenue, EBIT, net result, order intake, backlog) is ✓ from EQS releases and passes every internal arithmetic cross-check; the regional revenue split reconciles to group revenue **exactly** in both FY2024 and FY2025; the share-count/treasury/market-cap chain now reconciles to the penny. Everything else does not. **WebFetch and curl were blocked by egress policy on every host attempted (viscom.com, eqs-news.com, tradingview.com, even en.wikipedia.org — all 403). Zero pages of any primary filing were read.** Unverified: Dec-2025 bank overdraft/total financial debt (floor-critical), FY2025 operating cash flow and FCF, the Q1-2026 balance sheet, gross margin from filing, group-level customer concentration (the 62% is FY2023 and from the *AG* single-entity report), capitalized development costs, exact treasury share count, the AGM authorised-capital vote outcome, going-concern/covenant language. Per METHOD's non-English-filer rule, **C is capped at ≤2** until order book, revenue, GM, operating margin, net debt and share count are *all* confirmed from the primary filing.

### Grade & Tier

**GRADE: D · TIER: PARK.**

Not "interesting but gated" (grade C) — that is for a real asymmetry obscured by data holes. Here the adversarial pass shows the **asymmetry is absent on the company's own demonstrated economics**, independent of the data holes; the data holes are a second, separate problem.

Three METHOD reject-on-sight anti-patterns fire simultaneously: *"2x only via a heroic multiple," "slow multi-year cyclical grind,"* and *"structural-discount value trap (controlled co)."* A CONFIRMED RED-FLAG on management credibility independently caps the grade at C or below; the failed Gate, the dilution authority and the absent liquidity path take it to D.

---

## 5. Summary Block

```
GRADE: D  ·  TIER: PARK
Q 2/5 · F 2/5 · R 2/5 · C 2/5

Financial baseline (as of 2026-07-27; financials/V6C.DE.md):
  Revenue: €105.5M (FY22) → €118.78M (FY23) → €84.08M (FY24, -29.2%) → €81.705M (FY25, -2.8%) ✓
  Gross margin (German Rohertrag; personnel BELOW the line): 62.5% → 61.2% → ~64.7% ⚠ aggregator-only
  EBIT: +€8.1M (7.6%, FY22 = peak) → +€6.611M (5.6%) → -€11.818M (-14.1%) → -€1.815M (-2.2%) ✓
    clean FY24 EBIT -€7.095M (ex €4.723M restructuring) ✓ · FY25 has no add-back (write-downs recur)
  Net result: -€9.629M (FY24, EPS -€1.06) ✓ → -€5.625M (FY25) ✓
  Q1 2026: revenue €14.360M (-27.4%) ✓ · EBIT -€3.994M ✓ · orders €21.808M (+7%) ✓ · backlog €26.644M (+30%) ✓
  Derived Q4 2025: revenue €24.954M (≈€100M annualised) → EBIT ≈ €0. KEY.
  Derived OpEx: ~€57.3M (FY22) → €67.63M (FY23) → €63.28M (FY24) → €54.69M (FY25). Restructuring real (-19.1%).
  Derived breakeven revenue: ~€84.6M (ROBUST to the GM assumption). FY26 guidance midpoint €85M ≈ breakeven.
  Regional FY2025 (sums to group revenue EXACTLY ✓): Europe €46.849M (57.3%) at -7.5% EBIT margin ·
    Asia €24.175M (29.6%) at +2.7% · Americas €10.681M (13.1%) at +1.8%
  Concentration: top-5 customers ~62% of revenue (FY2023 ~, AG single-entity) · automotive ~70% ~
  Balance sheet Dec 31 2025: assets €90.648M ✓ · equity €44.022M ✓ (48.6%, from 53.6%) · cash €3.908M ✓
    current assets €59.810M ✓ · current liabilities €35.585M ✓ · NCAV €13.18M = €1.48/sh (3.4x NCAV)
  Net debt incl. IFRS16: ~€18-25M ⚠ UNVERIFIED (overdraft €9.88M Dec-24 ~, €15.88M Jun-25 ~, Dec-25 ?)
  Shares: 9,020,000 issued ✓ − 1.50% treasury = ~8.885M outstanding ✓ (reconciles cap exactly)
  Ownership: founders Heuser+Pape 60.36% (incl. foundations) ✓ · free float 38.14% ≈ €17M ✓
  Dilution: none historical ✓ BUT 4,500,000-share authorised capital (~50%) on the 5 Jun 2026 AGM agenda ⚠
  Dividend: cut Feb 2024 "to preserve liquidity"; last paid €0.05 on 3 Jun 2024; none since ✓
  Liquidity: ~€10-30k/day traded value ⚠ — a €500k position is 17-45 days of TOTAL market volume
  Price €4.98 (Jul 27; €5.50 on Jul 6, -9% in 3wks) · Cap €44.25M ✓ · EV ~€65M ~
  P/B ~1.11x (Mar-26 est. BVPS €4.48) · 3.4x NCAV · EV/Sales 0.80x · P/E n.m. · EV/EBITDA n.m.
  FCF: UNVERIFIED (FY2025 OCF not obtained)

Financials verified against primary filing: NO.
  Egress policy blocked WebFetch and curl on EVERY host attempted (viscom.com, eqs-news.com,
  ad-hoc-news.de, tradingview.com, en.wikipedia.org — all 403). Zero pages of the FY2025 annual
  report, the Q1 2026 quarterly statement, or any financial statement were read. All figures come
  from EQS press-release text relayed via web search, cross-checked for internal arithmetic
  consistency (the Q1/9M/FY bridges, the +7% and +30% Q1 deltas, the regional revenue sums, and
  the share-count→market-cap chain ALL reconcile). Headline P&L is high-confidence; the balance
  sheet below the equity line is not.

Base rate: "European small-cap capital-equipment makers guiding a margin recovery out of a trough
  re-rated 3 of 6 (SÜSS MicroTec, PVA TePla, Aixtron re-rated; Manz AG → INSOLVENT Dec 2024,
  LPKF Laser → serial misses and multi-year de-rating, Viscom itself → missed its own FY2025 guide).
  Swing factor = whether a SECULAR end-market inflection lifts revenue 50-100%+, not whether costs
  were cut. Every winner rode semis/advanced-packaging/AI; every failure guided a recovery the end
  market never delivered. Viscom's core is European automotive electronics — the one end market
  contracting, with customer capex frozen to preserve liquidity — so the swing factor is ABSENT."

Skeptic's checklist: 3 CONFIRMED, 3 PLAUSIBLE, 3 UNVERIFIED, 1 RED-FLAG
  ✓ CONFIRMED  — (2) revenue durability: order intake €80.98M FY25, backlog €26.64M (+30%), order
                   guidance raised to €90-100M, all quote-anchored; (5) customer concentration:
                   top-5 ~62%, automotive ~70%, Europe 57.3% and loss-making — concentration is
                   CONFIRMED AS SEVERE (the % itself is ~); (8) ownership & dilution: 60.36% founder
                   control, 1.50% treasury, no historical issuance — but a ~50% authorised capital
                   was tabled 5 Jun 2026
  ~ PLAUSIBLE  — (1) revenue recognition: acceptance/mix timing mechanism understood, €26.6M backlog
                   conversion unverified; (3) competitive capture: Koh Young core SMT +38% vs Viscom
                   -27.4% in the same quarter strongly implies share loss, no head-to-head
                   qualification evidence either way; (6) pricing power: GM rose 61.2%→64.7% in a
                   downturn, but the paid analyst concedes "limited pricing flexibility"
  ? UNVERIFIED — (4) moat stickiness / requalification-cycle length; (7) accounting quality — primary
                   filing never opened: no read of receivables/inventory vs revenue, capitalized
                   development costs, cash conversion, related parties, covenants. NOTE: inventory
                   and receivable valuation write-downs hit BOTH FY2024 and FY2025 — recurring
                   "one-offs" are an accounting-quality amber; (9) input/supply dependency (FX cited
                   as an FY2025 EBIT drag, unquantified)
  ⛔ RED-FLAG   — (10) MANAGEMENT CREDIBILITY. EBIT landed at or below the BOTTOM of the guided range
                   three years running (2023, 2024, 2025), including TWO formal cuts in 2024 that it
                   still missed. Reaffirmed FY2025 EBIT of +€1.6-4.5M on 13 Nov 2025 — seven weeks
                   from year-end — and delivered -€1.815M. Has now re-issued the NUMERICALLY IDENTICAL
                   guidance for FY2026 while Q1 2026 EBIT came in €4.0M worse than Q1 2025. Zero
                   management turnover through the entire collapse; co-founder on the supervisory
                   board overseeing co-founder on the management board, with 60.36% of the votes.

Open questions (what would raise C):
  1. Bank overdraft / total financial debt + IFRS16 leases at Dec 31 2025 — floor-critical, still `?`
  2. FY2025 operating cash flow and FCF; working-capital movement; is the loss cash or non-cash?
  3. Q1 2026 balance sheet (equity, cash, drawn overdraft at Mar 31 2026) — my €39.8M equity is DERIVED
  4. Outcome and final wording of the 5 Jun 2026 AGM authorised-capital resolution (~50% of capital)
  5. Group-level top-5 customer concentration for FY2024/FY2025 (the 62% is FY2023, AG single-entity)
  6. Gross margin confirmed from the filing + its exact definition (Rohertrag vs Umsatzkosten basis)
  7. Capitalized development costs (German industrials often capitalize R&D; material to real earnings)
  8. Size and delivery schedule of the June 2026 inline-CT battery order (inferred ~€10M, undisclosed)
  9. Covenant terms on the overdraft facility; any going-concern language
 10. Average daily traded value over 90 days — is any position size viable at all?

Buy-zone / upgrade trigger / downgrade trigger:
  BUY-ZONE (re-open §5 only here): ≤ €3.30/share ≈ €29M cap ≈ 0.74x book — where the €90-100M order
    book and €26.6M backlog are bought below liquidation-adjusted equity and the skew genuinely inverts.
    Even then, the €17M free float caps any position at token size.
  UPGRADE TRIGGER (any one, then re-run §5): (a) H1 2026 EBIT ≥ -€1.0M on H1 revenue ≥ €38M — proves
    OpEx held while volume returned, the load-bearing variable; (b) FY2027 guidance ≥ €95M revenue with
    EBIT ≥ 6%, i.e. a genuine step-change on the CT/semiconductor backlog; (c) Europe reaching EBIT
    breakeven on a disclosed regional basis; (d) the authorised capital left unused through FY2027.
  DOWNGRADE / KILL TRIGGER: FY2026 guidance cut at the H1 print (base case); OR net debt confirmed
    > €28M; OR ANY drawdown of the ~50% authorised capital; OR H1 2026 EBIT worse than -€5M; OR a
    third consecutive year of inventory/receivable write-downs → move PARK to KILL.

Asymmetry-to-risk in one sentence:
  You are paying ~1.11x an eroding, dilutable book and 0.80x sales for a sub-scale German inspection-
  equipment maker whose breakeven revenue (~€84.6M) sits ABOVE its own guidance midpoint, whose largest
  region (57% of revenue) loses money, whose top-5 customers are ~62% of sales, whose two nearest
  competitors grew 15-52% in the year it shrank 3%, whose board has missed the bottom of its own EBIT
  guidance three years running and re-issued the identical target after reaffirming it seven weeks
  before missing it, which is 60.36% founder-controlled with ~€10-30k/day of liquidity and a 50%
  dilution authority on the table — for roughly +33% of credible upside against -25% to -40% of
  credible downside.

HUMAN VERIFICATION CHECKLIST (before any capital):
  1. OPEN THE FY2025 ANNUAL REPORT PDF (viscom.com → IR → Financial Reports; I was egress-blocked)
     and read the balance sheet + cash-flow statement. Confirm the Dec-31-2025 bank overdraft, total
     financial debt, IFRS16 lease liabilities, and FY2025 operating cash flow. If net debt including
     leases exceeds €28M, the equity value in every scenario above falls by the excess and the floor
     argument collapses. THIS IS THE SINGLE MOST IMPORTANT UNRESOLVED NUMBER.
  2. CONFIRM THE 5 JUNE 2026 AGM OUTCOME on the ~€4.5M / 4,500,000-share authorised capital (~50% of
     share capital), including whether subscription rights can be excluded. Combined with €3.9M of
     cash and a drawn overdraft, this is the mechanism by which the "book value floor" gets diluted
     away. I could not verify whether it passed.
  3. VERIFY THE GUIDANCE-MISS SEQUENCE INDEPENDENTLY — pull the 13 Nov 2025 9M release and the
     23 Feb 2026 preliminary release side by side and confirm a 2-5% EBIT margin was reaffirmed seven
     weeks before a -2.2% print, and that FY2026 carries the identical 2-5% target. Also confirm the
     two 2024 guidance cuts (23 May, 6 Aug). The entire negative verdict rests on this pattern.
  4. RE-DERIVE THE BREAKEVEN from the audited P&L rather than my back-solved OpEx. Confirm the gross-
     margin DEFINITION (Rohertrag vs cost-of-sales) and whether personnel sits above or below the line.
     Then confirm FY2026 EBIT of €1.6-4.5M is only reachable at ~€87-90M revenue.
  5. CONFIRM THE COMPETITIVE READ from primary filings — Koh Young Q1 2026 (+42% revenue, +209% OP)
     and ViTrox FY2025 (+52.7%). If those are real while Viscom printed -27.4%, this is share loss,
     not a cycle, and no cyclical-recovery thesis is available at any price.
  6. CHECK LIQUIDITY BEFORE ANY SIZING. Free float ~€17M at ~€10-30k/day. Pull 90-day average traded
     value on Xetra/Tradegate. If it confirms, this name is untradeable at any meaningful size and the
     analysis above is academic regardless of the verdict.
```

---

*Sources (all web-search-relayed; no primary filing accessible — egress policy blocked WebFetch/curl on every host):*
*EQS ad-hoc 23 Feb 2026 (FY2025 preliminary + FY2026 guidance) · EQS corporate 31 Mar 2026 (audited FY2025: revenue €81,705K, EBIT -€1,815K, net -€5,625K, order intake €80,982K, assets €90,648K, equity €44,022K, cash €3,908K, current assets €59,810K, current liabilities €35,585K) · EQS 12 May 2026 (Q1 2026: revenue €14,360K, EBIT -€3,994K, orders €21,808K, backlog €26,644K) · EQS ad-hoc 4 Jun 2026 (order-intake guidance raised to €90-100M on an inline-CT battery-cell order; revenue in FY2027) · EQS 13 Nov 2025 (9M 2025: revenue €56,751K, EBIT -€1,769K, guidance reaffirmed) · EQS 14 Aug 2025 (H1 2025, guidance reaffirmed) · EQS 20 May 2025 (Q1 2025: revenue €19,789K, EBIT +€24K, orders €20,385K) · EQS 25 Mar 2025 (FY2024 results + FY2025 guidance 2-5% EBIT) · EQS ad-hoc 23 May 2024 and 6 Aug 2024 (the two FY2024 guidance cuts) · EQS ad-hoc 27 Feb 2024 (dividend cut "to preserve liquidity") · EQS AGM convocation for 5 Jun 2026 (authorised capital) · Viscom SE Satzung (9,020,000 shares) · Viscom IR shareholder-structure page (60.36% / 1.50% / 38.14%) · Jahresabschluss und Lagebericht der Viscom AG 2023 (top-5 customer concentration) · mwb research initiation "Navigating towards sustainable margins" (26 May 2025) and 05/2026 target raise · Koh Young FY2025 / Q1 2026 results · ViTrox FY2025 results · Manz AG insolvency filing 18 Dec 2024.*
