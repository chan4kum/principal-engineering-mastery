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
