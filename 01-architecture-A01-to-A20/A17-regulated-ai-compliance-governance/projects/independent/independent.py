"""Bind a simulated administrative effect to qualified review and evidence."""

import json
from dataclasses import asdict, dataclass
from hashlib import sha256


def digest(value) -> str:
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


@dataclass(frozen=True)
class Approval:
    reviewer: str
    request_digest: str
    expires_at: int


class Audit:
    def __init__(self, sources: set[str], reviewers: set[str]):
        self.sources = set(sources)
        self.reviewers = set(reviewers)
        self.events = []
        self.effects = set()

    def execute(self, request, approval: Approval, clock: int) -> bool:
        identity = digest(asdict(request))
        allowed = (
            request.purpose == "administrative-draft"
            and request.evidence_version in self.sources
            and approval.reviewer in self.reviewers
            and approval.reviewer != request.requester
            and approval.request_digest == identity
            and clock < approval.expires_at
        )
        outcome = "denied"
        if allowed:
            outcome = "replayed" if identity in self.effects else "recorded"
            self.effects.add(identity)
        previous = self.events[-1]["hash"] if self.events else "root"
        event = {
            "previous": previous,
            "case": request.case_id,
            "request": identity,
            "reviewer": approval.reviewer,
            "result": outcome,
            "clock": clock,
        }
        self.events.append({**event, "hash": digest(event)})
        return allowed


def verify(events, trusted_head: str) -> bool:
    previous = "root"
    for event in events:
        body = {key: val for key, val in event.items() if key != "hash"}
        if body.get("previous") != previous or digest(body) != event.get("hash"):
            return False
        previous = event["hash"]
    return previous == trusted_head
