"""Local example for A02.33. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

arrivals_per_sec, lifetime = 500, 60
port_budget = 20_000
retained = 0 if broken else arrivals_per_sec * lifetime
print("model exhausted:", retained > port_budget, "retained:", retained)
