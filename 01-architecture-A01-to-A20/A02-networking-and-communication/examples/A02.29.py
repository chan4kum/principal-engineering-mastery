"""Local example for A02.29. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

elapsed, deadline, backoff, minimum_attempt = 150, 200, 30, 40
remaining_after_backoff = deadline - elapsed - backoff
print(
    "retry admitted:",
    (deadline - elapsed if broken else remaining_after_backoff) >= minimum_attempt,
)
