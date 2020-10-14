num = int(input())
for i in range(1, num):
    A = 0
    for k in range(1, i // 2 + 1):
        if i % k == 0:
            A += k
    if A == i:
        print(A)

    