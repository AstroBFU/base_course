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
a = range (0, 10, 2)
print(a)
print(type(a))
print(a[3])
a = "Good"
for i in range(0, 10, 1):
    if i < len(a):
        print(a[i] + " - Bad")
    else:
        print(f'{i}' + " - Good")

