a, b, c = map(int, input().split())
d = b**2 - 4*a*c
if d < 0:
    print("Нет корней")
elif d == 0:
    x = -b / (2*a)
    print(x)
elif d > 0:
    x1 = (-(d**(1/2)) - b) / (2*a)
    x2 = ((d**(1/2)) - b) / (2*a)
    print(x1, x2)