# Independent project · Incident game-day and recovery automation

Build four isolated scenarios with a healthy baseline, one narrowly scoped fault, cleanup and recovery verification.

```text
healthy observations → choose one fault → collect evidence → classify and repair → verify
disposable backup → restore target → integrity and business invariant check
```

Implement `game_day(directory, fault)` for `cpu`, `lock` and `dns`. Return `timeline` with baseline, incident and recovery dictionaries containing `wall_ms`, `cpu_ms`, `database_busy`, and `dns_rcode`. Return `diagnosis` and `recovered` separately. Choose a bounded CPU action, a two-connection database lock and a local resolver fixture. Scope all faults to the scratch directory or loopback sockets.

Implement `recovery(directory, broken=False)` with `baseline_cents`, `restored_cents`, `target_corrupt`, and `restore_and_verify_ms`. The invariant is 500 cents. In failure mode, corrupt only the drill target and restore it from a verified backup. Include a rolled-back migration and verify the original schema and committed state.

```sh
P=01-architecture-A01-to-A20/A08-reliability-operations-and-sre/projects/independent
A08_GAME_DAY="$P/game_day.py" uv run --locked pytest -q tests/test_a08_projects.py -k independent
```

Submit an incident timeline and an evidence-based mitigation for each fault. State the stopping condition and show how you know that the fault state is gone.

<details>
<summary>Reference implementation after the independent attempt</summary>

[Local game day runner](reference_game_day.py)

</details>
