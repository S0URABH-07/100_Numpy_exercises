# Variance & Standard Deviation
import statistics

product_A = [100,102,101,99,98]
product_B = [80,100,120,90,110]
product_C = [50,150,60,170,90]

std_A = statistics.stdev(product_A)
std_B = statistics.stdev(product_B)
std_C = statistics.stdev(product_C)

print("Product A SD:", round(std_A,2))
print("Product B SD:", round(std_B,2))
print("Product C SD:", round(std_C,2))

smallest = min(std_A, std_B, std_C)

if smallest == std_A:
    print("Product A is the most consistent.")
elif smallest == std_B:
    print("Product B is the most consistent.")
else:
    print("Product C is the most consistent.")