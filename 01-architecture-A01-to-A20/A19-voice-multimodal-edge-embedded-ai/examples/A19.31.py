"""Compare the two controlled calculations for A19.31."""

import sys

if "--break" in sys.argv[1:]:
    result = True
else:
    result = 150 <= 100
print(repr(result))
