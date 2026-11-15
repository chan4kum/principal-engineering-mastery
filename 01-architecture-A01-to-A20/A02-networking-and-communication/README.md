# A02 · Networking & Communication

**38 lessons · 4 labs · 2 projects**

Follow a request from serialization and link delivery through transport, TLS, HTTP and failure diagnosis. IDs and titles follow the detailed roadmap and the V3 audited curriculum.

**Prerequisites.** [Stage 0](../../00-stage-0-diagnostic/README.md) and the [A01 exit gate](../A01-computer-systems-and-os/README.md#practice-and-exit-gate). For container labs, install Docker with Compose v2. macOS runners use a local Linux VM. No lab publishes a host port or needs a paid cloud account.

| ID | Lesson | Tier |
| --- | --- | --- |
| [A02.01](lessons/A02.01.md) | bits-to-bytes serialization | Foundation |
| [A02.02](lessons/A02.02.md) | network interface and NIC | Foundation |
| [A02.03](lessons/A02.03.md) | OSI vs TCP/IP | Foundation |
| [A02.04](lessons/A02.04.md) | Ethernet frames | Foundation |
| [A02.05](lessons/A02.05.md) | MAC vs IP | Foundation |
| [A02.06](lessons/A02.06.md) | packets and MTU | Foundation |
| [A02.07](lessons/A02.07.md) | IP addresses and CIDR | Foundation |
| [A02.08](lessons/A02.08.md) | subnets and routing | Foundation |
| [A02.09](lessons/A02.09.md) | ARP/neighbor discovery | Foundation |
| [A02.10](lessons/A02.10.md) | ports and sockets | Foundation |
| [A02.11](lessons/A02.11.md) | DNS resolution and caching | Core |
| [A02.12](lessons/A02.12.md) | NAT and PAT | Core |
| [A02.13](lessons/A02.13.md) | TCP three-way handshake | Core |
| [A02.14](lessons/A02.14.md) | sequence numbers, ACKs, retransmission and flow control | Core |
| [A02.15](lessons/A02.15.md) | UDP datagrams | Core |
| [A02.16](lessons/A02.16.md) | TCP congestion control | Core |
| [A02.17](lessons/A02.17.md) | TLS handshake and certificates | Core |
| [A02.18](lessons/A02.18.md) | TLS termination and mTLS | Core |
| [A02.19](lessons/A02.19.md) | HTTP methods and semantics | Core |
| [A02.20](lessons/A02.20.md) | headers/statuses | Core |
| [A02.21](lessons/A02.21.md) | keep-alive and connection pooling | Core |
| [A02.22](lessons/A02.22.md) | HTTP/1.1 vs HTTP/2 vs HTTP/3 | Core |
| [A02.23](lessons/A02.23.md) | reverse proxy and load balancer | Core |
| [A02.24](lessons/A02.24.md) | REST vs gRPC | Core |
| [A02.25](lessons/A02.25.md) | WebSockets, SSE and long polling | Core |
| [A02.26](lessons/A02.26.md) | TCP head-of-line blocking | Principal |
| [A02.27](lessons/A02.27.md) | QUIC streams | Principal |
| [A02.28](lessons/A02.28.md) | HTTP streaming and backpressure | Principal |
| [A02.29](lessons/A02.29.md) | retries and deadline budgets | Principal |
| [A02.30](lessons/A02.30.md) | connect vs read vs overall timeouts | Principal |
| [A02.31](lessons/A02.31.md) | idempotent network actions | Principal |
| [A02.32](lessons/A02.32.md) | service discovery and retries | Principal |
| [A02.33](lessons/A02.33.md) | connection exhaustion | Principal |
| [A02.34](lessons/A02.34.md) | proxy buffering | Principal |
| [A02.35](lessons/A02.35.md) | DNS TTL and failover | Principal |
| [A02.36](lessons/A02.36.md) | load-balancer health checks | Principal |
| [A02.37](lessons/A02.37.md) | cross-region latency | Principal |
| [A02.38](lessons/A02.38.md) | packet capture and distributed traces | Principal |

## Practice and exit gate

- [L1 · Packet path](labs/L1.md)
- [L2 · TLS chain](labs/L2.md)
- [L3 · NAT and routing](labs/L3.md)
- [L4 · Proxy timeouts](labs/L4.md)
- [Guided project · Packet-to-API network explorer](projects/guided/README.md)
- [Independent project · Network fault-injection and request-path debugger](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs, pass both project suites and score at least 80% on fresh applied questions. Diagnose one unfamiliar failure and pass a delayed re-test. Bring a request timeline showing the last verified hop, the failure evidence and the first successful recovery probe.

## Evidence and scope

The A02 IDs and source titles were cross-checked against the detailed roadmap and V3 audited index. Each lesson links to the relevant standard or implementation documentation, reviewed in November 2026. The examples label live observations and simplified models. Use L1–L4 for the actual request path and container behavior. The supported Python baseline is 3.12.

## Protocol references

- Transport framing and sequence behavior. [TCP RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html)
- Trust and key negotiation. [TLS 1.3 RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.html)
- Application methods and status semantics. [HTTP RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)
- Stream isolation and flow limits. [QUIC RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)
- RPC wire framing. [gRPC over HTTP/2](https://grpc.github.io/grpc/core/md_doc__p_r_o_t_o_c_o_l-_h_t_t_p2.html)
- Buffering and phase timeouts. [NGINX proxy module](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)
