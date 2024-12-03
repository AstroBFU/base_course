import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

n_0 = 10
m = 10
k = 10**(-6)
t = np.arange(0, 3/k, 100)

print("Закон увеличения бактерий: v = k * n,\nгде v - скорость, n - кол-во бактерий в моменте, k - коэфицент пропорциональности.")
print()

def bacterium_function(n, t):
    dndt = k * n
    return dndt

n_t = odeint(bacterium_function, n_0, t)

for i in range(len(n_t)):
    if round(n_t[i,0], 1) == m * n_0:
        print(f"Время, спустя которое бактерий станет в {m} раз больше", t[i])
        break

plt.plot(t, n_t[:,0], label="Размножение бактерий")
plt.xlabel("Время увеличения, секунды")
plt.ylabel("Функция увеличения")
plt.title("Закон увеличения")
plt.legend()

plt.savefig("lab_task1.png")