import numpy as np

def mult_func(a):
    x = 1
    for i in a:
        x = x * i
    return x

b = [1, 2, 4, 6]
c = np.array(b)
print(mult_func(c))
