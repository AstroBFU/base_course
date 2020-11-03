def srednee(a):
    c = 0
    for x in a:
        c = c + x
    z = c / len(a)
    print('Среднее арифметическое:',z)

srednee([2,4,7])

srednee([2,4,7,4,5,7,8])