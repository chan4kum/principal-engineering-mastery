# A01 · Applied assessment

Attempt these without lesson pages or AI help. Have a reviewer substitute fresh numbers and vary one failure condition for your delayed re-test. Pass eight of ten and complete the phase evidence separately.

1. A file is 8 MiB and moves at 16 Mb/s. Estimate ideal transfer time to two decimals.
2. Which integer does big-endian signed `ff fe` encode?
3. A model uses 4096-byte pages, and virtual page 4 maps to physical frame 9. Translate virtual address 16395.
4. Four workers each have 7 MiB private and share one 24 MiB region. Calculate summed RSS and summed PSS.
5. A parent called terminate and its Python process handle reports −15. Which fact does the status establish?
6. Both threads read counter 9 and independently add 1 before writing. What will their two stores leave behind?
7. What boundary determines whether a private mmap write modifies the original file?
8. One runnable thread needs 65 ms CPU, starting at a fresh cgroup period with quota 30 ms every 100 ms. When does it finish in the ideal model?
9. A workload shows exit 137 and the host has free RAM. Which evidence can establish a workload OOM?
10. An API has low CPU and high wall time. Its event loop heartbeat is smooth but storage calls take 150 ms. Name the leading hypothesis and a test that could falsify it.

<details>
<summary>Answers and reasoning</summary>

1. 4.19 s, from 8×8×1048576 / 16000000.
2. −2, from unsigned 65534 minus 65536.
3. 36875. Offset stays 11 and physical base is 9×4096.
4. 124 MiB RSS and 52 MiB PSS. RSS counts 24 four times, PSS distributes that same region.
5. The child exited due to SIGTERM on POSIX, as observed by the parent. It was not a normal exit status 15.
6. 10. Both store the same computed value.
7. Private copy-on-write changes the mapping only. A shared writable file mapping can change backing data.
8. 205 ms. Two full quota windows execute at 0–30 and 100–130. Five milliseconds remain at 200.
9. Correlate the runtime OOM flag or a scoped memory.events oom_kill increment with the task and timestamp.
10. Time spent awaiting storage is the first hypothesis. Replace storage with a bounded local fast fixture under equivalent load. If latency remains, this mechanism is insufficient.

</details>

For the unfamiliar failure checkpoint, collect a fresh request timeline, CPU-versus-wall sample, process status and cgroup evidence as appropriate. Make one controlled change and predict the expected observation before running it.
