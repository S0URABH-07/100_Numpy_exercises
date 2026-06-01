# Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
import numpy as np

index = np.unravel_index(99, (6, 7, 8))
print(index)

# We use np.unravel_index() because it converts a flat (1D) index into the corresponding 
# multi-dimensional index of an array.