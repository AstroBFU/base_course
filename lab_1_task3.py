import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m = 3
a_0 = 10
v_0 = 0
gamma = 0.2
t = np.linspace(0, 7, 10000)

def boost_function(v, t):
    dvdt = a_0 - (gamma/m) * v**2
    return dvdt

v_t = odeint(boost_function, v_0, t)

plt.plot(t, v_t[:,0], label="скорость")
plt.xlabel("Время, секунды")
plt.ylabel("Функция скорости")
plt.title("Закон изменения скорости")
plt.legend()

plt.savefig("lab_task3.png")


