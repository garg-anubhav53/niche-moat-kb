#!/usr/bin/env python3
"""Taiwan value-quality screen — TWSE OpenAPI (keyless). UPGRADED (v4):

The comprehensive-income endpoint (t187ap06_L_ci) exposes FULL fundamentals —
revenue, gross profit, operating income, net income (to parent) AND basic EPS —
not just gross margin. So Taiwan is the one non-English market where we reach
PRIMARY-SOURCE fundamentals keyless: we can compute gross/operating/net margin,
derive share count (= NI/EPS), and (when a price feed is reachable) a live P/E.

  python3 tools/screen_tw.py --min-gm 45 --min-om 12 --top 40

Deterministic, keyless. Fundamentals are annualized from the latest reported
quarter (APPROXIMATE, cyclically noisy — verify TTM per-name in §3.5/§5). Price
is BEST-EFFORT via Yahoo; if the feed is blocked (cloud proxy), the tool still
emits full fundamentals + EPS and marks price/PE n/a (get price separately).
Financial-sector cos + TPEx OTC are in separate TWSE tables (not covered here).
"""
import sys, json, urllib.request, argparse
from concurrent.futures import ThreadPoolExecutor

UA = {"User-Agent": "Mozilla/5.0"}
TWD = 31.5
BASE = "https://openapi.twse.com.tw/v1/opendata/"

def get(path):
    req = urllib.request.Request(BASE + path, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode("utf-8", "replace"))

def num(v):
    try: return float(str(v).replace(",", ""))
    except Exception: return None

def price(ticker):
    """Best-effort live price; None if every reachable feed is blocked."""
    for host in ("query1", "query2"):
        try:
            req = urllib.request.Request(
                f"https://{host}.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=1d", headers=UA)
            with urllib.request.urlopen(req, timeout=10) as r:
                return json.load(r)["chart"]["result"][0]["meta"].get("regularMarketPrice")
        except Exception:
            continue
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-rev", type=float, default=20.0, help="US$M (annualized)")
    ap.add_argument("--max-rev", type=float, default=4000.0, help="US$M (annualized)")
    ap.add_argument("--min-gm", type=float, default=45.0, help="%")
    ap.add_argument("--min-om", type=float, default=12.0, help="operating margin %")
    ap.add_argument("--max-pe", type=float, default=None, help="value gate (only if price feed reachable)")
    ap.add_argument("--top", type=int, default=40)
    a = ap.parse_args()

    try:
        names = {r["公司代號"]: (r.get("公司簡稱") or r.get("公司名稱"), r.get("產業別", ""))
                 for r in get("t187ap03_L")}
        fin = get("t187ap06_L_ci")
    except Exception as e:
        print(f"ERROR: TWSE OpenAPI fetch failed: {e}"); sys.exit(1)

    cands = []
    for r in fin:
        code = r.get("公司代號")
        rev = num(r.get("營業收入")); gp = num(r.get("營業毛利（毛損）")); oi = num(r.get("營業利益（損失）"))
        ni = num(r.get("淨利（淨損）歸屬於母公司業主")); eps = num(r.get("基本每股盈餘（元）"))
        if not rev or rev <= 0 or gp is None or oi is None or ni is None: continue
        gm = gp/rev*100; om = oi/rev*100; nm = ni/rev*100
        if gm < a.min_gm or gm > 98 or om < a.min_om or ni <= 0: continue
        rev_usd = rev*4*1000/TWD/1e6                       # NT$k quarterly -> annual US$M
        if not (a.min_rev <= rev_usd <= a.max_rev): continue
        nm_, ind = names.get(code, (code, ""))
        cands.append(dict(tkr=f"{code}.TW", code=code, name=nm_, ind=ind, gm=gm, om=om, nm=nm,
                          eps_ann=(eps*4 if eps else None), shares_k=(ni/eps if eps and eps > 0 else None),
                          rev_usd=rev_usd))

    # best-effort pricing (skips cleanly if the feed is blocked)
    with ThreadPoolExecutor(max_workers=12) as ex:
        prices = list(ex.map(price, [c["tkr"] for c in cands]))
    priced = 0
    for c, p in zip(cands, prices):
        c["price"] = p
        if p and c["eps_ann"] and c["eps_ann"] > 0:
            c["pe"] = p/c["eps_ann"]; priced += 1
            c["mc_usd"] = (p*c["shares_k"]*1000/TWD/1e6) if c["shares_k"] else None
        else:
            c["pe"] = None; c["mc_usd"] = None

    if a.max_pe is not None:
        cands = [c for c in cands if c["pe"] is not None and c["pe"] <= a.max_pe]

    # rank by a price-independent QUALITY score (robust when price feed is blocked);
    # when priced, tilt toward cheaper P/E.
    cands.sort(key=lambda c: (c["gm"]*0.4 + c["om"]*0.4 + c["nm"]*0.2)
               - (min(c["pe"], 40) if c["pe"] else 0)*0.5, reverse=True)

    price_note = f"{priced}/{len(cands)} priced" if priced else "PRICE FEED BLOCKED — fundamentals only (get price separately)"
    print(f"# Taiwan value-quality screen (TWSE keyless, full fundamentals) — {len(cands)} names · {price_note}")
    print(f"# gates: GM>={a.min_gm:.0f}% · opM>={a.min_om:.0f}% · profitable · rev ${a.min_rev:.0f}-{a.max_rev:.0f}M (annualized Q — verify TTM per-name)")
    print(f"# (financial-sector cos + TPEx OTC are separate TWSE tables; property/shipping industries run lumpy — check 'ind')\n")
    print(f"{'rank':<5}{'tkr':<10}{'GM%':<5}{'opM%':<5}{'netM%':<6}{'P/E':<7}{'mc$M':<8}{'ind':<5}name")
    for i, c in enumerate(cands[:a.top], 1):
        pe = f"{c['pe']:.1f}" if c["pe"] else "n/a"
        mc = f"{c['mc_usd']:.0f}" if c["mc_usd"] else "-"
        print(f"{i:<5}{c['tkr']:<10}{c['gm']:<5.0f}{c['om']:<5.0f}{c['nm']:<6.0f}{pe:<7}{mc:<8}{c['ind']:<5}{c['name']}")
    print("\n```json")
    print(json.dumps({"market": "TW", "worthwhile_universe": len(cands), "priced": priced,
                      "worklist": [{k: c.get(k) for k in ('tkr','name','ind','gm','om','nm','eps_ann','pe','mc_usd','rev_usd')}
                                   for c in cands[:a.top]]}, ensure_ascii=False))
    print("```")

if __name__ == "__main__":
    main()
