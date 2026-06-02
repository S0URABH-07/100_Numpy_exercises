# Print the minimum and maximum representable values for each numpy scalar type

import numpy as np
for dtype in [np.int8, np.int16, np.int32, np.int64]:
    print(dtype)
    print("Min:", np.iinfo(dtype).min) 
    print("Max:", np.iinfo(dtype).max)
    print()
    #iinfo()-->means integer information.It returns details about the integer type.