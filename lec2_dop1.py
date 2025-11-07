a, b, c=map(float, input("Введите a b c через пробел: ").split())

d = b**2 - 4*a*c

if d > 0:
    print((-b + d**0.5)/(2*a))
    print((-b - d**0.5)/(2*a))
if d == 0:
    print((-b + d**0.5)/(2*a))
if d <0:
    print("нет корней")