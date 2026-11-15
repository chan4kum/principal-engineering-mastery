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

## A03 evidence

- [ ] Reproduce all four labs
- [ ] Pass both project suites
- [ ] Pass fresh assessment and delayed re-test

- [ ] [A03.01](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.01.md) · Python execution pipeline
- [ ] [A03.02](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.02.md) · compilation to bytecode
- [ ] [A03.03](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.03.md) · object identity and references
- [ ] [A03.04](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.04.md) · mutability and aliasing
- [ ] [A03.05](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.05.md) · reference counting/cyclic GC
- [ ] [A03.06](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.06.md) · list/dict runtime costs
- [ ] [A03.07](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.07.md) · iterators/generators
- [ ] [A03.08](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.08.md) · type hints
- [ ] [A03.09](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.09.md) · exceptions and context managers
- [ ] [A03.10](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.10.md) · Python GIL and concurrency scope
- [ ] [A03.11](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.11.md) · coroutines, await and cooperative scheduling
- [ ] [A03.12](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.12.md) · event loop
- [ ] [A03.13](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.13.md) · Task/Future
- [ ] [A03.14](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.14.md) · cancellation and TaskGroup
- [ ] [A03.15](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.15.md) · threads/processes and pools
- [ ] [A03.16](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.16.md) · ASGI vs WSGI
- [ ] [A03.17](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.17.md) · Uvicorn worker model
- [ ] [A03.18](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.18.md) · FastAPI route lifecycle
- [ ] [A03.19](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.19.md) · dependency injection
- [ ] [A03.20](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.20.md) · middleware
- [ ] [A03.21](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.21.md) · Pydantic validation
- [ ] [A03.22](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.22.md) · API resource modeling
- [ ] [A03.23](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.23.md) · OpenAPI
- [ ] [A03.24](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.24.md) · errors and versioning
- [ ] [A03.25](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.25.md) · authN vs authZ
- [ ] [A03.26](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.26.md) · OAuth 2.0/OIDC/JWT
- [ ] [A03.27](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.27.md) · pagination and cursor semantics
- [ ] [A03.28](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.28.md) · bounded async fanout
- [ ] [A03.29](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.29.md) · CPU/I/O work separation
- [ ] [A03.30](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.30.md) · connection pooling
- [ ] [A03.31](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.31.md) · idempotency keys
- [ ] [A03.32](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.32.md) · rate limits and quotas
- [ ] [A03.33](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.33.md) · retry/timeout propagation
- [ ] [A03.34](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.34.md) · SDK construction
- [ ] [A03.35](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.35.md) · sync vs async SDK boundary
- [ ] [A03.36](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.36.md) · request tracing
- [ ] [A03.37](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.37.md) · structured logging
- [ ] [A03.38](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.38.md) · graceful shutdown
- [ ] [A03.39](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.39.md) · API compatibility testing
- [ ] [A03.40](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.40.md) · streaming and event cancellation
- [ ] [A03.41](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.41.md) · multi-tenant context propagation
- [ ] [A03.42](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/lessons/A03.42.md) · secure client libraries

## A04 evidence

- [ ] Reproduce all four PostgreSQL labs
- [ ] Pass both project suites
- [ ] Pass fresh assessment and delayed re-test

