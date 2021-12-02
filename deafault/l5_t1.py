#Написать функцию, которая вычисляет среднее арифметическое элементов одномерного массива, переданного ей в качестве аргумента.
import numpy as np

lst = np.random.randint(0, 1000, 300)
b = np.array(lst)

def averadge_x(b):
  return np.mean(b)
print(averadge_x(b))
