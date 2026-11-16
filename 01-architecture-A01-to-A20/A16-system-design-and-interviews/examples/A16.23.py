"""Compare the two controlled calculations for A16.23."""

import sys

if "--break" in sys.argv[1:]:
    result = 240 * 4
else:
    result = 240 * 4 // 8
print(repr(result))
