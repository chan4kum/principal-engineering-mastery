# Progress tracker

Active lesson:

Active project:

Next checkpoint:

- [ ] Score all five Stage 0 diagnostics and record gaps
- [ ] Complete A01 knowledge checks
- [ ] Reproduce L1 process anatomy
- [ ] Reproduce L2 CPU versus I/O
- [ ] Reproduce L3 memory pressure
- [ ] Reproduce L4 thread safety
- [ ] Pass Linux resource explorer acceptance tests
- [ ] Build concurrent task runner independently and pass acceptance tests
- [ ] Score at least 80% on fresh applied questions and diagnose unfamiliar failure
- [ ] Pass delayed re-test and teach back a syscall trace and resource failure

## A01 lesson evidence

- [ ] [A01.01](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.01.md) · binary and units
- [ ] [A01.02](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.02.md) · bits/bytes/words
- [ ] [A01.03](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.03.md) · signed integer encoding
- [ ] [A01.04](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.04.md) · CPU instruction sets
- [ ] [A01.05](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.05.md) · machine code vs source vs bytecode
- [ ] [A01.06](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.06.md) · what a program is
- [ ] [A01.07](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.07.md) · files and persistent storage
- [ ] [A01.08](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.08.md) · RAM vs cache vs registers
- [ ] [A01.09](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.09.md) · fetch-decode-execute
- [ ] [A01.10](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.10.md) · CPU register and program counter
- [ ] [A01.11](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.11.md) · kernel vs user mode
- [ ] [A01.12](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.12.md) · boot and system calls
- [ ] [A01.13](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.13.md) · process creation and lifetime
- [ ] [A01.14](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.14.md) · PID/PPID and parent-child tree
- [ ] [A01.15](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.15.md) · process address space
- [ ] [A01.16](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.16.md) · stack frames and call stacks
- [ ] [A01.17](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.17.md) · heap allocation
- [ ] [A01.18](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.18.md) · virtual memory and page tables
- [ ] [A01.19](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.19.md) · page faults, swap and TLB
- [ ] [A01.20](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.20.md) · threads and shared address space
- [ ] [A01.21](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.21.md) · context switching
- [ ] [A01.22](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.22.md) · scheduler and CPU timeslices
- [ ] [A01.23](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.23.md) · interrupts and traps
- [ ] [A01.24](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.24.md) · file descriptors and sockets
- [ ] [A01.25](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.25.md) · race conditions and synchronization
- [ ] [A01.26](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.26.md) · mutexes/semaphores/atomics
- [ ] [A01.27](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.27.md) · deadlock/livelock/starvation
- [ ] [A01.28](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.28.md) · CPU affinity and NUMA
- [ ] [A01.29](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.29.md) · cache hierarchy and false sharing
- [ ] [A01.30](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.30.md) · I/O blocking and async
- [ ] [A01.31](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.31.md) · mmap and copy-on-write
- [ ] [A01.32](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.32.md) · memory accounting RSS/PSS
- [ ] [A01.33](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.33.md) · cgroups and namespaces
- [ ] [A01.34](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.34.md) · container limits vs host resources
- [ ] [A01.35](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.35.md) · CPU throttling and OOMKilled
- [ ] [A01.36](01-architecture-A01-to-A20/A01-computer-systems-and-os/lessons/A01.36.md) · ARM vs x86 and cross-architecture deployment

## Review schedule

| Skill | First pass | D+1 | D+3 | D+7 | D+14 | D+30 | D+60 |
| --- | --- | --- | --- | --- | --- | --- | --- |

Enter a date and result in each review cell. Repeat missed questions with a fresh input and revise the next interval when recall fails.

## Error log

| Date and skill ID | Prediction or wrong assumption | Command, units and evidence | Corrected mechanism | Next review |
| --- | --- | --- | --- | --- |

Keep machine-specific traces, file paths and identifiers in your local copy.

## A02 evidence

- [ ] Reproduce L1 packet path
- [ ] Reproduce L2 TLS chain
- [ ] Reproduce L3 NAT and routing
- [ ] Reproduce L4 proxy timeouts
- [ ] Pass both A02 project suites
- [ ] Pass fresh applied assessment and delayed re-test

### A02 lessons

- [ ] [A02.01](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.01.md) · bits-to-bytes serialization
- [ ] [A02.02](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.02.md) · network interface and NIC
- [ ] [A02.03](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.03.md) · OSI vs TCP/IP
- [ ] [A02.04](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.04.md) · Ethernet frames
- [ ] [A02.05](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.05.md) · MAC vs IP
- [ ] [A02.06](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.06.md) · packets and MTU
- [ ] [A02.07](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.07.md) · IP addresses and CIDR
- [ ] [A02.08](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.08.md) · subnets and routing
- [ ] [A02.09](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.09.md) · ARP/neighbor discovery
- [ ] [A02.10](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.10.md) · ports and sockets
- [ ] [A02.11](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.11.md) · DNS resolution and caching
- [ ] [A02.12](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.12.md) · NAT and PAT
- [ ] [A02.13](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.13.md) · TCP three-way handshake
- [ ] [A02.14](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.14.md) · sequence numbers, ACKs, retransmission and flow control
- [ ] [A02.15](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.15.md) · UDP datagrams
- [ ] [A02.16](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.16.md) · TCP congestion control
- [ ] [A02.17](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.17.md) · TLS handshake and certificates
- [ ] [A02.18](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.18.md) · TLS termination and mTLS
- [ ] [A02.19](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.19.md) · HTTP methods and semantics
- [ ] [A02.20](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.20.md) · headers/statuses
- [ ] [A02.21](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.21.md) · keep-alive and connection pooling
- [ ] [A02.22](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.22.md) · HTTP/1.1 vs HTTP/2 vs HTTP/3
- [ ] [A02.23](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.23.md) · reverse proxy and load balancer
- [ ] [A02.24](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.24.md) · REST vs gRPC
- [ ] [A02.25](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.25.md) · WebSockets, SSE and long polling
- [ ] [A02.26](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.26.md) · TCP head-of-line blocking
- [ ] [A02.27](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.27.md) · QUIC streams
- [ ] [A02.28](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.28.md) · HTTP streaming and backpressure
- [ ] [A02.29](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.29.md) · retries and deadline budgets
- [ ] [A02.30](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.30.md) · connect vs read vs overall timeouts
- [ ] [A02.31](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.31.md) · idempotent network actions
- [ ] [A02.32](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.32.md) · service discovery and retries
- [ ] [A02.33](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.33.md) · connection exhaustion
- [ ] [A02.34](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.34.md) · proxy buffering
- [ ] [A02.35](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.35.md) · DNS TTL and failover
- [ ] [A02.36](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.36.md) · load-balancer health checks
- [ ] [A02.37](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.37.md) · cross-region latency
- [ ] [A02.38](01-architecture-A01-to-A20/A02-networking-and-communication/lessons/A02.38.md) · packet capture and distributed traces
