# A20 · Forward-Deployed Engineering, Product & Leadership

**30 lessons · 4 labs · 2 projects**


Prerequisite [study and exit criteria](../A19-voice-multimodal-edge-embedded-ai/README.md).


| ID | Lesson | Tier |
| --- | --- | --- |
| [A20.01](lessons/A20.01.md) | business discovery and workflows | Foundation |
| [A20.02](lessons/A20.02.md) | user journeys | Foundation |
| [A20.03](lessons/A20.03.md) | success metrics | Foundation |
| [A20.04](lessons/A20.04.md) | constraints | Foundation |
| [A20.05](lessons/A20.05.md) | MVP scoping | Foundation |
| [A20.06](lessons/A20.06.md) | stakeholder map | Foundation |
| [A20.07](lessons/A20.07.md) | user experience failure paths | Foundation |
| [A20.08](lessons/A20.08.md) | value hypothesis | Core |
| [A20.09](lessons/A20.09.md) | design thinking and product requirements | Core |
| [A20.10](lessons/A20.10.md) | prototyping and customer validation | Core |
| [A20.11](lessons/A20.11.md) | architecture strategy | Core |
| [A20.12](lessons/A20.12.md) | ADRs | Core |
| [A20.13](lessons/A20.13.md) | vendor evaluation | Core |
| [A20.14](lessons/A20.14.md) | integration contracts | Core |
| [A20.15](lessons/A20.15.md) | budgets | Core |
| [A20.16](lessons/A20.16.md) | delivery and sequencing | Core |
| [A20.17](lessons/A20.17.md) | Scrum/Kanban | Core |
| [A20.18](lessons/A20.18.md) | ownership and RACI | Core |
| [A20.19](lessons/A20.19.md) | code/design reviews | Core |
| [A20.20](lessons/A20.20.md) | mentoring | Core |
| [A20.21](lessons/A20.21.md) | principal technical authority | Principal |
| [A20.22](lessons/A20.22.md) | escalations and trade-off negotiation | Principal |
| [A20.23](lessons/A20.23.md) | customer-in-environment delivery | Principal |
| [A20.24](lessons/A20.24.md) | technical roadmap and org-level standards | Principal |
| [A20.25](lessons/A20.25.md) | responsible AI adoption | Principal |
| [A20.26](lessons/A20.26.md) | ROI and value measurement | Principal |
| [A20.27](lessons/A20.27.md) | reliability governance | Principal |
| [A20.28](lessons/A20.28.md) | executive storytelling | Principal |
| [A20.29](lessons/A20.29.md) | technology radar | Principal |
| [A20.30](lessons/A20.30.md) | cross-team architecture alignment | Principal |

## Guided walkthrough

Follow a customer problem from discovery and scope through deployment, measurement, and cross-team ownership.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Discover workflows, goals, and constraints (A20.01–A20.07)

1. **[A20.01 · business discovery and workflows](lessons/A20.01.md).** Observe the workflow, record inputs, actors, exception paths and decision latency. Confirm a baseline and model which step could improve. Workflow takes 7+12+6=25 minutes. Cutting the 12-minute step to 5 yields 18.
2. **[A20.02 · user journeys](lessons/A20.02.md).** Map trigger, actor, decisions, handoffs and recovery. Track what happens before and after the interface. Three stages have failures 0,1,2 across disjoint fixture cases. Total is 3.
3. **[A20.03 · success metrics](lessons/A20.03.md).** Separate outcome, adoption and guardrail metrics. Establish denominators, cohorts and windows before claiming value. Median task time falls from 20 to 15 minutes: 25% reduction, or 5 minutes absolute.
4. **[A20.04 · constraints](lessons/A20.04.md).** List fixed time, staffing, data access and reliability constraints. Record which assumptions require negotiation and test high-risk ones early. A required scope costs 18 person-days with 14 available. Gap is four.
5. **[A20.05 · MVP scoping](lessons/A20.05.md).** Choose minimum scope that tests one value hypothesis and preserves necessary controls. Separate deferred work from exit criteria. Three features cost 4,5,3 days with a budget of 8. Features costing 4+3 fit. All need 12.
6. **[A20.06 · stakeholder map](lessons/A20.06.md).** Identify affected users, sponsor, operators, security and decision makers. Record authority, dependencies and disagreement resolution. Four named roles, three present. One role needs a follow-up.
7. **[A20.07 · user experience failure paths](lessons/A20.07.md).** Design recovery states with specific reasons, next actions and ownership. Test accessibility and timeout paths with representative users. Three non-happy paths exist, error states cover two, so one remains.

### Validate value and plan delivery (A20.08–A20.20)

