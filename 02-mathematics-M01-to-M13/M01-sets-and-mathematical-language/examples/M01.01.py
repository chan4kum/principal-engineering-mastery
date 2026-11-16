"""Compare the two controlled calculations for M01.01."""

import sys

if "--break" in sys.argv[1:]:
    result = (3 // 2, 1)
else:
    result = (3 / 2, (1j) ** 2)
print(repr(result))
