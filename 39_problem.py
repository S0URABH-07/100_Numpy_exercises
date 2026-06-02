# Create array with negetive sign value than remove the sign and than sort and then Unique sorted array print

import numpy as np
arr = np.array([1,-2,4,5,7,97,3,-22,-11,5,9])
print("Original array: ",arr)

arr1 = np.abs(arr)
print("Sign Remove: ",arr1)

arr2 = np.sort(arr1)
print("Sort Array: ",arr2)

arr3 = np.unique(arr2)
print("Unique sorted array: ",arr3)