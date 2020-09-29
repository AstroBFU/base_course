import math
G = 9.8
H = 100
time = float(input('Время в секундах: '))
l = ((G**2 * time**2) / (H - 1)) * (4 * math.pi - 5 * G**(3/2)) - 10

print(l)
