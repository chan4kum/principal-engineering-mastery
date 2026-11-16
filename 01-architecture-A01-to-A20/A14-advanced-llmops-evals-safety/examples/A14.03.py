"""Compare the two controlled calculations for A14.03."""

import sys

if "--break" in sys.argv[1:]:
    result = 0.5 * 0.9 + 0.5 * 0.5
else:
    result = 0.75 * 0.9 + 0.25 * 0.5
print(repr(result))
