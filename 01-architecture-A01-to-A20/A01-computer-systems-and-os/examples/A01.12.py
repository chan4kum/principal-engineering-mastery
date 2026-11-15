"""Run with --break to select the controlled alternative."""

import sys as _sys
from pathlib import Path
from tempfile import TemporaryDirectory

broken = "--break" in _sys.argv[1:]

with TemporaryDirectory() as directory:
    config = Path(directory) / "config"
    if not broken:
        config.write_text("port=8000")
    try:
        print(config.read_text())
    except FileNotFoundError as error:
        print(f"startup errno={error.errno}")
