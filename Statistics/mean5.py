# Measure of Central Tendency (Mean, Median, Mode)
import statistics

product_a = [20,22,21,19,23,20,21]
product_b = [15,16,35,18,17,16,15]

mean_a = statistics.mean(product_a)
median_a = statistics.median(product_a)

mean_b = statistics.mean(product_b)
median_b = statistics.median(product_b)

gap_a = abs(mean_a - median_a)
gap_b = abs(mean_b - median_b)

print("Product A -> Mean:", mean_a, "Median:", median_a)
print("Product B -> Mean:", mean_b, "Median:", median_b)

if gap_a > gap_b:
    print("Product A has the larger gap.")
else:
    print("Product B has the larger gap.")