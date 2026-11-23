# M05 · Independent ML transfer

[Module index](../../README.md)

Build a spectral stability check for real symmetric transition matrices.

## Contract

Each case provides a finite square matrix. Reject a nonsymmetric matrix. Return its spectral radius and whether it is strictly below 1, which guarantees asymptotic decay of every initial state for the given transition rule.

Implement a local Python file with a callable `solve(case)` that accepts one dictionary and returns a dictionary with the documented fields. Use ordinary lists for array results. For an invalid case, return `{"status": "invalid"}`. The [public fixtures](cases.json) specify exact output keys and the expected results. Floating-point values are compared with tolerance.

## Acceptance evidence

Run from the repository root with the path to your own implementation.

```sh
uv run --locked --extra math python 02-mathematics-M01-to-M13/verify.py M05 project path/to/solution.py
```

- Pass all four published cases with your own implementation. The checker executes your local file.
- Include a numerical derivation or notebook, shape and error contracts, and at least one new valid case and one new counterexample with predicted outputs.
- Capture an initial failure and its repair or the verified rejection and recovery. Explain a numerical trade-off or limitation.
