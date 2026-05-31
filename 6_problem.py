#Reverse a vector (first element becomes last)

import numpy as np
arr2 = np.array([1,2,3,4,5,6,7,8,9])
print(arr2[::-1]) #using indexing
print(np.flip(arr2)) #using flip function 