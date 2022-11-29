a = [1, 2, 3, 4, 5, 6]
print(a)

def chek(t):
    count = 0
    s = 0
    for i in a:
        s += i
        count += 1
    t = s / count
    print(t)

chek(a)
