for N in range(1,50):
    b=bin(N)[2:]
    if b.count('1')%2==0: 
        b=b+'0'
        b='10'+b[2:]
    else:
        b=b+'1'
        b='11'+b[2:]
    r=int(b,2)
    if r>50: print(N,b,r)