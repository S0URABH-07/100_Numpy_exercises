import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()
print(data.shape[0])    
print(data.shape[1])

print(data[0])
print(data[-1])