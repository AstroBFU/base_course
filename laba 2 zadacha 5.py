print ( " vvedi  dva chisela  ")
a = int (input ())
print (a)
b = int (input ())
print (b)

if b == 0:
    print ( " resultat deleniya = besconechnost " )
else:
    if a % b == 0:
        c = a / b
        print ( c , " ostatok = 0 ")
    else:
        c = a / b
        k = a % b
        print ( " resultat deleniya =" , c  , " ostatok =" , k )