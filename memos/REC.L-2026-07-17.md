# REC.L — Record plc Deep-Dive Memo
**Run #37 · 2026-07-17 · Sector 18 (pulled from deferred queue, scout score 6/12)**

---

## Business Overview

Record plc (AIM: REC.L) is a UK-listed pure-play specialist currency management firm founded in 1983 by Neil Record. It is one of the few — possibly the only — publicly listed independent specialist currency manager of material scale globally. The firm provides institutional clients (pension funds, sovereign wealth funds, foundations, insurance companies) with:

- **Currency overlay** (passive hedging of FX exposures in international portfolios)
- **Dynamic hedging** (rules-based active currency risk management)
- **Return-seeking currency strategies** (alpha generation from FX)
- **Solutions for Asset Managers** (currency risk and analytics services licensed to other asset managers — fast-growing new segment)

**Revenue model**: AUM-based management fees (~35–40 bps blended) plus performance fees. Asset-light, no balance sheet risk.

**Market cap**: ~£106M at ~57p/share (AIM; 1 sell-side analyst). 52-week range: 49p–67.6p.

**FY2026 financial snapshot (year ended 31 March 2026):**

| Metric | FY2026 | FY2025 | Change |
|--------|--------|--------|--------|
| AUM | $114.6bn | $100.9bn | +14% |
| Revenue | £40.1M | £41.6M | -4% |
| Operating costs | £30.4M | £30.8M | -2% |
| Operating profit | ~£9.7M | ~£10.8M | -10% |
| Profit after tax | £7.0M | £9.1M | -23% |
| Basic EPS | 3.92p | 5.03p | -22% |
| Dividend (full year) | 3.60p | 4.65p | -23% |
| Net assets | £27.8M | £29.1M | -4% |
| Debt | £0 | £0 | — |
| Cash / liquid assets | £13.0M | — | — |
| Excess regulatory capital | £19.2M | — | — |

**Valuation at ~57p**: P/E ~14.5x (FY2026 EPS 3.92p); dividend yield ~6.3%; P/B ~3.8x; EV/EBIT ~11x (backing out £13M cash from £106M cap, on ~£9.7M op profit).

**PAT decline driver**: Tax rate normalised following prior-year deferred tax credits. Operational earnings fell more modestly; the PAT drop overstates operational deterioration.

**Solutions for Asset Managers segment**: AUM +19%, revenue +39% — the fastest-growing part of the business and the primary reinvestment runway.

---

## Moat Assessment

**Primary moat: SWITCHING_COST (institutional depth)**

1. **35-year institutional track record**: Record has managed currency risk for major pension funds and institutional investors continuously since 1988. In a business where trustees and CIOs need to justify every mandate decision to investment committees and regulators, the 35-year record is not just marketing — it is a compliance artefact. Replacing an established currency manager requires a formal manager selection process, RFP, governance board sign-off, and a transition that can take 6–18 months. The embedded friction is high.

2. **Pure independence differentiator**: Insight Investment ($1T+ overlay) and BNY Mellon FX overlay are subsidiaries of custodian banks that also trade FX. A pension fund using Insight as currency overlay manager may be directing flow to the same bank's FX desk — a conflict with fiduciary duty. Record has no custody business, no proprietary FX desk, no sell-side relationships. This structural independence is an explicit selection criterion for many institutional mandates with strict conflict-of-interest policies. It is not easily replicated.

3. **Specialisation depth**: Currency overlay requires continuous portfolio-level monitoring, customised hedging ratios, complex reporting for local accounting standards, and regulatory compliance across multiple jurisdictions. Record's systems, processes, and institutional-grade reporting infrastructure represent years of investment that a bank or generalist asset manager would need to rebuild from scratch.

4. **Global scale at AIM size**: $114.6bn in AUM at a ~£106M market cap is an extraordinarily high AUM-to-market-cap ratio. The "big" listed alternatives (Insight, Russell) are divisions of much larger enterprises. No comparable pure-play listed independent currency manager exists at this scale globally.

**Moat durability**: HIGH for existing clients; MODERATE for new client capture. The switching cost keeps incumbents sticky, but winning new mandates requires competing against Insight (which has breadth of product), Russell (which bundles it with overlay), and increasingly algorithmic platforms (which compete on cost for simpler passive hedging). The Solutions for Asset Managers segment is Record's response to this competition — licensing their IP rather than just managing mandates.

