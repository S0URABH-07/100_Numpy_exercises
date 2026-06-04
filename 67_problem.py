# Compute a matrix rank

import numpy as np
A = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [1, 1, 1]
])
rank = np.linalg.matrix_rank(A)
print(rank)
# Rank--> NumPy checks how many rows/columns are independent.
# np.linalg.matrix_rank()--> This is the standard NumPy function for computing the rank of a matrix.