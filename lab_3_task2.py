import lab_3_task1 as const
import numpy as np

h = 100
a = 45 / 180 * np.pi
b = 35 / 180 * np.pi
v = np.sqrt((const.g * h * np.tan(b)**2)/(2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))))
print(v)

T = 200 
E = 300
from lab_3_task1 import k
from lab_3_task1 import ht
N = (2 * ht * (const.e**( (-E) / (k * T))) * (E ** ( T/2 ))) / (np.sqrt(const.pi) * (k * T)**(3/2))
print(N)