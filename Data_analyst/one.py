import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()

attrition = data[:,1]

left = attrition == "Yes"

print(np.sum("Yes : ",left))

print(np.sum("No : ",~left))

print(np.mean("Mean: ",left) * 100)