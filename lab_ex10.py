num = int(input())
dividers = []
for i in range(1, num):
    if num % i == 0:
        dividers.append(i)
if sum(dividers) == num:
    print("Число совершенное")
else:
    print("Число не совершенное")
    