- [ ] [A04.01](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.01.md) · bytes and pages
- [ ] [A04.02](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.02.md) · record layouts
- [ ] [A04.03](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.03.md) · relational tables, keys and constraints
- [ ] [A04.04](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.04.md) · normalization
- [ ] [A04.05](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.05.md) · SQL operations
- [ ] [A04.06](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.06.md) · query plans
- [ ] [A04.07](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.07.md) · disk seek and random vs sequential I/O
- [ ] [A04.08](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.08.md) · indexes
- [ ] [A04.09](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.09.md) · B-tree and B+tree intuition
- [ ] [A04.10](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.10.md) · ACID and transactions
- [ ] [A04.11](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.11.md) · locks
- [ ] [A04.12](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.12.md) · isolation levels
- [ ] [A04.13](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.13.md) · lost updates/phantoms
- [ ] [A04.14](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.14.md) · MVCC
- [ ] [A04.15](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.15.md) · WAL/redo/undo concepts
- [ ] [A04.16](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.16.md) · checkpoints and crash recovery
- [ ] [A04.17](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.17.md) · backup and point-in-time restore
- [ ] [A04.18](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.18.md) · schema migration and online indexing
- [ ] [A04.19](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.19.md) · keyset vs offset pagination
- [ ] [A04.20](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.20.md) · soft deletion and retention
- [ ] [A04.21](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.21.md) · document vs key-value vs graph vs columnar stores
- [ ] [A04.22](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.22.md) · PostgreSQL query analysis
- [ ] [A04.23](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.23.md) · file-backed dictionaries
- [ ] [A04.24](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.24.md) · binary encodings
- [ ] [A04.25](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.25.md) · append-only and log-structured storage
- [ ] [A04.26](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.26.md) · Bitcask
- [ ] [A04.27](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.27.md) · LSM memtable/WAL/SSTable
- [ ] [A04.28](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.28.md) · Bloom/sparse indexes
- [ ] [A04.29](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.29.md) · compaction and write amplification
- [ ] [A04.30](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.30.md) · range and hash partitioning
- [ ] [A04.31](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.31.md) · shard maps
- [ ] [A04.32](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.32.md) · object store metadata
- [ ] [A04.33](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.33.md) · consistency and replication
- [ ] [A04.34](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.34.md) · hot/cold archival
- [ ] [A04.35](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.35.md) · checksums
- [ ] [A04.36](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.36.md) · online evolution
- [ ] [A04.37](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/lessons/A04.37.md) · data privacy deletions

## A05 evidence

- [ ] Reproduce cache, queue, load and limiter labs
- [ ] Pass both project suites
- [ ] Pass fresh assessment and delayed re-test

- [ ] [A05.01](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.01.md) · time vs throughput
- [ ] [A05.02](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.02.md) · QPS/RPS/TPS
- [ ] [A05.03](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.03.md) · mean vs percentiles
- [ ] [A05.04](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.04.md) · p95/p99 and tail latency
- [ ] [A05.05](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.05.md) · Little law and assumptions
- [ ] [A05.06](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.06.md) · utilization and queue build-up
- [ ] [A05.07](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.07.md) · CPU vs I/O bottlenecks
- [ ] [A05.08](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.08.md) · back-of-envelope resource units
- [ ] [A05.09](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.09.md) · horizontal vs vertical scaling
- [ ] [A05.10](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.10.md) · load balancers and health checks
- [ ] [A05.11](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.11.md) · Redis caching
- [ ] [A05.12](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.12.md) · cache-aside/read-through/write-through
- [ ] [A05.13](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.13.md) · TTL and eviction
- [ ] [A05.14](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.14.md) · LRU/LFU
- [ ] [A05.15](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.15.md) · cache invalidation
- [ ] [A05.16](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.16.md) · cache stampedes and hot keys
- [ ] [A05.17](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.17.md) · connection pools
- [ ] [A05.18](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.18.md) · bulkheads
- [ ] [A05.19](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.19.md) · batching
- [ ] [A05.20](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.20.md) · worker queues
- [ ] [A05.21](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.21.md) · rate limiter windows, token bucket/leaky bucket
- [ ] [A05.22](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.22.md) · load shedding
- [ ] [A05.23](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.23.md) · single-flight request coalescing
- [ ] [A05.24](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.24.md) · split hot keys
- [ ] [A05.25](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.25.md) · consistency under invalidation
- [ ] [A05.26](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.26.md) · sharding and resharding
- [ ] [A05.27](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.27.md) · consistent/rendezvous hashing
- [ ] [A05.28](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.28.md) · probabilistic cache admission
- [ ] [A05.29](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.29.md) · queueing model and contention
- [ ] [A05.30](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.30.md) · cost-aware scaling
- [ ] [A05.31](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.31.md) · latency budgeting
- [ ] [A05.32](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.32.md) · experiments, benchmarks and capacity envelopes
- [ ] [A05.33](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.33.md) · failure headroom
- [ ] [A05.34](01-architecture-A01-to-A20/A05-scalability-caching-performance/lessons/A05.34.md) · autoscaling interactions

