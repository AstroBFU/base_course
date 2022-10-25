a = int(input())
if a % 400 == 0:
  print('високосный')
elif a % 4 == 0:
  print('високосный')
elif a % 100 == 0:
  print('невисокосный')
else:
  print("невисокосный")