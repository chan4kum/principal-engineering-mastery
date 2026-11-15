"""Local example for A02.28. Run with --break for the failure control."""

import sys as _sys
from queue import Full, Queue

broken = "--break" in _sys.argv[1:]

pending = Queue(maxsize=0 if broken else 16)
for index in range(20):
    try:
        pending.put_nowait(index)
    except Full:
        break
print("application queue bytes:", pending.qsize() * 8192)
