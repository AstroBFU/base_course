a = int(input())
b = int(input())

if b == 0:
    print("Делить на 0 нельзя")
elif a % b == 0:
    print(f"{a} делится на {b}")
    print("Частное = ", a / b)
else:
    print(f"{a} не делится на {b}")
    print("Остаток = ", a % b)
    print("Частное = ", a / b)