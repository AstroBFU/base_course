print("Решение квадратного уравнения вида ax^2+bx+c=0\nВведите:")


a = float(input('первый член a='))
b = float(input('второй член b='))
c = float(input('третий член c='))

if a == 0:
    x = float(-c / b)
    print('\nРезультат')
    print('Корень уравнения равен', round(x, 5))

else:
    x = 0
    x1 = 0
    x2 = 0
    D = float(b**2-4*a*c)
    if D < 0:
        print('\nРезультат')
        print('Нет рациональных корней')
    elif D == 0:
        x = float(-b / (2 * a))
        print('\nРезультат')
        print('Корень уравнения равен', round(x, 5))
    elif D > 0:
        x1 = float((-b+D**0.5) / (2 * a))
        x2 = float((-b-D ** 0.5) / (2 * a))
        print('\nРезультат')
        print('Первый корень уравнения равен', round(x1, 5))
        print('Второй корень уравнения равен', round(x2, 5))
