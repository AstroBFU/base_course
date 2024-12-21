import matplotlib.pyplot as plt
import numpy as np

# Уравнение логарифмической спирали в полярных координатах: ρ = a * exp(b * θ)
a = 1  # Масштабный коэффициент
b = 0.2  # Коэффициент, определяющий крутизну спирали

theta = np.linspace(0, 10*np.pi, 500) # Угол от 0 до 10π
rho = a * np.exp(b * theta)

# Преобразование в декартовы координаты
x = rho * np.cos(theta)
y = rho * np.sin(theta)

# Построение графика
plt.figure(figsize=(8, 8))
plt.plot(x, y)
plt.title('Логарифмическая спираль')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box') # Для правильного отображения
plt.savefig('fig_task4log.png')