import math as m
import numpy as np

def fib(n):
    a=0
    b=1
    if n>=0:
        for i in range (1, n, 1):
            temp = b
            b += a
            a = temp
        return (a)
    else:
        for i in range (1, abs(n), 1):
            temp = b
            b = a-b
            a = temp
        return (a)     

print(fib(int(input())), "\nHere it's it!")
