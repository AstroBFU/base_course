def area(*arg, **kw):
    if kw['figure'] == 'square':
        S = arg[0] ** 2
    elif kw['figure'] == 'rectangle':
        S = arg[0] * arg[1]
    else:
        S = 1 / 2 * arg[0] * arg[1]
    print(S)
area(2, 5, 7, 8, figure='triangle')