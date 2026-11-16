"""Compare the two controlled calculations for A19.10."""

import sys

if "--break" in sys.argv[1:]:
    result = 5 - 3
else:
    result = (5 - 3) / 20
print(repr(result))
