number = int(input())
num = 0 

while number > 0:
  numebr1 = number % 10
  number = number // 10
  num = num * 10
  num = num + numebr1
print(num)