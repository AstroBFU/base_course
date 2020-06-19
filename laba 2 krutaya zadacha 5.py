#Вывести на экран, из каких простых множителей состоит введенное с клавиатуры натуральное число
print ( " vvedi chislo  " )
chislo = int (input ())
print ( " chislo =" , chislo )
k = 2
print ( " prosti mnoжetele:")
while chislo > 1:
    if chislo % k == 0:
       chislo = chislo / k
       print ( k )
    else:
        k = k + 1
        