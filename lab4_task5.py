import math as m
import numpy as np

def area(fgr):
    if fgr == "triangle":
        par_1 = float(input())
        par_2 = float(input())
        par_3 = float(input())
        per = (par_1 + par_2 + par_3)/2
        return (m.sqrt(per*(per-par_1)*(per-par_2)*(per-par_3)))
    elif fgr == "rectangle":
        par_1 = float(input())
        par_2 = float(input())
        return(par_1*par_2)
    else:
        return(2*m.pi*float(input()))

print("Enter, which figure's area you want to know(triangle, rectangle, circle)")
fgr = input()
print(area(fgr))
