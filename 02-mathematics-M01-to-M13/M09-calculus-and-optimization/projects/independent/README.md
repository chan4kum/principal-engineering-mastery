# M09 · Independent ML transfer

[Module index](../../README.md)

Build a one-step optimizer for a diagonal quadratic.

## Contract

Each case contains curvatures h, an initial weight vector w, and learning rate step. Match vector lengths and require nonnegative curvatures and step. Return the updated weights and the objective obtained by summing hᵢwᵢ²/2 at the updated point. Reject invalid inputs.

Implement a local Python file with a callable `solve(case)` that accepts one dictionary and returns a dictionary with the documented fields. Use ordinary lists for array results. For an invalid case, return `{"status": "invalid"}`. The [public fixtures](cases.json) specify exact output keys and the expected results. Floating-point values are compared with tolerance.

## Acceptance evidence

Run from the repository root with the path to your own implementation.

```sh
uv run --locked --extra math python 02-mathematics-M01-to-M13/verify.py M09 project path/to/solution.py
```

- Pass all four published cases with your own implementation. The checker executes your local file.
- Include a numerical derivation or notebook, shape and error contracts, and at least one new valid case and one new counterexample with predicted outputs.
- Capture an initial failure and its repair or the verified rejection and recovery. Explain a numerical trade-off or limitation.
