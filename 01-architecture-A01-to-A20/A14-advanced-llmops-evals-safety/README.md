# A14 · Advanced LLMOps, Evaluation & Safety

**28 lessons · 4 labs · 2 projects**


Prerequisite [study and exit criteria](../A13-agentic-ai-mcp-orchestration/README.md).


| ID | Lesson | Tier |
| --- | --- | --- |
| [A14.01](lessons/A14.01.md) | quality goals and ground truth | Foundation |
| [A14.02](lessons/A14.02.md) | deterministic vs probabilistic outputs | Foundation |
| [A14.03](lessons/A14.03.md) | offline vs online evaluation | Foundation |
| [A14.04](lessons/A14.04.md) | model and prompt versioning | Foundation |
| [A14.05](lessons/A14.05.md) | traces and token usage | Foundation |
| [A14.06](lessons/A14.06.md) | test datasets and golden sets | Core |
| [A14.07](lessons/A14.07.md) | retrieval vs generation evaluations | Core |
| [A14.08](lessons/A14.08.md) | groundedness and hallucination rates | Core |
| [A14.09](lessons/A14.09.md) | LLM judge calibration | Core |
| [A14.10](lessons/A14.10.md) | regression tests | Core |
| [A14.11](lessons/A14.11.md) | prompt/model registry | Core |
| [A14.12](lessons/A14.12.md) | eval in CI/CD | Core |
| [A14.13](lessons/A14.13.md) | model routing | Core |
| [A14.14](lessons/A14.14.md) | structured output validity | Core |
| [A14.15](lessons/A14.15.md) | cost and latency budgets | Core |
| [A14.16](lessons/A14.16.md) | streaming metrics | Core |
| [A14.17](lessons/A14.17.md) | experiment design | Core |
| [A14.18](lessons/A14.18.md) | human annotation | Core |
| [A14.19](lessons/A14.19.md) | A/B experiments and counterfactuals | Principal |
| [A14.20](lessons/A14.20.md) | data flywheel and labeling | Principal |
| [A14.21](lessons/A14.21.md) | observability taxonomies | Principal |
| [A14.22](lessons/A14.22.md) | drift and feedback loops | Principal |
| [A14.23](lessons/A14.23.md) | adversarial red-teaming | Principal |
| [A14.24](lessons/A14.24.md) | quality/latency/cost Pareto | Principal |
| [A14.25](lessons/A14.25.md) | rollback and guardrail failure paths | Principal |
| [A14.26](lessons/A14.26.md) | serving capacity planning | Principal |
| [A14.27](lessons/A14.27.md) | self-host/API economics | Principal |
| [A14.28](lessons/A14.28.md) | incident analysis and model governance | Principal |

## Guided walkthrough

Turn a model quality goal into a repeatable evaluation, then use the results to decide whether to release, route, or roll back.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Define the quality target and trace inputs (A14.01–A14.05)

1. **[A14.01 · quality goals and ground truth](lessons/A14.01.md).** Define each field, establish acceptable alternatives, adjudicate disagreements and freeze the labels before scoring. A label is a reviewable judgment produced by a protocol. Three of four adjudicated answers pass, so case accuracy is 3/4. Omitting the failure changes the denominator and reports 3/3.
2. **[A14.02 · deterministic vs probabilistic outputs](lessons/A14.02.md).** Separate the exact release identity from sampling variation. Measure repeated trials across fixed inputs and multiple draws. Identical inputs can still differ across infrastructure or model versions. Four responses score 1,1,0,1. Four draws estimate 75% pass. First draw alone reports 100%.
3. **[A14.03 · offline vs online evaluation](lessons/A14.03.md).** Offline replay isolates repeatable cases. Randomized live assignment estimates outcome under current traffic. Track cohort mix, guardrails and time windows separately. Equal-weight strata with scores 0.9 and 0.5 average 0.7. With 75% easy requests the weighted score is 0.8.
4. **[A14.04 · model and prompt versioning](lessons/A14.04.md).** Record identifiers for model snapshot, system prompt, schema, data snapshot and evaluator. Keep a stable canonical representation for content hashing. Two prompts and two models yield four combinations. A model-only key collapses them into two.
5. **[A14.05 · traces and token usage](lessons/A14.05.md).** Measure provider-reported input/output once per call. Attribute known subdivisions separately and reserve a category for unattributed input. Cached-token units follow the provider contract. Total input is 500 with 300 explicitly retrieved. Charging 500+300 counts those tokens twice.

