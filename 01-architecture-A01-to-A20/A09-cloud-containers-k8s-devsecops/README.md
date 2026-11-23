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

## Guided walkthrough

Follow an application from a local container to an authenticated and observable cloud workload.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Understand the container and cloud primitives (A09.01–A09.08)

1. **[A09.01 · Linux processes/namespaces/cgroups](lessons/A09.01.md).** Linux namespaces isolate certain views. Control groups account for and constrain resources. A PID namespace can change visible process IDs without providing a CPU budget. A 25 ms quota per 100 ms yields 0.25 CPU of sustained quota in the simple model.
2. **[A09.02 · filesystems](lessons/A09.02.md).** An image contributes read-only layers and the container has a writable layer. A volume attaches storage with a separate lifecycle. Mounting over a directory can hide its prior contents. If ten replicas each write 50 MiB into separate writable layers, they consume 500 MiB before snapshots and filesystem overhead.
3. **[A09.03 · image vs container](lessons/A09.03.md).** An image packages filesystem and configuration. A container is a running or stopped instance with instance-specific state. Replacing an image tag does not modify processes already running. Three running replicas from an old digest stay old until replacements occur, even if the tag now points at a new digest.
4. **[A09.04 · Dockerfile layers and cache](lessons/A09.04.md).** Docker reuses cached build decisions when the relevant instructions and inputs stay compatible. Copying rapidly changing source before dependency preparation can invalidate that work. At 20 source-only changes and 15 s installs, misplaced copies cost up to 300 s in the simple model.
5. **[A09.05 · image registries](lessons/A09.05.md).** Registries store blobs, manifests and indexes. Tags can be reassigned. A digest identifies content. Multi-platform indexes can point to separate platform manifests. A two-platform index with one manifest per platform references at least two image manifests, apart from any attestations.
6. **[A09.06 · virtual networks](lessons/A09.06.md).** Isolated network namespaces have their own interface and port views. Peer services may reach containers through virtual networking. Publishing creates a host-facing binding. Two different containers can both bind 8080. Publishing both on the same host IP and transport port requests one colliding endpoint.
7. **[A09.07 · IAM principles](lessons/A09.07.md).** IAM separates principals, credentials, actions and resource policy. Least privilege scopes actions to what the workload actually needs. Default deny and emergency access need explicit policy. A policy with two of ten possible actions enables 20% of that simplified action set. Resource and condition scope can further restrict it.
8. **[A09.08 · DNS and TLS](lessons/A09.08.md).** DNS maps a name to an address. TLS authenticates the endpoint under chain and name policies. A successful DNS answer does not establish that the certificate is usable. One TCP round trip plus one normal full TLS 1.3 round trip over a 20 ms path contributes about 40 ms before app data, excluding DNS and processing.

### Deploy and operate Kubernetes workloads (A09.09–A09.21)

9. **[A09.09 · Docker multi-stage/non-root](lessons/A09.09.md).** Multi-stage builds copy selected artifacts to a smaller runtime stage. A non-root user constrains ordinary process rights. Read-only and capability limits add separate guardrails. If build tools add 150 MiB to a 75 MiB runtime, copying them increases the image size to 225 MiB in the simple model.
10. **[A09.10 · Compose and persistent volumes](lessons/A09.10.md).** Compose describes multiple services and persistent volume attachments. Removing the volume or using only a container's writable layer can discard data when the container is recreated. Four replacements with one retained volume can preserve one data history. Four independent ephemeral layers produce four distinct histories.
11. **[A09.11 · CI/CD](lessons/A09.11.md).** CI verifies a build, while CD promotes a verified artifact through environments or gates. Rebuilding can introduce dependency and input drift. Three environments can reference one tested digest. Independent rebuilds produce up to three distinct candidate artifacts.
12. **[A09.12 · GitOps](lessons/A09.12.md).** GitOps uses declarative, versioned desired state with automated reconciliation. Manual apply can demonstrate drift repair but does not provide a continuous controller by itself. Three field edits outside the declared process can create three drift items even if the application remains healthy.
13. **[A09.13 · IaC/Terraform](lessons/A09.13.md).** Infrastructure as code describes resources and change plans. Terraform state maps declarations to remote objects. Certain backends provide locking. Plans can change when external state changes. If an infrastructure graph has 12 resources and a plan changes two, inspect those two operations and all affected dependencies before applying.
14. **[A09.14 · VPC, subnets, routes, NAT and endpoints](lessons/A09.14.md).** A VPC gives routing and policy boundaries. Subnets select address ranges, route tables select next hops, NAT modifies traffic, and endpoints can avoid internet egress where supported. A /24 contains 256 addresses before reservations. Capacity planning must include provider-specific reservations and per-workload allocation.
15. **[A09.15 · IAM, KMS, secrets](lessons/A09.15.md).** IAM authorizes actions, a key-management service protects key use, and secret storage controls which workloads can retrieve material. Encryption at rest and runtime access serve different purposes. If five consumers need a secret and only two are authorized, three should receive no plaintext.
16. **[A09.16 · EKS/AKS](lessons/A09.16.md).** EKS and AKS supply managed Kubernetes control planes plus provider-specific integrations for networking, identity, storage and operations. Portable objects can still rely on provider-specific classes and controllers. Three portable manifests and two cloud-specific dependencies require validating all five integration pieces during a migration.
17. **[A09.17 · pod, deployment, service and ingress/gateway](lessons/A09.17.md).** A Pod runs containers, a Deployment manages replicated Pod templates, a Service selects backends, and an ingress or gateway needs a matching controller and route. With three matching pods and one unready, a normal ready-endpoint route can send to two healthy pods in this model.
18. **[A09.18 · scheduling, requests/limits and probes](lessons/A09.18.md).** Requests guide scheduling and some policy. Limits constrain runtime resources. Probes govern readiness or restart actions. A failing startup can require a dedicated startup probe. A 2-core allocatable node can fit eight 250m CPU requests if CPU is the only constraint.
19. **[A09.19 · HPA](lessons/A09.19.md).** HPA uses metrics and configured targets with control-loop behavior. Resource utilization can depend on requested values. Scaling Pods does not create downstream capacity. With four replicas, observed utilization 80% and target 50%, ceil(4×80/50)=7 before tolerance and safeguards.
20. **[A09.20 · workloads and PVC](lessons/A09.20.md).** A PVC requests storage. Binding depends on class, access modes and topology. Stateful controllers can give workloads stable identities and volume claims. Backup is separate from placement. Three replicas with one 20 GiB claim each request 60 GiB. Actual costs and capacity depend on storage class and retention.
21. **[A09.21 · network policies](lessons/A09.21.md).** NetworkPolicy is enforced only by a supporting network plugin. Ingress and egress isolation and additive allow rules are scoped to selected Pods. Allowing one of three client groups leaves two groups denied for that isolated path if no other policy permits them.

