# A02 · Applied assessment

Work without AI or the lesson pages. Record the last verified boundary and what would falsify your diagnosis. Pass at least eight of ten, reproduce the labs, and pass both projects.

1. A tunnel adds 68 B to an outer 1500 B IP MTU. What is the payload bound with a 40 B IPv6 and 20 B TCP header, ignoring options?
2. Which next hop wins for 10.20.1.5 among 0.0.0.0/0 → A, 10.20.0.0/16 → B, and 10.20.1.0/24 → C?
3. A receiver expects 501 and then receives byte ranges 511–520 and 501–510 in that order. What two cumulative ACKs follow?
4. At 250 Mb/s and 80 ms RTT, what is the byte BDP?
5. A chain is trusted, but the leaf covers only service.test and the client requests other.test. Which check fails?
6. A client has 260 ms left, must back off 75 ms and needs at least 200 ms per attempt. Should the retry start?
7. A shared HTTP/2 TCP connection loses bytes for stream A before received bytes for stream B. Can transport deliver B's later bytes before the hole is filled?
8. A request succeeds every time with fresh connections after a DNS update, but some reused connections still reach the old host. Which observation would confirm stale pool entries?
9. An endpoint returns 200 headers and one streaming chunk, then the upstream stalls beyond the read inactivity timer. What might the downstream observe in L4?
10. A proxy span is [0, 160] ms. Child intervals are [20, 70] and [40, 100] ms. How much parent time lies outside their union?

<details>
<summary>Answers and reasoning</summary>

1. 1372 B. Subtract 68, 40 and 20 from 1500.
2. C. It has the longest matching prefix.
3. 501, then 521. The first segment leaves the hole, and the second fills it.
4. 2,500,000 B. Multiply 250,000,000 bits/s by 0.08 s and divide by eight.
5. Name verification. A trusted signing chain does not authorize a different name.
6. No. 185 ms remains after backoff.
7. No. TCP presents a contiguous ordered byte stream to HTTP/2.
8. Log the chosen IP of a fresh resolution and the remote peer and age on a reused lease.
9. The client may see an interrupted body after the first chunk, with the already-forwarded 200.
10. 80 ms. The children overlap and occupy [20, 100] ms together.

</details>

For the unfamiliar case, have a reviewer combine one readable response failure and one pre-HTTP fault in the local fixture. Diagnose the earlier boundary first, change one setting, and rerun before diagnosing the second. On a later day, repeat with changed MTU, DNS or timing inputs.

## Scenario from the audited curriculum

An LLM token stream disconnects at about 60 seconds through an ingress. Draw the path from DNS and TCP through TLS, the ingress and the backend, then back to the client. Ask one checkpoint at a time.

1. Did DNS, TCP and TLS succeed on the affected connection?
2. Did the ingress forward headers and the first token? Which clocks measure that?
3. Is 60 seconds measured from request start or from the last upstream byte? Compare a frequent-token stream and a silent upstream.
4. Do upstream writes occur earlier than downstream arrivals, suggesting buffering?
5. After the disconnect, does the backend observe cancellation and stop producing?

<details>
<summary>Diagnosis and principal interview</summary>

A successful handshake and observed first chunk move investigation to the streaming path. A gap measured from the last upstream byte is consistent with an upstream read inactivity limit. A fixed cutoff during steady bytes suggests an overall deadline or a different hop's timer. If upstream writes precede downstream batches, inspect buffering and client behavior. Confirm cancellation at the application because client closure alone does not establish that generation stopped.

**Why can adding HTTP retries increase both load and outages?** A failure under saturation can cause extra attempts before the original work has stopped. Independent retry layers multiply that traffic and synchronized backoff can align bursts. Bound attempts and elapsed time, coordinate retry ownership, and retry only where semantics and capacity permit. Check whether a retried stream can resume without duplicate effects.

</details>
