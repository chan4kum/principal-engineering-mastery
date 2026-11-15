# Contributing

Read the [teaching contract](TEACHING_CONTRACT.md) and check the [roadmap](ROADMAP.md) before proposing a new unit. Use a stable source ID and retain its topic. For a correction, include evidence from an exact command, trace or primary reference.

Use the [lesson](templates/lesson.md) and [lab](templates/lab.md) templates. Prefer short Mermaid node labels and plain-text traces that fit narrow screens. Label conceptual models, host-dependent observations, and every measured unit. Keep external services, credentials and private traces out of runnable examples.

## Pull request checklist

- [ ] Source ID, prerequisites and next link are accurate.
- [ ] Normal and failure runs are reproducible, bounded and clean up.
- [ ] Calculations can be reproduced from the given values.
- [ ] Answers are collapsed and a learner can attempt the task independently.
- [ ] New material is linked from its index and coverage reflects what ships.
- [ ] Run `uv run ruff check .` and `uv run pytest`. Record Linux-only checks and the host used.

Contributions are licensed according to [LICENSE](LICENSE).
