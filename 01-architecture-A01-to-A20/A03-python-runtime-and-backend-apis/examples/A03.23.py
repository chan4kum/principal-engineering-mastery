"""Run normal or controlled failure for A03.23."""

import sys as _sys
from fastapi import FastAPI

broken = "--break" in _sys.argv[1:]

app = FastAPI()


@app.get("/current" if not broken else "/new-path")
def resource():
    return {"ready": True}


print("contract path exists:", "/current" in app.openapi()["paths"])
