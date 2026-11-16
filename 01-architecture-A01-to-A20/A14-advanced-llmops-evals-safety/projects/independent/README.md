# A14 · Versioned LLM release pipeline with canary/rollback

[Phase index](../../README.md)

Admit an immutable candidate only on a complete matched case set, with a scope/safety veto and budget. Restore the stable artifact and prove its identity. This is an in-process release controller for recorded fixtures.

## Architecture

```mermaid
flowchart LR
    A["Fixture input"] --> B["Scope and invariant checks"]
    B --> C["Operation and observable result"]
```

## Acceptance evidence

- [L3](../../labs/L3.md). Record admission, live prompt identity and restored identity.
- [L4](../../labs/L4.md). Record the scope veto and retained baseline. The fixture uses no live model or privileged tool.

Run the verification commands from the linked labs. Inspect the [independent source](independent.py) after predicting the outcome.

Attempt an independent implementation and preserve normal and failure results before consulting the reference. Repeat with a counterexample from a different input family.
