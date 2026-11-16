"""Compare the two controlled calculations for A14.07."""

import sys

if "--break" in sys.argv[1:]:
    result = int("correct" == "correct")
else:
    result = (int("s2" in ["s1"]), int("s2" in ["s1", "s2"]))
print(repr(result))
