"""Compare the two controlled calculations for A17.09."""

import sys

if "--break" in sys.argv[1:]:
    result = bool("support")
else:
    result = "analytics" in {"support"}
print(repr(result))
