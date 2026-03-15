
import numpy as np
import time

N = 1_000_000

# Legacy RNG
start = time.time()
np.random.seed(42)
legacy_samples = np.random.normal(0, 1, N)
legacy_time = time.time() - start

# New Generator API
start = time.time()
rng = np.random.default_rng(42)
new_samples = rng.normal(0, 1, N)
new_time = time.time() - start

print("Legacy RNG time:", legacy_time)
print("New Generator time:", new_time)


def generate_regression_data():
    rng = np.random.default_rng(42)

    X = rng.normal(0, 1, size=(100, 3))
    w = np.array([2.5, -1.3, 0.7])
    noise = rng.normal(0, 0.5, size=100)

    y = X @ w + noise

    return X, y, w


X, y, w = generate_regression_data()

print("X shape:", X.shape)
print("y shape:", y.shape)
print("True weights:", w)

explanation = '''
np.random.Generator is the modern random number API introduced in NumPy 1.17.

It separates the random number algorithm (BitGenerator) from the user interface (Generator).
Unlike the legacy np.random module that uses a global random state, Generator allows multiple
independent random streams.

This improves reproducibility, parallel computation, and simulation reliability.
'''

print(explanation)
