a, b, c=map(float, input("Введите a b c через пробел: ").split())

if a<b+c and b<a+c and c<a+b:
    print("треутольник существует")
    if a == b ==c:
        print("равностороний")
    elif a == b or a==c or b ==c:
        print("Равнобедренный")
    else: print("Разностороний")
else: print("Несуществует")