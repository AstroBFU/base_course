import random
N = int(input('Введи конечное число диапазона: '))
count = int(input('Сколько чисел будет в списке: '))
lista = [random.randint(0,100) for i in range(count)] 
print(lista)
def notfoundnumber(b):
    newnumber = random.randint(0, N)
    while True:
        if newnumber != b:
            return newnumber
newnumbercall = list(map(notfoundnumber, lista ))
print(newnumbercall[0])

