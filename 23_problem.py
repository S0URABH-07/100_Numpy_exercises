# Creating a color
import numpy as np

color = np.dtype([('R', np.uint8),('G', np.uint8),('B', np.uint8),('A', np.uint8)])

pixel = np.array((255, 128, 64, 200), dtype=color)
print(pixel)
print(type(pixel))