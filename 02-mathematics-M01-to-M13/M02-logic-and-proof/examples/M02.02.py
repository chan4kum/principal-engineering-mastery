"""Compare the two controlled calculations for M02.02."""

import sys

if "--break" in sys.argv[1:]:
    result = [2]
else:
    result = [x for x in [1, 2, 3, 4] if x % 2 == 0]
print(repr(result))
