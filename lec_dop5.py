a = int(input("Vvedite chislo: "))

def del_fi(num):
    delitely = []
    for i in range(1, num):
        if num % i == 0:
            delitely.append(i)
    return delitely

for i in range(1, a+1):
    ls = del_fi(i)
    if sum(ls) == i:
        print(i)
    