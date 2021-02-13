import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()
move1,=plt.plot([],[],'-',color='r',label='Frak')
move2,=plt.plot([],[],'-',color='g',label='Frak')
xdata,ydata=[],[]
t=np.arange(0,2*np.pi,0.1)
ax.set_xlim(0,2*np.pi)
ax.set_ylim(-1,1)
x1,y1=[],[]
x2,y2=[],[]
def update(frame,i=t):
  t1=1*i
  t2=0.8*i
  x1.append(t1)
  y1.append(np.sin(t1)
  x2.append(t2)
  y2.append(np.sin(t2))
  move1.set_data(x1,y1)
  move2.set_data(x2,y2)
ani = FuncAnimation(fig, 
update, 
frames=100,
interval=30
)
ani.save('lab_7_task_2_DOP.gif')
