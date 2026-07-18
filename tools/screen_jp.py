#!/usr/bin/env python3
"""Japan systematic enumeration — EDINET API v2 (needs EDINET_KEY env var).

EDINET has no 'frames'-style bulk-financials call, so the systematic win here is
ENUMERATION: list every listed-company securities report over a window → the
denominator + a dedup'd worklist (ticker + filer). Fundamentals stay per-name
(consistent with the non-English-filing rule: translate + read the primary
filing, verify orders/revenue/margins/cash/shares). GM pre-filtering in bulk is
a future enhancement (fetch + parse each filing's XBRL).

  EDINET_KEY=... python3 tools/screen_jp.py --days 7
  (key is read from the environment — NEVER hardcode/commit it)

secCode is 5 digits; Yahoo ticker = first 4 digits + '.T'.
docTypeCode 120 = annual securities report (有報), 140 = quarterly (四半期).
"""
import os, sys, json, urllib.request, argparse
from datetime import date, timedelta

UA = "niche-moat-kb research (contact: research@example.com)"
KEY = os.environ.get("EDINET_KEY", "")

def docs_for(day):
    url = (f"https://api.edinet-fsa.go.jp/api/v2/documents.json"
           f"?date={day}&type=2&Subscription-Key={KEY}")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read()).get("results", [])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7, help="lookback window")
    ap.add_argument("--doc-types", default="120,140,160", help="EDINET docTypeCodes")
    ap.add_argument("--top", type=int, default=60)
    a = ap.parse_args()
    if not KEY:
        print("ERROR: EDINET_KEY env var not set (add it to the routine cloud env)."); sys.exit(1)

    want = set(a.doc_types.split(","))
    seen, filings = {}, 0
    today = date.today()
    for i in range(a.days):
        day = (today - timedelta(days=i)).isoformat()
        try:
            res = docs_for(day)
        except Exception as e:
            sys.stderr.write(f"{day}: {e}\n"); continue
        for x in res:
            sec = x.get("secCode")
            if not sec or x.get("docTypeCode") not in want:
                continue
            filings += 1
            tkr = sec[:4] + ".T"
            # keep the most recent filing per company
            if tkr not in seen:
                seen[tkr] = {"ticker": tkr, "name": x.get("filerName"),
                             "docType": x.get("docTypeCode"), "docID": x.get("docID"),
                             "period": x.get("periodEnd") or x.get("submitDateTime", "")[:10]}
    rows = sorted(seen.values(), key=lambda r: r["ticker"])
    print(f"# Japan (EDINET) enumeration — last {a.days} days, docTypes {a.doc_types}")
    print(f"# securities-report filings scanned: {filings}")
    print(f"# UNIQUE LISTED FILERS enumerated (this window): {len(rows)}")
    print(f"# → worklist for per-name diligence (Yahoo price via snapshot.py + read the primary filing).")
    print(f"# (widen --days to cover a full filing season for the true denominator)\n")
    print("ticker    docType  period      filer")
    for x in rows[:a.top]:
        print(f"{x['ticker']:<9} {x['docType']:<8} {x['period']:<11} {x['name']}")
    print("\n```json")
    print(json.dumps({"market": "JP", "window_days": a.days, "filers": len(rows),
                      "worklist": rows[:a.top]}, ensure_ascii=False))
    print("```")

if __name__ == "__main__":
    main()
