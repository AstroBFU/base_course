print ( " vvedi colichestvo chisel fibonachi ")
a = int (input ())
print (a)
print ()
k = 0
b = 1
d = 0
while k < a:
    c = d
    b = b + c
    print ( b )
    d = b - c
    
    k = k + 1
