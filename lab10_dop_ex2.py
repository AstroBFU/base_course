import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.01)

def diff_func(a, x):
     y, w = a
     dy = w
     dw = (dy ** 2 - (3 * y ** 2 / (w ** 0.5))) / y
     return dy, dw

y0 = 0.0001
w0 = 1
a0 = y0, w0


sol = odeint(diff_func, a0, x)

plt.plot(x, sol[:, 1], 'b', label='x(t)')

plt.legend()
plt.show()