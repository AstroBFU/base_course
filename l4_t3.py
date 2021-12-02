#в задаче 'Тело брошенное под углом' опущен главный элемент - угол под которым брошенно тело, а это меняет многое;)

from l4_const import g
from math import sin, cos
import numpy

print('Введите начальное положение в метрах:')
x0 = float(input())
print('Введите начальную высоту в метрах:')
y0 = float(input())
print('Введите начальную скорость, м/с:')
v0 = float(input())
if v0 == 0:
    print('И в школу не надо ходить, чтоб знать ответ:)')
    exit()
print('Под каким углом тело должно лететь?, в градусах:')
a = int(input())
if a == 0:
    print('Зачем ты хочешь решить задачу <<Тело брошенное под углом>> без угла?')
    exit()
print('Ответ:')

steps = 10 
answers = numpy.zeros((steps, 3))
c = 0

for t in numpy.linspace(0, 5, steps):
    x = abs(x0 + v0 * cos(a) * t)
    y = abs(y0 + v0 * sin(a) * t - ((g * t ** 2) / 2))
    answers[c, 0] = t
    answers[c, 1] = x
    answers[c, 2] = y
    c += 1
print(answers)

