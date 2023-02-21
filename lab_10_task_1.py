import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
x = np.arange(-5, 5, 0.01)

def diff_func(sis, x):
    y, z = sis
    dydx = y**2 * z
    dzdx = z / x - y * z**2
   
    return dydx, dzdx

y0 = 1
z0 = -3
sis =  y0, z0

sol = odeint(diff_func, sis, x)

plt.plot(x, sol[:, 1])

plt.savefig('task_1.png')