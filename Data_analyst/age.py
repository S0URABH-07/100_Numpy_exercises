import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()

age = data[:,0].astype(int)

print(np.max(age))
print(np.min(age))
print(np.mean(age))
print(np.median(age))