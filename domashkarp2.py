name = 'vladislavosadchenko'
myname ='_'.join(name)
myname1 = myname.upper()
myname2 = myname.lower()
ordmass1 = [ord(symbol) for symbol in myname1]
ordmass2 = [ord(symbol) for symbol in myname2]
print(ordmass1)
print(ordmass2)
print(f'Минимальное и максимальное для строки1 {min(ordmass1)}, {max(ordmass1)}')
print(f'Минимальное и максимальное для строки2 {min(ordmass2)}, {max(ordmass2)}')
