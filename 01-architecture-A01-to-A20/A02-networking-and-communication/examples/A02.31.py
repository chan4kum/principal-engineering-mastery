"""Local example for A02.31. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

balance, outcomes = 10, {}
for key, amount in (("k", 3), ("k", 3)):
    if broken or key not in outcomes:
        balance += amount
        outcomes[key] = (amount, balance)
    elif outcomes[key][0] != amount:
        raise ValueError("conflicting request")
print("final balance:", balance)
