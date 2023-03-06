import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
z = np.arange (0, 5, 0.01)

def diff_func(sys, z):
    x, y = sys
    z = ((d * y) / (d * x)) ** 2
    z = z - (3 * y ** 2) / np.sqrt(x)
    
    return z

x0 = 0
y0 = 1
sys = x0, y0

sol = odeint(diff_func, sys, z)

plt.plot(z, sol[:, 1])

plt.savefig('dop_task_2.png')