## A06 evidence

- [ ] Reproduce clocks, partition, quorum and fencing labs
- [ ] Pass both project suites
- [ ] Pass fresh assessment and delayed re-test

- [ ] [A06.01](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.01.md) · partial failure
- [ ] [A06.02](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.02.md) · time and clocks
- [ ] [A06.03](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.03.md) · network partition
- [ ] [A06.04](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.04.md) · retries and duplicates
- [ ] [A06.05](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.05.md) · delivery guarantees
- [ ] [A06.06](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.06.md) · ordering
- [ ] [A06.07](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.07.md) · monotonic sequence numbers
- [ ] [A06.08](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.08.md) · safety vs liveness
- [ ] [A06.09](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.09.md) · failure detection limits
- [ ] [A06.10](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.10.md) · consistency models
- [ ] [A06.11](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.11.md) · linearizability vs serializability
- [ ] [A06.12](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.12.md) · eventual consistency
- [ ] [A06.13](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.13.md) · leader/follower
- [ ] [A06.14](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.14.md) · quorums
- [ ] [A06.15](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.15.md) · CAP limits and PACELC
- [ ] [A06.16](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.16.md) · Lamport clocks
- [ ] [A06.17](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.17.md) · vector clocks
- [ ] [A06.18](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.18.md) · consensus/Raft
- [ ] [A06.19](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.19.md) · elections, terms and log replication
- [ ] [A06.20](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.20.md) · distributed locks, leases and fencing
- [ ] [A06.21](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.21.md) · idempotency and deduplication
- [ ] [A06.22](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.22.md) · split brain and stale lease holder
- [ ] [A06.23](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.23.md) · transaction coordination and sagas
- [ ] [A06.24](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.24.md) · metadata discovery
- [ ] [A06.25](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.25.md) · gossip and membership
- [ ] [A06.26](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.26.md) · distributed hash tables
- [ ] [A06.27](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.27.md) · consistent/rendezvous hashing
- [ ] [A06.28](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.28.md) · causal consistency
- [ ] [A06.29](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.29.md) · CRDT overview
- [ ] [A06.30](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.30.md) · clock skew
- [ ] [A06.31](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.31.md) · distributed ID/Snowflake
- [ ] [A06.32](01-architecture-A01-to-A20/A06-distributed-systems-coordination/lessons/A06.32.md) · failure injection and linearizability test design

## A07 evidence

- [ ] Reproduce worker replay, Redis Streams, saga and contract labs
- [ ] Pass both project suites
- [ ] Pass fresh assessment and delayed re-test

- [ ] [A07.01](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.01.md) · separation of concerns
- [ ] [A07.02](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.02.md) · coupling/cohesion
- [ ] [A07.03](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.03.md) · modules and packages
- [ ] [A07.04](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.04.md) · interfaces and contracts
- [ ] [A07.05](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.05.md) · state boundaries
- [ ] [A07.06](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.06.md) · monolith vs services
- [ ] [A07.07](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.07.md) · layered architecture
- [ ] [A07.08](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.08.md) · hexagonal ports/adapters
- [ ] [A07.09](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.09.md) · domain-driven design bounded contexts
- [ ] [A07.10](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.10.md) · modular monolith
- [ ] [A07.11](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.11.md) · microservices trade-offs
- [ ] [A07.12](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.12.md) · API gateway vs service
- [ ] [A07.13](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.13.md) · synchronous API vs queue vs stream
- [ ] [A07.14](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.14.md) · event contracts
- [ ] [A07.15](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.15.md) · CQRS
- [ ] [A07.16](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.16.md) · event sourcing
- [ ] [A07.17](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.17.md) · transactional outbox
- [ ] [A07.18](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.18.md) · CDC
- [ ] [A07.19](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.19.md) · saga compensation
- [ ] [A07.20](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.20.md) · Kafka event lifecycle
- [ ] [A07.21](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.21.md) · workflow engines vs event choreography
- [ ] [A07.22](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.22.md) · DAG orchestration
- [ ] [A07.23](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.23.md) · job scheduler
- [ ] [A07.24](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.24.md) · SKIP LOCKED queues
- [ ] [A07.25](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.25.md) · rule engines
- [ ] [A07.26](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.26.md) · replay and poison messages
- [ ] [A07.27](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.27.md) · schema registry
- [ ] [A07.28](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.28.md) · backward compatible events
- [ ] [A07.29](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.29.md) · change-safe database migrations
- [ ] [A07.30](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.30.md) · tenancy boundaries
- [ ] [A07.31](01-architecture-A01-to-A20/A07-application-integration-arch/lessons/A07.31.md) · architecture decision records and decomposition cost

