a = input()
b = len(a) - 1
a = int(a)
d = 0
i = 0

while b >= 0:
    c = a // (10 ** (b))
    d += c * (10 ** (i))
    a -= c * (10 ** (b))
    b -= 1
    i += 1

print(d)