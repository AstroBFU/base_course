
x0=10 #глобальной области видимость
def move(t): #переменная локальной осласи видимости
  x=x0*t
  return x
print(move(3))
#print x

x='Good'
def my_func():
  x='Bad'
  print(x)
my_func()
print(x)