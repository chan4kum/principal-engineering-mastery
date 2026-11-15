"""Linear and logistic fitting with analytic gradients and no model library."""

import numpy as np


def objective(design, outcome, coefficients, logistic: bool):
    prediction = design @ coefficients
    if logistic:
        loss = np.mean(np.logaddexp(0, prediction) - outcome * prediction)
        residual = np.exp(-np.logaddexp(0, -prediction)) - outcome
    else:
        residual = prediction - outcome
        loss = np.mean(residual**2) / 2
    return float(loss), design.T @ residual / len(outcome)


def fit(design, outcome, *, logistic=False, learning_rate=0.15, epochs=350):
    coefficients = np.zeros(design.shape[1], dtype=float)
    for _ in range(epochs):
        _, gradient = objective(design, outcome, coefficients, logistic)
        coefficients -= learning_rate * gradient
    return coefficients
