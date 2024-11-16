import numpy as np
from lab_3_task1 import g

v0x = int(input("Введите скорость тела: "))
x0 = int(input("Введите начальные координаты по x: "))
y0 = int(input("Введите начальные координаты по y: "))

mas = np.array([["x", "y", "z"]])
t = np.arange(0, 6, 1)
x = x0 + v0x * t
y = y0 + v0x * t - g * t**2 / 2

for i in range(6):
    mas = np.append(mas, [[t[i], x[i], y[i]]], axis = 0)
print(mas)

# mas = [["x", "y", "z"]]
# for t in range(0, 6):
#     x = x0 + v0x * t
#     y = y0 + v0x * t - g * t**2 / 2
#     mas.append([t, x, y])

# mas = np.array(mas)
# print(mas)
