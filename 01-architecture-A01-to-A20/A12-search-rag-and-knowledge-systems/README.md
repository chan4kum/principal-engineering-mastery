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

## Guided walkthrough

Follow a source document from parsing and indexing through authorized retrieval and evidence-backed answer generation.

Each linked lesson includes a model or control to run locally. Figures here describe the lesson examples.

### Build retrieval from text and vectors (A12.01–A12.09)

1. **[A12.01 · documents and tokenization](lessons/A12.01.md).** Tokenization defines searchable units. Index and query analyzers must be compatible, and original offsets matter for highlighting. Splitting sensor-data into two parts creates two terms instead of one compound term.
2. **[A12.02 · normalization](lessons/A12.02.md).** Normalize text consistently where the language permits. Unicode normalization, case folding and stemming are distinct operations with different collisions. If three spellings normalize to one key, posting aggregation changes from three buckets to one.
3. **[A12.03 · inverted indexes](lessons/A12.03.md).** An inverted index maps terms to document identifiers and optional posting attributes, such as term frequency and positions. A term appearing in 80 of 10000 documents can start from 80 postings instead of scanning 10000 documents.
4. **[A12.04 · posting lists](lessons/A12.04.md).** Posting lists are commonly sorted by document identifier. Linear merge intersection advances the smaller current identifier. Positions can support phrase checks. Intersect [1,3,7] and [3,4,7] to obtain [3,7], with O(a+b) worst-case merge work.
5. **[A12.05 · Boolean search](lessons/A12.05.md).** Boolean search applies set operators to document postings. Grouping, negation universe and field scope affect results. With postings {1,2} and {2,3}, AND returns one document while OR returns three.
6. **[A12.06 · TF-IDF and BM25](lessons/A12.06.md).** TF-IDF combines term frequency with rarity. BM25 saturates frequency gains and includes document-length normalization under its parameterization. At k1=1.2 and fixed normalized length one, tf=1 contributes 1.0 and tf=4 contributes about 1.692 before IDF.
7. **[A12.07 · stopwords](lessons/A12.07.md).** Stopword handling trades index size and noise against phrase meaning, domain vocabulary and query semantics. A four-token phrase with one removed stopword has three indexed tokens, but the original phrase still has four positions.
8. **[A12.08 · precision/recall](lessons/A12.08.md).** Precision is retrieved relevance over returned results. Recall is recovered relevance over all known relevant items in the judged set. With four returned, three relevant hits and six relevant total, precision is .75 and recall .5.
9. **[A12.09 · embeddings and vector similarity](lessons/A12.09.md).** Dot product depends on length and alignment. Cosine divides the dot product by vector norms. Zero vectors need a defined policy. Vectors [2,0] and [3,0] have dot product 6 and cosine 1.

### Retrieve, rerank, cite, and evaluate (A12.10–A12.21)

10. **[A12.10 · document parsing and lineage](lessons/A12.10.md).** Parsing extracts content with stable document and revision identifiers plus source spans. Normalization and chunking should maintain lineage to original evidence. If five pages produce two chunks each, ten chunks need lineage records even if their content repeats.
11. **[A12.11 · chunking](lessons/A12.11.md).** Chunk boundaries balance retrieval specificity against context and structural coherence. Measure using representative questions rather than one target length. A 1000-token document divided into nonoverlapping 250-token chunks yields four under the idealized model.
12. **[A12.12 · chunk overlap](lessons/A12.12.md).** Overlap preserves boundary context but increases storage and duplicate candidates. Window size w and overlap o give stride w−o. A 200-token window with 50-token overlap advances 150 tokens per step.
13. **[A12.13 · metadata and ACLs](lessons/A12.13.md).** Authorize the candidate set using trusted tenant and ACL scope before ranking, reranking or sending text to a model. For ten candidates with four unauthorized, six may advance to ranking under the fixture's simple policy.
14. **[A12.14 · hybrid sparse+dense search](lessons/A12.14.md).** Hybrid retrieval can fuse ranks or calibrated scores. Reciprocal rank fusion sums 1/(k+rank) across participating lists. For ranks 1 and 4 with k=60, RRF score is 1/61+1/64≈.03202.
15. **[A12.15 · approximate nearest neighbors](lessons/A12.15.md).** ANN trades search cost for neighbor recall. Use an exact baseline on a suitable sample and measure filtered and unfiltered performance separately. Eight matches with the exact top ten give an index recall of .8.
16. **[A12.16 · HNSW and index updates](lessons/A12.16.md).** HNSW uses a navigable hierarchy of proximity graphs. Build and search parameters affect cost and recall, and deletion support depends on the implementation. A graph with 1000 nodes and average 16 stored link references has about 16000 links before overhead.
17. **[A12.17 · query rewriting](lessons/A12.17.md).** Query rewriting changes expression, not authority or trusted filters. Preserve the original query and deterministic restrictions as separate fields. Three query variants with top five candidates each produce at most 15 candidates before deduplication.
18. **[A12.18 · reranking and cross encoders](lessons/A12.18.md).** A cross-encoder jointly scores a query and document, unlike independent embedding scoring. It is generally applied to a bounded candidate list. At 2 ms per pair and 50 serialized candidate pairs, reranking needs about 100 ms before queue overhead.
19. **[A12.19 · evidence citations](lessons/A12.19.md).** A usable citation identifies a retrievable source, revision and relevant span. Formatting a citation does not prove entailment. If two of four cited claims are actually supported, claim-level support is .5 under equal weighting.
20. **[A12.20 · retrieval metrics recall@k/MRR/nDCG](lessons/A12.20.md).** Recall@k counts judged relevant items found. Reciprocal rank emphasizes the first relevant rank. nDCG discounts ranked relevance gains and normalizes by ideal ordering. First relevant at rank four yields reciprocal rank .25. If two of five relevant items appear in the cutoff, recall is .4.
21. **[A12.21 · grounding and answer quality](lessons/A12.21.md).** Grounding tests whether claims follow from authorized, relevant evidence. An abstention policy handles unsupported or conflicting results. If seven of ten verifiable claims are supported, the support fraction is .7 under an equal-claim definition.

