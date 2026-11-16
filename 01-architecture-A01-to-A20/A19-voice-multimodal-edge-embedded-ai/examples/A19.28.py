"""Compare the two controlled calculations for A19.28."""

import sys

if "--break" in sys.argv[1:]:
    result = 4 / 100
else:
    result = (14 - 4) / 100
print(repr(result))
