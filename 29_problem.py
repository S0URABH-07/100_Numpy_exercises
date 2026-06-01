# How to get the dates of yesterday, today and tomorrow?

import numpy as np

today = np.datetime64('today')
yesterday = today - np.timedelta64(1, 'D')
tomorrow = today + np.timedelta64(1, 'D')

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)