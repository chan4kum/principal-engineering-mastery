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

## Guided walkthrough

Follow an API request from the bytes a client writes to the response it receives. Each stage has its own evidence. A successful DNS lookup establishes a name-to-address result, a TCP handshake establishes transport, and an HTTP response shows that an HTTP-speaking component replied.

### Bytes, links, and routing (A02.01–A02.10)

1. **Serialization.** A wire format specifies widths, byte order, and how a receiver finds message boundaries. The two bytes `02 01` encode `513` in big-endian order and `258` in little-endian order. Validate the declared length against the available bytes and the protocol’s maximum before accepting a frame.
2. **Interfaces and NICs.** A network interface is the OS attachment for a link. It can represent a physical NIC, a virtual link, or loopback. A service bound to loopback can answer local requests while a remote client connecting to the machine’s other address fails.
3. **OSI and TCP/IP.** Layering gives you useful boundaries for diagnosis. An HTTPS message is protected by TLS and carried by a transport, then by IP and the local link. For HTTP/1.1 over TCP, each layer adds its own information. A byte count depends on which layer and capture point you measure.
4. **Ethernet frames.** A frame carries source and destination MAC addresses and an EtherType or length field. Its on-wire representation can include padding and a frame check sequence that the capture may omit. A short capture alone does not establish that a runt frame went across the wire.
5. **MAC and IP.** IP identifies where the packet is routed. The MAC address identifies a next hop on the current Ethernet link. When the destination is remote, the client sends the frame to its gateway while keeping the remote destination in the IP header, absent address translation.
6. **Packets and MTU.** The MTU bounds the IP packet an interface can carry without fragmentation at that link. An MTU of `1,420` bytes leaves `1,380` bytes for TCP data with minimal IPv4 and TCP headers. Account for options and encapsulation when computing the available payload.
7. **Addresses and CIDR.** A prefix fixes the leading address bits. An IPv4 `/24` leaves eight variable bits and describes `2⁸ = 256` addresses. That is the count of addresses in the prefix. Host assignment depends on the subnet and platform rules.
8. **Subnets and routing.** Within a selected routing table, the longest matching prefix takes precedence. A matching `/24` route beats a default `/0` route. Inspect the route selected for the destination to identify the next hop and outgoing interface.
9. **ARP and neighbor discovery.** ARP resolves an IPv4 next hop to a link-layer address on Ethernet. IPv6 uses Neighbor Discovery. For a remote destination, the relevant local neighbor is usually the gateway. An unresolved neighbor can prevent any IP packet from leaving that link.
10. **Ports and sockets.** A listening socket accepts incoming connections on a bound address and port. Established TCP connections can share the server port because their client endpoint differs. The source and destination IP addresses and ports identify a connection within the relevant network context.

### Discovery, transport, and trust (A02.11–A02.18)

11. **DNS resolution and caching.** A recursive resolver can return a cached response until its associated TTL expires. During a record change, clients with different cache histories may see different addresses. Record the queried name, resolver, returned address, and TTL before interpreting a rollout result.
12. **NAT and PAT.** NAT translates addresses. Port address translation lets several internal flows share a public address by allocating distinct external ports and maintaining state for replies. Capacity depends on which mappings and ports the device can use for the traffic pattern.
13. **TCP handshake.** The initiator sends `SYN`, the peer replies `SYN-ACK`, and the initiator acknowledges it. The handshake synchronizes sequence state. The TLS handshake and application readiness require their own evidence.
14. **TCP sequence numbers, ACKs, retransmission, and flow control.** TCP numbers bytes. If contiguous bytes `100` through `104` arrive, cumulative ACK `105` means the receiver expects byte `105` next. Missing data can trigger retransmission, and the advertised receive window limits how much data the receiver is prepared to accept.
15. **UDP datagrams.** Each send creates a separate datagram. UDP itself provides no delivery, ordering, or retransmission guarantee. If the receive buffer is too small, the received datagram can be truncated. The next receive handles the next datagram.
16. **TCP congestion control.** The congestion window limits how much data the sender can have in flight based on network feedback. The receive window serves a separate purpose. A `100 Mb/s` path at `40 ms` RTT needs about `500,000` bytes in flight to fill the path, before overhead and loss.
17. **TLS handshake and certificates.** TLS negotiates session keys and typically authenticates the server with a certificate. Check that the certificate chains to a configured trust anchor and that the intended hostname matches. A TCP connection can succeed while either TLS check fails.
18. **TLS termination and mTLS.** A proxy that terminates TLS decrypts the incoming connection. Encryption and peer verification on the upstream hop are configured independently. With mutual TLS, peers authenticate via certificates. Explain that trust boundary per hop when tracing service identity.

### HTTP and connection behavior (A02.19–A02.28)

