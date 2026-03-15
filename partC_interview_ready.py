
import numpy as np

# Q2 Row normalize function
def row_normalize(arr: np.ndarray) -> np.ndarray:
    row_sums = arr.sum(axis=1, keepdims=True)
    normalized = np.divide(arr, row_sums, where=row_sums!=0)
    return normalized


# Example usage
arr = np.array([
    [1,2,3],
    [0,0,0],
    [2,2,2]
])

print(row_normalize(arr))


# Q3 Debug Fix
data = np.array([1, 2, 3, 4, 5])

mask = (data > 2) & (data < 5)

filtered = data[mask]

result = filtered.reshape(-1, 1)

print(result)
