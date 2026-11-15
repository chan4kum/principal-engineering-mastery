# Curriculum roadmap

The path below follows the detailed roadmap's stage order. The stage exit evidence translates each stage description into a reviewable checkpoint.

## Stage 0 · Diagnostic and discipline

Python memory model, arithmetic, process model, Linux commands, SQL and networking baselines; create practice repo and evidence log.

**Gate.** Run five diagnostics. Log misses and repeat with new inputs.

## Stage 1 · Computing and independent programming

A01, PY01-PY03, FND01, D01-D09, M01-M04, SQL01, OPS01: memory, syntax, runtime, DSA and measurable debugging.

**Gate.** Demonstrate independent programming and the A01 exit gate.

## Stage 2 · Backend and networks

A02-A04, PY04, SQL01, BE skills: socket-to-API trace, SQL/transactions, auth, caching, concurrency, reliable APIs.

**Gate.** Trace a request from socket to API to a transaction and recover a failed request.

## Stage 3 · Algorithms and multi-language systems

D10-D20, GO01-GO03, RUST01-RUST03, M05-M09: independent coding, complexity and systems reasoning.

**Gate.** Implement and analyze unfamiliar algorithms independently across the required languages.

## Stage 4 · Distributed platforms

A05-A09, G01-G02, platform/DevSecOps/SRE atlas: queues, consensus, container orchestration, incidents, Terraform.

**Gate.** Demonstrate failure recovery for a multi-service workload with observability evidence.

## Stage 5 · AWS, Azure and GCP architecture

W01-W13 and AZ01-AZ04, GC01-GC04, MC01-MC03: shared concepts then vendor implementation and cross-cloud design.

**Gate.** Defend a three-cloud design and a costed cleanup plan before any paid work.

## Stage 6 · ML and deep learning

M07-M13, A10, ML01X, DL01X-DL02X, G08: learning theory, gradients, backpropagation, statistical evaluation.

**Gate.** Derive and check a gradient, then evaluate a model with leakage controls.

## Stage 7 · Transformers and inference

A11, DL03X, I00-I30: attention by hand, tiny GPT, serving internals, capacity and profiling.

**Gate.** Trace attention and profile a constrained inference workload with a capacity calculation.

## Stage 8 · RAG, agents and LLMOps

A12-A14, security and AI skills atlas: enterprise retrieval, LangGraph/MCP, evals, governance, production operations.

**Gate.** Evaluate a retrieval or agent pipeline with data and failure cases.

## Stage 9 · Enterprise principal architecture

A15-A20, G03-G11, MC04, ENT01-ENT02, DSGN01-02, PRODUCT01, TEACH01: complex architecture and teaching.

**Gate.** Defend a principal design with architecture, operational and governance artifacts.

## Stage 10 · AI-assisted engineering last

AIC01-AIC03: prompt engineering, vibe/specification coding and loop/agentic coding, only after code independence gates.

**Gate.** Demonstrate independent coding first, then review AI-generated changes with tests and explicit stopping criteria.

## Curriculum index

Stage 0 and A01 have material in this edition. The remaining rows identify planned study by source ID. The inference crosswalk pairs the detailed roadmap's I00–I30 with the repository plan's 100–130.

### Architecture

| ID | Topic | Status |
| --- | --- | --- |
| A01 | Computer Systems & Operating Systems | [Available](01-architecture-A01-to-A20/A01-computer-systems-and-os/README.md) |
| A02 | Networking & Communication | Planned |
| A03 | Python Runtime & Backend API Engineering | Planned |
| A04 | Databases, SQL & Storage Engines | Planned |
| A05 | Scalability, Caching & Performance | Planned |
| A06 | Distributed Systems & Coordination | Planned |
| A07 | Application & Integration Architecture | Planned |
| A08 | Reliability, Operations & SRE | Planned |
| A09 | Cloud, Containers, Kubernetes & Platform Engineering | Planned |
| A10 | ML Foundations, AI Math & MLOps | Planned |
| A11 | Transformers, LLM Internals & Inference | Planned |
| A12 | Search, RAG & Knowledge Systems | Planned |
| A13 | Agentic AI, MCP & Workflow Orchestration | Planned |
| A14 | Advanced LLMOps, Evaluation & Safety | Planned |
| A15 | Security, Privacy & Global-Scale Architecture | Planned |
| A16 | System Design & Product-Company Interviews | Planned |
| A17 | Regulated AI: Compliance, Safety & Governance | Planned |
| A18 | Microsoft Foundry & Enterprise AI Platforms | Planned |
| A19 | Voice, Multimodal, Edge & Embedded AI | Planned |
| A20 | Forward-Deployed Engineering, Product & Leadership | Planned |

### Mathematics

| ID | Topic | Status |
| --- | --- | --- |
| M01 | Sets and mathematical language | Planned |
| M02 | Logic and proof | Planned |
| M03 | Linear systems | Planned |
| M04 | Vector spaces | Planned |
| M05 | Spectral methods | Planned |
| M06 | Projections | Planned |
| M07 | Low rank and SVD | Planned |
| M08 | ML math applications | Planned |
| M09 | Calculus and optimization | Planned |
| M10 | Probability | Planned |
| M11 | Joint random variables | Planned |
| M12 | Statistical inference | Planned |
| M13 | Information theory and deep learning | Planned |

### Data structures and algorithms

