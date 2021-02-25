import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.00001)

def diff_func(a, x):
     y, w = a
     dy = w
     dw = ((x * -w) + (4 * x ** 2 + 1/2) * y) / (x ** 2)
     return dy, dw

y0 = 3
w0 = 0
a0 = y0, w0


sol = odeint(diff_func, a0, x)

plt.plot(x, sol, 'b')

plt.legend()
plt.show()