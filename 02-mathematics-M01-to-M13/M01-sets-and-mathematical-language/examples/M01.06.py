"""Compare the two controlled calculations for M01.06."""

import sys

if "--break" in sys.argv[1:]:
    result = len(list(zip(range(2), range(3))))
else:
    result = len([(a, b) for a in range(2) for b in range(3)])
print(repr(result))
