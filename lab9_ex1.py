import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)
n_0 = 2
k = 2
	
def bacteria_function(n, t):
    dndt = k * n
    
    return  dndt

solve_Bi = odeint(bacteria_function, n_0, t)

# Построение решения в виде графика функции
plt.plot(t, solve_Bi[:,0], label='Размножение бактерий')
plt.xlabel('Время')
plt.ylabel('Функция размножения бактерий')
plt.title('Размножение бактерий делением на 2')
plt.legend()

plt.show()
