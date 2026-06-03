# How to convert a float (32 bits) array into an integer (32 bits) array in place?

import numpy as np
arr = np.array([1.5, 2.7, 3.9], dtype=np.float32)
print("Original arr: ",arr)
arr = arr.astype(np.int32)

print("Converted arr: ",arr)