import numpy as np 

lst = np.random.randint(1, 30, 10)
b = np.array(lst)

def multiplication_x(b):
  return np.prod(b)

print(multiplication_x(b))