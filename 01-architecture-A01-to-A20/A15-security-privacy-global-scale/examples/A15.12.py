"""Compare the two controlled calculations for A15.12."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = sum(x == "deny" for x in ["allow", "deny", "deny"])
print(repr(result))
