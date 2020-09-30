what=input('Какую операцию нужно выполнить(+,-,*,/): ')

a=float(input('Введите первое число: '))
b=float(input('Введите второе число: '))

if what == '+':
    c = a + b
    print('Результат: ' + str(c))
elif what == '-':
    c = a - b
    print('Результат: ' + str(c))
elif what == '*':
    c = a * b
    print('Результат: ' + str(c))
elif what == '/':
    c = a / b
    print('Результат: ' + str(c))
else:
    print('Выбрана неравильная операция')
input()
