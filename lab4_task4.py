import math as m
import numpy as np
import constant_module as cm

def func_x (mn, mx, cnt):
    arr = np.linspace(mn, mx, cnt)
    return arr*arr

print(func_x(float(input()), float(input()), int(input())))




