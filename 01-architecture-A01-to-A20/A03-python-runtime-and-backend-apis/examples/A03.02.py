"""Run normal or controlled failure for A03.02."""

import sys as _sys
import dis

broken = "--break" in _sys.argv[1:]

instructions = list(dis.get_instructions(compile("x + 1", "<fixture>", "eval")))
print("native count inferred" if broken else "CPython instructions inspected", bool(instructions))
