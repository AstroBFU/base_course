from math import sqrt

a, b, c = int(input()), int(input()), int(input())
D = b ** 2 - (4 * a * c)

if D < 0:
    print("Нет корней")
elif D == 0:
    print("x = ", end="")
    print((-b) / (2 * a))
else:
    print("x1 = ", end="")
    print((-b) + sqrt(D) / (2 * a))
    print("x2 = ", end="")
    print((-b) - sqrt(D) / (2 * a))
