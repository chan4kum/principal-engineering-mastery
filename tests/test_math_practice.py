"""Exercise the M04–M13 lab controls and public project checker."""

import json
from pathlib import Path
from runpy import run_path

import pytest


TRACK = Path(__file__).resolve().parents[1] / "02-mathematics-M01-to-M13"
MODULES = tuple(f"M{number:02}" for number in range(4, 14))


@pytest.fixture(scope="module")
def verifier():
    pytest.importorskip("numpy")
    return run_path(str(TRACK / "verify.py"))


@pytest.mark.parametrize("module", MODULES)
@pytest.mark.parametrize("lab", ("L1", "L2", "L3", "L4"))
def test_lab_changes_and_restores(verifier, module, lab):
    check = verifier["verify_lab"]
    normal = check(module, lab)
    changed = check(module, lab, broken=True)
    assert normal.startswith(f"{module} {lab} normal control: ")
    assert changed.startswith(f"{module} {lab} failure control: ")
    assert normal.split(": ", 1)[1] != changed.split(": ", 1)[1]
    assert check(module, lab) == normal


@pytest.mark.parametrize("module", MODULES)
def test_public_project_checker_accepts_and_rejects(verifier, module, tmp_path):
    project = verifier["module_path"](module) / "projects" / "independent"
    cases = json.loads((project / "cases.json").read_text())
    assert len(cases) == 4
    assert len({entry["name"] for entry in cases}) == 4
    assert len({json.dumps(entry["input"], sort_keys=True) for entry in cases}) == 4
    assert any(entry["expected"] == {"status": "invalid"} for entry in cases)

    # A fixture echo exercises the checker without implementing the project.
    submission = tmp_path / "submission.py"
    submission.write_text(
        f"cases = {cases!r}\n\n"
        "def solve(case):\n"
        "    return next(row['expected'] for row in cases if row['input'] == case)\n"
    )
    check = verifier["verify_project"]
    assert check(module, submission) == f"{module}: 4 independent project cases passed"

    submission.write_text("def solve(case):\n    return {}\n")
    with pytest.raises(SystemExit, match=cases[0]["name"]):
        check(module, submission)
