"""Deterministic lexical and dense baselines with judged retrieval metrics."""

import math
import re
import unicodedata
from collections import Counter

AXES = (
    {"archive", "backup", "recovery", "restore", "snapshot"},
    {"cache", "expiry", "latency", "redis", "ttl"},
    {"deploy", "rollout", "container", "pod", "release"},
)


def tokens(text: str) -> list[str]:
    return re.findall(r"\w+", unicodedata.normalize("NFKC", text).casefold())


def embed(text: str) -> tuple[int, ...]:
    words = tokens(text)
    return tuple(sum(word in axis for word in words) for axis in AXES)


def cosine(left: tuple[int, ...], right: tuple[int, ...]) -> float:
    norm = math.sqrt(sum(x * x for x in left) * sum(x * x for x in right))
    return sum(a * b for a, b in zip(left, right, strict=True)) / norm if norm else 0.0


def lexical(query: str, docs: dict[str, str]) -> list[str]:
    if not docs:
        return []
    frequencies = {key: Counter(tokens(text)) for key, text in docs.items()}
    average = sum(sum(row.values()) for row in frequencies.values()) / len(docs) or 1
    terms = sorted(set(tokens(query)))
    idf = {
        term: math.log1p((len(docs) - hits + 0.5) / (hits + 0.5))
        for term in terms
        for hits in [sum(term in row for row in frequencies.values())]
    }
    scores = {}
    for key, row in frequencies.items():
        denominator = 1.2 * (0.25 + 0.75 * sum(row.values()) / average)
        scores[key] = sum(
            idf[term] * 2.2 * row[term] / (row[term] + denominator) for term in terms
        )
    return ranked(scores)


def ranked(scores: dict[str, float]) -> list[str]:
    return sorted(
        (key for key, value in scores.items() if value > 0),
        key=lambda key: (-scores[key], key),
    )


def dense(query: str, docs: dict[str, str]) -> list[str]:
    vector = embed(query)
    return ranked({key: cosine(vector, embed(text)) for key, text in docs.items()})


def fuse(*rankings: list[str]) -> list[str]:
    scores: Counter[str] = Counter()
    for ranking in rankings:
        for rank, item in enumerate(ranking, 1):
            scores[item] += 1 / (60 + rank)
    return ranked(scores)


def evaluate(ranking: list[str], relevant: set[str], cutoff: int) -> dict[str, float]:
    if cutoff < 1 or not relevant or len(set(ranking)) != len(ranking):
        raise ValueError(
            "evaluation needs unique results, relevance judgments and positive cutoff"
        )
    observed = ranking[:cutoff]
    matches = [i for i, item in enumerate(observed, 1) if item in relevant]
    ideal = sum(1 / math.log2(i + 1) for i in range(1, min(cutoff, len(relevant)) + 1))
    return {
        "recall": len(matches) / len(relevant),
        "reciprocal_rank": 1 / matches[0] if matches else 0,
        "ndcg": sum(1 / math.log2(i + 1) for i in matches) / ideal,
    }


if __name__ == "__main__":
    collection = {"a": "snapshot archive", "b": "restore checklist", "c": "redis ttl"}
    for name, ranking in (
        ("bm25", lexical("backup", collection)),
        ("dense", dense("backup", collection)),
        ("hybrid", fuse(lexical("backup", collection), dense("backup", collection))),
    ):
        print(name, ranking, evaluate(ranking, {"a", "b"}, 2))
