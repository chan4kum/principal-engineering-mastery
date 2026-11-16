"""Compare the two controlled calculations for A16.04."""

import sys

if "--break" in sys.argv[1:]:
    result = 8640000 // 86400
else:
    result = 8640000 // 86400 * 4
print(repr(result))
