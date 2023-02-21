
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.01)


def diff_func(z ,x): 
    y, omega = z  

    dtheta_dt = omega 

    domega_d = omega * np.sin(y) - 3 * x * y -5

    return dtheta_dt, domega_d

theta0 = np.pi - 0.1
omega0 = 0

y0 = 0.01
omega = 0.05
z0 = y0, omega0

sol = odeint(diff_func, z0, x)

plt.plot(sol[:, 1], sol[:, 0], 'g', label='theta(omega)')
plt.legend()
plt.savefig('izmenenie.png')