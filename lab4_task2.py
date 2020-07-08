import math as m
import numpy as np

def mult(arr):
    res=1
    for i in range (0,len(arr),1):
        res *= arr[i]
    return int(res)

print("Enter array size")
sz = int(input())
mass = np.zeros((sz,1))
print("Enter array")
for i in range (0,sz,1):
    mass[i] = (int(input()))
print(mult(mass))
