n = int(input("Введите количество чисел в ряду Фибоначчи: "))
a = b = 1 
print(a,b, end=" ")
for i in range(2,n):
    a,b = b,a + b 
    print(b, end=" ")