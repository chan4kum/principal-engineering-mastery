"""Compare the two controlled calculations for A14.06."""

import sys

if "--break" in sys.argv[1:]:
    result = len({"g1", "g2"} & {"g1"})
else:
    result = len({"g1"} & {"g2"})
print(repr(result))
