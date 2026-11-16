"""Compare the two controlled calculations for A14.19."""

import sys

if "--break" in sys.argv[1:]:
    result = round((0.48 - 0.4) / 0.4, 2)
else:
    result = round(48 / 100 - 40 / 100, 2)
print(repr(result))
