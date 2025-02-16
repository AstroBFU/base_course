import matplotlib.pyplot as plt 
import numpy as np



img = plt.imread('head.jpg')
fig, ax = plt.subplots()
ax.imshow(img)

t=np.linspace(np.pi/2, np.pi/4.8 ,200)
x=0 + 380*np.cos(t)
y=800-430*np.sin(t)
ax.plot(x,y,'-',lw=2,color='r')

t=np.linspace(np.pi, np.pi/2.6 ,200)
x=450+150*np.cos(t)
y=530 -40*np.sin(t)
ax.plot(x,y,'-',lw=2,color='r')

x = [510,570]
y = [490,360]
ax.plot(x,y,'-',lw=2,color='r')

t=np.linspace(np.pi+np.pi/6, np.pi+np.pi/2.3 ,200)
x=420-175*np.cos(t)
y=320-90*np.sin(t)
ax.plot(x,y,'-',lw=2,color='r')

t=np.linspace(np.pi+np.pi/2,np.pi/2  ,200)
x=480+70*np.cos(t)
y=380 -30*np.sin(t)
ax.plot(x,y,'-',lw=2,color='r')

t=np.linspace(np.pi*2, np.pi+np.pi/2 ,200)
x=480 + 75*np.cos(t)
y=270-80*np.sin(t)
ax.plot(x,y,'-',lw=2,color='r')

x = [550,700]
y = [270,330]
ax.plot(x,y,'-',lw=2,color='r')

x = [700,730]
y = [330,410]
ax.plot(x,y,'-',lw=2,color='r')

x = [730,650]
y = [410,680]
ax.plot(x,y,'-',lw=2,color='r')

x = [650,730]
y = [680,690]
ax.plot(x,y,'-',lw=2,color='r')

x = [730,750]
y = [690,850]
ax.plot(x,y,'-',lw=2,color='r')

t=np.linspace(np.pi, np.pi/4.8 ,200)
x=1000 +250*np.cos(t)
y=850-90*np.sin(t)
ax.plot(x,y,'-',lw=2,color='r')

x = [0,0]
y = [370,899]
ax.plot(x,y,'-',lw=2,color='r')

x = [0,1199]
y = [899,899]
ax.plot(x,y,'-',lw=2,color='r')

x = [1199,1199]
y = [800,899]
ax.plot(x,y,'-',lw=2,color='r')




plt.savefig('horse_2.png')



