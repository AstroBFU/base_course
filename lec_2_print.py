number0 = int(input())
number1 = int(input())
number2 = int(input())

if number0 == number1 and number2:
  print("Треугольник равносторонний")
elif number0 != number1 != number2:
  print("Треугольник произвольный")
elif number1 or number2 == number0:
  print("Треугольник равнобедренный")
