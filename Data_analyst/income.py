import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()

income = data[:,18].astype(int)

print(np.max(income))
print(np.min(income))
print(np.mean(income))
print(np.std(income))
print(np.median(income))