"""Compare the two controlled calculations for A14.22."""

import sys

if "--break" in sys.argv[1:]:
    result = round(0.9 - 0.9, 2)
else:
    result = round(60 / 100 - 80 / 100, 2)
print(repr(result))
