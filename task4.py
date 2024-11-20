import numpy as np

def values(a, b, N):

    x = np.linspace(a, b, N)

    y = x ** 2

    return y


a = int(input('Введите первый промежуток'))  
b = int(input('Введите второй промежуток'))
N = int(input('Введите число точек'))
print(values(a, b, N))