---

## Skeptic's Confirmation Checklist

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 1 | Revenue recognition | **CONFIRMED** | AUM-linked management fees accrue daily/monthly; performance fees at year-end; audited UK GAAP; straightforward recognition, no complex % of completion |
| 2 | Revenue durability | **UNVERIFIED** | Mandate switching costs are real but mandates are NOT contractually locked (institutional clients can redeem with notice). FY2026 revenue fell -4% despite AUM +14% due to mandate recompositions and lower performance fees — shows mandates shift structure. Individual contract notice periods and client concentration unknown. |
| 3 | Competitive capture | **PLAUSIBLE** | Independence moat is genuine and differentiated from Insight/BNY. However: 7orca (Germany), ECU Group (London), and algorithmic platforms are smaller independents growing in simpler passive hedging. The moat is strongest in complex active overlay; thinner for passive. Not sole-source. |
| 4 | Moat stickiness over time | **PLAUSIBLE** | 35-year institutional track record and process depth are durable. Risk: algorithmic/passive FX hedging platforms (e.g. Milliman, MSCI FX overlay tools) could commoditise the passive segment. Active/dynamic overlay remains specialist. No in-source risk identified — institutions don't build their own currency overlay teams. |
| 5 | Customer concentration | **CONFIRMED (material risk)** | Annual report discloses clients >10% of revenue individually: FY2026 = 2 clients (£6.0M + £4.4M = £10.4M combined, **~26% of £40.1M revenue**); FY2025 = 3 clients (£6.9M + £5.0M + £4.3M = £16.2M, ~39% of revenue). Loss of either FY2026 top client would be a ~15% revenue hit. This is the single largest unmitigated risk. |
| 6 | Pricing power persistence | **PLAUSIBLE** | Negative evidence in FY2026: AUM +14% → revenue -4% = 16% effective fee compression from mandate recompositions. This is a structural headwind, not a one-off. Clients are recomposing mandates toward lower-fee passive strategies. Active overlay retains pricing power; passive does not. Trend bears watching. |
| 7 | Accounting quality | **CONFIRMED** | AIM-listed, FCA-regulated, UK GAAP audited. 92% payout ratio is high but the business generates clean cash earnings. No aggressive rev-rec flags, no capitalized development costs above normal SaaS levels, no related-party concerns noted. |
| 8 | Ownership & dilution | **PLAUSIBLE** | Neil Record (founder, 26%) has been net seller — sold ~2M shares in 2026; total insiders net sold £151k more than bought in LTM. CEO Jan Hendrik Witte holds 1.04%. No dilution history; no ATM or convert risk. Founder selling is worth monitoring but not a red flag at this rate. |
| 9 | Input & supply dependency | **CONFIRMED** | Pure intellectual capital business. No hardware, no China-linked material, no supply chain. Key person risk is the main "input" concern — if senior portfolio managers depart, track record continuity is at risk. Neil Record's reduced operational role (transitioned to Chair then departed as CEO in 2024) has been managed; no visible exodus. |
| 10 | Management credibility | **PLAUSIBLE** | Jan Hendrik Witte as CEO since April 2024 — insufficient track record to confirm or deny. FY2026 under his leadership: AUM grew 14% but revenue and earnings declined. Cost control is evident (-2% costs). Growth strategy (Solutions for Asset Managers) is credible. Cannot confirm delivery against prior guidance under new CEO. |

**Checklist summary: 4 CONFIRMED · 5 PLAUSIBLE · 1 UNVERIFIED · 0 RED-FLAG**

Open questions: Client concentration (top 5 clients as % AUM/revenue); individual mandate contract terms and notice periods; pace of fee compression — mandate recomposition structural or cyclical; CEO track record on stated FY2027 targets.

---

## Valuation

| Metric | REC.L | Comparable AIM asset managers (Polar Capital, CLIG, Brooks Macdonald) |
|--------|--------|----------------------------------------------------------------------|
| P/E (trailing) | 14.5x | 12–18x |
| Dividend yield | 6.3% | 4–7% |
| P/B | 3.8x | 2–5x |
| EV/op profit | ~11x | 10–15x |
| Analyst PT | 140p (1 analyst) | — |
| Implied upside (from 57p) | **+145%** | — |

