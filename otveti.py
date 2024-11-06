#1
sr_arifm = lambda massiv: sum(massiv)/len(massiv)
#2
def peremnogalka(om):
    um = 1
    for i in om:
        um *= i
    return um
#3
g = 9.81
poln_meh_en = lambda m,v,h: (m * v ** 2) / 2 + m*g*h
#4
def koran(a = 0,b =1,n = 5):
    znach = []
    for i in range(a,b,((b-a)/n)):
        znach.append(i * abs(i))
    return znach

