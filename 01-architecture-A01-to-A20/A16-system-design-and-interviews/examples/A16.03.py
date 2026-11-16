"""Compare the two controlled calculations for A16.03."""

import sys

if "--break" in sys.argv[1:]:
    result = 4
else:
    result = len({"create", "resolve"})
print(repr(result))
