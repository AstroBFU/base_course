import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
t = np.arange(-1, 1, 0.001)

def diff_func(sys, t):
    x, y, z = sys
    dxdt = 3 * x - y + z
    dydt = x + y + z
    dzdt = 4 * x - y + 4 * z
   
    return dxdt, dydt, dzdt

x0 = -71
y0 = 1
z0 = -3
sys = x0, y0, z0

sol = odeint(diff_func, sys, t)

plt.plot(t, sol[:, 1])

plt.savefig('dop_task_1.png')