import math as m
import numpy as np
import constant_module as cm

def avrg(arr):
    s=0
    for i in range (0,len(arr),1):
        s+=arr[i]
    return float(s/len(arr))

print("Enter array size")
sz = int(input())
mass = np.zeros((sz,1))
print("Enter array")
for i in range (0,sz,1):
    mass[i] = (int(input()))
print(avrg(mass))

