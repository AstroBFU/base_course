import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
x = np.arange(0, 10, 0.01)

def diff_func(z, x):
    y, omega = z
    dydx = omega
    dwdx = np.sin(y) * omega - 3*x*y - 5
   
    return dydx, dwdx

y0 = 0.01
omega0 = 0.05
z0 = y0, omega0
	
sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 1])

plt.savefig('omega.png')