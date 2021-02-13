import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()
move,=plt.plot([],[],'-',color='r',label='Frak')
point,=plt.plot([],[],'o',color='r')
circle,=plt.plot([],[],'-',color='r')
def ne_circle_move(R,i):
  t=np.linspace(0,4*np.pi,500)
  x1=R*(t[i]-np.sin(t[i]))
  y1=R*(1-np.cos(t[i]))
  return x1,y1
def circle_move(R,vx0,vy0,i):
  t=np.linspace(0,4*np.pi,500)
  y0=R
  alpha = np.arange(0, 2*np.pi, 0.1)
  x2=t[i]*R+R*np.cos(alpha)
  y2=y0+R*np.sin(alpha)
  return x2,y2
xdata,ydata=[],[]
edge=20
plt.axis('equal')
ax.set_xlim(-4*edge,6*edge)
ax.set_ylim(-edge,edge)

def update(i):
  xdata.append(ne_circle_move(R=4,i=i)[0])
  ydata.append(ne_circle_move(R=4,i=i)[1])
  move.set_data(xdata,ydata)
  point.set_data(ne_circle_move(R=4,i=i)[0],ne_circle_move(R=4,i=i)[1])
  circle.set_data(circle_move(R=4,vx0=1.6,vy0=0,i=i))
ani = FuncAnimation(fig,
update,
frames=500,
interval=30
)
ani.save('lab_7_task_1_cik_DOP.gif')
