# COVERAGE — the denominator, and how much of it we've seen

The point of the top-of-funnel rework: stop *hoping* web search surfaces names, and instead **enumerate a known universe and march through it best-first**, so we can answer "what % of the worthwhile microcaps have we actually looked at?"

## The worthwhile universe (the denominator)

**US — fully enumerable via SEC frames (`tools/screen.py`, deterministic, ~4 API calls, zero LLM):**
- All filers reporting revenue: ~4,200
- Worthwhile subset — revenue $20–400M, gross margin 45–95%, **profitable**: **~78** (as of CY2025; ~236 if you include cash-burners)
- This is the denominator. Coverage % = (US names deep-reviewed) ÷ 78. **A run that reviews the top-10 unreviewed covers ~13% of the worthwhile US universe.** By a handful of passes we can honestly cover the *majority* of profitable high-margin US microcaps — and know it.
- The screen is ranked by a quality proxy (operating margin, gross margin, capped growth), so we march **best-first** — even partial coverage captures the best names.

**International data sources — VERIFIED (probed 2026-07-18):**

| Market | Bulk source | Key? | Status |
|--------|-------------|------|--------|
| **US** | SEC XBRL `frames` API | none | ✅ built (`screen.py`) |
| **Europe (all EU-regulated exchanges + UK)** | **filings.xbrl.org** — ESEF/UKSEF XBRL index (keyless JSON:API; filing metadata + JSON URLs to the actual statements) | **none** | 🔨 buildable NOW |
| **Taiwan** | **TWSE OpenAPI** (`openapi.twse.com.tw`) — keyless company list (`t187ap03_L`) + financial statements incl. revenue 營業收入 & cost 營業成本 → GM (`t187ap06_L_ci`); + TPEx OTC | **none** | 🔨 buildable NOW |
| **Japan** | **EDINET API v2** — XBRL filings | **free key** (subscription key) | ⏳ needs `EDINET_KEY` |
| **Korea** | **OpenDART** (`opendart.fss.or.kr`) — XBRL financials | **free key** (`crtfc_key`) | ⏳ needs `OPENDART_KEY` |
| **Canada** | mostly via SEC (many TSX names file 40-F/20-F, already in US frames) + per-name Yahoo (.TO) | none | partial |
| **Australia/NZ** | no free bulk fundamentals; per-name Yahoo (.AX/.NZ) | none | per-name |
| **UK (also)** | Companies House API (free key) — but UK already covered by filings.xbrl.org UKSEF | free key | redundant |

**Build order:** Europe (filings.xbrl.org) + Taiwan (TWSE) are keyless → build next. Japan/Korea → build once the free keys are set as env vars in the routine environment. Canada is largely absorbed by the US frames (cross-listed 40-F filers); pure-domestic TSX names go per-name. For any market without bulk fundamentals, the denominator is "all listed in cap band" (exchange list) and we march per-name with `snapshot.py` price + the filing.

## Ledger — reviewed vs. remaining (updated by the routine)

| Universe | Denominator | Reviewed | Coverage % | Cursor (next best-unreviewed) |
|----------|-------------|----------|-----------|-------------------------------|
| US profitable high-GM microcaps | ~78 | 0 | 0% | run `screen.py`, start rank 1 |
| Japan (EDINET) | TBD (needs key) | 0 | — | pending EDINET key |
| Korea (OpenDART) | TBD (needs key) | 0 | — | pending OpenDART key |
| Other exchanges (list-enumerated) | per exchange | — | — | rotate |

*The routine refreshes `screen.py` periodically (the universe drifts as filings update), marks each reviewed CIK in SEEN, and advances the cursor down the ranked worklist. Never re-screen a SEEN ticker.*

## Why this matters
- **Measurable coverage** — we can state "we've reviewed X% of the worthwhile US universe," not "we searched a lot."
- **No wasted re-looks** — SEEN keyed by CIK/ticker; the ranked worklist is marched once.
- **Best-first** — even if we never hit 100%, we've covered the highest-quality names first.
- **Spend shifts to the top** — deterministic enumeration/pre-screen is nearly free; LLM tokens go only to names that already pass the hard numeric gates.
