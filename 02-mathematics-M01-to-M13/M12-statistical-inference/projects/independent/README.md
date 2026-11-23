# M12 · Independent ML transfer

[Module index](../../README.md)

Build a forecast scoring report for one evaluation cohort.

## Contract

Each case provides equal-length, nonempty probabilities and binary outcomes. Validate every entry. Return the mean squared probability error as brier and the absolute difference between mean prediction and event rate as gap. The gap describes a single cohort and can hide miscalibration across score bins.

Implement a local Python file with a callable `solve(case)` that accepts one dictionary and returns a dictionary with the documented fields. Use ordinary lists for array results. For an invalid case, return `{"status": "invalid"}`. The [public fixtures](cases.json) specify exact output keys and the expected results. Floating-point values are compared with tolerance.

## Acceptance evidence

Run from the repository root with the path to your own implementation.

```sh
uv run --locked --extra math python 02-mathematics-M01-to-M13/verify.py M12 project path/to/solution.py
```

- Pass all four published cases with your own implementation. The checker executes your local file.
- Include a numerical derivation or notebook, shape and error contracts, and at least one new valid case and one new counterexample with predicted outputs.
- Capture an initial failure and its repair or the verified rejection and recovery. Explain a numerical trade-off or limitation.
