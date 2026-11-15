"""Local example for A02.30. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

idle_limit, deadline = 100, 250
arrivals = (80, 160, 240, 320)
last = 0
for now in arrivals:
    if not broken and now >= deadline:
        print("overall deadline at", deadline)
        break
    if now - last >= idle_limit:
        print("read inactivity expired")
        break
    last = now
else:
    print("body still active at", last)
