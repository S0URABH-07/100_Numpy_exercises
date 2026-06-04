# Extract all the contiguous 3x3 blocks from a random 10x10 matrix

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
arr = np.random.randint(0, 10, (10, 10))
print(arr)
blocks = sliding_window_view(arr, (3, 3))
print(blocks.shape)
#           O/P
# 8 possible row positions
# 8 possible column positions
# 3 rows inside each block
# 3 columns inside each block