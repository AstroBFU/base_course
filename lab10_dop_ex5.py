import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-0.9999999, 1, 0.00001)
n = 4
def diff_func(a, x):
     y, w = a
     dy = w
     dw = ((3* x * dy) - n * (n+2) * y) / (1 - x ** 2)
     return dy, dw

y0 = 3
w0 = 0
a0 = y0, w0


sol = odeint(diff_func, a0, x)

for i in range(2,9):
    n = i
    lbl = 'n = ' + str(i) 
    sol = odeint(diff_func, a0, x)
    plt.plot(x, sol[:, 0], label = lbl)
    
    
plt.legend()
plt.show()