## A08 evidence

- [ ] Reproduce telemetry, SLO, backup and game-day labs
- [ ] Pass both project suites
- [ ] Pass fresh assessment and delayed re-test

- [ ] [A08.01](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.01.md) · availability vs durability
- [ ] [A08.02](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.02.md) · SLIs/SLOs/SLAs
- [ ] [A08.03](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.03.md) · reliability budget
- [ ] [A08.04](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.04.md) · success and failure definition
- [ ] [A08.05](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.05.md) · metrics/logs/traces
- [ ] [A08.06](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.06.md) · structured correlation IDs
- [ ] [A08.07](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.07.md) · timeout hierarchy
- [ ] [A08.08](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.08.md) · retry/backoff/jitter
- [ ] [A08.09](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.09.md) · circuit breaker
- [ ] [A08.10](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.10.md) · bulkhead
- [ ] [A08.11](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.11.md) · fallback
- [ ] [A08.12](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.12.md) · backpressure and admission control
- [ ] [A08.13](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.13.md) · health checks
- [ ] [A08.14](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.14.md) · graceful shutdown
- [ ] [A08.15](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.15.md) · error budgets
- [ ] [A08.16](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.16.md) · alerts and runbooks
- [ ] [A08.17](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.17.md) · on-call triage
- [ ] [A08.18](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.18.md) · backups, restore and disaster recovery
- [ ] [A08.19](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.19.md) · RPO and RTO
- [ ] [A08.20](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.20.md) · fault injection and chaos tests
- [ ] [A08.21](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.21.md) · cascading failures
- [ ] [A08.22](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.22.md) · retry storms
- [ ] [A08.23](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.23.md) · failure domains
- [ ] [A08.24](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.24.md) · single point of failure
- [ ] [A08.25](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.25.md) · multi-region active-passive vs active-active
- [ ] [A08.26](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.26.md) · distributed tracing and sampling
- [ ] [A08.27](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.27.md) · data migration safety
- [ ] [A08.28](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.28.md) · canary, blue-green and shadow traffic
- [ ] [A08.29](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.29.md) · cost/reliability trade-offs
- [ ] [A08.30](01-architecture-A01-to-A20/A08-reliability-operations-and-sre/lessons/A08.30.md) · abuse detection

## A09 evidence

- [ ] Reproduce all four labs for Cloud, Containers, Kubernetes & Platform Engineering
- [ ] Pass both project suites
- [ ] Pass fresh assessment and delayed re-test

