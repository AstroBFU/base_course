import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
t = np.arange(-1, 1, 0.001)

def diff_func(sys, t):
    y, z = sys
    dydt = z
    dzdt = np.sqrt(1 - z ** 2)

    return dydt, dzdt

y0 = 3 
z0 = 0
sys = y0, z0

sol = odeint(diff_func, sys, t)

plt.plot(t, sol[:, 1])

plt.savefig('dop_task_3.png')