import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
x = np.arange (0, 5, 0.5)

def diff_func(sys, x):
    z, y = sys
    dydx = z
    dzdx = z ** 2 / y - 3 * y / np.sqrt(x)

    return dydx, dzdx

z0 = 0
y0 = 1
sys = z0, y0

sol = odeint(diff_func, sys, x)

plt.plot(x, sol[:, 1])

plt.savefig('dop_task_2.png')
