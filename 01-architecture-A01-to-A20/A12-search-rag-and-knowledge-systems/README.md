# A12 · Search, RAG & Knowledge Systems

**34 lessons · 4 labs · 2 projects**

Build lexical and dense retrieval, evaluate rankings, and preserve document scope and lineage as sources change. The local reference uses deterministic synthetic embeddings and extractive evidence.

Prerequisite [A11 exit gate](../A11-transformers-llm-internals/README.md#practice-and-exit-gate).

| ID | Lesson | Tier |
| --- | --- | --- |
| [A12.01](lessons/A12.01.md) | documents and tokenization | Foundation |
| [A12.02](lessons/A12.02.md) | normalization | Foundation |
| [A12.03](lessons/A12.03.md) | inverted indexes | Foundation |
| [A12.04](lessons/A12.04.md) | posting lists | Foundation |
| [A12.05](lessons/A12.05.md) | Boolean search | Foundation |
| [A12.06](lessons/A12.06.md) | TF-IDF and BM25 | Foundation |
| [A12.07](lessons/A12.07.md) | stopwords | Foundation |
| [A12.08](lessons/A12.08.md) | precision/recall | Foundation |
| [A12.09](lessons/A12.09.md) | embeddings and vector similarity | Foundation |
| [A12.10](lessons/A12.10.md) | document parsing and lineage | Core |
| [A12.11](lessons/A12.11.md) | chunking | Core |
| [A12.12](lessons/A12.12.md) | chunk overlap | Core |
| [A12.13](lessons/A12.13.md) | metadata and ACLs | Core |
| [A12.14](lessons/A12.14.md) | hybrid sparse+dense search | Core |
| [A12.15](lessons/A12.15.md) | approximate nearest neighbors | Core |
| [A12.16](lessons/A12.16.md) | HNSW and index updates | Core |
| [A12.17](lessons/A12.17.md) | query rewriting | Core |
| [A12.18](lessons/A12.18.md) | reranking and cross encoders | Core |
| [A12.19](lessons/A12.19.md) | evidence citations | Core |
| [A12.20](lessons/A12.20.md) | retrieval metrics recall@k/MRR/nDCG | Core |
| [A12.21](lessons/A12.21.md) | grounding and answer quality | Core |
| [A12.22](lessons/A12.22.md) | search index synchronization and deletes | Principal |
| [A12.23](lessons/A12.23.md) | deduplication | Principal |
| [A12.24](lessons/A12.24.md) | sharded indexes | Principal |
| [A12.25](lessons/A12.25.md) | crawler pipelines | Principal |
| [A12.26](lessons/A12.26.md) | multi-hop retrieval | Principal |
| [A12.27](lessons/A12.27.md) | structured+graph retrieval | Principal |
| [A12.28](lessons/A12.28.md) | freshness | Principal |
| [A12.29](lessons/A12.29.md) | reranking budgets | Principal |
| [A12.30](lessons/A12.30.md) | tenant authorization at query time | Principal |
| [A12.31](lessons/A12.31.md) | prompt injection via retrieved data | Principal |
| [A12.32](lessons/A12.32.md) | large-scale ingestion reliability | Principal |
| [A12.33](lessons/A12.33.md) | eval drift and human review | Principal |
| [A12.34](lessons/A12.34.md) | autocomplete and spell correction | Principal |

## Practice and exit gate

- [L1 · Retrieval baseline](labs/L1.md)
- [L2 · Hybrid ranking](labs/L2.md)
- [L3 · Tenant isolation](labs/L3.md)
- [L4 · Freshness](labs/L4.md)
- [Guided · BM25 versus vector benchmark](projects/guided/README.md)
- [Independent · Tenant-safe hybrid RAG service with evaluations](projects/independent/README.md)
- [Applied assessment](ASSESSMENT.md)

Reproduce all labs and both project acceptance suites. Score at least 80% on a fresh set of questions, diagnose one unfamiliar failure, and repeat after a delay. Demonstrate the phase failure modes and defend the resource or trust boundaries with observed evidence.

Continue to [A13 · Agentic AI, MCP & Workflow Orchestration](../A13-agentic-ai-mcp-orchestration/README.md) when the prerequisite stage gates are met.
