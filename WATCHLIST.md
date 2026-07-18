# WATCHLIST — Quality Bench (great businesses, wrong price — buy on the dip)

Durable-moat, high-quality businesses (Q≥4, durable moat, real floor) that **pass every test except price** — they fail the Asymmetry Gate today only because the live price is at/above fair value. We don't discard these like a mediocre PARK; we **keep them and monitor the live price** (cheap, via `tools/snapshot.py`), and the instant the price dips into the buy-zone they promote to a live CANDIDATE for a fresh deep-dive at the new price.

**How a name earns a bench spot (vs. a PARK):** it must be one you'd genuinely *want to own* — the moat is durable (regulatory / process / sole-source that survives years, not a cyclical tailwind), the business compounds or throws off cash, the floor is real. A PARK is "not compelling regardless of price"; a Bench name is "compelling, just not at this price."

**Monitoring:** on each §7 REFLECT run, re-price the bench with `snapshot.py`; update `Last price`; if a name has dipped to/through its **Buy-zone**, move it to the shortlist as `QUEUED_HOT` (deep-dive at the new price) and note the trigger fired.

| Ticker | Company | Business · why the moat is durable | Quality | Fair value ref | **Buy-zone (promote trigger)** | Last price (as-of) | Added |
|--------|---------|-----------------------------------|---------|----------------|-------------------------------|--------------------|-------|
| WINA | Winmark | Franchise-royalty model (Play It Again Sports, Once Upon A Child) — asset-light, ~90% royalty margins, negative working capital, decades of durability | Very high (Q5/F4) | ~31x PE now | **≤ ~20–22x PE** (a real growth/market pullback) | — | 2026-07-18 |
| CODA | Coda Octopus | Patented Echoscope real-time 3D sonar — sole product, 15 yrs no replication; net cash, 66% GM | High (Q4/F4) | ~$14 (analyst FV) | **$8–10 / ≤ ~$107M cap** | — | 2026-07-18 |
| OFLX | Omega Flex | CSST gas-piping duopoly with arc-resistant code advantage; 60% GM, net cash, dividend | High (Q4/F4) | 37x trough PE now | **~$190–220M cap (~2x trough P/S)** | — | 2026-07-18 |
| DETEC.HE | Detection Technology | X-ray detector OEM, proprietary silicon-photodiode process; net cash, Nordic coverage void | High (Q4/F3) | ~fair now | **a pullback giving a ≥2x path** | — | 2026-07-18 |

*(The bench grows as the routine finds durable-moat names trading at/above fair value. Names leave the bench when they either dip into the buy-zone → promote, or the moat/quality thesis breaks → drop.)*
