import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
def ris(f):
  if f=='b':
    fig, ax = plt.subplots()
    babka, = plt.plot([], [], '-', color='r', label='Babochka')

    def babochka(time):
      alpha = np.arange(0,12*np.pi,0.1)
      x = np.sin(alpha)*(np.exp(np.cos(alpha))-2*np.cos(4*alpha)+np.sin(alpha/12)**5)
      y = np.cos(alpha)*(np.exp(np.cos(alpha))-2*np.cos(4*alpha)+np.sin(alpha/12)**5)
      return x, y

    plt.axis('equal')
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)

    def animate(i):
      babka.set_data(babochka(time=i))
    ani = FuncAnimation(fig,
    animate,
    frames=100,
    interval=30
    )
    ani.save('lab_7_task_3.gif')
  elif f=='h':
    fig, ax = plt.subplots()
    ser, = plt.plot([], [], '-', color='r', label='Hearth')

    def heart(time):
      alpha = (0,2*np.pi,0.1)
      x = 16*np.sin(alpha)**3
      y = 13*np.cos(alpha)-5*np.cos(2*alpha)-2*np.cos(3*alpha)-np.cos(4*alpha)
      return x, y

    plt.axis('equal')
    ax.set_xlim(-20,20)
    ax.set_ylim(-20,20)

    def animate(i):
      ser.set_data(heart(time=i))
    ani = FuncAnimation(fig,
    animate,
    frames=100,
    interval=30
    )
    ani.save('lab_7_task_3.gif')
print(ris(f='b'))
#---------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
def ris(f):
  if f=='b':
    fig, ax = plt.subplots()
    babka, = plt.plot([], [], '-', color='r', label='Babochka')
    xdata,ydata=[],[]
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)

    def update(i):
      t = 0.1*i
      x = np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5)
      y = np.cos(t)*(np.exp(np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5)

      xdata.append(x)
      ydata.append(y)
      babka.set_data(xdata,ydata)
      return babka,

    ani = FuncAnimation(fig,
    update,
    frames=100,
    interval=30
    )
    ani.save('lab_7_task_3.gif')
  elif f=='h':
    fig, ax = plt.subplots()
    ser, = plt.plot([], [], '-', color='r', label='Hearth')
    xdata,ydata=[],[]
    ax.set_xlim(-20,20)
    ax.set_ylim(-20,20)

    def update(i):
      t = 0.1*i
      x = 16*np.sin(t)**3
      y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)

      xdata.append(x)
      ydata.append(y)
      ser.set_data(xdata,ydata)
      return ser,
    ani = FuncAnimation(fig,
    update,
    frames=100,
    interval=30,
    )
    ani.save('lab_7_task_3.gif')
print(ris(f='b'))
