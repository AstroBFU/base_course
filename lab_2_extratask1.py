a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4*a*c
if D > 0:
    print(f"x1 = {( -b + D**(1/2)) / (2 * a)}, x2 = {( -b - D**(1/2)) / (2 * a)}")
elif D == 0:
    print(f"x = {( -b ) / (2 * a)}")
elif D < 0:
    print("Корней нет. Ну то есть они есть, но это комплексные корни, из-за этого можно сказать, что их нет.")