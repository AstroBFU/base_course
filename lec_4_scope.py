#scope - Область видимости
x0 = 10 # Переменная в области видимости

def move(t):
    x = x0 * t # Локальная область видимости - тело функции. Вне функции - глобальная область видимости
    return x

print(move(3))
 # print(x)
a = 'good'

def my_fun():
    a = 'bad'
    print(a)

my_fun()
print(a)
