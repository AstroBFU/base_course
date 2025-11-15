#Буловый тип

print(bool(2 > 3))

print(bool(2))

print(bool('Good'))

print(bool([1, 4, 5]))

print(bool(0))

print(bool(''))

print(bool([]))

print(bool([[]]))


#Конструкция if
''' - Документ строка / длинный комментарий
if <условие>: # Заголовок оператора
    <интсрукция_1>
    <интсрукция_2>
    <интсрукция_3>     # Тело оператора
        ....
    <интсрукция_n>
'''

if 1:
    print('hello 1')

a = 3
if a > 1:
    print(f'hello {a}')

b = 5
if b == 5:  # Операция сравнения
    print(f'hello {b}')


#Конструкция if – else
'''
if <условие>: # Заголовок оператора
    <интсрукция_1>
    <интсрукция_2>
    <интсрукция_3>     # Тело оператора
        ....
    <интсрукция_n>
else: # Оператор альтернативных условий
    <интсрукция_1>
    <интсрукция_2>
    <интсрукция_3>     # Тело оператора альтернативных условий
        ....
    <интсрукция_n>
'''

a = 3
if a > 4:
    print('hello 4')
else:
    print(f'hello {a}')


#Конструкция if – elif – else
'''
if <условие_1>: # Заголовок оператора
    <блок_интсрукций_1>
elif <условие_2>:
    <блок_интсрукций_2>
        ....              # Операторы нескольких альтернатив
elif <условие_n>:
    <блок_интсрукций_n>
else: # Оператор альтернативных условий
    <блок_интсрукций_else>
'''

a = 3
if a > 5:
    print('hello 5')
elif a < 2:
    print('hello 2')
else:
    print('Tupo hello')


#Логические операции
a = 3
b = 4
c = 5

if a > 4 and b == 2:  # and - операция логического "И"
    print('Good')
elif b > 3 or c == 5:  # or - операция логического "ИЛИ"
    print('Best')
else:
    print('Bad')


#Тренировка
a = 3
b = 5
c = -1

if a > 3 or c == 0:
    print('Good')
elif a <= 3 and b != 5:
    print('Best')
else:
    print('Bad')

if a >= 3 or b == 0:
    print('Good')
elif c == -1 or b > 4:
    print('Best')
else:
    print('Bad')

if ((a == 3 and c > 0) or (b == 5 and c < 0)) and c == -1:
    print('Good')
else:
    print('Bed')


#Операторы цикла for и while       
#Конструкция цикла for
'''
for <переменная цикла> in <значения переменной>: # Заголовок оператора
    <интсрукция_1>
    <интсрукция_2>
    <интсрукция_3>     # Тело оператора
        ....
    <интсрукция_n>
'''

for i in 1, 3, 4:
    print(i ** 2, end=' ')

print()

for i in 1, 3, 4:
    print(i ** 2, end='\n')

for i in 1, 3, 4:
    print(i, i ** 2, sep=' - ')

a = [1, 5, 7, 10]
for i in a:
    print(f'{i}**3 = {i ** 3}')


#Генератор последовательности range
'''
for <переменная цикла> in range(start, stop, step):
    <интсрукция_1>
    <интсрукция_2>
    <интсрукция_3>     # Тело оператора
        ....
    <интсрукция_n>

По умолчанию: start = 0, step = 1
Диапазон генерирования: [start, stop)
'''

a = range(0, 10, 2)
print(a)
print(type(a))
print(a[3])

a = 'Good'
for i in range(0, 10, 1):
    if i < len(a):
        print(a[i] + ' - Bad')
    else:
        print(f'{i}' + ' - Good')


#Конструкция цикла while
'''
while <переменная цикла> <условие>:
    <интсрукция_1>
    <интсрукция_2>
    <интсрукция_3>
        ....
    <интсрукция_n>

    <переменная цикла> += step
'''

i = 5
while i < 15:
    print('i: ', i)
    i += 2


#Команды break и continue
'''
if <условие прерывания>:
    break

if <условие пропуска>:
    continue
'''

for i in 'hello world':
    if i == 'o':
        break
    print(i)

for i in 'hello world':
    if i == 'o':
        continue
    print(i)
