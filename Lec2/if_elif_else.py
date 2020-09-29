import math
a = float(input())
if math.sqrt(a)%1==0:
    print('Ok')
elif math.sqrt(a)==0:
    print('Norm')
else: print("Not")