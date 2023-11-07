
a = int(input('Введите первый коэфицент: '))
b = int(input('Введите второй коэфицент: '))
c = int(input('Введите третий коэфицент: '))

d = b**2 - 4*a*c 

if d < 0 :
   print('Нет корней')
elif d == 0:
    print(f'-b/2*{a}'  )
else: 
    q = (d**(1/2) - b)/2*a
    w = (-b - d**(1/2))/2*a
    print( f'x1 = {q}')
    print( f'x2 = {w}')