### Verify platform safety, scaling, and cost (A09.22–A09.33)

22. **[A09.22 · CKAD workflows and debugging](lessons/A09.22.md).** Troubleshooting begins with desired state, events, controller status and logs. Scheduling failures and crashing containers need different evidence. A Deployment asking for two replicas but reporting zero scheduled exposes two unplaced replicas. Raising application timeouts does not schedule them.
23. **[A09.23 · CNI/CoreDNS/kube-proxy](lessons/A09.23.md).** CNI provides Pod networking, CoreDNS answers cluster DNS queries, and a Service data plane routes to eligible endpoints. Some implementations replace kube-proxy. If there are two Pods but neither is selected, DNS resolution can still succeed and the Service has zero selected backends.
24. **[A09.24 · resource quotas](lessons/A09.24.md).** ResourceQuota restricts aggregate namespace resources. Limits and requests govern individual Pods, and admission may require declarations for quota-controlled resources. With a 2 CPU request quota and 250m requests per Pod, at most eight fit before other usage.
25. **[A09.25 · pod disruption budgets](lessons/A09.25.md).** A PodDisruptionBudget limits some voluntary disruptions using the eviction API. It does not prevent node failures, and direct deletion bypasses eviction checks. With three ready Pods and minAvailable two, at most one can be voluntarily disrupted under the simple healthy model.
26. **[A09.26 · rolling/canary deploy](lessons/A09.26.md).** Rolling deployment controls updated and unavailable replicas. A canary intentionally offers part of traffic to a new version, which needs routing and evaluation evidence. A 5% cohort of 2000 RPS receives about 100 RPS under even routing.
27. **[A09.27 · workload identity](lessons/A09.27.md).** Workload identity maps a Kubernetes workload identity to cloud authority through provider-specific federation. Scope issuer, audience, subject and permissions. Four workloads needing different actions can have four scoped identities rather than sharing one blanket identity.
28. **[A09.28 · software supply chain SBOM/scanning](lessons/A09.28.md).** An SBOM inventories components. Scanning matches versions and context against a vulnerability database. Provenance and signatures address artifact origin and integrity separately. A scan of 80 components reporting two matches covers all 80 inventoried components only under the scanner's visibility assumptions.
29. **[A09.29 · admission controls](lessons/A09.29.md).** Admission checks an API request before persistence and scheduling. Some controllers mutate requests. Validating policy rejects invalid state. Audit existing objects separately. If one of five workloads violates a relevant rule, enforcing it can reject that one request while accepting four modeled valid requests.
30. **[A09.30 · GPU scheduling and topology](lessons/A09.30.md).** Kubernetes exposes devices as resources through supported plugins. Device count does not promise interconnect or locality. Placement and topology need explicit runtime support. A four-device node can serve two jobs asking for two devices each if no other constraints apply.
31. **[A09.31 · node autoscalers](lessons/A09.31.md).** A node autoscaler responds to eligible unschedulable demand and deployment constraints. Node startup and image pulls impose delay, and not every Pending Pod is solvable with more nodes. Ten Pods requesting 500m each demand five CPU cores before overhead and packing constraints.
32. **[A09.32 · AWS Bedrock/SageMaker integration](lessons/A09.32.md).** Amazon Bedrock and SageMaker provide distinct model access and deployment workflows. Both require deliberate authentication, regional support, connectivity, timeout and cost planning. With 100 requests each using 500 input and 200 output tokens, total input is 50000 and output is 20000 tokens. Cost requires actual provider meters.
33. **[A09.33 · FinOps and multi-AZ resilience](lessons/A09.33.md).** FinOps compares measured unit costs and utilization with reliability objectives. Multi-zone placement protects only independent paths with enough surviving capacity. Four replicas at 200 RPS each placed two per zone leave 400 RPS after loss of either zone under balanced capacity.

### Put it together

When a new release stalls, distinguish Pending pods from running but unready pods. Compare resource requests with node headroom for the first case, and inspect readiness and dependency behavior for the second. Then verify that routing only sends traffic to eligible endpoints and that rollback restores successful requests.

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
