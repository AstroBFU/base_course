a, b = map(float, input("введите 2 числа через пробел: ").split())
if b == 0: print("На 0 делить нельзя")
elif a % b == 0: print(f"{a} делится на {b}\nОстаток = {a%b}\nЧастное = {a/b}")
elif a % b != 0: print(f"{a} не делится на {b}\nОстаток = {a%b}\nЧастное = {a/b}")