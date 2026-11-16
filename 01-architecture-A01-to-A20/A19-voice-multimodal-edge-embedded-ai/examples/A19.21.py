"""Compare the two controlled calculations for A19.21."""

import sys

if "--break" in sys.argv[1:]:
    result = 4 * 30
else:
    result = 2 * 30
print(repr(result))
