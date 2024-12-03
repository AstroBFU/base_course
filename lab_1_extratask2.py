import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

S_0 = 1600
E_0 = 1360
k = 250 * 10**(-6)

t = np.arange(0, 24, 0.01)


def func_victoria_rega(S, t):
    if t >= 6 and t <= 18:
        dsdt = k * E_0*np.cos((12-t)*np.pi/12)*np.sqrt((S/10**4)**3/np.pi)*10**4
    else:
        dsdt = 0
    return dsdt

S_t = odeint(func_victoria_rega, S_0, t)

plt.plot(t, S_t, label="Площадь")
plt.xlabel("Время, часы")
plt.ylabel("Функция площади, см^2")
plt.title("Закон изменения площади")
plt.legend()

plt.savefig("lab_extratask2.png")
