"""Compare the two controlled calculations for A18.19."""

import sys

if "--break" in sys.argv[1:]:
    result = 8
else:
    result = 8 // 4
print(repr(result))
