import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()

attrition = data[:,1]

left = attrition == "Yes"

print(np.sum(left))

print(np.sum(~left))

print(np.mean(left) * 100)