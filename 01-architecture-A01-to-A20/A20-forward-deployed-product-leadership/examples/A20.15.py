"""Compare the two controlled calculations for A20.15."""

import sys

if "--break" in sys.argv[1:]:
    result = 40
else:
    result = sum([40, 10, 30])
print(repr(result))
