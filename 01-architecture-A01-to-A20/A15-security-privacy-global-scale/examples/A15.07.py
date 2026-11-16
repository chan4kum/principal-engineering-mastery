"""Compare the two controlled calculations for A15.07."""

import sys

if "--break" in sys.argv[1:]:
    result = "reader" == "reader"
else:
    result = "reader" == "reader" and "team-a" == "team-b"
print(repr(result))
