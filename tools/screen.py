#!/usr/bin/env python3
"""Systematic top-of-funnel: enumerate the ENTIRE US filer universe from SEC
'frames' (one call each for revenue & gross profit — all filers, one period),
quant-filter to the worthwhile microcap subset, and rank by a quality proxy.

This replaces "hope web search surfaces names" with a measurable march through a
known denominator. Output: a ranked worklist + the worthwhile-universe SIZE, so
coverage % = (names reviewed) / (worthwhile universe) is knowable.

  python3 tools/screen.py --min-rev 20 --max-rev 400 --min-gm 40 --top 400
  python3 tools/screen.py --period CY2024   # if CY2025 not yet fully populated

Deterministic, zero LLM, ~4 HTTP calls total. Revenue band is a microcap PROXY
(true market cap is confirmed per-name later by snapshot.py); GM≥40% is the moat
signal. Foreign markets (no SEC frames) keep the sector×geo web path.
"""
import sys, json, urllib.request, argparse

UA = "niche-moat-kb research (contact: research@example.com)"
REV_TAGS = ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues"]

def frame(tag, period, taxonomy="us-gaap", unit="USD"):
    url = f"https://data.sec.gov/api/xbrl/frames/{taxonomy}/{tag}/{unit}/{period}.json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            return {d["cik"]: d for d in json.load(r).get("data", [])}
    except Exception as e:
        sys.stderr.write(f"frame {tag} {period} failed: {e}\n")
        return {}

def revenue_frame(period):
    out = {}
    for t in REV_TAGS:               # merge tag variants; first-seen wins
        for cik, d in frame(t, period).items():
            out.setdefault(cik, d)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-rev", type=float, default=20.0, help="$M")
    ap.add_argument("--max-rev", type=float, default=400.0, help="$M")
    ap.add_argument("--min-gm", type=float, default=40.0, help="%")
    ap.add_argument("--period", default="CY2025")
    ap.add_argument("--prior", default="CY2024", help="for growth rank")
    ap.add_argument("--top", type=int, default=400)
    ap.add_argument("--profitable-only", action="store_true", help="drop cash-burners (biotech etc.)")
    a = ap.parse_args()

    rev = revenue_frame(a.period)
    gp  = frame("GrossProfit", a.period)
    oi  = frame("OperatingIncomeLoss", a.period)
    rev0 = revenue_frame(a.prior)
    if not rev or not gp:
        print("ERROR: frames unavailable (try an earlier --period, e.g. CY2024)."); sys.exit(1)

    universe_reporting = len(rev)
    rows = []
    for cik, r in rev.items():
        R = r["val"]
        if not (a.min_rev*1e6 <= R <= a.max_rev*1e6):   # microcap-proxy band
            continue
        g = gp.get(cik)
        if not g or R <= 0:
            continue
        gm = g["val"] / R * 100.0
        if gm < a.min_gm or gm > 95:                     # moat signal; >95% = tag/data error, drop
            continue
        o = oi.get(cik)
        om = (o["val"] / R * 100.0) if o else None
        profitable = om is not None and om > 0
        if a.profitable_only and not profitable:         # drop cash-burners (biotech etc.)
            continue
        gr = None
        if cik in rev0 and rev0[cik]["val"] > 0:
            gr = (R - rev0[cik]["val"]) / rev0[cik]["val"] * 100.0
        # quality proxy: profitability weighs most, then margin, then capped growth
        score = (om if om is not None else -20)*1.0 + gm*0.4 + (min(gr, 40)*0.3 if gr is not None else 0)
        rows.append({"cik": cik, "name": r["entityName"], "rev_$M": round(R/1e6, 1),
                     "gm_%": round(gm, 1), "op_margin_%": None if om is None else round(om, 1),
                     "rev_growth_%": None if gr is None else round(gr, 1),
                     "profitable": profitable, "score": round(score, 1)})

    rows.sort(key=lambda x: x["score"], reverse=True)
    worthwhile = len(rows)
    print(f"# US systematic screen — period {a.period}")
    print(f"# filers reporting revenue: {universe_reporting}")
    print(f"# WORTHWHILE UNIVERSE (rev ${a.min_rev:.0f}-{a.max_rev:.0f}M, GM≥{a.min_gm:.0f}%): {worthwhile}")
    print(f"# (coverage % = names you've reviewed ÷ {worthwhile})")
    print(f"# top {min(a.top, worthwhile)} by quality proxy (GM + capped growth):\n")
    print("rank  score  GM%   opM%   revM   growth%  name")
    for i, x in enumerate(rows[:a.top], 1):
        print(f"{i:<5} {x['score']:<6} {x['gm_%']:<5} "
              f"{('' if x['op_margin_%'] is None else str(x['op_margin_%'])):<6} {x['rev_$M']:<6} "
              f"{('' if x['rev_growth_%'] is None else str(x['rev_growth_%'])):<8} {x['name']}")
    # machine-readable worklist for the routine to march through
    print("\n```json")
    print(json.dumps({"period": a.period, "worthwhile_universe": worthwhile,
                      "worklist": rows[:a.top]}))
    print("```")

if __name__ == "__main__":
    main()
