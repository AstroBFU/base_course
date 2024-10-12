a = int(input())
b = 0
c = 1
for i in range(a):
    f = b+c
    print(c, end= '')
    c = b
    b = f
    print()