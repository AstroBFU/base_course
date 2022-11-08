import numpy as np

h = 100
g = 9.8
a = np.pi / 3
B = 30
c = h * g * np.tan(B)**2
b = 2 * np.cos(a)**2 * (1 - np.tan(B) * np.tan(a))
v = np.sqrt(c / b) 
print(v)

T = 200
E = 300
k = 1.380649 * 10**(-23)
e = 2.7
H = 6.62607015 * 10**(-27)
z = 2 / np.sqrt(np.pi)
y = H / ((k * T)**(3/2))
x = e**(-E/(k * T))
p = E**(T/2)
N = z * y * x * p
print(N)