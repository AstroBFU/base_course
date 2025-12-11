import numpy as np
from math import cos, tan, radians, sqrt
h = 100
a = radians(45)
b = radians(35)
g = 9.81
V = sqrt((g * h * np.tan(np.radians(35))**2/ (2 * np.cos(np.radians(45))**2 *( 1 - np.tan(np.radians(35)) * np.tan(np.radians(45))))))**0.5
print(V)

import numpy as np
T = 200
E = 300
k = 1.38 * 10**(-23)
e = 1.6 * 10**(-19)
h = 1.054 * 10**(-34)
N = (2 / np.sqrt(np.pi)) * np.sqrt(h *(k * 200)**3) * np.exp(-300 / (k * 200))
print(N)