"""Compare the two controlled calculations for A17.11."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = len({"primary", "vector"} - {"primary"})
print(repr(result))
