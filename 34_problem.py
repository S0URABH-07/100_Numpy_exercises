# Consider a generator function that generates 10 integers and use it to build an array

import numpy as np

def generate():
    for i in range(10):
        yield i

# yield returns one value at a time
arr = np.fromiter(generate(), dtype=int)

# generate() --> creates the generator
# np.fromiter() --> reads values from the generator

print(arr)