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
