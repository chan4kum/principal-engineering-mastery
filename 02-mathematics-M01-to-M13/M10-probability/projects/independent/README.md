# M10 · Independent ML transfer

[Module index](../../README.md)

Build a positive predictive value estimator.

## Contract

Each case provides prevalence, sensitivity, and false_positive_rate as probabilities in [0,1]. Return the expected positive rate and the probability of a true event conditional on a positive. Reject invalid probabilities. Return status undefined when there are zero expected positives.

Implement a local Python file with a callable `solve(case)` that accepts one dictionary and returns a dictionary with the documented fields. Use ordinary lists for array results. For an invalid case, return `{"status": "invalid"}`. The [public fixtures](cases.json) specify exact output keys and the expected results. Floating-point values are compared with tolerance.

## Acceptance evidence

Run from the repository root with the path to your own implementation.

```sh
uv run --locked --extra math python 02-mathematics-M01-to-M13/verify.py M10 project path/to/solution.py
```

- Pass all four published cases with your own implementation. The checker executes your local file.
- Include a numerical derivation or notebook, shape and error contracts, and at least one new valid case and one new counterexample with predicted outputs.
- Capture an initial failure and its repair or the verified rejection and recovery. Explain a numerical trade-off or limitation.
