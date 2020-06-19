print ( " vvedi chislo  " )
chislo = int (input ())
print ( " chislo =" , chislo )
m = 0
print ( " perevernutoe chislo:")
while chislo>0:
    m = m*10 + chislo%10
    chislo = chislo//10
print(m)