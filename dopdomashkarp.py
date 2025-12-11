import numpy as np, time
def matima(n):
    x = a*n**4 + b*n**3 + c**n*2 + d *n +e
    return x
a, b, c, d, e = 5, 2, 9, 7, 256
start = time.time()
count = list(np.arange(0, 10000)) 
logic = list(map(matima, count))
finish = time.time()
print(f'Время выполнения операции функцией map = {finish-start}')
start1 =time.time()
soso = [a*n**4 + b*n**3 + c**n*2 + d *n +e for n in range(0, 10000)]
finish1 = time.time()
print(f'Время выполнения операции списковым включением = {finish1-start1}')
start2 = time.time()
mass = []
for n in range(0, 10000):
    mass.append(a*n**4 + b*n**3 + c**n*2 + d *n +e)
finish2 = time.time()
print(f'Время выполнения операции циклом = {finish2-start2}')
