x1 = int(input())
x2 = int(input())
x3 = int(input())

D = (x2 ** 2) - (4 * x1 * x3)
if D < 0: 
  print("Нет решения")
else:
  if x2 > 0:
    xf1 = ((D ** 0.5) + (-(x2))) / 2
    xf2 = ((D ** 0.5) - (-(x2))) / 2
  elif x2 < 0:
    xf1 = ((D ** 0.5) + (x2)) / 2
    xf2 = ((D ** 0.5) - (x2)) / 2
print(f"Ответ х1 и х2 {xf1}, {xf2}")