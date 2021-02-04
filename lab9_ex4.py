import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 1000, 0.1)
V_0 = 0
b = 100
k = 10
m = 200000
F = b
	
def Force_function(F, t):
    a = F / m
    v_t = a * t
    dFdt = b - k * v_t 
    
    return  dFdt

solve_Bi = odeint(Force_function, F, t)

# Построение решения в виде графика функции
plt.plot(t, solve_Bi[:,0], label='Изменение силы тяги')
plt.xlabel('Время')
plt.ylabel('Функция подсчета силы')
plt.title('График изменения силы тяги локомотива')
plt.legend()

plt.show()
