# # Решить квадратное уравнение с коэффициентами, вводимыми с клавиатуры. 
# # Учесть разные случаи: нет корней, один корень, два корня. Вывести корни на экран.

print( " vvedite coaficenti a , b , c " )

a = int (input ())
print ( " a =" , a )

b = int (input ())
print ( " b =" , b )

c = int (input ())
print ( " c =" , c )

print()
print( " Otvet:")

d = pow( b , 2 ) - 4 * a * c

if d < 0 :
    
    print ( " net destvitelnix cornei" )
    
else:
    
    if d == 0 :
        
        x =( - b + ( pow ( d , 0.5 ) ) ) / 2 * a
        print ( " x =" , x )
        
    else:
        
        x1 = ( - b + ( pow ( d , 0.5 ) ) ) / 2 * a
        print ( " x1 =" , x1 )
        print()
        
        x2 =( - b - ( pow ( d , 0.5 ) ) ) / 2 * a
        print ( " x2 =" , x2 )
    
