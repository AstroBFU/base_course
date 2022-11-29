import numpy as np
s = np.arange(1, 10)
print(s)

def chek(t):
    b = 1
    for i in s:
        b *= i
    print(b)
chek(s)