"""Immutable synthetic release identities and measured rollback."""

import json
from dataclasses import dataclass
from hashlib import sha256


@dataclass(frozen=True)
class Release:
    model: str
    prompt: str
    fixture: str

    @property
    def identity(self):
        wire = json.dumps([self.model, self.prompt, self.fixture], separators=(",", ":"))
        return sha256(wire.encode()).hexdigest()


class Promotion:
    def __init__(self, stable: Release, expected_ids: frozenset[str]):
        if not expected_ids:
            raise ValueError("expected cases required")
        self.active = self.stable = stable
        self.expected_ids = expected_ids

    def consider(self, candidate: Release, evidence: dict, max_cost: int, cost: int):
        if candidate.fixture != self.stable.fixture or set(evidence) != self.expected_ids:
            return False
        valid = [row["answer"] and row["grounded"] and row["scope"] for row in evidence.values()]
        veto = any(
            not row["scope"] or (row["critical"] and not passed)
            for row, passed in zip(evidence.values(), valid, strict=True)
        )
        if veto or sum(valid) * 5 < len(valid) * 4 or not 0 <= cost <= max_cost:
            return False
        self.active = candidate
        return True

    def rollback(self):
        self.active = self.stable
        return self.active.identity
