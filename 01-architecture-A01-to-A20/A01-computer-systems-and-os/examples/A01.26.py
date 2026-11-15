"""Run with --break to select the controlled alternative."""

import sys as _sys
from threading import BoundedSemaphore

broken = "--break" in _sys.argv[1:]

capacity = BoundedSemaphore(3)
for index in range(4):
    acquired = capacity.acquire(blocking=False)
    print(index, acquired)
    if acquired and not broken:
        capacity.release()
