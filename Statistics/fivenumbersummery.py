# Five Number summery 
import numpy as np
arr = np.array([2,3,4,5,6,7,8,9,11,12,16,17,19,22,27,31,34,201])
print(arr)

Q1 = np.percentile(arr,25)
print("Q1 : ",Q1)

Q3 = np.percentile(arr,75)
print("Q3 : ",Q3)

IQR = Q3 - Q1
print("IQR : ",IQR)

UF = Q3 + (1.5*IQR)
LF = Q1 - (1.5*IQR)
print("Upper Fence: ",UF)
print("Lower Fence :",LF)

l = []
for i in arr:
    if i<=UF and i>=LF:
        l.append(i)
arr2 = np.array(l)

print(arr)
print(arr2)