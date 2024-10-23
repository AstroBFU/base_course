a = int(input())
f = 0
p = 1

for i in range(a):
    c = f + p
    print(c, end=" ")
    p = f
    f = c
print()