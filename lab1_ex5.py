x, y = map(int, input().split())

if y == 0:
    print("Делитель ноль")
elif x % y == 0:
    print("Делится")
    print(x % y, x // y)
else:
    print("Не делится")

