"""Compare the two controlled calculations for A19.05."""

import sys

if "--break" in sys.argv[1:]:
    result = max([120, 180, 40])
else:
    result = 120 + 180 + 40
print(repr(result))
