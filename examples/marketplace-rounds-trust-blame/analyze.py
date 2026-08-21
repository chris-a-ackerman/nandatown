# analyze.py -- reconstruct seller trust scores and per-round rejection from a marketplace trace
import json, sys
from collections import defaultdict

path = sys.argv[1]
sold = defaultdict(int)
rejected = defaultdict(int)
by_round = defaultdict(lambda: [0, 0])   # product-N -> [sold, reject]
reject_reason_price = 0

for line in open(path):
    ev = json.loads(line)
    if ev.get("kind") != "send":
        continue
    msg = ev["msg"].rsplit("|sig:", 1)[0]
    seller = ev["agent"]
    parts = msg.split(":")
    if msg.startswith("sold:"):
        sold[seller] += 1
        by_round[parts[1]][0] += 1
    elif msg.startswith("reject:"):
        rejected[seller] += 1
        by_round[parts[1]][1] += 1

sellers = sorted(set(sold) | set(rejected), key=lambda s: int(s.split("-")[1]))
scores = {}
for s in sellers:
    n = sold[s] + rejected[s]
    scores[s] = sold[s] / n if n else 0.5      # exactly what ScoreAverageTrust computes

print(f"== {path}")
print(f"sellers with any reports: {len(sellers)}")
print(f"mean seller trust score : {sum(scores.values())/len(scores):.3f}")
print(f"min  seller trust score : {min(scores.values()):.3f}  ({min(scores, key=scores.get)})")
print(f"sellers below 0.2       : {sum(1 for v in scores.values() if v < 0.2)}")
print("\nper-round: sold / reject / reject%")
for k in sorted(by_round, key=lambda p: int(p.split('-')[1])):
    s, r = by_round[k]
    print(f"  {k:12s} {s:3d} {r:3d}  {100*r/(s+r):5.1f}%")
