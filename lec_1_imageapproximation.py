import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

img = plt.imread('image.png')
fig, ax = plt.subplots()
ax.imshow(img)

t0 = np.linspace(np.pi-np.pi/8, np.pi/1.8, 100)
x0 = 400 + 240 * np.cos(t0)
y0 = 800 - 240 * np.sin(t0)
ax.plot(x0, y0, '-', lw=2, color = 'k')


t1 =  np.linspace(3 * np.pi/2, 2 * np.pi, 200)
x1 = 360 + 115 * np.cos(t1)
y1 = 348 - 215 * np.sin(t1)
ax.plot(x1, y1, '-', lw=2, color = 'k')

x = np.append(x0, x1)
y = np.append(y0, y1)


x2 = [475, 385]
y2 = [350, 370]
ax.plot(x2, y2, '-', lw=2, color = 'k')

x = np.append(x, x2)
y = np.append(y, y2)

t3 =  np.linspace(3 * np.pi/2, np.pi/2, 200)
x3 = 380 + 60 * np.cos(t3)
y3 = 320 - 50 * np.sin(t3)
ax.plot(x3, y3, '-', lw=2, color = 'k')

x = np.append(x, x3)
y = np.append(y, y3)

t4 =  np.linspace (3 * np.pi/2, 2 * np.pi,200)
x4 = 380 + 100 * np.cos(t4)
y4 = 160 - 109.9 * np.sin(t4)
ax.plot(x4, y4, '-', lw=2, color = 'k')

x = np.append(x, x4)
y = np.append(y, y4)

t5 =  np.linspace( np.pi,  3 * np.pi/2,200)
x5 = 610 + 130 * np.cos(t5)
y5= 155 - 45 * np.sin(t5)
ax.plot(x5, y5, '-', lw=2, color = 'k')

x = np.append(x, x5)
y = np.append(y, y5)

t6 =  np.linspace( 5 * np.pi/2, 2 * np.pi,200)
x6 = 610.05 + 105 * np.cos(t6)
y6 = 300 - 100 * np.sin(t6)
ax.plot(x6, y6, '-', lw=2, color = 'k')

x = np.append(x, x6)
y = np.append(y, y6)

x7 = [715, 690]
y7 = [300, 580]
ax.plot(x7, y7, '-', lw=2, color = 'k')

x = np.append(x, x7)
y = np.append(y, y7)


t8 =  np.linspace(np.pi/2, np.pi,  200)
x8 = 690.05 + 60 * np.cos(t8)
y8 = 705 - 125 * np.sin(t8)
ax.plot(x8, y8, '-', lw=2, color = 'k')

x = np.append(x, x8)
y = np.append(y, y8)


spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
figure_spline_part_manual = np.arange(0, 0.5, 0.01)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(spline_curve[0], spline_curve[1], 'b', lw=4)

plt.savefig('horse.png')