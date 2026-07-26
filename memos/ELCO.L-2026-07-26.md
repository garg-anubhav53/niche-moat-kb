# ELCO.L — Eleco plc — Deep-Dive Memo
Date: 2026-07-26
Analyst: Niche Moat Hunter (Opus adversarial pass)

---

## 0. Verdict up front

**The thesis as scouted does not survive. Downgrade to D / PARK.**

Three findings break it, in descending order of severity:

1. **Cash conversion collapsed and nobody has explained it.** OCF fell from £8.96m to £5.06m while adjusted EBITDA *rose* from £7.7m to £10.2m. OCF/adj-EBITDA went 116% → 50%; FCF/adj-EBITDA went 82% → 40%. The explanation recorded in our own `financials/ELCO.L.md` — "due to PEMAC acquisition outflow (£4.8m)" — **is an accounting error**: acquisition consideration is an *investing* outflow and cannot reduce operating cash flow. The decline is genuinely unexplained. On FCF the stock is 21x EV/FCF, not a cheap 2.15x anything.
2. **The catalyst has already fired, and the market ignored it.** The scout brief says "H1 2026 results due ~Sept/Oct 2026 as soft catalyst." Eleco published an H1 update on ~21–22 July 2026 — record recurring revenue, ARR £35.5m, **organic ARR +23%**, TRR 85% of revenue, debt-free. That was four to five days before this memo. The stock is ~117.5p, nearer its 52-week low (102.5p) than its high (182.5p). Good news printed; no re-rate. Under red-team check #12 this is worse than "asymmetry already captured" — it is *asymmetry offered and declined*.
3. **The 218p consensus is company-financed and stale.** Eleco's NOMAD **and** broker is Cavendish Capital Markets — which is what finnCap became after merging with Cenkos. The scout's "Zeus Capital, Cenkos, WH Ireland" is wrong: there is no evidence of Zeus or WH Ireland coverage, and "Cenkos" *is* the house broker under a legacy label. The 250p top of the range is Cavendish's, written when the stock was 130p and never marked down. The other identified house, Equity Development, publishes research its own boilerplate says is "commissioned and paid for by those companies themselves… not deemed to be independent as defined by the FCA."

The business itself is **not** broken — 89.6% gross margin, 85% recurring revenue, net cash, no debt, a growing dividend, and genuinely accelerating organic ARR. This is a PARK on **price, data quality and catalyst**, not on business quality. A named revisit zone is given in §7.

**⚠ Confidence warning, stated before anything else:** every external host was blocked by egress policy this session (`connect_rejected — policy denial` at the proxy for investegate, LSE, eleco.com, Stockopedia, Yahoo, and every search engine); `snapshot.py` returned `price: None`; the session WebSearch budget was exhausted at 200/200. **I could not open a single primary filing.** Every figure below is secondary. Per METHOD.md's non-primary-source rule, **C is hard-capped at 2**, and no figure in this memo may be treated as ✓ CONFIRMED.

---

## 1. What Eleco actually is — and a correction to the scout brief

The scout brief lists Eleco's products as "Archidata / Spec, PlanSwift, StairDesigner, ElectroBIM, Dds:D, PEMAC, Kivue." **At least two of these appear not to be Eleco products at all.** PlanSwift is a ConstructConnect (Roper Technologies) takeoff product; Archidata is a separate Canadian firm. Meanwhile the brief omits **Asta Powerproject**, which is Eleco's flagship and by some margin its most important asset — the dominant construction planning/scheduling package among UK contractors and the main domestic alternative to Oracle Primavera P6.

Eleco's actual portfolio, as best I can reconstruct: **Asta Powerproject** (construction scheduling, UK flagship), **Bidcon / Consultec** (Nordic estimating), **Dds-CAD / ElectroBIM** (Norwegian MEP & electrical BIM), **Staircon** (stair design — the brief's "StairDesigner"), **IconSystem** (building asset information), **ShireSystem** (UK CMMS), **BestOutcome** (PPM), **PEMAC** (Irish CMMS, Jan 2025), **Kivue** (PPM, Feb 2026), and **Veeuze** (German visualisation — impaired 2025, disposed April 2026).

**Why this matters, and it matters a lot:** the scout's moat paragraph — "PlanSwift competes with Bluebeam Revu, PlanGrid, Trimble, Sage Estimating" — is a competitive analysis of a product Eleco does not own. The entire §9 moat question has to be re-asked against Asta Powerproject. That is red-team check #1 failing at the level of *what the company even sells*.

*(Confidence: I am reasonably confident of the corrected list from sector knowledge, but I could not verify it in-session. Flagged as an explicit human-verification item.)*

---

## 2. The 12 adversarial red-team checks

### Check 1 — Re-derive every load-bearing number from primary source

Not possible this session (all primary sources blocked). What I *can* do is re-derive internal consistency and find where the scout's numbers break.

**Errors found in the scout brief and in our own `financials/ELCO.L.md`:**

| Scout / repo claim | What the evidence actually says | Severity |
|---|---|---|
| "~£4M Veeuze impairment" | **£2.3m** impairment of Veeuze GmbH (2024: £nil) | Material — the £4m is 74% overstated |
| "Veeuze (acquired 2022)" | Veeuze was **formed** in 2022 by merging active online GmbH (acquired 2018, €3.45m) and ESIGN GmbH — it was never acquired | Material — changes the capital-allocation read |
| repo: "EBIT / Op profit £5.2M (13.4%)" FY2025 | **Statutory operating profit £2.8m, down 32%** (2024: £4.1m); statutory PBT £2.8m, down 35% (2024: £4.3m) | Material — the repo file records an adjusted figure as statutory |
| repo: "OCF lower… due to PEMAC acquisition outflow (£4.8m)" | Acquisition consideration is an **investing** outflow. This cannot explain an operating cash decline. | **Critical — the one thing that needed explaining is explained wrongly** |
| "H1 2026 results due ~Sept/Oct 2026" | H1 update published **~21–22 July 2026** | Critical — the catalyst is spent |
| "Zeus Capital, Cenkos, WH Ireland" | NOMAD **and** broker is **Cavendish** (ex-finnCap, merged with Cenkos). No Zeus/WH Ireland evidence. | Critical — destroys analyst independence |
| "PlanSwift, Archidata" as Eleco products | Almost certainly not Eleco products; flagship **Asta Powerproject** omitted | Material |

**Organic growth, re-derived.** FY2024 £32.4m → FY2025 £38.8m = +£6.4m (+19.8%). Constant-currency revenue was £38.4m, so FX was a **+£0.4m (+1.2%) tailwind** — it will reverse if sterling strengthens. Acquisition contribution: PEMAC (14 Jan 2025, ~11.5 of 12 months) at €2.7m revenue ≈ £2.2m; Vertical Digital incremental (acquired 16 Apr 2024, so ~3.5 extra months in FY2025) ≈ £0.3m. Total inorganic ≈ £2.5m.

