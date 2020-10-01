n = int(input())
f1 = 1
f2 = 2
print(f1, f2, end=" ")
for i in range(3, n + 1):
    print(f1 + f2, end=" ")
    b = f1
    f1 = f2
    f2 = b + f1
