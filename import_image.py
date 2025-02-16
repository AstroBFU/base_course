import matplotlib.pyplot as plt 
import numpy as np


img = plt.imread('head.jpg')
fig, ax = plt.subplots()
ax.imshow(img, extent=[0,600,0,300])

t=np.linspace(np.pi-np.pi/8, np.pi/2,100)
x=400 +240*np.cos(t)
y= 800 -240*np.sin(t)
ax.plot(x,y,'-',lw=2,color='r')


plt.ylim(0,300)
plt.savefig('horse.png')