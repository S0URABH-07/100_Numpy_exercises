# Create a 5x5 matrix with row values ranging from 0 to 4
import numpy as np

arr = np.arange(5)
print(arr)

arr1 = np.tile(arr ,(5,1))
print("5x5 metrix:\n",arr1)