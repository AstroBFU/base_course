import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 126144000, 10)
n_0 = 1000
k = 0.08
	
def bacteria_function(n, t):
    dndt = -k * n
    
    return  dndt

solve_Bi = odeint(bacteria_function, n_0, t)

# Построение решения в виде графика функции
plt.plot(t, solve_Bi[:,0], label='Изменение инвестиций')
plt.xlabel('Время')
plt.ylabel('Функция подсчета инвестиций')
plt.title('График изменения инвестиций за 4 года')
plt.legend()

plt.show()
print("Oбъем инвестиций за 4 года составил", sum(solve_Bi[:,0]))