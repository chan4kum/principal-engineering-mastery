"""Compare the two controlled calculations for A15.03."""

import sys

if "--break" in sys.argv[1:]:
    result = 4 / 4
else:
    result = len({"auth", "db", "log"}) / 4
print(repr(result))
