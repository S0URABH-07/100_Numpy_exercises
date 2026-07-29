import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()
age = data[:,0].astype(int)
income = data[:,18].astype(int)
overtime = data[:,22]
attrition = data[:,1]

condition = ((age > 35) & (income > 12000) & (overtime == "Yes") & (attrition == "Yes"))

print(data[condition])