### Build evaluation evidence and release checks (A14.06–A14.18)

6. **[A14.06 · test datasets and golden sets](lessons/A14.06.md).** Separate development cases and held-out release cases by provenance groups. Freeze review, labels and membership, then add new regression cases without silently editing the old release. Two paraphrases share group g1. Group-based splitting puts one group in train and the other in test, with zero shared groups.
7. **[A14.07 · retrieval vs generation evaluations](lessons/A14.07.md).** Score retrieval against expected sources and answer against accepted content. Record the failure stage. A lucky guess can pass answer scoring with no evidence. Expected source s2 ranks second among two. Recall@1=0 and Recall@2=1. Answer success is a separate bit.
8. **[A14.08 · groundedness and hallucination rates](lessons/A14.08.md).** Break text into checkable claims, ensure cited evidence exists, then judge whether it supports each claim. Track unsupported and unverifiable separately by rubric. Three checkable claims have labels supported, supported, unsupported. Unsupported rate is 1/3, whereas all three list a citation.
9. **[A14.09 · LLM judge calibration](lessons/A14.09.md).** Sample human-labeled cases, define agreement, report a confusion matrix and recalibrate after evaluator changes. Review disagreements by cohort and failure severity. TP=3, FP=2, TN=4, FN=1 gives judge-positive precision 3/5 and recall 3/4.
10. **[A14.10 · regression tests](lessons/A14.10.md).** Apply both overall and slice-level thresholds. Keep a mandatory veto for high-severity policy failures. Compare on the same held-out fixtures. 99 of 100 pass, including zero of one safety-critical case. An overall 95% gate alone accepts.
11. **[A14.11 · prompt/model registry](lessons/A14.11.md).** Separate immutable versions and mutable release aliases. Bind the prompt, schema, model, evaluator and compatibility metadata into a release manifest. Prompt versions 1 and 2 reference different schemas. Rolling back alias to release 1 restores schema s1 too.
12. **[A14.12 · eval in CI/CD](lessons/A14.12.md).** Validate expected case count and version before executing the release gate. Treat missing data or an evaluator exception as an unavailable result and keep the release on hold. A gate requires three outcomes, all passing. An empty list satisfies Python all and fails the required-count check.
13. **[A14.13 · model routing](lessons/A14.13.md).** Filter candidates by capability and policy before optimizing for cost. Use a default abstention when no candidate qualifies and record the reason. A 900-token input needs a limit of at least 900. A cheap route at 512 is filtered, leaving the 1024-token route.
14. **[A14.14 · structured output validity](lessons/A14.14.md).** Parse JSON, validate structural types and required properties, then apply an independent domain invariant. A valid enum or number still can be semantically wrong. The first fixture has amount=4 in a dictionary. An empty dictionary parses as a document and fails the amount predicate.
15. **[A14.15 · cost and latency budgets](lessons/A14.15.md).** Track latency quantiles over consistent windows and input/output units separately. Apply independent budget gates to the same candidate. Three calls cost 2,3,5 units and take 10,40,70 ms. Total cost ≤10, max latency exceeds 50.
16. **[A14.16 · streaming metrics](lessons/A14.16.md).** Timestamp request submission, first token and each later token at the consumer. Separate time to first token, inter-token gaps and completion time. Tokens arrive at 50,60,130 ms from submission. TTFT=50 and max subsequent gap=70.
17. **[A14.17 · experiment design](lessons/A14.17.md).** Predefine the primary metric, sample unit and minimum useful effect. Match on cases for paired offline evaluation and preserve the randomization unit for live tests. Baseline scores [0,1,1,0], candidate [1,1,0,1]. Paired deltas average (1+0−1+1)/4=0.25.
18. **[A14.18 · human annotation](lessons/A14.18.md).** Annotate independently, report raw agreement and inspect disagreement before adjudicating. Chance-adjusted measures depend on label marginals and may differ from raw agreement. Review pairs (1,1),(1,0),(0,0),(1,1) yield 3/4 agreement. Removing the disagreement reports 1.

