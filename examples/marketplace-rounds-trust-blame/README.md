# Marketplace: raising `rounds` from 10 to 60 makes the trust layer blame honest sellers

MIT AI Studio Fall 2026, Step 2 assessment. Scenario: `marketplace`. Setting changed: `task.config.rounds`.

## The change

One line in `marketplace_rounds60.yaml` compared to the built-in scenario:

```diff
-    rounds: 10
+    rounds: 60
```

Same seed (42), same 50 buyers / 50 sellers, same plugins, no failure injection.

## Why I chose it

I wanted to see how the agents behaved differently when they were given significantly more rounds to use their budget without changing the actual budget or other protocols. 60 rounds will give them lots of "useless" rounds where the buyers are at 0 or close to 0 budget, and I wanted to see how the buyers/sellers behaved. 

## Hypothesis (written before running)

I'm changing task.config.rounds from 10 to 60 in the marketplace scenario. Given that the buyers and sellers rate each other, my hypothesis is that the rating system is going to not work as intended when buyers budget get close to 0, but not 0. My prediction is that seller rating will indiscriminately decrease when buyers don't have enough to offer, but more than nothing, and the market will break down. 

## What happened

As predicted, the seller's trust score decreased when compared to the baseline of only 10 rounds. After round 32 rejection rates increased sharply, and rounds beyond 41 were almost 100% rejections. The mean seller trust score decreased from .558 in the baseline to .443 in the experiment. 

Validators: all 3 marketplace validators (no_double_sell, all_responded, price_agreement) pass on both traces.

## What this means

Buyers that had between 1 and 9 budget remaining kept offering to buy from sellers, but the offerings were below the seller's threshold. As instructed in their protocol, they rejected the offers and responded with their minimum acceptable bid amount. Even when the buyer agents had sufficient information to determine whether the seller reasonably rejected their bid or not, they gave the sellers a bad rating, creating a feedback loop all the way to the final round. This is a design issue, not an agentic issue. Both the buyers and sellers followed their instructions as intended, but the market did not remain intact. 

## Why this matters

In a closed system like this, where the reputation ends and is not carried forward, this is okay. In a real-world scenario, sellers would be needlessly punished for rejecting bids that were below their minimum threshold, and buyer agents will get frustrated because they are not making any decisions of whether to continue bidding or not. In the real-world, if a buyer doesn't have sufficient funds to meet anyone's minimum bid, it makes no sense for the SELLERS to be punished. 

## How to reproduce

```bash
pip install "nest-core[plugins]"
cd examples/marketplace-rounds-trust-blame
nest run ./marketplace_baseline.yaml -o ./baseline.jsonl
nest run ./marketplace_rounds60.yaml -o ./rounds60.jsonl
python analyze.py baseline.jsonl
python analyze.py rounds60.jsonl
```

Same seed produces byte-identical traces, so the two `.jsonl` files in this folder should match what you get.

## Files

- `marketplace_baseline.yaml` / `marketplace_rounds60.yaml`: the two scenarios; `diff` them.
- `baseline.jsonl` / `rounds60.jsonl`: the traces I ran.
- `analyze.py`: reconstructs per-seller trust scores and per-round sold/reject counts from a trace.
- `analysis_report.md`: output of `analyze.py` on both traces, with a summary table.
- `validators.txt`: validator output on both traces.

## Tools and help used

I used Claude cowork and code to help understand the repo, as well as generate the analyze.py and analysis_report.md files. 
