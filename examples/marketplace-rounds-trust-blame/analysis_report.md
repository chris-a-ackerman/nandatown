# Marketplace Trace Analysis — Baseline vs. 60 Rounds

## Summary

| Metric | baseline.jsonl (10 rounds) | rounds60.jsonl (60 rounds) |
|---|---|---|
| Sellers with any reports | 50 | 50 |
| Mean seller trust score | 0.558 | 0.443 |
| Min seller trust score | 0.000 (seller-37) | 0.225 (seller-29) |
| Sellers below 0.2 | 1 | 0 |

## Key findings

1. **The first 10 rounds are identical in both runs** (same seed, same config), with reject rates in a healthy 40–58% band and all 50 outcomes recorded per round. The baseline run tells us nothing beyond this steady-state window.

2. **The 60-round run shows a market collapse starting around round 22.** Total activity per round (sold + rejected) holds at 50 through round 21, then steadily shrinks — 47 by round 22, ~28 by round 30, and only 9–10 outcomes per round by the end. Agents are progressively dropping out of trading.

3. **Rejection rates spiral to 100%.** Reject% stays in the 40–60% band through roughly round 32, then climbs sharply: 78% at round 33, 94% at round 38, and from round 41 onward almost every remaining interaction is a rejection. Rounds 41–59 record **zero or near-zero sales** (17 of the last 19 rounds have 0 or 1 sale).

4. **Trust scores erode rather than differentiate.** Mean trust falls from 0.558 to 0.443 as the late-run rejections accumulate against every seller. Notably, *no* seller ends below the 0.2 threshold (vs. 1 at baseline — seller-37 at 0.000 recovers with more data), so the trust layer never flags anyone as bad. Instead the whole population converges into a mediocre 0.2–0.5 band while the market dies. The `score_average` trust metric is failing to distinguish a market-wide breakdown from individual seller misbehavior.

<!-- Chris: rewrite interpretation here -->

## Per-round detail

### baseline.jsonl (10 rounds)

| Round | Sold | Rejected | Reject % |
|---|---|---|---|
| product-0 | 27 | 23 | 46.0% |
| product-1 | 25 | 25 | 50.0% |
| product-2 | 24 | 26 | 52.0% |
| product-3 | 26 | 24 | 48.0% |
| product-4 | 30 | 20 | 40.0% |
| product-5 | 21 | 29 | 58.0% |
| product-6 | 30 | 20 | 40.0% |
| product-7 | 27 | 23 | 46.0% |
| product-8 | 28 | 22 | 44.0% |
| product-9 | 28 | 22 | 44.0% |

### rounds60.jsonl (60 rounds)

| Round | Sold | Rejected | Reject % |
|---|---|---|---|
| product-0 | 27 | 23 | 46.0% |
| product-1 | 25 | 25 | 50.0% |
| product-2 | 24 | 26 | 52.0% |
| product-3 | 26 | 24 | 48.0% |
| product-4 | 30 | 20 | 40.0% |
| product-5 | 21 | 29 | 58.0% |
| product-6 | 30 | 20 | 40.0% |
| product-7 | 27 | 23 | 46.0% |
| product-8 | 28 | 22 | 44.0% |
| product-9 | 28 | 22 | 44.0% |
| product-10 | 26 | 24 | 48.0% |
| product-11 | 23 | 27 | 54.0% |
| product-12 | 26 | 24 | 48.0% |
| product-13 | 28 | 22 | 44.0% |
| product-14 | 25 | 25 | 50.0% |
| product-15 | 26 | 24 | 48.0% |
| product-16 | 25 | 25 | 50.0% |
| product-17 | 26 | 24 | 48.0% |
| product-18 | 29 | 21 | 42.0% |
| product-19 | 22 | 28 | 56.0% |
| product-20 | 24 | 26 | 52.0% |
| product-21 | 28 | 22 | 44.0% |
| product-22 | 25 | 22 | 46.8% |
| product-23 | 25 | 18 | 41.9% |
| product-24 | 22 | 18 | 45.0% |
| product-25 | 19 | 21 | 52.5% |
| product-26 | 16 | 23 | 59.0% |
| product-27 | 18 | 16 | 47.1% |
| product-28 | 14 | 20 | 58.8% |
| product-29 | 15 | 16 | 51.6% |
| product-30 | 16 | 12 | 42.9% |
| product-31 | 10 | 16 | 61.5% |
| product-32 | 11 | 14 | 56.0% |
| product-33 | 5 | 18 | 78.3% |
| product-34 | 11 | 12 | 52.2% |
| product-35 | 6 | 15 | 71.4% |
| product-36 | 8 | 12 | 60.0% |
| product-37 | 4 | 14 | 77.8% |
| product-38 | 1 | 16 | 94.1% |
| product-39 | 4 | 13 | 76.5% |
| product-40 | 1 | 13 | 92.9% |
| product-41 | 0 | 14 | 100.0% |
| product-42 | 0 | 14 | 100.0% |
| product-43 | 3 | 11 | 78.6% |
| product-44 | 0 | 11 | 100.0% |
| product-45 | 1 | 10 | 90.9% |
| product-46 | 0 | 10 | 100.0% |
| product-47 | 0 | 10 | 100.0% |
| product-48 | 0 | 10 | 100.0% |
| product-49 | 0 | 10 | 100.0% |
| product-50 | 0 | 10 | 100.0% |
| product-51 | 0 | 10 | 100.0% |
| product-52 | 1 | 9 | 90.0% |
| product-53 | 0 | 9 | 100.0% |
| product-54 | 0 | 9 | 100.0% |
| product-55 | 0 | 9 | 100.0% |
| product-56 | 0 | 9 | 100.0% |
| product-57 | 0 | 9 | 100.0% |
| product-58 | 0 | 9 | 100.0% |
| product-59 | 0 | 9 | 100.0% |
