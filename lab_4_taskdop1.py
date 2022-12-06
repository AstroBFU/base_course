def power(a, n):
    P = 1
    for i in range(n):
        P = P * a
    print(P)
power(3, 100)