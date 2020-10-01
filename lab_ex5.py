a, b = map(int, input().split())
if b == 0:
    print('Ошибка')
elif a % b == 0:
    print('Число', a, 'делится на число', b)
    print(a % b)
    print(a, '/', b, '=', int(a / b))
else:
    print(a, '/', b, '=', a / b)