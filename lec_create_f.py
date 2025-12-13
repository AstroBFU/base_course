'''
def name_func(arg1, arg2, ..., argN): # Заголовок функции
    <интсрукция_1>
    <интсрукция_2>
    <интсрукция_3>     # Тело функции
        ....
    <интсрукция_n>
    return <значение> # Возврат результата
'''

def mult_func(a):
    x = 3 * a
    return x

def my_print(a):
    print(f'Это мой принт с блэкджеком и {a}')

tmp = mult_func(4)
print(tmp)

print(mult_func(10))

print(mult_func('Good'))

my_print('Hello')

my_print(mult_func('50'))