import seaborn as sns
import pandas as pd
from scipy.stats import f_oneway
var = sns.load_dataset("titanic")
print(var)
print(var["pclass"].unique())

var = var[["age" , "pclass"]].dropna()

class_1 = var[var["pclass"] == 1]["age"]
class_2 = var[var["pclass"] == 2]["age"]
class_3 = var[var["pclass"] == 3]["age"]

f_stats ,p_value =f_oneway(class_1,class_2,class_3)
print(f_stats)
print(p_value)

# alpha = significant value
alpha = 0.05
if p_value<alpha:
    print("reject the null hypothesis and there is a significant diffrence in atleast one passenger class")
else:
    print("There is no significant diffrence")