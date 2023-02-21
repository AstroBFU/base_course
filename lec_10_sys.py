''''import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину
t = np.arange(0, 10, 0.01)

# Определяем функцию для системы диф.уравнений
def diff_func(z, t): # z-изменяемая величина для системы
    theta, omega = z  # Указание изменяемых функций,через z

    #1 уравнение системы
    dtheta_dt = omega 

    #2 уравнение системы
    domega_d = - b * omega - c * np.sin(theta) 

    return dtheta_dt, domega_d

theta0 = np.pi - 0.1
omega0 = 0

# Начальное значение изменяемой величины системы
z0 = theta0, omega0

b = 0.25
c = 5.0

#решение
sol = odeint(diff_func, z0, t)

plt.plot(t, sol[:, 1], 'b', label='theta(t)')

plt.legend()
plt.savefig('sys.png')'''




import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(0, 10, 0.01)


def diff_func(z, t): 
    theta, omega = z  

    
    dtheta_dt = omega 

    
    domega_d = - b  * omega - c * np.sin(theta) 

    return dtheta_dt, domega_d

theta0 = np.pi - 0.1
omega0 = 0


z0 = theta0, omega0

b = 0.25
c = 5.0


sol = odeint(diff_func, z0, t)

plt.plot(sol[:, 1], sol[:, 0], 'g', label='theta(omega)')

plt.legend()
plt.savefig('sys_1.png')