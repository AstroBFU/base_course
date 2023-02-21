import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
t = np.arange(-5, 5, 0.03)

def diff_func(sis, t):
    y, x = sis
    dxdt = np.sin(x) + np.cos(x)
    dydt = x
    
    return dxdt, dydt

x0 = 0
y0 = 3
sis0 = x0, y0

sol = odeint(diff_func, sis0, t)

plt.plot(t, sol[:, 1])

plt.savefig('task_3.png')