# Массив это список с одиннаковым типом данных 
import numpy as np
a = [1, 2, 4]
b = np.array(a) # Создание массива из списка
print(type(a))
print(type(b)) 
print(b * b)
print(b / b)
print(b - b)
c = np.append(b, "Good")
print(c)
print(b[-1])