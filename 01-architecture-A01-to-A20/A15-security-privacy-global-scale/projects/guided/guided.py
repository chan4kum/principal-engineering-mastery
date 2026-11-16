"""Threat-review evidence and bounded credential rotation for fixture secrets."""

from secrets import compare_digest


def uncovered(flows: set[str], controls: dict[str, str]) -> set[str]:
    return {flow for flow in flows if not controls.get(flow, "").strip()}


class CredentialVersions:
    def __init__(self, version: int, credential: str):
        self._current = (version, credential)
        self._previous = None

    def stage(self, version: int, credential: str) -> None:
        if version <= self._current[0] or not credential:
            raise ValueError("rotation needs a newer non-empty credential")
        self._previous, self._current = self._current, (version, credential)

    def retire_previous(self) -> None:
        self._previous = None

    def accepts(self, version: int, credential: str) -> bool:
        return any(
            item is not None
            and item[0] == version
            and compare_digest(item[1].encode(), credential.encode())
            for item in (self._current, self._previous)
        )
