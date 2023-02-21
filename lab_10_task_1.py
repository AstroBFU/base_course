import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def diff_func(pup, x): 
    y, z = pup
    dydx = y**2 * z
    dzdx = z / x - y * z**2

    return dydx, dzdx

y0 = 1
z0 = -3
pup = y0, z0

sol = odeint(diff_func, pup, x)

plt.plot(x, sol[:, 1])
plt.savefig('task1')