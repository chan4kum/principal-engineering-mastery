"""Compare the two controlled calculations for A14.15."""

import sys

if "--break" in sys.argv[1:]:
    result = sum([2, 3, 5]) <= 10
else:
    result = sum([2, 3, 5]) <= 10 and max([10, 40, 70]) <= 50
print(repr(result))
