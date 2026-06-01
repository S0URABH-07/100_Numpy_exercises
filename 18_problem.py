# Create a 8x8 matrix and fill it with a checkerboard pattern

import numpy as np
arr = np.zeros((8, 8), dtype=int)

arr[1::2, ::2] = 1
arr[::2, 1::2] = 1
print(arr)

# ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛
# ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜
# ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛
# ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜
# ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛
# ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜
# ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛
# ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