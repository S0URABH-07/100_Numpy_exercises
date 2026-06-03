# How to find the closest value (to a given scalar) in a vector?

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
value = 33

distance = arr - value 
sign_rmv = np.abs(distance)
closet_value = arr[sign_rmv.argmin()]

print(closet_value)

# arr - value --> distance from the target
# np.abs() --> Remove the sign of array values
# argmin() --> index of the smallest distance.