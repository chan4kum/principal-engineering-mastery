# Guided project · Queue-backed order workflow

```text
synchronous API → inventory then pricing → immediate result or failure
queued API → durable job receipt → worker effect → acknowledgment
```

Run `uv run --locked --extra api pytest -q tests/test_a07_projects.py -k guided`. Follow [the API and worker](queue_api.py) through a refused dependency, queue admission and the worker's abrupt exit after committing the effect. Explain why retrying before acknowledgment needs an effect identity. Verify that a new worker can acknowledge the same pending job without creating another effect. Document a state machine for pending, claimed, retried and completed jobs if adding competing workers.
