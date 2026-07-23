import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()
income = data[:,18].astype(int)
attrition = data[:,1]

condition = (income > 15000) & (attrition=="Yes")

print(np.sum(condition))