"""Compare the two controlled calculations for A19.01."""

import sys

if "--break" in sys.argv[1:]:
    result = 16000
else:
    result = 16000 // 2
print(repr(result))
