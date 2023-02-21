import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
t = np.arange(-5, 5, 0.03)

def diff_func(sis, t):
    y, x = sis
    dxdt = 4 * x + 5 * y
    dydt = x
    
    return dxdt, dydt

x0 = -1
y0 = 4
sis0 = x0, y0

sol = odeint(diff_func, sis0, t)

plt.plot(t, sol[:, 0])

plt.savefig('task_4.png')