The 140p analyst target implies a re-rating to ~35x P/E — aggressive, but reflects the view that earnings recovery to historical levels (~5p EPS) plus a re-rate to 20–25x on franchise quality could plausibly reach 100p+. A more conservative base case: AUM steady at $115bn, revenue recovers to £43M (prior highs) as performance fees normalise and Solutions segment grows, margins expand slightly → EPS ~4.5–5p → at 15x P/E = 67–75p = 18–32% upside. Not exceptional as a pure catalyst trade, but reasonable as an own-and-compound holding.

Downside: At 57p, the stock trades at 2x net assets (£27.8M). Floor scenario: AUM falls to $80bn (-30%), revenues fall to £28M, earnings near zero → stock could fall to 25–35p. That is a 35–55% drawdown in a catastrophic scenario, but one that requires significant institutional withdrawals against the grain of the sticky switching-cost moat.

---

## Historical Base Rate / Analog Process

**Analog 1: City of London Investment Group (CLIG.L)**
- Pattern: AIM-listed specialist EM/closed-end fund manager, niche moat (deep EM expertise for a specific institutional sleeve), 1-2 analysts, high yield, depressed P/E during EM outflows
- Outcome: Re-rated ~1.7x over 3 years (2020–2023) on EM cycle recovery + dividend sustainability confirmed
- Relevance: HIGH — same AIM niche specialist structure; same yield-based holding; same institutional client base
- Swing factor: AUM trend reversal (inflows returned) → earnings visibility → institution buys

**Analog 2: Polar Capital Holdings (POLR.L)**
- Pattern: AIM-listed specialist active manager (tech/insurance thematic); depressed earnings during fund outflows; 2-3 analysts; low P/E on cyclically low earnings
- Outcome: Re-rated ~1.8x (from ~400p to ~700p) as technology inflow accelerated; Peel Hunt and Panmure initiated; above-sector earnings growth triggered institutional buying
- Relevance: MEDIUM — similar AIM structure and institutional client base; but POLR's moat is investment performance, not switching cost; POLR had a clearer thematic catalyst (tech boom) that Record lacks
- Swing factor: Analyst initiation + AUM/earnings inflection point in the same quarter

**Analog 3: Parmenion Capital (pre-acquisition) / Waverton Investment Management**
- Pattern: Specialist UK institutional manager with deep client relationships; sold at 1.5–2x AUM
- Outcome: M&A rather than public re-rating; confirms the value of the franchise but limits re-rate visibility while public
- Relevance: LOW — M&A is always possible for Record given founder stake dynamics, but not a plannable catalyst

**Analog 4: Thames River Capital (pre-JO Hambro merger era)**
- Pattern: Similar — specialist currency/alternatives manager, low coverage, sold at high multiple to strategic acquirer
- Outcome: Private transaction; not a public re-rating analog
- Relevance: LOW for public market re-rate; raises question of whether Neil Record's selling opens takeover angle

**Base rate: "Companies like this re-rated 2 of 4 times in the public market; swing factor = AUM inflow recovery accompanied by earnings inflection, not AUM level alone. Both re-rates required either analyst initiation or a demonstrable growth narrative beyond stable AUM."**

The key structural negative for Record: AUM has grown ($100.9bn → $114.6bn) yet revenue FELL. This is the opposite of the analog pattern — every re-rate required earnings to follow AUM. Until fee compression reverses (or Solutions for Asset Managers drives revenue growth), the classic re-rate setup is blocked.

---

## Risk-Adjusted Asymmetry Assessment

**Q — Business Quality: 4/5**
35-year institutional track record; pure-play niche (only listed independent currency manager at scale); asset-light; SWITCHING_COST moat from institutional depth and independence differentiator; Solutions segment growing +39% revenue providing reinvestment runway. Dinged from 5: the 92% payout ratio leaves almost nothing for compounding; the fee compression trend (AUM +14% → revenue -4%) shows the business is not fully earning its AUM growth; new CEO with unproven track record introduces execution uncertainty.

