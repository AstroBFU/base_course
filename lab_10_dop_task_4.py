import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
x = np.arange(-1, 1, 0.001)

def diff_func(sys, x):
    y, z = sys
    dydx = z
    dzdx = (4 * x ** 2  + 1 / 2) * y - z * x
    
    return dydx, dzdx

x0 = 0
y0 = 3
sys = x0, y0

sol = odeint(diff_func, sys, x)

plt.plot(x, sol[:, 1])

plt.savefig('dop_task_4.png')