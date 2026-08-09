import numpy as np
from scipy.stats import norm
sample = [172,174,168,169,171,173,175,170,169,172]
sample_mean = np.mean(sample)
sample_std = np.std(sample,ddof=1)
n = len(sample)
mean_population = 170

t_stats = (sample_mean - mean_population) / ( sample_std / np.sqrt(n))
print(t_stats)