19. **HTTP methods.** Method semantics describe the request’s intended effect. `GET` is safe in that sense. An idempotent operation such as replacing a resource with the same `PUT` representation has the same intended effect when repeated. The responses can still differ.
20. **HTTP headers and status codes.** Headers carry metadata such as content type and caching policy. A `504` means a gateway or proxy timed out waiting for an upstream response. A later upstream `200` can coexist with that `504` because the client-facing response was already decided.
21. **Keep-alive and connection pooling.** Reuse spreads connection setup costs over multiple requests. For example, an 80 ms setup cost over 20 requests contributes 4 ms per request on average. Size pools for actual concurrency and handle connections that peers close while idle.
22. **HTTP/1.1, HTTP/2, and HTTP/3.** HTTP/1.1 typically uses multiple connections to achieve concurrency. HTTP/2 multiplexes streams on one TCP connection. HTTP/3 uses QUIC streams. The shared transport and its loss behavior matter when evaluating latency between streams.
23. **Reverse proxies and load balancers.** A reverse proxy receives client requests and forwards them upstream. A load-balancing policy selects an eligible backend. Check which component generated an error and which upstream it attempted before attributing the response to application code.
24. **REST and gRPC.** A REST-style interface typically presents resources through HTTP semantics. gRPC presents typed remote methods with a defined message format. In its HTTP/2 mapping, each gRPC message has a compression flag and a four-byte big-endian length prefix. HTTP status and gRPC status convey different information.
25. **WebSockets, SSE, and long polling.** WebSockets support messages in both directions over an established connection. Server-sent events stream events from the server over HTTP. Long polling holds a request until data or a timeout, then the client reconnects. Traffic direction and reconnect behavior drive the choice.
26. **TCP head-of-line blocking.** TCP provides an ordered byte stream. If a segment is missing, later bytes can arrive but remain unavailable to the application until the gap is filled. This can delay several HTTP/2 streams that share that connection.
27. **QUIC streams.** QUIC orders bytes within each stream. A loss affecting one stream does not inherently block delivery of data already received on another. Streams still share congestion control and connection-level limits, so loss can reduce throughput for the connection as a whole.
28. **HTTP streaming and backpressure.** If a producer writes faster than a consumer reads, queued bytes accumulate. A bounded buffer can pause the producer or trigger an explicit overflow policy. At a net gain of `32 KiB/s`, an empty `128 KiB` buffer fills in four seconds.

### Reliability and diagnosis (A02.29–A02.38)

29. **Retries and deadlines.** Attempts, backoff, and processing all consume the caller’s overall budget. If 60 ms remain and a retry needs at least 80 ms, skip it. Use bounded retry counts and jitter to avoid synchronized retry traffic.
30. **Connect, read, and overall timeouts.** Connect timeout bounds establishing the connection. A read inactivity timeout can reset whenever a new chunk arrives, depending on the client. An overall deadline limits the complete operation even when a trickle of bytes prevents the inactivity timer from firing.
31. **Idempotent actions.** A timed-out client may retry after the server committed the first attempt. For a mutation, atomically associate a scoped idempotency key and request fingerprint with the operation or its stored result. Otherwise, a retry can repeat the side effect or replay a result for different input.
32. **Service discovery and retries.** Discovery supplies candidate endpoints. Retrying a failed instance from an unchanged list can repeat the failure. Use fresh health or discovery information to select a different eligible instance when the remaining deadline permits a retry.
33. **Connection exhaustion.** Open connections consume file descriptors and memory. New outbound flows may also use ephemeral ports and translation state. A steady rate of `1,000` new connections per second and a `30 s` average lifetime imply about `30,000` concurrent connections. Measure the limiting resource before changing its cap.
34. **Proxy buffering.** A proxy can accumulate upstream bytes before forwarding them. Chunk emission at the upstream therefore does not necessarily equal chunk arrival at the client. Compare upstream and downstream timestamps when investigating delayed events, then evaluate the buffering policy for that route.
35. **DNS TTL and failover.** TTL governs cache reuse. Some clients still have old answers when DNS changes, and existing connections can outlive the TTL. Test both fresh lookups and existing connection behavior when planning a failover.
36. **Load-balancer health checks.** Health probes sample readiness at an interval. With probes every five seconds and two consecutive failures required, detection can take roughly five to ten seconds depending on when the failure starts, plus probe and propagation delays. Existing flows may follow a separate draining policy.
37. **Cross-region latency.** Put the round trips on the critical path. Three sequential exchanges at `80 ms` RTT impose about `240 ms` of network latency before processing. Reuse connections, remove dependent calls, or move required coordination closer when the consistency requirements permit it.
38. **Packet capture and distributed traces.** A packet capture shows transport events at a particular interface. A trace ties together application spans. Correlate a narrow time window, connection endpoints, and a trusted request ID where available. Encrypted payloads and clock differences limit what you can infer from either source alone.

For a request that ended in `504`, build the timeline in order. Resolve the name, identify the chosen peer, check transport and TLS, then compare the proxy’s deadline with the upstream span. Name the last successful phase, the first concrete failure, and the first recovery probe that succeeded. This makes the diagnosis testable even when several components report different outcomes for the same request.

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

Continue to [A03 · Python Runtime & Backend API Engineering](../A03-python-runtime-and-backend-apis/README.md) after the exit gate.
