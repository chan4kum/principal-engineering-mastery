"""Synthetic policy simulator for administrative requests."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Request:
    case_id: str
    purpose: str
    evidence_version: str
    requester: str


def triage(request: Request, allowed_purposes: set[str], sources: set[str]) -> str:
    if request.purpose not in allowed_purposes:
        return "denied"
    if request.evidence_version not in sources:
        return "needs evidence"
    return "needs review"
