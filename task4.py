a = int(input('число: '))
b = [1]
for i in range(1, a+1):
    if i ==1:
        b.append(i)
    else:
        b.append(b[i-2]+b[i -1])
    print(b) 
