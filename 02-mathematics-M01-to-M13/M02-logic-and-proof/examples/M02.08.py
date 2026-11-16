"""Compare the two controlled calculations for M02.08."""

import sys

if "--break" in sys.argv[1:]:
    result = 4 * 3 // 2
else:
    result = 4 * 5 // 2
print(repr(result))
