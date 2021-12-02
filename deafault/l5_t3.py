from l4_const import g

m, v, h  = float(input()), float(input()), float(input())
Ep = m * g * h
Ek = (m * v ** 2) / 2 
E = Ep + Ek

def energy_x(E):
  return E
print(energy_x(E))