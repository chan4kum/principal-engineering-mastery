# Guided project · Containerized API on local Kubernetes

Run the [deployment scenario](../../labs/L2.md) and follow the [manifest](platform.yaml).

```text
non-root image → Deployment → ready replica set → Service
```

Show the image UID, replacement Pod, readiness failure and repaired rollout. Compare a Pod process running with a Pod being eligible for normal Service traffic. Record observed fields and explain how you would promote the exact verified artifact.
