# Independent project · Secure multi-service Kubernetes platform

Implement a disposable namespace containing a two-replica API, a restricted client, a Service, a disruption budget, and enforced ingress policy. Application Pods must be non-root with dropped capabilities, read-only root filesystems, declared resources and no mounted service-account credential. An admitted client must reach the API; verify a denial and a recovery using only an explicit selector and port.

```text
client Pod → Service DNS → Calico ingress policy → restricted API Pod
```

Use a dedicated kind cluster with a policy-capable CNI. Submit the resource graph, DNS and endpoint evidence, positive and negative policy traces, an admission rejection, and the scope of the PodDisruptionBudget.

<details>
<summary>Reference manifests and check</summary>

[Client](client.yaml) · [Ingress denial](deny-ingress.yaml) · [Client allow rule](allow-client.yaml) · [Disruption budget](disruption.yaml)

```sh
bash 01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/labs/run.sh platform
```

</details>
