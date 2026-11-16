"""Compare the two controlled calculations for A18.12."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = sum(h <= 4 for h in [2, 6])
print(repr(result))
