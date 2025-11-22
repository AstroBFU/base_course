import numpy as np

a = range(0, 5, 1)
print(a)

# a = range(0, 10, 0.1)

b = np.arange(0, 5, 0.1) #хранит массив с данными. как рандж включает старт, не включает стоп
print(b)

d = np.linspace(0, 5, 10) #включает старт, включает стоп, хранит массивы
print(d)