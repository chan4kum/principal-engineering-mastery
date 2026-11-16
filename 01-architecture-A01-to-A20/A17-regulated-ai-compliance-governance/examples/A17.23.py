"""Compare the two controlled calculations for A17.23."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = len({"privacy", "lead", "ops"} - {"lead", "ops"})
print(repr(result))
