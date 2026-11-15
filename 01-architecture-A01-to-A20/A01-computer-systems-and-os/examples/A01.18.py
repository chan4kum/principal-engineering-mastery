"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]


def translate(address: int, table: dict[int, int], size: int = 4096) -> int:
    page, offset = divmod(address, size)
    return table[page] * size + offset


try:
    print(translate(8199, {} if broken else {2: 11}))
except KeyError as error:
    print("unmapped page:", error.args[0])
