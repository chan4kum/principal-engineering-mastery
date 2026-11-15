"""Observe a short-lived child before and after explicit termination."""

import argparse
import os
from pathlib import Path
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--break", dest="terminate", action="store_true")
args = parser.parse_args()
program = "import time; time.sleep(0.25)"
with subprocess.Popen([sys.executable, "-c", program]) as child:
    print(f"parent={os.getpid()} child={child.pid}")
    status = Path(f"/proc/{child.pid}/status")
    if status.is_file():
        for line in status.read_text().splitlines():
            if line.startswith(("Name:", "State:", "Pid:", "PPid:")):
                print(line)
    else:
        print("Linux /proc unavailable")
    if args.terminate:
        child.terminate()
    print("child returncode:", child.wait(timeout=3))
