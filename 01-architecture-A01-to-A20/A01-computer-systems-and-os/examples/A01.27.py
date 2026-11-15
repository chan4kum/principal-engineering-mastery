"""Run with --break to select the controlled alternative."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

waiting_for = {"A": "B", "B": "A"} if broken else {"B": "A"}
visited = set()
worker = "B"
while worker in waiting_for and worker not in visited:
    visited.add(worker)
    worker = waiting_for[worker]
print("cycle:", worker in visited)
