"""Compare the two controlled calculations for A20.27."""

import sys

if "--break" in sys.argv[1:]:
    result = 0.002
else:
    result = 0.002 / 0.001
print(repr(result))
