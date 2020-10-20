import numpy as np
from lab_3_physic_constant import x0,V0x,y0,g
t=np.arange(0,5,0,1)
x=x0+V0x*t
y=y0+V0x*t-(g*t**2/2)
print(x)
print(y)
