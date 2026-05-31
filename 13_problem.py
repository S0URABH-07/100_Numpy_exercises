# Create a 2d array with 1 on the border and 0 inside

import numpy as np
arr = np.zeros((5, 5), dtype=int)

arr[0, :] = 1      # Top row
arr[-1, :] = 1     # Bottom row
arr[:, 0] = 1      # Left column
arr[:, -1] = 1     # Right column

print(arr)