import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()
experience = data[:,28].astype(int)

print(experience[experience > 10])

print(np.sum(experience > 10))