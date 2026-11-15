"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]


def recursive_sum(n: int) -> int:
    return 0 if n == 0 else n + recursive_sum(n - 1)


try:
    print(recursive_sum(10_000 if broken else 2))
except RecursionError:
    print("iteration:", sum(range(1, 10_001)))
