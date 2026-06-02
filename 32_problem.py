# Extract the integer part of a random array of positive numbers using 4 different methods

import numpy as np
arr = np.random.uniform(0,10,(10))
print("Original array: ",arr)

print("Method One: ",arr.astype(int))
# astype() --> Converts each float to an integer by removing the decimal part.

print("Method Two: ",np.trunc(arr))
# trunc() --> removes the fractional part and returns the integer part as floats.

print("Method Three: ",np.floor(arr))
# floor() --> Rounds down to the nearest integer.

print("Method four: ",arr - arr % 1)