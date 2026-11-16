"""Compare the two controlled calculations for A15.20."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = len({"service", "research"} - {"service"})
print(repr(result))
