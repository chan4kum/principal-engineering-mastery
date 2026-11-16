"""Compare the two controlled calculations for A19.07."""

import sys

if "--break" in sys.argv[1:]:
    result = min(8, 15)
else:
    result = min(8 + 6 + 6, 15)
print(repr(result))
