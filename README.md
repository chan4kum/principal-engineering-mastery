# Principal Engineering Mastery

![Coverage](https://img.shields.io/badge/curriculum-Stage%200%20%2B%20A01--A06-1f6feb)
![Labs](https://img.shields.io/badge/labs-local--first-147d64)
![Python](https://img.shields.io/badge/python-3.12%2B-345f9c)
![License](https://img.shields.io/badge/license-MIT%20%2F%20CC%20BY--SA%204.0-555)

**Understand → Calculate → Implement → Break → Repair → Rebuild → Teach → Retain**

A practice-first curriculum for software, cloud and AI systems. Start with a diagnostic, then connect program behavior to OS evidence. Each A01–A06 lesson includes a trace, a runnable example, and a controlled alternative.

| Start here | What you'll do |
| --- | --- |
| [Stage 0 diagnosis](00-stage-0-diagnostic/README.md) | Check five prerequisite skills and log gaps |
| [A01 systems and OS](01-architecture-A01-to-A20/A01-computer-systems-and-os/README.md) | Work through 36 lessons, four labs and two projects |
| [A02 networking](01-architecture-A01-to-A20/A02-networking-and-communication/README.md) | Trace requests through DNS, transport, TLS and HTTP |
| [A03 Python runtime and backend APIs](01-architecture-A01-to-A20/A03-python-runtime-and-backend-apis/README.md) | Trace execution, concurrency and API behavior |
| [A04 databases and storage](01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/README.md) | Diagnose SQL plans, transactions and recovery |
| [A05 scalability and performance](01-architecture-A01-to-A20/A05-scalability-caching-performance/README.md) | Estimate capacity and test cache, queue and admission behavior |
| [A06 distributed systems](01-architecture-A01-to-A20/A06-distributed-systems-coordination/README.md) | Trace partitions, quorum, retries and fencing |
| [Curriculum roadmap](ROADMAP.md#curriculum-index) | Inspect later tracks and their planned scope |
| [Teaching contract](TEACHING_CONTRACT.md) | Pair with a tutor and preserve independent assessment |
| [Progress tracker](PROGRESS_TRACKER.md) | Record evidence and schedule retrieval practice |

## Five-minute quickstart

Install [uv](https://docs.astral.sh/uv/) and use Python 3.12 or later.

```sh
git clone https://github.com/chan4kum/principal-engineering-mastery.git
cd principal-engineering-mastery
uv sync --locked
uv run python 00-stage-0-diagnostic/diagnose.py
uv run --locked --extra math --extra api pytest -q
```

Use Linux for real /proc and cgroup evidence. macOS supports the portable exercises and can run the Linux labs through a local Docker engine. The diagnostic and Phase A01 require no paid service. See the lab instructions for container limits and cleanup.

## Dependency path

```mermaid
flowchart TD
    s0["0 · Diagnostic and discipline"]
    s1["1 · Computing and independent programming"]
    s2["2 · Backend and networks"]
    s3["3 · Algorithms and multi-language systems"]
    s4["4 · Distributed platforms"]
    s5["5 · AWS, Azure and GCP architecture"]
    s6["6 · ML and deep learning"]
    s7["7 · Transformers and inference"]
    s8["8 · RAG, agents and LLMOps"]
    s9["9 · Enterprise principal architecture"]
    s10["10 · AI-assisted engineering last"]
    s0 --> s1
    s1 --> s2
    s2 --> s3
    s3 --> s4
    s4 --> s5
    s5 --> s6
    s6 --> s7
    s7 --> s8
    s8 --> s9
    s9 --> s10
    classDef available fill:#d5f2e3,stroke:#147d64,color:#10252a
    class s0 available
```

Stage 1 includes A01. Stage 2 includes A02–A04. Stage 4 currently includes A05 and A06. See the [roadmap](ROADMAP.md) for stage gates and the [curriculum index](ROADMAP.md#curriculum-index) for coverage by track.

### Curriculum by track

[Architecture](ROADMAP.md#architecture) · [Mathematics](ROADMAP.md#mathematics) · [DSA](ROADMAP.md#data-structures-and-algorithms) · [Inference](ROADMAP.md#inference) · [AWS, Azure and GCP](ROADMAP.md#cloud) · [Platform and enterprise](ROADMAP.md#platform-and-enterprise) · [Capstones and interviews](ROADMAP.md#capstones-and-interviews)

## How to study

On a tablet, predict outputs and use the diagrams and collapsed answer sections. On a laptop, compare normal and failure modes and save the exact command, result and repair. Choose sessions of 15–90 minutes and work on one active concept at a time. Give your AI tutor the contract and the current tracker entry when resuming.

## Source and design

Lesson IDs and A01 titles follow the detailed *Principal Software, Cloud & AI Complete Mastery Roadmap* and the architecture index of *Principal AI Architect Master Roadmap v3*. The supplied standalone teaching contract and combined edition inform the learner and tutor protocol.

Navigation, active recall, progressive builds and runnable projects were benchmarked against [The System Design Primer](https://github.com/donnemartin/system-design-primer), [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero) and [Build Your Own X](https://github.com/codecrafters-io/build-your-own-x).

[Contribute](CONTRIBUTING.md) · [License](LICENSE)
