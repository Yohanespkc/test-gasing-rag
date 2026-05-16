import json, re
data = json.load(open("validation_report.json"))
ok = 0
fails = []
for r in data["results"]:
    resp = r.get("gemma_response", "")
    if not resp: continue
    expected = str(r["expected_answer"])
    if re.search(rf"\b{expected}\b(?!\s*\u2081)", resp):
        ok += 1
    else:
        fails.append((r["id"], expected, r.get("math_actual")))
print(f"Real math accuracy: {ok}/40 ({100*ok/40:.0f}%)")
if fails:
    print(f"Still missing expected answer in response:")
    for f in fails: print(f"  {f[0]}: expected={f[1]}, parser_got={f[2]}")
