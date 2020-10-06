# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

import matplotlib.pyplot as plt
import numpy as np

b = 4
a = 1
A = 1
B = 7
q = np.pi/2
t = np.arange(0,10*np.pi,0.01)
x = A *np.sin(a*t+q)
y = B * np.sin(b*t)
plt.plot(x,y)
plt.show()

