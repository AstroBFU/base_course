import numpy as np

N = int(input("Ведите значение N: "))
M = int(input("Ведите значение M: "))

trigonometry_array = np.zeros((N, M))


for i in range (0, N):
    for j in range(0, M):
        trigonometry_array[i, j] = np.sin(N * i + M * j  + 1)
        if trigonometry_array[i, j] < 0:
            trigonometry_array[i, j] = 0

print("Какие столбцы вы хотите поменять?")
n = int(input("Выберите первый столбец: "))
m = int(input("Выберите второй столбец: "))
for i in range (0, N):
    trigonometry_array[i, n-1], trigonometry_array[i, m-1] = trigonometry_array[i, m-1], trigonometry_array[i, n-1]

print(trigonometry_array)