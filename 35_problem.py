# Create a vector of size 10 with values ranging from 1 to 100, both excluded

import numpy as np

arr = np.linspace(1,100,12)[1:-1]
print(arr)

# linspace(start, stop, num) generates num equally spaced values between start and stop
# [1:-1] --> 1 start from the 2nd element and -1 stop before the last element