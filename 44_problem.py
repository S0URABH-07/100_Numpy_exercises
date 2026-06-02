# Create random vector of size 10 and replace the maximum value by 0
import numpy as np

arr = np.random.randint(1,100,(10))

arr[arr == arr.max()] = 0
# arr.max()--> Return max value
# arr == arr.max() --> Cretes boolean mask like this [False False True False False]
# True = max value | False = Not Max
# arr[] = 0  Replace value arr == arr.max() to 0
print(arr)