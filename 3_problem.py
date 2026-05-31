#How to find the memory size of any array

import numpy as np
arr = np.array([[[1,3],[4,5]],[[6,7],[8,9]]])
print("Memory Size", arr.nbytes)
# each value take 8 bytes to store in memory 