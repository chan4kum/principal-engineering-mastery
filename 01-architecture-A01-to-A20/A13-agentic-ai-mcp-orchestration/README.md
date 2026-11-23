# A13 · Agentic AI, MCP & Workflow Orchestration

**32 lessons · 4 labs · 2 projects**

Trace state and tool proposals while enforcing permissions, approvals and idempotent effects outside the model. All tools are local fixtures and the write records a simulated notice.

Prerequisite [A12 exit gate](../A12-search-rag-and-knowledge-systems/README.md#practice-and-exit-gate).

| ID | Lesson | Tier |
| --- | --- | --- |
| [A13.01](lessons/A13.01.md) | deterministic workflows | Foundation |
| [A13.02](lessons/A13.02.md) | state machines | Foundation |
| [A13.03](lessons/A13.03.md) | function calling | Foundation |
| [A13.04](lessons/A13.04.md) | structured outputs | Foundation |
| [A13.05](lessons/A13.05.md) | tool definitions | Foundation |
| [A13.06](lessons/A13.06.md) | tasks vs agents | Foundation |
| [A13.07](lessons/A13.07.md) | context window and state | Foundation |
| [A13.08](lessons/A13.08.md) | retries and side effects | Foundation |
| [A13.09](lessons/A13.09.md) | LangGraph state/nodes/edges | Core |
| [A13.10](lessons/A13.10.md) | tool execution loop | Core |
| [A13.11](lessons/A13.11.md) | checkpoints | Core |
| [A13.12](lessons/A13.12.md) | resume/replay | Core |
| [A13.13](lessons/A13.13.md) | human interrupts | Core |
| [A13.14](lessons/A13.14.md) | planning vs execution | Core |
| [A13.15](lessons/A13.15.md) | parallel fanout/fanin | Core |
| [A13.16](lessons/A13.16.md) | agent memory vs chat history | Core |
| [A13.17](lessons/A13.17.md) | MCP host/client/server/tool/resource/prompt | Core |
| [A13.18](lessons/A13.18.md) | schema contracts | Core |
| [A13.19](lessons/A13.19.md) | authorization and secrets | Core |
| [A13.20](lessons/A13.20.md) | idempotent external actions | Core |
| [A13.21](lessons/A13.21.md) | multi-agent coordination vs single agent | Principal |
| [A13.22](lessons/A13.22.md) | bounded autonomy | Principal |
| [A13.23](lessons/A13.23.md) | escalation/approval | Principal |
| [A13.24](lessons/A13.24.md) | robust delegation | Principal |
| [A13.25](lessons/A13.25.md) | long-running durable agents | Principal |
| [A13.26](lessons/A13.26.md) | trace-level observability | Principal |
| [A13.27](lessons/A13.27.md) | adversarial tool outputs | Principal |
| [A13.28](lessons/A13.28.md) | prompt injection and privilege boundaries | Principal |
| [A13.29](lessons/A13.29.md) | per-agent budgets | Principal |
| [A13.30](lessons/A13.30.md) | policy enforcement | Principal |
| [A13.31](lessons/A13.31.md) | evaluation of task success and side effects | Principal |
| [A13.32](lessons/A13.32.md) | supervision and rollback | Principal |

## Guided walkthrough

Start with explicit workflow state. Add model-selected actions only where the control flow, permissions, and side effects can be supervised.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Define workflow state and tool contracts (A13.01–A13.08)

1. **[A13.01 · deterministic workflows](lessons/A13.01.md).** A deterministic workflow selects a transition from versioned inputs and state. Nondeterministic calls can be isolated behind recorded results. A three-stage path executes three transitions before any retries. Two alternate branches require covering both paths in tests.
2. **[A13.02 · state machines](lessons/A13.02.md).** A state machine identifies allowed transitions for each state and event. Illegal or repeated events must have defined outcomes. In a linear three-state lifecycle there are two allowed forward edges rather than six possible non-self directed edges.
3. **[A13.03 · function calling](lessons/A13.03.md).** Function calling produces a request with a name and arguments. Application code validates and authorizes it, executes the tool and returns an observation. Three proposed calls with one policy denial result in at most two executions under this policy.
4. **[A13.04 · structured outputs](lessons/A13.04.md).** Structured output constrains syntax and types. Semantic rules, authority and real-world existence are application checks. Four shape-valid proposals with one missing resource leave three eligible in this example.
5. **[A13.05 · tool definitions](lessons/A13.05.md).** A tool definition specifies purpose, schema, return shape, error conditions and effect class. Tool exposure and authorization have separate lifecycles. Two tools with three contract cases each need six focused checks before workflow integration tests.
6. **[A13.06 · tasks vs agents](lessons/A13.06.md).** A task describes an outcome. An agent may select steps dynamically, increasing flexibility and uncertainty. A fixed workflow is easier to bound where outcomes are predictable. At two steps per task versus five potential agent steps, ten tasks cost twenty versus fifty steps in the model.
7. **[A13.07 · context window and state](lessons/A13.07.md).** Context windows limit available model input. Application state records data needed by the workflow independently of transcript summarization or trimming. A 10000-token limit with 1500 reserved for output leaves at most 8500 for the rest before additional overhead.
8. **[A13.08 · retries and side effects](lessons/A13.08.md).** Retry policy must treat ambiguous effects as potentially committed. Idempotency keys and durable receipts allow same-intent replays. Two deliveries of a three-unit write should cause three units of effect with one durable receipt, rather than six.

### Execute, checkpoint, and resume safely (A13.09–A13.20)

9. **[A13.09 · LangGraph state/nodes/edges](lessons/A13.09.md).** LangGraph organizes state, nodes and edges. A node returns state updates and routing determines which node runs next. Concurrent state updates need appropriate reducers. A path through three nodes can have two internal edges before termination.
10. **[A13.10 · tool execution loop](lessons/A13.10.md).** A tool loop chooses or accepts a proposal, validates it, calls an allowed tool, and evaluates stopping conditions. Bound steps, errors and wall time. With a five-step cap and three used, at most two remain.
11. **[A13.11 · checkpoints](lessons/A13.11.md).** Checkpoints save workflow state for a known thread and position. They do not automatically persist external side effects. Use versioned contracts and durable stores for restart. If a snapshot saves after step four of seven, three later steps may need future processing or reconciliation.
12. **[A13.12 · resume/replay](lessons/A13.12.md).** Resume continues from a persisted state. Replay may rerun nodes and thus must reconcile effects and approval versions. Tool receipts and inputs should be stable. With one prior write and one replay attempt, a durable receipt still permits one committed effect.
13. **[A13.13 · human interrupts](lessons/A13.13.md).** Human interrupts pause execution at an explicit boundary. Authorization and approval must precede the effect, cover exact action and input, and survive replay. In a fixture with one pending approval and no affirmative decision, authorized mutation count is zero.
14. **[A13.14 · planning vs execution](lessons/A13.14.md).** Planning generates candidates. Execution occurs behind independently enforced policy. Revalidate plan entries against current state and approved boundaries at execution. If tools include one write and two reads, read-only authority exposes at most two operations.
15. **[A13.15 · parallel fanout/fanin](lessons/A13.15.md).** Fanout starts independent subtasks. Fanin needs explicit merge semantics, concurrency bounds and a policy for partial results. With six independent jobs and two workers, ideal execution takes three waves for equal job lengths.
16. **[A13.16 · agent memory vs chat history](lessons/A13.16.md).** Chat history records interaction. Memory retains selected facts or preferences under a lifecycle. Neither grants authorization to act. Five retained facts with one revoked leaves four eligible facts under a simple deletion policy.
17. **[A13.17 · MCP host/client/server/tool/resource/prompt](lessons/A13.17.md).** In MCP the host manages integration, a client connects to a server, and servers expose negotiated features including tools, resources or prompts. Discovery is separate from authorization. Five advertised tools and two approved for a workflow means only two may execute under its policy.
18. **[A13.18 · schema contracts](lessons/A13.18.md).** Schema contracts specify required fields, types and version assumptions. Validate at ingress and verify compatibility through existing clients. Two writer and two reader versions yield four rollout pairs in a full compatibility matrix.
19. **[A13.19 · authorization and secrets](lessons/A13.19.md).** Authentication establishes identity and authorization scopes actions. Broker secrets through trusted application code and limit payload and response disclosure. With one already scoped, trusted secret provider, zero raw secrets need to be inserted into the model prompt.
20. **[A13.20 · idempotent external actions](lessons/A13.20.md).** Use a stable scoped action identity and external idempotency contract where available. Persist outcome and reconcile uncertain work before retrying. Three identical deliveries of one operation can yield one effect with working downstream deduplication.

### Bound autonomy and supervise effects (A13.21–A13.32)

21. **[A13.21 · multi-agent coordination vs single agent](lessons/A13.21.md).** Multiple agents are useful for independent work with explicit ownership. They add coordination, merge conflicts and latency on shared state. Three agents with all directed pairwise edges can create six communication paths before a supervisor is counted.
22. **[A13.22 · bounded autonomy](lessons/A13.22.md).** Bound autonomy with action scope, step and time budgets, escalation rules, and independently enforced stop conditions. For a limit of eight with six spent, two steps remain.
23. **[A13.23 · escalation/approval](lessons/A13.23.md).** Approval should identify the exact action, subject, parameters, expiry and authorized reviewer. Revalidate after any scope or input change. Two distinct payloads require two matching approvals if both are executed. One approval covers one identified payload.
24. **[A13.24 · robust delegation](lessons/A13.24.md).** Robust delegation names the problem, evidence, expected output, allowable tools and side effects. The parent verifies material results before merging them. An investigation granted two of seven possible resources should be able to access only the scoped two.
25. **[A13.25 · long-running durable agents](lessons/A13.25.md).** Long-running agents need durable state, replay-safe calls, leases or ownership and version migration. External dependencies may expire mid-run. After day one of four, three planned days remain, but completed effects still need outcome reconciliation.
26. **[A13.26 · trace-level observability](lessons/A13.26.md).** Trace-level observability records state transitions, proposals, approvals, execution outcomes and correlation under controlled data policy. Four workflow steps with one event each plus one failure record yield five events in this model.
27. **[A13.27 · adversarial tool outputs](lessons/A13.27.md).** Treat tool results as untrusted data. Validate expected output type and provenance. Only trusted policy changes can grant capabilities. One malicious-looking response should add zero permissions when authority is external.
28. **[A13.28 · prompt injection and privilege boundaries](lessons/A13.28.md).** Prompt injection crosses a data-to-instruction trust boundary. Guard high-impact operations outside the model and scope what data can influence. An untrusted input that requests three new privileges should acquire zero without an authorized decision.
29. **[A13.29 · per-agent budgets](lessons/A13.29.md).** Per-agent limits should fit a shared budget with reserved retry and aggregation capacity. Track consumed and reserved units. Five delegates with a shared budget of twenty calls can receive four each under equal allocation before reserving overhead.
30. **[A13.30 · policy enforcement](lessons/A13.30.md).** Deterministic enforcement should gate operations at their actual execution boundary. Validate identity, action, scope and current approval. One allowed operation in a three-operation registry leaves two denied by default.
31. **[A13.31 · evaluation of task success and side effects](lessons/A13.31.md).** Evaluate outcome correctness, forbidden effects, acceptable cost and evidence. Trace assertions should distinguish proposals from persisted effects. Two effect records for an operation expected once violate its side-effect condition, even if final text says success.
32. **[A13.32 · supervision and rollback](lessons/A13.32.md).** Supervision includes interrupting execution, observing outstanding work and reconciling side effects. Rollback may be compensation, not database undo. If three resources were allocated and two have confirmed cleanup, one still needs reconciliation.

### Put it together

A tool call may finish before the workflow records its result. On resume, reconcile the existing operation using its durable identity before issuing the action again. For an approved write, verify that the exact payload is still authorized and that the result records what changed.

## Practice and exit gate

- [L1 · Stateful workflow](labs/L1.md)
- [L2 · Tool authorization](labs/L2.md)
- [L3 · Approval checkpoint](labs/L3.md)
- [L4 · Workflow evaluation](labs/L4.md)
- [Guided · LangGraph stateful mock-tool workflow](projects/guided/README.md)
- [Independent · Approval-gated enterprise agent with audit](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Demonstrate the phase failure modes and defend the resource or trust boundaries with observed evidence.

Continue with [A14 · Advanced LLMOps, Evaluation & Safety](../A14-advanced-llmops-evals-safety/README.md) after the applicable gates.
