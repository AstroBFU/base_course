ka = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a + b <= c or a + c <= b or b + c <= a:
  print("Не существует") 
elif a == b and b == c:
  print("Равносторонний")
elif a == c or a == b:
  print("Равнобедренный")
elif a != b and b != c:
  print("Разносторонний")
else: 
  print("Существует")