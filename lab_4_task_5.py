def area(figure, data):
    if figure == 'круг':
        print(data[0])
        res = 3.14*(data[0]**2)
    if figure == 'квадрат':
        a,b = data
        res = a*b
    if figure == 'треугольник':
        res = (a*b)/2
    return ' Площадь {} = {}'.format(figure, res)
    