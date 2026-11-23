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

## Guided walkthrough

Follow a worker from the bytes it reads to the resources that constrain it in production. The examples below use simplified inputs. Use the linked lessons and labs to observe the corresponding behavior locally.

### Data and instruction execution (A01.01–A01.10)

1. **Binary and units.** A set bit contributes its place value. `10110₂ = 16 + 4 + 2 = 22`. Binary size prefixes use powers of two, while decimal rates use powers of ten. For a 1 GiB payload on a 100 Mb/s link, convert both inputs before dividing. `1,073,741,824 bytes ÷ 12,500,000 bytes/s ≈ 85.90 s`.
2. **Bits, bytes, and words.** A byte has eight bits on the systems used here. The meaning of *word* depends on the architecture or format. The same bytes `12 34` decode as `0x1234` in big-endian order or `0x3412` in little-endian order. Specify the width and byte order at a binary boundary.
3. **Signed integers.** In eight-bit two’s complement the top bit has weight `−128`. The range is `−128` to `127`, and `0x80` represents `−128`. Range-check before serialization, because masking `128` into eight bits creates exactly that pattern.
4. **Instruction sets.** An instruction set architecture defines encodings, registers, and visible instruction effects. An ABI adds conventions such as how to pass arguments and return values. Two CPUs can implement the same ISA with different pipelines and still run the same compatible binary.
5. **Source, bytecode, and machine code.** CPython compiles source into code objects containing bytecode. Its interpreter runs native machine instructions to carry out those bytecode operations. Inspect bytecode with the same interpreter version used to run the program.
6. **Program and process.** A program supplies executable code. Launching it creates a live execution with arguments, environment, open handles, and an exit status. Two invocations of the same program can produce different results and have independent lifetimes.
7. **Files and persistence.** A write can pass through application buffers and the kernel page cache before reaching persistent storage. A second reader may see the update while it is still vulnerable to a crash. A durable replacement requires the sync and rename sequence appropriate to the filesystem.
8. **Registers, cache, and RAM.** Registers hold operands close to the CPU’s execution units. Caches keep copies of data in lines, and RAM holds a larger working set. With 64-byte lines, offsets `0` and `32` from an aligned base share a line, while offset `64` starts another.
9. **Fetch, decode, and execute.** Fetch reads the instruction at the program counter. Decode identifies its operation and operands, and execution updates architectural state. A taken branch supplies the next instruction address. Applying the fall-through increment afterward can skip the target.
10. **Registers and the program counter.** A register can hold an operand, result, address, or other architectural state. For a fixed-width four-byte instruction at byte address `8`, fall-through is `12`. A taken branch to `20` instead selects `20` as the next address.

### Privilege, processes, and memory (A01.11–A01.19)

11. **User and kernel mode.** A system call enters a controlled kernel path. For `read`, the kernel resolves the descriptor and validates the request before returning bytes or an error. A user program cannot directly manipulate the kernel objects behind its descriptors.
12. **Boot and system calls.** Firmware starts a loader, the loader starts the kernel, and the kernel starts user space. An application later opens its configuration through a system call. `ENOENT` at that point identifies a failed file lookup for the application.
13. **Process lifetime.** A child may still be running when its parent checks it. After exit, the parent collects its status by waiting. On POSIX systems an exited child can remain a zombie until it is reaped, so cleanup must also wait after termination.
14. **PID and PPID.** PID identifies a process in the observer’s PID namespace. PPID identifies its current parent in that view. A child can be reparented when its parent exits, and PID values can be reused. Treat a process tree as a snapshot.
15. **Address spaces.** Each process sees virtual mappings for code, data, stacks, heap, and mapped files. Two processes can use the same virtual address for different bytes. Across a process boundary, send a value or an offset into an agreed shared mapping.
16. **Stack frames.** A call adds an active frame that holds the state needed to execute and return. `f(2) → f(1) → f(0)` reaches three active frames. Recursion depth follows the longest pending chain of calls, so unbounded input depth can hit a runtime stack limit.
17. **Heap allocation.** A list can keep an object alive after its local variable is deleted. Even after the object becomes unreachable and is freed, the allocator may keep the region for reuse. Compare live allocation evidence with resident memory when investigating growth.
18. **Virtual memory and page tables.** With 4,096-byte pages, virtual address `8,199` is page `2` at offset `7`. If page `2` maps to frame `11`, the physical address is `11 × 4,096 + 7 = 45,063`. The mapping also controls permissions.
19. **TLBs, faults, and swap.** A TLB caches address translations. A miss can be resolved by walking the page table. A page fault enters the kernel, which may supply a zero-filled page, recover data from backing storage, or reject the access. Disk I/O depends on what resolves the fault.

