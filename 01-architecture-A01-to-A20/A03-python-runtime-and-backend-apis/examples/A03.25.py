"""Run normal or controlled failure for A03.25."""

import sys as _sys

broken = "--break" in _sys.argv[1:]

principal = {"tenant": "a", "authenticated": True}
resource = {"tenant": "b", "id": 8}
print(
    "allowed:", principal["authenticated"] and (broken or principal["tenant"] == resource["tenant"])
)
