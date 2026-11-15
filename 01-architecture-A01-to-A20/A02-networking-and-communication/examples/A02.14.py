"""Local example for A02.14. Run with --break for the failure control."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

expected = 100
for start, end in [(100, 105), (110, 115)]:
    if broken or start == expected:
        expected = end
print("next expected:", expected)
