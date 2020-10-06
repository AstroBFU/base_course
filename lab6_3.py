# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:07:14 2020

@author: student
"""

import matplotlib.pyplot as plt
import numpy as np
a = int(input())
b = int(input())
x = np.arange(0,10,0.1)
y = np.zeros(len(x))

for i in range(len(x)):
    if x[i]<a:
        y[i] = a**2
    
    if a<=x[i]<=b:
        y[i] = x[i]**2
        
    if x[i]>b:
        y[i] = b**2
        
plt.plot(x,y)
plt.show()
