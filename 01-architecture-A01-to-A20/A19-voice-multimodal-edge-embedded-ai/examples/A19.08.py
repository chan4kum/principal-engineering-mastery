"""Compare the two controlled calculations for A19.08."""

import sys

if "--break" in sys.argv[1:]:
    result = 48 <= 96
else:
    result = 48 + 24 + 32 <= 96
print(repr(result))
