# Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates

import numpy as np
arr = np.random.random((10, 2))

X = arr[:, 0]
Y = arr[:, 1]

R = np.sqrt(X**2 + Y**2)
T = np.arctan2(Y, X)

print("Cartesian Coordinates:")
print(arr)

print("\nRadius (r):")
print(R)

print("\nAngle (θ):")
print(T)