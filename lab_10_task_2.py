import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
t = np.arange(-1, 1, 0.003)

def diff_func(b, t):
    y, x = b
    dxdt = 3 * x - 2 * y + np.e **(3 * t) / (np.e ** t + 1)
    dydt = x - np.e ** 3 * t / (np.e ** t + 1)
   
    return dxdt, dydt

x0 = 5
y0 = -7
b = x0, y0

sol = odeint(diff_func, b, t)

plt.plot(t, sol[:, 1])

plt.savefig('task_2.png')