> Organic, constant-currency = (38.4 − 32.4 − 2.5) / 32.4 = **~10.8%** — which ties to the company's stated 11%. The 11% is honest.

**The 29% ARR growth is not.** £26.6m → £34.3m = +£7.7m. Strip PEMAC ARR (undisclosed; est. £1.8–2.3m on £2.2m revenue) and FX (~£0.3–0.4m): organic ARR growth ≈ **+19–21%**.

**So there is a persistent ~9-point wedge between organic ARR growth (~20%) and organic revenue growth (11%).** That wedge is the crux of the whole name. It is legitimate during a perpetual→subscription transition (ARR steps up as licences convert while recognised revenue lags). But **TRR is already 85% of revenue** — the transition is nearly complete, so the wedge should be closing, not widening. If FY2027 still shows ~20% ARR growth against ~11% revenue growth, the ARR metric is not measuring what a buyer thinks it measures.

**One test the company passes.** ARR/TRR ratio: FY2023 1.092, FY2024 1.068, FY2025 1.096. No drift, no ARR-definition creep. Credit where due — this is the check that would catch an inflated ARR and it comes back clean.

**PEMAC + Kivue: cost vs contribution.**

| | PEMAC (Jan 2025) | Kivue (Feb 2026) | Vertical Digital (Apr 2024) |
|---|---|---|---|
| Initial consideration | €6.0m (~£5.1m) cash | £2.3m (£1.84m cash + 337,363 shares) | €1.3m (~£1.1m) cash |
| Earn-out | **up to €2.4m, 2026 & 2027** | none found (unconfirmed) | **up to €250k, 2026** |
| Max total | ~€8.4m (~£7.1m) | £2.3m | ~€1.55m |
| Target revenue | €2.7m (FYE Nov-24) | £1.5m (12m to Oct-25) | €1.2m (FY2023) |
| Target EBITDA | €0.6m — **22% margin** | £0.2m — **13% margin** | €0.3m PBT |
| Price / revenue | ~2.2–3.1x | ~1.5x | ~1.1–1.3x |

Two observations. First, Eleco buys at 1.1–3.1x revenue while trading at 2.15x — mildly accretive arbitrage, genuinely fine. Second, and less comfortable: **both software acquisitions carry margins below the group's 26.3%** (PEMAC 22%, Kivue 13%). The acquisitions are margin-*dilutive*. Group adjusted EBITDA margin nevertheless rose from 23.8% to 26.3%, which means either organic margin expansion is doing heavy lifting, or the *adjustments* are. Given statutory operating profit fell 32% in the same year, I lean toward the latter.

**Is 2.15x EV/Rev cheap for 11% organic + 89.6% GM? Not once you use the right denominator.**

The 2.15x is computed on £38.8m of revenue that includes £3.7m from Veeuze — a business Eleco gave away for €1 in April 2026. And on £16.3m of net cash that ignores ~£2.2m of earn-outs and the £1.84m already paid for Kivue.

| Basis | EV | Multiple |
|---|---|---|
| As scouted (£16.3m net cash, £38.8m revenue) | £83.0m | **2.14x EV/Rev** |
| Honest (H1-26 cash £15.4m − ~£2.2m earn-outs = £13.2m; continuing revenue £35.1m) | **£86.1m** | **2.45x EV/Rev** |
| EV / ARR | £86.1m / £34.3m | 2.51x |
| EV / adj EBITDA | £86.1m / £10.2m | 8.4x |
| EV / "EBITDA after impairment" (£6.9m, *down* from £7.2m) | | **12.5x** |
| EV / OCF | £86.1m / £5.06m | **17.0x** |
| **EV / FCF** | £86.1m / £4.1m | **21.0x** |
| P/E adjusted | £99.3m / £5.2m | 19.1x |
| P/E statutory | £99.3m / £1.3m | 76x |

**Rule of 40:** 11% organic + 26.3% adj EBITDA margin = **37.3** — sub-40, which maps to value-tier pricing, not premium. On cash: 11% + 10.6% FCF margin = **21.6**, which is poor.

The "cheap" case rests entirely on adjusted EBITDA. On free cash flow this is a 21x stock growing organically at 11%. That is not cheap; it is roughly fair.

### Check 2 — "Too good to be true" is a DATA ALARM

An 84% gap to consensus on a name covered for years is exactly the anomaly METHOD.md flags. It resolved as an alarm, decisively.

- **Cavendish Capital Markets is Eleco's Nominated Adviser AND its Broker.** Related-party language in the April 2026 Veeuze disposal RNS confirms the NOMAD role: *"the independent Directors of Eleco, having consulted with the Company's nominated adviser, Cavendish Capital Markets Limited, consider the terms… fair and reasonable."*
- **The lineage matters more than the scout realised.** finnCap → rebranded Cavendish Capital Markets → finnCap Group merged with **Cenkos Securities** (2023–24) into Cavendish Financial plc. So "Cenkos" and "Cavendish" on this stock are **the same paid adviser**, not two opinions. The scout counted one relationship as two.
- **The 250p target is Cavendish's**, published with the stock at 130p and never revised through the fall to ~117.5p. On Cavendish's own FY26 EPS of 6.7p, 250p is a **~37x forward P/E** exit multiple against the 19.4x they concede the stock trades on — roughly half the implied upside is pure multiple expansion.
- **Equity Development also covers Eleco**, and their standing disclosure reads: *"Research produced and distributed by Equity Development on its client companies is normally commissioned and paid for by those companies themselves ('issuer financed research') and as such is not deemed to be independent as defined by the FCA."*
- **The vendor datasets do not agree, and their ranges barely overlap** — which is the tell that "consensus" is one to three stale points:

| Source | "Consensus" | Range | n |
|---|---|---|---|
| MarketScreener / Stockopedia | **218.33p** | 200–250p | ~3 |
| Investing.com / TradingView | 185.33p | 176–200p | 3 |
| MarketBeat | 176p | — | **1** |

The 218p range (200–250p) *excludes* the 176p point; the 185p range (176–200p) *excludes* the 250p point. These are different samples, not two measurements of one number.

- **218p is 19.5% above the 52-week high (182.5p).** 250p is ~37% above it. Targets that require a new all-time high merely to be *reached*, set by the firms the company pays, unrevised through both beats and a 35% de-rating, are not doing valuation work.

**Verdict: the 84% "upside to consensus" should be discarded, not banked.** The one plausibly independent data point (176p, possibly Canaccord) is the lowest in the range and sits outside the 218p band entirely.

### Check 3 — Strip one-offs → clean operating earnings

| | FY2024 | FY2025 |
|---|---|---|
| Adjusted EBITDA | £7.7m | £10.2m (+32%) |
| **"EBITDA after impairment"** | **£7.2m** | **£6.9m (−4%)** |
| Statutory operating profit | £4.1m | **£2.8m (−32%)** |
| Statutory PBT | £4.3m | **£2.8m (−35%)** |
| Statutory net income | £3.3m | £1.3m |
| Adjusted net income | £4.2m | £5.2m |

