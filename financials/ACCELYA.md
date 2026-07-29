# NSE:ACCELYA — Accelya Solutions India Ltd. — Financial Baseline

**Date created:** 2026-07-29 (run #97) | **Confidence:** C≤2 ~ (web/aggregator; BSE annual report not retrieved — Indian filing format structurally blocks COGS-based GM computation)
**Source:** Accelya Solutions India Q4 FY2025-26 investor presentation / press release via web aggregator; BSE exchange filings; CMIE/Screener web data

---

## §3.5 Financial Snapshot

| Metric | FY2024-25 | FY2025-26 | Note |
|--------|-----------|-----------|------|
| Revenue (INR crore) | ~390 ~ | ~415 ~ | estimated; filing-confirmed figures pending |
| Operating Profit Q4 FY25-26 (INR crore) | — | 51.19 | Q4 highest-ever op profit; confirmed press release |
| Operating Margin (full year) | ~30.9% ~ | ~30.9% ~ | Confirmed from multiple aggregator sources |
| Net Income | positive ~ | positive ~ | Not separately confirmed; profitable entity |
| Gross Margin | **UNRESOLVABLE** | **UNRESOLVABLE** | Indian Ind-AS "nature-of-expense" P&L format: no COGS line; GM structurally uncomputable from web |
| Shares | ~14.9–15.0M ~ | ~14.9–15.0M ~ | estimated from aggregator; BSE filing required |

**GM gate: PENDING / UNRESOLVABLE** — Indian Ind-AS filings use "nature-of-expense" format (Employee benefits, Depreciation, Other expenses) rather than "function-of-expense" (COGS, Gross Profit). No COGS line exists in web-accessible data. Operating margin 30.9% confirmed but **does not equal gross margin** and cannot be used as a GM proxy.

**NI gate: PROBABLE PASS** (Q4 highest-ever op profit ✓; full-year profitable based on aggregator data; exact NI figure not filing-confirmed)

**Revenue gate: PROBABLE PASS** (INR ~390-415 crore ~= ~$47-50M USD >> $20M floor)

---

## §3.5 Status

**QUEUED_CONDITIONAL — MAINTAINED** (run #92 QUEUED_CONDITIONAL assigned; run #97 2026-07-29 resolution attempt FAILED — structural barrier, not data gap)

**Reason QUEUED_CONDITIONAL:** COGS-based gross margin cannot be computed from web-accessible Indian Ind-AS filings. The "nature-of-expense" P&L format used by Indian listed companies (per Ind-AS 1 / IND-AS Schedule III) does not include a COGS line or gross profit subtotal. Even with direct BSE filing access (PDF annual report), GM computation requires decomposing expense categories (e.g., allocating employee benefits between cost-of-revenue and S&A/R&D) which is impossible from web data alone.

**Next steps to resolve:**
1. Direct BSE annual report PDF download (URL format: `https://www.bseindia.com/bseplus/AnnualReport/<scrip_code>/...`) — may be accessible with direct BSE access outside proxy-blocked environment
2. Alternatively: Management Discussion & Analysis (MD&A) section of BSE annual report sometimes discloses gross margin or service delivery cost breakdowns for SaaS companies
3. If BSE PDF inaccessible: use Annual Report section data disclosed in BSE XBRL structured data filing (BSE XBRL viewer)
4. Cap C at ≤2 until GM confirmed from filing

---

## Stock Price & Capitalization

| | Value | Note |
|---|---|---|
| Price (INR) | ~1,850–1,900 ~ | estimated range (web aggregator; not filing-confirmed) |
| Shares (est.) | ~14.9–15.0M ~ | estimated from aggregator; BSE filing required |
| Market Cap (INR crore) | ~2,750–2,850 ~ | estimated ~$330–340M USD at INR 83/$1 |
| Exchange | NSE / BSE | India; ACCELYA ticker |

---

## Business Description

Accelya Solutions India Ltd. provides airline revenue management and financial settlement software:
- **IATA billing and settlement:** ARC/BSP airline ticketing settlement infrastructure for global airline distribution
- **Revenue accounting:** Passenger revenue accounting, interline billing, and cargo revenue management SaaS
- **NDC distribution:** New Distribution Capability (NDC) offer and order management for modern airline retailing
- **Parent:** Accelya Group (private equity — Vista Equity Partners); Accelya Solutions India is the listed Indian subsidiary

**Moat thesis (§3.5 level — unverified §4):**
1. IATA BSP/ARC settlement infrastructure = quasi-utility for ~250+ airlines; switching requires IATA re-certification of replacement vendor (18–24+ month process)
2. Revenue accounting handles interline proration (sharing revenue across codeshare flights) — requires decades of IATA standards implementation depth; only 3–4 global vendors viable
3. NDC order management = forward-looking regulatory compliance moat (IATA NDC mandates progressively enforced post-2023)
4. Listed Indian subsidiary of Vista PE-backed global platform = Indian entity may have capex-light SaaS margins even if parent has PE leverage

**Risk flags:**
- Vista Equity Partners PE ownership → potential future go-private / delisting risk (⚑PE_OWNED)
- Indian Ind-AS filing format → GM not directly verifiable from web (⚑non-EN filing complexity)
- Small float (~14.9M shares) → liquidity constraint for meaningful position sizing
- Revenue concentration in airline industry → cyclical travel demand exposure

**Exchange:** NSE/BSE (India) | **Filing language:** English (but Ind-AS "nature-of-expense" format) | **Confidence:** C≤2

---

## Run History

| Run | Date | Action | Status |
|-----|------|--------|--------|
| #92 | 2026-07-28 | §3.5 baseline initiated; GM resolution attempted; QUEUED_CONDITIONAL assigned | QUEUED_CONDITIONAL |
| #97 | 2026-07-29 | GM resolution re-attempted; structural barrier confirmed (Ind-AS format); status maintained | QUEUED_CONDITIONAL MAINTAINED |
