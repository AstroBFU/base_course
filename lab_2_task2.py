a=int(input('Введите первый член прогрессии: '))
b=int(input('Введите знаменатель:'))
c=int(input('Введите количество членов:'))

for i in range(1, c+1):
    d =a*(b**(i-1))
    print(d)