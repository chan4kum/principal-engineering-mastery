"""Track customer-environment rollout, evidence and safe rollback."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Evidence:
    identity_verified: bool
    integration_tested: bool
    owner_present: bool
    good: int
    total: int

    def eligible(self) -> bool:
        return (
            self.identity_verified
            and self.integration_tested
            and self.owner_present
            and self.total > 0
            and 0 <= self.good <= self.total
            and 100 * self.good >= 99 * self.total
        )


class Delivery:
    def __init__(self, stable: str):
        self.active = self.stable = stable
        self.log = []

    def rollout(self, version: str, data: Evidence) -> bool:
        if not version or version == self.stable:
            raise ValueError("candidate version required")
        allowed = data.eligible()
        if allowed:
            self.active = version
        self.log.append(("promoted" if allowed else "held", version, data))
        return allowed

    def monitor(self, data: Evidence):
        if self.active != self.stable and not data.eligible():
            prior = self.active
            self.active = self.stable
            self.log.append(("restored", prior, data))
        return self.active
