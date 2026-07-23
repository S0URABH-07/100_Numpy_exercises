import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()
income = data[:,18].astype(int)

print(np.percentile(income,25))
print(np.percentile(income,50))
print(np.percentile(income,75))