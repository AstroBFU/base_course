import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 50, 0.1)
V_0 = 0
a_0 = 2
k = 0.5
m = 10
	
def speed_function(V, t):
    dVdt = a_0 - ((V**2) * k) / m
    
    return  dVdt

solve_Bi = odeint(speed_function, V_0, t)

# Построение решения в виде графика функции
plt.plot(t, solve_Bi[:,0], label='Изменение скорости')
plt.xlabel('Время')
plt.ylabel('Функция подсчета скорости')
plt.title('График изменения скорости')
plt.legend()

plt.show()
