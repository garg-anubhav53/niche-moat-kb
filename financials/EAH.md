# ECO Animal Health Group plc (EAH.L) — Financial Baseline

**As-of date:** 2026-07-20 · **Source:** Web search (trust: ~, single-source; SEC EDGAR XBRL N/A — UK AIM filer; snapshot.py blocked by proxy 403)
**Ticker:** EAH.L (AIM London) · **ISIN:** GB00B24CCG53
**Sector:** Specialty veterinary pharma (niche antibiotic + parasiticide platform; Aivlosin/tylvalosin flagship)

---

## Income Statement (FY2026 = year ended 31 March 2026)

| Metric | FY2026 | FY2025 | YoY |
|--------|--------|--------|-----|
| Revenue | £87.5M | ~£79.5M | +10% ~ |
| Gross margin | ~49% | ~47-48% | +~1pp ~ |
| Adj EBITDA | £8.5M | ~£7.0M ~ | +21% ~ |
| EBIT (adj) | ~£5.0M ~ | — | — |
| Net income (reported) | ~£3.65M ~ | — | — |
| Net margin | ~4.2% ~ | — | — |

## Balance Sheet (as at 31 March 2026)

| Metric | Value | Trust |
|--------|-------|-------|
| Cash & equivalents | ~£30M ~ | ~ |
| Total debt (gross) | ~£4.6M ~ | ~ |
| Net cash | ~£25.4M ~ | ~ |
| Market cap (at EAH.L ~38.5p · ~153M shares) | ~£58.95M | ~ |
| Enterprise value | ~£33.55M | ~ |

## Valuation Ratios (derived)

| Multiple | Value |
|----------|-------|
| P/S | ~0.67x |
| P/E (on £3.65M NI) | ~16.1x |
| EV/EBITDA (£33.55M / £8.5M) | ~3.9x |

## fin_check.py reconciliation

`snapshot.py` blocked (Yahoo Finance 403). Manual cross-check:
- Market cap = ~38.5p × ~153.1M shares = ~£58.9M ✓ consistent with web search
- EV = £58.9M cap − £25.4M net cash = £33.5M ✓
- EV/EBITDA = £33.5M / £8.5M = 3.9x ✓

Trust: **~ (web-search-sourced, not primary-filing anchored)**. AIM semi-annual results and RNS releases are the primary source; no EDGAR filing available. All figures should be treated as unconfirmed pending primary AIM interim/annual RNS review.

## Business snapshot

- **Product:** Aivlosin (tylvalosin) — prescription-only antibiotic for swine respiratory disease (SRD) and porcine proliferative enteropathy (PPE); poultry mycoplasmosis
- **Moat claimed:** REGULATORY — EPA/EMA-registered veterinary antibiotic with species-specific data packages; 18-24mo re-registration barrier for generics; formulary-embedded in major UK/EU pig/poultry integrators
- **Moat durability concern:** Patent cliff — Aivlosin APIs are increasingly off-patent; generic tylvalosin manufacturers (China-based API suppliers) have entered some EU markets; long-term generic erosion is the central risk
- **Geographic exposure:** UK/EU primary (~60%); US, Asia secondary
- **Customer base:** Veterinary prescription channel; major pig and poultry integrators; distributor relationships (Zoetis/Elanco not direct competition — different drug classes)
- **Analyst coverage:** 2 AIM analysts (per web search, both BUY) → COVERAGE gate: 2 ≤ 4 = PASS
- **Cap zone:** £58.95M = core zone ($20-300M equivalent)

## §4 Promise Score and Verdict

Score: **6/12** (Moat=1, Quality=1, Coverage=2, Valuation=1, Catalyst=0, Floor=1)

- Moat=1: REGULATORY moat is genuine (registration process, data packages) but generic erosion is a confirmed, active threat — not textbook "unbreachable"; IP-protected window is narrowing not widening
- Quality=1: 4.2% net margin is thin; Adj EBITDA 9.7% = below franchise-grade threshold; Revenue +10% but driven partly by geographic mix vs true pricing power
- Coverage=2: 2 analysts = genuine small-cap coverage void; English-language discoverability limited
- Valuation=1: EV/EBITDA ~4x = appears cheap vs sector (peers trade 8-12x) BUT the discount reflects generic erosion risk — "cheap" is potentially a value trap at declining revenues
- Catalyst=0: No identifiable hard-dated ≤6mo catalyst; generic erosion trend is the operative story, not a re-rating event; no new product approval visible
- Floor=1: Net cash £25.4M = floor asset (~43% of cap) but earnings floor is thin and declining, not compounding

**Asymmetry Gate: FAIL**
1. Entry test: EV/EBITDA 4x appears cheap but reflects rightly-discounted declining-moat business — NOT mispriced in the traditional sense
2. Bull ≥2x: No clear bull case to £120M cap without either (a) generic erosion reversing or (b) new product launch
3. Skew: Unfavorable (generic entry = downside, not upside)
4. Trigger: No discrete catalyst; diffuse "analysts might notice the cheapness" = explicitly rejected

**Verdict: PARK 6/12** — cheap on multiples but generic erosion = structural discount, not exploitable mispricing. Q≈1 (thin margin, moat erosion) precludes Bench eligibility (Bench requires Q≥4 + durable moat). Do not deep-dive. REVISIT IF: (a) New regulatory approval for Aivlosin indication (pipeline candidate) + (b) generic erosion demonstrably arrested (≥2 quarters of revenue growth at stable margins) + (c) cap corrects below £40M.
