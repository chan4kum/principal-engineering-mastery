"""Compare the two controlled calculations for M02.01."""

import sys

if "--break" in sys.argv[1:]:
    result = 1 > 2
else:
    result = 3 > 2
print(repr(result))
