"""Типы данных
Неизменяемые данные (unmutable)
Числовые данные (int, float, complex)
Символьные строки (str)
Кортежи (tuple)
Списки (list)
Изменяемые данные (mutable)
Множества (set)
Словари (dict)"""

# Coplex numbers
x = 3
y = 4

z = complex(x, y)
print(z)

w = complex(y, x)
print(z + w)

# Strings
s = 'hello'
print(s[0])

# s[0] = 'H'

# Tuple кортедж - неизменяемый список
t = (1, 4, 9)
print(t)
print(t[0])

# t[0] = 3

# list список
l = [1, 4, 9]
l[0] = 3
print(l)

# Dict словари
d = {'key_1':4, 2:'red', 'str':'Hello'}
print(d['key_1'])
print(d[2])
print(d['str'])

d['str'] = 'Good'
print(d)

d['new_key']='Best'
print(d)