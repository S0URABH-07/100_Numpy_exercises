# Create a custom dtype that describes a color as four unsigned bytes (RGBA)
import numpy as np

color = np.dtype([('R', np.uint8),('G', np.uint8),('B', np.uint8),('A', np.uint8)])

print(color)