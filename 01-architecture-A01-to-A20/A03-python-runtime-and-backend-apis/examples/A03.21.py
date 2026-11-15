"""Run normal or controlled failure for A03.21."""

import sys as _sys
from pydantic import BaseModel, ValidationError

broken = "--break" in _sys.argv[1:]


class Input(BaseModel):
    amount: int


try:
    print(Input.model_validate({"amount": "3"}, strict=not broken))
except ValidationError:
    print("strict rejection")
