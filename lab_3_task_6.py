import numpy as np
from random import randint

a = np.zeros((4, 3))
b = np.zeros((4, 3))
c = np.zeros((4, 3))

for i in range(4):
  for j in range(3):
   a[i, j] = randint(0, 100)
   b[i, j] = randint(0, 100)
  
print(a)
print(b)

for i in range(4):
  for j in range(3):
    if a[i, j] > b[i, j]:
      c[i,j] = a[i, j]
    else:
      c[i,j] = b[i, j]
    c[i,j] = max(a[i,j],b[i,j])
    
print(c)



    