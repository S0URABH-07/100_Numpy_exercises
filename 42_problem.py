# Make an array immutable (read-only)
import numpy as np

Z = np.array([1, 2, 3, 4, 5])
Z.flags.writeable = False # Make the array read only 

print(Z)