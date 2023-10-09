a = int(input('Введите год: '))
if ( a%4==0 and a%100 !=0) or a%400==0:
    print(f'{a} - високосный')
else:
    print(f'{a} - не високосный')
