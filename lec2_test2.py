n = float(input("1 chlen: "))
zn = float(input("Znamenatel: "))
cnt = int(input("Kolvo chlenov: "))

a = 0
list = []

for i in range(cnt):
    list.append(n * zn**a)
    a += 1

print(list)