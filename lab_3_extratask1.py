import numpy as np

print("Введите размеры массивов:")
n = int(input("Ведите количесво строк: "))
m = int(input("Ведите количесво столбцов: "))

mas_one = np.zeros((n, m))
mas_two = np.zeros((n, m))
mas_three = np.zeros((n, m))

for i in range(0, n):
    for j in range(0, m):
        mas_one[i, j] = int(input(f"Ведите значение ячейки {i+1}-ой строки {j+1}-ого столбца: "))

for i in range(0, n):
    for j in range(0, m):
        mas_two[i, j] = int(input(f"Ведите значение ячейки {i+1}-ой строки {j+1}-ого столбца: "))

for i in range(0, n):
    for j in range(0, m):
        if mas_one[i, j] >= mas_two[i, j]:
            mas_three[i, j] = mas_one[i, j]
        else:
            mas_three[i, j] = mas_two[i, j]

mas_three = np.array(mas_three)
print(mas_three)