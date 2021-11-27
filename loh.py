print("Введите коэффицент для уравнения")
print("ax^2 +bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == 0:
  print("Не является квадратным уравнением")
else:
  disсr = b ** 2 - 4 * a * c
  print("disсr = ",disсr)
if disсr > 0:
  x1 =(-b + a ** 0,5) / (2 * a)
  x2 = (-b - a ** 0,5) / (2 * a)
elif disсr == 0:
   x = -b / (2 * a)
   print("x = disсr" , disсr)
else:
  print("Корней нет")
