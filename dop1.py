a = int(input())
b = int (input())
c = int(input())
D = b**2 - 4*a*c
if D < 0:
    print('уравнение не имеет решения')
elif D== 0:
    print('уравнение имеет один код', int(( -b + D**0.5) / (2*a)))
else:
    print('уравнение имеет два корня:')
    print(((-b+ D**0.5) / (2*a)))
    print(((-b -D**0.5) / (2*a)))