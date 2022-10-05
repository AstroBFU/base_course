number0 = int(input())
number1 = int(input())
number2 = int(input())

if number0 == number1 and number2:
  print("Треугольник равносторонний")
elif number0 == number1 or number2:
  print("Треугольник равнобедренный")
else:
  print("Треугольник произвольный")