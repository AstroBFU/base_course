x0 = 10 # глобальная область видимости
def move(t):
    x = x0 * t #
    return x   # локальная область видимости
print(move(10))
#print(x)
a = 'Good'
def my_func():
    a = 'Bad'
    print(a)
my_func()
print(a)