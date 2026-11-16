"""Compare the two controlled calculations for A18.22."""

import sys

if "--break" in sys.argv[1:]:
    result = (20, 20)
else:
    result = (40 // 4, 40 * 3 // 4)
print(repr(result))
