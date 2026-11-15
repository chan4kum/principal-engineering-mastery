# BM25 versus vector benchmark

Compare BM25, deterministic dense cosine, and RRF on a fixed judged collection. Include one unseen synonym, one literal term and one empty result. Show the raw rankings and all three judged metrics. The dense representation is a handcrafted teaching fixture.

Run the acceptance suite after the independent attempt where applicable.

```sh
uv run --locked --extra api pytest -q tests/test_a12_projects.py
```

[Reference implementation](benchmark.py)

Record one observed failure, its cause and the first successful recovery. Document the assumptions and one production trade-off.
