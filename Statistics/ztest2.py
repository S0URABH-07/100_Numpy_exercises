import numpy as np
from scipy.stats import norm
sample = [172,174,168,169,171,173,175,170,169,172]
population_mean = 170
population_std = 3
sample_mean = np.mean(sample)
n = len(sample)

z_score = (sample_mean - population_mean) / (population_std / np.sqrt(n))
print(z_score)

#  cdf = cumulative distribution function 
p_value = 2 * (1 - norm.cdf(abs(z_score)))
print(p_value)

# alpha = significant value
# Direct compare p value to the significant value
alpha = 0.05
if p_value < alpha:
    print("I will reject the null hypothesis")
else:
    print("I will accept the null hupothesis")