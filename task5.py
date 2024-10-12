a = int(input())
b = int(input())
if b == 0:
    print('no delit 0')
elif a % b == 0:
    print(f'{a}delit {b}')
    print('Chastnoe =', a / b)
else:
    print(f'{a}no delit {b}')
    print('ostatok = ', a%b)
    print('Chastnoe = ', a/b)