a = float(input())
b = float(input())
c = float(input())

if a < b + c and b < a + c and c < a + b:
    print("Такой треугольник существует")
    if a != b != c:
        print("Этот треугольник разностороний")
    elif a == b == c:
        print("Этот треугольник равносторенний")
    elif a == b or b == c or a == c:
        print("Этот треугольник равнобедренный")
else:
    print("Такой треугольник не существует")