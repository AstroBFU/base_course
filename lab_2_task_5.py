a = int(input())
b = int(input())
if b == 0:
  print('делитель не должен быть равен 0')
elif a % b == 0:
  print('делится')
  print(a / b)
else:
  print('не делится')
  print(a // b)
  print(a % b)