Adjusted EBITDA rose 32%. The nearest-to-statutory EBITDA measure **fell 4%**. Every pound of apparent progress lives inside the adjustments.

**The bridge does not fully reconcile.** £10.2m − £6.9m = **£3.3m** of adjusting items, of which the Veeuze impairment is **£2.3m**. That leaves **~£1.0m unidentified** — presumably share-based payments, acquisition costs and restructuring, but I could not read the reconciliation. A £1.0m unexplained gap on £10.2m of "adjusted" EBITDA is not trivial.

**Two further adjustments METHOD.md §3 demands that the scout did not make:**

1. **Capitalised development costs.** Eleco capitalises development spend. Adjusted EBITDA is struck *before* deducting it, and the 89.6% gross margin is flattered because capitalised dev sits in intangibles rather than cost of sales. The quantum is undisclosed to me — an explicit open question. This is the standard software-company flattery and it is precisely where DXRX.L's memo in this same KB found the problem.
2. **Veeuze is in the base.** FY2025 revenue of £38.8m includes ~£3.7m from a subsidiary with a £1.3m loss before tax and £1.1m of net liabilities, disposed for €1 with separation effective 1 January 2026. Continuing revenue is **£35.1m**. *(Inference: the impairment appears to sit within continuing operating profit rather than below the line, so Veeuze was probably still consolidated in continuing ops in FY2025 — flagged as an inference, not a fact.)*

**Now the OCF question, which is the centre of the memo.**

| | FY2024 | FY2025 |
|---|---|---|
| OCF | £8.96m | **£5.06m (−44%)** |
| OCF / adj EBITDA | **116%** | **50%** |
| FCF | ~£6.3m | ~£4.1m |
| FCF / adj EBITDA | **82%** | **40%** |

Cash conversion **halved** in the year ARR grew 29%. For an 85%-recurring business at 89.6% gross margin, this is backwards: subscription businesses bill in advance, so deferred income should *grow* with ARR and OCF should *lead* EBITDA — as it did in FY2024 at 116%.

The candidate explanations, none of which I could confirm: a receivables build (collection or revenue-quality problem); deferred income failing to grow with ARR (which would directly undermine the ARR number); a tax catch-up; acquisition costs expensed through operating; or Veeuze's cash burn. **The £2.3m impairment is non-cash and is added back — it explains none of it.**

For calibration, our own KB has the peer comparison: **TRB.L (Tribal Group) — "FCF £16.1M = excellent cash conversion 142%."** Eleco at 40% is not in the same category.

### Check 4 — Score each item once

Explicitly enforced. The organic ARR wedge (~20% ARR vs 11% revenue) is scored **once**, as a *negative* under revenue quality (§Check 8). It is **not** also counted as growth quality in Q, nor as a valuation argument, nor as a catalyst. The £16.3m net cash is scored once, in **F**, and is *reduced* to ~£13.2m there; it is not separately credited as a valuation cushion in the EV maths and then again as a floor. The Veeuze disposal is scored once, as a capital-allocation negative in Q; the fact that it removes a loss-maker is noted but not double-credited as margin improvement.

### Check 5 — Absence of a catalyst is NOT a catalyst

The scout's R rested on "H1 2026 results due ~Sept/Oct 2026" plus a coverage void. Both fail.

- **The H1 information is already public.** Eleco's ~21–22 July 2026 update reported ARR £35.5m (+16% reported, **+23% organic**), TRR 85% of revenue, debt-free, £15.4m cash. The load-bearing metric — organic ARR growth — is out, and it was *good*. The stock is ~117.5p. The September full-results print will add P&L and cash-flow detail, not new ARR news.
- **An AIM broker note is not an institutional initiation** — and here it is worse than neutral: the notes that exist are issuer-financed, so incremental "coverage" on this name arrives pre-discredited. There is no independent initiation to wait for; the equilibrium is the equilibrium.
- **£131k/day of liquidity is why the coverage void persists.** Average daily volume ~111,325 shares at ~117.5p, with a 116/119 bid-offer (~2.55% spread). No institution with a mandate minimum can build a position. That is a *structural* exclusion that no print resolves — it is the 20-year steady state METHOD.md warns about, not a temporary condition awaiting correction.

**R is scored on what remains: one dated print (September H1 results) that tests the thesis but cannot deliver a 2x, plus an undated takeout path.** Undated does not count.

### Check 6 — Base rate must include the FAILURES

See §4 for the full treatment. Headline: I cloned and independently verified the sibling `rerating-situations-kb`. Across **561 logged ≥2x re-raters, 2018–2025**, exactly **10 are UK-listed (1.8%)**, and **not one is a profitable niche B2B software company**.

### Check 7 — No hard-rule overrides

Applied without exception. **C = 2** because I could not open a single primary filing — not because the facts are unknowable, but because they were unreachable this session. Per METHOD.md, "resolvable with one lookup" means *do the lookup or cap the grade*; I could not, so the grade is capped. Customer concentration, NRR/churn, capitalised development quantum, and the deferred-income balance are all **UNVERIFIED**, and each could justify a permanent discount. None is waved through as "probably fine."

### Check 8 — Decompose revenue quality

TRR of £31.3m = 81% of FY2025 revenue (85% at H1 2026). Decomposing what that 81% actually contains:

- **Core Eleco subscription (Asta Powerproject, Bidcon, Dds-CAD, Staircon, IconSystem, ShireSystem)** — genuine annual licence/subscription, the bulk of TRR. Highest quality, but note much of it is *annual licence renewal* on desktop products rather than multi-tenant cloud SaaS. Annual renewals churn more easily than multi-year cloud contracts.
- **PEMAC (~£2.2m)** — described in the acquisition RNS as *"SaaS Computerised Maintenance and Management Software ('CMMS') and specialist services."* That is **the acquirer's own characterisation**, and the phrase "and specialist services" plus a validation-heavy regulated customer base (life sciences, healthcare) is exactly the profile where validated on-prem installs and implementation services sit alongside subscription. **The cloud-SaaS vs on-prem-licence-plus-maintenance split is UNVERIFIED** — and it is the single biggest driver of the 29% headline.
- **Kivue (~£1.5m, FY2026 onward)** — genuinely cloud ("ISO-certified and Cyber Essentials accredited cloud-based platform, Perform"; customers include London City Airport, Aon, Virgin Atlantic). But a **13% EBITDA margin on £1.5m of revenue is not subscription economics** — it implies a meaningful implementation/consulting component.
- **Vertical Digital** — not a software asset at all. A Romanian captive development shop bought for R&D capacity and cost arbitrage. Contributes services, not ARR.
- **Non-recurring ~19% (£7.5m)** — perpetual licences, implementation, training, consultancy.

