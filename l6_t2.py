#Создать функцию, строящую графики кривых второго порядка, заданных явно: Парабола Гипербола на вход, функции подаются: пределы изменения переменной (xa, xb), количество точек N, на которое разбиваются соответствующие пределы, необходимые параметры a, b, c, … и название графика.
import matplotlib.pyplot as plt
import numpy

Xa = int(input())
Xb = int(input())
N = int(input())
a = int(input())   
b = int(input())
c = int(input())

def parabola_and_giperbola(a, b, c, Xa, Xb, N,  title = 'Паробола и гипербола'):
  x = numpy.linspace(Xa, Xb, N)
  
  y = a * x ** 2 + b * x + c
  y1 = 1 / x

  plt.plot(x, y)
  plt.plot(x, y1)
  plt.show()

parabola_and_giperbola(a, b, c, Xa, Xb, N)