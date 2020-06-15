a = 10
b = 5
c = 1
if a > b :
    print (" ok" )

if a < ( b + c ):
    print ( " ok ")
    
else:
    print ( " net " )

a = 1
b = 2
c = 3
if a > b :
    print ( " a = kruto " )
elif a < c :
    print ( " a = pochti cruto ")
else:
    print ( " a = ne kruto")
    
a = 1
b = 2
c = 3
if a > b or a < c:
    print ( " a = kruto " )
    print ()
if b > a and b > c:
      print ( " b = kruto " )
      print ()
else:
    print ( "b = ne kruto " )
    
a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, ]
for x in a:
    print ( x )
    print ()

print ()    
print ("/////////////////////////////////////////////////////////////////")
print (
        )  
a = 0
while a < 200:
    print ( a )
    print ()  
    a += 5

for i in range ( 5 ):
    print ( i )
    print ()  

print("//////////////////////////")

for i in range ( 5 , 10 ):
    print ( i )
    print ()  