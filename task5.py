a = int(input())
b = int(input())
if a % b == 0:
    print('первое число делится на второе')
    print(f'остаток {a%b}')
    print(f'a/b = {int(a/b)}')
else:
    print('первое число не делится на второе')
    print(f'остаток{a%b}')
    print( f'a/b = {int(a/b)}')
