#!/usr/bin/env python3
"""Europe systematic enumeration — filings.xbrl.org (ESEF/UKSEF, keyless).

ESEF per-filer tagging is too inconsistent for a reliable BULK gross-margin
screen (even large filers mis-tag revenue), so — like Japan — the systematic win
is ENUMERATION: list every ESEF/UKSEF annual filer in a trustworthy-democracy
country → the denominator + a dedup'd worklist (entity name, LEI, country).
Fundamentals go per-name (snapshot.py live price + read the primary filing).

  python3 tools/screen_eu.py --countries DE,FR,SE,FI,NL,GB --top 60

Trustworthy-democracy allowlist only; excludes non-democratic/weak-rule-of-law
filers that also appear on filings.xbrl.org (e.g. UA). LEI→ticker is resolved
per-name downstream (GLEIF/name lookup); the entity name identifies the company.
"""
import sys, json, urllib.request, argparse

UA = "niche-moat-kb research (contact: research@example.com)"
# EU/EEA democracies + UK (ISO-2). Excludes CN/RU/UA/etc.
DEFAULT = "AT,BE,CH,CZ,DE,DK,ES,FI,FR,GB,IE,IT,LU,NL,NO,PL,PT,SE"

def filings(country, size=100):
    url = (f"https://filings.xbrl.org/api/filings?filter%5Bcountry%5D={country}"
           f"&page%5Bsize%5D={size}&sort=-period_end&include=entity")
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--countries", default=DEFAULT)
    ap.add_argument("--size", type=int, default=100, help="filings per country")
    ap.add_argument("--top", type=int, default=80)
    a = ap.parse_args()

    seen = {}
    per_country = {}
    for c in a.countries.split(","):
        c = c.strip()
        try:
            d = filings(c, a.size)
        except Exception as e:
            sys.stderr.write(f"{c}: {e}\n"); continue
        # entity names live in `included`
        names = {}
        for inc in d.get("included", []):
            if inc.get("type") == "entity":
                names[inc["id"]] = inc.get("attributes", {}).get("name")
        n = 0
        for f in d.get("data", []):
            at = f["attributes"]
            ju = at.get("json_url", "") or ""
            lei = ju.strip("/").split("/")[0] if ju else f.get("id")
            ent = f.get("relationships", {}).get("entity", {}).get("data", {}) or {}
            name = names.get(ent.get("id")) or ju.strip("/").split("/")[-1].split("-")[0]
            if lei in seen:
                continue
            seen[lei] = {"lei": lei, "name": name, "country": c, "period": at.get("period_end")}
            n += 1
        per_country[c] = n

    rows = sorted(seen.values(), key=lambda r: (r["country"], r["name"] or ""))
    print(f"# Europe (filings.xbrl.org ESEF/UKSEF) enumeration — trustworthy democracies")
    print(f"# countries: {', '.join(f'{k}:{v}' for k,v in per_country.items())}")
    print(f"# UNIQUE FILERS enumerated (this sweep): {len(rows)}")
    print(f"# → worklist for per-name diligence (resolve LEI→ticker, snapshot.py price, read primary filing).")
    print(f"# (page deeper / more countries for the fuller denominator)\n")
    print("country  period      entity (LEI)")
    for x in rows[:a.top]:
        print(f"{x['country']:<8} {str(x['period']):<11} {x['name']}  ({x['lei']})")
    print("\n```json")
    print(json.dumps({"market": "EU", "filers": len(rows), "worklist": rows[:a.top]}, ensure_ascii=False))
    print("```")

if __name__ == "__main__":
    main()
