a = int(input('Введите год: '))
if (a/400==0 or a/4==0) and a/100 != 0:
    print('a - високосный')
else:
    print('a - не високосный')
