# Guided project · Secure FastAPI CRUD API

Use [api.py](api.py) to trace a strict request through identity, authorization and tenant-scoped storage. The fixture tokens are for this local exercise. The store is process-local, with a lock around each compound update.

```text
request → schema + bearer identity → permission and tenant check → locked CRUD → public representation
```

```sh
uv sync --locked --extra api
uv run --locked --extra api pytest -q tests/test_a03_projects.py -k crud
```

Predict the results for a missing token, a read-only token writing, and an authenticated request for another tenant's object. Re-run with the authorized writer and confirm that creation, read, replacement and deletion work. Inspect the generated OpenAPI schema and compare its response descriptions with the actual responses.

Save the status and affected tenant for the failed and repaired runs. In a scratch copy, explain how to move the same checks into a durable store used by several workers. Public deployments need an actual identity provider, trusted transport, secret management, abuse protections, and persistence.