- [ ] [A09.01](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.01.md) · Linux processes/namespaces/cgroups
- [ ] [A09.02](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.02.md) · filesystems
- [ ] [A09.03](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.03.md) · image vs container
- [ ] [A09.04](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.04.md) · Dockerfile layers and cache
- [ ] [A09.05](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.05.md) · image registries
- [ ] [A09.06](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.06.md) · virtual networks
- [ ] [A09.07](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.07.md) · IAM principles
- [ ] [A09.08](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.08.md) · DNS and TLS
- [ ] [A09.09](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.09.md) · Docker multi-stage/non-root
- [ ] [A09.10](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.10.md) · Compose and persistent volumes
- [ ] [A09.11](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.11.md) · CI/CD
- [ ] [A09.12](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.12.md) · GitOps
- [ ] [A09.13](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.13.md) · IaC/Terraform
- [ ] [A09.14](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.14.md) · VPC, subnets, routes, NAT and endpoints
- [ ] [A09.15](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.15.md) · IAM, KMS, secrets
- [ ] [A09.16](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.16.md) · EKS/AKS
- [ ] [A09.17](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.17.md) · pod, deployment, service and ingress/gateway
- [ ] [A09.18](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.18.md) · scheduling, requests/limits and probes
- [ ] [A09.19](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.19.md) · HPA
- [ ] [A09.20](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.20.md) · workloads and PVC
- [ ] [A09.21](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.21.md) · network policies
- [ ] [A09.22](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.22.md) · CKAD workflows and debugging
- [ ] [A09.23](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.23.md) · CNI/CoreDNS/kube-proxy
- [ ] [A09.24](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.24.md) · resource quotas
- [ ] [A09.25](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.25.md) · pod disruption budgets
- [ ] [A09.26](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.26.md) · rolling/canary deploy
- [ ] [A09.27](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.27.md) · workload identity
- [ ] [A09.28](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.28.md) · software supply chain SBOM/scanning
- [ ] [A09.29](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.29.md) · admission controls
- [ ] [A09.30](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.30.md) · GPU scheduling and topology
- [ ] [A09.31](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.31.md) · node autoscalers
- [ ] [A09.32](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.32.md) · AWS Bedrock/SageMaker integration
- [ ] [A09.33](01-architecture-A01-to-A20/A09-cloud-containers-k8s-devsecops/lessons/A09.33.md) · FinOps and multi-AZ resilience

## A10 evidence

- [ ] Reproduce all four labs for ML Foundations, AI Math & MLOps
- [ ] Pass both project suites
- [ ] Pass fresh assessment and delayed re-test

- [ ] [A10.01](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.01.md) · sets, logic and functions
- [ ] [A10.02](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.02.md) · vectors/matrices
- [ ] [A10.03](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.03.md) · derivatives and gradients
- [ ] [A10.04](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.04.md) · probability distributions
- [ ] [A10.05](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.05.md) · conditional probability and Bayes
- [ ] [A10.06](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.06.md) · expectation/variance
- [ ] [A10.07](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.07.md) · train/validation/test separation
- [ ] [A10.08](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.08.md) · linear regression and losses
- [ ] [A10.09](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.09.md) · dataset quality and leakage
- [ ] [A10.10](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.10.md) · sampling and stratification
- [ ] [A10.11](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.11.md) · classification/regression metrics
- [ ] [A10.12](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.12.md) · bias/variance
- [ ] [A10.13](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.13.md) · gradient descent
- [ ] [A10.14](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.14.md) · optimizer/learning rates
- [ ] [A10.15](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.15.md) · feature engineering
- [ ] [A10.16](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.16.md) · experiment tracking
- [ ] [A10.17](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.17.md) · datasets/versioning DVC
- [ ] [A10.18](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.18.md) · model registry
- [ ] [A10.19](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.19.md) · model serving
- [ ] [A10.20](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.20.md) · drift
- [ ] [A10.21](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.21.md) · calibration
- [ ] [A10.22](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.22.md) · monitoring
- [ ] [A10.23](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.23.md) · MLflow and pipelines
- [ ] [A10.24](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.24.md) · CNN/NLP and representation learning
- [ ] [A10.25](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.25.md) · transformers fundamentals
- [ ] [A10.26](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.26.md) · transfer learning
- [ ] [A10.27](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.27.md) · PCA and SVD
- [ ] [A10.28](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.28.md) · inference statistics
- [ ] [A10.29](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.29.md) · uncertainty and significance
- [ ] [A10.30](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.30.md) · causal vs correlational pitfalls
- [ ] [A10.31](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.31.md) · responsible ML
- [ ] [A10.32](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.32.md) · offline/online evaluation
- [ ] [A10.33](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.33.md) · retraining triggers
- [ ] [A10.34](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.34.md) · shadow deployments
- [ ] [A10.35](01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops/lessons/A10.35.md) · hardware and cost budgets

