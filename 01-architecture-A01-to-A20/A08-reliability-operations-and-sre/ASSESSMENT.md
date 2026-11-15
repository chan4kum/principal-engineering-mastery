# A08 · Applied assessment

Pass at least eight of ten, reproduce all labs and both projects, then retest with changed inputs.

1. Can an API have high uptime and low durable-write reliability?
2. At 99.9% over one million eligible requests, how many bad requests fit?
3. An observed 1% error fraction against that objective burns at what rate?
4. An API returns 200 with invalid data. Should it count as good for a correctness SLI?
5. Which signal measures the denominator, and which signals help explain an individual failure?
6. Three layers each allow three attempts. What is the worst-case nested attempt count?
7. If a dependency is unavailable, why can restarting every web worker worsen the incident?
8. An outage starts at 12:45, the last recoverable record is 12:40 and service returns at 12:59. Calculate observed loss window and recovery duration.
9. At 1% head sampling, how many of ten rare errors are captured in expectation?
10. Name a measurable canary rollback trigger with an explicit request cohort and window.

<details>
<summary>Answers</summary>

1. Yes. Availability and durability measure distinct outcomes under specified faults.
2. 1000.
3. 10×.
4. No, if correct data is an eligibility requirement of a good response.
5. Complete request counters measure eligible population. Correlated logs and spans explain examples and dependencies.
6. 27.
7. It removes healthy frontend capacity, shifts load and can synchronize reconnection or retry work.
8. Five minutes of data exposure and 14 minutes to verified recovery under those boundaries.
9. 0.1.
10. For example, abort after five minutes of statistically adequate canary volume if the good request fraction is below its fixed gate and lower than the healthy control. Define the sample and decision threshold before releasing.

</details>

## Source scenario

A dependency takes ten seconds and causes retries and an overload cascade. Draw the timeline for one request and one retry, then propose a reversible admission or retry mitigation. Measure success and queue depth through recovery.

**Principal interview.** Explain how a product can have 99.9% uptime and still violate latency, correctness, or a narrower user-journey SLO.