**Three quality knocks:**
1. **NRR and gross revenue retention are not disclosed anywhere.** For a company headlining 85% recurring revenue, silence on retention is itself informative — a business running 110%+ NRR puts it in the first paragraph. Our own KB shows the contrast: TRB.L discloses 95% GRR / 108% NRR.
2. **The ARR/revenue wedge** (~20% vs 11% organic) means a material part of "ARR growth" is re-labelling existing perpetual customers as subscribers, not winning new economic value.
3. **FX flatters ARR.** ARR is a point-in-time translated number across GBP/EUR/SEK/NOK. FX added ~1.2% to FY2025 revenue and reverses when sterling strengthens — as it appears to have done into H1 2026 (reported ARR +16% vs organic +23%).

### Check 9 — Moat durability at 3 / 5 / 10 years

Re-asked against **Asta Powerproject**, the actual asset.

**3 years — solid (4/5).** Asta is embedded in UK contractor planning workflows: programme files, planner training, subcontractor programme submission formats, and a large installed base taught in UK construction courses. Nobody rips out a planning tool mid-project. Switching cost is real.

**5 years — eroding (3/5).** The threat is not a like-for-like competitor swapping in; it is **bundling**. Autodesk Construction Cloud, Trimble and Procore are absorbing scheduling into platforms that already own the model, the documents and the field data. Oracle Primavera P6 remains the enterprise standard for large infrastructure. Nemetschek owns Bluebeam and has been consolidating AEC point tools. A standalone scheduling vendor at £38.8m of revenue cannot match platform R&D. Critically, **the moat is workflow and training — not regulatory or certification-based.** There is no standard Eleco owns, no accreditation a competitor must obtain, no code that mandates its use. METHOD.md's warning about over-claiming certification moats does not even apply here, because there is no certification moat to over-claim.

