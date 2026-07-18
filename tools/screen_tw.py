#!/usr/bin/env python3
"""Taiwan systematic screen — TWSE OpenAPI (keyless). Mirrors screen.py:
enumerate the TWSE main-board universe, quant-filter to worthwhile microcaps by
revenue band + gross margin, rank best-first, print a measurable denominator.

  python3 tools/screen_tw.py --min-rev 20 --max-rev 400 --min-gm 40 --top 40

Two keyless calls: company list (t187ap03_L) + comprehensive-income statements
(t187ap06_L_ci: 營業收入 revenue, 營業毛利 gross profit). Values are NT$ thousands
(most recent reported quarter). Revenue band given in US$M, converted at ~31 TWD.
Tickers get the .TW suffix for snapshot.py/Yahoo. Fundamentals here are the
worthwhile-filter; live price + true market cap are confirmed per-name later.
"""
import sys, json, urllib.request, argparse

UA = "niche-moat-kb research (contact: research@example.com)"
TWD_PER_USD = 31.0
BASE = "https://openapi.twse.com.tw/v1/opendata/"

def get(path):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8", "replace"))

def f(v):
    try: return float(str(v).replace(",", ""))
    except Exception: return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-rev", type=float, default=20.0, help="US$M")
    ap.add_argument("--max-rev", type=float, default=400.0, help="US$M")
    ap.add_argument("--min-gm", type=float, default=40.0, help="%")
    ap.add_argument("--top", type=int, default=40)
    a = ap.parse_args()

    try:
        names = {r["公司代號"]: (r.get("公司簡稱") or r.get("公司名稱"), r.get("產業別", ""))
                 for r in get("t187ap03_L")}
        fin = get("t187ap06_L_ci")   # general-industry comprehensive income
    except Exception as e:
        print(f"ERROR: TWSE OpenAPI fetch failed: {e}"); sys.exit(1)

    lo = a.min_rev * 1e6 * TWD_PER_USD / 1000.0   # US$M → NT$ thousands
    hi = a.max_rev * 1e6 * TWD_PER_USD / 1000.0
    rows, reporting = [], 0
    for r in fin:
        tkr = r.get("公司代號"); rev = f(r.get("營業收入")); gp = f(r.get("營業毛利（毛損）"))
        if rev is None: continue
        reporting += 1
        if not (lo <= rev <= hi) or rev <= 0 or gp is None: continue
        gm = gp / rev * 100.0
        if gm < a.min_gm or gm > 95: continue
        nm, ind = names.get(tkr, (tkr, ""))
        rows.append({"ticker": f"{tkr}.TW", "name": nm, "industry_code": ind,
                     "rev_$M": round(rev * 1000 / TWD_PER_USD / 1e6, 1), "gm_%": round(gm, 1)})
    rows.sort(key=lambda x: x["gm_%"], reverse=True)

    print(f"# Taiwan (TWSE main board) systematic screen — most recent reported quarter")
    print(f"# companies reporting revenue: {reporting}")
    print(f"# WORTHWHILE UNIVERSE (rev ${a.min_rev:.0f}-{a.max_rev:.0f}M, GM≥{a.min_gm:.0f}%): {len(rows)}")
    print(f"# (coverage % = reviewed ÷ {len(rows)}; note: financial-sector cos + TPEx OTC are separate tables)\n")
    print("rank  GM%   revM   ticker      name")
    for i, x in enumerate(rows[:a.top], 1):
        print(f"{i:<5} {x['gm_%']:<5} {x['rev_$M']:<6} {x['ticker']:<11} {x['name']}")
    print("\n```json")
    print(json.dumps({"market": "TW", "worthwhile_universe": len(rows), "worklist": rows[:a.top]}, ensure_ascii=False))
    print("```")

if __name__ == "__main__":
    main()