### Operate a fresh and isolated search system (A12.22–A12.34)

22. **[A12.22 · search index synchronization and deletes](lessons/A12.22.md).** CDC or another change feed needs revisions, durable offsets, deletion propagation and reconciliation. Cache keys need scope and version. At 40 updates/s and 5 s pipeline lag, about 200 updates can be pending under stable rate.
23. **[A12.23 · deduplication](lessons/A12.23.md).** Exact deduplication uses content identity. Near-duplicate methods trade recall and false merges. Maintain provenance and permissions for retained copies. Seven identical copies and three distinct items produce four unique content groups.
24. **[A12.24 · sharded indexes](lessons/A12.24.md).** Each shard returns candidates. A coordinator merges them under a shared scoring convention. Local corpus statistics and partial shard failure can change global behavior. Four shards returning three candidates each supply up to 12 for merge before duplicates.
25. **[A12.25 · crawler pipelines](lessons/A12.25.md).** A crawl frontier tracks canonical URLs, visit state and bounded scheduling. Respect scope, robots and allowlisted test data. Crawling is separate from parser retries. Ten pages with four links each create up to 40 discovered edges, not necessarily 40 unique URLs.
26. **[A12.26 · multi-hop retrieval](lessons/A12.26.md).** Multi-hop retrieval follows intermediate entities or evidence relationships. Each intermediate claim needs provenance and scope. Branching increases latency and error risk. A branching factor three over two levels gives at most nine leaf candidates before pruning.
27. **[A12.27 · structured+graph retrieval](lessons/A12.27.md).** Structured queries filter typed fields and join known relationships. Graph traversal and text retrieval can complement each other under shared authority boundaries. Two starting entities with three outgoing eligible edges each yield at most six one-hop targets before deduplication.
28. **[A12.28 · freshness](lessons/A12.28.md).** Freshness depends on source update, queue, indexing, publication and cache invalidation. An index revision can be included in cache identity. An update taking 3 s to index and 2 s to invalidate can remain stale for roughly 5 s along that serial path.
29. **[A12.29 · reranking budgets](lessons/A12.29.md).** Candidates per request multiply request rate and score cost. Cap candidate counts and apply deadline-aware degradation only with policy. At 100 RPS and 20 candidates per request, demand is 2000 pairs/s before retries.
30. **[A12.30 · tenant authorization at query time](lessons/A12.30.md).** Authorization should independently constrain every query, candidate and returned source. Cache keys need trusted scope and revision, and mixed-scope sharing needs explicit proof. Two tenants and one query yield two scoped cache entries in this example.
31. **[A12.31 · prompt injection via retrieved data](lessons/A12.31.md).** Treat retrieved data as evidence rather than authority. Capability and access checks belong outside the model. An untrusted passage may be quoted or summarized under policy without controlling tool permissions. One retrieved record can add zero tool scopes when authorization is held outside the retrieved context.
32. **[A12.32 · large-scale ingestion reliability](lessons/A12.32.md).** A durable ingestion identity ties source, revision and processing stages. Bound retries, isolate failures, reconcile missing records and trace lag. At 80 docs/min incoming and 60 docs/min processed, queue depth grows 20/min if those rates persist.
33. **[A12.33 · eval drift and human review](lessons/A12.33.md).** Evaluation drift includes changing traffic, source coverage, annotations and expectations. Maintain a stable baseline plus audited rolling slices with human review. A 20% review sample of 500 cases contains 100 cases under the simplified sampling model.
34. **[A12.34 · autocomplete and spell correction](lessons/A12.34.md).** Autocomplete ranks prefix candidates under context and policy. Spell correction compares candidate costs and language evidence, leaving valid exact matches where appropriate. At maximum edit distance one, a candidate requiring two edits is excluded in a simple policy.

### Put it together

When an answer lacks its expected citation, test retrieval before tuning generation. Compare whether the target passage appears in the eligible candidate set, survives reranking, and reaches the model with its source identifier. Repeat with a caller who lacks permission and verify the passage stays absent at every stage.

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
