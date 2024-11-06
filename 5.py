# Импортируем все нужное
from math import sqrt as koren
from numpy import pi, sin


# Делаем функции
def ploscshad(figure):
    if figure == 'triangle':
        return triangle(int(input("Введите 1-ю сторону: ")),int(input("Введите 2-ю сторону: ")),int(input("Введите 3-ю сторону: ")))
    if figure == 'circle':
        return circle(int(input('Введите радиус: ')))
    if figure == 'rectangle':
        return rectangle(int(input("Введите сторону: ")),int(input("Введите другую: ")),float(input("Введите угол: ")))

def triangle(a,b,c):
    p = (a + b + c) / 2
    return(koren(p*(p-a)*(p-b)*(p-c)))

def circle(r):
    return(pi*(r**2))

def rectangle(a,b,alph):
    return a * b * sin(alph)


#тестим
print(ploscshad(input("Введите фигуру: ")))