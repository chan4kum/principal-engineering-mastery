"""Compare the two controlled calculations for A19.23."""

import sys

if "--break" in sys.argv[1:]:
    result = 100 * 4
else:
    result = 5 * 4
print(repr(result))
