import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 3, 0.00001)

def diff_func(a, t):
     y, w = a
     dy = w
     dw = (1 - w ** 2) ** 0.5
     return dy, dw

y0 = 1
w0 = 0
a0 = y0, w0


sol = odeint(diff_func, a0, t)

plt.plot(t, sol, 'b', label='x(t)')

plt.legend()
plt.show()