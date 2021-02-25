import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.001)

def diff_func(a, t):
    x, y, z  = a
    dx = 3 * x - y + z
    dy = x + y + z
    dz = 4 * x - y + 4 * z
    
    return dx, dy, dz

x0 = -71
y0 = 1
z0 = -3

a0 = x0, y0, z0

b = 0.25
c = 5.0

sol = odeint(diff_func, a0, t)

plt.plot(t, sol[:, 1], 'b', label='x(t)')

plt.legend()
plt.show()