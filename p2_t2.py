a, b, c = int(input()), int(input()), int(input())

if all([a + b > c, a + c > b, c + b > a]):
    print("Треугольник существует")
    if (any([a == b, b == c, c == a])):
        print("Треугольник равнобедренный")
    elif (a == b == c):
        print(print("Треугольник равносторонний"))
else:
    print("Треугольник не существует")