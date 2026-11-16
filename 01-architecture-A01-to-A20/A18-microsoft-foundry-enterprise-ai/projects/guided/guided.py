"""Framework-neutral Foundry routing and tenant-scoped retrieval model."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    region: str
    deployment: str
    healthy: bool


def route(candidates: list[Route], allowed_regions: set[str]) -> Route:
    for candidate in candidates:
        if candidate.healthy and candidate.region in allowed_regions:
            return candidate
    raise LookupError("no eligible route")


def search(tenant: str, scope: str, grants: dict[str, str], rows):
    if grants.get(tenant) != scope:
        raise PermissionError("unavailable index scope")
    eligible = [row for row in rows if row[0] == tenant and row[1] == scope]
    ranked = sorted(eligible, key=lambda row: (-row[2], row[3]))
    return tuple(row[3] for row in ranked)
