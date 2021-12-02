import math
from l4_const import k, e, hp, g

b = math.radians(30)
a = math.pi / 3
h = 100

v = math.sqrt((g * h * (math.tan(b) ** 2)) / (2 * (math.cos(a) ** 2) * (1 - math.tan(b) * math.tan(a))))
print(v)

T = 200
E = 300

N = (2 / math.sqrt(math.pi)) * (hp / (k * T) ** 1.5) * (e ** (-E / k * T)) * E ** (T / 2)
print(N)