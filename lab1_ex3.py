year = int(input())

if year % 4 != 0:
    print("Год не високосный")
elif year % 100 != 0:
    print("Год високосный")
elif year % 400 == 0:
    print("Год високосный")
else:
    print("Год не високосный")