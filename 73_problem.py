# Considering a 10x3 matrix, extract rows with unequal values (e.g. [2,2,3]) 

import numpy as np
Z = np.random.randint(0, 5, (10, 3))
result = Z[np.any(Z != Z[:, [0]], axis=1)]
print("Original Matrix:\n", Z)
print("\nRows with unequal values:\n", result)