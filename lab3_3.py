import numpy as np
from lab3_base import g

v0x=10
v0y=3
x0=4
y0=0

t = np.linspace(0, 10, 100)

x=x0+v0x*t
y=y0+v0x*t-((g*t**2)/2)
print(t)
print(x)

traj = np.ndarray(shape=(100,3))

for i in range(100):
    traj[i,0]=t[i]
    traj[i,1]=x[i]
    




