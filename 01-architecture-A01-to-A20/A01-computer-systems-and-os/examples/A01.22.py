"""Run with --break to select the controlled alternative."""

import sys as _sys
from collections import deque

broken = "--break" in _sys.argv[1:]

queue = deque([("A", 5), ("B", 3)])
clock = 0
while queue:
    job, left = queue.popleft()
    used = min(left, 8 if broken else 2)
    clock += used
    print(job, used, clock)
    if left > used:
        queue.append((job, left - used))
