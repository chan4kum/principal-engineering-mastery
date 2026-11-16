"""Compare the two controlled calculations for A20.30."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = sum(v != 2 for v in [2, 1, 2])
print(repr(result))
