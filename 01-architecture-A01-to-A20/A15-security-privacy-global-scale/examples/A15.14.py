"""Compare the two controlled calculations for A15.14."""

import sys

if "--break" in sys.argv[1:]:
    result = len({"allow"})
else:
    result = len({"allow", "deny"})
print(repr(result))
