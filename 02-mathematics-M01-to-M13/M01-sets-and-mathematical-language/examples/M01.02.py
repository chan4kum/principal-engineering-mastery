"""Compare the two controlled calculations for M01.02."""

import sys

if "--break" in sys.argv[1:]:
    result = (-3) ** 2
else:
    result = -(3**2)
print(repr(result))
