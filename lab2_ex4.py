n = int(input())
i = 2
primfac = []
while i * i <= n:
    while n % i == 0:
        primfac.append(i)
        n = n / i
    i = i + 1
if n > 1:
    primfac.append(n)
print(primfac)
