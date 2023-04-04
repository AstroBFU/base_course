import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
def circle_plotter(radius=10):

    x1 = np.arange(-2*radius, 2*radius, 0.1)
    y1 = np.arange(-2*radius, 2*radius, 0.1)
 
    X1, Y1 = np.meshgrid(x, y)
 
    fxy = X1**2 + Y1**2 
 
    plt.contour(X1, Y1, fxy, levels=[radius**2])
    plt.axis('equal')
    plt.show()
    
circle_plotter()

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day = 24 * 60 * 60
years = 0.5
t = np.linspace(0, years*seconds_in_year, frames)
 
x10 = 149 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 30000

def move_func(s, t):
    (x2, v_x2, y2, v_y2) = s
 
    dxdt2 = v_x2
    dv_xdt2 = (
      	    - G * m1 * (x2 - x1)
            / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
            + k * q2 * q1 / m2 * (x2 - x1)
               / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
    	      )
    dydt2 = v_y2
    dv_ydt2 = (
      	    - G * m1 * (y2 - y1)
               / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
            + k * q2 * q1 / m2 * (y2 - y1)
               / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
              )

    return (dxdt2, dv_xdt2, dydt2, dv_ydt2)
 
x20 = - 149 * 10**9
v_x20 = 1
y20 = 0
v_y20 = - 30000
 
s0 = (x20, v_x20, y20, v_y20)
 
m1 = 6 * 10**(24)
q1 = - 1.1 * 10**(20)
 
m2 = 2.1 * 10**(5)
q2 = 2.1 * 10**(20)
 
G = 6.67 * 10**(-11)
k = 8.98755 * 10**9
 
sol = odeint(move_func, s0, t)
 
fig, ax = plt.subplots()
 
balls = []
balls_lines = []
	
for i in range(3):
    balls.append(plt.plot([], [], 'o', color='r'))
    balls_lines.append(plt.plot([], [], '-', color='r'))
 
def animate(i):
    for j in range(3):
        balls[j][0].set_data(sol[i, 4*j], sol[i, 4*j+2])
        balls_lines[j][0].set_data(sol[:i, 4*j], sol[:i, 4*j+2])
 
ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)
 
plt.axis('equal')
edge = 2 * x10
edge = 2 * x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
	
ani.save('n_body.gif')