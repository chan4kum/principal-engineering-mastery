# A01 · Computer Systems & Operating Systems

**36 lessons · 4 labs · 2 projects**

How do instructions execute, and why do finite resources constrain software? Build up from bit patterns to process, CPU and memory evidence. Lesson IDs and titles follow the detailed roadmap and V3 audited architecture index.

| ID | Lesson | Tier |
| --- | --- | --- |
| [A01.01](lessons/A01.01.md) | binary and units | Foundation |
| [A01.02](lessons/A01.02.md) | bits/bytes/words | Foundation |
| [A01.03](lessons/A01.03.md) | signed integer encoding | Foundation |
| [A01.04](lessons/A01.04.md) | CPU instruction sets | Foundation |
| [A01.05](lessons/A01.05.md) | machine code vs source vs bytecode | Foundation |
| [A01.06](lessons/A01.06.md) | what a program is | Foundation |
| [A01.07](lessons/A01.07.md) | files and persistent storage | Foundation |
| [A01.08](lessons/A01.08.md) | RAM vs cache vs registers | Foundation |
| [A01.09](lessons/A01.09.md) | fetch-decode-execute | Foundation |
| [A01.10](lessons/A01.10.md) | CPU register and program counter | Foundation |
| [A01.11](lessons/A01.11.md) | kernel vs user mode | Core |
| [A01.12](lessons/A01.12.md) | boot and system calls | Core |
| [A01.13](lessons/A01.13.md) | process creation and lifetime | Core |
| [A01.14](lessons/A01.14.md) | PID/PPID and parent-child tree | Core |
| [A01.15](lessons/A01.15.md) | process address space | Core |
| [A01.16](lessons/A01.16.md) | stack frames and call stacks | Core |
| [A01.17](lessons/A01.17.md) | heap allocation | Core |
| [A01.18](lessons/A01.18.md) | virtual memory and page tables | Core |
| [A01.19](lessons/A01.19.md) | page faults, swap and TLB | Core |
| [A01.20](lessons/A01.20.md) | threads and shared address space | Core |
| [A01.21](lessons/A01.21.md) | context switching | Core |
| [A01.22](lessons/A01.22.md) | scheduler and CPU timeslices | Core |
| [A01.23](lessons/A01.23.md) | interrupts and traps | Core |
| [A01.24](lessons/A01.24.md) | file descriptors and sockets | Core |
| [A01.25](lessons/A01.25.md) | race conditions and synchronization | Principal |
| [A01.26](lessons/A01.26.md) | mutexes/semaphores/atomics | Principal |
| [A01.27](lessons/A01.27.md) | deadlock/livelock/starvation | Principal |
| [A01.28](lessons/A01.28.md) | CPU affinity and NUMA | Principal |
| [A01.29](lessons/A01.29.md) | cache hierarchy and false sharing | Principal |
| [A01.30](lessons/A01.30.md) | I/O blocking and async | Principal |
| [A01.31](lessons/A01.31.md) | mmap and copy-on-write | Principal |
| [A01.32](lessons/A01.32.md) | memory accounting RSS/PSS | Principal |
| [A01.33](lessons/A01.33.md) | cgroups and namespaces | Principal |
| [A01.34](lessons/A01.34.md) | container limits vs host resources | Principal |
| [A01.35](lessons/A01.35.md) | CPU throttling and OOMKilled | Principal |
| [A01.36](lessons/A01.36.md) | ARM vs x86 and cross-architecture deployment | Principal |

## Practice and exit gate

- [L1 · Process anatomy](labs/L1.md)
- [L2 · CPU versus I/O](labs/L2.md)
- [L3 · Memory pressure](labs/L3.md)
- [L4 · Thread safety](labs/L4.md)
- [Guided project · Linux resource explorer](projects/guided/README.md)
- [Independent project · Concurrent task runner](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs, pass both project suites, diagnose one unfamiliar failure, and score at least 80% on a fresh applied assessment. On a later day, retest with changed inputs and explain a syscall trace plus a resource failure. Record evidence in the [progress tracker](../../PROGRESS_TRACKER.md).

Each lesson includes primary references and notes separating architectural rules, Linux behavior and simplified local models. The source references were reviewed in November 2026.

Continue to [A02 · Networking & Communication](../A02-networking-and-communication/README.md) after the exit gate.
