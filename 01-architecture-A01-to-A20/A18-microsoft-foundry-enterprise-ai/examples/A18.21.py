"""Compare the two controlled calculations for A18.21."""

import sys

if "--break" in sys.argv[1:]:
    result = 0
else:
    result = len({"primary", "backup", "telemetry"} - {"primary", "backup"})
print(repr(result))
