"""Compare the two controlled calculations for M01.04."""

import sys

if "--break" in sys.argv[1:]:
    result = [x for x in range(1, 4) if x % 2 == 0]
else:
    result = [x for x in range(-3, 4) if x % 2 == 0]
print(repr(result))
