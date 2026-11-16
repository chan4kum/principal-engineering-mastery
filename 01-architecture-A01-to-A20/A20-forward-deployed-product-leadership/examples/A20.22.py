"""Compare the two controlled calculations for A20.22."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = sum(x <= 3 for x in [2, 5])
print(repr(result))
