"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

instruction = 0xF3 if broken else 0x13
opcode, immediate = divmod(instruction, 16)
print(2 + immediate if opcode == 1 else "unsupported opcode")
