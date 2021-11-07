n = int(input())
while n > 1:
    i = 2
    f = 0
    while 1:
        if n%i == 0:
            n = n // i
            print(i, end=' ')
            f = 1
            break
        else:
            i += 1
    if f == 1:
        continue
print()