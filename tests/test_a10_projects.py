"""Validate both analytical gradients and the model's data boundary."""

import importlib.util
import os
from pathlib import Path

import pytest

PHASE = (
    Path(__file__).resolve().parents[1]
    / "01-architecture-A01-to-A20/A10-ml-foundations-math-and-mlops"
)


def module(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec is not None and spec.loader is not None
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


@pytest.mark.parametrize("logistic", [False, True])
def test_guided_finite_differences_and_fit(logistic):
    np = pytest.importorskip("numpy")
    implementation = module(PHASE / "projects/guided/regression.py")
    design = np.column_stack([np.ones(4), [-2, -1, 1, 2]])
    outcome = np.array([0, 0, 1, 1] if logistic else [-3, -1, 3, 5])
    initial = np.zeros(2)
    start, analytic = implementation.objective(design, outcome, initial, logistic)
    eps = 1e-5
    for dimension, displacement in enumerate(np.eye(2) * eps):
        plus = implementation.objective(
            design, outcome, initial + displacement, logistic
        )[0]
        minus = implementation.objective(
            design, outcome, initial - displacement, logistic
        )[0]
        # Subtraction and division by eps amplify float64 roundoff near zero.
        assert analytic[dimension] == pytest.approx((plus - minus) / (2 * eps), abs=1e-9)
    trained = implementation.fit(design, outcome, logistic=logistic)
    assert implementation.objective(design, outcome, trained, logistic)[0] < start / 3


def test_pipeline_holdout_invariance(tmp_path):
    np = pytest.importorskip("numpy")
    selected = Path(
        os.getenv("A10_PIPELINE", str(PHASE / "projects/independent/pipeline.py"))
    )
    implementation = module(selected)
    first, second = tmp_path / "first.json", tmp_path / "second.json"
    initial = [[1, 3], [2, 5], [3, 7]]
    receipt = implementation.train([*initial, [8, 22]], 3, first)
    implementation.train([*initial, [500, 37]], 3, second)
    assert receipt["mean"] == 2
    assert first.read_bytes() == second.read_bytes()
    np.testing.assert_allclose(implementation.predict(first, [4, 5]), [9, 11])
    with pytest.raises(ValueError):
        implementation.predict(first, [float("nan")])
