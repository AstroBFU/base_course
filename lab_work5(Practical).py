from math import e
from sympy import cos, sin

p = int(input("p = "))
d = int(input("d = "))
a = int(input("a (от 1 до 5) = "))

def ch(alpha):
    return (e**alpha + e**-alpha)/2

def sh(alpha):
    return (e**alpha - e**-alpha)/2

if (1 <= a <= 5):
    x = a*sh(p)/(ch(p) - cos(d))
    y = a*sin(p)/(ch(p) - cos(d))

    print(f"({x.evalf()}; {y.evalf()})")
else:
    print("Недопустимое значение a") 