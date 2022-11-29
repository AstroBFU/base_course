import numpy as np

'''s = np.arange(5, 25, 1)
def func(s):
    s1 = []
    for i in s:
        y = i**2
        np.append(i)
        np.append(y)
    print(s1)
func(s)

def chek(a, b):
    s = []
    for i in range(a, b, 1):
        y = i**2
        s.append(i)
        s.append(y)
    print(s)
chek(2, 5)'''

def y(a, b, N):
    x = np.linspace(a, b, N)
    y = x ** 2
    print(y)
y(-10, 10, 10)