### Compare trade-offs and govern incidents (A14.19–A14.28)

19. **[A14.19 · A/B experiments and counterfactuals](lessons/A14.19.md).** Assign by stable unit and use intention-to-treat denominators. An observational difference estimates association unless a defensible identification strategy handles confounding. Control 40/100 and treatment 48/100 yields an 8 percentage-point difference. Dividing by 0.4 instead yields 20% relative lift.
20. **[A14.20 · data flywheel and labeling](lessons/A14.20.md).** Deduplicate based on case provenance, record selection and review lag, then split by source or incident group to reduce leakage. Three records cite incident 7 twice and 8 once. Independent incident groups count two.
21. **[A14.21 · observability taxonomies](lessons/A14.21.md).** Use a stable low-cardinality error class and a trace ID for investigation. Separate transport failure, policy denial and invalid output from domain outcomes. Three events have one timeout and two different external IDs. Counting raw IDs yields three series. Counting the single failure class yields one.
22. **[A14.22 · drift and feedback loops](lessons/A14.22.md).** Compare input or cohort frequency, feedback coverage and cohort-level outcomes. Outcome drift requires delayed ground truth or an explicitly identified proxy. Easy share moves 80/100 to 60/100 while evaluator score stays 90/100. Easy share falls by 20 points.
23. **[A14.23 · adversarial red-teaming](lessons/A14.23.md).** Build a fixed corpus of benign local boundary checks with mock effects. Count prevented unauthorized effects and separately score legitimate requests that policy denies. One forbidden and two legitimate fixtures are exercised. A policy denying all prevents all forbidden effects while blocking two legitimate cases.
24. **[A14.24 · quality/latency/cost Pareto](lessons/A14.24.md).** A candidate is Pareto dominated if another is at least as good on every objective and strictly better on one. Retain nondominated choices before applying policy thresholds. A=(quality 90, ms 80) and B=(90,100). A dominates B because quality is equal and latency lower.
25. **[A14.25 · rollback and guardrail failure paths](lessons/A14.25.md).** Represent candidate and stable versions separately, evaluate a small cohort, and atomically choose a serving alias. Preserve last-known-good artifacts and verify restored behavior. The candidate fails one required case and stable v1 remains active. A blind promotion selects v2.
26. **[A14.26 · serving capacity planning](lessons/A14.26.md).** Estimate arrival and service rates in the same units. Headroom, queue memory and burst admission matter before saturation. Measure observed percentiles under realistic requests. Four workers at 20 requests/s provide nominal 80. At 60 requests/s, utilization is 0.75. Loss of two workers raises it to 1.5.
27. **[A14.27 · self-host/API economics](lessons/A14.27.md).** Compare cost on identical load and quality targets. Include utilization, idle and operational cost, retries and commitment amortization. Fixed cost 300 units and variable 0.02 versus API 0.05 per request yields break-even at 10,000 requests.
28. **[A14.28 · incident analysis and model governance](lessons/A14.28.md).** Keep a timeline, bound exposure, identify the causal change, and assign verification evidence to an owner. Trace provenance and access from every released artifact. Three corrective controls expire in 7,14,30 days. A weekly review catches the earliest at day 7. Checking only the last deadline misses it.

### Put it together

Suppose a candidate improves aggregate pass rate from 88% to 91% but fails a required safety slice. Inspect that slice and the adjudicated examples before rollout. Keep the candidate and baseline versions pinned so the team can reproduce the difference and verify a rollback against the same cases.

## Practice and exit gate

- [L1 · Golden set](labs/L1.md)
- [L2 · Cost trace](labs/L2.md)
- [L3 · Canary change](labs/L3.md)
- [L4 · Safety tests](labs/L4.md)
- [LLM golden-set evaluator](projects/guided/README.md)
- [Versioned LLM release pipeline with canary/rollback](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Score at least 80% on fresh cases, reproduce four labs, meet both project acceptance criteria, diagnose one unfamiliar failure, and repeat the assessment after a delay.

Continue with [A15 · Security, Privacy & Global-Scale Architecture](../A15-security-privacy-global-scale/README.md) after the applicable gates.
