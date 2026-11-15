"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]


def headroom(limits_and_usage: list[tuple[int, int]]) -> int:
    return max(0, min(limit - usage for limit, usage in limits_and_usage))


scopes = [(8192, 1024)]
if not broken:
    scopes.append((256, 96))
print(headroom(scopes), "MiB headroom in model")
