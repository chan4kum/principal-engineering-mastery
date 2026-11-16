"""Tenant-scoped read boundary and artifact admission evidence."""

from dataclasses import dataclass
from hashlib import sha256


@dataclass(frozen=True)
class Principal:
    tenant: str
    permissions: frozenset[str]


def retrieve(principal: Principal, scope: str, records: dict):
    if principal.tenant != scope or "read" not in principal.permissions:
        raise PermissionError("scope or grant missing")
    return tuple(records.get(scope, ()))


def verify_artifact(data: bytes, pinned_digest: str, sbom: dict, unresolved: set[str]) -> bool:
    """Check a pinned digest, minimal inventory shape and supplied scan evidence."""
    components = sbom.get("components")
    return (
        sha256(data).hexdigest() == pinned_digest
        and isinstance(components, list)
        and bool(components)
        and all(isinstance(x, str) and bool(x) for x in components)
        and not unresolved
    )
