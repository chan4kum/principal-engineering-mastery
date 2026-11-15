"""CPU-only ML labs with synthetic, deterministic observations."""

import argparse
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "projects/guided"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "projects/independent"))
from pipeline import predict, train
from regression import objective


def loss_check(broken: bool) -> tuple[float, float]:
    x = np.array([[1.0], [2.0]])
    y = np.array([2.0, 4.0])
    state = np.array([0.0])
    start, grad = objective(x, y, state, False)
    expected_derivative = -5.0
    assert np.isclose(grad[0], expected_derivative)
    step = 0.1 * grad * (-1 if broken else 1)
    end, _ = objective(x, y, state - step, False)
    return start, end


def leakage() -> dict[str, float]:
    epochs = np.arange(100)
    labels = np.where(epochs < 80, epochs % 2, 1 - epochs % 2)
    random = np.random.default_rng(42).permutation(len(epochs))
    temporal_train, temporal_test = epochs[:80], epochs[80:]

    def accuracy(indices, validation, feature):
        design = np.column_stack([np.ones(len(indices)), feature[indices]])
        coef = np.linalg.lstsq(design, labels[indices], rcond=None)[0]
        prediction = coef[0] + feature[validation] * coef[1] >= 0.5
        return float(np.mean(prediction == labels[validation]))

    return {
        "random_score": accuracy(random[:80], random[80:], epochs % 2),
        "future_score": accuracy(temporal_train, temporal_test, epochs % 2),
        "leaked_future_score": accuracy(temporal_train, temporal_test, labels),
    }


def evaluation(broken: bool) -> dict[str, float | int]:
    truth = np.array([0, 0, 1, 1] if not broken else [0] * 18 + [1, 1])
    score = np.array([0.1, 0.6, 0.7, 0.4] if not broken else [0.1] * 20)
    positive = score >= 0.5
    tp = np.count_nonzero(positive & (truth == 1))
    fp = np.count_nonzero(positive & (truth == 0))
    tn = np.count_nonzero(~positive & (truth == 0))
    fn = np.count_nonzero(~positive & (truth == 1))
    return {
        "tp": int(tp),
        "fp": int(fp),
        "tn": int(tn),
        "fn": int(fn),
        "accuracy": float(np.mean(positive == truth)),
        "precision": float(tp / (tp + fp)) if tp + fp else 0.0,
        "recall": float(tp / (tp + fn)),
        "brier": float(np.mean((score - truth) ** 2)),
        "mean_probability": float(score.mean()),
        "observed_positive_rate": float(truth.mean()),
        "pr_curve": [
            {
                "threshold": float(threshold),
                "precision": float(truth[score >= threshold].mean()),
                "recall": float(truth[score >= threshold].sum() / truth.sum()),
            }
            for threshold in sorted(set(score), reverse=True)
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("lab", choices=["L1", "L2", "L3", "L4"])
    parser.add_argument("--break", dest="broken", action="store_true")
    args = parser.parse_args()
    if args.lab == "L1":
        print("loss before and after:", loss_check(args.broken))
    elif args.lab == "L2":
        print(leakage())
    elif args.lab == "L3":
        print(evaluation(args.broken))
    else:
        with TemporaryDirectory() as scratch:
            artifact = Path(scratch) / "model.json"
            model = train(
                [[1, 3], [2, 5], [3, 7], [20, 41], [40, 81]],
                3,
                artifact,
                broken=args.broken,
            )
            print("preprocessing mean:", model["mean"])
            print("reopened artifact predictions:", predict(artifact, [4, 5]))