## A11 evidence

- [ ] Reproduce all four labs for Transformers, LLM Internals & Inference
- [ ] Pass both project suites
- [ ] Pass fresh assessment and delayed re-test

- [ ] [A11.01](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.01.md) · tensor shapes
- [ ] [A11.02](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.02.md) · dot product and matrix multiplication
- [ ] [A11.03](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.03.md) · softmax, cross entropy and gradients
- [ ] [A11.04](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.04.md) · tokens and tokenization
- [ ] [A11.05](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.05.md) · embeddings
- [ ] [A11.06](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.06.md) · attention Q/K/V
- [ ] [A11.07](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.07.md) · positional encoding
- [ ] [A11.08](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.08.md) · residual connections
- [ ] [A11.09](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.09.md) · normalization
- [ ] [A11.10](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.10.md) · transformer forward pass
- [ ] [A11.11](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.11.md) · autoregressive decoding
- [ ] [A11.12](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.12.md) · logits and sampling
- [ ] [A11.13](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.13.md) · prefill vs decode
- [ ] [A11.14](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.14.md) · KV cache and memory math
- [ ] [A11.15](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.15.md) · GPU memory hierarchy
- [ ] [A11.16](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.16.md) · TTFT/TPOT/ITL/E2E
- [ ] [A11.17](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.17.md) · throughput vs goodput
- [ ] [A11.18](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.18.md) · benchmarking
- [ ] [A11.19](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.19.md) · vLLM/SGLang engines
- [ ] [A11.20](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.20.md) · continuous batching
- [ ] [A11.21](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.21.md) · schedulers, fairness and cancellation
- [ ] [A11.22](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.22.md) · PagedAttention
- [ ] [A11.23](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.23.md) · prefix caching
- [ ] [A11.24](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.24.md) · mixed-length workloads
- [ ] [A11.25](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.25.md) · BF16/FP8/INT8/4-bit formats
- [ ] [A11.26](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.26.md) · AWQ/GPTQ/SmoothQuant
- [ ] [A11.27](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.27.md) · KV quantization
- [ ] [A11.28](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.28.md) · profiling and roofline
- [ ] [A11.29](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.29.md) · FlashAttention
- [ ] [A11.30](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.30.md) · Triton and kernel fusion
- [ ] [A11.31](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.31.md) · torch.compile and CUDA graphs
- [ ] [A11.32](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.32.md) · speculative decoding
- [ ] [A11.33](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.33.md) · MoE routing and parallelism
- [ ] [A11.34](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.34.md) · TP/PP/DP/CP
- [ ] [A11.35](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.35.md) · NCCL/NVLink
- [ ] [A11.36](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.36.md) · disaggregated prefill-decode
- [ ] [A11.37](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.37.md) · offload and long-context tiers
- [ ] [A11.38](01-architecture-A01-to-A20/A11-transformers-llm-internals/lessons/A11.38.md) · model routing and serving economics

## A12 evidence

- [ ] Reproduce all four labs for Search, RAG & Knowledge Systems
- [ ] Pass both project suites
- [ ] Pass fresh assessment and delayed re-test

