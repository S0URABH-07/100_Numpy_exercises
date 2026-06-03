# Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors

import numpy as np
img = np.array([
    [[255,0,0], [255,0,0]],
    [[0,255,0], [0,0,255]]
], dtype=np.uint8)

colors = np.unique(img.reshape(-1,3), axis=0)

print(colors)
print(len(colors))