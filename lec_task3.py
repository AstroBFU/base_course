import numpy as np
import time
g=9.8
t=0

x0=0
y0=0
vox=6
voy=7

a=[]
while t in range(0,5):
    t+=1
    x=x0+vox*t
    y=y0+voy*t-((g*t**2)/2)
    b = [x,round(y,1),t]
    #print(b)
    a.append(b)
print(a)

v=5
alpha=np.pi/180*45
vx_0=v*np.cos(alpha)
vy_0=v*np.sin(alpha)

timer = time.time()
coords = []
for t in np.arange(0,5,0.00001):
    x=x0+vx_0*t
    y=y0+vy_0*t-((g*t**2)/2)
coords=np.array(coords)
print(coords)
print(time.time()-timer)

timer = time.time()
step=0.00001
t=np.arange(0,5,step)
x=x0+vx_0*t
y=y0+vy_0*t-((g*t**2)/2)
coords = np.zeros((len(t),3))
coords[:,0]=t
coords[:,1]=x
coords[:,2]=y
print(coords)
print(time.time()-timer)


timer = time.time()



