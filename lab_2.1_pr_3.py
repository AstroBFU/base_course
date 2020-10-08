a=input('Введите число: ')
#b=a//10 
#c=b//10
#d=c//10
#e=d//10
#f=a%10
#g=b%10
#h=c%10
#l=d%10
#print(f,g,h,l)

chisla = []
naoborot = []
for i in a:
    chisla.append(i)
    naoborot.append(chisla[::-1])
    
print(naoborot[len(a)-1])
print(chisla)