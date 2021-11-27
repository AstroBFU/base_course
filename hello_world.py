a = int(input("Напиши первое число:"))
b = int(input("А теперь напиши второе число:"))
if b == 0:
  print('На ноль делить нельзя')
else: 
  if a%b == 0:
    print("Число делится нацкло")
    print(a/b)
  else: 
    print('Число не делится без остатка')
    print(a%b)
    print(a//b)