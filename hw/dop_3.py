import matplotlib.pyplot as plt
import numpy as np
def fig_el(x,a,b):
    if x<a:
        y=a**2
    elif a<=x<=b:
        y=x**2
    else:
        y=b**2