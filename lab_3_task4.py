import numpy as np

N = int(input("Ведите значение N: "))
M = int(input("Ведите значение M: "))

trigonometry_array = np.zeros((N, M))


for i in range (0, N ):
    for k in range(0, M ):
        trigonometry_array[i, k] = np.sin(N * i + M * k + 1)
        if trigonometry_array[i, k] < 0:
            trigonometry_array[i, k] = 0
    
print(trigonometry_array)