### Scheduling, I/O, and concurrency (A01.20–A01.30)

20. **Threads.** Threads share process memory and descriptors. Each has its own stack and scheduling state. If a worker appends a result, joining the worker before reading establishes the required order.
21. **Context switching.** When one task blocks for I/O, the CPU can save that task’s execution state and run another. The first task becomes eligible again when its wait completes. Compare elapsed time with CPU time to see how much time the task actually spent executing.
22. **Scheduling and timeslices.** In a round-robin model with a 2 ms quantum, jobs of 5 ms and 3 ms run as `A2 B2 A2 B1 A1`. B completes at 7 ms and A at 8 ms. Shorter quanta can improve responsiveness at the cost of more switching.
23. **Interrupts and traps.** A device interrupt can arrive independently of the running instruction. An invalid instruction causes a synchronous exception. The kernel handles these events, and some exceptions can lead to a signal for the application.
24. **Descriptors and sockets.** A file descriptor is a process-local handle to an open kernel resource. On a stream socket, an orderly peer shutdown is observed as EOF after buffered data is drained. Retrying an empty read indefinitely can spin.
25. **Races.** Two threads can each read `0`, compute `1`, and overwrite the same counter with `1`. The invariant is one increment per completed operation, so synchronize the whole read-modify-write sequence.
26. **Mutexes, semaphores, and atomics.** A mutex protects an exclusive critical section. A semaphore with three permits admits up to three holders. An atomic operation supplies guarantees for a specific operation and memory ordering. An invariant across several values may need a larger critical section.
27. **Deadlock, livelock, and starvation.** Deadlock can occur when A holds lock 1 and waits for lock 2 while B holds lock 2 and waits for lock 1. A common acquisition order breaks that cycle. Livelock means tasks keep reacting without completing, and starvation means a particular task is repeatedly denied progress.
28. **CPU affinity and NUMA.** Affinity constrains where a task may run. On NUMA hardware, the cost of reading memory can depend on the CPU’s location relative to the page. Pinning can improve locality or overload a subset of CPUs. Measure the effect under representative load.
29. **Cache hierarchy and false sharing.** Two cores can write to different counters yet repeatedly transfer ownership of a shared cache line. With a 64-byte line and an aligned base, counters at offsets `0` and `8` share a line. Changing the layout can reduce those transfers.
30. **Blocking I/O and async.** When a coroutine suspends, the event loop can run another task. Two 30 ms waits started together can overlap. A blocking 30 ms call on the loop thread stops other loop tasks from running during that call.

### Mappings, containers, and deployment (A01.31–A01.36)

31. **Memory mapping and copy-on-write.** A file mapping lets a process access file offsets through virtual addresses. In the private mapping example, writing `Z` to a mapping of `ABC` yields `ZBC` in the process while the file remains `ABC`. A shared mapping has different visibility and persistence semantics.
32. **RSS and PSS.** RSS counts a shared resident page in full for each process that maps it. PSS divides its cost among those processes. With 10 MiB private per worker and 40 MiB shared by two workers, each has 50 MiB RSS and 30 MiB PSS.
33. **Namespaces and cgroups.** Namespaces alter what resources a process can see. Cgroups track and constrain resource use. A process can see itself as PID 1 inside a container while the host kernel still schedules it under the container’s CPU budget.
34. **Container limits and host resources.** A container capped at 256 MiB with 96 MiB already charged has a simple headroom estimate of 160 MiB, even on an 8 GiB host. Check ancestor limits and account for other charged memory before setting worker concurrency.
35. **CPU throttling and OOM kills.** A group using a 20 ms CPU quota in a 100 ms period can be throttled after spending its budget. Inspect `cpu.stat` for throttling. For a memory kill, corroborate an exit status of 137 with a cgroup OOM event or runtime metadata, since any `SIGKILL` can produce that status.
36. **ARM and x86 deployment.** Executable compatibility depends on the ISA, OS, and ABI. A multi-platform image index can reference separate `linux/arm64` and `linux/amd64` manifests. Validate the platform selection and smoke-test each published variant.

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
