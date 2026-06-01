# Normalize a 5x5 random matrix (Array)

import numpy as np
arr = np.random.random((5, 5))

# Normalize formula
normalized_arr = (arr - arr.min()) / (arr.max() - arr.min())

print("Original Array :\n", arr)
print("\nNormalized Array :\n", normalized_arr)