- [ ] [A12.01](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.01.md) · documents and tokenization
- [ ] [A12.02](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.02.md) · normalization
- [ ] [A12.03](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.03.md) · inverted indexes
- [ ] [A12.04](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.04.md) · posting lists
- [ ] [A12.05](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.05.md) · Boolean search
- [ ] [A12.06](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.06.md) · TF-IDF and BM25
- [ ] [A12.07](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.07.md) · stopwords
- [ ] [A12.08](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.08.md) · precision/recall
- [ ] [A12.09](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.09.md) · embeddings and vector similarity
- [ ] [A12.10](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.10.md) · document parsing and lineage
- [ ] [A12.11](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.11.md) · chunking
- [ ] [A12.12](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.12.md) · chunk overlap
- [ ] [A12.13](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.13.md) · metadata and ACLs
- [ ] [A12.14](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.14.md) · hybrid sparse+dense search
- [ ] [A12.15](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.15.md) · approximate nearest neighbors
- [ ] [A12.16](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.16.md) · HNSW and index updates
- [ ] [A12.17](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.17.md) · query rewriting
- [ ] [A12.18](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.18.md) · reranking and cross encoders
- [ ] [A12.19](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.19.md) · evidence citations
- [ ] [A12.20](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.20.md) · retrieval metrics recall@k/MRR/nDCG
- [ ] [A12.21](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.21.md) · grounding and answer quality
- [ ] [A12.22](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.22.md) · search index synchronization and deletes
- [ ] [A12.23](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.23.md) · deduplication
- [ ] [A12.24](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.24.md) · sharded indexes
- [ ] [A12.25](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.25.md) · crawler pipelines
- [ ] [A12.26](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.26.md) · multi-hop retrieval
- [ ] [A12.27](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.27.md) · structured+graph retrieval
- [ ] [A12.28](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.28.md) · freshness
- [ ] [A12.29](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.29.md) · reranking budgets
- [ ] [A12.30](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.30.md) · tenant authorization at query time
- [ ] [A12.31](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.31.md) · prompt injection via retrieved data
- [ ] [A12.32](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.32.md) · large-scale ingestion reliability
- [ ] [A12.33](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.33.md) · eval drift and human review
- [ ] [A12.34](01-architecture-A01-to-A20/A12-search-rag-and-knowledge-systems/lessons/A12.34.md) · autocomplete and spell correction

## A13 evidence

- [ ] Reproduce all four labs for Agentic AI, MCP & Workflow Orchestration
- [ ] Pass both project suites
- [ ] Pass fresh assessment and delayed re-test

- [ ] [A13.01](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.01.md) · deterministic workflows
- [ ] [A13.02](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.02.md) · state machines
- [ ] [A13.03](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.03.md) · function calling
- [ ] [A13.04](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.04.md) · structured outputs
- [ ] [A13.05](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.05.md) · tool definitions
- [ ] [A13.06](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.06.md) · tasks vs agents
- [ ] [A13.07](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.07.md) · context window and state
- [ ] [A13.08](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.08.md) · retries and side effects
- [ ] [A13.09](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.09.md) · LangGraph state/nodes/edges
- [ ] [A13.10](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.10.md) · tool execution loop
- [ ] [A13.11](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.11.md) · checkpoints
- [ ] [A13.12](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.12.md) · resume/replay
- [ ] [A13.13](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.13.md) · human interrupts
- [ ] [A13.14](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.14.md) · planning vs execution
- [ ] [A13.15](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.15.md) · parallel fanout/fanin
- [ ] [A13.16](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.16.md) · agent memory vs chat history
- [ ] [A13.17](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.17.md) · MCP host/client/server/tool/resource/prompt
- [ ] [A13.18](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.18.md) · schema contracts
- [ ] [A13.19](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.19.md) · authorization and secrets
- [ ] [A13.20](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.20.md) · idempotent external actions
- [ ] [A13.21](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.21.md) · multi-agent coordination vs single agent
- [ ] [A13.22](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.22.md) · bounded autonomy
- [ ] [A13.23](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.23.md) · escalation/approval
- [ ] [A13.24](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.24.md) · robust delegation
- [ ] [A13.25](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.25.md) · long-running durable agents
- [ ] [A13.26](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.26.md) · trace-level observability
- [ ] [A13.27](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.27.md) · adversarial tool outputs
- [ ] [A13.28](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.28.md) · prompt injection and privilege boundaries
- [ ] [A13.29](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.29.md) · per-agent budgets
- [ ] [A13.30](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.30.md) · policy enforcement
- [ ] [A13.31](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.31.md) · evaluation of task success and side effects
- [ ] [A13.32](01-architecture-A01-to-A20/A13-agentic-ai-mcp-orchestration/lessons/A13.32.md) · supervision and rollback
