
# AI-Augmented Task

## Prompt Used
Write a NumPy function that performs min-max normalization on a 2D array,
scaling each column to [0, 1] range.

## AI Output
```python
import numpy as np

def minmax_normalize(arr):
    min_vals = arr.min(axis=0)
    max_vals = arr.max(axis=0)
    return (arr - min_vals) / (max_vals - min_vals)
```

## Critical Evaluation
The function correctly performs column-wise min-max normalization using NumPy broadcasting.
However, it does not handle the edge case where all values in a column are the same,
which causes division by zero and produces NaN values.

A safer implementation would check for zero ranges and replace them with 1 to avoid errors.

The solution is fully vectorized and uses broadcasting correctly. However, to make it
production-ready, we should add:

range_vals = np.where(max_vals - min_vals == 0, 1, max_vals - min_vals)

Then divide by range_vals instead of (max_vals - min_vals).
