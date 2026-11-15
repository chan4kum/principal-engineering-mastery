"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]


def next_pc(current: int, target: int | None, width: int) -> int:
    address = current + width if target is None else target
    if address % width:
        raise ValueError("misaligned target in toy ISA")
    return address


try:
    print(next_pc(8, 5 if broken else 20, 4))
except ValueError as error:
    print(error)