8. **[A20.08 · value hypothesis](lessons/A20.08.md).** Propose an outcome, audience, baseline and time horizon with a guardrail. Define what evidence would reject the hypothesis. Baseline yield 60/100 and candidate 70/100 gives 10 percentage points, below a 12-point success target.
9. **[A20.09 · design thinking and product requirements](lessons/A20.09.md).** Prototype the smallest slice that captures a key assumption. Use observation to update the requirement and retain accessible failure acceptance tests. Of five observed tasks, three succeed unaided. Success share is 60%.
10. **[A20.10 · prototyping and customer validation](lessons/A20.10.md).** Define a sample, comparable tasks and evidence capture. Test real workflow constraints with a synthetic prototype when customer data is unavailable. Four observed users include two able to finish. Reporting one selected success inflates 50% to 100%.
11. **[A20.11 · architecture strategy](lessons/A20.11.md).** Map current constraints to a sequence of bounded changes. Establish interfaces, ownership, rollback and milestones tied to product outcomes. Three steps have verified dependencies, only first and second completed. One remains.
12. **[A20.12 · ADRs](lessons/A20.12.md).** Use an ADR with context, options, decision, measurable consequences and condition for revisiting. Link it to work and tests. Version 1 is superseded by version 2. Exactly one is current.
13. **[A20.13 · vendor evaluation](lessons/A20.13.md).** Apply mandatory capability and security criteria, then compare contract, operational cost, portability and lifecycle evidence on eligible options. Choices A/B meet 3/4 and 4/4 mandatory requirements. One qualifies.
14. **[A20.14 · integration contracts](lessons/A20.14.md).** Agree on schema, errors, deadlines, authentication, idempotency and ownership. Version contracts and run producer and consumer compatibility tests. Consumer requires fields a and b. Provider v2 emits a and c. One is missing.
15. **[A20.15 · budgets](lessons/A20.15.md).** Budget each cost driver and uncertainty, including one-time work, run cost and staffing. Tie spend to outcome metrics and capacity assumptions. Compute 40, storage 10 and support 30 total 80 units. Compute only reports 40.
16. **[A20.16 · delivery and sequencing](lessons/A20.16.md).** Model dependency ordering, unblock irreversible bottlenecks early, and bound work in progress. Verify the critical path through serial and parallel work. Two parallel tasks take 4 and 7 days then a 3-day integration. Critical path is 10, not 14.
17. **[A20.17 · Scrum/Kanban](lessons/A20.17.md).** Scrum defines roles, events and increments within sprints. Kanban defines flow and active work policies. Choose operating agreements and surface queues. WIP limit 3 with 2 active leaves one available slot.
18. **[A20.18 · ownership and RACI](lessons/A20.18.md).** Assign responsible and accountable roles, plus consultation and notification as appropriate. Decide who can resolve conflicting instructions. Two required decisions and one with named accountable owner leave one gap.
19. **[A20.19 · code/design reviews](lessons/A20.19.md).** Review behavior, failure handling, test evidence and decision risks. Separate blocking findings by actual consequences. One authorization defect and two nits yield one modeled rollout blocker.
20. **[A20.20 · mentoring](lessons/A20.20.md).** Choose a skill, practice, evidence and feedback loop. Scaffold early work and measure unaided performance after a delay. Three independent checks pass out of four, giving 75%.

### Lead decisions, adoption, and alignment (A20.21–A20.30)

21. **[A20.21 · principal technical authority](lessons/A20.21.md).** Clarify technical authority, escalation and exceptions. Retain the evidence and constraints behind the decision while inviting feedback. Three decision types include two with clearly assigned rights. One is ambiguous.
22. **[A20.22 · escalations and trade-off negotiation](lessons/A20.22.md).** Make trade-offs observable, identify decision owners, document exceptions with expiry, and compare options against a shared target. Option one risks 2 units and costs 8. Option two risks 5 and costs 5. Under risk cap 3 only one passes.
23. **[A20.23 · customer-in-environment delivery](lessons/A20.23.md).** Inventory identity, endpoints, policies and operational ownership in the customer environment. Validate connectivity, migration, rollback and useful observability. A readiness gate needs identity, routes and emergency contact. Two available yields a hold.
24. **[A20.24 · technical roadmap and org-level standards](lessons/A20.24.md).** Define scope, rationale, example implementation and time-bound exception process. Track adoption and unintended costs. Six teams in scope, four verified implementations gives adoption 4/6.
25. **[A20.25 · responsible AI adoption](lessons/A20.25.md).** Declare intended use, approved data categories, oversight, evaluations and incident response. Verify guardrails across rollout stages. Four capability classes, two approved, one requested is outside approved set.
26. **[A20.26 · ROI and value measurement](lessons/A20.26.md).** Estimate benefits against baseline and include recurring cost, one-time cost and uncertainty. Define payback and ROI denominator. Benefits 150 and total costs 100 yield net 50 and simple ROI 0.5.
27. **[A20.27 · reliability governance](lessons/A20.27.md).** Assign service-level ownership, release rules and incident review. Express burn as observed bad fraction divided by target bad fraction. At allowed bad rate 0.001, observed 0.002 gives 2x burn.
28. **[A20.28 · executive storytelling](lessons/A20.28.md).** State the outcome, current evidence and uncertainty, decision needed, owner and next checkpoint. Keep operational details traceable. Two options meet quality, one meets cost cap. The decision list contains one eligible choice.
29. **[A20.29 · technology radar](lessons/A20.29.md).** Use a reviewable adoption status and evidence across maturity, support, constraints and reversibility. Revisit after observed pilots. Three tooling options, one meets all gates and two remain in trial.
30. **[A20.30 · cross-team architecture alignment](lessons/A20.30.md).** Document shared invariants, owners and evolution. Use end-to-end contract evidence and track exceptions. Three integrations require revision 2. Two meet it and one needs change.

### Put it together

A customer workflow takes 25 minutes in the fixture. A prototype reduces one step by seven minutes, producing an 18-minute modeled total. Validate the result with representative users, track error and escalation paths, and agree on ownership and rollout criteria before expanding the deployment.

## Practice and exit gate

- [L1 · Small reproducible experiment](labs/L1.md)
- [L2 · Measured comparison](labs/L2.md)
- [L3 · Failure injection](labs/L3.md)
- [L4 · Independent exercise](labs/L4.md)
- [Customer discovery and MVP requirements](projects/guided/README.md)
- [Forward-deployed product from discovery through operations](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Score at least 80% on fresh cases, reproduce four labs, meet both project acceptance criteria, diagnose one unfamiliar failure, and repeat the assessment after a delay.
