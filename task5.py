import numpy as np

def calculate_area(shape):
    if shape == 'круг':
        radius = int(input("Введите радиус круга: "))
        area = np.pi * radius ** 2
        return area
    elif shape == 'прямоугольник':
        length = int(input("Введите длину прямоугольника: "))
        width = int(input("Введите ширину прямоугольника: "))
        area = length * width
        return area
    elif shape == 'треугольник':
        base = int(input("Введите основание треугольника: "))
        height = int(input("Введите высоту треугольника: "))
        area = 0.5 * base * height
        return area
    else:
        return "Некорректная фигура!"


user_shape = input("Введите фигуру (круг, прямоугольник, треугольник): ")
area = calculate_area(user_shape)

print(f"Площадь {user_shape} составляет: {area}")