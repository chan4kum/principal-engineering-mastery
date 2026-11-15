# A07 · Applied assessment

Attempt all ten and pass at least eight. Reproduce the labs and both projects, diagnose one new failure and repeat the assessment with fresh inputs after a delay.

1. Why should pricing logic be testable without a web process?
2. A gateway authenticates a user. Which component authorizes access to an individual order?
3. At a stable 30 queued completions/s and 2 s average residence, estimate queue-stage population.
4. After charging a customer, order confirmation fails. What distinguishes a compensating refund from a transaction rollback?
5. A publisher sends an event and crashes before updating its outbox row. What happens after restart?
6. When is committing a Kafka consumer offset before the effect unsafe?
7. A DAG has a 15 ms step followed by parallel 40 ms and 60 ms branches. Estimate the dependency-imposed lower bound.
8. What should a worker do with a malformed message after its attempt cap is reached?
9. A new event reader adds a field. What determines whether it can consume older events?
10. How do you scope operation identities for customers reusing the same external order ID?

<details>
<summary>Answers</summary>

1. Pricing owns business rules, independent of protocol translation.
2. The owner of the order verifies the subject's action on that resource.
3. Roughly 60 in the measured stage under Little's Law assumptions.
4. Refund is a new operation with an independent outcome and retry policy.
5. It may publish again under the same event identity. The consumer must deduplicate effects.
6. If the consumer can fail between offset commit and the durable effect, the next owner can skip unfinished work.
7. 75 ms before join overhead.
8. Quarantine it with failure evidence for controlled review and replay.
9. Encoding, compatibility mode, field defaults and semantic behavior.
10. Combine verified tenant, operation kind and external ID in the appropriate scope.

</details>

## Source scenario

Checkout commits a database row, but Kafka publication fails. Draw producer, database, relay, broker and consumer. Mark the committed outbox, the relay retry, delivered event identity, consumer effect and acknowledgment. Show recovery from both ambiguous outcomes.

**Principal interview.** A new AI product deploys one team across three unstable business boundaries. Explain when a modular monolith gives a shorter feedback loop and what observable change would justify extracting a service.