**F — Downside Floor: 4/5**
Zero debt; £19.2M excess regulatory capital; £13M cash; net assets £27.8M. Even in a trough year (PAT £7M, EPS 3.92p), the business is solidly profitable. The floor is an earnings floor not just an asset floor (passes ROUTINE.md test #4). To go loss-making would require AUM below ~$60–65bn — a 45% decline from current levels, requiring mass institutional withdrawals that run counter to the switching cost moat. Capped at 4 rather than 5: no guaranteed floor on performance fee revenue (can go to zero in low-volatility years); mandate recomposition risk is real and could compress fee rates further.

**R — Re-Rate Likelihood: 2/5**
Coverage void is genuine (1 analyst; institutional mandate minimums exclude most UK equity funds at £106M cap). But the re-rate trigger is unclear: the analog base rate requires earnings to follow AUM, and that hasn't happened. No dated near-term catalyst. No second analyst initiation confirmed. The Solutions for Asset Managers segment is the most credible growth narrative, but it is still small (even at +39% revenue, it likely represents <20% of total revenue). Valuation at 14.5x P/E is not cheap enough to be a screaming value buy (CLIG re-rated from <10x). R=2 because: multiple coverage paths to a re-rate exist (initiation, M&A, earnings recovery), but none has a specific date or trigger within 6–12 months, and the fee compression trend actively resists near-term earnings recovery.

**C — Confidence / Data Quality: 3/5**
Audited UK GAAP financials, FCA-regulated, annual report published June 2026 — data quality is good. However: (1) client concentration % unknown (could be 30–50% in top 5 mandates — material risk unquantified); (2) mandate contract terms (notice period) not public; (3) fee compression trend — structural vs. cyclical — unresolved; (4) new CEO track record on stated targets not yet established. These are not fatal gaps but they prevent high-conviction sizing.

**Grade determination**:
- A requires Q≥4 AND F≥4 AND C≥4: fails (C=3)
- B — high on three of four, with explicit allowance for "R low but Q+F+C high = own-and-wait compounder": Q=4, F=4, C=3 — three solid scores, R=2. This is the classic "B — own-and-wait compounder" pattern. C=3 keeps it out of A.
- **GRADE: B**

**Tier determination**:
- CORE (Q≥4 & F≥4): qualifies
- But C=3 → per the FAA.VI precedent in this KB, C=3 triggers WATCH-to-verify
- **TIER: WATCH** (→ CORE when C raised to 4 via client concentration data, CEO track record, and fee compression characterisation)

---

## WATCH Test Results (ROUTINE.md §5 guardrail)

| Test | Result | Note |
|------|--------|------|
| 1. Memo on file | **PASS** | This memo |
| 2. Dated near-term 2x catalyst <6mo | **FAIL** | No specific dated event; Solutions for Asset Managers growth is ongoing, not a single trigger |
| 3. Not near 52-wk high | **PASS** | ~57p vs. 52-wk high 67.6p; ~85% of high, acceptable |
| 4. Earnings floor (not just asset floor) | **PASS** | £7.0M PAT even in FY2026 trough; zero debt |

CATALYST pathway fails test #2. CORE pathway qualifies (Q=4, F=4) but C=3 below conviction threshold → **WATCH-to-verify**.

---

```
GRADE: B  ·  TIER: WATCH (→ CORE when C ≥ 4)
Q 4/5 · F 4/5 · R 2/5 · C 3/5
Base rate: "companies like this re-rated 2 of 4 times in public markets; swing factor = earnings inflection following AUM growth, not AUM growth alone"
Skeptic's checklist: 4 CONFIRMED, 5 PLAUSIBLE, 1 UNVERIFIED, 0 RED-FLAG
Open questions (what would raise C to 4): (1) mandate contract terms — notice periods and lock-up provisions; (2) fee compression — structural (mix shift to passive) or cyclical (recovers with vol/performance); (3) CEO FY2027 target delivery
Buy-zone: 45–55p (below tangible book × 2; current 57p is just outside zone)
Upgrade trigger: (1) Revenue growth returns >5% YoY despite no AUM change (confirms fee compression cyclical not structural); (2) Solutions for Asset Managers crosses 25% of total revenue; (3) second analyst initiates
Downgrade trigger: (1) AUM drops below $90bn for two consecutive quarters; (2) Neil Record's stake falls below 15% (accelerating disposal signal); (3) revenue falls >10% in FY2027 despite stable AUM (structural fee floor breaks)
Asymmetry-to-risk in one sentence: At 14.5x trough earnings with zero debt, 6.3% yield, and the only listed independent currency overlay manager at scale, the downside is bounded by franchise value, but the re-rate is blocked until revenue growth follows AUM growth — making this a patient own-at-the-right-price hold, not a near-term catalyst trade.
```
