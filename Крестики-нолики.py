import sys
x=[1,2,3,4,5,6,7,8,9,"x"]
print("Начальное поле")
print(x[0],x[1],x[2]) # Я знаю про print(x[0:3])
print(x[3],x[4],x[5]) # Я знаю про print(x[0:3])
print(x[6],x[7],x[8]) # Я знаю про print(x[0:3])
cher=str('d') # Просто объявляю.
m=0 # Потом за счет ее четности буду определять, чей ход
# Сам код
while not((x[0]==x[1]==x[2]==cher) or (x[3]==x[4]==x[5]==cher) or (x[6]==x[7]==x[8]==cher) or (x[0]==x[3]==x[6]==cher) or (x[1]==x[4]==x[7]==cher) or (x[2]==x[5]==x[8]==cher) or (x[0]==x[4]==x[8]==cher) or (x[6]==x[4]==x[2]==cher)):
    n=10 # Строка для входа в цикл снизу
    if m%2==0: # Собственно говоря, определяю чей ход
        cher=('x')
    else:
        cher=('y')
    while (x[n-1]=="o") or (x[n-1]=="x"): # А вспомнил
        print("\nВведите, в какую  клетку вы хотите поместить ", cher," ",end='')
        n=int(input())
        
    x[n-1]=cher
    print("\n\n\n\n\n\n\n\n\n\n\n") # А чеб нет))) Если можно как то очистить весь аутпут - лучше так сделаю, но на данный момент я такого не знаю.
    print("Номер хода: ", n)
    print(x[0],x[1],x[2]) # Я знаю про print(x[0:3])
    print(x[3],x[4],x[5]) # Я знаю про print(x[0:3])
    print(x[6],x[7],x[8]) # Я знаю про print(x[0:3])
    m=m+1 # Меняю ход при проверке на четность
print("Победитель - ", cher)
sys.exit()
