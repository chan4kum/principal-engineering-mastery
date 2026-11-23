# M13 · Information theory and deep learning

**7 topics** · [Mathematics index](../README.md)

## Guided walkthrough

Connect probabilities, losses, and gradients, then test whether a training improvement carries over to unseen data.

1. **M13.01 · entropy/cross entropy/KL.** With base-2 logs, H(p)=−Σp log₂p and H(p,q)=−Σp log₂q. Their difference is KL divergence D(p‖q). If p=(1,0) and q=(1/2,1/2), the three values are 0, 1, and 1 bit. A zero q where p is positive makes cross entropy infinite.
2. **M13.02 · softmax and logsumexp.** Softmax exponentiates logits and divides each exponential by the sum of exponentials. Subtract the largest logit before exponentiating. The same shift yields stable logsumexp m+log(Σ exp(zᵢ−m)). For logits (1000,1000), softmax is (0.5,0.5) and logsumexp is 1000+log 2.
3. **M13.03 · backprop.** Backpropagation applies the chain rule from the loss back to each parameter. With y=wx, target 1, and L=(y−1)²/2, the gradient is (wx−1)x. At w=2 and x=3 it equals 15.
4. **M13.04 · normalization.** Normalization specifies which axes supply the mean and variance. Layer normalization over a feature vector uses that vector’s features. For (1,3), the mean is 2 and population variance is 1, giving (−1,1) before the stabilizing epsilon and learned affine transform.
5. **M13.05 · optimizers.** Optimizers convert gradients into updates. Plain SGD with gradient 4 and learning rate 0.1 subtracts 0.4. Momentum and adaptive methods maintain additional state, so their update also depends on previous steps.
6. **M13.06 · learning rates.** The learning rate scales the update. For L(w)=w²/2, gradient descent gives w_new=(1−η)w. With η=0.5 the magnitude halves each step. With η=2.5 it grows by 1.5 while changing sign.
7. **M13.07 · generalization.** Generalization concerns performance on unseen inputs drawn from the population of interest. Training accuracy of 99% and held-out accuracy of 80% give a 19-point gap. Check distribution differences and data leakage before assigning a cause.

### Put it together

For logits (1000,1000) and target class 0, the stable softmax loss is log 2 in natural units. The gradient with respect to the logits is (−0.5,0.5). Verify it by perturbing one logit at a time and comparing the measured change in loss with the gradient.

### Verify with NumPy

Run this block with NumPy after working the example by hand.

```python
import numpy as np

def loss(values):
    shifted = values - values.max()
    return np.log(np.exp(shifted).sum()) - shifted[0]

logits = np.array([1000.0, 1000.0])
np.testing.assert_allclose(loss(logits), np.log(2))
delta = 1e-3 * np.eye(2)
numerical = [(loss(logits + d) - loss(logits - d)) / 2e-3 for d in delta]
np.testing.assert_allclose(numerical, [-0.5, 0.5], atol=1e-10)
```

[Previous · M12 Statistical inference](../M12-statistical-inference/README.md)
