"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

program = [("ADD", 2), ("JUMP", 3), ("ADD", 9), ("HALT", 0)]
pc = register = 0
for _ in program:
    if not 0 <= pc < len(program):
        print("PC outside program")
        break
    opcode, arg = program[pc]
    print(pc, opcode, register)
    if opcode == "HALT":
        break
    if opcode == "ADD":
        register += arg
    pc = arg + int(broken) if opcode == "JUMP" else pc + 1
