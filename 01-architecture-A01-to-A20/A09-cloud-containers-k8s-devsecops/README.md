# A09 · Cloud, Containers, Kubernetes & Platform Engineering

**33 lessons · 4 labs · 2 projects**

Build deployable artifacts and reason about reconciliation, service connectivity and workload boundaries. The local labs use disposable kind clusters and never provision paid infrastructure.

Prerequisite [A08 exit gate](../A08-reliability-operations-and-sre/README.md#practice-and-exit-gate).

| ID | Lesson | Tier |
| --- | --- | --- |
| [A09.01](lessons/A09.01.md) | Linux processes/namespaces/cgroups | Foundation |
| [A09.02](lessons/A09.02.md) | filesystems | Foundation |
| [A09.03](lessons/A09.03.md) | image vs container | Foundation |
| [A09.04](lessons/A09.04.md) | Dockerfile layers and cache | Foundation |
| [A09.05](lessons/A09.05.md) | image registries | Foundation |
| [A09.06](lessons/A09.06.md) | virtual networks | Foundation |
| [A09.07](lessons/A09.07.md) | IAM principles | Foundation |
| [A09.08](lessons/A09.08.md) | DNS and TLS | Foundation |
| [A09.09](lessons/A09.09.md) | Docker multi-stage/non-root | Core |
| [A09.10](lessons/A09.10.md) | Compose and persistent volumes | Core |
| [A09.11](lessons/A09.11.md) | CI/CD | Core |
| [A09.12](lessons/A09.12.md) | GitOps | Core |
| [A09.13](lessons/A09.13.md) | IaC/Terraform | Core |
| [A09.14](lessons/A09.14.md) | VPC, subnets, routes, NAT and endpoints | Core |
| [A09.15](lessons/A09.15.md) | IAM, KMS, secrets | Core |
| [A09.16](lessons/A09.16.md) | EKS/AKS | Core |
| [A09.17](lessons/A09.17.md) | pod, deployment, service and ingress/gateway | Core |
| [A09.18](lessons/A09.18.md) | scheduling, requests/limits and probes | Core |
| [A09.19](lessons/A09.19.md) | HPA | Core |
| [A09.20](lessons/A09.20.md) | workloads and PVC | Core |
| [A09.21](lessons/A09.21.md) | network policies | Core |
| [A09.22](lessons/A09.22.md) | CKAD workflows and debugging | Principal |
| [A09.23](lessons/A09.23.md) | CNI/CoreDNS/kube-proxy | Principal |
| [A09.24](lessons/A09.24.md) | resource quotas | Principal |
| [A09.25](lessons/A09.25.md) | pod disruption budgets | Principal |
| [A09.26](lessons/A09.26.md) | rolling/canary deploy | Principal |
| [A09.27](lessons/A09.27.md) | workload identity | Principal |
| [A09.28](lessons/A09.28.md) | software supply chain SBOM/scanning | Principal |
| [A09.29](lessons/A09.29.md) | admission controls | Principal |
| [A09.30](lessons/A09.30.md) | GPU scheduling and topology | Principal |
| [A09.31](lessons/A09.31.md) | node autoscalers | Principal |
| [A09.32](lessons/A09.32.md) | AWS Bedrock/SageMaker integration | Principal |
| [A09.33](lessons/A09.33.md) | FinOps and multi-AZ resilience | Principal |

## Practice and exit gate

- [L1 · Container lab](labs/L1.md)
- [L2 · Kubernetes reconciliation](labs/L2.md)
- [L3 · Service connectivity](labs/L3.md)
- [L4 · GitOps drift](labs/L4.md)
- [Guided · Containerized API on local Kubernetes](projects/guided/README.md)
- [Independent · Secure multi-service Kubernetes platform](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Demonstrate a locally deployable workload, troubleshoot one broken path, and justify a secure rollout and recovery policy.

Continue to [A10 · ML Foundations, AI Math & MLOps](../A10-ml-foundations-math-and-mlops/README.md) when the prerequisite stage gates are met.
