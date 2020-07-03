import math as m
import numpy as np
import constant_module as cm

def erct(a,n):
    res=1
    for i in range (0,n,1):
       res*=a
    return res
 
print("Enter number and index")
print(erct(float(input()),int(input())), "\nHere it's it!")