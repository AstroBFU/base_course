a = int(input("Введите сегодняшнее число: "))
b = int(input("Введите месяц в численном виде: "))
c = int(input("Введите год: "))

if b > 7 or (b == 7 and a >= 1):
    d = (c + 776) // 4 + 1
    k =(c + 776) % 4
    print(f"OL {d}.{k}")
else:
    d = (c + 775) // 4 + 1
    k =(c + 775) % 4
    print(f"OL {d}.{k}")