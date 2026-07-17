#!/usr/bin/env python3
"""Deterministic financial sanity checks — reduces LLM number errors that
"be careful" cannot. Reads JSON of the fetched basics from stdin; prints
PASS/FAIL/SKIP per assertion. Any FAIL → those figures are auto-⚠ (never ✓).

Usage:
  python3 tools/fin_check.py <<'JSON'
  {"revenue":115.4,"gross_profit":31.7,"gross_margin":27.5,"net_income":15.7,
   "cash":155.1,"total_debt":0,"net_cash":155.1,"market_cap":230,"ev":75,
   "ocf":18,"capex":2,"fcf":16,"shares":9.6,"shares_prior":9.6,
   "revenue_prior":113.2,"pe":14.6,"ev_ebitda":null,"ps":2.0}
  JSON
All figures in the same units (e.g. $M). Omit or null anything unknown (→ SKIP).
"""
import sys, json

TOL = 0.03  # 3% relative tolerance for rounding/vendor differences

def rel_close(a, b):
    if a is None or b is None: return None
    if abs(b) < 1e-9: return abs(a) < 1e-6
    return abs(a - b) / abs(b) <= TOL

def num(d, k):
    v = d.get(k)
    return v if isinstance(v, (int, float)) else None

def main():
    try:
        d = json.load(sys.stdin)
    except Exception as e:
        print(f"FATAL: bad JSON ({e})"); sys.exit(2)

    rev, cogs, gp, gm = num(d,'revenue'), num(d,'cogs'), num(d,'gross_profit'), num(d,'gross_margin')
    ni, cash, debt, ncash = num(d,'net_income'), num(d,'cash'), num(d,'total_debt'), num(d,'net_cash')
    mcap, ev = num(d,'market_cap'), num(d,'ev')
    ocf, capex, fcf = num(d,'ocf'), num(d,'capex'), num(d,'fcf')
    sh, sh0, rev0 = num(d,'shares'), num(d,'shares_prior'), num(d,'revenue_prior')
    pe, ps = num(d,'pe'), num(d,'ps')

    fails, flags = [], []
    def check(name, cond, detail=""):
        if cond is None: print(f"  SKIP  {name} (missing inputs)")
        elif cond:       print(f"  PASS  {name} {detail}")
        else:            print(f"  FAIL  {name} {detail}"); fails.append(name)
    def flag(name, cond, detail=""):
        if cond: print(f"  FLAG  {name} {detail}"); flags.append(name)

    print("— arithmetic reconciliation —")
    # gross margin recomputes
    if rev and gm is not None:
        gp_calc = gp if gp is not None else (rev - cogs if cogs is not None else None)
        if gp_calc is not None:
            check("gross_margin = gross_profit/revenue", rel_close(gp_calc/rev*100, gm),
                  f"(calc {gp_calc/rev*100:.1f}% vs reported {gm:.1f}%)")
        else: check("gross_margin recompute", None)
    else: check("gross_margin recompute", None)
    # net cash = cash - debt
    if cash is not None and debt is not None and ncash is not None:
        check("net_cash = cash - debt", rel_close(cash - debt, ncash),
              f"(calc {cash-debt:.1f} vs reported {ncash:.1f})")
    else: check("net_cash = cash - debt", None)
    # EV = mcap + debt - cash
    if mcap is not None and debt is not None and cash is not None and ev is not None:
        check("EV = mktcap + debt - cash", rel_close(mcap + debt - cash, ev),
              f"(calc {mcap+debt-cash:.1f} vs reported {ev:.1f})")
    else: check("EV = mktcap + debt - cash", None)
    # FCF = OCF - capex
    if ocf is not None and capex is not None and fcf is not None:
        check("FCF = OCF - capex", rel_close(ocf - abs(capex), fcf),
              f"(calc {ocf-abs(capex):.1f} vs reported {fcf:.1f})")
    else: check("FCF = OCF - capex", None)
    # P/S = mcap / revenue
    if mcap and rev and ps is not None:
        check("P/S = mktcap/revenue", rel_close(mcap/rev, ps), f"(calc {mcap/rev:.2f} vs reported {ps:.2f})")
    else: check("P/S = mktcap/revenue", None)
    # P/E = mcap / net income (only if profitable)
    if mcap and ni and ni > 0 and pe is not None:
        check("P/E = mktcap/net_income", rel_close(mcap/ni, pe), f"(calc {mcap/ni:.1f} vs reported {pe:.1f})")
    else: check("P/E = mktcap/net_income", None)

    print("— range / plausibility —")
    check("0 ≤ gross_margin ≤ 100", None if gm is None else (0 <= gm <= 100), f"({gm})" if gm is not None else "")
    if gm is not None and ni is not None and rev:
        nm = ni/rev*100
        check("net_margin ≤ gross_margin", nm <= gm + 0.5, f"(net {nm:.1f}% vs gross {gm:.1f}%)")
    else: check("net_margin ≤ gross_margin", None)
    # dilution / buyback
    if sh is not None and sh0 is not None and sh0:
        chg = (sh - sh0)/sh0*100
        flag("share count YoY", chg > 3, f"DILUTION +{chg:.1f}% (floor risk)")
        flag("share count YoY", chg < -1, f"buyback {chg:.1f}% (positive)")
        if abs(chg) <= 3: print(f"  PASS  share count YoY (stable {chg:+.1f}%)")
    else: check("share count YoY", None)
    # revenue growth plausibility
    if rev and rev0 and rev0:
        g = (rev - rev0)/rev0*100
        flag("revenue YoY plausibility", g > 100 or g < -50, f"{g:+.0f}% — verify units/period/FYE")
        if -50 <= g <= 100: print(f"  PASS  revenue YoY ({g:+.0f}%)")
    else: check("revenue YoY plausibility", None)
    # extreme multiples → likely a units/period error
    flag("P/E sanity", pe is not None and (pe > 200 or (ni is not None and ni>0 and pe<0)), f"P/E={pe} — suspect")
    flag("P/S sanity", ps is not None and ps > 50, f"P/S={ps} — suspect units")

    # Provenance — internal consistency ≠ truth. A set of numbers from one wrong
    # vendor feed reconciles perfectly. The only defense is FILING provenance on the
    # figures that determine the floor. Pass "provenance": {"revenue":"filing", ...}
    # with values filing | aggregator | none.
    print("— provenance (anti-vendor-feed) —")
    prov = d.get('provenance') or {}
    FLOOR_CRITICAL = ['revenue', 'cash', 'total_debt', 'shares']
    unanchored = []
    if not prov:
        print("  WARN  no provenance map → cannot certify filing-anchoring; "
              "floor-critical figures may NOT be tagged ✓ on internal consistency alone")
        unanchored = FLOOR_CRITICAL[:]
    else:
        for k in FLOOR_CRITICAL:
            src = prov.get(k)
            if src == 'filing':
                print(f"  PASS  {k}: primary filing")
            elif src == 'aggregator':
                print(f"  FLAG  {k}: aggregator-only → cap at ~SINGLE-SOURCE, cannot be ✓"); unanchored.append(k)
            else:
                print(f"  FLAG  {k}: no filing provenance → ?, cannot be ✓"); unanchored.append(k)

    print("— verdict —")
    if fails:
        print(f"  ⚠ {len(fails)} FAIL(s): {', '.join(fails)} → tag these figures ⚠ DISCREPANT, dig before qualifying.")
    if flags:
        print(f"  ⚑ {len(flags)} FLAG(s): {', '.join(flags)} → note in the skepticism coaching.")
    if unanchored:
        print(f"  ⚑ NOT filing-anchored: {', '.join(unanchored)} → these cap the floor confidence; "
              f"read the actual filing before CANDIDATE/CORE. Reconciling ≠ true.")
    if not fails and not flags and not unanchored:
        print("  ✓ all checks reconcile AND floor-critical figures are filing-anchored.")
    # exit 1 on hard fail OR when no floor-critical figure is filing-anchored (the bad-vendor-feed trap)
    sys.exit(1 if (fails or len(unanchored) == len(FLOOR_CRITICAL)) else 0)

if __name__ == "__main__":
    main()
