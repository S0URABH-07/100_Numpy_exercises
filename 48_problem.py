#  How to print all the values of an array?

import numpy as np
np.set_printoptions(threshold=np.inf) 
arr = np.arange(1000)
print(arr)
# np.inf = Means infinity 
# set_printoptions()--> Controls how NumPy displays arrays.
# threshold --> Maximum number of elements before NumPy starts shortening the output.
# threshold=np.inf --> Never truncate the array. Print all elements.