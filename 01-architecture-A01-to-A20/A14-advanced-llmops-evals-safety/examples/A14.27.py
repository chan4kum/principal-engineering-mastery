"""Compare the two controlled calculations for A14.27."""

import sys

if "--break" in sys.argv[1:]:
    result = round(300 / 0.05)
else:
    result = round(300 / (0.05 - 0.02))
print(repr(result))
