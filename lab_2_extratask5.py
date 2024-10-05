a = int(input())
b = 0

while a > 0:
    for i in range(1, a):
        if a % i == 0:
            b += i
    if a == b:
        print(f"Число {a} - совершенное")
    b = 0
    a -= 1
