"""Run with --break to select the controlled alternative."""

import sys as _sys
import os
from pathlib import Path
from tempfile import TemporaryDirectory

broken = "--break" in _sys.argv[1:]

with TemporaryDirectory() as directory:
    path = Path(directory) / "state"
    with path.open("wb") as stream:
        stream.write(b"OK")
        if not broken:
            stream.flush()
            os.fsync(stream.fileno())
        print(path.read_bytes())
