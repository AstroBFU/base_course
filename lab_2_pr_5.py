a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
if b==0:
    print('Нельзя делить на ноль!')
elif a%b==0:
    print(a/b)
else:
    print('Число не делится нацело!')
    print('Ответ: ',a/b)
    print('Целое число: ',a//b)
    print('Остаток: ', a%b)
