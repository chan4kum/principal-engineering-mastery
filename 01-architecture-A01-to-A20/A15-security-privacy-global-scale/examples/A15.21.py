"""Compare the two controlled calculations for A15.21."""

import sys

if "--break" in sys.argv[1:]:
    result = (18 <= 10, 5 <= 15)
else:
    result = (5 <= 10, 18 <= 15)
print(repr(result))
