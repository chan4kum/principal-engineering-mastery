"""Scoped usage attribution and admission for a synthetic SaaS service."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Usage:
    tenant: str
    input_tokens: int
    output_tokens: int


class Meter:
    def __init__(self, tenant_limits: dict[str, int], shared_limit: int):
        self.tenant_limits = dict(tenant_limits)
        self.shared_limit = shared_limit
        self.requests = {}

    def charge(self, principal: str, request_id: str, usage: Usage) -> int:
        if principal != usage.tenant or principal not in self.tenant_limits:
            raise PermissionError("tenant scope denied")
        if min(usage.input_tokens, usage.output_tokens) < 0 or not request_id:
            raise ValueError("invalid usage")
        key = (principal, request_id)
        units = usage.input_tokens + 3 * usage.output_tokens
        prior = self.requests.get(key)
        if prior:
            if prior != (usage, units):
                raise ValueError("usage identity conflict")
            return prior[1]
        tenant_total = sum(
            amount for item, amount in self.requests.values() if item.tenant == principal
        )
        service_total = sum(amount for _, amount in self.requests.values())
        if (
            tenant_total + units > self.tenant_limits[principal]
            or service_total + units > self.shared_limit
        ):
            raise OverflowError("quota exhausted")
        self.requests[key] = (usage, units)
        return units

    def total(self, tenant: str):
        return sum(units for item, units in self.requests.values() if item.tenant == tenant)
