"""Compare the two controlled calculations for A19.02."""

import sys

if "--break" in sys.argv[1:]:
    result = (25, 10)
else:
    result = (16000 * 25 // 1000, 16000 * 10 // 1000)
print(repr(result))
