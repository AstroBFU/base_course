# По длинам трех отрезков, вводимых с клавиатуры, определить возможность существования треугольника,
#  составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

print( " vvedite storoni treugolnika  a , b , c " )

a = int (input ())
print ( " a =" , a )

b = int (input ())
print ( " b =" , b )

c = int (input ())
print ( " c =" , c )

print()
print( " Otvet:")
print()

if  a + b > c  and  b + c > a  and  c + a > b :
    
    print ( " takoi treugolnik est ")
    print ()
    
    if  a == b == c :
    
        print ( " on ravnostoronni ")
    
    else:
        
        if  a == b  or  b == c  or  c ==a :
            
            print ( " on ravnobocii ")
            
else:
    print ( " takoi treugolnik ne treugolnic ")