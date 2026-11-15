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

## Practice and exit gate

- [L1 · Stateful workflow](labs/L1.md)
- [L2 · Tool authorization](labs/L2.md)
- [L3 · Approval checkpoint](labs/L3.md)
- [L4 · Workflow evaluation](labs/L4.md)
- [Guided · LangGraph stateful mock-tool workflow](projects/guided/README.md)
- [Independent · Approval-gated enterprise agent with audit](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Demonstrate the phase failure modes and defend the resource or trust boundaries with observed evidence.
