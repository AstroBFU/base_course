a = int(input()) 
b = int(input())
c = int(input())

D = b**2 - 4*a*c
if D > 0:
    x1 = b * - 1 + (D** 0.5) / (2 * a) 
    x2 = b * - 1 - (D ** 0.5) / (2 *a)
    print(x1)
    print(x2)
elif D == 0:
    x1 = -b / 2 * a
    print(x1)
elif D < 0:
    print('Нет решения')

    
