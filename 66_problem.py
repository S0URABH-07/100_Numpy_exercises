# How to compute averages using a sliding window over an array?

import numpy as np

arr = np.arange(10)
print(arr)
window = 3

result = np.convolve(arr, np.ones(window)/window, mode='valid')
print(result)