import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

n_0 = 1000
k = 0.08
t = np.arange(0, 10, 0.01)
summa = 0

print("Закон изменения инвестиций: v = 0.08 * n,\nгде v - скорость, n - инвестируемые в данный момент времени средства, k - коэфицент пропорциональности.")
print()

def investment_function(n, t):
    dndt = -(k * n * t)
    return dndt

for i in range(0, 5):
    summa += n_0 * (1-k)**i

print("Объём инвестиций за 4 года:", round(summa))


n_t = odeint(investment_function, n_0, t)

plt.plot(t, n_t[:,0], label="Инвестиции")
plt.xlabel("Время уменьшения, дни")
plt.ylabel("Функция уменьшения")
plt.title("Закон уменьшения")
plt.legend()

plt.savefig("lab_task2.png")