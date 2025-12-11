name = 'Borislov Osadchenko'
mass1 = [ord(symbol.upper()) for symbol in name]
mass2 = [ord(symbol.lower()) for symbol in name]
print(mass1)
print(mass2)
print(f'Сумма кодов списка: {sum(mass1 + mass2)}')