| ID | Topic | Status |
| --- | --- | --- |
| D01 | Complexity, math, recursion | Planned |
| D02 | Arrays | Planned |
| D03 | Hashing | Planned |
| D04 | Strings | Planned |
| D05 | Two pointers | Planned |
| D06 | Sliding window | Planned |
| D07 | Prefix/range | Planned |
| D08 | Sorting/intervals | Planned |
| D09 | Binary search | Planned |
| D10 | Linked lists | Planned |
| D11 | Stacks/queues | Planned |
| D12 | Trees/BST | Planned |
| D13 | Heap/top-k | Planned |
| D14 | Graphs | Planned |
| D15 | Backtracking | Planned |
| D16 | 1D DP | Planned |
| D17 | 2D DP | Planned |
| D18 | Greedy | Planned |
| D19 | Bits/number theory | Planned |
| D20 | Advanced data structures | Planned |

### Inference

| ID | Topic | Status |
| --- | --- | --- |
| 100 / I00 | Foundations | Planned |
| 101 / I01 | Serve a first LLM | Planned |
| 102 / I02 | One token end-to-end | Planned |
| 103 / I03 | Prefill, decode and KV cache | Planned |
| 104 / I04 | Benchmarking | Planned |
| 105 / I05 | Operating envelope | Planned |
| 106 / I06 | Serving engine | Planned |
| 107 / I07 | Continuous batching | Planned |
| 108 / I08 | PagedAttention | Planned |
| 109 / I09 | One GPU optimization | Planned |
| 110 / I10 | Prefill/prefix | Planned |
| 111 / I11 | Quantization/KV compression | Planned |
| 112 / I12 | Profiling | Planned |
| 113 / I13 | Triton kernels | Planned |
| 114 / I14 | Attention kernels | Planned |
| 115 / I15 | Compilation/CUDA graphs | Planned |
| 116 / I16 | Speculative decode | Planned |
| 117 / I17 | Engine comparison | Planned |
| 118 / I18 | Multi GPU | Planned |
| 119 / I19 | Mixture of experts | Planned |
| 120 / I20 | Long context | Planned |
| 121 / I21 | Disaggregated prefill/decode | Planned |
| 122 / I22 | Model lifecycle | Planned |
| 123 / I23 | Routing/autoscaling | Planned |
| 124 / I24 | Reliability/security | Planned |
| 125 / I25 | Economics | Planned |
| 126 / I26 | Specialized workloads | Planned |
| 127 / I27 | Engine reading | Planned |
| 128 / I28 | Mini engine | Planned |
| 129 / I29 | Research replication | Planned |
| 130 / I30 | Capstone | Planned |

### Cloud

| ID | Topic | Status |
| --- | --- | --- |
| W01 | Multi-account foundation and governance | Planned |
| W02 | Identity and access for AI workloads | Planned |
| W03 | Networking and private AI | Planned |
| W04 | Data foundation for AI and ML | Planned |
| W05 | Classical ML on SageMaker AI | Planned |
| W06 | MLOps on AWS | Planned |
| W07 | Foundation models and inference on AWS | Planned |
| W08 | RAG and knowledge systems on AWS | Planned |
| W09 | Agents and tool execution on AWS | Planned |
| W10 | LLMOps on AWS | Planned |
| W11 | Security, safety and governance for AI | Planned |
| W12 | DevSecOps and platform delivery | Planned |
| W13 | Reliability, scale and FinOps | Planned |
| AZ01 | Azure identity, governance and landing zones | Planned |
| AZ02 | Azure networking and hybrid connectivity | Planned |
| AZ03 | Azure compute, data and reliability | Planned |
| AZ04 | Azure AI platforms, ML and Agent systems | Planned |
| GC01 | GCP organization, identity and governance | Planned |
| GC02 | GCP networks and connectivity | Planned |
| GC03 | GCP compute, data and Kubernetes | Planned |
| GC04 | GCP AI, ML and GenAI | Planned |
| MC01 | Multi-cloud design and strategy | Planned |
| MC02 | Multi-cloud security, compliance and governance | Planned |
| MC03 | Cloud migration and modernization | Planned |
| MC04 | Enterprise architecture and operating model | Planned |

### Platform and enterprise

| ID | Topic | Status |
| --- | --- | --- |
| G01 | Kubernetes administration from first principles | Planned |
| G02 | Infrastructure as code, GitOps and zero trust | Planned |
| G03 | Data platforms for AI: lakehouse, Databricks, Snowflake, data mesh | Planned |
| G04 | Software architecture practice and documentation | Planned |
| G05 | AI security engineering and governance | Planned |
| G06 | Enterprise architecture and TOGAF | Planned |
| G07 | Cloud migration, hybrid networking and Well-Architected reviews | Planned |
| G08 | Distributed training and GPU systems | Planned |
| G09 | Claude and agent platforms in practice | Planned |
| G10 | Technical leadership, delivery and business cases | Planned |
| G11 | Kubernetes and pipeline security, and AI for DevSecOps | Planned |

### Capstones and interviews

| ID | Capstone | Status |
| --- | --- | --- |
| CAP01 | Independent Software Product - Transactional Service | Planned |
| CAP02 | Kubernetes Multi-Service Platform and SRE Game Day | Planned |
| CAP03 | Distributed Coordination and Event-Driven Backend | Planned |
| CAP04 | ML from First Principles to Reproducible Pipeline | Planned |

The principal interview bank, job-keyword index and 400-problem DSA catalogue are planned. The source roadmap also includes supplementary language, skills atlas, and product modules.

## Study cadence

On a short day, spend 15 minutes on a prediction, a dry-run and one retrieval question. For 90 minutes, use 15 for recall and reasoning, 20 for a guided experiment, 40 for independent work, 10 for errors and 5 for the evidence log. Use every sixth session for retrieval and rebuilding. Recheck at +1, +3, +7, +14, +30 and +60 days.
