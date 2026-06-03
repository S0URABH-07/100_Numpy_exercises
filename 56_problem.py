# How to sort an array by the nth column?

import numpy as np
Z = np.array([
    [1, 4, 3],
    [3, 1, 2],
    [2, 5, 1]
])

n = 1 # Sort by the 2nd column
# O/P depends only 2nd column. Short the array according to 2nd column
print(Z)
Z = Z[Z[:, n].argsort()]

print(Z)