**10 years — genuinely uncertain (2/5).** Construction scheduling and quantity takeoff are among the most automatable tasks in AEC. AI-native scheduling and takeoff (Togal.AI, Kreo, and the incumbents' own AI layers) attack exactly the tasks Asta and Bidcon perform. Eleco's own H1 commentary leans on "AI products" — which is simultaneously the right response and an admission that the architecture is being rewritten. **A tool moat is a lagging asset when the workflow it encodes is the thing being automated.**

**Can Autodesk/Trimble/Nemetschek replicate it?** Technically, yes — trivially. Commercially, they would more likely **buy** it, which is the real bull case (§4) and also the reason the moat question is somewhat academic: Eleco's defensibility is less "they can't build this" than "it's cheaper to acquire the installed base."

### Check 10 — Hunt the disclosure that FLIPS it

I hunted specifically for it. Four candidates, in order of importance:

1. **The OCF decline is the disclosure — and it is missing.** The working-capital line detail, and specifically the **deferred income / contract liabilities balance**, would resolve it in one line. Deferred income up strongly → benign timing, thesis intact. Deferred income flat or down while ARR is "+29%" → **the ARR number is not converting to billings and the thesis is dead.** I could not obtain the balance. This is the single most load-bearing unread fact in the memo.
2. **Earn-outs are not in the stated net cash.** PEMAC carries **up to €2.4m** payable in two tranches across **2026 and 2027**; Vertical Digital **up to €250k** payable **2026**. Together ~£2.2m. Eleco headlines gross cash and "free of debt," so these almost certainly sit outside the £16.3m figure. Add the £1.84m already paid for Kivue in February 2026 and the real deployable balance is ~£13.2m, not £16.3m — the net-cash floor is **~19% softer than advertised**. *(That the earn-outs are recognised as contingent-consideration liabilities under IFRS 3 is near-certain; that headline cash is struck before them is inference.)*
3. **Veeuze is a documented capital-allocation failure, and it flips the "serial acquirer" narrative.** Eleco bought active online GmbH in 2018 for €3.45m (€2.95m cash + 597,004 shares at 73.55p + up to €0.4m bonus), combined it with ESIGN GmbH into Veeuze in 2022, impaired it **£2.3m** in 2025, and **sold it on 10 April 2026 for an initial €1** plus a profit share capped at €250k to 2030 — to **3A Consult UG, whose controlling shareholder is a former Veeuze director** (i.e. a related-party MBO requiring the independent directors' fairness opinion). A c.£3m+ investment returned approximately nothing. Any serial-acquirer thesis has to price that in: **the acquisition track record is 1 clear failure out of 4–5 deals.**
4. **Free cash flow after dividends and earn-outs is close to nil.** FCF ~£4.1m − dividend (1.20p × 84.1m ≈ £1.0m) = ~£3.1m retained, against ~£2.2m of earn-outs falling due 2026–27. The M&A flywheel that is the entire growth story has **~£1m/year of organic funding** unless cash conversion recovers or the balance sheet is drawn down. The serial-acquirer model is running on the existing cash pile, not on generated cash.

**No litigation, going-concern language, restatement, or covenant issue was found** — but "not found" here means "not searched successfully," given the access failure. It is not a clean bill of health.

### Check 11 — The trigger must test the LOAD-BEARING variable

**The single load-bearing assumption: that Eleco's reported ARR converts into cash at software-like rates.** Everything else — the 8.4x EV/EBITDA, the 89.6% gross margin, the 2.45x EV/revenue — is downstream of that. If ARR converts, the stock is cheap. If it does not, adjusted EBITDA is an accounting artefact and 21x EV/FCF is the true multiple.

**The scout's proposed trigger fails.** "H1 results showing continued ARR growth" cannot falsify the thesis, because ARR growth is precisely the number in question — it can print big for reasons unrelated to cash generation (acquisitions, FX, perpetual-to-subscription re-labelling). A metric cannot be its own test. Per METHOD.md, that makes it **unfalsifiable and rejected as a trigger**. This is the identical error the KB's DXRX.L memo caught: *"Revenue +25% does not test cash conversion… Correct trigger = cash generation, specifically OCF after capitalised development."*

**The correct trigger: the September 2026 H1 full results, read for three lines and nothing else** —
1. **Net cash from operating activities, H1 2026 vs H1 2025.** Does OCF/adj-EBITDA return toward 90%+, or stay near 50%?
2. **The deferred income / contract liabilities balance.** Is it growing at least as fast as ARR?
3. **Capitalised development expenditure**, and OCF *after* deducting it.

This trigger is informative in both directions, which is what makes it valid. **But note its expected sign is neutral-to-negative** — the ARR good news is already out, so September can only confirm the cash problem or dispel it. **It is a risk event as much as a catalyst**, and it cannot plausibly produce a 2x on its own.

### Check 12 — Is the asymmetry already CAPTURED?

Not captured — **declined**. That is a different and worse finding.

`snapshot.py` returned `price: None` (Yahoo blocked), so the best available prints are 117.50p (bid 116 / offer 119) on 3 July 2026 and ~120.18p on 17 June 2026 — call it 115–125p. Against a 52-week range of 102.5–182.5p, the stock sits in the lower third.

The sequence matters:
- July 2025: ~182.5p (52-week high)
- 28 April 2026: FY2025 results — revenue +20%, adj EBITDA +32%, both "exceeding market expectations," ARR +29%, dividend +20%, debt-free
- ~21–22 July 2026: H1 update — record recurring revenue, organic ARR +23%, TRR 85%
- 26 July 2026: **~117.5p**

**A ~35% de-rating delivered on a sequence of beats, with no profit warning and no single-day crash** — three successive 50-day moving-average breakdowns at 147p → 132p → 115p. The market has had two clean opportunities to re-rate this stock on good news in the last 90 days and has declined both.

Three structural explanations, all of which are *reasons the discount persists* rather than reasons it closes:
1. **Liquidity.** £131k/day. A £1m position is ~8 days of full ADV with ~2.5% round-trip friction before impact. Institutions are mechanically excluded.
2. **No anchor holder.** Largest identified holder Raymond James Wealth Management at 6.08%; **Ameriprise/Threadneedle cut from 5.068% to 3.92%** through the decline; JPMorgan filed a TR-1 amendment 21 July 2026. There is no strategic blockholder to defend the price or force an outcome.
3. **Insiders did not step in.** No director bought a single share in the open market during the entire 35% fall. The only open-market purchase found is NED James Pellatt, 6,052 shares at 165.05p on 19 June 2025 — **£9,990, or 0.007% of the company**, now ~29% underwater. The only 2026 director activity is **option exercises** (187,812 new shares to the CEO and CFO, admitted 3 June 2026) — issuance to insiders, not conviction buying. Resulting stakes: **CEO 289,968 shares = 0.34%; CFO 66,205 = 0.08%.** 1,015,000 options struck at 121p are currently underwater. No buyback found.

Management holding 0.42% between them, publishing a 250p house-broker target, watching the stock fall 35%, sitting on £15m of cash, and buying nothing, is the most eloquent fact in this memo.

---

## 3. The Skeptic's Confirmation Checklist

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | **Revenue recognition** — will ARR convert to cash? | **RED-FLAG** | OCF/adj-EBITDA 116%→50%; FCF/adj-EBITDA 82%→40%; ARR +29% while OCF −44%. Unexplained. Repo's stated explanation (PEMAC outflow) is an accounting error — acquisitions are investing, not operating. |
| 2 | **Revenue durability** — can contracts be cancelled? | **UNVERIFIED** | No churn, GRR or NRR disclosed anywhere, in any year. Much of TRR is *annual* licence renewal on desktop products, which churns more readily than multi-year cloud. Peer TRB.L discloses 95% GRR / 108% NRR; Eleco's silence is informative. |
| 3 | **Competitive capture** — Autodesk/Trimble/Nemetschek? | **PLAUSIBLE (risk is real)** | No regulatory or certification barrier anywhere in the portfolio. Asta competes with Oracle P6, MS Project, Trimble; the structural threat is platform bundling (Autodesk Construction Cloud, Procore) rather than a like-for-like rival. |
| 4 | **Moat stickiness over time** | **PLAUSIBLE 3yr / UNVERIFIED 5–10yr** | Workflow + training + file-format lock-in is genuine near-term. Long-term, scheduling and takeoff are among the most AI-automatable AEC tasks; the moat is a lagging asset. |
| 5 | **Customer concentration** | **UNVERIFIED** | Not disclosed. Probably benign (~35,000 users, SME-weighted, four countries), but *probably* is not a verification. Not waved through per check #7. |
| 6 | **Pricing power persistence** — hold 89.6% GM? | **PLAUSIBLE** | GM stable ~89–89.6% across three years is genuine evidence of price-holding. Discount it: GM is flattered by capitalised development sitting in intangibles rather than cost of sales (quantum unknown). |
| 7 | **Accounting quality** | **RED-FLAG** | (a) OCF collapse unexplained; (b) £3.3m adj-EBITDA bridge only £2.3m identified — ~£1.0m unaccounted; (c) statutory operating profit −32% while adjusted EBITDA +32%; (d) "EBITDA after impairment" *fell* £7.2m→£6.9m; (e) capitalised dev quantum undisclosed; (f) our own `financials/ELCO.L.md` records op profit £5.2m against the £2.8m statutory figure. |
| 8 | **Ownership & dilution** | **PLAUSIBLE** | Dilution genuinely modest: ~0.5%/yr including Kivue's 337,363 consideration shares; options 3.655m = 4.3%; no ATM, no converts, no placings. *But* alignment is very weak — CEO 0.34%, CFO 0.08%, zero open-market director buying through a 35% decline. |
| 9 | **Input & supply dependency** | **PLAUSIBLE** | Software — no physical supply chain, no single-source input, no China exposure. Real FX translation exposure (GBP/EUR/SEK/NOK): +1.2% revenue tailwind FY2025, apparently reversing in H1 2026 (ARR +16% reported vs +23% organic). |
| 10 | **Management credibility** | **PLAUSIBLE** | Positives are real: consistent beats, no profit warning in 2025–26, dividend +20% to 1.20p, revenue compounded £28.0m→£38.8m in two years. Against that: the **Veeuze write-off** — c.€3.45m+ invested from 2018, impaired £2.3m in 2025, disposed for **€1** in April 2026 via a related-party MBO. 1 clear failure in 4–5 deals, and trivial personal ownership. |

**Tally: 0 CONFIRMED · 6 PLAUSIBLE · 2 UNVERIFIED · 2 RED-FLAG**

Zero CONFIRMED is the honest consequence of not reaching a single primary filing. Both RED-FLAGs are accounting/cash-conversion issues that go to the thesis core — per METHOD.md this alone **caps the grade at C or below**, before the asymmetry gate is even applied.

---

## 4. Historical base rate — including the ones that stayed cheap

**Primary evidence (independently verified this session).** I cloned the sibling `rerating-situations-kb` referenced at METHOD.md:141 and counted the rows myself rather than trusting a summary. It logs **561 situations that ≥2x'd within a calendar year, 2018–2025**. Filtering for UK listings returns **exactly 10 (1.8%)**:

| Ticker | Type | Move | Category |
|---|---|---|---|
| PET.L | AIM oil/gas explorer | ~17x | Penny/speculative (KB flags as likely pump) |
| NCYT.L | AIM diagnostics | ~20x | COVID binary |
| SNG.L | AIM biotech | ~25x | Clinical binary (later Ph3 failure) |
| GDR.L | AIM diagnostics | ~2x | COVID binary, round-tripped |
| STX.L | AIM biotech | ~5–6x | FDA approval binary |
| ORPH.L | AIM biotech | ~3x | Reverse-merger platform story |
| ITM.L | LSE hydrogen | ~8–9x | Thematic/policy story |
| CWR.L | LSE fuel cells | ~3.5x | Thematic/policy story |
| AFC.L | AIM hydrogen | ~3–5x | Thematic penny stock |
| RR.L | LSE aero | ~2x | Mega-cap turnaround |

**Not one is a profitable niche B2B software company. Not one re-rated on multiple expansion off good-but-unspectacular organic growth.** Every UK ≥2x in an eight-year census was a binary regulatory/clinical event, a thematic story, or a mega-cap recovery. The KB logs only winners, so it cannot give a denominator — but the **absence of the entire category from the winners' list** is the meaningful signal, and it is the opposite of survivorship bias.

**Named analogs that STAYED CHEAP or re-rated only via takeout:**

- **IDOX plc (AIM)** — the KB's own prior analog, previously cited in the FAA.VI memo as "re-rated 3x (2016–21)." Ending: **taken private by MBO, May 2026, ~120p / ~£530m EV.** The re-rate was ultimately harvested by private equity, not by public shareholders re-rating the multiple.
- **Aptitude Software (APTD.L)** — a *live* stayed-cheap case in this very KB. 2.1x EV/Rev, revenue declining three straight years (£74.4m→£70.0m→£65.0m), ARR declining, strategic review capping any exit at ~1.5–2x revenue. Parked run #56 for asymmetry-gate failure. **This is what Eleco looks like if organic growth stalls.**
- **Instem (AIM)** — range-bound for years, then taken private by ARCHIMED at 833p (Nov 2023), ~41% premium to a 590p undisturbed price the board had already rejected multiple approaches against since March 2023. Cheap-then-takeout, not cheap-then-re-rate.
- **Sopheon (AIM)** — innovation-management SaaS; never re-rated as a public stock; acquired by Wellspring, completed February 2024. *(Note: our `KILL-LIST.md` records "Sopheon B.V. buyout, 2023" — the acquirer and date appear to be wrong and should be corrected.)*
- **Diaceutics, Ebiquity, GlobalData** — the DXRX.L memo's failure set: range-bound 2021–2024 despite growth. **Craneware re-rated and then de-rated hard.**
- **Ideagen** — the apparent counter-example, and it isn't one. Hg paid 350p / ~£1.09bn EV = **11.2x EV/Revenue** (April 2022). But the *undisturbed* price of 230p already implied ~7.2–7.4x. **The market re-rated Ideagen first; PE paid a premium on top.** Ideagen was never a 2.15x stock waiting to be discovered.
- **Gresham Technologies** — taken out by STG Partners at ~£147m, roughly **8–9x ARR** (Q3 2024). Eleco trades at **2.5x ARR**. That gap is the bull case's best single number — and also a warning, because Gresham's Clareti was higher-growth, higher-quality fintech ARR with disclosed retention.

**Base rate: UK AIM vertical B2B software re-rated ~1 of 6 as a public stock over five years; where a ≥2x was actually realised, it came via TAKEOVER, not market repricing. Swing factor = demonstrated cash conversion, not the revenue or ARR growth headline.**

That swing factor is not a generic caution — it is the exact variable on which Eleco currently fails.

---

## 5. Risk Profile

**Single load-bearing assumption.** That Eleco's reported ARR converts to cash at software-like rates. Everything cheap about the stock is downstream of it. At FY2024 conversion (116% OCF/EBITDA) the stock is genuinely inexpensive; at FY2025 conversion (50%) it is 21x EV/FCF for 11% organic growth, which is roughly fair value.

**Clean operating earnings, and what they are actually worth.** Strip the adjustments and the disposal: continuing revenue **£35.1m**, "EBITDA after impairment" **£6.9m** (*down* from £7.2m), statutory operating profit **£2.8m** (−32%), FCF **~£4.1m**. Against a true EV of **~£86.1m** (H1 cash £15.4m less ~£2.2m earn-outs), that is **12.5x EV/EBITDA-after-impairment and 21x EV/FCF**. A software business growing organically at 11% with sub-40 Rule-of-40 deserves roughly 2.5–3.5x revenue. **Fair value ≈ 3.0–3.5x FY2026E revenue of ~£40.4m = EV £121–141m + £13.2m net cash = £134–155m = 160–184p.** That is **+36% to +56%** from ~117.5p — real, but **not a 2x**.

**Informative trigger.** September 2026 H1 full results. Read three lines only: (1) H1 OCF vs H1 2025 and OCF/adj-EBITDA; (2) the deferred income / contract liabilities balance vs ARR growth; (3) capitalised development expenditure, and OCF after deducting it. Everything else in that print is noise for this thesis.

**Moat durability.** 3yr **4/5** (workflow, training and file-format lock-in in UK contractor scheduling is real). 5yr **3/5** (platform bundling by Autodesk/Trimble/Procore/Nemetschek; no regulatory barrier anywhere). 10yr **2/5** (scheduling and takeoff are among the most AI-automatable tasks in AEC; the moat is a lagging asset).

**Revenue-quality decomposition.** 85% "recurring" splits into: core annual licence/subscription renewals on largely desktop products (the majority, decent quality but annual-renewal rather than multi-year cloud); PEMAC ~£2.2m of **UNVERIFIED** SaaS-vs-on-prem-maintenance mix; Kivue ~£1.5m of genuine cloud but at a 13% EBITDA margin implying heavy implementation content; Vertical Digital, which is a captive dev shop and not ARR at all; and ~19% outright non-recurring. Retention is **not disclosed in any year**. Organic ARR growth (~20%) exceeds organic revenue growth (11%) by ~9 points — a wedge that must close now that TRR is 85% of revenue, and whose direction of closure is the open question.

**The one disclosure that would flip it.** The **deferred income / contract liabilities balance** in the FY2025 accounts, alongside the working-capital lines of the cash-flow statement. If deferred income grew in line with the 29% ARR increase, the OCF decline is benign timing and this memo is too harsh — upgrade toward C/CANDIDATE immediately. If deferred income is flat or down while ARR is "+29%", the ARR metric is not converting into billings, adjusted EBITDA is an artefact, and the correct grade is D with a lower target. **One line of one note decides it, and I could not reach it.**

**Return if nothing re-rates.** FCF yield ~4.1%; dividend yield ~1.0% (1.20p at 117.5p). If organic revenue compounds at 11% with stable margins and *cash conversion normalises*, adjusted EPS grows ~10–12%/yr and a flat multiple returns **~12–14%/yr** — a perfectly acceptable compounder. **If cash conversion stays at 40%, the owner's real return is the ~4% FCF yield plus whatever growth actually reaches cash — call it 5–7%/yr.** The spread between those two outcomes is precisely the unread disclosure above. You are not being paid to guess which.

---

## 6. Q / F / R / C

**Q — Business Quality: 3/5**
For: 89.6% gross margin, stable across three years; TRR 81%→85% of revenue; revenue compounded £28.0m→£38.8m in two years; organic ARR +23% at H1 2026; net cash, zero debt; dividend +20%; a genuine 20-year franchise position in UK contractor scheduling; modest dilution (~0.5%/yr, no placings or converts).
Against: organic *revenue* growth only 11%; cash conversion halved (FCF/adj-EBITDA 82%→40%); statutory operating profit **−32%**; "EBITDA after impairment" *fell* YoY; both software acquisitions are margin-dilutive (22% and 13% vs group 26.3%); retention never disclosed; the Veeuze write-off is a documented capital-allocation failure (c.€3.45m+ in, €1 out); insider ownership trivial (CEO 0.34%, CFO 0.08%); the moat is workflow lock-in with no regulatory component.
Solid and defensible — not a franchise compounder. **Q=3, and therefore not eligible for the Quality Bench (which requires Q≥4).**

**F — Downside Floor: 4/5**
For: ~£13.2m of genuinely deployable net cash after earn-outs (~13% of market cap); zero debt; profitable on both statutory and adjusted bases; 85% recurring revenue means trough earnings power is real, not cyclical; dividend covered ~4x by FCF; a credible takeout floor at 2–3x recurring revenue given the IDOX/Sopheon/Instem/Gresham precedent set.
Against: the floor is earnings-based, not asset-based — the balance sheet is goodwill-heavy after four acquisitions, and the Veeuze impairment is proof that this goodwill is impairable; stated net cash is ~19% softer than headlined; £131k/day liquidity means exiting into weakness is costly.
**F=4.**

**R — Re-Rate Likelihood: 2/5**
The scout's R rested on a catalyst that had **already fired** (~21–22 July 2026) with good numbers and no price response, and on a coverage void that is a 20-year structural equilibrium enforced by £131k/day of liquidity, not a temporary condition. The 218p consensus is house-broker and issuer-financed research, stale at a 130p share price, unrevised through both beats and a 35% de-rating, and pitched 19.5% above the 52-week high. The base rate is stark: 561 logged ≥2x re-raters, 10 UK-listed, zero profitable B2B software; UK AIM vertical software re-rates via takeout, not repricing.
Not 1/5, because two real mechanisms remain: a **dated** September H1 print that genuinely tests the load-bearing variable, and a **precedented** takeout path (Gresham went at 8–9x ARR against Eleco's 2.5x). But the print cannot deliver a 2x and its expected sign is neutral-to-negative, and the takeout is undated — which METHOD.md explicitly does not credit.
**R=2.**

**C — Confidence / Data Quality: 2/5 (hard-capped)**
Every finance and company domain returned `connect_rejected — policy denial` at the egress proxy; `snapshot.py` returned `price: None`; the WebSearch budget was exhausted at 200/200. **Zero primary filings opened.** Every figure is secondary. The scout brief contained at least six material errors that this pass identified (Veeuze impairment 74% overstated; Veeuze "acquired" when it was internally formed; catalyst timing wrong by two months in the wrong direction; broker identity wrong; two flagship products misattributed; statutory vs adjusted operating profit conflated in our own baseline file). The £3.3m adjusted-EBITDA bridge is only £2.3m explained. Retention, customer concentration, capitalised development and deferred income are all unread.
`fin_check.py` returns "all checks reconcile AND floor-critical figures are filing-anchored" — but METHOD.md's anchor discipline is explicit that internal consistency ≠ truth, and the provenance tags were inherited from a prior session's scrape, not established by me. **C=2.**

---

## 7. Asymmetry Gate and disposition

| Gate test | Result |
|---|---|
| 1. Materially below defensible fair value at the live price? | **MARGINAL** — ~117.5p vs 160–184p defensible FV. Real, but the 218p anchor is discredited. |
| 2. Realistic bull case ≥2x? | **FAIL** — best supported case +36–56%. A 2x (236p) needs ~4.6x EV/Rev, above every AIM precedent except Ideagen, which was already re-rated before its takeout. |
| 3. Upside meaningfully exceeds downside? | **MARGINAL PASS** — +36–56% up vs −24% to ~90p (or −32% to ~80p if cash conversion disappoints in September). |
| 4. Discrete dated catalyst, OR CORE-grade quality (Q≥4 & F≥4)? | **FAIL** — the September print is dated but cannot deliver 2x; the takeout is undated. Q=3, so no CORE-grade standalone quality. |

**Gate fails on magnitude and trigger.** Per METHOD.md, a gate failure routes to Quality Bench only if **Q≥4** with a durable moat. Q=3 and the moat has no regulatory component. **Therefore: PARK, with a named revisit trigger.**

This is a **PARK on price, catalyst and data quality — not on business quality.** Eleco is a real, profitable, cash-generative software company with a defensible niche. It is simply not offering a 2x at 117.5p, its stated catalyst has already been spent, its analyst anchor is company-financed, and its most important financial question is unanswered.

---

```
GRADE: D  ·  TIER: PARK
Q 3/5 · F 4/5 · R 2/5 · C 2/5

Downgrade from scout 10/12 QUEUED_HOT. Three reasons: (1) cash conversion halved —
OCF/adj-EBITDA 116%→50%, FCF/adj-EBITDA 82%→40% — and the explanation in our own
financials/ELCO.L.md ("PEMAC acquisition outflow") is an accounting error, since
acquisition consideration is an investing not an operating outflow; (2) the stated
catalyst ALREADY FIRED ~21-22 Jul 2026 (H1 update: organic ARR +23%, TRR 85%, record
recurring revenue) and the stock sits at ~117.5p in the lower third of its 102.5-182.5p
range — good news printed, no re-rate; (3) the 218p consensus is house-broker
(Cavendish = NOMAD AND broker = ex-finnCap, merged with Cenkos) plus issuer-financed
research (Equity Development, "not deemed to be independent as defined by the FCA"),
written at a 130p share price, never revised, and pitched 19.5% ABOVE the 52-week high.

Financial baseline: Rev £28.0m (FY23) → £32.4m (FY24) → £38.8m (FY25, +20% reported /
  +19% cc / +11% ORGANIC); continuing revenue ex-Veeuze £35.1m · GM 89.6% (stable, but
  flattered by capitalised development in intangibles) · adj EBITDA £10.2m (26.3%) vs
  "EBITDA after impairment" £6.9m (DOWN from £7.2m) · statutory operating profit £2.8m
  (−32%) · statutory PBT £2.8m (−35%) · statutory NI £1.3m · adj NI £5.2m · Veeuze
  impairment £2.3m (NOT the £4m in the scout brief) · cash £16.3m FY25 / £15.4m H1-26,
  £0 debt, LESS ~£2.2m PEMAC+Vertical Digital earn-outs = ~£13.2m deployable ·
  shares 84,139,760 (+~0.5% incl. Kivue consideration shares; options 4.3%) ·
  OCF £5.06m (from £8.96m) · FCF ~£4.1m · dividend 1.20p (+20%) ≈ £1.0m ·
  mktcap ~£99.3m @117.5p · TRUE EV ~£86.1m · EV/Rev 2.45x on continuing revenue
  (not the 2.15x scouted) · EV/ARR 2.5x · EV/adj EBITDA 8.4x · EV/FCF 21.0x ·
  P/E adj 19.1x · P/E stat 76x · Rule of 40 = 37.3 (21.6 on FCF).
  [Source: FY2025 Final Results RNS 28 Apr 2026 + H1 update ~21-22 Jul 2026, both
   accessed ONLY via secondary summaries; financials/ELCO.L.md — which contains at
   least two errors this memo corrects]

Financials verified against primary filing: NO — every finance/company domain returned
  `connect_rejected: policy denial` at the egress proxy (investegate, LSE, eleco.com,
  Stockopedia, Yahoo, all search engines); snapshot.py returned price: None; WebSearch
  budget exhausted 200/200. ZERO primary filings opened. C hard-capped at 2 per METHOD.md.

Base rate: "UK AIM vertical B2B software re-rated ~1 of 6 as a public stock over 5 years;
  where a >=2x was realised it came via TAKEOVER, not market repricing; swing factor =
  demonstrated CASH CONVERSION, not the revenue/ARR growth headline." Independently
  verified in the sibling rerating-situations-kb: of 561 logged >=2x re-raters 2018-2025,
  only 10 are UK-listed (1.8%) — PET.L, NCYT.L, SNG.L, GDR.L, STX.L, ORPH.L, ITM.L,
  CWR.L, AFC.L, RR.L — and NOT ONE is a profitable niche B2B software company; all are
  clinical/regulatory binaries, thematic story stocks, or a mega-cap turnaround.
  Stayed-cheap / takeout-only set: IDOX (MBO May 2026), Aptitude APTD.L (live, PARKed),
  Instem (range-bound then ARCHIMED 833p), Sopheon (never re-rated, Wellspring Feb 2024),
  Diaceutics/Ebiquity/GlobalData (range-bound), Craneware (re-rated then de-rated hard).
  Ideagen is NOT a counter-example: undisturbed 230p already implied ~7.2x EV/Rev.

Skeptic's checklist: 0 CONFIRMED, 6 PLAUSIBLE, 2 UNVERIFIED, 2 RED-FLAG
  RED-FLAGs (both thesis-core, both capping the grade at C or below):
    #1 revenue-recognition/cash-conversion — ARR +29% while OCF −44%, unexplained
    #7 accounting quality — £3.3m adj-EBITDA bridge only £2.3m identified; statutory
       operating profit −32% while adjusted EBITDA +32%
  UNVERIFIED: #2 retention (no churn/GRR/NRR disclosed in ANY year — peer TRB.L
    discloses 95% GRR / 108% NRR); #5 customer concentration (not disclosed)

Open questions (what would raise C): (1) deferred income / contract liabilities balance
  FY2025 vs FY2024 — THE single load-bearing unread number; (2) full working-capital
  lines of the FY2025 cash-flow statement; (3) capitalised development expenditure and
  its amortisation charge; (4) the ~£1.0m of adjusting items unexplained in the £3.3m
  bridge; (5) gross/net revenue retention; (6) PEMAC's true cloud-SaaS vs on-prem-
  licence-plus-maintenance split; (7) customer concentration; (8) confirmation of
  Eleco's actual product list (the scout brief attributes PlanSwift and Archidata to
  Eleco — they appear to belong to ConstructConnect/Roper and a Canadian firm
  respectively — while omitting the flagship, Asta Powerproject).

Buy-zone / upgrade trigger / downgrade trigger:
  BUY-ZONE: <=90-95p (below the 102.5p 52-wk low) — the only price at which a genuine
    2x to the 160-184p defensible fair value exists. Do NOT buy at 117.5p on the 218p
    "consensus"; that number is company-financed and stale.
  UPGRADE to C / CANDIDATE: September 2026 H1 full results show OCF/adj-EBITDA back
    above ~85% AND deferred income growing at least in line with ARR AND organic ARR
    growth >=20% sustained. Any credible bid approach or strategic review also upgrades.
  DOWNGRADE / abandon: H1 OCF conversion stays below ~60%, OR deferred income flat/down
    against "+29% ARR", OR organic revenue growth decelerates below ~8%, OR FY2026
    reported revenue lands below ~£39m (the Veeuze disposal alone cuts ~£3.7m, so
    FY2026 reported growth should be only ~+4% — see the bridge below; a miss on that
    already-low bar means organic growth has stalled).

Asymmetry-to-risk in one sentence: A genuinely good 89.6%-gross-margin niche software
  business whose entire "cheap" case (8.4x EV/EBITDA) evaporates on the cash-flow
  statement (21x EV/FCF, conversion halved to 40% and unexplained), whose stated
  catalyst already fired four days ago to complete market indifference, and whose 84%
  "upside to consensus" is a stale target written by the company's own paid NOMAD —
  leaving roughly +36-56% of defensible upside against -24-32% of downside, which is
  a fair-value stock, not an asymmetric one.

FY2026 revenue bridge (why the growth optics get worse before better):
  £38.8m FY25 − £3.7m Veeuze (disposed, effective 1 Jan 2026) = £35.1m continuing
  + ~£1.4m Kivue (11 months) + ~11% organic on £35.1m = ~£40.4m => reported growth
  only ~+4%, down from +20%. A serial acquirer's narrative rarely survives a
  deceleration from +20% to +4% headline, however sound the organic number beneath it.

HUMAN VERIFICATION CHECKLIST (before any capital):
  - THE DECIDER: open the FY2025 Annual Report cash-flow statement and the deferred
    income / contract liabilities note. If deferred income grew ~in line with the 29%
    ARR increase, the OCF collapse is benign timing and this memo is too harsh — upgrade
    on the spot. If it is flat or down, ARR is not converting to billings and the
    grade should stay D. This single note decides the name.
  - Confirm the analyst position independently: pull the eleco.com AIM Rule 26 page to
    verify Cavendish is sole NOMAD+broker with no independent joint broker, and obtain a
    broker-by-broker target table (Refinitiv/Bloomberg/Research Tree) to establish who
    owns the 176p / 200p / 250p points. If 200p is Equity Development or Progressive,
    the 218p "consensus" is 100% issuer-financed and must be discarded outright.
  - Verify the corrected product list — specifically that Asta Powerproject is the
    flagship and that PlanSwift/Archidata are NOT Eleco products. The scout's entire
    moat and competitive analysis was written about products the company may not own.
  - Confirm the earn-out treatment: are the PEMAC (up to EUR 2.4m, 2026-27) and Vertical
    Digital (up to EUR 250k, 2026) contingent liabilities carried on balance sheet, and
    is the headline £16.3m "net cash" struck BEFORE deducting them? This is ~19% of the
    stated floor.
  - Re-check the live price on an unrestricted connection (snapshot.py returned None;
    best available print is 117.50p bid 116/offer 119 on 3 Jul 2026) and confirm
    liquidity before sizing — ~111,325 shares/day (~£131k) at a ~2.55% spread means a
    £1m position is ~8 days of full ADV.
```
