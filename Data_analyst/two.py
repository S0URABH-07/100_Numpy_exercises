import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()
overtime = data[:,22]
attrition = data[:,1]

condition = (overtime=="Yes") & (attrition=="Yes")

print(np.sum(condition))