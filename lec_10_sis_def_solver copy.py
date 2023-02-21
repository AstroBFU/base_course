import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
t = np.arange(0, 10, 0.03)

def diff_func(z, t):
    theta, omega = z
    dtheta_dt = omega
    domega_d = - b * omega - c * np.sin(theta) 
    
    return dtheta_dt, domega_d

theta0 = np.pi - 0.1
omega0 = 0

z0 = theta0, omega0

b = 0.44
c = 6.0

sol = odeint(diff_func, z0, t)

plt.plot(t, sol[:, 1], 'b', label='theta(t)')

plt.legend()
plt.savefig('func')