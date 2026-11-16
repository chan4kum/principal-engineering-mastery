"""Compare the two controlled calculations for A20.28."""

import sys

if "--break" in sys.argv[1:]:
    result = 2
else:
    result = sum(x <= 8 for x in [7, 11])
print(repr(result))
