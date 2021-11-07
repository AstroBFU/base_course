for i in range(1, int(input())):
    divider_sum = 0
    for j in range(1, i):
        if i % j == 0:
            divider_sum += j
    if i == divider_sum:
        print(i)
