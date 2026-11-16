"""Compare the two controlled calculations for A15.15."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = ["T1", "T1", "T2", "T1"].count("T1")
print(repr(result))
