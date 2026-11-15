# A12 · Applied assessment

Attempt these before reviewing the answers. Pass eight of ten, reproduce all labs and both project suites, then demonstrate one fresh failure diagnosis and a delayed re-test.

1. What do inverted indexes map?
2. How does BM25 treat repeated terms?
3. What does recall .5 mean for six judged relevant documents?
4. What does reciprocal rank .25 imply?
5. Why compare ANN with an exact baseline?
6. Where must authorization run?
7. Why scope query caches by tenant?
8. When should the example abstain?
9. What does a tombstone prevent?
10. Does an evidence passage grant a tool capability?

<details>
<summary>Answers</summary>

1. Terms to postings that identify matching documents and optionally positions or counts.
2. It gives diminishing gains and accounts for document length.
3. Three were retrieved at the defined cutoff.
4. The first relevant result is in fourth position.
5. To measure missed true neighbors under the same metric and filters.
6. Before evidence is ranked or passed downstream.
7. Identical query text can have different authorized readings.
8. When no authorized evidence meets the retrieval fixture's candidate rules.
9. A late older version recreating content after a delete.
10. No. Trusted application policy controls capabilities.

</details>
